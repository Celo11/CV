"""
DATA CLEANING + FEATURE EXTRACTION EXERCISES  (pandas / numpy / scipy)

The story: a customer wants to detect a ~300 Hz bearing fault. They sent you
recordings from 3 machines in ../customer_data/. Your job is to turn their
messy CSVs into clean data that Edge Impulse (and a model) can trust.

How to work:
  1. python make_messy_data.py          (once, creates the customer data)
  2. Fill in one function below (replace `raise NotImplementedError`)
  3. python run_checks.py               (shows PASS / FAIL / TODO for each)
  4. Stuck for >15 min? Peek at solutions.py, then close it and write it yourself.
  5. When everything passes: python solutions.py  (plays the full case study)

Useful pandas / numpy you will need (look each one up as you go):
  pd.read_csv, df.columns, df.rename, df.drop_duplicates, df.sort_values,
  df.interpolate, df.dropna, df.isna().sum(), df.describe(), df.iloc / df.loc
  np.diff, np.median, np.sqrt, np.interp, np.where, np.split, np.arange,
  np.fft.rfft, np.fft.rfftfreq, np.hanning
  scipy.signal.butter, scipy.signal.sosfilt

Before writing code, LOOK at the data like an engineer:
  df = pd.read_csv("../customer_data/machineB_run1_normal.csv")
  print(df.head()); print(df.describe()); print(df.isna().sum())
  print(df["time_us"].diff().describe())
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import signal

G = 9.80665
DATA = Path(__file__).resolve().parent.parent / "customer_data"
AXES = ["ax", "ay", "az"]


# ---------------------------------------------------------------- 1. LOAD
def load_recording(path):
    """Read any customer CSV into one standard DataFrame with columns: t_s, ax, ay, az

    Requirements:
      - time column may be 'timestamp' (milliseconds) or 'time_us' (microseconds)
        -> convert to seconds in a column called t_s
      - axis columns may be accX/accY/accZ or ax/ay/az -> rename to ax, ay, az
      - remove exact duplicate rows
      - sort by time
      - if two rows have the same timestamp, keep the first
      - t_s must start at 0.0
      - return with a clean 0..N-1 index (reset_index(drop=True))
    """
    raise NotImplementedError


# ---------------------------------------------------------------- 2. INSPECT TIMING
def estimate_sample_rate(df):
    """Return the real sample rate in Hz, worked out from the t_s column.

    Hint: the typical time step between samples is the MEDIAN of np.diff(t).
    (Median, not mean: one big gap would drag the mean.)
    """
    raise NotImplementedError


def find_gaps(df, fs, factor=1.5):
    """Find lost samples. Return a DataFrame with columns:
      start_s          time just before the gap
      length_s         duration of the gap
      missing_samples  round(length_s * fs) - 1

    A gap is any time step bigger than factor / fs.
    """
    raise NotImplementedError


def split_at_gaps(df, fs, factor=1.5):
    """Return a LIST of DataFrames: the recording cut at every gap.

    Each piece should have t_s restarting at 0 and a clean index.
    Why: interpolating across a 60 ms hole would invent fake data.
    Hint: np.where(np.diff(t) > factor / fs)[0] + 1 gives the cut positions.
    """
    raise NotImplementedError


# ---------------------------------------------------------------- 3. CLEAN VALUES
def detect_units(df):
    """Return 'g', 'm/s2', 'counts' or 'unknown'.

    Trick: a sensor sitting on a machine always feels gravity (1 g).
    Work out the magnitude sqrt(ax^2 + ay^2 + az^2) for every row and take the
    median (ignore NaNs):  ~1 -> 'g',  ~9.8 -> 'm/s2',  ~16000 -> 'counts'.
    """
    raise NotImplementedError


def clipping_fraction(df, limit=32767):
    """Fraction (0..1) of rows where ANY axis is >= limit or <= -(limit + 1).

    These samples are saturated: the real value was bigger than the sensor could
    report. Check this on raw counts, before converting units.
    """
    raise NotImplementedError


def counts_to_ms2(df, counts_per_g=16384):
    """Convert the three axis columns from raw counts to m/s^2. Return a COPY.

    m/s^2 = counts / counts_per_g * G
    """
    raise NotImplementedError


def fill_missing(df, max_gap=3):
    """Fill single empty cells (and short runs of them) by linear interpolation.

    Fill at most max_gap empty cells in a row, and only holes that are INSIDE the
    data (never invent values before the first or after the last real sample).
    Return a COPY.
    Hint: DataFrame.interpolate has 'limit' and 'limit_area' arguments.
    """
    raise NotImplementedError


def resample_uniform(df, fs):
    """Return a new DataFrame on a perfectly regular time grid.

    t_new = np.arange(0, last_time, 1 / fs); then np.interp each axis onto t_new.
    Columns: t_s, ax, ay, az.
    """
    raise NotImplementedError


# ---------------------------------------------------------------- 4. FILTER
def remove_gravity(x, fs, cutoff=10.0, order=4):
    """High-pass filter a (N, 3) numpy array. Return a (N, 3) array.

    Steps:
      1. subtract the mean of each column (removes the big gravity offset)
      2. sos = signal.butter(order, cutoff, btype="highpass", fs=fs, output="sos")
      3. return signal.sosfilt(sos, x, axis=0)
    Think: if you filter here before training, what must the device do?
    """
    raise NotImplementedError


# ---------------------------------------------------------------- 5. WINDOW
def make_windows(x, fs, window_s, stride_s):
    """Slice a (N, C) array into overlapping windows -> (n_windows, W, C).

    W = samples per window, S = samples per stride
    n_windows = (N - W) // S + 1   (0 windows if N < W)
    Check yourself: 10 s at 1 kHz, 2 s window, 0.2 s stride -> 41 windows.
    Bonus: do it without a Python loop (build an index array with broadcasting).
    """
    raise NotImplementedError


# ---------------------------------------------------------------- 6. FEATURES
BANDS = [(0, 75), (75, 150), (150, 250), (250, 350), (350, 500)]


def extract_features(win, fs):
    """Turn one (W, 3) window into a dict of features (mini Spectral Analysis block).

    Required keys:
      rms_ax, rms_ay, rms_az     sqrt(mean(x^2)) of each axis
      p2p_ax, p2p_ay, p2p_az     max - min of each axis
      peak_hz                    frequency with the most power (ignore the 0 Hz bin)
      band_LO_HI for each band   sqrt(sum of power in [LO, HI) Hz) / W

    Spectrum: power = |rfft(win * hanning(W)[:, None], axis=0)|^2, summed over axes.
    Frequencies: np.fft.rfftfreq(W, 1 / fs)
    """
    raise NotImplementedError


# ---------------------------------------------------------------- 7. EXPORT
def export_edge_impulse_csv(df, out_dir, label, name):
    """Write a cleaned recording as  out_dir / f"{label}.{name}.csv"  and return the path.

    Columns: timestamp (integer milliseconds), accX, accY, accZ
    (Edge Impulse's uploader takes the label from the text before the first dot.)
    """
    raise NotImplementedError
