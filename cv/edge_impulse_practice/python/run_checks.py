"""
Checks your exercises.  Usage:
    python run_checks.py              -> checks exercises.py (your work)
    python run_checks.py solutions    -> checks solutions.py (should be all PASS)
"""
import importlib
import sys
import tempfile
import traceback
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "customer_data"
A = DATA / "machineA_session1_normal.csv"
B = DATA / "machineB_run1_normal.csv"
C = DATA / "machineC_fault.csv"


def check_load(m):
    df = m.load_recording(B)
    assert list(df.columns) == ["t_s", "ax", "ay", "az"], f"columns are {list(df.columns)}"
    assert df["t_s"].iloc[0] == 0, "t_s must start at 0"
    assert df["t_s"].is_monotonic_increasing, "rows are not sorted by time"
    assert not df["t_s"].duplicated().any(), "repeated timestamps left in"
    assert not df.duplicated().any(), "duplicate rows left in"
    assert list(df.index[:3]) == [0, 1, 2], "reset the index"
    a = m.load_recording(A)
    assert abs(a["t_s"].iloc[1] - 0.001) < 1e-9, "machine A timestamps are in ms -> 0.001 s steps"


def check_fs(m):
    fa = m.estimate_sample_rate(m.load_recording(A))
    fc = m.estimate_sample_rate(m.load_recording(C))
    assert abs(fa - 1000) < 10, f"machine A should be ~1000 Hz, got {fa:.1f}"
    assert abs(fc - 400) < 4, f"machine C should be ~400 Hz, got {fc:.1f}"


def check_gaps(m):
    df = m.load_recording(B)
    g = m.find_gaps(df, 1000)
    assert len(g) == 1, f"expected 1 gap in machine B, found {len(g)}"
    assert 0.05 < g["length_s"].iloc[0] < 0.07, f"gap length {g['length_s'].iloc[0]:.3f} s"
    assert 55 <= g["missing_samples"].iloc[0] <= 65
    assert len(m.find_gaps(m.load_recording(A), 1000)) == 0, "machine A has no gaps"


def check_split(m):
    parts = m.split_at_gaps(m.load_recording(B), 1000)
    assert isinstance(parts, list) and len(parts) == 2, "machine B should split into 2 pieces"
    for p in parts:
        assert p["t_s"].iloc[0] == 0, "each piece must restart at t_s = 0"
        assert p.index[0] == 0, "reset each piece's index"


def check_units(m):
    assert m.detect_units(m.load_recording(A)) == "m/s2"
    assert m.detect_units(m.load_recording(B)) == "counts"
    g = m.load_recording(A)
    g[["ax", "ay", "az"]] /= 9.80665
    assert m.detect_units(g) == "g"


def check_clipping(m):
    fb = m.clipping_fraction(m.load_recording(B))
    assert 0 < fb < 0.01, f"machine B clips briefly during the bump, got {fb:.4f}"
    assert m.clipping_fraction(pd.DataFrame({"ax": [0, 32767], "ay": [0, 0], "az": [-32768, 0]})) == 1.0


def check_convert(m):
    raw = m.load_recording(B)
    out = m.counts_to_ms2(raw)
    assert abs(np.nanmedian(out["az"]) - 9.81) < 0.2, "gravity on Z should be ~9.81 m/s^2"
    assert np.nanmedian(raw["az"]) > 10000, "do not modify the input DataFrame (return a copy)"


def check_fill(m):
    df = pd.DataFrame({"t_s": [0, 1, 2, 3, 4], "ax": [np.nan, 1.0, np.nan, 3.0, 4.0],
                       "ay": [0.0] * 5, "az": [0.0] * 5})
    out = m.fill_missing(df)
    assert out["ax"].iloc[2] == 2.0, "a hole between 1 and 3 should become 2"
    assert np.isnan(out["ax"].iloc[0]), "do not invent data before the first real sample"
    assert np.isnan(df["ax"].iloc[2]), "return a copy"
    b = m.fill_missing(m.counts_to_ms2(m.load_recording(B)))
    assert b[["ax", "ay", "az"]].isna().sum().sum() == 0, "machine B's single empty cells should be filled"


def check_resample(m):
    rng = np.random.default_rng(0)
    t = np.cumsum(0.001 + rng.normal(0, 0.00003, 2000))
    t -= t[0]
    df = pd.DataFrame({"t_s": t, "ax": np.sin(2 * np.pi * 5 * t), "ay": 0.0, "az": 1.0})
    out = m.resample_uniform(df, 1000)
    assert list(out.columns) == ["t_s", "ax", "ay", "az"]
    assert np.allclose(np.diff(out["t_s"]), 0.001), "time steps must be exactly 1/fs"
    assert np.allclose(out["ax"], np.sin(2 * np.pi * 5 * out["t_s"]), atol=1e-3)


def check_filter(m):
    a = m.load_recording(A)
    x = a[["ax", "ay", "az"]].to_numpy()
    y = m.remove_gravity(x, 1000)
    assert y.shape == x.shape
    assert abs(y[500:, 2].mean()) < 0.05, "gravity (~9.81 on Z) should be removed"
    assert y[500:, 0].std() > 0.3, "the 50 Hz vibration should survive a 10 Hz high-pass"


def check_windows(m):
    x = np.arange(10000 * 3, dtype=float).reshape(10000, 3)
    w = m.make_windows(x, 1000, 2.0, 0.2)
    assert w.shape == (41, 2000, 3), f"expected (41, 2000, 3), got {w.shape}"
    assert np.array_equal(w[1][0], x[200]), "window 2 should start 0.2 s (200 samples) later"
    assert m.make_windows(x[:500], 1000, 2.0, 0.2).shape[0] == 0, "too short -> 0 windows"


def check_features(m):
    import solutions as ref
    fs, n = 1000, 1000
    t = np.arange(n) / fs
    win = np.stack([np.sin(2 * np.pi * 300 * t), 0.5 * np.sin(2 * np.pi * 50 * t), 0.1 * t], axis=1)
    f, r = m.extract_features(win, fs), ref.extract_features(win, fs)
    missing = set(r) - set(f)
    assert not missing, f"missing keys: {sorted(missing)}"
    assert abs(f["peak_hz"] - 300) < 2, f"peak should be 300 Hz, got {f['peak_hz']}"
    for k in r:
        assert np.isclose(f[k], r[k], rtol=1e-3, atol=1e-6), f"{k}: yours {f[k]:.5f} vs {r[k]:.5f}"


def check_export(m):
    df = pd.DataFrame({"t_s": [0, 0.001, 0.002], "ax": [1.0, 2, 3], "ay": [0.0] * 3, "az": [9.8] * 3})
    with tempfile.TemporaryDirectory() as d:
        p = Path(m.export_edge_impulse_csv(df, d, "fault", "A_s3_0"))
        assert p.name == "fault.A_s3_0.csv", f"file name is {p.name}"
        back = pd.read_csv(p)
        assert list(back.columns) == ["timestamp", "accX", "accY", "accZ"]
        assert back["timestamp"].tolist() == [0, 1, 2], "timestamp must be integer milliseconds"


CHECKS = [
    ("1  load_recording", check_load), ("2a estimate_sample_rate", check_fs),
    ("2b find_gaps", check_gaps), ("2c split_at_gaps", check_split),
    ("3a detect_units", check_units), ("3b clipping_fraction", check_clipping),
    ("3c counts_to_ms2", check_convert), ("3d fill_missing", check_fill),
    ("3e resample_uniform", check_resample), ("4  remove_gravity", check_filter),
    ("5  make_windows", check_windows), ("6  extract_features", check_features),
    ("7  export_edge_impulse_csv", check_export),
]


def main():
    if not B.exists():
        sys.exit("No customer data yet - run:  python make_messy_data.py")
    name = sys.argv[1] if len(sys.argv) > 1 else "exercises"
    m = importlib.import_module(name)
    passed = 0
    for label, fn in CHECKS:
        try:
            fn(m)
            print(f"  PASS  {label}")
            passed += 1
        except NotImplementedError:
            print(f"  TODO  {label}")
        except Exception as e:  # noqa: BLE001
            msg = str(e) or traceback.format_exc(limit=1).strip().splitlines()[-1]
            print(f"  FAIL  {label}: {msg}")
    print(f"\n{passed}/{len(CHECKS)} passed")
    if passed == len(CHECKS) and name == "exercises":
        print("All done! Now run:  python solutions.py   to see the full customer case study.")


if __name__ == "__main__":
    main()
