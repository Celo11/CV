"""
REFERENCE SOLUTIONS for exercises.py  (try the exercises first!)

Running this file directly plays through the whole customer case study:
    python solutions.py

Pipeline (the bit Edge Impulse customers struggle with most):
    load -> inspect -> clean -> fix units -> fix timing -> filter
         -> window -> features -> honest train/test split -> export
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import signal

G = 9.80665
DATA = Path(__file__).resolve().parent.parent / "customer_data"
AXES = ["ax", "ay", "az"]
AXIS_NAMES = {"accx": "ax", "accy": "ay", "accz": "az", "ax": "ax", "ay": "ay", "az": "az"}


# ---------------------------------------------------------------- 1. LOAD
def load_recording(path):
    """Read any customer CSV into one standard shape: columns t_s, ax, ay, az.

    - time in SECONDS starting at 0 (customers use ms, us, or device uptime)
    - consistent axis names
    - exact duplicate rows removed, rows sorted by time, repeated timestamps removed
    """
    raw = pd.read_csv(path)
    cols = {c.lower(): c for c in raw.columns}
    if "time_us" in cols:
        t = raw[cols["time_us"]] / 1e6
    elif "timestamp" in cols:
        t = raw[cols["timestamp"]] / 1e3
    else:
        raise ValueError(f"No time column found in {path}: {list(raw.columns)}")

    df = pd.DataFrame({"t_s": t.astype(float)})
    for c in raw.columns:
        std = AXIS_NAMES.get(c.lower())
        if std:
            df[std] = raw[c].astype(float)

    df = df.drop_duplicates()                                  # re-sent lines
    df = df.sort_values("t_s")                                 # out-of-order lines
    df = df.drop_duplicates(subset="t_s", keep="first")        # same time, different values
    df["t_s"] = df["t_s"] - df["t_s"].iloc[0]                  # start at zero
    return df.reset_index(drop=True)


# ---------------------------------------------------------------- 2. INSPECT TIMING
def estimate_sample_rate(df):
    """Real sample rate from the timestamps. NEVER trust what the customer says."""
    return 1.0 / np.median(np.diff(df["t_s"].to_numpy()))


def find_gaps(df, fs, factor=1.5):
    """Places where the time step is much bigger than normal = lost samples."""
    t = df["t_s"].to_numpy()
    dt = np.diff(t)
    mask = dt > factor / fs
    return pd.DataFrame({
        "start_s": t[:-1][mask],
        "length_s": dt[mask],
        "missing_samples": np.round(dt[mask] * fs).astype(int) - 1,
    })


def split_at_gaps(df, fs, factor=1.5):
    """Cut a recording into continuous pieces instead of drawing fake data across gaps."""
    t = df["t_s"].to_numpy()
    breaks = np.where(np.diff(t) > factor / fs)[0] + 1
    pieces = np.split(np.arange(len(df)), breaks)
    out = []
    for idx in pieces:
        part = df.iloc[idx].copy()
        part["t_s"] -= part["t_s"].iloc[0]
        out.append(part.reset_index(drop=True))
    return out


# ---------------------------------------------------------------- 3. CLEAN VALUES
def detect_units(df):
    """Guess the units from the size of gravity (a still sensor reads 1 g)."""
    mag = np.sqrt((df[AXES] ** 2).sum(axis=1, min_count=3))
    m = np.nanmedian(mag)
    if 0.5 < m < 2:
        return "g"
    if 5 < m < 20:
        return "m/s2"
    if m > 1000:
        return "counts"
    return "unknown"


def clipping_fraction(df, limit=32767):
    """Fraction of rows where any axis hit the sensor's limit (saturated = data lost).

    Must be checked on RAW counts, before converting units.
    """
    vals = df[AXES].to_numpy()
    clipped = (vals >= limit) | (vals <= -limit - 1)
    return float(np.any(clipped, axis=1).mean())


def counts_to_ms2(df, counts_per_g=16384):
    """Raw sensor integers -> m/s^2 (16384 counts = 1 g on a 16-bit, +/-2 g sensor)."""
    out = df.copy()
    out[AXES] = out[AXES] / counts_per_g * G
    return out


def fill_missing(df, max_gap=3):
    """Fill short holes (a few empty cells) by straight-line interpolation.

    At most max_gap cells in a row are filled, and only inside the data.
    Big holes in time (lost samples) are handled separately by split_at_gaps.
    """
    out = df.copy()
    out[AXES] = out[AXES].interpolate(limit=max_gap, limit_area="inside")
    return out


def resample_uniform(df, fs):
    """Put samples on a perfectly regular time grid (removes timing jitter).

    Edge Impulse and every FFT assume equally spaced samples.
    NOTE: resampling UP cannot recover frequencies that were never captured.
    """
    t = df["t_s"].to_numpy()
    t_new = np.arange(0, t[-1], 1 / fs)
    out = pd.DataFrame({"t_s": t_new})
    for a in AXES:
        out[a] = np.interp(t_new, t, df[a].to_numpy())
    return out


# ---------------------------------------------------------------- 4. FILTER
def remove_gravity(x, fs, cutoff=10.0, order=4):
    """High-pass filter: removes gravity (0 Hz) and slow drift, keeps vibration.

    Uses a CAUSAL filter (sosfilt), like a microcontroller would.
    IMPORTANT: whatever filtering you do before training, the device must do
    exactly the same. Safest: let the Edge Impulse DSP block do the filtering,
    because the same block code is compiled into the device library.
    """
    sos = signal.butter(order, cutoff, btype="highpass", fs=fs, output="sos")
    x = x - x.mean(axis=0)            # remove the big DC offset first to avoid start-up ringing
    return signal.sosfilt(sos, x, axis=0)


# ---------------------------------------------------------------- 5. WINDOW
def make_windows(x, fs, window_s, stride_s):
    """Slice (N, channels) into overlapping windows -> (n_windows, W, channels).

    n_windows = floor((N - W) / S) + 1      (10 s, 2 s window, 0.2 s stride -> 41)
    """
    W = int(round(window_s * fs))
    S = int(round(stride_s * fs))
    if len(x) < W:
        return np.empty((0, W, x.shape[1]))
    n = (len(x) - W) // S + 1
    idx = np.arange(W)[None, :] + S * np.arange(n)[:, None]
    return x[idx]


# ---------------------------------------------------------------- 6. FEATURES
BANDS = [(0, 75), (75, 150), (150, 250), (250, 350), (350, 500)]


def extract_features(win, fs):
    """A mini version of Edge Impulse's Spectral Analysis block.

    win: (W, 3) one window, already gravity-free.
    2,000 raw numbers in -> ~12 meaningful numbers out.
    """
    feats = {}
    for i, a in enumerate(AXES):
        feats[f"rms_{a}"] = float(np.sqrt(np.mean(win[:, i] ** 2)))
        feats[f"p2p_{a}"] = float(np.ptp(win[:, i]))
    W = len(win)
    spec = np.abs(np.fft.rfft(win * np.hanning(W)[:, None], axis=0)) ** 2
    power = spec.sum(axis=1)                      # combine the 3 axes
    freqs = np.fft.rfftfreq(W, 1 / fs)
    feats["peak_hz"] = float(freqs[1:][np.argmax(power[1:])])
    for lo, hi in BANDS:
        sel = (freqs >= lo) & (freqs < hi)
        feats[f"band_{lo}_{hi}"] = float(np.sqrt(power[sel].sum()) / W)
    return feats


# ---------------------------------------------------------------- 7. EXPORT
def export_edge_impulse_csv(df, out_dir, label, name):
    """Write one cleaned recording in a CSV shape Edge Impulse can ingest.

    File name 'label.name.csv' -> the Edge Impulse CLI uploader reads the label
    from the part before the first dot. Upload whole recordings: Edge Impulse
    does the windowing itself (window size + stride are set in the impulse).
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = pd.DataFrame({
        "timestamp": np.round(df["t_s"].to_numpy() * 1000).astype(int),  # ms
        "accX": df["ax"].round(5), "accY": df["ay"].round(5), "accZ": df["az"].round(5),
    })
    path = out_dir / f"{label}.{name}.csv"
    out.to_csv(path, index=False)
    return path


# =================================================================== CASE STUDY
def clean_recording(path, fs_target=1000, convert_units=True, verbose=False):
    """Full cleaning pipeline -> list of clean continuous pieces (DataFrames)."""
    df = load_recording(path)
    fs = estimate_sample_rate(df)
    units = detect_units(df)
    clip = clipping_fraction(df) if units == "counts" else 0.0
    if units == "counts" and convert_units:
        df = counts_to_ms2(df)
    df = fill_missing(df)
    df = df.dropna()
    pieces = split_at_gaps(df, fs)
    pieces = [resample_uniform(p, fs_target) for p in pieces if len(p) > fs]
    if verbose:
        gaps = find_gaps(load_recording(path), fs)
        print(f"  {Path(path).name:32s} fs~{fs:6.0f} Hz | units={units:6s} | "
              f"clipped={clip:6.2%} | gaps={len(gaps)} | pieces={len(pieces)}")
    return pieces, fs


def windows_and_features(pieces, fs=1000, window_s=1.0, stride_s=0.2):
    rows = []
    for p in pieces:
        x = remove_gravity(p[AXES].to_numpy(), fs)
        x = x[int(0.2 * fs):]                       # drop filter start-up
        for w in make_windows(x, fs, window_s, stride_s):
            rows.append(extract_features(w, fs))
    return pd.DataFrame(rows)


def train_nearest_centroid(X, y):
    """The simplest possible classifier, so the lesson is about DATA, not models."""
    mu, sd = X.mean(axis=0), X.std(axis=0) + 1e-9
    Z = (X - mu) / sd
    labels = sorted(set(y))
    cents = np.stack([Z[y == lab].mean(axis=0) for lab in labels])
    return dict(mu=mu, sd=sd, labels=labels, cents=cents)


def predict(model, X):
    Z = (X - model["mu"]) / model["sd"]
    d = ((Z[:, None, :] - model["cents"][None, :, :]) ** 2).sum(axis=2)
    return np.array(model["labels"])[d.argmin(axis=1)]


def confusion(y_true, y_pred, labels=("normal", "fault")):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)   # avoid pandas index mis-alignment
    m = pd.crosstab(pd.Series(y_true, name="actual"), pd.Series(y_pred, name="predicted"))
    return m.reindex(index=list(labels), columns=list(labels), fill_value=0)


def build_table(meta, convert_units=True):
    frames = []
    for _, r in meta.iterrows():
        pieces, fs = clean_recording(DATA / r.file, convert_units=convert_units)
        f = windows_and_features(pieces)
        f["machine"], f["session"], f["label"] = r.machine, r.session, r.label
        f["true_fs"] = fs
        frames.append(f)
    return pd.concat(frames, ignore_index=True)


def main():
    meta = pd.read_csv(DATA / "recordings.csv")
    feat_cols = None

    print("\n=== STEP 1: Inspect every file (never trust the customer's notes) ===")
    for f in meta.file:
        clean_recording(DATA / f, verbose=True)

    tbl = build_table(meta)
    feat_cols = [c for c in tbl.columns if c.startswith(("rms", "p2p", "band", "peak"))]
    acc = lambda y, p: float((y == p).mean())

    print("\n=== STEP 2: The trap - random 80/20 split of overlapping windows, machine A only ===")
    a = tbl[tbl.machine == "A"].reset_index(drop=True)
    rng = np.random.default_rng(0)
    test = rng.random(len(a)) < 0.2
    m = train_nearest_centroid(a.loc[~test, feat_cols].to_numpy(), a.loc[~test, "label"].to_numpy())
    print(f"  Test accuracy (random windows, same machine): "
          f"{acc(a.loc[test, 'label'].to_numpy(), predict(m, a.loc[test, feat_cols].to_numpy())):.1%}")
    b = tbl[tbl.machine == "B"]
    pb = predict(m, b[feat_cols].to_numpy())
    print(f"  Same model on machine B:                       {acc(b.label.to_numpy(), pb):.1%}")
    print(confusion(b.label, pb).to_string().replace("\n", "\n    ").join(["    ", ""]))

    print("\n=== STEP 3: Honest split - train and test on DIFFERENT sessions, both machines ===")
    train_s, test_s = {"s1", "s3", "r1", "r2"}, {"s2", "s4", "r3", "r4"}
    tr, te = tbl[tbl.session.isin(train_s)], tbl[tbl.session.isin(test_s)]
    m2 = train_nearest_centroid(tr[feat_cols].to_numpy(), tr.label.to_numpy())
    p2 = predict(m2, te[feat_cols].to_numpy())
    print(f"  Test accuracy on unseen sessions (A + B): {acc(te.label.to_numpy(), p2):.1%}")
    print(confusion(te.label, p2).to_string().replace("\n", "\n    ").join(["    ", ""]))

    print("\n=== STEP 4: The units bug - machine B left in raw counts ===")
    tbl_bug = build_table(meta[meta.machine == "B"], convert_units=False)
    tbl_bug = tbl_bug[tbl_bug.session.isin(test_s)]
    p4 = predict(m2, tbl_bug[feat_cols].to_numpy())
    print(f"  Accuracy on machine B test sessions WITHOUT unit conversion: "
          f"{acc(tbl_bug.label.to_numpy(), p4):.1%}")
    print(confusion(tbl_bug.label, p4).to_string().replace("\n", "\n    ").join(["    ", ""]))

    print("\n=== STEP 5: Machine C - the customer said 1 kHz ===")
    c = tbl[tbl.machine == "C"]
    print(f"  Real sample rate from timestamps: {c.true_fs.iloc[0]:.0f} Hz "
          f"-> Nyquist limit {c.true_fs.iloc[0] / 2:.0f} Hz, but the fault is at 300 Hz")
    for lab in ["normal", "fault"]:
        s = c[c.label == lab]
        print(f"  {lab:6s}: energy 75-150 Hz = {s.band_75_150.median():.4f} | "
              f"energy 250-350 Hz = {s.band_250_350.median():.4f}")
    p5 = predict(m2, c[feat_cols].to_numpy())
    print(f"  Accuracy on machine C: {acc(c.label.to_numpy(), p5):.1%}")
    print(confusion(c.label, p5).to_string().replace("\n", "\n    ").join(["    ", ""]))
    print("  -> The 300 Hz fault folded down to 100 Hz. No cleaning can undo this: re-record at >= 1 kHz.")

    print("\n=== STEP 6: Export cleaned recordings for Edge Impulse ===")
    out_dir = DATA.parent / "edge_impulse_upload"
    n = 0
    for _, r in meta[meta.machine != "C"].iterrows():
        pieces, _ = clean_recording(DATA / r.file)
        for k, p in enumerate(pieces):
            export_edge_impulse_csv(p, out_dir, r.label, f"{r.machine}_{r.session}_{k}")
            n += 1
    print(f"  Wrote {n} files to {out_dir} (machine C excluded until re-recorded)")


if __name__ == "__main__":
    main()
