# Qualcomm / Edge Impulse: Customer Scenario Bank (Post-Sales)

> Practise saying each one out loud in about 90 seconds. Zin's team is the "customer-facing technical arm", so expect *"A customer comes to you with X. What do you do?"*
> Every scenario follows the same rhythm, which is also how you worked at JLR and in SimEco:

## The 6-step rhythm (say it once early, then use it every time)
1. **Listen & get facts:** what exactly happens, on which device, since when, and how do they know?
2. **Reproduce:** get the data or buffer and reproduce it in Studio or on a dev board.
3. **Isolate:** data, DSP, model, device code, or expectations?
4. **Fix:** smallest change that solves it; verify on the real device.
5. **Prevent:** add the case to the test set, monitor, write a feature request if the tool could help.
6. **Communicate:** short written recap to the customer's engineers *and* a one-line status for their manager.

> **Line to open with:** *"Before touching the model, I want to understand the symptom and get the actual data, so we're fixing the real problem rather than guessing."*

---

## S1. "The model won't fit on our microcontroller" (build fails / crashes / out of RAM)

- **Ask first:** Which chip? How much RAM and flash are **left after their own firmware** (their app, RTOS, radio stack also use memory)? float32 or int8?
- **Look in Studio:** the DSP and model pages show **estimated RAM, flash and time** for the chosen target. Compare with what's actually free.
- **Fixes, cheapest first:**
  1. Switch to **int8** (≈4× smaller weights).
  2. Use the **EON Compiler** (removes the interpreter, less RAM/flash).
  3. Make the DSP output smaller: fewer FFT bins, lower sampling rate if Nyquist allows, shorter window.
  4. Smaller model; let the **EON Tuner** search for the best accuracy that fits the memory limit.
  5. If it truly can't fit: be honest. Offer a bigger chip or a Linux/Qualcomm board.
- **Say to the customer:** *"Your chip has about 100 KB free after your firmware. The current model needs 180 KB. With int8 and EON it estimates 70 KB, and accuracy drops only 1%. I'd go with that and verify on your board."*
- **Your link:** working within hard limits like timing requirements (2 s alert at JLR) and agreeing trade-offs with suppliers.

## S2. "Too many false alarms in the field" (anomaly detector fires every morning)

- **Ask first:** When exactly do the alarms happen? What's the machine doing then? What's worse for them: a false alarm or a missed fault?
- **Likely cause:** **cold start** (or a cleaning cycle, a different product, weekend shutdown) was never in the "normal" training data, so the model calls it abnormal.
- **Fix:**
  1. Collect data from those conditions and add it to the **normal** training set, then retrain.
  2. Tune the **anomaly threshold** using real field windows, not a guess.
  3. Add **debouncing** in the device logic: alarm only if the score is high for e.g. 5 windows in a row.
  4. Agree the target with them in numbers, e.g. "fewer than 1 false alarm per machine per week".
- **Say:** *"The model isn't broken. It's never seen a cold start, so to it that looks abnormal. We'll add a week of morning start-ups to the normal data and add a 1-second confirmation before alarming."*
- **Your link:** JLR false-positive / false-negative test sets when choosing between three radar calibrations.

## S3. "It's too slow: inference takes 400 ms, we need under 100 ms"

- **Ask first:** Which part is slow? Studio shows **DSP time and model time separately**.
- **If DSP is slow:** shorter FFT, fewer filters/bins, lower sample rate, or use the chip's optimised maths libraries (Edge Impulse uses CMSIS-DSP/NN on Arm when available).
- **If the model is slow:** int8 (integer maths is faster), smaller network, or run it on an accelerator (e.g. the **Hexagon NPU** on Qualcomm boards).
- **Also check:** do they really need an answer every 0.2 s? A longer stride means fewer runs per second.
- **Say:** *"80% of the time is the FFT, not the neural network. Halving the FFT length gets us to about 90 ms with the same accuracy on the test set."*

## S4. "We have 500 GB of messy data in an S3 bucket. Can you help?"

- **Ask first:** What's in it (sensors, rates, formats)? How are faults recorded (maintenance logs, technician notes)? Who owns it?
- **Plan:**
  1. Agree one **standard format**: column names, units, sampling rate.
  2. Write a Python transformation that cleans, resamples and converts the files (Edge Impulse enterprise has **cloud bucket connections, transformation blocks and data pipelines** for this).
  3. Add **metadata** to every file: machine ID, site, date, operating mode. That's what lets you split by machine later (no leakage).
  4. **Labels:** match maintenance-log dates to recordings ("bearing replaced on 12 March" → the weeks before = worn).
  5. Start with a small clean slice, prove value, then scale.
- **Say:** *"Let's not upload everything on day one. We'll agree the format, convert one site's data, train a first model in two weeks, then automate the rest."*
- **Your link:** you built the **STAX uploader, JSON parameter GUI and dashboard pipelines** at FiveAI across 1,000+ hours of data.

## S5. "Accuracy is stuck at 80%, we need 95%"

- **Look first:** the **confusion matrix**. Which classes get mixed up? (Usually it's 2 of them, not everything.)
- **Then:** the **Feature Explorer**. If those two classes' dots overlap, the model can't separate them with these features.
- **Common causes and fixes:**
  - **Wrong labels:** look at the worst samples; some are mislabelled. Clean them.
  - **Too little data** for the confused classes: record more of exactly those.
  - **DSP settings:** the difference lives in a frequency band the current settings cut off. Change the filter or FFT settings.
  - **The sensor physically can't see it:** e.g. the sensor is too far from the bearing. Be honest: move the sensor or add a second one.
- **Say:** *"95% overall isn't the real target. Missing 'bearing wear' matters more than confusing 'idle' and 'off'. Let's agree which mistakes matter and measure those."*

## S6. "It works on our first unit, but fails on unit #2"

- **Cause:** unit-to-unit variation: sensor tolerance, mounting torque or position, different machine batch.
- **Fix:** collect data from **several units** (not one), split train/test **by unit**, consider a quick calibration step at installation, and write a mounting procedure (position, torque, orientation).
- **Say:** *"The model learned unit #1's fingerprint. We need at least 4–5 units in training, and we test on a unit it has never seen."*
- **Your link:** LEVC: ~20 returned generators, same procedure on each one; production thinking vs one prototype.

## S7. "It was great for 3 months, now it's getting worse" (drift)

- **Causes:** seasons (temperature), machine wear, new product on the line, a sensor replaced.
- **Fix:**
  1. **Monitor** in the field: log confidence and anomaly scores over time.
  2. Send **low-confidence windows** back to Studio, label them, add them to the dataset.
  3. Retrain, compare with the old version on the same test set (Zin's *block versioning* idea), and ship the update (over-the-air if they have it).
- **Say:** *"Models need maintenance like any machine. Let's set up a monthly check of field scores and a simple retrain process."*
- **Your link:** FiveAI: comparing the same tests across stack versions to catch regressions.

## S8. "We're moving from the microcontroller PoC to a Qualcomm Linux board"

- **Plan:** deploy as the **Linux `.eim`** (optimised for the Qualcomm board) and use the Python/C++ SDK in their app. Then **prove parity**: run the same test set on old and new targets and compare scores; benchmark latency on the NPU vs CPU.
- **Watch out:** a different camera or sensor on the new board means new data, so check for domain shift.
- **Say:** *"Same impulse, new target. Before switching, I'll show you both give the same answers on 200 test windows, and how fast it runs on the NPU."*
- **Your link:** DrivingCube: comparing real vehicle vs dyno vs simulation on the same scenarios.

## S9. "Our keyword detector triggers on the TV" (audio)

- **Cause:** training only had the keyword and silence. The model never learned "other sounds".
- **Fix:** add a **noise** class (background: TV, kitchen, factory) and an **unknown** class (other words) with plenty of data; tune the confidence threshold; for continuous audio, use Edge Impulse's post-processing / performance calibration to set the false-trigger rate.
- **Say:** *"The model only knows two choices, so everything gets forced into one of them. We'll teach it what 'not the keyword' sounds like."*

## S10. "The camera model fails at night / in a new factory"

- **Cause:** training images only covered daytime / one site.
- **Fix:** collect images in the new lighting and backgrounds, add them, test on a held-out site. Also check camera settings (exposure, IR) match training.
- **Your link:** JLR: the HiL rig passed, the proving ground didn't. Test where the system will really be used.

---

## Customer-service scenarios (non-technical, Zin will care a lot)

### C1. Frustrated customer before renewal: "We've paid for 6 months and nothing is in production"
1. **Listen without defending.** Let them say everything; write it down.
2. **Acknowledge:** *"That's fair. Six months without production isn't the outcome either of us wanted."*
3. **Get facts:** where exactly is it stuck: data, accuracy, device integration, or their own resources?
4. **Reset the plan:** 3–4 concrete milestones with dates and owners on both sides; weekly 30-min technical sync; a monthly update for their manager.
5. **Internal:** brief our account team / customer success honestly; escalate product blockers with evidence.
6. **Follow up in writing** the same day.
- **Your link:** SimEco at FiveAI: partner teams blocked across shared tools; you found the real owner of each problem and got it fixed.

### C2. "Can Edge Impulse do X?" (and it can't)
- Understand the **real need** behind the request (*"What would that let you do?"*).
- Offer a **workaround now** if one exists (e.g. script it with the Edge Impulse API / Python SDK).
- Write a **feature request** with: customer, use case, impact (time or money), a small example, what "done" looks like.
- **Never promise roadmap dates.** *"I can't promise if or when, but I'll make sure the product team understands exactly why you need it."*
- **Your link:** DOORS requirements at JLR; the Copilot scenario helper came from spotting a slow workflow.

### C3. Customer's engineers aren't ML experts and don't trust the results
- Show, don't lecture: **Feature Explorer** (they can see healthy and faulty dots separate), the **confusion matrix** in plain words ("8 times out of 100 it calls wear 'healthy'").
- Use their language: a mechanical engineer understands "energy in the 200–300 Hz band" better than "neural network".
- Run a **live test** on their machine with them watching.
- **Your link:** Space Camp (explaining to 9–16-year-olds) and training VW partner engineers.

### C4. The customer wants it all yesterday / the scope keeps growing
- Agree **one first use case** with a clear success measure; park the rest in a written list with priorities.
- *"Let's get bearing wear on one line into production first. That proves the value, and then the other three use cases go faster because the data pipeline is already built."*
- **Your link:** splitting work packages and weekly reviews when you led 5 engineers.

### C5. You don't know the answer on a call
- *"Good question. I don't want to guess. I'll check with our embedded team and get back to you by tomorrow."* Then actually do it, in writing.
- Honest is better than confident and wrong; the customer remembers that you followed up.

---

## Quick self-test (cover the answers)
1. Model too big for the chip: 3 things to try? → int8, EON Compiler, smaller DSP output / EON Tuner (else a bigger chip).
2. False alarms every morning? → cold start missing from normal data; add it, tune threshold, debounce.
3. Slow inference: first thing to check? → DSP time vs model time in Studio.
4. Accuracy stuck: first two screens? → confusion matrix, Feature Explorer.
5. Works on unit #1 only? → collect from many units, test on an unseen unit.
6. Keyword triggers on the TV? → add noise and unknown classes.
7. Angry customer before renewal? → listen, acknowledge, facts, milestone plan, written follow-up.
