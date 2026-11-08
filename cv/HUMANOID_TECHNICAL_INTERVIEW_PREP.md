# Humanoid: Senior Hardware Test Engineer – Technical Interview Prep

**Status (Thu 29 Oct 2026):** recruiter screen with Amar Gohil passed on Mon 26 Oct. **Technical Execution Interview on Friday 30 Oct** with Dmitrii Ovsiannikov (Lead Test Engineer), Max Inerfield and Richard Weight (both Senior Test and Validation Engineers). All three are hands-on test engineers: see Section 1b. Still to confirm: time, length, and whether there is an exercise.

**Rules for every answer**
- Only say what you did. Anything marked **[CONFIRM]** needs your real detail, or drop it.
- If you haven't done something, say so in one sentence, then show how you would do it.
- Keep FiveAI/Bosch internals high level. Bosch is Humanoid's manufacturing partner, so discretion counts double.
- Your facts source of truth: `CANDIDATE_PROFILE_NOTES.md`.

**Study from here:** Section 13 (priority vs auxiliary plan) and Section 14 (self-test questions). Model answers from the mock interview are in Section 12.

**Fast path if short on time:** Sections 0, 1b, 2, 3 (S1, S5, S6, S11, S12, S13), 4.1, 4.2, 4.6, 4.8, 5 (D1, D3, D7), 6, 7, 12.

Must-know items are marked ★.

---

## 0. Fix these first (Gemini notes vs your real record) ★

The Gemini notes are useful, but several "facts" about you and about Humanoid are wrong. In a technical round, one claim that collapses under a follow-up question costs more than an honest gap. Your CV says AVL 11/2018–10/2021, so they can check.

| Don't say | Say instead |
|---|---|
| "8+ years" | "Nearly eight years" (since Nov 2018) |
| "Nearly four years embedded at JLR" | "About two years on-site at JLR, within three years at AVL" |
| "Robustness Engineer at JLR" | "ADAS Systems Engineer, feature owner for RCTA, BSM and Rear Pre-Crash" |
| CV: "experimental testing to find the variables of a thermal model"; Gemini: "you experimentally validated stator thermal models" | "My dissertation designed the test (thermocouple placement, enclosure, method) and used MotorCAD's thermal network. The bench wasn't built within the project." |
| Gemini: "you built and wired a 6-DOF platform with the same inverse kinematics challenges as a robot limb" | "A team project: I wired it and commanded each servo from an Arduino, checking with encoder data. We started the inverse kinematics in MATLAB but didn't finish full pose control." |
| "Years debugging CAN, CAN FD and Automotive Ethernet" | "I analysed vehicle network logs in CANoe and CANape. I haven't done physical-layer or deep Ethernet work." |
| "The radar saw the target but the state-machine threshold delayed the alert" | "Near the edge of its field of view the radar ignored targets until late. The alert logic was fine; the supplier's engineer recalibrated the radar on site." Full version in S1. |
| "AVL Cube: you put a real vehicle on a rolling dyno, injected torque on an airstrip and calibrated the hardware against simulation" | Mostly true, but say your exact part (S5): "On AVL's DrivingCube project I built the CarMaker scenarios, fitted GNSS ground truth to the car, drove the steering-torque injection tests on an airstrip, drove the MIRA circuit for the PID calibration data, and owned the checks before each DrivingCube run." |
| "Sony project", "UFO targets", "mirror cameras" | Not in your record. Leave out. (FMEA is fine: you took part in one at AVL for a lane change feature.) |
| "I rebuild engines and wiring looms" | "I repair my own cars and build my own PCs." |
| "I use an oscilloscope" | "My electrical checks have been multimeter and logger based. I haven't used a scope professionally." |
| "System 1 VLA runs at 30 Hz, System 2 below 1 Hz" | Public figures: the VLA predicts at 5–10 Hz; each prediction is a chunk of actions at 30–50 Hz, executed by System 0 (RL whole-body control) at 50 Hz. |
| "$300M Schaeffler deal for 1,850 units", "Ford PoC", "279 totes/h", "human parity" | Only quote numbers you can source. Public: binding phased deployment plus a 5-year actuator supply deal (see Section 8). Siemens PoC: 60 totes/h, 8 h+ uptime, >90% success. |
| "I practised ros2 topic hz this week" | True only after you do the drill in Section 10 today. |
| "I can start in three weeks" | "I can start within about two weeks; I'll confirm the exact date once my leaving date at Bosch is agreed." See the availability answer in Section 2. |

---

## 1. What the technical round is testing

**The job in one line:** decide what "good" looks like for every part of HMND 01 (actuator → arm → whole robot), prove it with tests you design and run yourself, then turn those tests into production checks for the Bosch-built line and the Schaeffler actuators.

They will probe six things:
1. **Test design with numbers:** a method, the data, pass/fail limits, and where each limit comes from.
2. **Hands-on:** bring-up of new hardware, instruments, rigs, safety.
3. **Failure analysis:** a method, not luck. Is it the part, the process, the test, or the design?
4. **Production test:** in-process checks, end-of-line (EOL) tests, rig requirements, traceability, takt.
5. **Systems thinking:** how a component problem shows up as robot behaviour.
6. **Working through others:** influencing Manufacturing Engineering (ME), Production Ops, Supply Chain Quality (SCQ) and the automation team without owning their work.

### How to answer "How would you test X?" (the 5-part answer) ★
1. **Purpose:** what decision does the test support, and which requirement does it check?
2. **Setup:** device under test (DUT), fixture, load, instruments (with accuracy), safety.
3. **Method:** steps, conditions, sample size.
4. **Data and criteria:** what you record, how you compute the metric, pass/fail, and where the limit comes from.
5. **What could fool me:** rig errors, measurement uncertainty, temperature, unit-to-unit variation.

Then link it up: *"At robot level this matters because…"*

### How to answer "Tell me about a time…"
STAR in 60–90 seconds: Situation (one sentence), Task (one), Action (three or four, say "I"), Result (a number if you have one), then one line on how it applies here. Stop and let them ask.

### Phrases that keep you honest and calm
- "I haven't done that hands-on. Here's how I'd approach it."
- "Let me think out loud for a moment."
- "The first thing I'd ask is what the requirement is at robot level."
- "A typical range is about X, but I'd take the real limit from the design spec and from data on known-good units."

---

## 1b. Your panel: who they are and what each will probe ★

"Technical Execution Interview" means they'll test how you *do* the work: plan a test, run it, read the data, find the cause, report it, and close the loop. Expect "walk us through…" and "what would you do on Monday?" more than definitions.

### Dmitrii Ovsiannikov: Lead Test Engineer (probably your future manager)
- **Background (LinkedIn):**
  - Lead Test Engineer at Humanoid since April 2025.
  - Before that, Head of QA at Martistel (Dubai), whose product was AS/RS shuttle robots (automated storage and retrieval). There he:
    - set the test strategy for 5 hardware devices, 3 software products and the whole system
    - created production QC test methods for robotic devices, in several stages
    - designed test equipment
    - introduced quality gates matched to product maturity, and release management
    - built pytest and Allure automation in a TeamCity CI pipeline
    - set up incident tracking for systems in operation, and a test management system in YouTrack.
  - Before that, at Arrival: tech lead for charging-system embedded software, releasing to maturity levels, and designing test equipment.
  - 12 years in hardware and software validation; Moscow Aviation Institute.
- **He'll probe:**
  - test strategy across levels (component → subsystem → system → production)
  - **quality gates by maturity** (what must be true to pass EVT, DVT, PVT)
  - production test in stages
  - incident tracking from the field
  - risk-based prioritisation
  - how you'd work in his team.
- **Your material:** S1, S6, S10, S2, 4.1, 4.8, D5, D7.
- **Prepare this answer: "How would you set quality gates by maturity?"**
  - **EVT exit:** the design works at nominal on N units; bring-up and characterisation done; the main risks known, each with a test plan.
  - **DVT exit:** every requirement verified with margin on production-intent parts; environmental, EMC and endurance passed; test methods and limits frozen.
  - **PVT exit:** the line builds at rate and meets its first pass yield target; production tests proven (MSA, seeded faults, correlation with the lab); traceability live.
  - **Mass production:** SPC running; field incidents feed back through 8D/CAPA.
  - **Every gate:** written entry and exit criteria, plus an open-issue rule, e.g. "no open severity-1 issues; severity-2 only with an owner, a plan and a date".
  - **Software and firmware releases get gates too:** bench or HiL smoke test → regression on a reference robot → soak test → staged fleet rollout. At FiveAI, KPI regressions in the CI pipeline played that role.

### Max Inerfield: Senior Test and Validation Engineer (joined Sep 2026)
- **Background:** about 4.5 years at BSI (the UK national standards body, also a testing and certification company), most recently Lead Mechatronics Engineer. Before that, mechatronics engineer at Interactive Imagination (visitor attractions, from concept and design through manufacture and installation). University of Liverpool.
- **He'll probe:**
  - test procedures that are repeatable and defensible
  - measurement uncertainty and calibration traceability
  - standards and certification for robots
  - hands-on mechatronics: fixtures, sensors, wiring.
- **Your material:** D1 (spec with uncertainty and calibration), S1 timing accuracy (MSA thinking), 4.10, 4.15, 4.18, S10, ISO 26262/SOTIF training.
- **Learn tonight:**
  - **ISO/IEC 17025:** what testing and calibration labs are accredited to (UKAS in the UK). It covers validated, documented methods; measurement uncertainty; traceability of calibrations to national standards; equipment records; staff competence; impartiality; reporting.
  - **Robot certification in one breath:** risk assessment (ISO 12100) → apply harmonised standards (ISO 10218-1/-2, ISO 13849-1, IEC 60204-1) → technical file → declaration of conformity and the CE/UKCA mark. The EU Machinery Regulation applies from January 2027.

### Richard Weight: Senior Test and Validation Engineer, automation and AI (joined Apr 2026)
- **Background:**
  - At Humanoid: "automated and AI agentic test design".
  - Before: GE Aerospace (Advanced Lead System Verification Engineer).
  - Vertical Aerospace: built the **Iron Bird** HIL rig, covering the structure, mechanical and electrical integration, a dynamic loading rig, HIL models in Simulink, HV integration, emulated aircraft components, fault-injection hardware, and LabVIEW control and logging. Also built DO-160G environmental test rigs with automated LabVIEW.
  - Magnomatics: **dyno-tested prototype magnetically geared motors from 2 to 500 kW**, controlling dynos and inverters in LabVIEW and Simulink, debugging EMI, HV cabling and CAN, designing LV looms, tuning inverters, programming embedded and FPGA position computation, designing test PCBs, and soldering, crimping and wiring looms.
- **He'll probe:**
  - actuator and motor dyno tests in depth (4.2, D1, D4)
  - inverters, EMI, CAN debugging
  - HIL and fault injection
  - data logging; what to automate (4.7)
  - **AI-assisted test design** (his specialism).
- **Your material:** S1 (he built HIL rigs; your "the rig bypassed the stage that failed" point will land), S5 (torque injection is system identification), S11 (your Copilot helper that turns regulation and NCAP text into test scenarios is AI-assisted test design), S7, 4.2, 4.7, 4.17.
- **Be careful:** he has run far more motor dynos than you. Don't bluff dyno details. Say what you'd do and why, say plainly you haven't run a motor dyno yourself, and ask him a good question instead.
- **Rapport question for him:** "How are you using AI agents in test design here? At FiveAI I built a Copilot-based helper that builds test scenarios from regulation and NCAP text, using hand-made building blocks. The hard part was getting people to check its output rather than trust it. How do you keep agent-generated tests trustworthy?"

### What this panel means for you
- Lead with method and evidence, not company facts. Section 8 is background only.
- Every answer needs the data: what you record, at what rate, how you compute the metric, and the pass/fail limit and where it comes from.
- When you don't know, say so, then reason out loud from first principles. Test leads respect that; they spot bluffing at once.

---

## 2. Your openers

### "Tell me about yourself" (technical version, about 75 seconds) ★
"I'm a mechanical engineer with nearly eight years in testing safety-related automotive systems. Three parts are relevant here.

Hardware testing: at AVL I spent about two years on-site at Jaguar Land Rover as feature owner for three corner-radar features. I wrote the requirements and the test cases for each system state, ran them on HiL and ViL rigs, in vehicles and on the proving ground, and analysed the logs in CANoe and CANape. I also worked on AVL's DrivingCube, a real car on a lab test bed: I fitted GNSS ground truth to the car and drove the steering tests on the track that we used to calibrate the simulation. And at the LEVC taxi factory I checked range-extender generators that came back faulty and got the evidence to the supplier.

Test design at scale: for the last five years at FiveAI, now Bosch, I've worked on an L4 driving stack. I built over 120 parameterised test scenarios that generate thousands of test cases, defined the pass/fail KPIs, and built Python tools that make runs repeatable and the results comparable. For a year I led five engineers.

The engineering base: for my BSc I designed and built a 6-DOF Stewart platform. My MSc dissertation designed a test to measure how an electric motor stator heats up, using MotorCAD's thermal model. And I still fix my own cars.

I want to get my hands back on hardware and own a test area. Deciding what good looks like, from one actuator to the whole robot, is exactly that."

### "Why Humanoid?"
"You've moved past demos: proofs of concept at Siemens, Bosch and Schaeffler, a binding deployment at Schaeffler starting in December, and Bosch as your contract manufacturer. The next problem is making every robot that leaves the line as good as the one in the lab. That's a test problem, and it's the part of engineering I enjoy most. The automotive way of scaling, with suppliers, production tests and traceability, is where I come from."

### "Why this role?" (in case they know you first applied for Senior Systems Engineer)
"I applied for the systems role first, but this one fits me better. It's hands-on, it's about test methods and root causes, and it sits where design meets production, which is where my JLR and LEVC work was."

### "Why leave Bosch?"
"FiveAI/Bosch is restructuring and my project is winding down, so the timing is right. But I'd want this role anyway, because I want to get back to hardware." Keep it short and positive.

### "When could you start?"
"I'm in a redundancy consultation at Bosch, so I have flexibility. I expect to be able to start within about two weeks, and I'll confirm the exact date as soon as my leaving date is agreed."
- **Check before Friday:** that leaving early won't cost you the redundancy payment. In the UK, resigning before you're formally given notice of redundancy can lose it. Once you're under notice, leaving early usually needs Bosch's agreement or a written counter-notice given at the right time. Check with HR or your settlement terms (ACAS has a free guide) before you promise a date.

### "Your last five years were simulation. Why should we trust your hands-on skills?" ★ (likely)
"Fair question. My hands-on years were at AVL: rigs, vehicles, the proving ground and the LEVC factory. The last five years built the other half of this job: test methods, KPIs, automation and data at scale. I've kept my hands busy at home with cars and PCs, and I'm deliberately moving back to hardware. I'll need to learn your rigs and instruments quickly, and I will. What I bring from day one is deciding what good looks like and getting the evidence for it."

---

## 3. Your story bank (real examples)

Fill every [CONFIRM] tonight (list in Section 11). Specific details such as speeds, counts and tool names make a story believable.

### Coverage: every JD area has an example

| JD area | Your real example | Worked example (how you'd do it) |
|---|---|---|
| Component test methods | S3 MSc thermal test design, S2 LEVC generator checks | 4.2 actuator plan, D1 spec |
| Subsystem tests | S4 Stewart platform, S10 state-based test cases | 4.3 arm, hand, base, battery |
| Whole-robot tests | S1 vehicle and proving ground, S5 track tests, S6 scenario matrix | 4.4, D3 |
| Prototype bring-up | S4, S5 (readiness checks before each run), new releases on the JLR HiL rig | 4.5 |
| Failure analysis | S1, S2, S8 | 4.6, D2, D3, D4 |
| Documentation others can repeat | S9, S10, S6 templates | D1 |
| Automation inputs and data | S11 (staged generation, errors kept apart from failures, audited passes), S7, S6 | 4.7 |
| Fixtures, jigs, instruments | S4, S3, S5 (fitted GNSS ground truth to the car) | 4.2 rig, 4.10 |
| Production test | S2 (receiving end of escapes), S1 (a rig that passed because it bypassed the failing stage) | 4.8, D5 |
| Quality and design loop | S2, S1 supplier fix | 4.9 |
| Matrix working | S1, S8, S9 | 4.16 |
| Systems thinking | S1, S5 | 4.1 error budget, 4.14 RL link |

### S1 ★★ The radar alert that passed on the HiL but failed on the track (JLR)
**Use for:** failure analysis, test design, systems thinking, rig coverage ("does this rig verify what it should?"), supplier work, "tell me about a time a test failed". Your best story: lead with it.

**Facts (confirmed 29 Oct)**
- **Feature:** Rear Cross Traffic Alert, which also requested braking. Requirement: alert at least 2 s before the collision.
- **HiL (dSPACE):** the real radar modules and their ECUs on the real vehicle CAN network. Simulated objects were fed to the ECUs, bypassing the radar antenna and the radar's own object creation. Every test passed.
- **Proving ground, same tests:** with traffic approaching at 45°, from where the radar wasn't looking directly, we got either no alert and no braking, or an alert about 0.5 s before. Too late to matter.
- **Test matrix (you designed the scenarios, drawn on Miro):**
  - approach angle 30°, 45°, 60°
  - target: walking pedestrian, running pedestrian, vehicle at 10, 20, 30 and 40 mph
  - near side and far side
  - ego reversing speed up to 10 mph in 2 mph steps
- **Method:** coarse grid first → found where failures outnumbered passes → smaller steps around that boundary → detailed logging at the boundary.
- **Logging:** vehicle CAN tapped from one of the main CAN buses; the supplier's tool for the radar's detections, objects and internal state-machine logs (their tooling, needed their permission); a camera for visual reference. All into one data-logging PC.
- **Synchronisation and analysis (confirmed in the mock):** you aligned three time bases (camera timestamps, CAN global time and the radar module's message counter) in CANoe, with a layout showing one panel per stream. You compared the failing run with the **nearest passing run**: with everything else the same except the parking angle, the target reached high confidence much later. Then you narrowed the angle steps to find the exact border.
- **Finding:** comparing the ECU outputs with the supplier's detection and object data showed that, near the edge of the field of view, the radar ignored some targets until late. The HiL had already shown the alert logic worked once it got the object.
- **Fix:** I sent the boundary data, my reasoning and the logs to the supplier. Their engineer came on site and we calibrated live on the proving ground. There were **three calibration candidates**. I ran each through coarse and fine test sets, **including false-alert tests (targets just outside the alert zone, and stationary targets)**, and we chose the best.
- **Close-out:** [CONFIRM: re-test at the boundary passed, defect closed, boundary cases added to the regression set?]
- **Verification:** re-ran the tests around the boundary on the track, plus more variations on the HiL.

**The chain (draw this if you get a whiteboard)**
```
Real world: target → antenna → detections → OBJECT CREATION → alert/brake logic → vehicle CAN
HiL:        simulated objects ───────────────────────────────→ alert/brake logic → vehicle CAN
Failure:    in OBJECT CREATION, the one stage the HiL never exercised
```

**90-second answer** (rehearse out loud)
"At JLR I owned Rear Cross Traffic Alert. The requirement was an alert at least two seconds before a collision. On our dSPACE HiL rig every test passed. But on the proving ground, with traffic coming in at 45 degrees, we got either no alert and no braking, or an alert half a second before: too late to matter.

The HiL result was the clue. On the HiL we fed simulated objects straight into the radar ECUs, bypassing the antenna and the radar's own object creation. So it proved the alert logic worked, but it had never tested the sensor's perception.

I designed a sweep for the track: 30, 45 and 60 degrees; walking and running pedestrians, and vehicles up to 40 miles an hour; both sides; with our car reversing at up to 10. Once I'd found where failures outnumbered passes, I used smaller steps around that boundary and logged it in detail: the vehicle CAN, the supplier's detection and object data, and a camera, all synchronised. Near the edge of the field of view, the radar was ignoring targets until it was too late.

I took that data to the supplier. Their engineer came on site, we ran the boundary tests together, and he recalibrated. I then re-ran the boundary cases on the track, plus more variations on the HiL.

What I took from it: always know which part of the chain your rig actually tests."

**Why it lands at Humanoid (close with one of these)**
- **Rig coverage:** "Every rig is a model of reality with something cut out. Ours cut out exactly the stage that failed. When Manufacturing Engineering shows me a rig design, my first question is which part of the chain it really exercises and which part it bypasses."
- **Robot equivalents:**
  - a whole-body controller tested only in simulation never sees real actuator friction or heat
  - an actuator tested on the dyno with a short lab cable never sees the arm harness voltage drop or cable flex
  - an end-of-line joint sweep without load can't find a gearbox problem that only shows under load
  - a grasp test with new, clean totes never sees worn or wet ones
- **Boundary search:** "Same method for tote handling: sweep weight, offset and rotation, find where success drops, refine there, and repeat runs, because near the boundary results vary from run to run."
- **Layer isolation:** the same method as the "hardware or AI?" drill (D3): compare at each stage of the chain before blaming anyone.

**Numbers behind it**
- 40 mph ≈ 17.9 m/s. A 2 s warning means the alert goes out when the vehicle is still about 36 m from the collision point; 0.5 s is about 9 m.
- 0.5 s is shorter than a driver's reaction time (about 1 s), so the alert is useless. 2 s roughly covers reacting (about 1 s) plus braking from 10 mph (about 0.9 s at 0.5 g). That's physics, not necessarily how JLR set the requirement.
- Full coarse grid: 3 angles × 6 target cases × 2 sides × 5 ego speeds = 180 combinations, before repeats. [CONFIRM how many you ran on the track, and the repeats per point]

**Follow-ups to be ready for**
- *"Why did the HiL pass?"* "It fed simulated objects in after the radar's object creation, so it tested the alert logic, not the sensor's perception. The HiL pass was still useful evidence: it showed the alert logic worked when it got the object, so I could focus on the radar."
- *"How did you find the boundary without testing everything?"* "Coarse grid first, then smaller steps only where the results flipped. Near the boundary results vary run to run, so I repeated runs and defined the boundary as where failures outnumbered passes."
- *"How did you know the alert came 0.5 s before the collision? What was your reference?"* "Two ways, cross-checked. On the track, when the alert or braking fired, we stopped and marked on the ground where the target and our car were, measured the distances and worked out the time from the speeds. In the logs, I found the moment the activation signal fired and took the speeds at that moment. The target ran at a constant speed. Our car's speed could differ slightly from the spec, because at low speed over such short distances it doesn't settle exactly, so I used the measured speed, not the planned one."
  - **Accuracy** (worth volunteering; it's the MSA idea): the shortfall was about 1.5 s. At 40 mph a 0.5 m marking error is only about 0.03 s, so the conclusion was solid. For a walking pedestrian (about 1.4 m/s) the same 0.5 m is about 0.36 s, so near the boundary "I'd trust the logged signal timing more than the ground marks."
  - **Humanoid link:** "Record the actual test conditions, not the planned ones: actual payload, actual temperature, actual speeds. Otherwise manual and automated runs can't be compared."
- *"What exactly did the supplier change?"* "A calibration in their object-creation logic. It's their proprietary software, so I saw the effect, not the code. My part was to prove where and when it failed, and to check the fix."
- *"How did you make sure the fix didn't cause false alerts?"* "The calibration candidates went through our coarse and fine test sets, including tests aimed at false alerts and missed alerts: targets just outside the alert zone, and stationary targets. The supplier also checked false alerts on their side with their own data."
  - **Why they'll ask:** moving a detection threshold always trades missed targets against false alarms, so you need evidence on both sides. You had it.
  - **Humanoid link:** "When a supplier changes a calibration, firmware or a part, I want evidence on both sides: the failure is fixed, and nothing new broke. If Schaeffler changes an actuator's current limit, re-run the torque tests and the thermal tests."
- *"If the HiL bypasses the radar, what did the extra HiL runs prove?"* (a sharp interviewer will spot this) "Regression: that the update hadn't broken the alert logic or anything else on the network. The proof of the fix itself came from the track runs around the boundary."
- *"What was your role?"* "Feature owner. I designed the scenarios and the sweep, analysed the logs, made the case to the supplier, ran the joint tests and checked the fix." [CONFIRM who built the scenarios in dSPACE: you or the HiL team?]
- *"How was the logging connected, and how did you sync it?"* "One logging PC: the vehicle CAN through an interface on a main bus, the radar's detection, object and state-machine data through the supplier's own tool, which needed their permission, and a camera. I aligned the three time bases (camera timestamps, CAN global time and the radar's message counter) in CANoe, with a panel per stream. Then I could line up when the target appeared, when the radar detected it, when it became a confident object and when the alert went out. I don't remember the exact wiring of the supplier's interface; it was their tooling."
- *"What would you do differently?"* "Treat any requirement that depends on the sensor as untested until it has run against the real sensor. So: plan track time early, or use an over-the-air radar target simulator with the sensor turned through the angles. And add the boundary cases to the regression set from the start."

**Background: how this scenario is built in dSPACE** (for your understanding; they're unlikely to ask)
- **The tools:**
  - **ASM (Automotive Simulation Models):** Simulink models of the vehicle, roads, traffic (ASM Traffic includes pedestrians) and sensors, running in real time on the HiL hardware (e.g. SCALEXIO).
  - **ModelDesk:** the GUI that sets up ASM. Road Generator for the road or car park, Maneuver Editor for what the ego car does, traffic scenario editing for the other road users and their triggers, and parameter sets.
  - **ControlDesk:** runs the experiment: dashboards, signal monitoring, recording.
  - **AutomationDesk:** automated test sequences that can run 24/7, linked to SYNECT for test management.
  - **Restbus simulation:** simulates the rest of the car's network so the real ECUs behave as if they're in a car.
  - **Sensor stimulation, three levels:**
    - object lists fed into the ECU (what your HiL did)
    - sensor-realistic simulation (dSPACE AURELION)
    - over-the-air radar target simulators that send echoes to the real antenna (dSPACE DARTS)
  - **Newer:** ASM OpenX with native OpenSCENARIO, OpenDRIVE and OSI.
- **Your RCTA case, step by step:**
  1. Road: a car park with the ego car in a bay, parked cars either side, and the crossing path at 30, 45 or 60°.
  2. Ego manoeuvre: reverse out at a set speed (a parameter).
  3. Target: a pedestrian or vehicle crossing behind at a set speed, from the near or far side, triggered so it reaches the conflict point at the same time as the ego car.
  4. Sensor: an object sensor model at the radar's mounting position with its field of view; the objects go to the ECU over CAN.
  5. Evaluation: log the alert and brake request from the ECU; compute time to collision at the moment of the alert from the model's ground truth; pass if it's at least 2.0 s.
  6. Sweep: AutomationDesk (or a Python script) runs through the parameter grid, records each run and writes the report.
- It's the same structure as your OpenSCENARIO 2 work: road, actors, manoeuvres, triggers, parameters, evaluation.

### S2 ★ Returned range-extender generators at LEVC (factory, hands-on electrical, supplier loop)
**Use for:** hands-on electrical checks, multimeter, motor failure analysis, production and quality loop, suppliers, "closed loop with design".

**Facts (confirmed 29 Oct)**
- As part of AVL, local engineer at the LEVC (London taxi) factory for range-extender generators returned as faulty. About 20 units.
- Followed a predefined procedure: multimeter checks at specified connector pins (phase-to-phase resistance, continuity); powered the control unit from a low-voltage bench supply so the supplier's logging device could connect.
- Connected the supplier's data-logging device to the control unit, ran a predefined command to download the logs (probably including the last stored faults), and saved them.
- Sent measurements and logs to the supplier's engineering team in China.
- Never learned the root causes (that sat with the supplier), but some failures recurred.

**60–75 second answer**
"At AVL I also worked at the LEVC taxi factory as the local engineer for range-extender generators that came back faulty. I handled about twenty units.

My job was to get the supplier the evidence they needed for root cause. For each unit I followed a fixed procedure: multimeter checks at specified connector pins, phase-to-phase resistance and continuity. Then I powered the generator's control unit from a bench supply, connected the supplier's logging device and ran their command to download the stored logs and faults. I sent the measurements and logs, per unit, to the supplier's engineering team in China.

The root-cause analysis sat with the supplier, so I didn't see the final causes. But some failures kept recurring, and that's a signal in itself.

Two things I took from it. Evidence is only useful if every unit gets the same checks and the data is tied to the serial number. And the loop has to close back to where failures are found, so the tests and the design improve. That's what I'd build here: every line failure linked to a serial, a failure code, a root cause, and a change to a test or the design."

**Know the technical "why"** (for follow-ups; don't claim checks you didn't do)
- **Why phase-to-phase resistance:** the three windings should match within a few %. One phase reading low suggests shorted turns; one reading high suggests a broken strand or a bad joint or crimp. Values are small (milliohms to about an ohm), so lead resistance matters. Use 4-wire, or inject a known current from a bench supply and measure the voltage drop (R = V ÷ I). Correct for temperature (copper +0.39%/°C) before comparing with the spec value.
- **Continuity:** windings and connections intact end to end. And no path from a phase to the housing (a short to ground).
- **What else you'd check today:**
  - insulation resistance from phase to housing with a megger (e.g. 500 V DC; expect MΩ to GΩ)
  - temperature sensor resistance against its table
  - resolver windings (excitation, sine, cosine), the usual position sensor on this kind of machine
  - visual: discolouration, burnt smell, oil or coolant ingress, connector damage
  - bearings: noise or roughness turning the shaft by hand, shaft play
- **Logs first:** download stored faults and logs before disturbing the unit, so the evidence isn't lost.

**Follow-ups**
- *"What did you find?"* "The analysis sat with the supplier, so I didn't see the final causes. Some failures recurred across units, which told us it wasn't a one-off." [CONFIRM if you remember the type: same fault code? same symptom?]
- *"What would you do differently?"* "Ask for the findings to come back, and keep a simple tracker: serial, symptom, measurements, fault codes, supplier finding. Then you can see patterns, like a Pareto chart of failure modes, and feed them into incoming inspection or end-of-line tests."
- *"Did you read schematics?"* "I worked from the supplier's procedure and pin list." [CONFIRM]

**Humanoid link**
- Returns from the line or from Schaeffler's sites need the same thing: a fixed triage procedure, data per serial, a closed loop with the supplier (8D), and trends fed into Supply Chain Quality's incoming checks and into design reviews.
- "I've been the person at the end of that chain, so I know what a good triage procedure needs. When a unit fails on the line or at a customer site, the data should already exist."

### S3 Designing a thermal test for a motor stator (MSc, WMG)
**Use for:** thermal testing, test design, sensor placement, thermal models. Be precise: this was test design and modelling, not testing.

**Facts (confirmed 29 Oct)**
- Dissertation: how to find the unknown values of a thermal model of an electric motor stator by testing.
- Used MotorCAD's thermal network (it works like an electrical circuit diagram) to understand the heat paths. [CONFIRM what Portunus and Simulink were used for, if anything]
- Designed the test in detail: where the type-K thermocouples would go, what the enclosure would look like, and the method.
- **The bench was not built within the project.**

**Careful with your CV:** the CV Humanoid has says "experimental testing to find the variables of a thermal model". If the MSc comes up, be precise: "The dissertation designed the test and used the thermal model; the bench wasn't built within the project." Never say you ran the tests.

**60-second answer**
"My MSc dissertation at Warwick was about finding the unknown values in a thermal model of an electric motor stator by testing. I used MotorCAD's thermal network, which works like an electrical circuit: thermal resistances and capacities between the windings, the iron and the housing, with the losses as heat sources. That shows which values are uncertain and matter most, like the path from the copper through the slot insulation to the iron. Then I designed the test to pin them down: where the type-K thermocouples would go, the enclosure, and the method. The bench wasn't built within the project, so I'd call it test design rather than testing. But it's the thinking I'd bring to actuator thermal tests here: understand the heat paths, put the sensors at the hot spots, and design the test to answer a specific question."

**The thermal network in one picture** (know this cold)
- **The analogy:** temperature ↔ voltage, heat flow (W) ↔ current, thermal resistance (K/W) ↔ resistor, thermal capacity (J/K) ↔ capacitor, losses ↔ current sources.
- **Typical nodes:** winding in the slot, end windings, stator teeth, back iron, housing, ambient.
- **Heat path:** copper → slot liner and impregnation (poor conductors, usually the biggest resistance) → teeth and back iron → stator-to-housing contact (an uncertain gap) → housing → air or coolant.
- **Steady state:** ΔT = P × R_th. Example: 50 W of copper loss through 0.8 K/W from winding to ambient gives a 40 K rise.
- **Transient:** like an RC circuit, time constant τ = R_th × C_th. 63% of the final rise after τ, about 95% after 3τ. Windings heat fast (small mass), the housing slowly (big mass). That's why a motor can take peak current for seconds but not for minutes.
- **What you can't calculate well and must measure:** slot insulation and impregnation conductivity, stator-to-housing contact resistance, end-winding cooling. That's what "finding the variables" means.

**How such a test works** (your design plus what a full test adds)
- Type-K thermocouples in the slots (top and bottom), on the end windings at both ends (often the hottest spot), on the teeth and back iron, on the housing, plus ambient. Insulated tips bonded with thermally conductive epoxy, wires routed away from the phases.
- Heat with DC current through the windings. That gives copper loss only (no iron loss), so you know exactly how much heat goes in (P = V × I).
- Average winding temperature from resistance: T_hot = (R_hot ÷ R_cold) × (234.5 + T_cold) − 234.5. This cross-checks the thermocouples.
- Heat to steady state (change below about 1 °C in 10 min), then switch off and record the cool-down. Fit the network values to both curves.
- The enclosure keeps the surroundings repeatable (still air, no draughts), so cooling doesn't change from run to run.

**Follow-ups**
- *"Why wasn't it built?"* [CONFIRM the real reason, e.g. the project's time and scope]
- *"Where's the hottest spot in a motor?"* "Usually the end windings or the middle of the slot. Heat has to cross the slot insulation to reach the iron, and the end windings have no iron around them, only air."
- *"Thermocouple or RTD?"* Type K: small, cheap, wide range, about ±2.2 °C. RTD (PT100): more accurate. Thermocouples next to live windings pick up PWM noise, so use insulated tips and filtering, or heat with DC.

**Humanoid link**
- "An actuator's continuous torque rating is a thermal limit. It's fine for five minutes; the question is minute ninety of a shift. I know the heat paths, where the hot spots are, and how I'd instrument and run a thermal test."
- "A thermal model matched to test data predicts when a joint will derate in a real shift, without running every shift on the robot."

### S4 6-DOF Stewart platform (BSc team project)
**Use for:** robotics, kinematics, building and wiring, bring-up, actuators, CAD. Be precise: the project wasn't finished.

**Facts (confirmed 29 Oct)**
- BSc final-year team project: a 6-DOF Stewart platform (six actuators moving one platform), designed in SolidWorks.
- Actuators: servos (you think) with encoder feedback.
- You wired it yourself and learned Arduino to send commands to each motor.
- You plotted the signals and values to check the actuators did what was commanded.
- Inverse kinematics was attempted in MATLAB, but full pose control wasn't finished. You got to the stage of moving each actuator by the angle you wanted.

**45–60 second answer**
"For my BSc final project, our team designed and built a 6-DOF Stewart platform: six servo actuators moving one platform, designed in SolidWorks and driven from an Arduino. I did the wiring and learned Arduino to command each actuator, and we used the encoder feedback and plotted the signals to check each one went where we commanded. We worked on the inverse kinematics in MATLAB, but we didn't finish full pose control within the project. We got as far as moving each actuator by the angle we wanted. It taught me to bring hardware up one actuator at a time: direction, range and response first, then the whole system. It's also a parallel robot, the opposite of a humanoid's serial arms: easy inverse kinematics, hard forward kinematics."
(The bring-up lesson is a suggested reflection; change it if it doesn't ring true.)

**Inverse kinematics refresher** (relearn today; four lines)
- Base anchor points aᵢ (fixed), platform anchor points bᵢ (move with the platform), i = 1…6.
- Wanted pose: position p = (x, y, z) and rotation R (roll, pitch, yaw).
- Each leg vector: Lᵢ = p + R·bᵢ − aᵢ. Leg length: lᵢ = |Lᵢ|. That's the whole inverse kinematics: closed form, one answer per leg, fast.
- With rotary servos and crank arms, one more step turns each leg length into a crank angle (the triangle formed by the crank, the rod and the leg).
- **Forward kinematics** (six lengths → pose) is the hard direction: no general closed form and several possible poses, so it's solved numerically.
- **Serial arm (HMND-01):** the opposite. Forward kinematics is easy (multiply the joint transforms along the chain); inverse kinematics is harder (several solutions, singularities); errors add up along the chain.

| | Parallel (Stewart platform) | Serial (robot arm) |
|---|---|---|
| Inverse kinematics | Easy, closed form | Harder; several solutions |
| Forward kinematics | Hard, numerical | Easy |
| Stiffness and accuracy | High (loads shared by six legs) | Lower; errors add up joint by joint |
| Workspace | Small | Large |

**Follow-ups**
- *"Why didn't it get finished?"* [CONFIRM the real reason, e.g. time or parts]
- *"What would you do differently?"* "Prove the kinematics in simulation first, and plan bring-up in stages with a check at each: one actuator, then pairs, then the whole platform."
- *"What did you learn about hardware?"* Wiring, servo commands, reading feedback, and that plotting commanded against actual is the first test of any actuator.

**Humanoid link:** "Bring-up is the same on HMND-01 at a bigger scale: one joint at a time, direction, limits, homing and response, before whole-body motion."

### S5 ★ AVL DrivingCube: calibrating the simulation with real track data (AVL)
**Use for:** hands-on testing, instrumentation, ground truth, sim-to-real, controller calibration, test readiness, "your last five years were simulation".

**Facts (confirmed 29 Oct)**
- Project with **AVL DrivingCube**, AVL's vehicle-in-the-loop test bed: a real car on a lab test bed running against a simulated world, with sensor stimulation and full-range steering ("brings the proving ground to the testbed").
- **Simulation:** you built CarMaker scenarios where the ego car drives a circle with a parameterised radius, to see how much steering-wheel torque each radius needs.
- **Instrumentation:** you fitted an external GNSS system to the car to give ground truth for its position during the airstrip tests.
- **Track tests:** you drove while a colleague on the logger injected torque into the steering at set speeds, capturing the vehicle's response to each torque injection.
- **Calibration:** you drove a circuit at HORIBA MIRA (Nuneaton); its corners gave the data to calibrate the PID controller on the simulation side.
- **DrivingCube runs:** you checked readiness before every run: logging healthy, the correct simulation loaded, all systems active.

**75–90 second answer**
"At AVL I worked on a project with AVL's DrivingCube, where a real car runs on a test bed in the lab against a simulated world. For that to be worth anything, the simulation has to behave like the real car, especially the steering.

I worked on both sides. On the simulation side, I built CarMaker scenarios where the car drives circles of different radii, to see how much steering torque each one needs. On the real side, I fitted an external GNSS system to the car for position ground truth, and on an airstrip I drove while a colleague on the logger injected steering torque at set speeds, so we captured the car's response to each injection. Then we drove a circuit at MIRA in Nuneaton, where the corners gave us the data to calibrate the steering PID controller in the simulation.

On the DrivingCube runs themselves I was responsible for readiness: logging healthy, the right simulation loaded, and every system active before we pressed start.

What I took from it: a simulation is only as good as the real data you calibrate it with, and a test run is only as good as the checks before you press start."

**Why it lands at Humanoid**
- **Sim-to-real:** Humanoid trains System 0 entirely in simulation. "I've done that loop: real measurements, calibrate the model, compare again. For a robot, the real measurements are actuator torque response, friction, latency and limits from the bench."
- **Torque injection is system identification:** it's the same idea as torque steps and frequency sweeps on an actuator dyno (4.2).
- **Ground truth:** GNSS on the car is the same principle as a laser tracker or motion capture on the robot. The robot's own sensors can't see their own errors.
- **Readiness checks:** the same as an automated pre-run check for a robot test: nodes alive, topic rates right, no active faults, battery charged, correct software version. A run with bad data is worse than no run.

**Follow-ups**
- *"What's the DrivingCube?"* "AVL's vehicle-in-the-loop test bed: the real car in the lab, with the world simulated and the sensors stimulated, so you can test ADAS repeatably without a track."
- *"Why the external GNSS?"* "Ground truth. To judge the car's or the simulation's behaviour, you need a reference that doesn't depend on the car's own sensors."
- *"How was the torque injected?"* [CONFIRM: from the logging laptop through the power steering over CAN, or a steering robot? Say so if you don't know: your role was driving at the set speed.]
- *"What did you check before each run?"* "That logging was running and healthy, that the correct simulation and scenario were loaded, and that every system was active." [CONFIRM any specifics]
- *"What was the result? How close did the simulation get?"* [CONFIRM. If you don't know: "I wasn't involved in the final comparison report."]

**Background:** AVL describes a steering force emulator on the DrivingCube that gives force feedback from the virtual road. That only feels and behaves right if the steering torque in the simulation matches the real car, which is what this kind of calibration is for.

### S6 ★ Scenario-based testing and KPIs at FiveAI (test design at scale)
**Use for:** test methodology, "where do pass/fail limits come from?", coverage, data, regression, "a time your data found something".

**Facts (confirmed 29 Oct)**
- 120+ parameterised OpenSCENARIO 2 scenarios generating thousands of test cases (Euro NCAP junction tests, UN R79 lane change). KPI and pass/fail criteria, e.g. comfort acceleration and deceleration limits, checked over 1,000+ hours of data. Euro NCAP templates used by others.
- **Where the thresholds came from:** UN R79 or Euro NCAP, and sometimes customer requirements.
- **A real catch:** the KPIs included lane-change success and failure counts and lateral acceleration, with road curvature recorded alongside as a metric. Above a certain curvature, lane-change success dropped, even though the curvature was still within spec. That led to a fix in the steering controller. [CONFIRM your part: did you spot it in the data?]
- **Results that flipped between runs:** if it was a regression, you compared the same test across stack versions to see what had changed, then found the root cause from there.

**60-second answer: "Tell me about a time your test data found something"**
"On the lane-change work for UN R79, our KPIs were lane-change success rate and lateral acceleration, and we also recorded the road curvature for every run. When we looked at success against curvature, it dropped above a certain curvature, even though that curvature was inside the spec the feature had to cover. So it wasn't the scenario being unfair; the feature had a real weakness inside its own operating range. That went back to the developers and led to a fix in the steering controller. The lesson I keep: always record the test conditions next to the results, so you can split the results by condition. A single overall pass rate would have hidden it."

**Follow-ups**
- *"Where did your thresholds come from?"* "Regulation or protocol where one exists (UN R79, Euro NCAP), otherwise the customer's requirements. Here I'd add the robot-level flow-down and data from known-good units (4.1)."
- *"What did you do when results flipped between runs?"* "If it's a regression, run the same test on the old and new stack versions and look at what's different, then root-cause from there. If it flips on the *same* version, it's variability, not a regression: repeat the runs, report a rate rather than one result, and look for the source (timing, initial conditions, randomness)." (The second half is the general method; your confirmed part is the version comparison.)

**Humanoid link**
- "Same as tote handling: record the tote weight, offset, rotation, temperature and battery charge with every run. If success drops above some weight that's still within the payload spec, that points at something real, like a wrist actuator's torque limit or the controller."
- Test matrix language: functional "pick a tote from a stack" → logical "weight 2–15 kg, offset ±50 mm, rotation ±15°, stack height 1–5" → concrete: the actual runs. Coverage comes from the parameter ranges, not from one golden run.

### S7 ★ Tools that removed manual errors and made results comparable (FiveAI)
**Use for:** automation support, data definition, "what would you automate".
- JSON parameter GUI, because parameter combinations were hard to get right by hand.
- Ad hoc scenario config creator for dt_flow runs, because the edit-save-push loop came before knowing whether a new scenario worked.
- Local uploader so local runs reached the dashboards like pipeline runs [CONFIRM exactly what it did]. Pipelines into dashboards. Built with Copilot.
- In your words: "If a step in my workflow is clumsy, I automate it. I find those steps by using the toolchain end to end."
- **Humanoid link:** "Automated runs must produce results comparable to the manual baseline. My uploader solved the same problem: a local run and a pipeline run had to look the same in the results."

### S8 Cross-team triage in the solutions team (ADA with VW Group)
**Use for:** matrix working, influence without authority, root cause across team boundaries.
- Trained partner engineers on our toolchain; founding member of the SimEco solutions team; diagnosed problems across shared toolchains, maps and add-on tools; worked out where the fault really was; got the right team to fix it.
- **Humanoid link:** "When the line reports a failure: is it the part, the process, the rig or the design? Same triage, same need for evidence before blame."

### S9 Leading five engineers (FiveAI)
**Use for:** leadership, teaching, making methods repeatable.
- Technical lead (not line manager) for a year. Taught the tools and evaluation logic; split creation and evaluation so they ran in parallel.
- **Humanoid link:** "A test spec another engineer can run without asking questions. Teaching a team shows you every gap in a method." [CONFIRM a concrete example]

### S10 Requirements to test cases, with signal lists (JLR)
**Use for:** traceability, writing test cases, "how do you write a test spec".
- Use cases → state diagrams → high- to low-level requirements in DOORS/MKS (ASPICE). Signal list for each module traced against the state machine. Test cases per state, traced to requirements; defects in RTC/RQM.
- **Humanoid link:** robot states (off, homing, idle, active, fault, E-stop) each need tests, including every transition.

### S11 ★★ AI-assisted test design: the Copilot scenario helper (FiveAI) (your bridge to Richard)
**Use for:** "how do you use AI?", test automation, test design at scale, "how do you know a pass is real?", initiative.

**Facts (confirmed 29 Oct)**
- **Golden references:** a folder of "perfect" scenario files that never change and hold most of the logic.
- **Context for the AI:** the OpenSCENARIO 2 DSL documentation, plus the whole Euro NCAP protocol as text.
- **A Copilot skill** with the formatting and logic rules, and the method: build modular scenarios to cut repetition.
- **Staged generation:**
  1. The AI plans first.
  2. It creates each scenario with default parameters only.
  3. You run the default set and check every scenario by hand.
  4. Only then add parameterisation.
  5. Then write validation evaluations that run after every scenario execution.
- **Triage in a fixed order:**
  1. **Errors** (the scenario didn't run): usually the stack didn't activate or the DSL syntax was wrong. That usually meant the AI skill hadn't anticipated a parameterisation step, so you improved the skill.
  2. **Failures** (it ran, but the check failed): e.g. for some parameter values the ego car drove off the edge of the map. You fixed the scenario by hand or removed that parameter.
  3. **Random passes, spot-checked:** to catch a "pass" that only happened because an evaluation was missing.
- Used across the project; about ten times more scenario output. **Basis:** a scenario took about a day by hand and about an hour with the helper. Say "roughly an order of magnitude"; it isn't a formal measurement.

**75-second answer**
"I built a Copilot skill that writes OpenSCENARIO test scenarios from Euro NCAP protocols. I gave it a folder of golden scenarios that never change, the DSL documentation, the NCAP text, and rules for formatting and for building modular scenarios. It plans first, then writes each scenario with default parameters only, and I run and check that default set by hand before adding any parameter ranges. Then I add evaluations that run after every scenario.

I triage in a fixed order. Errors first: the scenario didn't run, usually a syntax problem or the stack not starting. That tells me what the skill didn't anticipate, so I fix the skill, not just the file. Then failures: it ran but something was wrong, like the car leaving the map at some parameter values. And then I spot-check random passes, because the dangerous case is a pass that only happened because an evaluation was missing. It gave us roughly ten times more scenarios: one used to take me about a day by hand, and about an hour with the helper. The rule I taught people was: the AI writes, a human verifies."

**The principles to say out loud** (they transfer to robot test automation)
- **Golden references:** known-good examples anchor the generator, like a golden unit on a production rig.
- **Stage it:** generate simple, verify, then add complexity. Never generate the full parameter space before the simple case is proven.
- **Errors and failures are different results:** error = the test couldn't run (rig, infrastructure, syntax); failure = it ran and the product failed. Count them separately, or a broken rig looks like a broken robot. Pytest makes the same distinction.
- **Audit the passes:** a test that can't fail proves nothing. Make checks fail when data is missing ("no data" must not count as a pass), and seed known faults to prove the checks catch them.

**Humanoid link:** "Agent-generated robot tests need the same guard-rails: golden reference sequences, staged generation, errors kept separate from failures, and passes audited with seeded faults. On a robot, a vacuous pass might be a torque check run against an empty log channel."

### S12 ★ Fault-finding on 12 V systems: garage and test vehicles
**Use for:** hands-on electrical, multimeter, systematic fault isolation, "something you fixed", "a module doesn't work: what do you do?".

**(a) Garage: the Mercedes that drained its battery**
- **Car:** Mercedes S-Class V12 Biturbo. You wrote "S900"; Mercedes didn't make one, so it's probably the S600. Check before you name it.
- **Method:** with the car off and asleep, you probed across each fuse with the multimeter to see which circuits were drawing current. Where one fuse showed too much, you traced it to its module and replaced the module. [CONFIRM: which module, and whether the drain stopped]
- **Why it works:** a fuse has a small, known resistance, so current through it shows as a millivolt drop across its two ends. You see which circuit is drawing current without disconnecting anything, so nothing wakes up.

**(b) Work: modules that wouldn't activate on test vehicles** [CONFIRM: JLR test vehicles at AVL, including electrified ones?]
- Not every feature test is a driving test; many are activation and deactivation checks. When a module didn't activate on request, you read the fault codes.
- For a voltage or lost-communication fault: check the fuse for that module. If it had blown, find out *why*. Sometimes that meant taking the module out, powering it from a 12 V bench supply and checking whether it behaved normally.
- **The logic:** does the fault follow the module (module problem) or stay with the vehicle (harness, short, supply)? That's an A/B isolation.
- **What you'd add today:** a **current-limited** bench supply, so a shorted module can't damage itself or blow another fuse; and a check of the harness for chafing or a short to ground near the module.

**60-second answer (b)**
"Many of our feature tests were activation checks, not driving. When a module didn't activate on request, I read the fault codes. If they pointed to a voltage or communication fault, I checked that module's fuse. A blown fuse is a symptom, not a cause, so I'd find out why it blew. Sometimes that meant taking the module out and powering it on the bench from a 12 V supply, to see whether the fault followed the module or stayed with the car's wiring. I do the same at home: I found a battery drain on my Mercedes by measuring across each fuse with the car asleep, and traced it to a module."

**Humanoid link:** "Same workflow when a robot joint won't enable: read the drive's fault code, check its supply and comms, and if a fuse or protection tripped, find out why. Then take the drive or actuator to the bench on a current-limited supply and see whether the fault follows the part or stays with the harness."

### S13 ★ A mistake: the map converter I validated by eye (FiveAI)
**Use for:** "a mistake you made", "a test that gave the wrong answer", "how do you validate your tools?", MSA thinking.

**Facts (confirmed 29 Oct)**
- The simulator used OSM-format maps; the validation tooling that judged the test logs used OpenDRIVE (.xodr). You'd been told conversion was hard because the two formats define geometry differently. [CONFIRM: OSM here = OpenStreetMap or Lanelet2-style .osm?]
- You found an open-source OSM-to-XODR converter, adapted it with Copilot, and converted a batch of maps.
- **The mistake:** you validated the conversion with a visual check and a small set of simple parameterised scenarios. They ran fine through the toolchain.
- **What happened:** later the two validation streams disagreed. The OpenDRIVE-based validator reported "stay in lane" failures. The converted OpenDRIVE lane lines weren't curved like the originals (coarse, straight segments), so on bends the ego appeared to touch the lane marking. They were false failures caused by the conversion.
- **What you'd do now:** test your own fixes more rigorously, understand the maths of how the two formats differ, and ask the subject experts earlier.

**75-second answer**
"At FiveAI the simulator used OSM-format maps, but the tool that validated the test results used OpenDRIVE. I was told converting between them is hard because they describe geometry differently, but I found an open-source converter and adapted it with Copilot. My mistake was how I validated it: a visual check and a small set of simple scenarios, which all passed.

Later the two validation streams disagreed. The OpenDRIVE-based validator started reporting 'stay in lane' failures. The cause was my conversion: on curves, the converted lane lines were coarse straight segments instead of smooth curves, so on bends the car appeared to touch the lane marking. The test tool was producing false failures.

What I changed: I now validate a tool on the cases that stress it, here tight curves, with a numeric acceptance check, like the maximum distance between the original and converted lane lines, not by eye. I make sure I understand the maths behind both formats, and I ask the experts earlier. In hardware terms, I'd trusted a measurement tool without doing an MSA on it."

**The geometry, if they ask why** (it shows you understood the root cause)
- A straight segment of length L across a curve of radius R misses the true curve by up to about L² ÷ (8R) at its middle (the sagitta).
  - 10 m segments on a 50 m radius: about 0.25 m.
  - 10 m segments on a 30 m radius: about 0.42 m.
  - 5 m segments on a 50 m radius: about 0.06 m.
- A 1.9 m-wide car in a 3.5 m lane has only about 0.8 m either side, so a few tens of centimetres of map error easily turns into a "touched the lane marking" verdict on bends, while straight roads look perfect. That's why simple scenarios passed.

**Humanoid link:** "Any tool in the measurement chain needs validating on its hardest cases before you trust its pass/fail: a motion-capture system at the edge of its volume, a log converter that might drop or shift timestamps, a torque transducer at the bottom of its range. And when two measurement streams disagree, suspect the measurement before the product."

### S14 Testing AI output like a test engineer (personal project, in your own time)
**Use for:** Richard, if he goes deeper on AI; "how do you keep up?"; "how do you know an AI tool is good enough?" Keep it short; this is a hardware role.
- **What:** in your own time you're learning applied AI engineering. You built a tool that extracts job adverts into structured data with a local LLM (Qwen2.5 7B on Ollama, on your own GPU), and an evaluation suite for it.
- **What you did:**
  - Hand-written ground truth for three adverts.
  - A scorer with recall and precision for the skill lists.
  - **30 runs per setting**, because one run is misleading.
  - Baseline: must-have skills recall 0.35, precision 0.43.
  - One prompt change ("list each skill separately") raised recall on one advert from 0.27 to 0.65.
  - Calibrated an embedding-similarity threshold on your own matched and unmatched pairs, and rejected an option that narrowed the gap between them.
- **The lessons you can say:**
  - A schema fixes the format, not the content: valid JSON can still be wrong.
  - Never build ground truth from the model's own output.
  - One run proves nothing with a random system.
  - Test empty and edge inputs: with an empty input the model invented an answer.
  - Check that a test can fail: you once wrote an assert that never could.
- **Humanoid link:** "That's how I'd judge an AI-driven test tool, or a policy: ground truth, repeated runs, false passes against false fails, a calibrated threshold. The same discipline as hardware tests."

---

## 4. Question bank with model answers

### 4.1 Test methodology ★

**Q: How do you write a test spec another engineer can run without asking you questions?**
Use a fixed template (full example in D1):
- ID, version, owner, requirement(s) traced.
- Purpose and scope: part numbers, hardware/firmware revisions, what is not covered.
- Safety: hazards, guarding, E-stop check, current limits.
- Equipment with range, accuracy and calibration status; fixture IDs.
- Preconditions: temperature, warm-up, DUT state, zeroing.
- Numbered steps, one action each, with the expected observation and hold points.
- Data: signals, units, sample rates, file naming, metadata.
- Analysis: exact formula, filter, script version.
- Pass/fail: numbers with units and conditions, and what to do on a fail.
- Report: template, and where results are stored.

*"Then I test the spec itself: someone who hasn't seen the rig runs it while I watch. Every question they ask is a gap I fix."*

**Q: Where do pass/fail limits come from?** ★★ (the most important question in this interview)
Five sources, in this order:
1. Flow-down from a robot-level requirement (an error budget).
2. Design intent: datasheets, models, simulation.
3. Data from known-good units: limits around the measured spread, but still inside the design limit.
4. Margins for safety, temperature and ageing.
5. Measurement uncertainty, which sets the guard band.

Example with numbers (systems thinking):
- 1 arcmin of lost motion in the shoulder moves the hand about 0.2 mm on a 0.7 m arm (0.7 m × 0.00029 rad).
- A 10 kg tote at 0.5 m puts 49 Nm on the shoulder. With a joint stiffness of 10,000 Nm/rad that's 0.0049 rad, about 2.5 mm at the hand.
- So if the hand must place a tote within ±5 mm, stiffness matters more than backlash. The error budget tells you which component limit to make tight.

**Q: How do design validation tests differ from production tests?** ★
- **Design validation** asks: does the design meet spec, with margin, across conditions and over its life? Few units, long tests, tests to margin or to failure.
- **Production test** asks: was this unit built right? Every unit, short enough to fit takt, catches assembly and part defects. It doesn't re-prove the design.
- Production limits come from validation data and process spread. Tighten them by the measurement uncertainty (guard band) so a pass really meets spec, but not so much that you scrap good units.
- Example: Kt spec ±5%, rig uncertainty ±1% → production limit ±4%.

**Q: How many units or trials do you need?** ★
- **Pass/fail rates, rule of three:** zero failures in n trials gives about 95% confidence that the failure rate is below 3/n. Claiming 99% success needs about 300 trials without a failure; 99.9% needs about 3,000.
- So ">90% success" from a two-week trial and "99%" are very different claims. 90% vs 99% also means ten times more interventions per hour.
- **Measured values:** test several units, not one golden prototype. 30+ units gives a rough σ; capability studies often use 50+.
- **MSA:** typically 10 parts × 3 operators × 2–3 repeats.

**Q: Verification vs validation?**
Verification: did we build it right (does it meet spec)? Validation: did we build the right thing (does it do the job in the real environment)? An actuator torque test is verification. HMND 01 moving totes for a full shift at Schaeffler is validation.

**Q: Which test design techniques do you use?**
Requirement-based tests; boundary values (your radar story); equivalence classes; corner cases (cold + low battery + max payload); design of experiments when several factors interact; fault injection; endurance; regression after every hardware or software change. Keep a coverage matrix: requirements × tests, and failure modes (from FMEA) × tests.

**Q: How do you document so people can repeat and trust results?**
Spec + raw data + analysis script + versions (hardware, firmware, test software, limits) + rig ID and calibration + photos of the set-up. Anyone should be able to recompute the result from the raw data.

### 4.2 Component level: the actuator ★★ (most likely deep dive)

**Q: "We've got a new joint actuator revision. How would you test it?"**

**What's inside:** motor (PMSM/BLDC); gearbox (strain-wave/harmonic, planetary or cycloidal); output bearing (often cross-roller); encoders on the motor side and output side; driver with field-oriented control; maybe a brake; temperature sensors; comms (CAN FD or EtherCAT).

**The rig ("actuator dyno")**
- Rigid bedplate. Mount the DUT with the robot's real interface (same bolt pattern, similar stiffness).
- Torsionally stiff coupling (bellows or disc) that tolerates small misalignment. Check alignment and runout with a dial test indicator so the rig doesn't side-load the bearings.
- In-line torque transducer with full scale about 1.5–2× the maximum torque you'll measure.
- Load motor (back-to-back dyno that can drive and brake) or a brake. Inertia disc for dynamic tests. Mechanical lock for stiffness tests.
- Reference encoder (or autocollimator) for accuracy tests.
- Programmable DC supply with current limit; bus voltage and current logged; power analyser for efficiency.
- Thermocouples on housing and stator plus the internal sensor; thermal chamber for temperature extremes.
- Guarding, E-stop, interlocks.

**The tests**
1. **Incoming and electrical safety:** visual, serial and revision, phase resistance balance (4-wire), insulation to housing, temperature sensor reads ambient.
2. **Bring-up and functional:** comms, firmware version, encoder direction and plausibility, commutation, brake holds and releases, homing, limits, fault reactions (over-current, over-temperature, over-voltage, comms timeout → safe state).
3. **Performance:**
   - Torque constant (Kt) and linearity: lock the output, step the current, read the torque transducer.
   - Torque ripple and cogging: very slow constant speed, torque vs angle, FFT.
   - Friction: no-load current vs speed, breakaway torque, back-drive torque.
   - Efficiency map: mechanical power out (torque × speed) ÷ electrical power in (V × I) over speed and torque.
   - Speed-torque envelope: peak and continuous, at nominal and at minimum battery voltage.
   - Lost motion (backlash) and torsional stiffness: hysteresis loop (see below).
   - Position accuracy against the reference encoder.
   - Dynamic response: torque and position steps, frequency sweeps → rise time, overshoot, settling, bandwidth.
   - Thermal: continuous torque to steady state; time at peak torque before the limit; derating behaviour; thermal time constant.
   - Regeneration: bus voltage rise when braking hard.
4. **Stress and life:**
   - Endurance with a real duty cycle from robot logs (e.g. the tote-lift torque profile), run 24/7, with checkpoints that re-measure friction, backlash, stiffness and Kt to track wear.
   - Overload and shock: collision, fall, a tote dropped into the hand.
   - Environment: temperature, humidity, dust/IP rating, transport vibration and shock, EMC.
5. **Data:** serial, hardware/firmware revisions, rig ID and calibration, ambient temperature, raw time series (torque/current/position about 1–10 kHz, temperatures about 1–10 Hz), derived metrics, limits version, pass/fail, operator, time. All stored against the serial number.

**Example pass/fail** (illustrative; real values come from the design spec and characterisation data):
- Kt within ±5% of nominal; linear within ±2% of rated torque up to rated current.
- Lost motion < 1 arcmin (strain-wave); stiffness ≥ design value.
- No-load current below the limit at a set speed.
- 60 min at continuous torque with the winding below the insulation limit minus a margin; no faults.
- After endurance: friction and lost motion changed less than an agreed %.

**Why each matters at robot level**
- Kt error → torque and force control error, and a mismatch with the simulator the RL policy learned in.
- Lost motion and stiffness → hand placement error.
- Friction → wasted energy, heat, less back-drivability (matters in collisions).
- Thermal → how long the robot can move heavy totes before it slows down.
- Regeneration → bus over-voltage trips when many joints brake at once.

**Follow-ups**
- *"How do you measure backlash / lost motion?"* Lock the motor side. Apply slowly increasing torque at the output from −X to +X Nm and back. Measure the output angle with a high-resolution encoder, or a lever arm and dial gauge: 1 arcmin on a 500 mm lever is 0.145 mm, easy to see on a 0.01 mm gauge. The torque–angle plot is a hysteresis loop: its width near zero torque is lost motion, its slope is stiffness. Warm up first (grease), and measure the rig's own compliance so you don't blame the actuator for it.
- *"What's cogging?"* Torque ripple from the magnets lining up with the stator teeth, even with no current. You feel it turning the shaft by hand. It causes small speed ripple in slow, precise moves.
- *"Kt vs Ke?"* Torque per amp and back-EMF per unit speed come from the same physics (magnets and windings). Spinning the motor on the dyno and measuring back-EMF is a quick, non-destructive magnet check. Watch definitions: per amp RMS vs peak and phase vs line differ by √2 or √3.
- *"What happens when the motor gets hot?"* Copper resistance rises about 0.39%/°C (about +29% from 25 to 100 °C), so more heat at the same current. NdFeB magnets lose about 0.1%/°C, so Kt drops about 8% at 100 °C. The controller then asks for more current, which makes more heat.
- *"Bearing life?"* L10 ∝ (C/P)³ for ball bearings, so 20% more load means about 42% less life. Endurance tests need realistic loads; over-testing changes what fails.

**Gearbox and bearing cheat card**
- **Strain-wave (harmonic):** ratio about 30–160:1, near-zero backlash, compact. But non-linear stiffness, hysteresis, a small kinematic error, and it can ratchet (teeth skip) under overload; dual encoders catch the sudden offset.
- **Planetary:** efficient, robust, some backlash; about 3–10:1 per stage.
- **Cycloidal:** very shock tolerant, low backlash, heavier.
- **Quasi-direct drive (ratio about 6–10:1):** back-drivable; motor current works as a force sensor; common in legs.
- **Linear:** ball screw or planetary roller screw.
- **Cross-roller bearing:** carries radial, axial and moment loads in one bearing; common at actuator outputs.
- **Bearing failures:** brinelling (impact dents), spalling (fatigue), contamination, wrong preload, misalignment.

**Other components (short answers)**
- **Encoder:** resolution is not accuracy. Compare against a reference over a full turn (a once-per-rev error means eccentricity). Also noise at standstill, temperature drift, magnetic interference from the motor or brake at high current, correct absolute position after a power cycle, latency. 14-bit = 0.022°; 17-bit ≈ 10 arcsec; 19-bit ≈ 2.5 arcsec. Dual encoders: motor side for commutation and speed, output side for the true joint angle; the difference shows lost motion and wind-up.
- **IMU:** six-position static test (each axis up and down) for accelerometer bias and scale; stationary gyro bias and noise; temperature drift; vibration at its mounting point on the robot.
- **6-axis force/torque sensor:** dead weights at known positions to check forces and moments; crosstalk between axes; zero drift with temperature and after overload.
- **Cameras:** calibration (reprojection error); camera-to-body position stays the same after vibration and transport; frame rate and latency (e.g. film an LED flash and compare timestamps); factory lighting (UK mains is 50 Hz, so lights flicker at 100 Hz); dirty lens.
- **Electronics (driver board):** power-up sequencing, rail voltages and ripple, current-sense accuracy, MOSFET temperatures (thermal camera), protections, comms error counters, watchdogs, firmware update and rollback.
- **Structural parts:** proof load (e.g. 1.5× maximum operating load, measure before and after for permanent set), stiffness, fatigue with a realistic load spectrum, critical dimensions (CMM), drop and impact.

### 4.3 Subsystem level

**Q: How would you test an arm?** ★
- **Accuracy and repeatability (ISO 9283):** five points in a cube in the main workspace (P1 at the centre, P2–P5 on a diagonal plane), 30 cycles, at rated load and speed (then lower). Measure with an external reference (laser tracker or motion capture).
  - Repeatability RP = mean distance from the cluster centre + 3σ.
  - Accuracy AP = distance from the commanded point to the cluster centre.
- **Why external measurement:** joint encoders can't see link bending, gearbox wind-up or kinematic calibration errors.
- **Also:** path accuracy (line, circle); static compliance (deflection per kg at full reach); payload at full reach (torque and temperature margins); maximum speed and acceleration; gravity compensation (the arm floats without drifting); joint limits and self-collision; cable flex life through rotating joints.
- **Thermal:** repeat the real task (e.g. one tote lift a minute for two hours) until joint temperatures level off below derating.
- **Power:** peak bus current, and voltage at the wrist joint when all joints accelerate together (margin above the drivers' under-voltage lockout).

**Q: How would you test a hand or gripper?**
- Grip force vs command (load cell); finger position repeatability; closing time; grasp success on a fixed object set (the customer's real totes and boxes); slip and pull-out force (dust, oil, different plastics); tactile and F/T response; cycle life (100k+ open/close); tendon wear if tendon-driven; overload and jamming.
- HMND 01 can use a 5-finger hand (12 DOF) or a parallel gripper.

**Q: How would you test legs and balance?** (bipedal R&D platform)
- **Standing:** the centre of pressure stays inside the support polygon (force plates, IMU).
- **Push recovery:** a calibrated impulse (pendulum or instrumented push stick) at the torso from several directions, increased until it fails → recovery envelope in N·s.
- **Walking:** speed, slopes, steps, uneven and slippery floors; foot impact loads; joint torque and temperature; energy per metre.
- **Falls:** detection and safe-fall behaviour, inspection after falls; early tests on a gantry or harness.

**Q: The wheeled base?** ★ (the commercial product, so likely)
- **Stability:** tip-over margin with 15 kg held at full reach while the base accelerates, brakes and turns.
- **Stopping:** distance at maximum speed with payload, including E-stop.
- **Positioning:** docking repeatability at a workstation (matters for picking), odometry drift, door thresholds and ramps.

**Q: Power and battery?**
- Runtime on a real robot duty cycle against spec (about 4 h reported for HMND 01).
- Internal resistance (pulse test: ΔV ÷ ΔI).
- Voltage sag at peak load at low charge and in the cold, against the drivers' under-voltage lockout.
- Regeneration at full charge and in the cold (the battery can't absorb it → bus over-voltage).
- BMS protections (over/under-voltage, over-current, short circuit, over-temperature), using a battery simulator where possible; state-of-charge accuracy over a shift; pack temperature rise; charging or swapping.
- Power path: pre-charge and inrush, fuses, contactors, DC/DC converters, cable voltage drop, E-stop power-removal timing.
- Standards to recognise: UN 38.3 (transport), IEC 62619 (industrial lithium batteries).

**Q: Torso and head?**
- Waist and lift joints (floor-to-2 m reach means large torques when lifting from the floor), head camera mounts staying calibrated, cable routing, cooling.
- Compute heat: if the Jetson Thor throttles in a hot factory, the VLA slows down and the task slows or fails. A component problem that shows up as robot behaviour.

### 4.4 Whole robot ★

**Q: How would you define system-level tests for the full robot?**
1. **Integration sequence:** power-on → self-test → homing → calibration checks → slow motion through every joint range → full speed → payload → task.
2. **Task tests:** tote handling with KPIs: throughput (totes/h), success rate, interventions per hour, placement accuracy, cycle-time spread, energy per tote, thermal margins. Build the test matrix from parameter ranges (weight, offset, rotation, stack height, lighting), as in your scenario work.
3. **Endurance:** shift-length runs (8 h+, with charging or swapping as designed). Trend temperatures, currents and faults over time.
4. **Failure-mode behaviour:** E-stop, power loss, comms loss between compute and drives, camera dropout or stale frames, a joint fault or derating mid-task, low battery, a slipping tote, a collision, losing the fleet connection. Each needs an expected safe behaviour and a measurement: stopping time and distance, how far the arms drop, whether the tote is held.
5. **Regression:** after every hardware revision or software release, a fixed motion sequence plus the task suite, compared against a baseline.

**Q: The robot fails a task. Is it hardware or AI?** ★★ (full drill in D3)
- Follow the signal chain and compare at each boundary: cameras (rate, timestamps) → System 1 VLA command → System 0 joint commands → drive → actuator → actual motion.
- If the command was wrong but tracked perfectly, look at the policy. If the command was right but a joint didn't follow, look at the hardware: temperature and derating, current limit, bus voltage, encoder disagreement, friction.
- Then replay the same joint commands with the AI out of the loop. If the hardware alone fails, it's hardware.

### 4.5 Bring-up of a new hardware revision ★
1. Read what changed since the last revision. Changed parts get tested first.
2. Before power: visual (fasteners, cables, connectors, clearances); joints move freely by hand where safe; resistance checks on power rails for shorts; polarity.
3. First power: current-limited supply, logic first, then motor power. Watch the current.
4. Check rails, comms (every drive found), firmware versions, sensors plausible (encoders, IMU reads 1 g, temperatures at ambient).
5. E-stop and brakes **before** any motion.
6. Joint by joint at low speed and torque limits: direction matches the model, limits, homing.
7. Whole-body slow sequences, then characterise against design intent, focusing on what changed.
8. Report to design within days: what works, what doesn't, data, photos, next steps.

Your link: first power-up of the Stewart platform [CONFIRM a real moment]; new releases on the HiL rig at JLR.

### 4.6 Failure analysis ★
**Memory hook for every "something failed" question:** Contain → Capture → Compare → Reproduce → Fix → Prevent. (Compare = failing against passing: the nearest pass, sibling robots, bench against arm. The cause is in the differences: load or loss? power or signal?)

**Method (8D style)**
1. **Make safe and preserve evidence.** Don't power-cycle or clear faults before capturing logs and fault codes. Photos. Tag and quarantine the unit.
2. **Describe it precisely.** What, when, how often, which units and revisions. Is / is not: robot 3 but not robots 1–2; only after 2 h; only the right arm.
3. **Check the test before the unit.** Rig calibration, fixture, software and limits versions, steps followed.
4. **Reproduce it**, then change one factor at a time.
5. **Isolate** along the chain. A/B swap: move the suspect part to a good robot. Does the fault follow the part?
6. **Root cause with evidence:** teardown, measure against the drawing, involve the supplier.
7. **Fix and verify:** re-run the failing test and the regression set, on more than one unit.
8. **Prevent:** update the spec, limits, FMEA, work instruction or supplier spec. **Escape analysis:** which test should have caught this, and why didn't it?

**Tools:** 5 Whys; fishbone (people, machine, method, material, measurement, environment); fault tree; Pareto of failure codes.
**Your examples:** S1 (boundary), S2 (evidence to supplier), S8 (which team owns it).

**A robot example to have ready** (hypothetical, present it as an example): "Random EtherCAT dropouts on one arm, only when the wrist rotates past about 90°. The cause is a cable fatiguing inside the rotating joint. At robot level it looks like the arm faulting at random during tote handling. The per-port error counters on the bus point to the segment, and a flex test on the cable confirms it."

### 4.7 Automation ★

**Q: What would you automate, and what stays manual?**
- **Automate:** repeatable steps, numeric criteria, frequent tests (every unit, build or release), long tests (endurance), timing-critical tests (step response), data-heavy tests, high-energy tests (people out of the cell).
- **Keep manual:** first bring-up of a new revision; exploration when you don't yet know what to measure; subjective checks (noise, feel, cosmetics) until they can be defined in numbers; one-offs; rigs that aren't stable yet.
- **Usual path:** manual → scripted analysis (same maths every time) → semi-automatic (manual set-up, automated sequence) → fully automatic.

**Q: What do you hand to the automation team?**
Inputs and DUT state; step sequence with timing; signals, units and rates; analysis with exact formulas and filters; limits with versions; outputs (report, database fields); error handling (never retry a failed hardware test silently); safety interlocks; and an acceptance test for the automation itself: it matches manual results on N units and fails known-bad units.
- **Result states, defined up front:** PASS, FAIL (it ran and the unit is out of limits), ERROR (the test couldn't run: rig, comms, fixture) and INVALID (data missing or out of range). Only PASS counts as a pass. Errors go to the rig owner, failures to the part's owner. That's the lesson from your scenario helper (S11).

**Q: How do you make automated results comparable to your manual baseline?** ★
- Same signals, units, sign conventions, coordinate frames, sample rates, filters and warm-up. One shared metrics library. Same limits.
- Correlation study: run the same units both ways; the differences must sit within the measurement uncertainty.
- Daily golden-unit check on the automated rig.
- Your example: S7 (local runs and pipeline runs had to look the same).

### 4.8 Production test ★

**Words to know**
- **EVT** (engineering validation test): does the design work? Prototypes; find design problems.
- **DVT** (design validation test): does the design meet every spec, including environment, reliability and safety, on production-intent parts? Design freeze at the end.
- **PVT** (production validation test): can the real line build it at rate and quality, with real tooling and test stations?
- **MP:** mass production.
- **Takt time** = available time ÷ demand. **Cycle time** = how long a station takes. The slowest station (the bottleneck) sets output.
- **First pass yield (FPY)** = units passing first time ÷ units tested.
- **Work instruction:** step-by-step operator instructions with pictures, tools, torques and checks.
- **Traveler (router):** the record that goes with each unit through the line, paper or digital: operations done, part serials, measurements, sign-offs, non-conformances.
- **MES:** manufacturing execution system, the production database.
- **NCR:** non-conformance report. **CAPA:** corrective and preventive action.

**Takt example:** two 7.5 h shifts = 900 min a day. Demand 15 robots a day → takt 60 min. A 90-minute end-of-line test needs two test bays in parallel, or the long part moves to a sampled, offline run-in.

**Q: What do you give Manufacturing Engineering for a production rig?** ★
- What it measures (characteristic and range).
- Resolution and accuracy. Rule of 10: uncertainty about a tenth of the tolerance, 4:1 at worst.
- Conditions (temperature, warm-up) and fixturing (datums, repeatable location, no side loads).
- Cycle time target that fits takt.
- Data outputs and database fields, linked to the serial number.
- Pass/fail logic and limits version.
- Operator interface and safety.
- How it will be proved: golden unit, known-bad (seeded-fault) units, MSA acceptance (%GRR below 10%).

**Q: How do you sign off a rig?** ★
"I check it catches what it's meant to catch: MSA on real parts; known-bad units with seeded faults, which it must reject every time; correlation with lab results on the same units; and a check that the data lands in the database against the right serial. A rig that passes everything has proved nothing. My radar story is why I care: our HiL passed every test because it fed objects in after the stage that failed."

**Q: In-process verification?**
- At each station, check what that station could get wrong (from the process FMEA): right parts (scan serials), fastener torque and angle recorded, sub-assembly function (e.g. phase resistance after the motor, drag torque after the gearbox, encoder calibration), connectors seated (bus enumeration), cable continuity.
- Each check has a rework path: what to do, where the unit re-enters the line, the maximum rework loops, then quarantine and NCR. Example table in D5.

**Q: Traceability?**
Serial-number genealogy (robot ↔ actuator serials ↔ boards ↔ battery) plus every result, raw data, rig ID, limits version, software and firmware versions, operator and time, in a database you can query. For example: "show every robot with actuators from lot X whose friction was in the top 10%."

**Q: Final acceptance for a robot leaving the line?**
Visual and labels; power-up and self-test; every sensor; every joint (range, speed, and current signature on a standard motion compared with a golden template); brakes; E-stop and safety functions; calibration check (e.g. hand–eye with a target); battery and charging; a short task run (e.g. 20 tote cycles, zero failures); run-in on a sample if needed; the test record stored against the serial.

### 4.9 Quality: SPC, MSA, FMEA, 8D ★

**SPC (statistical process control)**
- A control chart has a centre line and control limits (±3σ, from the process). These are not the spec limits (from the design).
- Act on: a point outside 3σ; 7–9 points in a row on one side; 6 points rising or falling in a row.
- **Cp** = (USL − LSL) ÷ 6σ: could the process fit? **Cpk** = min(USL − μ, μ − LSL) ÷ 3σ: does it fit, given where it's centred? 1.33 is a common minimum; 1.67 for critical or new processes.
- Worked example: Kt nominal 0.100, spec ±5% (0.095–0.105), measured μ = 0.101, σ = 0.001. Cp = 0.010 ÷ 0.006 = 1.67. Cpk = min(0.004, 0.006) ÷ 0.003 = 1.33. Being off-centre cost capability.
- In this role: trend incoming actuator data per lot (friction, Kt, backlash) and raise a drift before parts start failing.

**MSA (measurement system analysis): is the measurement good enough?**
- Bias, linearity, stability, repeatability (same operator, part and gauge), reproducibility (different operators).
- **Gauge R&R:** e.g. 10 parts × 3 operators × 2–3 repeats. %GRR below 10% good; 10–30% maybe acceptable; above 30% not. Number of distinct categories at least 5.
- **Bosch's own method** (Booklet 10, similar to VDA 5): Type 1 (one reference part measured about 25–50 times → Cg and Cgk ≥ 1.33); Type 2 (with operator influence, like Gauge R&R); Type 3 (automated rig, no operator influence, e.g. 25 parts × 2 runs). Worth knowing because Bosch will build HMND 01.

**FMEA**
- Design FMEA and process FMEA: failure mode → effect → cause → current prevention and detection controls → severity, occurrence, detection → RPN (S × O × D) or AIAG-VDA action priority (high/medium/low).
- For a test engineer, detection controls are tests. The FMEA tells you what to test and where.
- Honest line: "I took part in an FMEA at AVL for a lane change feature." [CONFIRM your role: contributor or facilitator, design FMEA or a safety analysis] "In this role I'd use the design and process FMEAs to decide what each test must detect."

**8D:** team; problem description; containment; root cause (why it happened and why it escaped); corrective action; implement and validate; prevent recurrence; close.

**Supplier quality**
- SCQ owns incoming inspection, PPAP (control plan, PFMEA, MSA, capability, dimensional results), first article inspection and AQL sampling.
- Your part: define the system-level characteristics the actuator must meet (Kt range, friction, lost motion, stiffness, thermal performance, encoder accuracy, plus the test conditions), so SCQ and Schaeffler can turn them into incoming and supplier EOL checks. Then correlate: measure the same units on Schaeffler's rig and on yours.

**Closed loop with design**
Example: "Actuators with friction in the top 10% run 8 °C hotter in tote handling and derate earlier → tighten the incoming limit, or change the design." Take trends to design reviews with data.

### 4.10 Mechanical and metrology

**Your real experience (use it)**
- Calipers and micrometers: you used them to set up and calibrate your own tools so they cut straight.
- Torque wrench: car and bicycle repairs, and checking the control-arm fasteners on a test vehicle. [CONFIRM: at AVL?]
- Wiring and soldering: wired your car's sound system; soldered motor drive cables onto a PCB.
- Not done: load cells or torque transducers, Gauge R&R, insulation testing.

**Tools**
- **Digital caliper:** 0.01 mm resolution, about ±0.02–0.03 mm accuracy; fine for tolerances of about ±0.1 mm or wider. Measure near the base of the jaws, use steady pressure, zero it first.
- **Micrometer:** 0.001 mm resolution (digital), about ±0.002 mm; for tolerances around ±0.01 mm.
- **Dial test indicator:** runout, alignment, flatness on a surface plate.
- Height gauge and surface plate, gauge blocks, pin gauges, feeler gauges, calibrated torque wrench, CMM for GD&T, laser tracker or motion capture for robot accuracy.
- **Rule of 10:** the measuring tool should be about ten times better than the tolerance. ±0.05 mm tolerance → micrometer, not caliper.
- **Temperature:** aluminium grows 23 µm per metre per °C (steel about 12). A 100 mm aluminium part grows 2.3 µm for every °C.

**Sensors**
- **Load cell:** strain gauges in a Wheatstone bridge, output in mV/V, needs excitation and an amplifier. Errors: side loads, temperature, creep, hysteresis, overload. Calibrate with dead weights, use roughly 10–90% of the range, zero it first.
- **Torque transducer:** rotary (in-line, spinning) or reaction (static). Couplings keep bending loads off it.
- **Thermocouple (type K):** wide range, fast, about ±2.2 °C, needs cold-junction compensation, picks up motor PWM noise. **RTD (PT100/PT1000):** accurate (about ±0.15–0.3 °C), use 4-wire. **NTC thermistor:** sensitive, non-linear, cheap, common inside motors. **Thermal camera:** set the emissivity; shiny metal reads wrong.
- **Data acquisition:** sample at least twice the highest frequency (Nyquist), in practice 5–10 times, with an anti-aliasing filter; all channels on one clock or trigger.

**Words**
- Accuracy (close to the true value) vs precision or repeatability (close to each other) vs resolution (smallest step shown).
- Hysteresis: a different reading going up than coming down.
- Calibration: compare with a traceable standard (e.g. a UKAS lab) and record or adjust the error. Verification: check it's still within tolerance.

**Drawings and fits**
- First-angle projection (UK and Europe) vs third-angle (US). Sections, ± tolerances, surface finish (Ra).
- Fits: H7/g6 clearance (sliding), H7/k6 transition (location), H7/p6 interference (press fit, e.g. a dowel or bushing). Bearing seats use the fits the bearing maker recommends.

**GD&T from zero** ★★ (a must-have in the job ad; learn it today)
- **What it is:** Geometric Dimensioning and Tolerancing, a symbol language on drawings.
  - A ± tolerance only says how big a feature may be. GD&T says how flat, straight, round, square or precisely placed it must be, and *relative to what*.
  - The US standard is ASME Y14.5. Europe uses ISO GPS (ISO 1101) with the same symbols; at university you may have learned it as "form and position tolerances".
- **Three ideas carry everything:**
  1. **Datums:** the reference surfaces you measure from, normally the ones that locate the part in the assembly (e.g. A = the mounting face, B = a locating bore or spigot, C = a side or a pin hole). Drawn as a letter in a box attached to a small triangle on the surface. A (primary) touches at 3 points, B (secondary) at 2, C (tertiary) at 1. Together they fix all six degrees of freedom.
  2. **Feature control frame:** a box read left to right: `[symbol | tolerance | datums]` → "this feature's [property] must be within [tolerance] relative to [datums]". A Ø in front of the tolerance means a cylindrical zone.
  3. **Tolerance zone:** the space the real surface or axis must stay inside. For example, flatness 0.05 means the whole surface lies between two parallel planes 0.05 mm apart. **Basic dimensions** (numbers in a box) are exact; the tolerance comes from the frame instead.
- **The symbols in five groups:**

| Group | Symbols | Datum needed? |
|---|---|---|
| Form | flatness ⏥, straightness ⏤, circularity ○, cylindricity ⌭ | No |
| Orientation | parallelism ∥, perpendicularity ⊥, angularity ∠ | Yes |
| Location | position ⌖ | Yes |
| Runout | circular runout ↗, total runout ⌰ | Yes (an axis) |
| Profile | profile of a line ⌒, profile of a surface ⌓ | Usually |

- **MMC (Ⓜ, maximum material condition):** the feature at its "most material" size (smallest hole, largest shaft). With Ⓜ, the position tolerance grows as the hole gets bigger (bonus tolerance), because a bigger hole still fits the bolt. This is what makes a simple go/no-go pin gauge possible.
- **Read these four aloud** (an actuator example):
  - `[⏥ | 0.05]` on the actuator's mounting face: "flat within 0.05 mm, all points between two parallel planes 0.05 apart. No datum, because it's form."
  - `[⊥ | Ø0.02 | A]` on the output shaft: "the shaft's axis must lie inside a 0.02 mm cylinder perpendicular to the mounting face A."
  - `[⌖ | Ø0.1 Ⓜ | A | B | C]` on the six flange bolt holes: "each hole's axis must sit inside a 0.1 mm cylinder at its exact position from A, B and C, with bonus tolerance as the hole gets bigger."
  - `[↗ | 0.03 | A-B]` on a bearing seat: "spin the part on the A-B axis; the dial indicator may vary by at most 0.03 mm at any section."
- **How it's checked:** CMM (coordinate measuring machine); a surface plate with a height gauge and dial indicator; V-blocks or centres for runout; functional gauges for MMC position.
- **Why a test engineer cares** ★
  1. **Failure analysis:** high friction or heat in one actuator? Check the measured geometry (runout, perpendicularity, bearing-seat shape) against the drawing. Misalignment side-loads bearings, causing friction, heat, wear, then torque and thermal problems at robot level.
  2. **Fixtures:** "A test fixture should locate the part on its datums, the same surfaces the assembly uses. Then the test measures what the robot will see, and results repeat from part to part."
- **Honest line:** "I read drawings with dimensions and tolerances, and I've refreshed the GD&T symbols. I haven't specified GD&T on drawings myself." [CONFIRM whether your Ege technical drawing course covered form and position tolerances]

**Mechanical design points**
- **Fasteners:** torque ≈ 0.2 × clamp force × diameter (dry steel). About 90% of the torque goes into friction, so torque is a poor measure of clamp force. Production lines use torque-and-angle tools and record every joint.
- Also know: bearing preload; stiffness vs strength; fatigue at stress concentrations; different expansion of aluminium and steel; sealing and IP rating.

### 4.11 Electrical ★ (your weakest must-have: be honest and fluent)

**Reading a schematic**
- Symbols: resistor, capacitor, inductor, diode, MOSFET, op-amp, connector. Reference designators (R12, C5, U3, J1). Nets and net labels, power symbols, test points (TP).
- Start with the power tree: battery → fuse → contactor and pre-charge → DC bus → DC/DC converters (e.g. 48 → 24 → 5 → 3.3 V) → loads. Then follow one signal from connector to chip.

**Multimeter**
- Voltage across, current in series (mind the fuse), resistance only with power off, continuity, diode test.
- Low resistance (motor windings about 0.1–1 Ω): use 4-wire (Kelvin). 2-wire test leads add about 0.1–0.2 Ω.
- **Parasitic drain hunt (you've done this; S12):** a battery goes flat with the car off, so something is drawing current while asleep. Two methods:
  - **Ammeter in series** at the battery negative: start on the 10 A range (wake-up current), wait for the modules to sleep (can take 10–45 min on modern cars), then pull fuses one at a time until the current drops. That circuit holds the faulty load. A healthy sleep current is typically tens of mA.
  - **Millivolt drop across each fuse** with everything left in place: any fuse showing a drop has current flowing. Nothing gets disconnected, so the modules stay asleep.
  - **Humanoid link:** "A system-level symptom (flat battery in the morning) traced to one component (a module that doesn't sleep). On a robot: battery drain while docked, or standby current per board."
- **Voltage-drop test under load** (not done yet; know it): with the circuit working, measure the voltage across a cable, connector or switch. A good connection drops almost nothing (tens of mV). A high drop means a bad crimp, corrosion or a loose terminal. It finds faults a resistance check misses, because it tests the connection at real current.

**Insulation testing from zero** (you haven't done it; know the idea)
- **Purpose:** prove there's no leakage path from the conductors (motor windings, cables) to the metal housing or chassis, and between circuits that must stay separate. Damaged winding enamel, a nicked cable, moisture or dirt create such paths, giving shorts to the frame, shock risk and failures later.
- **Why a multimeter isn't enough:** it applies only a few volts. A weak spot that only breaks down at hundreds of volts looks perfect on a multimeter.
- **Insulation resistance test ("megger"):** applies a DC test voltage (e.g. 250, 500 or 1000 V, chosen for the system voltage) between the conductors and the housing, measures the tiny leakage current and shows the resistance. Good insulation reads hundreds of MΩ to GΩ. A low or falling value means damage, moisture or contamination.
- **Hipot (dielectric withstand) test:** applies a much higher voltage for a set time (seconds in production, a minute in type tests; the product standard sets the level, e.g. IEC 60034-1 for motors). Pass if the leakage current stays below a limit and nothing breaks down. A standard end-of-line test for motors, harnesses and power electronics.
- **Safety:** high voltage, so use an interlocked enclosure and trained operators, and discharge the part afterwards (windings hold charge like a capacitor).
- **Where it fits here:** actuator end-of-line (phase to housing), harness checks, battery isolation. In D5 it's the "insulation resistance or hipot" check after the motor station.

**Oscilloscope** (say: "I haven't used one professionally; here's how I'd use it in this role")
- Basics: volts per division, time per division, trigger (edge and level; single-shot for intermittent events), 10× probes (compensate them on the calibration square wave), short ground lead, bandwidth 3–5 times the signal, FFT, persistence mode for glitches.
- Safety: the probe ground is mains earth. For floating points (motor phases, high-side shunts) use a differential probe or an isolated scope. Current probes: Hall-effect (DC and AC) or Rogowski (AC only).
- Uses here: bus voltage droop during peak torque; inrush at power-up; ripple on supply rails; CAN signal quality; encoder signals; brake coil current; E-stop timing (button press to torque off and brake engaged).

**Power integrity**
- Droop = I × R. For example, 40 A through 0.1 Ω of harness, connectors and battery loses 4 V. Low charge and cold add more sag. If the drivers' under-voltage lockout is close, joints reset during heavy lifts. Corner case worth testing: low charge + cold + all joints accelerating at once.
- Inrush (capacitors charging) → pre-charge circuits. Regeneration → bus voltage rises when joints brake (worst at full charge). Also ripple, ground bounce, brown-out resets.

**Signal integrity**
- **CAN:** two 120 Ω terminators → 60 Ω between CAN_H and CAN_L with power off (120 Ω means one is missing). Recessive: both about 2.5 V. Dominant: CAN_H about 3.5 V, CAN_L about 1.5 V (about 2 V difference). Short stubs, twisted pair; check error frames and error counters in the logs.
- Noise from motor PWM coupling into sensor lines; shielding and grounding; ground loops; connectors that go intermittent under vibration; cable flex fatigue in moving joints.

### 4.12 Fieldbus and embedded
- **CAN:** up to 1 Mbit/s, 8-byte payload; the lowest ID wins arbitration, so low-priority messages can be delayed (not deterministic under load).
- **CAN FD:** up to 64-byte payload with a faster data phase (several Mbit/s), same arbitration.
- **EtherCAT:** one Ethernet frame passes through every drive "on the fly", and each drive reads and writes its own part. Distributed clocks keep drives in sync to well under a microsecond. Cycle times of 1 ms or faster are normal. Diagnostics: working-counter errors, lost frames, and CRC error counters per port, which point to the exact bad cable or connector.
- **Drive profile CiA 402** (over CANopen or EtherCAT): switch-on disabled → ready to switch on → switched on → operation enabled, plus quick-stop and fault states. Test every transition, including fault reset.
- **What to test:** cycle time and jitter, command-to-motion latency, error counters over long runs, behaviour when a cable is pulled, watchdog timeouts and the safe reaction, noise immunity next to motors.
- **Embedded:** record the firmware version per serial. Calibration data stored in the actuator (encoder offsets, Kt) must be written and checked at production test.
- **HMND 01 timing (public):** System 1 VLA predicts at 5–10 Hz; each prediction is a chunk of actions at 30–50 Hz, executed by System 0 at 50 Hz. Joint-level current and position loops on the drives typically run much faster (kHz).
- **Honest line:** "My bus experience is CAN at signal and log level in CANoe and CANape. I haven't used EtherCAT. I understand why robots use it: deterministic timing across many joints."

### 4.13 ROS 2 for a test engineer
- **Nodes** (processes), **topics** (publish/subscribe streams), **services** (request/reply), **actions** (long tasks with feedback), **parameters**, **launch files**.
- **QoS:** reliable vs best effort (sensor topics are often best effort, so drops can be by design), history depth, durability.
- **ROS 1 vs ROS 2:** ROS 1 has a central master (roscore); ROS 2 uses DDS discovery, QoS and better real-time support. ROS 1 Noetic reached end of life in 2025.
- **Bags:** `ros2 bag record`, `info`, `play` (MCAP format by default in recent versions). Bags are test evidence.
- **Tools:** `ros2 node list`, `ros2 topic list/echo/hz/info -v`, rqt_graph, PlotJuggler, Foxglove, RViz2, tf2.
- **ros2_control:** hardware interface (talks to the actuators) plus controllers (e.g. joint trajectory controller).
- **How you'd use it:** health checks in tests (nodes alive, topic rates, timestamps); bags as evidence with metadata; Python analysis of bags; automated tests with launch_testing and pytest.
- **Honest line** ★: "I've used a ROS 1 Noetic-based set-up as a user: a VLA model in Docker, bridged with rosbridge to our simulator and orchestrator, and Foxglove to look at results. I haven't written ROS nodes. For validation, ROS 2 would be my data backbone: bags as evidence, topic rates and latency as health checks, Python on top."
- After the drill in Section 10 you can add: "This week I ran ROS 2 in Docker and practised checking topic rates and recording bags."

### 4.14 Robotics basics
- **HMND 01:** 29 DOF excluding end effectors; the 5-finger hand has 12 DOF.
- **Serial arm:** links in a chain, so errors add up along it. Forward kinematics is easy, inverse kinematics is harder (several solutions). **Parallel robot** (your Stewart platform): the opposite; stiff and accurate, small workspace.
- **Jacobian:** maps joint speeds to hand speed. Its transpose maps a force at the hand to joint torques (τ = Jᵀ F), e.g. the torques needed to hold 15 kg. **Singularities:** some hand motions need huge joint speeds; keep test paths away from them or test them on purpose.
- **Control loops:** current (fastest) → velocity → position. Impedance or torque control for soft contact. Gravity compensation. Feedforward.
- **Legged balance:** support polygon, centre of pressure / ZMP, capture point, whole-body control.
- **RL and hardware testing** ★ (a strong point for Humanoid): System 0 is trained only in simulation (about 15,000 hours of experience), normally with randomised physical parameters. Hardware testing feeds that in two ways:
  1. Actuator characterisation (friction, Kt, backlash, latency, torque limits) keeps the simulator honest.
  2. The unit-to-unit spread you measure in production must stay inside the ranges the policy was trained on, or an outlier robot behaves differently.
  It's the same idea as calibrating the CarMaker model to real recordings (S5).
- **Wheeled mobile manipulator:** keep the combined centre of mass inside the wheelbase, including when accelerating with an extended payload.

### 4.15 Safety basics
- **E-stop vs protective stop. Stop categories (IEC 60204-1):** 0 = cut power immediately; 1 = controlled stop, then cut power; 2 = controlled stop, power stays on. A legged robot or a loaded arm can't just drop: category 1 with brakes, or a safe crouch or fall.
- **Safe torque off (STO)** in the drives; spring-applied brakes that hold when power is lost.
- **Standards to recognise:** ISO 12100 (risk assessment); ISO 13849-1 (performance levels a–e); IEC 62061 (SIL); ISO 10218-1/-2 (industrial robots, revised 2025); ISO/TS 15066 (contact limits for collaborative robots); ISO 3691-4 (driverless industrial trucks, relevant to the base); ISO 25785-1 (in development, for industrial robots that actively balance); EU Machinery Regulation 2023/1230 (applies from January 2027).
- **The test engineer's job:** measure safety functions with evidence: response time, stopping distance, contact force, brake hold.
- **AI and safety** (relevant for a robot run by a VLA and RL policy): under the Machinery Regulation, machinery whose safety functions rely on self-learning (ML) behaviour needs third-party conformity assessment. The common design answer is to keep safety functions in a conventional, certified safety controller, independent of the policy. Separately, the EU AI Act treats AI that is a safety component of machinery as high-risk, with those obligations due from August 2027.
- **Certification path in one line:** risk assessment (ISO 12100) → safety functions to a performance level (ISO 13849) → robot standards (ISO 10218, ISO 3691-4) → electrical (IEC 60204-1) and EMC → technical file → declaration of conformity → CE mark (UKCA in Great Britain). **ISO 9283 is a performance test method, not a safety standard.**
- **Your link:** trained in ISO 26262 and SOTIF; wrote ISO 26262 requirements for a lane change feature.

### 4.16 Behavioural and matrix questions
- **"Influencing without authority."** S1 (as an AVL contractor between JLR and the supplier) or S8.
- **"You disagree with Manufacturing Engineering about a rig."** "It's their rig to design and build. I'd go back to what it must verify, show data (MSA, seeded faults, correlation), offer options, and agree acceptance criteria for the rig itself. I'd only escalate, with data, if we couldn't agree."
- **"Design says your test is too strict."** "Maybe it is. I'd check where the limit came from and the measurement first, then show the robot-level consequence. If a limit can't be traced to a need, I'd relax it."
- **"Pressure to pass a unit before a deadline."** "I don't change a limit to make something pass. If the business wants to ship with a known issue, that's a documented deviation signed off by the risk owner, with a mitigation. 'We accepted a risk' and 'the test passed' are different facts."
- **"Too many requests."** Prioritise by risk (severity × likelihood) and schedule impact, and make the trade-off visible to the programme lead.
- **"Designs change every month."** Modular test methods under version control. Characterise first, freeze limits later, improve with data.
- **"Why should we hire you?"** "I define tests with numbers and traceability (JLR, FiveAI). I find root causes across boundaries (radar, LEVC, the solutions team). I make tests repeatable by other people and by automation. Where I'm newer, your instruments, your robot and production test, I'll learn fast and be honest about what I know."
- **"First 30–90 days?"** "Weeks 1–2: learn the robot and the lab, join bring-up, read the existing test docs and the failure history. Then pick the highest-risk area with you, probably actuator acceptance for the Schaeffler parts or robot acceptance for the Schaeffler deployment. Write or upgrade the spec, run it on several units, set limits from data, and hand it to automation. By month three: production test requirements for the Bosch line (in-process and end-of-line), MSA on the rigs, and per-serial traceability."

### 4.17 Reading test data: pattern → likely cause → next check ★ (expect a plot or a "what would you think if…")

| What you see | Likely causes | Next check |
|---|---|---|
| Torque ripple repeating a fixed number of times per revolution | Cogging (set by the slot and pole count), gear tooth mesh | FFT against shaft rotation; does it change with load? |
| Position error once per revolution | Eccentricity, encoder or coupling runout | Dial indicator runout; compare with the output encoder |
| Sudden step offset between motor and output encoders | Strain-wave ratcheting, a slipping coupling, a loose clamp | Check the coupling and fasteners; repeat under the same overload |
| Current spike at every direction change | Stiction or backlash; controller saturating | Friction against speed; lost-motion test |
| Temperature still rising with no sign of levelling off | Cooling path problem, overload, or the test is shorter than 3τ | Is the rate of rise falling? Compare with the expected τ and the loss estimate |
| Same part runs hotter than its siblings | Higher friction or loss (preload, grease, misalignment) | No-load current and drag torque; compare with lot data |
| Overshoot and ringing on a step | Under-damped loop, a compliant coupling, a resonance | Ringing frequency against the rig's resonance; lower the gain |
| Bus voltage dips exactly when joints accelerate | Harness, connector or battery resistance | Voltage at the source and at the load (drop = I × R); compare with under-voltage lockout |
| Noise that follows the PWM frequency or its harmonics | EMI coupling into sensor lines | Shielding and grounding; move cables; spectrum with a near-field probe |
| Dropouts only at certain joint angles | Cable flex damage, a connector under strain | Wiggle test while watching error counters; flex test |
| Slow drift at standstill | Sensor drifting with temperature, rig warming up | Log temperature next to it; warm up before testing |
| Results differ by rig, operator or day | Measurement system, not the part | MSA: Type 1 study, Gauge R&R, a golden unit on each rig |
| A rise in failures that follows a part lot or a date | A supplier or process change | Stratify by lot, station and shift; check the change log |

### 4.18 Environmental and EMC testing basics (in case Max or Richard goes there)
- **Environmental (IEC 60068-2 series):**
  - cold (-2-1), dry heat (-2-2), damp heat (-2-78 steady, -2-30 cyclic), temperature change and thermal cycling (-2-14)
  - vibration: sine (-2-6), random (-2-64); shock (-2-27)
  - Aerospace uses DO-160 for the same kinds of test.
- **Ingress (IEC 60529):** e.g. IP54 means dust protected and splashing water.
- **EMC for industrial equipment:**
  - Immunity: IEC 61000-6-2. Typical tests: ESD (61000-4-2, about ±4 kV contact and ±8 kV air), radiated RF (-4-3, about 10 V/m), fast transients (-4-4), surge (-4-5), conducted RF (-4-6), power-frequency magnetic field (-4-8).
  - Emissions: IEC 61000-6-4 / CISPR 11.
- **Why it matters on a robot:**
  - Motor drives switch fast (high dV/dt), the biggest internal noise source.
  - Operators touching the robot (ESD); nearby welders and variable-speed drives in the factory; Wi-Fi for the fleet link.
- **Pre-compliance:** near-field probes and a spectrum analyser on the bench before paying for the accredited lab.
- **Accelerated testing:**
  - HALT: step up stress to find weak points in design.
  - HASS: screen production units with milder stress to catch build defects.
  - Rule of thumb for temperature acceleration: reaction-driven ageing roughly doubles every 10 °C (Arrhenius). Use it with care.
- **Honest line:** "I know these standards and why they matter. I haven't run EMC or environmental tests myself. I'd plan pre-compliance early, because a failed EMC test late in DVT is expensive."

---

## 5. Whiteboard drills

### D1 ★ Write a test spec: actuator torque constant, linearity and hysteresis
All numbers are illustrative. Practise writing this from memory on paper once today.

**TS-ACT-003, version 0.1**

| Field | Content |
|---|---|
| Purpose | Check Kt and torque linearity of actuator P/N xxx against design spec DS-ACT-001, and measure hysteresis. Traced to REQ-ACT-012 and REQ-ACT-013. |
| Scope | P/N xxx, hardware rev C or later, firmware 1.4 or later. Not covered: thermal and dynamic tests (TS-ACT-005, TS-ACT-006). |
| Safety | Guard closed. E-stop checked before starting. Supply current limit at 1.2× the test maximum. Drive torque limit at 110% of rated. |
| Equipment | Bedplate BP-01. Output lock LF-02. Torque transducer ±200 Nm, ±0.1% of full scale, calibration in date. DC supply 60 V / 50 A. DAQ at 1 kHz or faster, synchronised with the drive log. DC current clamp for a cross-check. Thermocouple on the housing. Script `kt_staircase.py` v1.2. |
| Preconditions | Ambient 23 ± 3 °C. DUT at ambient for at least 2 h. Warm-up: 5 min at 30 rpm unloaded (settles the grease). Transducer zeroed with no load. Output locked (4× M8 at 25 Nm). |
| Steps | 1. Mount the DUT (6× M6 at 10 Nm, cross pattern). Check coupling runout is below 0.02 mm with a DTI and record it. 2. Power the logic. Record serial and firmware; confirm no active faults. 3. Enable torque mode. 4. Run the script: 0 → +100% rated current in 10% steps, 3 s each, back to 0, then 0 → −100% and back. Repeat 3 times. 5. Abort on any fault, torque above 110% of rated, or housing above 60 °C; record it and tell the test owner. 6. Disable. Save raw data as `<serial>_TS-ACT-003_<date>_<run>`. |
| Data | Time, commanded current, measured current (drive and clamp), output torque, motor and output encoder angles, bus voltage, housing temperature, all at 1 kHz. Metadata: serial, revisions, rig ID, calibration dates, ambient, operator, script and limits versions. |
| Analysis | For each step, take the mean of the last 2 s. Kt = slope of a least-squares fit of torque against current (0–100%). Linearity = largest deviation from the fit, as % of rated torque. Hysteresis = largest up/down difference at the same current, as % of rated. Repeatability = Kt spread over the 3 runs. |
| Pass/fail | Kt within ±5% of nominal. Linearity ≤ 2%. Hysteresis ≤ 3%. Kt spread over 3 runs ≤ 0.5%. No faults. On a fail: re-check the set-up and repeat once. If it fails again: FAIL, quarantine the unit, raise a ticket with the data attached. |
| Uncertainty | ±0.1% of 200 Nm = ±0.2 Nm. That's 0.2% at 100 Nm (25:1 against the ±5% tolerance), but 2% at 10 Nm, so the fit relies on the upper steps. |
| Report | Plot and table generated automatically; result written to the database against the serial. |

Why the details matter: the warm-up (friction depends on grease temperature), three repeats (repeatability), abort criteria (safety), file naming and versions (traceability), the uncertainty line (you know your measurement is good enough).

### D2 ★ "End-of-line repeatability failures went from 1% to 8% this week. What do you do?"
1. **Contain:** hold the affected units. Has anything already shipped?
2. **Check the test first:** golden unit on the rig; calibration; any change to the rig, fixture, software, limits or operators? Re-test a few failed units on another rig.
3. **Stratify the data** by station, shift, operator, part lot, supplier and date. SPC charts: a sudden step or a slow drift?
4. **If it follows a part lot** (e.g. a gearbox lot): quarantine the lot, A/B swap a suspect actuator into a good arm, measure lost motion and stiffness on the bench, involve SCQ and the supplier.
5. **Fix and verify;** release the lot only with data.
6. **Escape analysis:** why didn't incoming inspection or the actuator EOL test catch it? Add or tighten that check.

### D3 ★★ "The robot drops a tote on cycle 85. The AI team blames hardware, hardware blames AI."
1. **Preserve:** logs and bags for the minutes around the event, fault codes, video. Don't power-cycle first.
2. **Line up timestamps** across camera, System 1, System 0, drive and actuator data.
3. **Boundary 1, sensors → System 1:** were the frame rate and timestamps fine as the hand approached?
4. **Boundary 2, System 1 command → actual motion:** commanded hand pose against actual (from encoders and kinematics).
   - The command missed the handle but was tracked perfectly → policy or perception.
   - The command was right but a joint lagged → hardware: temperature and derating after 84 heavy lifts? Current at its limit? Bus voltage sag? Motor and output encoders diverging (slip, ratcheting, a loose fastener)? Grip force dropping?
5. **Replay** the same joint commands with the AI out of the loop. If it still fails, it's hardware.
6. **Reproduce on the bench** (arm rig or actuator dyno at the same temperature and load), fix it, and add the check to regression.

Close with: *"Whether it's a corner radar or a robot hand, I look at time-aligned data at each boundary before blaming anyone."*

### D4 "Your lab rig and the production rig disagree on Kt by 6%."
- Measure the same units on both rigs first.
- Then check definitions and conditions: per amp RMS vs peak, phase vs line (√2 and √3 mix-ups); torque at the motor vs the output (gear ratio, whether friction is included); temperature (6% is roughly 50–60 °C of magnet heating); warm-up state; current measured by the drive vs an external probe; transducer calibration; rig compliance; filtering.
- Agree one method, write it into both specs, and run MSA on both rigs.

### D5 In-process checks for actuator → arm assembly (example)

| Station | What can go wrong | Check | Data stored | On fail |
|---|---|---|---|---|
| Kitting | Wrong part or revision | Scan serials against the BOM | Part ↔ assembly serial | Swap the part |
| Motor | Winding damage, wrong connection | Phase resistance balance (4-wire); insulation resistance or hipot | Values | Reject to supplier, NCR |
| Gearbox fitted | Wrong preload, damage, dirt, misalignment | Drag torque or no-load current; noise/vibration; lost motion | Values, spectrum | Re-seat and re-test (one loop maximum) |
| Fasteners | Under- or over-tightened | Torque and angle per bolt from a traceable tool | Per bolt | Replace the bolt, re-torque |
| Encoder and driver | Offset not calibrated, wrong firmware or parameters | Calibration routine; firmware and parameter checksum | Offsets, versions | Re-flash, re-calibrate |
| Actuator EOL | Performance | Kt at 3 points, friction, lost motion, temperature sensor, brake hold, fault reactions | Metrics and raw data | Rework by failure code, or NCR |
| Arm assembly | Pinched cable, connector not fully home | Bus enumeration; continuity; joint sweeps with current signature against a golden unit | Per joint | Inspect, rework |
| Arm calibration | Kinematic offsets | Poses measured with a tracker or vision target | Offsets | Re-calibrate |
| Robot EOL | Integration | Full acceptance (4.8) | Everything | Rework path by failure code |

### D6 "How many tote cycles to claim 99% success?"
About 300 cycles with zero failures gives roughly 95% confidence of at least 99% success (rule of three). With failures, use a binomial confidence interval. Report interventions per hour too, not just a percentage.

### D7 ★★ "A new actuator revision arrives on Monday. The design review is Thursday. Walk us through your week." (an execution question)
- **Before Monday:**
  - Get the change list from design (what changed and why) and the risks it creates.
  - Book the rig; check the calibration dates; prepare the scripts and the data template.
  - Agree with design which questions Thursday must answer.
- **Monday:**
  - Incoming checks on every unit (aim for at least 3): visual, serials and revisions, phase resistance balance, insulation.
  - Safe bring-up: logic power first, current-limited supply, comms, firmware version, encoder direction, brake, fault reactions.
  - Mount the first unit on the dyno.
- **Tuesday:**
  - Characterise what changed first, then a short regression of the key characteristics: Kt and linearity, friction, lost motion and stiffness, step response.
  - **A/B test against the previous revision on the same rig, the same day, with the same script**, so differences come from the part, not the set-up.
  - Start an overnight thermal soak on one unit.
- **Wednesday:**
  - Analyse the thermal run. Repeat anything odd on a second unit before calling it.
  - If something fails: contain it, check the test first, and start root cause with the design engineer.
  - Write the report: results against limits, deltas against the old revision, plots, open risks.
- **Thursday (review):** one page:
  - pass/fail against spec
  - what changed against the old revision, with data
  - what we didn't test yet and the risk that leaves
  - recommendation: release to arm build, hold, or release with conditions
  - the next tests (endurance, environment).
- **The principles they're listening for:** test what changed first; same rig, same script, same conditions for comparisons; several units, not one; check the test before blaming the part; state the untested risk out loud.

---

## 6. Numbers card ★ (memorise)

| Item | Value |
|---|---|
| 1 arcmin | 1/60° = 0.29 mrad → 0.29 mm per metre of lever |
| 1° | 17.5 mm per metre of lever |
| Deflection, torque | deflection = lever × angle; torque = mass × 9.81 × lever |
| Copper resistance | +0.39% per °C; T_hot = (R_hot ÷ R_cold) × (234.5 + T_cold) − 234.5 |
| NdFeB magnets | about −0.1% per °C → Kt about 8% lower at 100 °C than at 25 °C |
| Motor | torque = Kt × I; mechanical power = torque × ω (1000 rpm = 104.7 rad/s); electrical power = V × I |
| Thermal time constant τ | 63% of the final rise after τ; about 95% after 3τ |
| Measurement | rule of 10; 4:1 at worst |
| Capability | Cp = (USL − LSL) ÷ 6σ; Cpk = min(USL − μ, μ − LSL) ÷ 3σ; 1.33 / 1.67 |
| Gauge R&R | below 10% good, 10–30% maybe, above 30% no; distinct categories ≥ 5 |
| Rule of three | 0 failures in n trials → failure rate below 3/n (95%) |
| Takt | available time ÷ demand |
| Bearing life | ∝ (C/P)³ ball, (C/P)^(10/3) roller |
| CAN | 60 Ω across CAN_H–CAN_L with power off; dominant about 2 V differential |
| Sampling | at least 2× the highest frequency (Nyquist); 5–10× in practice |
| Bolts | torque ≈ 0.2 × F × d; about 90% of torque goes into friction |
| Expansion | aluminium 23 µm/m/°C; steel about 12 |
| ISO 9283 | 5 points, 30 cycles; RP = mean distance + 3σ |
| Encoder bits | 14-bit = 0.022°; 17-bit ≈ 10 arcsec; 19-bit ≈ 2.5 arcsec |
| HMND 01 timing | System 1 VLA 5–10 Hz (actions 30–50 Hz); System 0 50 Hz |

---

## 7. Honest gaps and how to answer them ★

| Gap | Nearest real experience | What to say |
|---|---|---|
| Oscilloscope | Multimeter (LEVC, cars), logger data, CANoe/CANape | "Not professionally. My electrical diagnosis has been multimeter and logger based. Here's what I'd use a scope for in this role: bus droop under peak torque, inrush, CAN signal quality, E-stop timing. I'd get on the lab scope in week one." |
| Production test and EOL rigs | LEVC factory returns; supplier fixes at JLR | "I haven't owned production tests. I've been on the receiving end of escapes at LEVC, so I know what evidence matters. I know the concepts (takt, travelers, in-process checks, MSA), and I'd lean on ME and Production Ops for their practice." |
| SPC/MSA hands-on | KPI analysis over 1,000+ hours of data | "I know the methods and the maths; I haven't run a formal Gauge R&R. Running one on the first rig would be one of my first jobs." [CONFIRM] |
| GD&T | Mechanical degree, SolidWorks, technical drawings | "I read drawings with dimensions and tolerances, and I've refreshed the GD&T symbols. I haven't specified GD&T on drawings myself." Learn 4.10 "GD&T from zero" today. |
| Insulation / hipot testing | Multimeter checks at LEVC | "I haven't done insulation or hipot tests. I know what they're for: proving there's no leakage path from the windings to the housing at well above the working voltage, which a multimeter can't show." |
| Fixture design at work | Stewart platform build; MSc test design (sensor placement, enclosure; not built) | "My build experience is the Stewart platform and my own repairs. My MSc designed a thermal test set-up, though it wasn't built within the project. ME owns production rig design; my job is the requirements and the sign-off." |
| Robotics at work | Stewart platform; autonomous vehicles | "Autonomous vehicles are robots on wheels: sensors, perception, planning, actuation, the same test problems. And HMND 01 Alpha is on wheels too." |
| EtherCAT | CAN logs in CANoe/CANape | See 4.12. |
| ROS 2 development | ROS 1 as a user (VLA in Docker + rosbridge), Foxglove | See 4.13. |
| Xray / TestRail | RTC/RQM, DOORS, MKS, Jira | "Same idea: test cases linked to requirements and defects. I've used RTC/RQM and Jira." |
| FMEA | Took part in one at AVL for a lane change feature | "I took part in an FMEA at AVL for a lane change feature. Here I'd use the design and process FMEAs to decide what each test must detect." |
| "5+ years hardware test" | About 3 hardware-heavy years at AVL + 5 years of test design | The "why trust your hands-on skills" answer in Section 2. |

---

## 8. Company facts (checked 29 Oct 2026)

**Company:** Humanoid (SKL Robotics Ltd), founded in 2024 by Artem Sokolov. London HQ, offices in Boston and Vancouver, 200+ engineers.

**HMND 01 Alpha Wheeled** (the commercial robot):
- Built in 7 months. Hardware designed "simulation-first": actuator selection, joint strength and mass distribution optimised virtually.
- Reported specs: about 2.2 m tall, about 300 kg, 29 DOF excluding end effectors, about 15 kg payload, omnidirectional base at about 7.2 km/h, about 4 h battery, NVIDIA Jetson Thor compute.
- Sensors (official page): RGB, depth, 6D F/T sensors, haptic feedback. End effectors: 5-finger hand with 12 DOF, or a parallel gripper.

**HMND 01 Alpha Bipedal:** research and development platform aimed at service and household use.

**KinetIQ** (four-layer AI stack):
- System 3: fleet agent; assigns tasks, talks to facility systems.
- System 2: robot-level reasoning (omni-modal language model), seconds to under a minute; checks whether System 1 is making progress and asks for human help.
- System 1: VLA predicting at 5–10 Hz; each prediction is a chunk of actions at 30–50 Hz.
- System 0: RL whole-body control at 50 Hz, trained only in simulation (about 15,000 hours of experience).
- KinetIQ Ascend: real-world learning by trial and error. Simulation and training on NVIDIA Isaac Sim and Isaac Lab.

**Proofs of concept**
- Schaeffler: PoCs and a strategic partnership (announced January 2026).
- Martur Fompak with SAP (Jan–Feb 2026): totes from a pallet to a trolley. Martur Fompak is a Turkish automotive seating supplier, a small personal connection if it comes up.
- Bosch, Bühl (March 2026): five box sizes from conveyors to a trolley.
- Siemens, Erlangen (announced April 2026): two-week trial, 60 tote moves per hour, 8 h+ uptime, over 90% pick-and-place success.

**Schaeffler deal (13 May 2026)**
- Binding, phased deployment and supply agreement, Robot-as-a-Service (maintenance, 24/7 support, updates included).
- First phase December 2026 to June 2027 at two German sites: Herzogenaurach (box handling in live production) and Schweinfurt (three months of capability demonstration and integration testing, then three months validating stable, continuous operation near full production scale).
- Target: a four-digit number of wheeled units across Schaeffler's sites by 2032.
- Separate 5-year actuator supply agreement: Schaeffler becomes preferred supplier for more than 50% of joint actuators for the wheeled platforms through 2031.

**Bosch deal (May 2026):** contract manufacturing partner for Europe, with a design-for-excellence framework (manufacturability, reliability, serviceability, cost). Bosch actuators, drives and sensors may be integrated in future versions.

**Reported:** a Beta version reaches customers in Q4 2026.

**What this means for the role**
1. EVT → production with Bosch: production test definitions (in-process, EOL, traceability) are needed now.
2. Schaeffler actuators (over half of the wheeled platform's joints): incoming performance characteristics, and correlation between Schaeffler's EOL tests and yours.
3. The Schaeffler deployment from December includes a "stable continuous operation" phase: per-robot acceptance and endurance evidence.
4. System 0 is trained in simulation: actuator characterisation and production spread feed the simulator and the policy's robustness.
5. Bosch components may come in later: second-source qualification using the same test methods.
6. Wheeled first: base stability with payload, battery runtime over a shift, docking repeatability.

Sources: thehumanoid.ai (Alpha Wheeled page; Schaeffler release, 13 May 2026); The Robot Report (KinetIQ; Siemens PoC; Bosch and Schaeffler partnership); roboselect360.com HMND 01 page (checked 13 Oct 2026).

---

## 9. Questions to ask them (pick 3–4; one per person is ideal)
**For Dmitrii (test lead):**
1. How do you define the gates between EVT, DVT and PVT here, and which subsystem goes through DVT first?
2. When a robot has an incident at a customer site, like Schaeffler, how does that data flow back into the test methods?
3. What would make the first 90 days a success for this role?

**For Max (standards and mechatronics):**
4. Coming from BSI, how much are you designing tests with certification in mind already, e.g. ISO 10218 or the Machinery Regulation from 2027?
5. How do you handle measurement uncertainty and calibration on the lab rigs today?

**For Richard (automation and AI):**
6. How are you using AI agents in test design, and how do you keep agent-generated tests trustworthy? (Give your Copilot-helper context first; see 1b.)
7. Is there a full-robot HIL or an "iron humanoid" rig with real actuators and emulated loads, like your Iron Bird at Vertical?

**For anyone:**
8. For the Schaeffler actuators, who owns the actuator end-of-line test today, and how will you correlate their data with yours?
9. When a task fails, how do you separate hardware issues from policy issues today? Is there a standard data set you capture?
10. How do the test, test automation and quality teams split the work today?

---

## 10. Today and tomorrow
*(The original plan from this morning; for the rest of today use Section 13. The ROS 2 drill below is still valid if you have time.)*

| Time | Do |
|---|---|
| 09:30–10:00 | Sections 0 and 1. Say the opener out loud three times; record yourself on your phone. |
| 10:00–11:30 | Fill every [CONFIRM] (Section 11). Then tell S1, S2 and S6 out loud in 90 seconds each. |
| 11:30–13:00 | 4.1 and 4.2, then write D1 from memory on paper. |
| 13:00–13:45 | Break and a walk. |
| 13:45–15:00 | 4.6, 4.8 and 4.9, plus D2, D3 and D5. Do the Cpk and takt sums on paper. |
| 15:00–15:45 | 4.10, 4.11 and Section 7. |
| 15:45–16:30 | ROS 2 drill (below). |
| 16:30–17:30 | Mock interview with me: rapid-fire questions plus two whiteboard drills. |
| Evening | Numbers card, company facts, your questions. Early night. |
| Friday morning | 30 minutes: opener, S1/S2/S6, numbers card. Check camera and mic; have pen and paper ready for sketches. |

### ROS 2 drill (about 45 minutes, uses a public Docker image of about 1 GB)
Terminal 1:
```bash
docker run -it --rm --name ros2drill ros:jazzy-ros-base bash
apt-get update && apt-get install -y ros-jazzy-demo-nodes-cpp
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_cpp talker
```
Terminal 2:
```bash
docker exec -it ros2drill bash
source /opt/ros/jazzy/setup.bash
ros2 node list
ros2 topic list
ros2 topic info /chatter -v      # publishers, subscribers and QoS
ros2 topic hz /chatter           # expect about 1 Hz
```
Terminal 3 (a fake 30 Hz joint command):
```bash
docker exec -it ros2drill bash
source /opt/ros/jazzy/setup.bash
ros2 topic pub -r 30 /joint_cmd std_msgs/msg/Float64 "{data: 1.0}"
```
Back in terminal 2:
```bash
ros2 topic hz /joint_cmd                          # expect about 30 Hz
ros2 bag record -o drill_bag /chatter /joint_cmd  # Ctrl-C after about 10 s
ros2 bag info drill_bag                           # duration, message counts, storage format
```
Done when you can answer: what rate did `hz` show for each topic? What QoS did `info -v` show? Do the message counts in `bag info` match rate × duration (30 Hz × 10 s ≈ 300)? That last check is exactly the kind of thing you'd automate in a test.

---

## 11. Fill in tonight (only you know these)
1. **S1 radar:** done (29 Oct). Optional extras: which combinations failed; how many track runs and repeats; who built the scenarios in dSPACE; what the pedestrian targets were.
2. **S2 LEVC:** done (29 Oct). Optional extras: what the recurring failures looked like; whether you read a pinout or schematic.
3. **S3 MSc:** done (29 Oct): test design and modelling, bench not built. Still needed: why it wasn't built; what Portunus and Simulink were used for.
4. **S4 Stewart platform:** done (29 Oct): team project, not finished; each actuator moved to commanded angles. Still needed: why it wasn't finished. Relearn the inverse kinematics refresher today.
5. **S5 DrivingCube:** done (29 Oct). Still needed: how the torque was injected; the result of the comparison, if you know it.
6. **S6 KPIs:** done (29 Oct). Still needed: your part in the curvature finding.
7. **S7 tools:** what exactly the uploader did; who used the tools; the effect.
8. **S9:** one concrete teaching example.
9. **S12:** done (29 Oct). Still needed: the car model, which module drained the battery, and whether the work part (b) was on JLR test vehicles. **S13:** done (29 Oct).
10. **Hands-on check:** done (29 Oct). Done: calipers and micrometers, torque wrench, parasitic drain hunt, wiring and soldering, FMEA (AVL). Not done: voltage-drop test, insulation test, Gauge R&R, load cells. Learn GD&T today.
11. **Notice period:** done: about two weeks (redundancy consultation). Check that leaving early doesn't affect the redundancy payment before promising a date.
12. **The interview:** done: Technical Execution Interview with Dmitrii, Max and Richard (Section 1b). Still unknown: time, length, any exercise.


---

## 12. Mock interview log (29 Oct)

### Round 1: Richard (rigs, dynos, automation)
| Question | Your score | What was missing | Fix |
|---|---|---|---|
| Characterise a new actuator revision | 5/10 | You asked "what do you mean by characterising?" (it's in the job ad); you described the rig, but not the measurements or how to decide it's good; no safety or bring-up | Purpose → safety → rig → measurements → criteria → robot link (4.2). "Characterise" = measure what it actually does across its range; set limits from that data |
| Kt is 6% below the datasheet | 6/10 | Repeats and averaging catch noise, not bias; no systematic causes | Same definition? (RMS vs peak, motor vs output: gearbox losses), temperature (about 0.1%/°C), current probe cross-check, transducer calibration and alignment, drive limiting, saturation; golden unit and a second unit; then the supplier with data (D4) |
| A joint drops off CAN FD only on fast moves, only on the arm | 5/10 | Missed the "works here, fails there" clue; didn't use your own S12 method | List the differences (harness flex, PWM noise, supply sag, longer network); reset (power) or bus-off (signal)?; correlate with angle and speed; scope the supply and CAN; flex or swap or separate supply; soak test; add error counters to end-of-line |

**Patterns to fix:** answer every part of the question; repeats catch noise, not bias; "works here, fails there" → list the differences; use your stories as evidence; always end with prevention.

**Terms to get right:** an *in-line rotary* torque transducer for a spinning dyno (a *reaction* transducer is for static tests); insulation is checked with a megger, not a multimeter.

### Round 2: Dmitrii (test lead: strategy, gates, ownership)
| Question | Your score | What was missing | Fix |
|---|---|---|---|
| A test failure you owned end to end (S1) | 7/10 | Left out "it passed on the HiL" (your headline); no numbers; too much "we"; no close-out | Open with the requirement (2 s) against reality (none, or 0.5 s), then the HiL-passed clue; say "I"; finish with the close-out (re-test, defect closed, boundary cases in regression) and the lesson |
| Gates from EVT to DVT to PVT | 5/10 | Design freeze is at the end of DVT, not EVT; PVT is a small build proving the line, not "1000 robots"; no entry and exit criteria | EVT: does the design work? DVT: does the production-intent design meet every requirement with margin, then freeze? PVT: can the line build it at rate with proven tests and traceability? Plus an open-issue rule (Section 1b) |
| Over-temperature trip at Schaeffler, never seen in the lab | 6/10 | No containment or evidence preservation; no load-versus-loss split; no serial record; no fleet check | Contain, then preserve the logs; load or loss?; compare with sibling robots and the lab duty cycle; the unit's production record; dyno with the field duty cycle; fleet thermal margins; escape analysis → field-based endurance profile, tighter end-of-line limit, field alert; 8D |

**Patterns:** contain and preserve evidence first; split load from loss for thermal problems; use per-serial traceability (it's in the job ad); every escape ends with a changed test.

### Model answers: Rounds 1 and 2 (study these)

**R1-Q1 [Richard] "A new actuator revision is on your bench. How would you characterise it: rig, measurements, how you decide it's good?"**
> "First I'd ask what changed from the last revision, and get the spec and the old results, so I test what changed first.
> **Bring-up:** visual and serial checks, phase resistance balance, insulation with a megger. Then logic power first on a current-limited supply, comms and firmware, encoder direction, brake, fault reactions, with the E-stop checked before anything moves.
> **Rig:** the actuator on a rigid bracket matching the robot's interface, a disc coupling aligned with a dial indicator, an in-line torque transducer, and a back-to-back load motor. Plus a lock for static tests and an inertia disc for dynamic ones, a reference encoder, and thermocouples. I'd log the actuator's own CAN FD data (current, both encoders, bus voltage, temperature, faults), synchronised with the DAQ.
> **Measurements:** Kt and linearity with the output locked and current steps; friction and no-load current against speed; lost motion and stiffness from a torque–angle loop; position accuracy against the reference encoder; step response; the speed–torque envelope at minimum battery voltage; and thermal: continuous torque to steady state, and how long it can hold peak torque.
> **Deciding it's good:** at least three units, against the spec limits, and A/B against the old revision on the same rig with the same script. Where there's no limit yet, I'd characterise and set limits from the spread, inside the design margin. I'd also check my measurement uncertainty is small compared to the tolerance.
> **Why it matters at robot level:** Kt drives force accuracy and how well the simulator matches; lost motion and stiffness set hand placement; thermal sets how long it can move heavy totes in a shift."

**R1-Q2 [Richard] "Kt comes out 6% below the datasheet. What do you check before telling Schaeffler?"**
> "Before blaming the part, I'd check the test. First, am I comparing like with like: RMS or peak, phase or line current, motor side or output side? At the output, gearbox losses alone could explain a few percent. Second, temperature: magnets lose about 0.1% per degree, so 6% is like running 60 °C hotter, so I'd check the winding temperature. Third, cross-check the drive's current with a probe, and the transducer's calibration and alignment. Also check the drive isn't limiting, and compare at the datasheet's current level, because Kt drops with saturation. Then run a known-good unit and a second new unit on the same rig. If everything's 6% low, it's my method; if only this one is, it's the part. Then I'd go to Schaeffler with the data and compare methods, ideally by measuring the same unit on both rigs."
- Key idea: **repeats catch noise, not bias.** A steady offset is a bias, so look for a systematic cause.

**R1-Q3 [Richard] "A joint drops off CAN FD only during fast moves on the full arm, never on the bench. How do you go after it?"**
> "The clue is that it only happens on the arm and only on fast moves, so I'd list what's different from the bench: the harness through moving joints, the other motors switching next to it, the supply shared by every joint, and a longer network.
> First I'd find out what kind of drop it is. If the node *reset*, that points to power. If it went error-passive or bus-off, that points to the signal. The fault codes and CAN error counters tell me which.
> Then I'd look for a pattern in the logs: a particular joint angle, speed, or which joints accelerate together.
> Then measure: a scope on the supply at that joint during a fast move, to see if it dips towards the under-voltage limit; and on CAN high and low, to look for noise bursts in step with the PWM. And check the termination reads 60 Ω.
> Then isolate: flex the harness at that joint by hand with the arm still while watching the error counters; swap that cable section; or feed the joint from a separate supply.
> After the fix, a long soak of fast moves to prove it, and I'd add bus error counters to the standard test and the end-of-line check so it can't come back. It's the same logic as my fuse work on test vehicles: the fault code is a symptom; find what's different and isolate it."

**R2-Q1 [Dmitrii] "A test failure you owned end to end: root cause and close-out."** The S1 version in Section 3, told this way:
> "At JLR I owned Rear Cross Traffic Alert. A defect came in from testing: no warning and no braking when a target approached while the car reversed out of an angled parking space. The requirement was a warning at least two seconds before the collision; we got none, or about half a second.
> The interesting part was that the same scenarios had passed on our dSPACE HiL. That was a clue, because the HiL fed simulated objects straight into the ECU, so it never exercised the radar's own detection and object creation.
> I pulled the failing logs: camera, vehicle CAN, and the radar's internal detection and state-machine data. I synchronised the three clocks in CANoe and built a layout with a panel per stream, then compared the failing run with the nearest passing run. With everything the same except the parking angle, the target reached high confidence much later. So I narrowed the angle steps to find the exact pass/fail border. Near the edge of the field of view, the radar held objects as low confidence until they came further in, which was too late.
> I wrote up the evidence and my reasoning and sent it to the supplier with the logs. Their engineer came on site and we calibrated live on the proving ground. We had three candidate calibrations. I ran each through coarse and fine test sets, including false-alert tests with targets just outside the zone and stationary targets, and we chose the best.
> To close it out, [your real close-out]. The lesson: know which part of the chain each rig really tests, and always compare a failure with its nearest pass."

**R2-Q2 [Dmitrii] "When is the arm ready to move from EVT to DVT to PVT?"**
> "I'd define each gate by exit criteria agreed with design and production up front, plus an open-issue rule: no open severity-1 issues, and severity-2 only with an owner and a date.
> **EVT asks 'does the design work?'** It exits when the arm meets its key functions at nominal on several units, we've characterised it against design intent (accuracy, payload, thermal, power), and every major risk from the FMEA has a test or a design change planned for DVT.
> **DVT asks 'does the production-intent design meet every requirement, with margin?'** It exits when every requirement is verified with evidence across the operating range: endurance with enough cycles to make a statistical claim, environmental and EMC, and the safety functions, with pre-compliance for certification. The design, the test methods and the limits are then frozen.
> **PVT asks 'can the line build it repeatably at rate?'** It exits when the production tests are proven (MSA on every rig, seeded faults rejected, results matching the lab), first-pass yield is on target, cycle times fit takt, every unit's results are in the database against its serial number, and supplier parts like the Schaeffler actuators come with their approval evidence.
> **In mass production**, SPC on the key characteristics, and field incidents feed back through 8D.
> My job as test owner is a test plan that says, for each gate, which tests, how many units, which limits and what evidence."

**R2-Q3 [Dmitrii] "An over-temperature trip on a shoulder joint at Schaeffler, never seen in the lab. What do you do?"**
> "First, contain: robot and people safe, the customer kept running, and the logs and fault codes pulled before anyone power-cycles it.
> Then: is it load or loss? Was the shoulder working harder than in the lab, or is this actuator wasting more energy as heat? I'd compare its current, torque and temperature history with the other robots on the same job, and with our lab duty cycle, and check the ambient and the totes. If the others are fine, it's this unit, so I'd pull its production test record by serial (friction, no-load current, Kt), check the temperature sensor is believable, and bring the actuator back to the dyno to run the real field duty cycle.
> In parallel, I'd check the thermal margin on that joint across the whole fleet, so we know if others are close.
> Then the escape analysis: why didn't the lab catch it? Probably our duty cycle or ambient was gentler than reality, or our end-of-line limits let a high-friction unit through. So the fix goes into the tests: an endurance profile built from field logs, a tighter friction or no-load-current limit at end-of-line, and a thermal-margin alert in the field. If it's a design issue, the data goes to design. I'd run it as an 8D so every action has an owner and gets closed."

### Round 3: Max (procedures, measurement, standards)
| Question | Your score | What was missing | Fix |
|---|---|---|---|
| A production grip-force procedure a technician can run without you, where two technicians agree | 5/10 | Generic headings; nothing on reproducibility | Remove judgement (the fixture locates on datums, the rig commands, measures and decides); define every condition; equipment IDs and calibration; reaction plan on fail; results straight to the database; prove it with a dry run, Gauge R&R and a golden unit each shift |
| Repeatability 0.4 mm against a 0.5 mm spec: pass? | 4/10 | Said "yes" straight away; no measurement uncertainty or conditions | Uncertainty first (ISO 14253-1: measured + U inside the limit); ISO 9283 conditions (rated load and speed, 30 cycles, warm-up); same statistic; several arms; guard band; your stack-up point last |
| Which standards apply to HMND-01, and how does that change the test plan? | 3/10 | "Don't know" with no map; called ISO 9283 a certification standard | Honest + map: Machinery Regulation (Jan 2027) and CE/UKCA, ISO 12100, ISO 13849, ISO 10218, ISO 3691-4, ISO 25785-1 (in development), IEC 60204-1, EMC, batteries; test plan: safety-function evidence, early EMC and environmental pre-compliance, technical file; ML-dependent safety functions need third-party assessment |

**Patterns:** "What would you want to know first?" means question the measurement and the conditions before giving a verdict; reproducibility has to be designed in and then proven (Gauge R&R); "I don't know" + the map you'd expect + what it means for testing.

### Model answers: Round 3

**R3-Q1 [Max] "A production grip-force check a technician runs without you, where two technicians get the same answer."**
> "I'd write it so nothing is left to judgement, then prove it.
> It covers the scope, meaning which hand part numbers and revisions; safety, meaning pinch points, the guard and the E-stop; and the equipment with IDs, meaning a calibrated grip-force fixture with its range, accuracy and calibration date, holding the hand on its mounting face so the fingers close on the sensor at the same points every time. Then the preconditions: firmware version, supply voltage, hand at room temperature, sensor zeroed. Then numbered steps with photos: mount the hand, scan the serial, zero, command a grip at the set force, wait two seconds, record the average over the next second, release, and repeat three times. Then the limit with units, what to do on a fail (one retest after re-seating, then quarantine and an NCR), and results going straight into the database against the serial.
> To make two technicians agree, I take the judgement out: the fixture locates the hand, the rig commands and measures, and the software decides. Then I prove it: a dry run by someone who's never seen it, and a Gauge R&R with ten hands, three technicians and a few repeats each, aiming for under 10% of the tolerance. A golden hand at the start of each shift catches drift."

**R3-Q2 [Max] "Repeatability measured ±0.4 mm with a laser tracker; spec ±0.5 mm. Pass?"**
> "Not yet. I'd want three things first. One, the measurement uncertainty. A laser tracker is good to a few hundredths of a millimetre, but target mounting and temperature add to it. If the total is around ±0.03 mm, 0.4 plus that is still inside 0.5, so it's a real pass; if it were ±0.1, I'd call it inconclusive. Two, the conditions: was it measured as the spec defines it, like ISO 9283 with rated payload and speed, 30 cycles, warmed up? Three, how many arms: one arm with 0.1 mm of margin doesn't tell me the design is good, so I'd measure several and look at the spread. If it passes, it's a pass for this unit, and for production I'd add a guard band. And since the arm feeds a bigger error budget with other parts in series, I'd check that 0.5 really comes from the robot-level requirement."
- Background: **ISO 14253-1 decision rule**: conformance is proven only when the measured value plus its uncertainty is inside the specification; nonconformance only when it minus its uncertainty is outside; anything in between is inconclusive.

**R3-Q3 [Max] "Which standards apply to HMND-01 in Europe, and how does that change your test plan?"**
> "I'm from automotive, where my world was ISO 26262 and SOTIF, so the machinery side I'd be learning. But the structure is similar. I'd expect the EU Machinery Regulation from January 2027 and the CE mark; a risk assessment to ISO 12100; safety functions like the E-stop, protective stop and speed limits designed and validated to a performance level under ISO 13849; ISO 10218 for industrial robots; IEC 60204-1 for the electrical side; and industrial EMC. The base looks like ISO 3691-4 territory, and there's ISO 25785-1 coming for robots that balance. ISO 9283 is the performance test method, useful but not a safety standard.
> For the test plan, that means three things. Safety functions get their own verification with evidence: stopping times and distances, brake holding, behaviour on power loss, all measured, not assumed. EMC and environmental pre-compliance early in DVT, so we don't fail at the accredited lab late. And everything traceable into the technical file. One thing I'd flag: as I understand it, under the new regulation, if safety functions depend on self-learning AI, you need a third-party assessment, so I'd want the safety functions independent of the policy."
- Background (don't lead with it): the EU AI Act treats AI that is a safety component of machinery as high-risk, with those obligations due from August 2027.

### Round 4: the panel (execution scenarios)
| Question | Your score | What was missing | Fix |
|---|---|---|---|
| Tote dropped on cycle 85: hardware or AI? | 7/10 (your best) | Following the chain at the moment of the drop (commanded vs actual, grip force); replaying commands with the AI out of the loop; named suspects for "cycle 85"; presenting to both teams together | See the model answer: capture → follow the chain → trend every cycle (what builds up?) → replay without the AI → swap versions → share jointly → add a regression test |
| New actuator Monday, design review Thursday: your week | 6/10 | Change list first; ≥3 units; safety and bring-up; same rig, same script, same day for A/B; overnight thermal soak; state the untested risk; Thursday is a recommendation | D7 and the model answer below |

**Patterns:** with the six steps your answers jumped to 6–7. Keep using them. For planning questions, give days, units, what runs overnight, and what you *won't* know by the deadline.

### Model answers: Round 4

**R4-Q1 [Panel] "Tote dropped on cycle 85; the AI team blames hardware, the hardware team blames the policy."**
> "First, stop and make it safe, and capture everything before anything is reset: logs and bags, fault codes, video, software and hardware versions, ambient, battery charge, and the tote itself.
> Then I'd let the data settle it, not the teams. Two quick checks. One, follow the chain at the moment of the drop: did the cameras deliver frames on time, was the commanded hand pose right, did the joints follow it, did the grip force hold? If the command missed the handle and the joints tracked it perfectly, it's the policy. If the command was right but a joint lagged or the grip faded, it's hardware. Two, why cycle 85 and not cycle 1? Something builds up. So I'd trend every cycle (joint temperatures and derating flags, battery voltage, grip force, tracking error, camera latency, tote position) and compare 85 with 84 and with cycle 1.
> Then reproduce: replay the same joint commands with the policy out of the loop. If it still drops, it's hardware. If this is new, swap versions, old and new policy against old and new hardware, to find which change brought it in.
> I'd share it with both teams together, with the plots. And I'd close it with a test: if the grip force fades as the hand warms up, a thermal soak and grip-force check in the regression suite, so it's caught on the bench next time."

**R4-Q2 [Panel] "New actuator revision Monday; design review Thursday. Your week."**
> "Before Monday, I'd get the change list from design and agree what question Thursday has to answer. That sets my priorities: what changed first, then a short regression of the key characteristics. I'd check what I can reuse from the existing plan and rig, whether the fixture fits the new revision, and whether any requirement changed.
> **Monday:** incoming checks on at least three units, safe bring-up, first unit on the dyno.
> **Tuesday:** characterise what changed, then the regression set (Kt, friction, lost motion, step response), A/B against the old revision on the same rig with the same script. And I'd start an overnight thermal soak, because that won't fit in a day.
> **Wednesday:** analyse, repeat anything odd on a second unit before I call it, and if something fails, check my test first, then start root cause with design. I'd give design a heads-up rather than surprise them on Thursday.
> **Thursday:** one page. Pass/fail against spec, the differences from the old revision with plots, what we haven't tested yet and the risk that leaves, and a recommendation: release to the arm build, hold, or release with conditions."

---

## 13. Study plan: priority and auxiliary (Thursday evening, Friday morning)

### Priority study: must be solid tonight, in this order ★
1. **Six core stories, out loud, 60–90 s each,** using "I", with a number and a lesson:
   - S1 radar (passed on the HiL, failed on the track)
   - S5 DrivingCube (GNSS ground truth, torque injection, readiness checks)
   - S11 AI helper (staged generation, errors kept apart from failures, audited passes)
   - S12(b) fuses ("a blown fuse is a symptom"; bench power to isolate)
   - S13 mistake (validated a tool by eye)
   - S6 curvature finding
   - S2 LEVC as a seventh.
2. **The failure method:** Contain → Capture → Compare → Reproduce → Fix → Prevent. Plus the four rules:
   - "works here, fails there" → list the differences
   - repeats catch noise, not bias
   - load or loss?
   - reset (power) or bus-off (signal)?
3. **Actuator questions:** R1-Q1 (characterise), R1-Q2 (Kt 6% low), and D1, the test spec. Write D1 from memory on paper once.
4. **Execution questions:** R4-Q1 (tote drop, hardware or AI?) and R4-Q2 (Monday to Thursday week).
5. **Gates and production:** R2-Q2 (EVT/DVT/PVT); 4.8 (what to give ME for a rig, how to sign it off, in-process checks, traceability); D5 table.
6. **Measurement:** R3-Q2 (uncertainty and the decision rule), R3-Q1 (procedure plus Gauge R&R); MSA, Cpk and rule of 10 in 4.9 and 4.10.
7. **GD&T from zero** (4.10): read the four example frames aloud until it's easy.
8. **Numbers card** (Section 6).
9. **Openers** (Section 2): tell me about yourself, why Humanoid, why trust your hands-on skills, when can you start.
10. **Questions to ask** (Section 9): pick one per interviewer.

### Auxiliary study: if time allows
- 4.15 safety and certification map (R3-Q3), including the point about AI-dependent safety functions.
- 4.11 electrical: insulation testing, voltage-drop test, what a scope is for, CAN at 60 Ω.
- 4.17 reading test data (pattern → cause → next check); 4.18 environmental and EMC basics.
- 4.2 details: gearbox types, encoder resolution, Kt and temperature, bearing life.
- 4.3 subsystem tests: arm (ISO 9283), hand, wheeled base, battery.
- 4.12 EtherCAT and CiA 402; 4.13 ROS 2 plus the 45-minute Docker drill (Section 10).
- 4.14 robotics basics: kinematics, Jacobian, how the RL controller depends on actuator data.
- S3 thermal network; S4 Stewart platform inverse kinematics.
- Section 8 company facts (background only for this panel).

### Friday morning (30–45 min)
- Say the opener and S1 out loud once each.
- Run the six-step method through one imaginary failure.
- Numbers card; one question per interviewer ready.
- Camera, microphone, water, pen and paper for sketches (the chain diagram, a torque–angle loop, a gate table).

---

## 14. Self-test question bank
Ask me "quiz me on P1" (or P2, P3), and I'll ask these one at a time, score your answer and show the model answer. "Answer in" points to where the model answer is.

### P1: most likely (must answer well)
| # | Question | Answer in |
|---|---|---|
| 1 | Tell me about yourself. | Section 2 |
| 2 | Why Humanoid, and why this role? | Section 2 |
| 3 | Your last five years were simulation. Why should we trust your hands-on skills? | Section 2, S5, S12 |
| 4 | Tell me about a test failure you owned end to end: root cause and close-out. | S1, R2-Q1 |
| 5 | A new actuator revision is on your bench. How do you characterise it? | R1-Q1, 4.2 |
| 6 | Kt comes out 6% below the datasheet. What do you check before telling the supplier? | R1-Q2, D4 |
| 7 | A joint drops off CAN FD only on fast moves on the arm, never on the bench. | R1-Q3 |
| 8 | When is the arm ready to move from EVT to DVT to PVT? | R2-Q2, 1b |
| 9 | An over-temperature trip at a customer site that you never saw in the lab. | R2-Q3 |
| 10 | Write a production procedure two technicians will get the same answer from. | R3-Q1, D1 |
| 11 | Repeatability 0.4 mm against a 0.5 mm spec: pass? | R3-Q2 |
| 12 | The robot drops a tote on cycle 85: hardware or AI? | R4-Q1, D3 |
| 13 | New revision Monday, design review Thursday: your week. | R4-Q2, D7 |
| 14 | Where do your pass/fail limits come from? | 4.1, S6 |
| 15 | What would you automate, and what stays manual? | 4.7 |
| 16 | What do you give Manufacturing Engineering for a production rig, and how do you sign it off? | 4.8 |
| 17 | What do you check at each assembly station, and what happens on a fail? | 4.8, D5 |
| 18 | Tell me about a mistake you made. | S13 |
| 19 | How do you use AI in test design, and how do you trust what it generates? | S11 |
| 20 | Tell me about a time your test data found something. | S6 |

### P2: likely follow-ups
| # | Question | Answer in |
|---|---|---|
| 21 | How do you measure lost motion (backlash) and stiffness? | 4.2 |
| 22 | How would you test an arm's accuracy and repeatability? | 4.3 |
| 23 | How would you test the wheeled base and the battery? | 4.3 |
| 24 | Read these GD&T frames: flatness 0.05; perpendicularity Ø0.02 to A; position Ø0.1 Ⓜ to A, B, C. | 4.10 |
| 25 | What's an insulation test, and why isn't a multimeter enough? | 4.11 |
| 26 | What is Cpk? Work an example. | 4.9 |
| 27 | What is MSA or Gauge R&R, and what result is acceptable? | 4.9 |
| 28 | How many trials to claim 99% success? | D6 |
| 29 | What happens to a motor's performance when it gets hot? | 4.2, S3 |
| 30 | Design says your test is too strict; or you're pushed to pass a unit before a deadline. | 4.16 |
| 31 | Your lab rig and the production rig disagree on Kt by 6%. | D4 |
| 32 | Results flip between runs. What do you do? | S6 |
| 33 | Tell me about an electrical fault you found. | S12 |
| 34 | Which standards apply to HMND-01, and how do they change your test plan? | R3-Q3, 4.15 |
| 35 | What does a HiL not tell you? | S1 |

### P3: auxiliary
| # | Question | Answer in |
|---|---|---|
| 36 | What is EtherCAT, and why do robots use it? | 4.12 |
| 37 | How would you use ROS 2 in testing? | 4.13 |
| 38 | Serial vs parallel robots; how does Stewart platform inverse kinematics work? | S4, 4.14 |
| 39 | Where is the hottest spot in a motor? Explain a thermal network. | S3 |
| 40 | Which environmental and EMC tests would HMND-01 need? | 4.18 |
| 41 | Torque ripple at a fixed number of cycles per rev; current spikes at direction changes; voltage dips on acceleration. What do they suggest? | 4.17 |
| 42 | How would you test a hand or gripper? | 4.3 |
| 43 | Why does an RL controller trained in simulation depend on your actuator tests? | 4.14 |
| 44 | What would your first 30–90 days look like? | 4.16 |
| 45 | What's AVL's DrivingCube, and what did you learn there? | S5 |
| 46 | How do quality gates apply to software and firmware releases? | 1b |
