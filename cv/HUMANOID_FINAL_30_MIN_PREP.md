# Humanoid – Final 30-Minute Prep

**Friday 30 Oct · Technical Execution Interview · Senior Hardware Test Engineer**

**How to use this:** read it top to bottom once (about 25 minutes). The answers are written to be spoken; if you're skimming, read the **bold words**.
**Only 10 minutes?** Read Section 1, the 60-second opener, D1, R1, R4 and P1.

## 1. Before you walk in

### The panel
- **Dmitrii Ovsiannikov, Lead Test Engineer** (probably your manager). Ex-Head of QA at Martistel (warehouse shuttle robots): test strategy, quality gates by maturity, production QC in stages, tracking field incidents. Ex-Arrival.
- **Max Inerfield, Senior Test and Validation Engineer.** Ex-BSI, Lead Mechatronics Engineer: repeatable procedures, measurement, standards.
- **Richard Weight, Senior Test and Validation Engineer (automation and AI test design).** Ex-GE Aerospace; built Vertical Aerospace's Iron Bird HIL rig; ran motor dynos (2–500 kW) at Magnomatics. **Don't bluff dyno details with him.**

### Six rules
1. **Answer every part.** "How would you test X?" → purpose → safety → rig → measurements → pass/fail → why it matters on the robot.
2. **Something failed?** Contain → Capture → Compare → Reproduce → Fix → Prevent.
3. **Before a verdict, question the measurement:** uncertainty, conditions, how many units. Repeats catch noise, not bias.
4. **Clues:** works here, fails there → list the differences. Too hot → load or loss? Dropped off the bus → reset (power) or bus-off (signal)?
5. **Say "I", give one number, end with prevention:** "…and I'd add it to the end-of-line test."
6. **Don't know?** Say so → the map you'd expect → what it means for testing.

### Get these right
- **"Nearly eight years."** AVL from November 2018; about two years on-site at JLR.
- **MSc:** "I designed the test; the bench wasn't built." (Your CV says "experimental testing".)
- **Stewart platform:** a team project, not finished; each actuator moved to the commanded angle.
- **Your car:** say "my Mercedes S-Class V12", with no model number.
- **Start date:** "Within about two weeks. I'll confirm the exact date once my leaving date at Bosch is agreed."
- **ROS:** user level, ROS 1 Noetic. Only say you practised ROS 2 if you actually did the drill.

### Two sketches to be ready to draw
```
Radar:  real world  target → antenna → detections → OBJECT CREATION → alert logic → CAN
        HiL         simulated objects ─────────────────────────────→ alert logic → CAN
        The failure was in OBJECT CREATION: the one stage the HiL never exercised.

Robot:  cameras → System 1 VLA (5–10 Hz, actions 30–50 Hz) → System 0 whole-body (50 Hz)
        → drives → actuators → motion. Check timing and values at every arrow.
```

## 2. Your background story

### 60-second opener: "Tell me about yourself"
> "I'm a mechanical engineer with nearly eight years testing safety-related automotive systems.
> At AVL I spent about two years on-site at Jaguar Land Rover as feature owner for three corner-radar features. I wrote the requirements and test cases, and tested on HiL rigs, in vehicles and on the proving ground, analysing logs in CANoe and CANape. I also worked on AVL's DrivingCube, fitting GNSS ground truth and driving the steering tests we used to calibrate the simulation, and at the LEVC taxi factory, checking generators that came back faulty.
> For the last five years, at FiveAI, now Bosch, I've worked on an L4 driving stack: over 120 parameterised test scenarios, the pass/fail KPIs and Python tools, and I led five engineers for a year.
> I want to get my hands back on hardware and own a test area. Deciding what good looks like, from one actuator to the whole robot, is exactly that."

### 2-minute story: "Walk me through your background"
> "I'm originally from Turkey. I studied mechanical engineering at Ege University in Izmir. Alongside the degree I taught science and space technology part-time at Space Camp Turkey for about three years, which taught me to explain technical things simply. I did an internship at TEMSA, the bus maker, calculating power and torque for a new electric bus powertrain in MATLAB and Simulink. For my final project our team built a six-degree-of-freedom Stewart platform. I did the wiring and the Arduino code to drive each servo. We didn't finish full pose control, but that's where I found I like building real things that move.
> In 2017 I came to the UK for an MSc in Sustainable Automotive Engineering at Warwick. My dissertation designed a thermal test for an electric motor stator.
> In 2018 I joined AVL in Coventry. AVL placed me at Jaguar Land Rover for about two years as feature owner for three corner-radar features, from requirements and state diagrams through to testing on HiL rigs, in cars and on the proving ground. The problem I'm proudest of from there is a radar alert that passed on the HiL but failed on the track; happy to go into it. I also worked on AVL's DrivingCube and at the LEVC taxi factory.
> In 2021 I moved to FiveAI in Cambridge, now part of Bosch, working on an L4 automated driving stack. I built over 120 parameterised test scenarios, set the pass/fail KPIs, trained Volkswagen Group partner engineers on our toolchain, helped found our solutions team and led five engineers for a year. I also build tools: if a step is clumsy, I automate it. My AI helper cut writing a scenario from about a day to about an hour. Recently I've been running a vision-language-action model in our simulation tests.
> FiveAI is restructuring, and it's the right moment to go back to hardware. Outside work I fix my own cars, build my own PCs and learn applied AI engineering. Humanoid brings it all together: real hardware, an AI-driven robot, and the job of deciding what good looks like."

### If they follow up
- **Why Humanoid?** "You've moved past demos: proofs of concept at Siemens, Bosch and Schaeffler, Bosch building the robots, and robots going live at Schaeffler from December. The next problem is making every robot that leaves the line as good as the one in the lab. That's a test problem, and it's the part of engineering I enjoy most."
- **Why robots, coming from cars?** "An autonomous car is a robot on wheels: sensors, perception, planning, actuators, and the same test problems. HMND-01's commercial version is on wheels too. And my final-year project was a small robot."
- **"Your last five years were simulation. Why trust your hands-on skills?"** "My hands-on years were at AVL: HiL rigs, vehicles, the proving ground, the DrivingCube and the LEVC factory. The last five years built the other half of this job: test methods, KPIs and automation at scale. I've kept my hands busy with my own cars; I found a battery drain on my Mercedes fuse by fuse. I'll learn your rigs and instruments quickly."
- **Why leave Bosch?** "FiveAI/Bosch is restructuring and my project is winding down, so the timing is right. But I'd want this role anyway: I want to get back to hardware."
- **When can you start?** "I'm in a redundancy consultation, so I'm flexible: within about two weeks. I'll confirm the exact date once my leaving date is agreed."
- **Five years from now?** "Owning a test area here first, then leading a small test team or a work package."
- **Your MSc?** "I designed a test to find the unknown values in a thermal model of a motor stator: MotorCAD's thermal network, where the thermocouples go, the enclosure, the method. The bench wasn't built within the project, so it's test design rather than testing. It's why I think of actuator thermal tests as heat paths and hot spots."
- **Your Stewart platform?** "A team project: six servos moving one platform, designed in SolidWorks and driven from an Arduino. I did the wiring and the code to command each servo, and we plotted the signals to check each did what we commanded. We started the inverse kinematics in MATLAB but didn't finish full pose control. The lesson: bring hardware up one actuator at a time."
- **Salary** (unlikely today): "Happy to cover that with Amar. I'm flexible for the right role."

## 3. Dmitrii: strategy, gates, ownership

### D1. "Tell me about a test failure you owned end to end."
*Your experience: the JLR radar alert*
> "At JLR I owned Rear Cross Traffic Alert. The requirement was a warning **at least two seconds** before a collision. A defect came in: reversing out of an angled space with traffic at **45 degrees**, we got **no warning and no braking, or about half a second**.
> The clue was that the same scenarios **passed on our dSPACE HiL**. But the HiL fed simulated objects straight into the ECU, so it never tested the radar's own detection.
> I designed a sweep for the track: 30, 45 and 60 degrees; walking and running pedestrians and vehicles up to 40 mph; both sides; our car reversing at up to 10 mph. I found where failures outnumbered passes and refined there. I **synchronised the camera, the CAN and the radar's internal data** in CANoe and **compared the failing run with the nearest passing one**. Near the edge of the field of view, the radar held targets as low confidence until it was too late.
> I took the evidence to the supplier. Their engineer came on site, we tested **three calibration candidates** through coarse and fine test sets, **including false-alert tests**, and picked the best. I re-ran the boundary cases on the track to verify it.
> **The lesson: know which part of the chain each rig really tests.**"

### D2. "When is the arm ready to move from EVT to DVT to PVT?"
*Your experience: ASPICE at JLR, regressions at FiveAI*
> "I'd agree **exit criteria for each gate up front**, plus an **open-issue rule**: no open severity-1 issues, and severity-2 only with an owner and a date.
> **EVT: does the design work?** Key functions at nominal on several units, characterised against design intent, and a test planned for every major FMEA risk.
> **DVT: does the production-intent design meet every requirement with margin?** Endurance with enough cycles for a statistical claim, environmental and EMC, safety functions. Then **freeze the design, the methods and the limits**.
> **PVT: can the line build it at rate?** Production tests proven (MSA, seeded faults rejected, results matching the lab), first-pass yield on target, results stored against every serial number.
> I've worked this way before: at JLR every level of requirement in the ASPICE V-model had its own verification, and at FiveAI I compared KPI results across stack versions to catch regressions."

### D3. "Three weeks after go-live at Schaeffler, a robot trips on shoulder over-temperature. We never saw it in the lab."
*Your experience: the radar lesson, LEVC returns*
> "**Contain** first: safe, the customer kept running, and **logs pulled before anyone power-cycles it**.
> Then **load or loss?** Was the joint working harder than in the lab (heavier totes, more lifts, hotter ambient), or is this actuator losing more, like higher friction? I'd **compare with the sibling robots** on the same job and with our lab duty cycle, and pull the actuator's **production test record by serial**. Then it goes on the dyno with the **real field duty cycle**, and I'd check the thermal margin across the fleet.
> Then the **escape**: why didn't the lab catch it? Probably our duty cycle or limits were gentler than reality. So the fix goes into the tests: an endurance profile from field logs, a tighter end-of-line friction limit, a field alert. I'd run it as an 8D.
> It's the radar lesson again: the lab passed because it didn't reproduce the real condition. And from the LEVC factory I know returned units are only useful when every unit has the same checks and data tied to its serial."

### D4. "How do you make sure other people can run your tests? How did you lead your team?"
*Your experience: technical lead for five engineers at FiveAI*
> "At FiveAI I was technical lead for five engineers for a year. I taught them the tools and the evaluation logic, and split the work so writing scenarios and evaluating them ran in parallel. Teaching shows you every gap in a method: each question someone asks is something the method is missing.
> So my specs leave nothing to memory: equipment with calibration, preconditions, numbered steps, the exact analysis, limits with versions, and what to do on a fail. Then someone who has never seen it runs it while I watch."

### D5. "Tell me about a mistake you made."
*Your experience: the map converter at FiveAI*
> "At FiveAI I converted our simulator's maps to OpenDRIVE for the validation tool, with an open-source converter I adapted using Copilot. My mistake was **validating it by eye** and with a few simple scenarios. Later the validator reported **'stay in lane' failures that weren't real**: on curves, the converted lane lines had become coarse straight segments, so the car seemed to touch the line.
> Now I validate any tool in the measurement chain on its **hardest cases, here tight curves, with a numeric check**. I learn the maths behind both sides, and I ask the experts earlier. In hardware terms, I'd trusted a measurement tool without an MSA."

### D6. "You disagree with design or Manufacturing about a limit. What do you do?"
*Your experience: between JLR and the radar supplier*
> "Go back to **what the test must prove, and the data**. At JLR I was an AVL contractor between JLR and the radar supplier. I had no authority over either, so my only lever was **evidence**: synchronised logs at the exact boundary and a clear hypothesis. That's what got their engineer on site.
> If a limit can't be traced to a robot-level need, I'll relax it. If it can, I show the consequence. And I don't change a limit to make something pass: shipping with a known issue is a documented, signed-off deviation."

### D7. "Tell me about a time your test data found something."
*Your experience: the curvature finding at FiveAI*
> "On UN R79 lane-change testing at FiveAI, our KPIs were lane-change success and lateral acceleration, and we recorded road curvature with every run. **Above a certain curvature, success dropped, even though that curvature was inside the spec** the feature had to handle. So it was a real weakness inside the feature's own operating range, not an unfair test, and it led to a **fix in the steering controller**.
> The lesson: **record the test conditions next to the results**, so you can split the results by condition. An overall pass rate would have hidden it."

## 4. Max: procedures, measurement, standards

### M1. "A production grip-force check that a technician runs without you, and two technicians get the same answer."
*Your experience: the fixed procedure at LEVC*
> "I'd **take the judgement out, then prove it**. A fixture holds the hand by its mounting face, so the fingers close on the sensor at the same points; the rig commands the grip, measures and decides.
> The procedure has scope, safety, equipment IDs with calibration dates, and preconditions (firmware, supply voltage, zeroed sensor). Numbered steps: scan the serial, zero, command the grip, wait two seconds, average the next second, three repeats. Then the limit with units; a **reaction plan** (one retest after re-seating, then quarantine and an NCR); and results straight to the database against the serial.
> Then I prove it: a **dry run by someone new**, a **Gauge R&R** (ten hands, three technicians, two or three repeats, under 10% of the tolerance) and a **golden hand** at the start of each shift.
> At LEVC I was on the other side of this: I ran the supplier's fixed procedure on about twenty returned generators. Every unit got the same checks and log download, which is what makes recurring failures visible."

### M2. "Repeatability measured 0.4 mm; the spec is 0.5 mm. Can we sign it off?"
*Your experience: timing the radar alerts*
> "Not yet. Three questions first. **Measurement uncertainty**: if the tracker set-up is good to a few hundredths of a millimetre, 0.4 plus that is still inside 0.5 and it's a real pass; if it's ±0.1, it's inconclusive. **Conditions**: was it measured as the spec defines, ISO 9283 with rated payload and speed, 30 cycles, warmed up? **How many arms**: one arm with 0.1 mm of margin doesn't prove the design.
> I met this on the radar work. We timed alerts two ways: marks on the ground and the logged signal. At 40 mph, half a metre of marking error is a few hundredths of a second; for a walking pedestrian it's over a third of a second. So near a boundary, the logged timing is the one to trust."

### M3. "Which standards apply to HMND-01, and how do they change your test plan?"
*Your experience: ISO 26262, SOTIF and FMEA at AVL*
> "My background is automotive: I wrote ISO 26262 requirements, I'm trained in SOTIF, and I took part in an FMEA for a lane change feature at AVL. On the machinery side I'd expect: the **EU Machinery Regulation from January 2027** and the CE mark; risk assessment to **ISO 12100**; safety functions to a performance level under **ISO 13849**; **ISO 10218** for industrial robots; **IEC 60204-1** for the electrical side; industrial **EMC**; and **ISO 3691-4** for the mobile base. ISO 9283 is a performance test method, not a safety standard.
> For the test plan, that means **safety functions verified with measured evidence** (stopping times, brake holding, power loss), **EMC and environmental pre-compliance early in DVT**, and everything traceable into the technical file. And if a safety function relied on the AI policy, the new regulation requires a third-party assessment, so I'd want safety functions independent of the policy."

### M4. "How do you know your measurement or ground truth is right?"
*Your experience: GNSS on the DrivingCube project, the map converter*
> "With an **independent reference, checked on its hardest cases**. On AVL's DrivingCube project I **fitted an external GNSS system** to the car, so we judged the car against something that didn't depend on its own sensors. It's the same idea as a laser tracker on a robot arm: the arm's encoders can't see their own errors.
> My map-converter mistake taught me the other half: a tool checked only on easy cases gave false failures on the hard ones. So: an independent reference, calibration in date, a golden unit, and an MSA before I trust a rig."

### M5. "What hands-on tools and instruments have you used?"
*Your experience: LEVC, test vehicles, your own cars*
> "Mostly the **multimeter**: resistance and continuity checks on returned generators at LEVC, and fuse-by-fuse fault-finding on test vehicles and my own cars. A **torque wrench**, including checking the control arms on a test vehicle. **Calipers and micrometers**, which I used to set up my own tools to cut straight. I've **soldered motor drive cables onto a PCB** and wired a car audio system. For logging: CANoe, CANape, GNSS ground truth and cameras synced with vehicle data.
> I haven't used an oscilloscope or load cells professionally. I know what I'd use them for here, and I'd pick them up in the first weeks."

### If GD&T comes up
Read a frame left to right: **symbol | tolerance | datums**.
- `[⏥ | 0.05]`: flat within 0.05 mm (form, so no datum).
- `[⊥ | Ø0.02 | A]`: the axis lies inside a 0.02 mm cylinder perpendicular to datum A.
- `[⌖ | Ø0.1 Ⓜ | A | B | C]`: the hole's axis lies inside a 0.1 mm cylinder at its true position from A, B and C; bonus tolerance as the hole gets bigger.
- `[↗ | 0.03 | A-B]`: spin the part on the A-B axis; the dial may vary by at most 0.03 mm.
- **Why it matters:** runout or misalignment side-loads bearings, which means friction, heat and wear, then torque and thermal problems on the robot. Fixtures should locate parts on their datums.
- **Honest line:** "I read drawings and tolerances, and I've refreshed GD&T. I haven't specified it myself."

## 5. Richard: rigs, dynos, HIL, automation and AI

### R1. "A new actuator revision is on your bench. How would you characterise it?"
*Your experience: torque injection on the DrivingCube project*
> "First I'd find out **what changed** from the last revision, and get the spec and the old results, so I test what changed first.
> **Bring-up, safely:** visual and serial checks, phase resistance balance, insulation. Then logic power first on a current-limited supply, comms, encoder direction, brake and fault reactions, with the E-stop checked before anything moves.
> **Rig:** a bracket matching the robot's interface, an aligned coupling, an in-line torque transducer, a back-to-back load motor, a lock and an inertia disc, thermocouples, and the actuator's own CAN FD data logged in sync with the DAQ.
> **Measure:** Kt and linearity, friction and no-load current, lost motion and stiffness, step response, the speed–torque envelope at minimum battery voltage, and thermal: continuous torque to steady state, and time at peak torque.
> **Decide:** at least three units against the spec, and **A/B against the old revision on the same rig with the same script**. Where there's no limit yet, I characterise and set limits from the spread.
> I haven't run a motor dyno myself. My closest is the DrivingCube work, where we injected steering torque at set speeds to capture the car's response and calibrate the simulation. Same idea: system identification."

### R2. "Kt comes out 6% below the datasheet. What do you check before telling Schaeffler?"
*Your experience: the HiL that passed for the wrong reason*
> "Repeats won't help: **a steady 6% is a bias, not noise.** So I'd check the test first.
> **Same definition?** RMS or peak, phase or line current, motor side or output side; gearbox losses alone could be a few percent. **Temperature:** magnets lose about 0.1% per degree, so 6% is like running 60 °C hotter. **Current:** cross-check the drive's reading with a probe. **Torque:** transducer calibration and alignment. And is the drive limiting?
> Then a **known-good unit and a second new unit** on the same rig: if everything reads low, it's my method; if only this one does, it's the part. Then I go to Schaeffler with data, ideally measuring the same unit on both rigs.
> That's the radar lesson: our HiL said pass because of how it tested, not because the system was right. Check the test before blaming the part."

### R3. "One joint drops off CAN FD, only during fast moves on the full arm, never on the bench."
*Your experience: fuse and module fault-finding on test vehicles*
> "**Works here, fails there, so I list the differences:** the harness through moving joints, other motors switching nearby, a supply shared with every joint, a longer network.
> Then **what kind of drop?** A reset points to power; error-passive or bus-off points to the signal. The fault codes and error counters tell me which. I'd look for a pattern with joint angle and speed.
> Then **measure:** a scope on the supply at that joint during a fast move, and on CAN high and low for noise in step with the PWM; check the termination reads 60 Ω. Then **isolate:** flex the harness by hand while watching the counters, swap the cable, feed the joint from a separate supply.
> A long soak to prove the fix, and **bus error counters go into the end-of-line test**.
> It's how I found faults on test vehicles: when a module didn't activate, the fault code was only the symptom. I'd check its fuse, find out why it blew, and sometimes power the module on the bench from 12 V to see whether the fault followed the module or stayed with the car."

### R4. "What does a HIL not tell you?"
*Your experience: the JLR radar HiL*
> "**Whatever it bypasses.** Our dSPACE HiL at JLR had the real radar ECUs on the real vehicle CAN, but it fed **simulated objects in after the radar's object creation**. So it proved the alert logic but never tested the sensor's perception, which is exactly where the failure was. Every test passed; the track failed at 45 degrees.
> Now, for any rig (HIL, dyno or end-of-line), my first question is **which part of the chain it really exercises and which part it emulates**. Anything that depends on the emulated part counts as untested until it runs on real hardware."

*Then ask him: "How did you decide what to emulate on the Iron Bird?"*

### R5. "How do you use AI in test design, and how do you trust what it generates?"
*Your experience: the Copilot scenario helper at FiveAI*
> "I built a Copilot skill that writes OpenSCENARIO test scenarios from Euro NCAP protocols. It had a folder of **golden scenarios that never change**, the DSL documentation, the NCAP text and rules for building modular scenarios.
> It **plans first, then writes with default parameters only**. I run and check that set by hand before adding parameter ranges and the evaluations.
> Then I triage in order. **Errors**: it didn't run, usually syntax or the stack not starting, which tells me what the skill didn't anticipate, so I fix the skill. **Failures**: it ran but went wrong, like the car leaving the map at some parameter values. And **random passes**, because the dangerous result is a pass that only happened because an evaluation was missing.
> A scenario went from **about a day to about an hour**. The rule I taught: the AI writes, a human verifies. For robot tests I'd keep the same guard-rails: golden references, errors kept apart from failures, and passes audited with seeded faults."

### R6. "What would you automate, and what stays manual?"
*Your experience: the tools you built at FiveAI*
> "Automate what's **repeatable, numeric, frequent, long or risky**: every-unit tests, endurance, step responses, anything better done with people out of the cell. Keep **first bring-up, exploration and subjective checks manual** until we know what to measure. The path is manual, then scripted analysis, then semi-automatic, then fully automatic.
> I find what to automate by using a process end to end. At FiveAI I built a JSON parameter GUI because parameter combinations were easy to get wrong by hand, a config creator so new scenarios could be tried without the edit-save-push loop, and a local uploader to get local results into our dashboards.
> When I hand a test to automation, I define **PASS, FAIL, ERROR and INVALID** up front, plus an acceptance test: the automated rig must match my manual results and reject known-bad units."

## 6. Panel scenarios

### P1. "HMND-01 drops a tote on cycle 85. The AI team blames hardware; the hardware team blames the policy."
*Your experience: the radar investigation, the curvature finding*
> "Stop, make it safe, and **capture everything before any reset**: logs and bags, fault codes, video, software and hardware versions, ambient, battery, and the tote itself.
> Then let the data decide, not the teams. **Follow the chain at the moment of the drop:** frames on time? Commanded hand pose right? Joints followed it? Grip force held? If the command was wrong but tracked perfectly, it's the policy. If the command was right but a joint lagged or the grip faded, it's hardware.
> **Why cycle 85 and not cycle 1?** Something builds up, so I'd trend every cycle (joint temperatures and derating, battery voltage, grip force, tracking error, camera latency) and compare 85 with 84 and with 1.
> **Replay the same joint commands with the policy out of the loop.** If it still drops, it's hardware. If the problem is new, swap old and new policy against old and new hardware.
> I'd share the plots with both teams together, and add a test so it's caught on the bench next time.
> I did this with the radar at JLR: synchronised logs, then compare with the nearest pass. And at FiveAI our curvature finding only showed up because we recorded the conditions with every run."

### P2. "A new actuator revision arrives Monday; the design review is Thursday. Walk us through your week."
*Your experience: readiness checks on the DrivingCube*
> "**Before Monday:** get the change list from design and agree what Thursday has to answer.
> **Monday:** incoming checks on at least three units, safe bring-up, first unit on the dyno.
> **Tuesday:** what changed first, then a short regression (Kt, friction, lost motion, step response), **A/B against the old revision on the same rig with the same script**. Start an **overnight thermal soak**.
> **Wednesday:** analyse, repeat anything odd on a second unit, check my test before blaming the part, and give design a **heads-up**.
> **Thursday:** one page: pass/fail, differences from the old revision, **what we haven't tested and the risk**, and a recommendation: release, hold, or release with conditions.
> It's how I ran DrivingCube days: readiness checks before every run (logging healthy, the right simulation loaded, every system active), because a run with bad data is wasted."

## 7. Quick answers, numbers and your questions

### Honest one-liners
- **ROS 2?** "I've used a ROS 1 Noetic set-up as a user: a VLA model in Docker, bridged with rosbridge to our simulator and orchestrator, and Foxglove for results. I haven't written ROS nodes. In testing I'd use bags as evidence and topic rates and latency as health checks."
- **Oscilloscope?** "Not professionally; my electrical work has been multimeter and logger based. Here I'd use one for bus droop under peak torque, inrush, CAN signal quality and E-stop timing."
- **EtherCAT?** "Not used. My bus experience is CAN at signal and log level in CANoe and CANape. Robots use EtherCAT for deterministic timing across many joints."
- **Production test?** "I haven't owned production tests. I've been on the receiving end of escapes at LEVC, I know the concepts (takt, travellers, in-process checks, MSA), and I'd lean on Manufacturing Engineering and Production Ops for their practice."
- **Gauge R&R?** "I know the method; I haven't run a formal study. I'd run one on the first rig."
- **Insulation or hipot testing?** "Not done. It proves there's no leakage path from the windings to the housing at well above the working voltage, which a multimeter can't show."
- **Motor dyno?** (Richard) "Not myself; my closest is torque injection on the DrivingCube project. I'd want to learn how you run yours."

### Numbers
- **Your record:** 2 s required, got none or about 0.5 s; 30/45/60°; targets up to 40 mph; your car reversing at up to 10 mph; three calibration candidates; about 20 generators at LEVC; 120+ scenarios; 1,000+ hours of data; 5 engineers for a year; about a day → about an hour per scenario.
- **HMND-01:** 29 DOF (the hand has 12); the VLA predicts at 5–10 Hz with actions at 30–50 Hz; System 0 whole-body control at 50 Hz; Siemens trial: 60 totes an hour, over 90% success, 8+ hours; Schaeffler is the preferred actuator supplier (over half the wheeled robots' joint actuators, to 2031); Schaeffler go-live from December; Bosch builds the robots.
- **Rules of thumb:**
  - 1 arcmin ≈ 0.29 mm per metre of lever.
  - Copper resistance +0.39% per °C; magnets about −0.1% per °C (Kt about 8% lower at 100 °C).
  - Measurement tool about 10× better than the tolerance (4:1 at worst).
  - Cpk ≥ 1.33 (1.67 for critical); Gauge R&R below 10% good, above 30% not acceptable.
  - Zero failures in n trials → failure rate below 3/n (95% confidence), so about 300 clean trials for 99%.
  - CAN: 60 Ω between CAN_H and CAN_L with the power off.
  - ISO 9283: 5 points, 30 cycles.

### Your questions (one each)
- **Dmitrii:** "How do you define the gates between EVT, DVT and PVT here, and which subsystem goes through DVT first?" or "What would make the first 90 days a success for this role?"
- **Max:** "How do you handle measurement uncertainty and calibration on the lab rigs today? And how much are you designing tests with certification in mind already?"
- **Richard:** "How are you using AI agents in test design, and how do you keep the generated tests trustworthy?" or "Is there a full-robot HIL, an iron humanoid? How did you decide what to emulate on the Iron Bird?"

### Last two minutes
- Water; pen and paper for sketches.
- Slow down. Short answer first, then ask: "Shall I go deeper on any part?"
- A pause is fine: "Let me think out loud for a moment."
- They're future teammates. Be curious about their work.
