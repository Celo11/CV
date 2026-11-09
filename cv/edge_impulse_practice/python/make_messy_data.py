"""
Generates realistic, MESSY customer vibration recordings for practice.

Story: a customer wants to detect a bearing fault (~300 Hz) on a pump.
They send you recordings from three machines, recorded by three different
people, with three different set-ups. This is what real customer data looks like.

Run:  python make_messy_data.py
Out:  ../customer_data/*.csv  and  ../customer_data/recordings.csv (metadata)

DO NOT read this file before doing the exercises if you want the full
"detective" experience - the problems hidden in the data are listed at the bottom.
"""
from pathlib import Path

import numpy as np
import pandas as pd

G = 9.80665                  # m/s^2 per g
COUNTS_PER_G = 16384         # typical 16-bit accelerometer on the +/-2 g range
OUT = Path(__file__).resolve().parent.parent / "customer_data"
rng = np.random.default_rng(42)


# Every machine is a little different (motor speed, mounting, sensor position).
# This is exactly why a model tested on only one machine can fool you.
MACHINES = {
    #      shaft Hz, shaft amplitude, bearing-fault amplitude (m/s^2)
    "A": dict(shaft_hz=50, shaft_amp=0.5, bearing_amp=0.6),
    "B": dict(shaft_hz=60, shaft_amp=0.9, bearing_amp=0.35),  # sensor mounted further away
    "C": dict(shaft_hz=50, shaft_amp=0.5, bearing_amp=0.6),
}


def vibration(t, fault, shaft_hz, shaft_amp, bearing_amp, shock_at=None):
    """True physical acceleration in m/s^2 for 3 axes."""
    n = len(t)
    shaft = shaft_amp * np.sin(2 * np.pi * shaft_hz * t)   # motor turning (normal vibration)
    ax = shaft + 0.15 * rng.standard_normal(n)
    ay = 0.6 * shaft + 0.15 * rng.standard_normal(n)
    az = G + 0.3 * shaft + 0.15 * rng.standard_normal(n)  # gravity sits on Z
    if fault:
        # worn bearing: 300 Hz tone that "pulses" a little
        bearing = bearing_amp * (1 + 0.3 * np.sin(2 * np.pi * 3 * t)) * np.sin(2 * np.pi * 300 * t)
        ax += bearing
        ay += 0.5 * bearing
        az += 0.3 * bearing
    if shock_at is not None:
        # someone bumps the machine: a big decaying spike on Z
        k = np.clip(t - shock_at, 0, None)
        az += np.where(t >= shock_at, 15 * np.exp(-k * 40) * np.cos(2 * np.pi * 20 * k), 0)
    return ax, ay, az


def machine_a(name, fault, seconds=10.0, fs=1000):
    """Machine A: the 'good' set-up. 1 kHz, m/s^2, Edge Impulse style CSV."""
    t = np.arange(0, seconds, 1 / fs)
    ax, ay, az = vibration(t, fault, **MACHINES["A"])
    df = pd.DataFrame({
        "timestamp": np.round(t * 1000).astype(int),      # milliseconds
        "accX": ax.round(4), "accY": ay.round(4), "accZ": az.round(4),
    })
    df.to_csv(OUT / name, index=False)


def machine_b(name, fault, seconds=10.0, fs=1000):
    """Machine B: an engineer logged raw sensor output over serial. Messy."""
    period_us = 1e6 / fs
    n = int(seconds * fs)
    # timestamps in MICROseconds, with jitter (the logging loop is not perfectly regular)
    t_us = np.cumsum(np.full(n, period_us) + rng.normal(0, 25, n))
    t_us -= t_us[0]
    t_us += 1_734_000_000  # device uptime counter, does not start at zero
    # serial buffer overflow: ~60 ms of samples were lost in the middle
    keep = ~((t_us - t_us[0] > 4.20e6) & (t_us - t_us[0] < 4.26e6))
    t_us = t_us[keep]
    t = (t_us - t_us[0]) / 1e6
    ax, ay, az = vibration(t, fault, **MACHINES["B"], shock_at=7.0)
    # sensor gives raw integer counts, and saturates at the int16 limits
    to_counts = lambda a: np.clip(np.round(a / G * COUNTS_PER_G), -32768, 32767)
    df = pd.DataFrame({
        "time_us": t_us.round().astype(np.int64),
        "ax": to_counts(ax), "ay": to_counts(ay), "az": to_counts(az),
    })
    # a few corrupted readings (I2C glitch) come through as empty cells
    for col in ["ax", "ay", "az"]:
        idx = rng.choice(len(df), size=8, replace=False)
        df.loc[idx, col] = np.nan
    # logging script re-sent some lines -> exact duplicate rows
    dup = df.sample(6, random_state=1)
    df = pd.concat([df, dup])
    # and lines arrived slightly out of order
    df = df.sort_values("time_us").reset_index(drop=True)
    i = 5000
    df.iloc[[i, i + 1]] = df.iloc[[i + 1, i]].values
    df["ax"] = df["ax"].astype("Int64")
    df["ay"] = df["ay"].astype("Int64")
    df["az"] = df["az"].astype("Int64")
    df.to_csv(OUT / name, index=False)


def machine_c(name, fault, seconds=10.0, fs=400):
    """Machine C: customer *thinks* they log at 1 kHz. They actually log at 400 Hz."""
    t = np.arange(0, seconds, 1 / fs)
    ax, ay, az = vibration(t, fault, **MACHINES["C"])  # sampled directly at 400 Hz -> real aliasing
    df = pd.DataFrame({
        "timestamp": np.round(t * 1000, 1),  # ms, with decimals
        "accX": ax.round(4), "accY": ay.round(4), "accZ": az.round(4),
    })
    df.to_csv(OUT / name, index=False)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    machine_a("machineA_session1_normal.csv", fault=False)
    machine_a("machineA_session2_normal.csv", fault=False)
    machine_a("machineA_session3_fault.csv", fault=True)
    machine_a("machineA_session4_fault.csv", fault=True)
    machine_b("machineB_run1_normal.csv", fault=False)
    machine_b("machineB_run2_fault.csv", fault=True)
    machine_b("machineB_run3_normal.csv", fault=False)
    machine_b("machineB_run4_fault.csv", fault=True)
    machine_c("machineC_normal.csv", fault=False)
    machine_c("machineC_fault.csv", fault=True)

    meta = pd.DataFrame([
        ("machineA_session1_normal.csv", "A", "s1", "normal", "Customer: 1 kHz, m/s^2"),
        ("machineA_session2_normal.csv", "A", "s2", "normal", "Customer: 1 kHz, m/s^2"),
        ("machineA_session3_fault.csv", "A", "s3", "fault", "Customer: 1 kHz, m/s^2"),
        ("machineA_session4_fault.csv", "A", "s4", "fault", "Customer: 1 kHz, m/s^2"),
        ("machineB_run1_normal.csv", "B", "r1", "normal", "Customer: logged straight from sensor"),
        ("machineB_run2_fault.csv", "B", "r2", "fault", "Customer: logged straight from sensor"),
        ("machineB_run3_normal.csv", "B", "r3", "normal", "Customer: logged straight from sensor"),
        ("machineB_run4_fault.csv", "B", "r4", "fault", "Customer: logged straight from sensor"),
        ("machineC_normal.csv", "C", "c1", "normal", "Customer: 1 kHz, m/s^2"),
        ("machineC_fault.csv", "C", "c2", "fault", "Customer: 1 kHz, m/s^2"),
    ], columns=["file", "machine", "session", "label", "customer_notes"])
    meta.to_csv(OUT / "recordings.csv", index=False)
    print(f"Wrote {len(meta)} recordings + recordings.csv to {OUT}")


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# SPOILERS - the problems hidden in the data:
#  Machine B: different column names (time_us, ax, ay, az), microseconds,
#             timestamps do not start at 0, timing jitter, a ~60 ms gap,
#             raw counts instead of m/s^2, clipping during a bump at t=7 s,
#             empty cells, duplicate rows, two rows out of order.
#             Physically different too: 60 Hz motor, stronger shaft vibration,
#             weaker bearing signal (sensor mounted further away).
#  Machine C: really sampled at 400 Hz (customer says 1 kHz). The 300 Hz
#             bearing fault is above Nyquist (200 Hz) and aliases to 100 Hz.
#             No amount of cleaning can fix this -> it must be re-recorded.
# ---------------------------------------------------------------------------
