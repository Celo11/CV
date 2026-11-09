# Edge Impulse practice pack: data cleaning, feature extraction, and microcontroller C++

**Why this exists:** in the Qualcomm / Edge Impulse interview (9 Nov 2026), Zin said the part customers struggle with most is **data and feature extraction**. If there is a next round, expect questions or a hands-on task about cleaning sensor data and getting it into a device correctly.

Everything here runs on this laptop. No board and no Edge Impulse account needed.

```
edge_impulse_practice/
├── python/
│   ├── make_messy_data.py   creates realistic, messy customer recordings (run once)
│   ├── exercises.py         13 functions for you to write  ← YOUR WORK
│   ├── run_checks.py        PASS / FAIL / TODO for each exercise
│   └── solutions.py         reference answers + full customer case study
├── cpp/
│   ├── 01_sensor_to_classifier.cpp   sensor → units → ring buffer → signal_t → classifier
│   ├── 02_int8_quantization.cpp      what int8 really does, with numbers
│   ├── 03_exercises.cpp              6 microcontroller-style functions  ← YOUR WORK
│   ├── 03_solutions.cpp              reference answers
│   └── 03_tests.inc                  shared tests (don't edit)
├── customer_data/            generated customer recordings (3 machines)
└── edge_impulse_upload/      cleaned output from solutions.py, ready for Edge Impulse
```

---

## How to run

Open a terminal in `edge_impulse_practice` first.

**Python**
```powershell
cd python
..\.venv\Scripts\python.exe make_messy_data.py     # once
..\.venv\Scripts\python.exe run_checks.py          # after each exercise
..\.venv\Scripts\python.exe solutions.py           # the full case study (try at the end)
```

**C++** (the compiler is installed in the venv as the `ziglang` package)
```powershell
cd cpp
..\.venv\Scripts\python.exe -m ziglang c++ -std=c++11 -O2 03_exercises.cpp -o 03.exe
.\03.exe
```
Swap in `01_sensor_to_classifier.cpp` or `02_int8_quantization.cpp` the same way. You can also paste any file into https://godbolt.org or onlinegdb.com. For `03_exercises.cpp`, paste the contents of `03_tests.inc` at the bottom in place of the `#include` line.

---

## The customer story (what the data contains)

A customer wants to detect a **~300 Hz bearing fault** on pumps. They send recordings from three machines. They say everything is "1 kHz, m/s²". Your job is to find out what's actually in the files.

| Machine | What the customer says | Your job: find out |
|---|---|---|
| A | 1 kHz, m/s² | Is it really clean? |
| B | "Logged straight from the sensor" | Format, units, timing, missing data… (lots hidden) |
| C | 1 kHz, m/s² | Check the timestamps yourself |

Don't read the bottom of `make_messy_data.py` first: it lists the hidden problems.

What `solutions.py` shows at the end (these are real outputs from this pack):

| Step | Result | Lesson |
|---|---|---|
| Random 80/20 split of overlapping windows, machine A only | **100%** test accuracy | Looks perfect… |
| Same model on machine B | **50%** (calls everything "fault") | …it only learned machine A. That's data leakage |
| Split by session, train on both machines | **98.8%** on unseen sessions | This is the honest number |
| Machine B left in raw counts | **50%** (everything "fault") | The units bug from round 2, Question 3 |
| Machine C | **50%** (misses every fault) | It's really 400 Hz, so the 300 Hz fault aliased to 100 Hz. Must re-record |

---

## Study plan (about 10 sessions of 1–2 hours)

| # | Session | Do | You should be able to say |
|---|---|---|---|
| 1 | pandas basics | Read the pandas "10 minutes" guide. Open each customer CSV and run `head()`, `describe()`, `isna().sum()`, `diff()` | "First I look at the data before trusting any note" |
| 2 | Exercises 1, 2a–2c | Loading, sample rate, gaps | "I check the real sample rate from timestamps, and I look for dropped samples" |
| 3 | Exercises 3a–3e | Units, clipping, missing values, resampling | "Gravity tells me the units; I convert counts to the training units" |
| 4 | numpy + filtering | Exercises 4 and 5. Read the numpy beginners guide (arrays, shapes, broadcasting) | "Any filter I apply before training must also run on the device, so I put it in the DSP block" |
| 5 | FFT and features | Exercise 6. Plot one normal and one fault spectrum with matplotlib | "The DSP block turns 3,000 numbers into a dozen that make the fault obvious" |
| 6 | Exercise 7 + case study | Export, then run `solutions.py` and explain every step out loud | The 5 lessons in the table above |
| 7 | C++ basics | Read learncpp.com chapters on types, arrays, pointers, structs. Run `02_int8_quantization.cpp` | "int8 = 256 steps; outliers make the steps coarse" |
| 8 | C++ on a microcontroller | Read and run `01_sensor_to_classifier.cpp`. Do its four "TRY THIS" items | "Raw counts → units → ring buffer → interleaved float buffer → `signal_t` → `run_classifier`" |
| 9 | C++ exercises | `03_exercises.cpp` until 16/16 PASS | Ring buffers, unsigned maths traps, O(1) filters |
| 10 | Real Edge Impulse | Free account: upload the files in `edge_impulse_upload/`, build Spectral Analysis + classifier, look at the Feature Explorer and confusion matrix. Optional: download the C++ library and build `example-standalone-inferencing` | "I've taken messy data all the way to a model and a C++ build myself" |

---

## Customer data intake checklist (the interview gold)

When a customer sends data or says "the model doesn't work", ask or check:

1. **Real sample rate.** Work it out from the timestamps. Is it more than 2× (ideally 3–5×) the fault frequency?
2. **Units.** Counts, g, or m/s²? The same on the device as in training?
3. **Sensor range and clipping.** ±2 g sensor on a machine that hits 3 g = data lost.
4. **Gaps and jitter.** Dropped samples (serial/BLE buffers) and irregular timing.
5. **Column / axis order.** Is X really X on the device? Is the buffer interleaved as `[x0, y0, z0, x1, …]`?
6. **Duplicates and empty cells.** Logging scripts re-send lines; I2C glitches give blanks.
7. **Pre-processing.** Did they filter or scale in Python before upload? Then the device must do exactly the same, or move it into the DSP block.
8. **Variety.** How many machines, sessions, days, loads, operators? (This is where leakage comes from.)
9. **Balance.** How much fault data versus normal? Look at the confusion matrix, not accuracy.
10. **Same sensor, same mounting** in training and in the field?

**One-line answer if asked "what goes wrong with customer data?":**
> "Usually it's not the model, it's the data path: wrong sample rate, wrong units, dropped samples, or pre-processing done in Python that the device doesn't repeat. And the test set is often too similar to training. I check those first, from the raw buffer on the device back to the training data."

---

## Resources
- pandas, 10 minutes to pandas: https://pandas.pydata.org/docs/user_guide/10min.html
- NumPy for absolute beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
- SciPy signal processing tutorial: https://docs.scipy.org/doc/scipy/tutorial/signal.html
- C++ from scratch (free, very good): https://www.learncpp.com/
- Edge Impulse docs: https://docs.edgeimpulse.com (search for: *C++ library*, *CSV Wizard*, *Data forwarder*, *Ingestion API*, *Spectral features*)
- Edge Impulse standalone C++ example (this is what `01_sensor_to_classifier.cpp` copies): https://github.com/edgeimpulse/example-standalone-inferencing
- Edge Impulse DSP block source code, in Python (see how Spectral Analysis really works): https://github.com/edgeimpulse/processing-blocks
