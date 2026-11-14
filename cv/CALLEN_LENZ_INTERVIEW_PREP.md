# Callen-Lenz – Senior Systems Engineer: Study Pack

**Interview: Thu 12 Nov 2026 · Senior Systems Engineer (Vacancy CLA-294) · Salisbury, on-site · £50–65k**

Source material: `Callen-Lenz Interview Prep Guide.pdf` (Gemini chat), checked against `CANDIDATE_PROFILE_NOTES.md` and a web check on 11 Nov.

**How to use this:**
- **Tonight (about 90 min):** Sections 1–3, then the two refreshers (**Section 4 SOTIF**, **Section 5 FMEA**), then do the self-test in Section 10 out loud.
- **Then (45 min):** run the **mock interview in Section 11** with a timer, recording yourself on your phone. Score each answer and redo anything that scored 0.
- **Then (25 min):** **Section 13 HARA refresher.** Learn the S/E/C tables and the sum shortcut, then do the parking-brake practice out loud.
- **Then (30 min):** **Section 14 feature design.** Learn the **PHISTOV** method, then answer one practice question in 14.12 out loud: draw the states, then say how you'd prove it.
- **Then (30 min):** **Section 12 whiteboard sketches.** Draw the six must-knows from memory on paper while saying the "Say" line out loud.
- **Tomorrow morning (20 min):** Section 0, the pitch, the four stories, the "gap" lines, and your questions.
- The answers are written to be spoken. If you're skimming, read the **bold words**.

---

## 0. Last-look card (read this in the car park)

1. **Callen-Lenz** = UK UAS company near Salisbury, part of **BAE Systems FalconWorks** since 2024. Aircraft: **Nyan** (one-way effector), **Koios** (VTOL ISR), **Fregata** (catapult-launched ISR); own avionics and mission system.
2. **My bridge:** "An uncrewed aircraft is an autonomous vehicle in 6 degrees of freedom with tighter weight, power and radio limits. The systems engineering is the same: requirements, interfaces, safety analysis, staged verification."
3. **My best story:** the RCTA radar that **passed on the HiL but failed on the track** (it's also a textbook SOTIF case, see 4.6).
4. **SOTIF in one line:** hazards when **nothing is broken** but the function isn't good enough (sensor limits, missing spec, foreseeable misuse). ISO 26262 = hazards from **faults**.
5. **HARA in one line:** top-down. Vehicle-level **malfunction × driving situation** → rate **S, E, C** → **ASIL** → **safety goals**. Add them up: 10 = D, 9 = C, 8 = B, 7 = A. Aerospace equivalent: **FHA**.
6. **FMEA in one line:** bottom-up. For each part/function: **how can it fail → what's the effect → what's the cause → how bad (S), how likely (O), how well we'd catch it (D) → act** on the worst first.
7. **Honest gaps (one sentence, then the bridge):** no aircraft / UAV work, no aerospace standards (ARP4754A, ARP4761, DO-178C), no SysML / MBSE tools, no FHA / FTA done myself.
8. **"Design feature X" questions:** use **PHISTOV**: Purpose → Hazards → Inputs → States → Transitions (guard, debounce, hysteresis, priority) → Operator → Verify (state × event table, SIL sweeps, Iron Bird fault injection, build-up flight test). Test that it fires when it should **and doesn't when it shouldn't**.
9. **Ask:** which programme, sim vs Iron Bird vs flight balance, tools (DOORS? Cameo?), SC vs UK Eyes Only.

---

## 1. Company and role (checked facts)

| Item | What to know |
|---|---|
| Who | UAS design, avionics and flight-operations company near Salisbury, Wiltshire, founded 2007. **Wholly owned by BAE Systems since 2024**, part of **FalconWorks** (BAE's rapid-innovation / advanced air power division). |
| **Nyan** | One-way effector (strike drone). Built for contested, **GNSS-denied** environments. Trialled by the Army and Royal Navy. **First launch from HMS Queen Elizabeth**: four Nyans launched by **pneumatic catapult** during **Exercise Neptune Reach B** (Project **VANTAGE**, the "Hybrid Navy" / hybrid carrier air wing idea); all four hit their strike points. Earlier sea launch from **XV Patrick Blackett** (Neptune Reach A). |
| **Koios** | Runway-independent **autonomous VTOL** ISR aircraft, 4 m wingspan, multi-fuel engine, electric lift motors for take-off and landing, then forward flight. |
| **Fregata** | Fixed-wing ISR, 4 m wingspan, **pneumatic catapult** launch, skid landing, **8–12 h endurance**. About **90 % parts in common with Koios** (simpler logistics, maintenance and training). |
| Avionics / software | Own autopilots / flight control, platform management and the **SC3** mission management / ground control system. Payload-agnostic: EO/IR turrets, SIGINT, etc. |
| **Applied Intuition** | **MoU signed at Farnborough 2026** with Applied Intuition UK: AI-enabled autonomous and **collaborative (multi-aircraft) behaviours**, reducing operator workload while keeping human oversight. |
| The role | Reports to the **Systems Engineering Manager**. Full lifecycle systems engineering for **crewed and uncrewed** aircraft across technical services, products and platforms. Works with software, hardware, flight controls and avionics teams. On-site, rural Wiltshire. |
| Must-haves (from the guide) | British citizen, 5+ years UK residence (for SC), full UK licence. You meet all three. |

> [!WARNING]
> **Check before quoting:** the Gemini guide says the HMS Queen Elizabeth launch was on **6 November 2026** ("last week"), that Nyan has a **2.9 m wingspan** and that **over 1,000** were built. I could confirm the launch itself but **not those exact numbers or the date**. One web source called Nyan "jet-powered / low-observable", which doesn't match the Gemini description. Say **"I saw Nyan launched from HMS Queen Elizabeth recently"**, with no date or numbers, unless you've checked them yourself.

---

## 2. Fixes to the Gemini guide (don't say these)

The Gemini PDF is useful but it **overstates** a few things compared with your confirmed notes. Use the corrected version.

| Gemini guide says | Say this instead |
|---|---|
| "Proving-ground **homologation** under **UN R79**" at AVL/JLR | UN R79 was **FiveAI** (KPIs for automatic lane change in simulation). At JLR you did **vehicle and proving-ground verification**, not homologation. |
| "**Owned** verification from SIL… and real-time **HiL/ViL rigs**" / "your dSPACE HiL" | You **wrote the test cases**, tested **in vehicles, on the proving ground and on AVL's DrivingCube ViL**. The **HiL was run by the HiL team**; you analysed why it disagreed with the track. |
| "**Architected** 120+ scenarios" | "**Built** over 120 parameterised OpenSCENARIO 2 scenarios." |
| Diagnosing "**CAN FD, Ethernet**" bugs | **CAN** analysis in CANoe / CANape. The car had FlexRay and Automotive Ethernet but you did no deep work on them. |
| Defect triage in "RTC/RQM **and Jira**" | **RTC / RQM** (Jira isn't confirmed in your notes). |
| "Redundancy concluded **on great terms**" | "VW Group withdrew from the project and my role was made redundant. My last day was 6 November, so I can **start immediately**." |
| "Mechanical **and Systems** Engineer with eight years developing… safety-critical autonomous systems" | Fine to say "eight years in **driver assistance and automated driving** systems". Keep "safety-related" rather than claiming you developed safety-critical software. |
| MSc / BSc (if they come up) | **MSc:** "I designed the test; the bench wasn't built." **Stewart platform:** team project, not finished; each actuator moved to a commanded angle. |

---

## 3. Your pitch, stories and gap lines

### 3.1 The 90-second "Tell me about yourself" (corrected)

> "I'm a mechanical engineer with eight years in driver assistance and automated driving systems.
> From 2018 to 2021 I was at AVL, and I spent about two years on-site at Jaguar Land Rover as **feature owner for three corner-radar features**: Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. I wrote the **use cases, state diagrams and requirements**, broke them down from system to module level in **DOORS and MKS Integrity** under the ASPICE V-model, defined the **signal lists** for each module, and wrote the test cases. Then I verified them **in vehicles and on the proving ground**, working closely with the radar supplier. I also wrote **ISO 26262 requirements** for a lane change feature and took part in its **FMEA**.
> For the last five years I was at **FiveAI, now Bosch**, on an L4 automated driving stack for the Volkswagen Group. I built over **120 parameterised test scenarios**, turned **UN R79 and Euro NCAP** rules into pass/fail KPIs, **led five engineers** for a year, and helped found the solutions team that diagnosed problems across the partners' toolchains.
> VW withdrew from the project and my role ended last week. I want to take the same systems discipline, requirements, interfaces, safety and staged testing, into aerospace. Callen-Lenz stood out: uncrewed aircraft with your own avionics, the Nyan launch from HMS Queen Elizabeth, and the work with Applied Intuition on autonomy."

### 3.2 Four stories to have ready

**S1. HiL passed, track failed (RCTA radar) – your signature story.** Use it for: "a difficult problem", "V&V strategy", "working with a supplier", "SOTIF".
- **Situation:** RCTA with braking request; requirement: alert **at least 2 s before collision**. All HiL tests passed. On the proving ground at a **45° approach** there was no alert, or an alert only ~0.5 s before.
- **Why the HiL missed it:** the HiL fed **simulated objects** straight into the ECUs, **bypassing the antenna and the radar's object creation**. The fault was in exactly the stage the rig didn't exercise.
- **What you did:** designed the test matrix (approach 30/45/60°; walking / running pedestrian, vehicle 10–40 mph; near and far side; ego reversing up to 10 mph). **Coarse grid first, then finer steps** around the boundary. Logged **vehicle CAN, supplier radar detections/objects and a camera** on one time-synced PC; compared the failing run with the nearest passing run in **CANoe**. Only the angle changed, and the target reached high confidence much later: **targets near the edge of the field of view were picked up late**.
- **Fix:** supplier engineer came on site, ran the boundary tests together, supplier made a **calibration change**. Three candidates went through coarse and fine sets **including false-positive tests** (targets outside the boundary, stationary targets); the best was chosen. Re-verified on the track and with more HiL variations.
- **Lesson (say this!):** "**Know which stages your rig emulates and which it exercises.** Anything bypassed is unproven until you test it for real. On a UAS that's the Iron Bird versus ground and flight test."

**S2. FMEA on a lane change feature (AVL).** Use it for: "Have you done FMEA?" See 5.7 for how to talk about it honestly.

**S3. KPI that found a real problem (FiveAI).** Thresholds from UN R79 / Euro NCAP. Lane-change success **dropped above a certain road curvature that was still inside the spec**, which led to a **steering controller fix**. When results flipped between releases, you compared the same test across stack versions to find the cause. (Your exact part in the fix is unconfirmed, so say "my KPI work surfaced it".) Also a SOTIF example: a performance limit inside the operating envelope.

**S4. Mistake story (map converter).** Converted OSM maps to OpenDRIVE with an adapted open-source converter, validated only visually and with simple scenarios. Later the validator gave false "stay in lane" failures because curves became coarse straight segments. **Lesson:** validate tools on their **hardest cases with numeric checks**, understand both formats, ask experts earlier. (Aerospace link: this is **tool qualification** thinking: DO-330 exists because a tool you trust can hide errors.)

### 3.3 Gap lines (one sentence, then the bridge)

- **UAV / aerospace:** "I haven't worked on aircraft or aerospace standards yet. My career has followed the automotive equivalent: V-model traceability, ISO 26262, SOTIF, fail-safe state design and staged verification, and I've been reading ARP4754A and ARP4761 to map them across."
  *(Only say "reading" if you actually skim Section 6 tonight.)*
- **MBSE / SysML:** "I haven't used Cameo or Capella. My architecture work was in DOORS, MKS Integrity, state diagrams and signal lists, and I'm keen to learn MBSE on the job."
- **FHA / FTA:** "I've taken part in an FMEA. I haven't led an FHA or built a fault tree myself, but I know where they sit: FHA top-down at function level, FTA to show a top event meets its probability target, FMEA bottom-up to feed it."
- **Defence:** "I'm new to defence. I'm a British citizen, in the UK since 2017, no current clearance but happy to be vetted."

---

## 4. SOTIF refresher (ISO 21448)

### 4.1 One-line definition
**Safety Of The Intended Functionality** = "absence of unreasonable risk due to hazards resulting from **functional insufficiencies** of the intended functionality or its implementation", including **reasonably foreseeable misuse**.

In plain words: **the system works exactly as designed, nothing is broken, and it's still unsafe**, because the design or the sensors aren't good enough for some situations.

### 4.2 Where it sits

| Standard | Question it answers | Cause of the hazard | Example (your RCTA) |
|---|---|---|---|
| **ISO 26262** (functional safety) | What if something **fails**? | Faults: random hardware failures, systematic (design/software) errors | Radar ECU loses power, CAN message corrupted, software bug |
| **ISO 21448** (SOTIF) | What if it works as designed but **isn't good enough**? | **Performance limits** and **specification gaps**, plus foreseeable misuse | Target at the **edge of the FOV** picked up late; driver over-trusts the system |
| ISO/SAE 21434 (cybersecurity) | What if someone **attacks** it? | Malicious action | Spoofed radar / CAN injection |

Related names to recognise: **ISO/PAS 8800** (AI / machine learning in road vehicles, 2024), **UL 4600** (safety case for autonomous products), **ISO 34502** (scenario-based safety evaluation), **ISO 34503** (ODD taxonomy).

### 4.3 Key terms (know these cold)

- **Functional insufficiency:** either
  - **Specification insufficiency:** the spec itself is incomplete or wrong (e.g. nobody specified behaviour for a target approaching at 45°).
  - **Performance insufficiency:** a component can't meet what's needed (e.g. radar detection confidence drops near the FOV edge; camera blinded by low sun).
- **Triggering condition:** a specific condition in a scenario that **sets off** a hazardous reaction through an insufficiency (e.g. 45° approach angle, rain, low sun, metal guardrail reflections, GNSS multipath).
- **Hazardous behaviour:** what the system does wrong: **false negative** (no alert/brake when needed) or **false positive** (braking for nothing, which is also dangerous).
- **Reasonably foreseeable misuse:** what users will predictably do (driver ignores the alert, operator over-trusts autonomy).
- **ODD (Operational Design Domain):** the conditions the function is designed to work in. UAS equivalent: the **operating envelope / CONOPS** (wind, temperature, altitude, day/night, EMI environment, launch platform).
- **Acceptance criteria / validation targets:** how much residual risk is acceptable, and how much evidence (e.g. hours, km, scenario coverage) proves it. Common principles: **GAMAB** ("at least as good as" the existing system/human), **positive risk balance**, **ALARP** (UK).

### 4.4 The four areas (the picture they may ask you to draw)
More pictures like this in **Section 12** (18 whiteboard sketches).

```
                 KNOWN                         UNKNOWN
          ┌───────────────────────┬───────────────────────┐
   SAFE   │ Area 1: known safe    │ Area 4: unknown safe  │
          ├───────────────────────┼───────────────────────┤
  UNSAFE  │ Area 2: known unsafe  │ Area 3: unknown unsafe│
          └───────────────────────┴───────────────────────┘
  Goal: shrink Areas 2 and 3 until the residual risk is acceptable.
    Area 3 → Area 2  : DISCOVER (exploratory / boundary / field testing, sim at scale)
    Area 2 → Area 1  : FIX (design change, restrict the ODD, warn the user)
```

### 4.5 The SOTIF process (ISO 21448:2022, clauses 5–13)

| # | Clause | What you actually do |
|---|---|---|
| 5 | Specification and design | Describe the function, its ODD, sensors, algorithms, actuators, known limits. |
| 6 | Hazard identification and evaluation | Find hazardous behaviours (HARA-style: **Severity, Controllability**). If no harm is possible, stop here. Set **acceptance criteria**. |
| 7 | Functional insufficiencies and triggering conditions | Analyse each sensor / algorithm / actuator for limits; list triggering conditions (weather, geometry, targets, EMI…). Methods: HAZOP-style guide words, STPA, sensor-limit tables, expert review, field data. |
| 8 | Functional modifications | Fix: improve the sensor/algorithm, add redundancy or sensor diversity, **restrict the ODD**, hand over to the driver/operator, add a warning. |
| 9 | V&V strategy | Plan the evidence: what's tested in sim, on rigs, on track, on the road; how much is enough (validation targets). |
| 10 | Evaluate **known** scenarios | Prove Area 2 is handled: requirement-based and boundary tests, injecting each triggering condition. |
| 11 | Evaluate **unknown** scenarios | Hunt for Area 3: randomised / parameterised sim at scale, long-run field testing, fleet data. |
| 12 | Evaluate achievement of SOTIF | Argue residual risk is acceptable; release decision (sometimes with conditions). |
| 13 | Operation phase | Field monitoring: new triggering conditions found in service flow back into the process. |

### 4.6 Your RCTA story told as SOTIF (great answer to "Have you applied SOTIF?")

> "My clearest SOTIF case was the RCTA feature. Nothing was broken. The radar and ECU worked as designed, and every HiL test passed. But the HiL bypassed the antenna and the radar's object creation, so it couldn't show a **performance insufficiency**: near the **edge of the field of view**, targets reached high confidence too late. The **triggering condition** was a target approaching at around **45°**. That was an **unknown unsafe** scenario, Area 3, until the proving-ground tests found it. Coarse-to-fine boundary tests **mapped where the unsafe area was**. The fix was a **functional modification**, a supplier calibration change, and we checked it didn't move the risk elsewhere by testing **false positives** too, because braking for nothing is also a hazard. Then we re-verified on the track and on the HiL. Lesson: in SOTIF your test method must **exercise the real perception chain**, not just the logic after it."

FiveAI version: "Our parameterised scenario sweeps were basically **Clause 10 and 11 work at scale**: sweeping parameters inside the ODD to find where performance drops. The curvature finding was a **performance limit inside the spec** that led to a controller fix."

### 4.7 SOTIF on a Callen-Lenz aircraft (show you can transfer it)

Aerospace doesn't have a standard called "SOTIF", but the idea lives in **requirements validation** (ARP4754A: "are these the right, complete requirements?") and in operating-envelope / **CONOPS** analysis. Autonomy and AI (the Applied Intuition work) make it more important.

| Function | Performance / spec insufficiency | Triggering condition | Hazardous behaviour | Possible measure |
|---|---|---|---|---|
| Navigation (Nyan in GNSS-denied ops) | GNSS lost/spoofed; dead-reckoning drift grows with time | Jamming, spoofing, long flight without fixes | Wrong position → misses target / leaves the safe area | IMU + airdata + terrain/visual aiding, spoof detection (GNSS vs IMU disagreement), geofence / flight termination, limit time in dead reckoning |
| **Ship launch (HMS Queen Elizabeth)** | Magnetometer and GNSS assumptions made for land | **Steel deck** (magnetic disturbance), **multipath** off the superstructure, **ship motion** during IMU alignment, air wake | Bad heading at launch → wrong initial path | Align with ship's own nav data, delay mag use until clear of the ship, launch envelope limits (sea state, wind over deck) |
| Koios VTOL landing | Height / position estimate poor near ground | Dust, ground effect, sloping or moving landing site, gusts during transition | Hard landing / tip-over | Landing site limits in CONOPS, extra height sensor, abort-and-climb logic |
| AI target / object detection (EO/IR) | Model trained on limited data | Low sun, fog, thermal crossover at dawn/dusk, unusual targets, decoys | Missed or wrong detection, wrong decision | ODD limits, confidence thresholds, **human on the loop**, scenario-based sim testing at scale |
| Operator interface (SC3) | Display/alerting not designed for overload | Several aircraft (collaborative behaviours), lost link, fatigue | Operator misses an alert / over-trusts autonomy (**foreseeable misuse**) | Alert prioritisation, workload trials, training |

### 4.8 Likely SOTIF questions – answer skeletons

- **"What's the difference between ISO 26262 and SOTIF?"** → Faults vs insufficiencies (table 4.2). One example each from RCTA. "They complement each other; a feature needs both."
- **"How do you know you've tested enough?"** → Acceptance criteria first (what residual risk is OK), then validation targets; known scenarios by boundary tests on each triggering condition; unknown scenarios by parameter sweeps in sim, then sampled on rigs and in the real world; field monitoring after release. "Simulation gives coverage, real tests give credibility, and you must know which stages each method actually exercises."
- **"How would you find triggering conditions for a UAS sensor?"** → Go sensor by sensor (GNSS, IMU, magnetometer, pitot, EO/IR, radio link). For each: physics of what degrades it (weather, geometry, interference, vibration, temperature). Review flight-test and field data. Guide words: no / too much / too little / early / late / wrong.
- **"What do you do if you can't fix the insufficiency?"** → Restrict the ODD/envelope (e.g. no ship launch above sea state X), add monitoring and fallback (degraded mode), hand over to the operator, document the residual risk and get it accepted.

---

## 5. FMEA refresher

### 5.1 What it is
**Failure Mode and Effects Analysis**: a structured, **bottom-up** (inductive) review. For each item or function you ask: **how can it fail? what happens? why would it happen? how bad, how likely, how well would we catch it? what do we do about it?**
It's done **early** (when the design can still change) and kept **alive** as the design evolves.

Types:
- **DFMEA** – design (a product, a part, a function).
- **PFMEA** – process (manufacturing, assembly, maintenance, a test procedure).
- **System / functional FMEA** – at function or architecture level (what you most likely did for lane change).
- **FMEA-MSR** – Monitoring and System Response: what happens after the system detects the fault (degraded modes).
- **FMECA** – FMEA + **Criticality** analysis. **Common in aerospace and defence** (MIL-STD-1629A; SAE ARP5580 for non-automotive FMEA). Expect Callen-Lenz to say FMECA.

### 5.2 The failure chain (the most important idea)

```
   CAUSE  ──→  FAILURE MODE  ──→  EFFECT
   (why)       (how it fails)     (what the user/system/aircraft sees)

   Example (servo channel):
   CAUSE:        connector pin fretting from vibration
   FAILURE MODE: intermittent loss of servo command
   EFFECT:       control surface goes to failsafe position → loss of roll control
```
The **effect** at one level is the **failure mode** at the next level up. Keep the three separate: mixing them up is the most common FMEA mistake.

### 5.3 The 7 steps (AIAG & VDA FMEA Handbook, 2019)

| Step | Name | What happens |
|---|---|---|
| 1 | Planning and preparation | Scope and boundary, team (cross-discipline!), timing. The "5 Ts": InTent, Timing, Team, Tasks, Tools. |
| 2 | Structure analysis | Break the system into a tree: system → subsystem → component (or process steps). Draw the boundary and interfaces. |
| 3 | Function analysis | What does each element do, and its requirements (with numbers). |
| 4 | Failure analysis | Build the chains: failure effects ← failure modes ← failure causes. |
| 5 | Risk analysis | Current **prevention** controls and **detection** controls; rate **S, O, D**; get the **Action Priority**. |
| 6 | Optimisation | Actions to reduce risk, owners and dates; re-rate after actions. |
| 7 | Results documentation | Report, communicate, link to requirements, tests and other analyses. |

### 5.4 The ratings (1–10 each)

- **Severity (S):** how bad the **effect** is. 9–10 = safety or regulatory (10 without warning). **Severity only changes if the design changes** (e.g. adding redundancy changes the effect), not by testing more.
- **Occurrence (O):** how likely the **cause** is, given the **prevention controls** (proven design, derating, design rules, analysis).
- **Detection (D):** how likely your **detection controls** (tests, analysis, reviews; in FMEA-MSR, on-board monitoring) find the cause or failure mode **before release**. **1 = almost certain to detect, 10 = can't detect**. People mix this one up, so state it clearly.
- **RPN = S × O × D** (1–1000): the older method. Problem: the same RPN for very different risks (S10·O2·D5 = 100 = S2·O10·D5), and thresholds like "act if RPN > 100" can hide severity-10 items.
- **Action Priority (AP: High / Medium / Low):** the newer AIAG-VDA method. A lookup table that **puts Severity first, then Occurrence, then Detection**. High = must act or justify.
- **Order of preference for actions:** remove or reduce the **severity** by design (eliminate the failure, add redundancy) → reduce **occurrence** (prevention) → improve **detection**. Better detection is the weakest fix.

### 5.5 FMECA (aerospace / defence flavour) – know the shape

- **Severity categories (MIL-STD-1629A / MIL-STD-882):** **I Catastrophic** (loss of aircraft / death), **II Critical** (major damage / serious injury / mission loss), **III Marginal**, **IV Minor**.
- **Qualitative criticality:** severity category vs probability level (A Frequent … E Extremely improbable) on a **criticality matrix**.
- **Quantitative criticality:** failure-mode criticality **Cm = β · α · λp · t**, where λp = part failure rate, α = fraction of failures in this mode, β = probability the mode causes the effect, t = operating time.
- FMEA / FMES numbers **feed the fault tree** in an aerospace safety assessment (ARP4761, see 6.3).

### 5.6 Worked example: new EO/IR turret on Koios / Fregata (practise reading it aloud)

Boundary: payload + its power, data and mechanical interfaces to the airframe.

| Item / function | Failure mode | Effect (aircraft level) | Cause | S | Prevention control | O | Detection control | D | AP | Action |
|---|---|---|---|---|---|---|---|---|---|---|
| Payload power feed: supply 28 V to turret | **Short circuit** on payload harness | Main bus voltage sags → **FCC brownout / reset** → loss of control | Chafed harness on airframe edge | **10** | Harness routing rules, grommets | 4 | Harness inspection, insulation check | 5 | **H** | **Separate, fused / current-limited payload bus**, FCC on its own protected supply; fault-injection test on Iron Bird |
| Payload power at boot | **Inrush current** exceeds budget | Bus dip at power-on, possible avionics resets | Turret heaters + motors start together | 8 | Power budget from datasheet | 5 | Bench measurement with current probe | 4 | **H** | Soft-start / staged power-up in ICD; measure on bench before integration |
| Turret mounting | Mass / CG outside limits | Pitch trim limit reached, lower endurance, unstable | Heavier turret than datasheet, cabling added | 8 | Mass & CG budget, CAD | 3 | Weigh and CG check before flight | 2 | M | Mass margin in requirements; ballast plan |
| Video data link (Ethernet) | **Babbling / flooding** the shared network | Telemetry or command messages delayed → stale data in FCC | Payload firmware fault | 9 | Separate VLAN / network for payload | 3 | Network load test on Iron Bird | 4 | **H** | Keep payload off the flight-critical network; rate limiting; FCC must not depend on payload |
| RF emissions | **Electromagnetic interference** with GNSS / C2 | GNSS loss / C2 range drop | Unshielded cable, switching noise near GNSS band | 9 | EMC design rules, shielding | 4 | **Ground EMI / desense test, all systems on** | 3 | **H** | Ground test with motors, servos, payload and radios all running; check GNSS C/N0 and link margin |
| Gimbal | Stuck / runaway | Wrong pointing → mission degraded (no flight safety effect if isolated) | Encoder fault | 5 | Supplier qualification | 4 | Built-in test at power-on | 3 | L | Report to operator via BIT; no action on airframe side |

**Talking points from this table:** the highest risk isn't the camera failing, it's the **camera taking the aircraft down with it** (power and data **isolation**). Severity is reduced by **architecture**, not by testing.

### 5.7 Talking about your own FMEA (lane change, AVL) – honestly

Your notes only confirm "**took part in an FMEA at AVL for the lane change feature**". Before the interview, **jot down what you actually remember** (your role, a couple of failure modes, any action that came out of it). If you can't remember details, use this shape and keep it general:

> "At AVL I took part in the FMEA for a lane change feature, alongside writing its ISO 26262 requirements. We worked through the functions (detecting the target lane is free, deciding, steering, handing back to the driver), looked at how each could fail (for example a missed vehicle in the blind spot, or a steering request that's too large or too late), the effect on the driver, the likely causes, and the controls we had. The useful part for me was that **actions fed straight back into requirements and test cases**: if a failure mode had no detection control, we added a requirement or a test."

> [!IMPORTANT]
> Don't make up specific rows, ratings or outcomes. If asked for a detail you don't remember: "I don't remember the exact ratings; it was a few years ago. What I took from it was…"

Typical lane change failure modes (useful vocabulary, **not your actual sheet**): side radar misses an approaching vehicle (SOTIF-type cause) or loses power (26262-type cause); lane markings misread; steering torque request too high / wrong direction / too late; driver not notified when the function aborts; manoeuvre not aborted when a vehicle appears.

### 5.8 FMEA vs the other analyses (they love this question)

| Method | Direction | Question | When |
|---|---|---|---|
| **FHA** (Functional Hazard Assessment) | Top-down, function level | Which **function failures** are hazardous and how bad? Gives failure condition classes and targets. | First, at concept |
| **FTA** (Fault Tree Analysis) | **Top-down, deductive** | What combination of failures causes this **one top event**? Gives a probability and shows single points of failure. | Architecture onwards |
| **FMEA / FMECA** | **Bottom-up, inductive** | What does **each failure** of each part/function cause? | Design onwards |
| **HAZOP** | Guide words on interfaces / flows | What if it's **no / more / less / reverse / early / late**? | Concept / interfaces |
| **STPA** | Control-loop based | Which **unsafe control actions** (incl. software, humans, no failure) cause hazards? Good for autonomy and SOTIF. | Concept onwards |
| **CCA** (Common Cause Analysis) | – | Can one event break redundant channels together (zonal, common mode)? | Architecture |

**One-liner:** "FHA tells you what matters, FTA proves the top events meet their targets, FMEA checks every part bottom-up so nothing slips through. FMEA alone misses **combinations** of failures; FTA alone can miss **failure modes nobody thought of**."

### 5.9 Likely FMEA questions – answer skeletons

- **"Walk me through how you'd run an FMEA for X."** → 7 steps in your own words: scope and team → structure → functions → failure chains → S/O/D and AP → actions with owners → keep it linked to requirements and tests.
- **"What's the weakness of RPN?"** → Same number for different risks; hides high-severity items; AP fixes it by putting severity first.
- **"Detection is rated 2. What does that mean?"** → Our current verification is very likely to catch it before release. (Low number = good.)
- **"How do you reduce severity?"** → Only by changing the design: redundancy, isolation, failsafe state, limiting authority.
- **"How do FMEA results connect to the rest of the work?"** → Actions become **requirements** (e.g. isolate payload bus), **tests** (fault injection on the Iron Bird), **BIT / monitoring** (FMEA-MSR), and feed the **FTA / safety case**.

---

## 6. Safety standards bridge: automotive → aerospace / UK defence

### 6.1 ISO 26262 recap (what you know)
- **HARA** → **ASIL** from **S** (severity S0–S3) × **E** (exposure E0–E4) × **C** (controllability C0–C3): QM, A, B, C, D. Full refresher with worked examples in **Section 13**.
- **Safety goal** → **functional safety concept** (functional safety requirements) → **technical safety concept** → HW / SW requirements.
- **ASIL decomposition:** split a requirement over independent channels, e.g. D = D(D) + QM(D), C(D) + A(D), B(D) + B(D). Needs **independence** (shown by dependent failure analysis).
- Hardware metrics for ASIL D: SPFM ≥ 99 %, LFM ≥ 90 %, PMHF < 10 FIT.

### 6.2 Standards cheat sheet

| Aerospace / defence | What it does | Your automotive bridge |
|---|---|---|
| **SAE ARP4754A / B** | Aircraft & system development process: requirements capture, allocation, **validation** (right requirements?) and **verification** (met?), traceability, **DAL** assignment | ASPICE V-model in DOORS / MKS Integrity; requirements validation = SOTIF-type thinking |
| **SAE ARP4761 / A** | Safety assessment: **FHA → PSSA → SSA**, using FTA, FMEA/FMES, CCA | ISO 26262 HARA → safety concepts → safety analyses |
| **DO-178C** (software) / **DO-254** (complex hardware) | Assurance by **DAL A–E** (A = catastrophic) | ASIL D…QM. **Rough analogy only**: ASIL comes from S×E×C, DAL from the failure condition class. |
| **DO-160G / MIL-STD-810** | Environmental qualification (vibration, temperature, altitude, humidity…) | ECU environmental validation |
| **MIL-STD-461** | EMC / EMI | Automotive EMC (CISPR 25) |
| **DO-330** | Tool qualification | Your map converter lesson |
| **STANAG 4703** | Airworthiness for **light fixed-wing UAS (< 150 kg)**, the class Koios / Fregata fall in | – |
| **STANAG 4671** | Airworthiness for larger fixed-wing UAS (150–20,000 kg) | – |
| **MAA Regulatory Articles** (UK Military Aviation Authority) | UK military air safety rules; the **Duty Holder** owns **Risk to Life** | No real automotive equivalent |
| **Def Stan 00-56** | UK MoD safety management: hazard log, **safety case**, risk reduced **ALARP** | ISO 26262 safety case / work products |
| **CAA CAP 722** / **SORA** | UK civil UAS guidance / Specific Operations Risk Assessment (civil "specific" category) | – |

Failure condition classes (FHA): **Catastrophic** > **Hazardous** > **Major** > **Minor** > **No safety effect**, each with a probability target per flight hour (for large crewed aircraft roughly 1e-9, 1e-7, 1e-5, 1e-3). UAS targets are less strict and depend on class and use. Don't quote numbers for UAS.

### 6.3 Three UK defence safety ideas worth dropping in
- **ALARP** ("As Low As Reasonably Practicable"): UK law (Health and Safety at Work Act). Reduce risk until further reduction is grossly disproportionate to the benefit. Def Stan 00-56 and the MAA are built on it.
- **Safety case:** a structured argument with evidence that the system is acceptably safe for a given use. Often drawn in **GSN (Goal Structuring Notation)**: goals → strategies → evidence. Your test reports, FMEAs and traceability are the **evidence**.
- **Hazard log:** the live record of every hazard, its controls, and its status. It's the backbone of a Def Stan 00-56 safety case.

---

## 7. UAS systems engineering essentials (condensed from the Gemini guide)

### 7.1 System boundary: UAS, not UAV
Always name all segments:
1. **Air vehicle:** **flight control computer** (hard real-time inner loop, IMU, airdata, magnetometer, GNSS, servos / ESCs) and **mission / platform management computer** (autonomy, routing, payload management, Ethernet). *Bridge: safety ECUs on CAN vs your L4 stack in containers.*
2. **Payloads:** EO/IR turret, SIGINT, designators… swapped via **ICDs**.
3. **Data links:** **C2 link** (low bandwidth, high reliability: telemetry and commands) and **payload link** (high bandwidth video).
4. **Ground segment:** GCS (SC3), antennas, launch & recovery (catapult, VTOL pad), **and people + procedures + maintenance**.

**Key architecture principle:** keep **flight-critical** functions (FCC) **isolated** from complex, non-deterministic functions (AI mission software, payloads). That's the same as keeping a safety function independent of an AI policy.

### 7.2 SWaP-C (Size, Weight, Power, Cost)
On a 35 kg aircraft, every gram and watt costs endurance. +1 kg payload → less fuel or higher hover current; **CG shift** → trim drag or instability. Power from a small alternator + battery (e.g. 28 V bus): **peak** (boot, heaters, VTOL lift) matters as much as average. Less cooling at altitude. **RF co-existence:** ESCs, radios and Ethernet in a small composite airframe can **desense GNSS**.

### 7.3 The ICD: four layers
1. **Mechanical:** mass, CG, inertia, mounting, **FOV clearance**, vibration isolation, connector keep-out.
2. **Electrical:** voltage, steady and **peak / inrush** current, enable / kill lines, fusing, grounding and shielding.
3. **Data & timing:** physical layer (Ethernet, CAN, RS-422), message set, **units, rates, endianness, validity flags, init values**, **time sync** (PPS + GNSS time / PTP). *This is your signal-list work at JLR.*
4. **Environmental & EMC:** temperature, cooling airflow, emission limits near GNSS / C2 bands.
Plus **behaviour**: what the payload does on power loss, link loss, or a "shed load" command.

### 7.4 Modes, degraded modes and failsafes
Nominal: **Power-on / PBIT → Pre-flight ready → Launch / VTOL climb → Transition → Cruise / on station → Return to base → Recovery → Safe / disarmed.** **CBIT** runs continuously (heartbeats, bus voltage, servo current, airspeed vs groundspeed, geofence).
Know three contingencies:
1. **Lost C2 link:** debounce (seconds), then a pre-planned **lost-link procedure**: climb / continue leg / fly to a **rally / loiter point**, auto-recover if the link doesn't return.
2. **GNSS jammed / spoofed:** detect (signal drop, GNSS vs IMU / airspeed disagreement) → switch to dead reckoning / other aiding → alert operator, leave the area, limit time.
3. **Geofence breach / flyaway:** an **independent flight termination system** cuts propulsion / deploys a parachute inside the safe area.
*Bridge: your JLR state diagrams with degraded and fail-safe states, and signal lists traced to them.*

### 7.5 The verification ladder
**Analysis / model → SIL → HiL / Iron Bird → ground & combined systems test (EMI, all on) → flight test with incremental envelope expansion.**
- Each step **removes a layer of emulation**. Write down **what each rig emulates vs exercises** (your RCTA lesson).
- Verification methods: **IADT** = **I**nspection, **A**nalysis, **D**emonstration, **T**est. Pick per requirement.
- Never jump to flight: a crash destroys the evidence and stops the programme.

### 7.6 General systems engineering vocabulary (expect at least one of these)
- **Verification** = built it right (meets requirements). **Validation** = built the right thing (meets the need).
- **Good requirement:** necessary, singular, **unambiguous, verifiable**, feasible, traceable, with a rationale. Bad: "The system shall be robust." Good: "The aircraft shall maintain C2 link at up to 50 km line-of-sight with packet loss below 1 %."
- **Traceability:** need → system req → subsystem req → design → test → result, both ways. Lets you see the impact of a change and prove coverage.
- **CONOPS**: how, where, by whom the system will be used. Starting point for requirements and the operating envelope.
- **Trade study:** criteria and weights agreed **before** scoring options.
- **Reviews:** SRR (requirements) → PDR (preliminary design) → CDR (critical design) → TRR (test readiness).
- **TRL** (Technology Readiness Level 1–9).
- **MBSE / SysML:** models instead of documents; diagrams like block definition, internal block (interfaces), state machine, requirements. Tools: Cameo, Capella. (Your gap; say it.)
- **Change control / configuration management:** baselines, change requests, impact analysis through traceability.

---

## 8. Model technical question (practise out loud, ~3 minutes)

> **"A customer wants a heavier EO/IR turret and an encrypted datalink on an existing 35 kg VTOL UAS in 8 weeks. No requirements, just two datasheets. What do you do?"**

1. **Understand the need first:** CONOPS with the customer: what must it detect, at what range, day/night, endurance needed, launch and recovery, where it operates. Turn that into a short set of **testable requirements and acceptance criteria**; agree them early because 8 weeks is tight.
2. **Impact assessment (SWaP + safety):** mass & CG with mechanical/aero, steady and peak power vs the bus budget with electrical, data rates and link budget, EMI risk to GNSS/C2. A quick **delta FMEA** and hazard review on the change (e.g. 5.6: a payload short must never brown out the FCC → **isolate power and data**).
3. **ICD and modes:** write the ICD (four layers + behaviour), and what the payload does in each aircraft mode (e.g. **shed payload power** if bus voltage drops during VTOL landing).
4. **Staged verification:** payload on the bench (power supply + bus analyser) → Iron Bird (timing, **fault injection**: pull the payload mid-mission, the aircraft must fly on) → ground test, everything running, EMI check → incremental flight test with a test matrix.
5. **Plan and risks:** long-lead items, what can run in parallel, what's on the critical path, early flag to the customer if 8 weeks threatens safety evidence.
6. **Close with your bridge:** "It's what I did at JLR: requirements, signal lists, state diagrams, then rig, vehicle and track, but with weight, power and radio margins much tighter."

---

## 9. Your questions and logistics

**Ask (pick 2–3):**
1. "Will this role sit on one programme, like Nyan or Koios / Fregata, or across customer payload integrations and FalconWorks projects?"
2. "With the Applied Intuition partnership, how do you balance simulation and Iron Bird testing against flight trials?" (Your sim-at-scale experience fits here.)
3. "Which tools does the systems team use day to day, such as DOORS or Cameo / SysML?"
4. "Which safety framework do you work to on the military side, Def Stan 00-56 and MAA regulations, or something lighter for smaller UAS?"
5. "Does the role need SC, or are some projects UK Eyes Only? I'm a British and Turkish dual national, so I'd like to check early."
6. "What would success look like in the first six months?"

**Logistics:**
- Salisbury is about 2 hours from Coventry; you're **willing to relocate**. Ask about on-site days and travel to trial sites.
- Salary band £50–65k. Aim for **£60–65k** (senior end). Your floor is £55–60k. Don't open with your £70k unless asked.
- **Available immediately** (last day at Bosch was 6 Nov).
- Clearance: British citizen, UK resident since 2017, no current clearance, willing to be vetted.

---

## 10. Self-test (cover the answers, say them aloud)

1. Define SOTIF in one sentence. How is it different from ISO 26262?
2. What are the two kinds of functional insufficiency? Give one example of each.
3. What's a triggering condition? Give two for a UAS launched from a ship.
4. Draw the four SOTIF areas. Which two do you shrink, and how?
5. Tell the RCTA story in 90 seconds, then again in SOTIF terms.
6. Name the three parts of the FMEA failure chain, using one UAS example.
7. What do S, O and D mean? Is a detection rating of 2 good or bad?
8. What's wrong with RPN? What replaced it?
9. What's FMECA, and how is criticality calculated?
10. FMEA vs FTA vs FHA: direction and purpose of each.
11. How do you reduce severity in an FMEA?
12. What goes into a payload ICD (four layers + one)?
13. What should a UAS do on lost C2 link? On GNSS spoofing?
14. Name the verification ladder steps. What did RCTA teach you about rigs?
15. ARP4754A, ARP4761, DO-178C: one line each.
16. What's ALARP? What's a safety case?
17. Verification vs validation?
18. Rewrite "the payload shall be lightweight" as a good requirement.
19. Give your one-sentence gap lines for UAV, MBSE and FTA.
20. Why Callen-Lenz? (Uncrewed aircraft + own avionics + autonomy work + a chance to bring sim-at-scale and staged-verification discipline into aerospace.)

<details>
<summary>Quick answers (check yourself)</summary>

1. Absence of unreasonable risk from functional insufficiencies / foreseeable misuse, with no fault present. 26262 = faults.
2. Specification insufficiency (45° approach not specified); performance insufficiency (radar FOV edge confidence).
3. A scenario condition that sets off hazardous behaviour through an insufficiency. Steel deck magnetic disturbance; GNSS multipath; ship motion during alignment; air wake.
4. Shrink Area 2 (known unsafe) and Area 3 (unknown unsafe). Discover 3 → 2 by exploration; fix 2 → 1 by modification / ODD restriction.
5. See S1 in 3.2 and the SOTIF version in 4.6.
6. Cause → failure mode → effect. Vibration fretting → intermittent servo command → loss of roll control.
7. Severity of effect, occurrence of cause, detection by current controls. 2 = good (likely to be caught).
8. Same RPN for different risks, hides high severity. Action Priority (severity first).
9. FMEA + criticality. Cm = β · α · λp · t, or severity vs probability matrix.
10. FHA top-down functions; FTA top-down one event, combinations, probability; FMEA bottom-up each failure.
11. Design change only: redundancy, isolation, failsafe state, limit authority.
12. Mechanical, electrical, data & timing, environmental/EMC + behaviour in modes / faults.
13. Debounce → lost-link procedure → rally point → auto recover. Detect disagreement → dead reckoning / other aiding → alert, leave area.
14. Analysis → SIL → HiL / Iron Bird → ground / combined test → incremental flight. Know what each rig emulates vs exercises.
15. Development process & DAL; safety assessment (FHA/PSSA/SSA); airborne software assurance by DAL.
16. Reduce risk until further reduction is grossly disproportionate. Structured argument + evidence that it's acceptably safe for a use.
17. Built it right vs built the right thing.
18. e.g. "The payload installation, including mounts and cabling, shall weigh no more than 2.5 kg and keep the aircraft CG within X–Y mm of datum."
19. See 3.3.
</details>

---

## 11. Mock interview round (about 45 minutes)

**How to run it:** set a timer, read one question, **answer out loud** (record on your phone), then check it against **"Strong answer hits"**. Score each one:
- **0** = missed the point or rambled for more than 3 minutes
- **1** = right idea, but missed parts or had no example
- **2** = structured, specific, one real example or number, honest about gaps

Aim for an average of **1.5 or more**. Redo every 0 straight away, then once more tomorrow morning.
Likely format: a first round with the Systems Engineering Manager and maybe a senior engineer, 45–60 minutes, starting with background and moving to technical questions.

### Part A – Warm-up (5 min)

**A1. "Tell me about yourself."** → Use 3.1.
- **Hits:** under 2 minutes; both employers; one number (120+ scenarios, a team of 5); ends with **why Callen-Lenz**.
- **Red flag:** starting from school in Turkey; going past 2 minutes.

**A2. "Why move from automotive to uncrewed aircraft?"**
> "I didn't choose ADAS. A project needed people and I stayed because I enjoyed the systems side. What I've enjoyed most is **proving a system works**, from simulation through rigs to the real world. A UAS is the same problem with **tighter margins**: weight, power, radio. And Callen-Lenz does the **whole aircraft**: avionics, mission system and flight operations, so a systems engineer sees the full loop. I also want to get back closer to hardware."

**A3. "What do you know about us?"** → Section 1.
- **Hits:** BAE Systems FalconWorks; Nyan / Koios / Fregata; own avionics and SC3; Applied Intuition partnership; Nyan launched from HMS Queen Elizabeth.
- **Red flag:** quoting numbers you haven't checked (wingspan, units built, exact date).

### Part B – Systems engineering (10 min)

**B1. "Fix this requirement: 'The UAS shall have long endurance.'"**
> "It's not verifiable. I'd write: '**The air vehicle shall achieve at least 8 hours endurance** at its economical cruise speed and [altitude], in [temperature] conditions, **with the baseline ISR payload fitted** and a **fuel reserve of X % at landing**.' I'd add a **rationale** that traces it to the CONOPS, and a **verification method**: analysis first, then confirmed by flight test."
- **Hits:** a number; the **conditions**; the verification method; traceability to the need.

**B2. "The customer changes a requirement halfway through. What do you do?"**
- **Hits:** don't just say yes. **Impact analysis using traceability**: which subsystem requirements, ICDs, safety analyses (FMEA, hazard log) and tests are affected; cost and schedule effect; decision at a **change board**; update the **baseline**; plan the **regression testing** (what must be re-verified).
- **Bridge:** "That's why I kept requirements linked to test cases in DOORS and MKS Integrity: when something changes, you can see what it touches."

**B3. "Give me a verification method for each: (a) payload mass, (b) C2 link range, (c) lost-link behaviour, (d) flight software timing."**
- (a) **Inspection / measurement**: weigh it, and check CG.
- (b) **Analysis** (link budget), then **test**: ground range test, then flight.
- (c) **Test with fault injection** on SIL and the Iron Bird (cut the link in every flight phase), then **demonstrate** in flight.
- (d) **Analysis** (worst-case execution time, scheduling), then **test** on the HiL / Iron Bird under worst-case load.
- **Hits:** knows **IADT**; often **more than one method** per requirement; analysis before test.

**B4. "Sketch the architecture of a small ISR UAS and show me where the safety-critical boundary is."** → Section 7.1.
- **Hits:** all **four segments** (air vehicle, payload, links, ground); **FCC vs mission computer**; payload on **separate power and data**; C2 link vs payload link; **independent flight termination**. Say: "Anything complex or AI-based stays outside the boundary and **can't take the FCC down**."

### Part C – SOTIF (10 min)

**C1. "You've got SOTIF on your CV. Explain it to me as someone from aerospace."**
> "In aerospace terms it's close to **requirements validation and the operating envelope**: are the function's requirements and sensors good enough for every situation it will meet, **even when nothing has failed**? ISO 26262 is like ARP4761 failure analysis: it deals with **faults**. SOTIF covers the case where every part works but the **design falls short**, plus predictable misuse. It became necessary once cars started to rely on perception: a radar can be perfectly healthy and still miss something."

**C2. "Give me an example from your own work."** → 4.6 (RCTA).
- **Follow-up 1: "How did you know the fix didn't make things worse?"** → three calibration candidates, coarse and fine tests, **false-positive tests** (targets outside the boundary, stationary targets), chose the best, re-verified on the track and the HiL.
- **Follow-up 2: "Could you have found it earlier?"**
  > "Probably, yes. Poor performance at the **edge of the field of view is a known radar limit**. If we'd listed the sensor's limits at the start, boundary-angle tests would have been in the plan from day one, and we'd have known the HiL couldn't cover them because it bypassed object creation. Now I'd write down **what each test stage actually exercises** when I plan the tests."
- **Hits:** names **performance insufficiency**, **triggering condition**, **unknown → known unsafe**; is honest about what you'd do differently.

**C3. "We're bringing AI-based autonomy onto our aircraft with Applied Intuition. How would you approach its safety?"**
- **Hits:**
  1. **Define the operating envelope (ODD)** the AI is allowed to work in.
  2. **Architecture first:** the AI runs on the mission computer and is **bounded by deterministic protections**: FCC envelope limits, geofence, independent flight termination, and a monitor that can override it. (This is often called **runtime assurance**.)
  3. **Scenario-based testing at scale in simulation**, sweeping the envelope parameters (your FiveAI work), then sampled on the Iron Bird and in flight.
  4. **Data coverage:** was the model trained and tested on the conditions it'll meet? (ISO/PAS 8800 idea.)
  5. **Human on the loop**, and clear alerts when the AI is unsure.
  6. **Monitoring in service**: new triggering conditions feed back into testing.
- **Red flag:** "we'll just test it a lot."

**C4. "List triggering conditions for an EO/IR camera used for autonomous tracking or landing."**
- **Hits:** low sun / glare; **thermal crossover** at dawn and dusk (IR contrast disappears); fog, rain, haze; **vibration blur**; low-contrast or unusual targets, decoys; a **moving landing site** (ship deck); dust at landing; lens icing or dirt.

**C5. "How do you decide the residual risk is acceptable, and who decides?"**
- **Hits:** acceptance criteria agreed **early** (e.g. at least as good as the current way, or reduced **ALARP**); **validation targets** that say how much evidence is enough; a release decision by the safety authority in the organisation. In UK military aviation the **Duty Holder** accepts the **Risk to Life**, with the safety case as the evidence.

### Part D – FMEA (10 min)

**D1. "Talk me through an FMEA you've done."** → Section 5.7.
- **Hits:** honest about your role ("took part"); explains the **failure chain**; says **actions fed back into requirements and tests**.
- **Red flag:** made-up ratings or rows.

**D2. Live exercise: "Do an FMEA on the servo driving the aileron. Give me three or four rows."**

| Failure mode | Effect (aircraft) | Cause | S | Main action |
|---|---|---|---|---|
| **Jams** at a deflection | Uncommanded roll; possible loss of aircraft | Stripped gear, debris, icing | 10 | Split control surfaces / one servo per surface so the other can counter; **jam detection** from position feedback; RTB on detection |
| **Goes limp** (no power or signal) | Surface floats; less roll authority | Connector backs out, fuse or regulator failure | 9 | Locking connectors; redundant power feed; **CBIT on servo current** |
| **Oscillates / jitters** | Vibration, possible flutter, fatigue, poor control | Noisy command line, **EMI from ESCs**, worn feedback sensor | 7 | Shielding and filtering; ground test with all motors running |
| **Moves the wrong way** | Crash at launch | **Reversed after maintenance** (a process failure) | 10 | **Pre-flight control-surface check** in the checklist; keyed connectors; maintenance procedure (PFMEA) |

- **Hits:** keeps cause, mode and effect **separate**; rates severity **at aircraft level**; reaches for **design fixes before detection**; spots the **maintenance / process** failure (interviewers love this one).

**D3. "One item has RPN 80 with severity 10. Another has RPN 200 with severity 4. Which first?"**
> "The severity-10 one. RPN hides it: 10 × 2 × 4 is only 80. That's why the newer **Action Priority** method looks at **severity first**. A severity of 9–10 needs action, or a written justification, whatever the RPN."

**D4. "How is FMEA different from FTA, and when would you choose FTA?"** → Section 5.8.
- **Hits:** FMEA **bottom-up**, one failure at a time; FTA **top-down** from one top event (e.g. "loss of control" or "flyaway"), finds **combinations** and **single points of failure**, gives a **probability** against a target. Use FTA when you must show a catastrophic event is rare enough, or to check redundancy really works.

**D5. "What makes an FMEA go wrong?"**
- **Hits:** done **too late** as paperwork; the wrong team (no cross-discipline people); **mixing up cause, mode and effect**; too vague or far too detailed; actions with **no owner or date**; never updated; detection rated too optimistically; **ignoring the interfaces between subsystems**, which is where most real problems sit (your RCTA and FiveAI toolchain experience).

### Part E – UAS scenarios and troubleshooting (7 min)

**E1. "On the ground everything's fine. In flight, the GNSS fix degrades whenever the payload streams video. What do you do?"**
Use **Contain → Capture → Compare → Reproduce → Fix → Prevent**:
1. **Contain:** safety first. Limit payload use or flight area until it's understood; make sure the aircraft can navigate without GNSS.
2. **Capture:** time-synced logs: GNSS signal strength (C/N0) and satellite count, payload transmitter on/off and power, bus voltage.
3. **Compare:** good vs bad periods. If the only difference is the video transmitter, suspect **RF interference / desense** (harmonics or intermodulation near the GNSS band, around 1575 MHz) or **power supply noise**.
4. **Reproduce on the ground:** **ask why the ground test passed**. Was the transmitter at **full power**? Same antenna positions and orientation? Motors and vibration on? Then repeat with everything running and a spectrum analyser.
5. **Fix:** filtering, shielding, moving the antennas apart, a different frequency plan, cleaner power.
6. **Prevent:** add emission limits to the **ICD** and a full **combined-systems EMI test** to the pre-flight test plan.
- **Bridge:** "It's my RCTA lesson again. When it passes in one place and fails in another, **list what's different between the two environments**."

**E2. "The Iron Bird passes, but on the first flight the aircraft oscillates in roll. Where do you look?"**
- **Hits:** **What does the Iron Bird emulate?** The aerodynamic model, sensor noise, structural flex, servo loads. Likely gaps: the **servo is slower or has backlash under real air loads**; **IMU vibration** in flight; **extra latency**; aero model errors. Compare the **flight log with the simulation using the same inputs**; update the model; retune the gains; **step back** in the envelope expansion.
- **Bridge:** "On AVL's DrivingCube we calibrated the simulation against real recordings and swept the steering PID gains. It's the same idea: match the model to reality before trusting it."

**E3. "Design the lost-link behaviour for one of our aircraft."** → Section 7.4, plus:
- Requirements: timeout, climb altitude, **rally point**, how long to loiter, then recovery.
- Edge cases: link lost **during launch, VTOL transition, landing, or near the geofence**; link lost while GNSS is also degraded.
- The operator must always **know what the aircraft will do** (it's predictable and shown on the GCS).
- Verification: cut the link in **every phase** on SIL and the Iron Bird, then demonstrate in flight.

### Part F – Behavioural (5 min)

**F1. "Tell me about solving a problem with a supplier."** → S1. Focus on **evidence**: time-synced logs, inviting their engineer on site, running the boundary tests **together**, agreeing the fix on data. Don't invent a conflict that didn't happen.

**F2. "Tell me about a mistake."** → S4 (map converter). Own it, show the lesson, and say what you **do differently now**.

**F3. "Tell me about leading a team."** → Five engineers for a year at FiveAI: taught them the tooling and evaluation logic, **split the work** into scenario creation and evaluation so it ran in parallel. Say clearly: "It wasn't formal line management."

**F4. "How do you work when there are no requirements?"** → Section 8: start from the CONOPS, write **testable** requirements, agree them early with the customer.

### Part G – Curveballs (practise at least three)

- **"Why hire you over someone who's worked on aircraft?"**
  > "Fair question. I haven't worked on aircraft. What I bring is eight years of the same systems discipline on safety-related autonomous systems: requirements, interfaces, safety analysis, staged testing from simulation to the real world. And I've done **simulation-based verification at scale** for an L4 stack, which fits your autonomy work with Applied Intuition. I learn fast, and I'd pair with your aircraft experts on the airworthiness side."
- **"Your last five years were simulation. Are you still hands-on?"** → AVL years: vehicles, the proving ground, the DrivingCube, the LEVC factory; your own cars (the battery drain found fuse by fuse). "I want to get back to hardware; that's part of why I'm here."
- **"What's a DAL?"** → Design Assurance Level, A to E, set by the worst failure condition a function can contribute to (A = catastrophic). It drives how much rigour DO-178C / DO-254 demand. Roughly like an ASIL, but derived differently.
- **"What would you do in your first 90 days?"** → Learn the aircraft, the avionics architecture and the process (requirements tool, safety framework); sit in on Iron Bird and flight-test work; take ownership of one well-defined piece (an interface, a requirements set, a test campaign) and deliver it.
- **"Salary expectations?"** → "Around **£60–65k**, given the senior level, but I'm flexible for the right role." (Don't volunteer £70k.)
- **"Any concerns about clearance?"** → "I'm a British citizen and have lived in the UK since 2017. I'm also a Turkish national, so I'd like to check whether any projects are UK Eyes Only. I'm happy to go through vetting."

### Score sheet

| Part | Questions | Your scores (0–2) | Redo? |
|---|---|---|---|
| A Warm-up | A1 A2 A3 | | |
| B Systems engineering | B1 B2 B3 B4 | | |
| C SOTIF | C1 C2 C3 C4 C5 | | |
| D FMEA | D1 D2 D3 D4 D5 | | |
| E Scenarios | E1 E2 E3 | | |
| F Behavioural | F1 F2 F3 F4 | | |
| G Curveballs | pick 3 | | |

---

## 12. Whiteboard sketches (pictures they may ask you to draw)

Being able to **draw it while you talk** makes you look like you own the topic. For each sketch: **When** = the question it answers; **Say** = what to say while you draw.
**Practise:** pick five, draw each one from memory on paper in under 2 minutes, then check against the page. Must-knows: **12.1, 12.2, 12.4, 12.6, 12.10, 12.11**.

### 12.1 Three ways to get a hazard (ISO 26262 vs SOTIF vs cyber)
**When:** "What's the difference between ISO 26262 and SOTIF?"

```
                      HAZARD  (missed alert, unwanted braking, flyaway)
                                            ▲
            ┌───────────────────────────────┼───────────────────────────────┐
            │                               │                               │
   something FAILED              nothing failed, but the          someone ATTACKED it
   (random HW fault, bug)        function wasn't good enough      (spoofing, injection)
                                 (+ foreseeable misuse)

   ISO 26262                     ISO 21448  SOTIF                 ISO/SAE 21434
   aero: ARP4761, DO-178C        aero: requirements valid-        aero: DO-326A
                                 ation, operating envelope
```

**Say:** "Three different doors lead to the same hazard. ISO 26262 covers **faults**, SOTIF covers a function that works as designed but **isn't good enough**, and cybersecurity covers **attacks**. A feature needs all three."

### 12.2 The SOTIF cause chain
**When:** "Explain triggering conditions" / "Walk me through a SOTIF analysis."

```
 TRIGGERING       FUNCTIONAL          HAZARDOUS          HAZARDOUS           HARM
 CONDITION   ──►  INSUFFICIENCY  ──►  BEHAVIOUR   ──►    EVENT       ──►     (if it can't
 (the scenario)   (spec or            (missed, false,    (behaviour in a     be controlled
                  performance)        late action)       real situation)     or avoided)

 RCTA  target at  radar confidence    alert late or      car reverses into   collision
       ~45° angle low at FOV edge     missing            crossing traffic

 UAS   steel ship magnetometer        wrong heading      aircraft launches   loss of
       deck       disturbed           at launch          off its planned     aircraft
                                                         path
```

**Say:** "A **triggering condition** in the scenario hits an **insufficiency** in the function, which produces **hazardous behaviour**. Whether it becomes harm depends on the situation and on whether someone can still control it. You break the chain anywhere: remove the insufficiency, avoid the condition (restrict the ODD), or keep it controllable (warn, hand over)."

### 12.3 The SOTIF process as a loop
**When:** "How would you run SOTIF on a new function?"

```
  ┌────────────────────────────────────────┐
  │ 5    Specify function + ODD / envelope │
  └───────────────────┬────────────────────┘
                      ▼
  ┌────────────────────────────────────────┐   no harm possible
  │ 6    Hazards + acceptance criteria     │──────────────────────► stop
  └───────────────────┬────────────────────┘
                      ▼
  ┌────────────────────────────────────────┐
  │ 7    Insufficiencies + triggers        │◄─────────────────────────────┐
  └───────────────────┬────────────────────┘                              │
                      ▼                                                   │
  ┌────────────────────────────────────────┐                              │
  │ 8    Modify: fix / restrict ODD / warn │◄──────────────┐              │
  └───────────────────┬────────────────────┘               │              │
                      ▼                                    │              │
  ┌────────────────────────────────────────┐               │ not          │
  │ 9-11 V&V: known + unknown scenarios    │               │ acceptable   │
  └───────────────────┬────────────────────┘               │              │
                      ▼                                    │              │
  ┌────────────────────────────────────────┐               │              │
  │ 12   Residual risk acceptable?         │───────────────┘              │
  └───────────────────┬────────────────────┘                              │
                      ▼ yes                                               │
  ┌────────────────────────────────────────┐  new triggering condition    │
  │ 13   Release + field monitoring        │──────────────────────────────┘
  └────────────────────────────────────────┘
```

**Say:** "It's a loop, not a checklist. If the residual risk isn't acceptable you **modify and re-verify**. After release, **field data** finds new triggering conditions and feeds them back in. At FiveAI our scenario sweeps were the 'unknown scenarios' step at scale."

### 12.4 What the rig exercises vs what it emulates (your RCTA story)
**When:** "Tell me about a difficult problem" / "How do you trust a HiL or Iron Bird?"

```
            ┌─────────┐   ┌────────────┐   ┌──────────────┐   ┌─────────┐   ┌───────────┐
 TRACK      │ antenna │──►│ detections │──►│ object/track │──►│ alert   │──►│ CAN, HMI, │
 (real)     │         │   │            │   │ creation     │   │ logic   │   │ brake     │
            └─────────┘   └────────────┘   └──────────────┘   └─────────┘   └───────────┘
            └───────── NOT exercised on the HiL ──────────┘        ▲
                                                                   │
 HiL RIG     simulated objects ────────────────────────────────────┘

 Fault: targets near the FOV edge reached high confidence late → inside object creation.
 UAS:   an Iron Bird simulates aero, sensors and RF → prove those in ground and flight test.
```

**Say:** "The HiL injected objects **after** the radar's object creation, so the one stage that had the fault was never tested. My rule now: for every rig, **write down which stages are real and which are emulated**, and plan real tests for everything emulated."

### 12.5 Coarse-to-fine boundary testing
**When:** "How did you find where it failed?" / "How do you test efficiently?"
**Illustrative layout only. These are not your real results; describe the method, not the numbers.**

```
 STEP 1: coarse grid                    STEP 2: fine steps where results flip
               30°   45°   60°
 walking ped   P     F     ?               40°  42°  44°  46°  48°  50°
 running ped   P     F     ?         ped    P    P    P    F    F    F
 car 20 mph    P     P     ?         car    P    P    F    F    F    F
 car 40 mph    P     F     ?
                                   → border ≈ 44–46°: compare the NEAREST
 P = alert ≥ 2 s before                      PASS with the FIRST FAIL, same conditions
 F = late or no alert
```

**Say:** "A coarse grid first, so you don't waste track time. Then fine steps **only where passes turn into failures**. Then compare the closest pass with the first fail: everything is equal except one parameter, so the logs point straight at the cause. The same idea works for envelope expansion on an aircraft."

### 12.6 The FMEA failure chain across levels
**When:** "Explain failure mode, cause and effect" / "How do you do a system FMEA?"

```
             CAUSE                    MODE                     EFFECT

 COMPONENT   pin fretting       ──►   servo loses        ──►   aileron floats
             (vibration)              command
                 ┌──────────────────────┘                         │
                 │                          ┌─────────────────────┘
                 ▼                          ▼
 SUBSYSTEM   servo loses        ──►   aileron floats     ──►   less roll
             command                                           authority
                 ┌──────────────────────┘                         │
                 │                          ┌─────────────────────┘
                 ▼                          ▼
 AIRCRAFT    aileron floats     ──►   less roll          ──►   loss of aircraft
                                      authority                → rate SEVERITY here

 Rule: the MODE at one level is the CAUSE one level up; the EFFECT becomes the MODE one level up.
```

**Say:** "Keep cause, mode and effect separate. The **same event moves up a column** as you go up a level. Rate **severity at the top**, on the aircraft, because that's where the harm is."

### 12.7 The FMEA worksheet (draw the headers, fill one row)
**When:** "Show me how you'd lay out an FMEA."

```
 Item /    Failure   Effect     S   Cause      Prevention O  Detection  D  AP  Action /
 function  mode                                control       control           owner
 ───────── ───────── ────────── ─   ────────── ────────── ─  ────────── ─  ──  ──────────
 Payload   short     FCC        10  chafed     routing    4  harness    5  H   separate
 power     circuit   brownout       harness    rules         inspection        fused bus
```

**Say:** "Left to right it tells a story: **what** fails, **so what**, **why**, how we **prevent** it, how we'd **catch** it, and **what we'll do**. S goes with the effect, O with the cause, D with the detection control."

### 12.8 Fault tree with AND / OR gates
**When:** "How is FTA different from FMEA?" / "How does redundancy help?"

```
                          ┌────────────────────────────┐
                          │ TOP: loss of roll control  │
                          └──────────────┬─────────────┘
                                         │ OR
             ┌───────────────────────────┼───────────────────────────┐
   ┌─────────┴────────┐        ┌─────────┴────────┐        ┌─────────┴────────┐
   │ both ailerons    │        │ FCC sends        │        │ roll sensing     │
   │ lost             │        │ wrong command    │        │ wrong (IMU)      │
   └─────────┬────────┘        └──────────────────┘        └──────────────────┘
             │ AND
       ┌─────┴─────────┐
┌──────┴──────┐ ┌──────┴──────┐
│ left servo  │ │ right servo │
│ fails       │ │ fails       │
└─────────────┘ └─────────────┘

 OR  gate: any one input is enough → probabilities ADD       (P ≈ P1 + P2 + P3)
 AND gate: all inputs are needed   → probabilities MULTIPLY  (P = PL × PR)
 Redundancy turns 1e-4 × 1e-4 into 1e-8 ONLY IF the failures are independent.
 Same power feed, same software, same wiring route = common cause → check with CCA.
```

**Say:** "FTA starts from **one bad outcome** and works down. OR gates add, AND gates multiply, so redundancy is powerful, but only if nothing **common** can take out both channels at once."

### 12.9 Aerospace V-model with the safety process (ARP4754A + ARP4761)
**When:** "Do you know ARP4754A / ARP4761?" / "How does safety fit the lifecycle?"

```
 Need / CONOPS ················································ Validation (flight trials)
   ╲  FHA                                                     ╱
     System requirements ·································· System verif. (Iron Bird)
       ╲  PSSA: FTA, CCA                                  ╱ SSA: FTA, FMEA/FMES, CCA
         Subsystem requirements ······················· Subsystem verif. (HiL)
           ╲                                          ╱
             Item design ·························· Item test (bench)
               ╲                                  ╱
                 Build: software DO-178C, hardware DO-254

 ····· = traceability: every requirement has its verification. Safety runs alongside.
```

**Say:** "Same V as ASPICE. **FHA** at the top finds which function failures matter, **PSSA** checks the architecture can meet the targets, and **SSA** on the right side proves it with evidence. In ISO 26262 terms: HARA, safety concept, then safety analyses and verification."

### 12.10 UAS architecture and the flight-critical boundary
**When:** "Sketch the architecture" / "Where does the AI or the payload sit?"

```
                         UAS SYSTEM BOUNDARY
┌──────────────────────────────────────────────────────────────────────────────┐
│ GROUND AND SUPPORT                                                          │
│ Operator ──► mission planning ──► GCS / SC3                                │
│                                      ▲  │                                   │
│                       telemetry / C2 │  │ C2 commands                       │
│                       payload data   │  │                                   │
├──────────────────────────────────────┼──┼───────────────────────────────────┤
│ AIR VEHICLE                          │  │                                   │
│                                      │  ▼                                   │
│  FLIGHT-CRITICAL DOMAIN              │ Airborne radios                      │
│  ┌──────────────────────┐           │ C2 + payload data links              │
│  │ Flight sensors       │           │                                      │
│  │ IMU, airdata, GNSS,   │           │                                      │
│  │ compass, altitude    │           │                                      │
│  └──────────┬───────────┘           │                                      │
│             ▼                       │                                      │
│  ┌──────────────────────┐ validated │   ┌─────────────────────┐            │
│  │ FCC / autopilot      │──────────────►│ Mission computer    │            │
│  │ control laws/limits  │ state/health│   │ autonomy / route   │            │
│  └──────┬─────────▲─────┘           │   └──────────┬──────────┘            │
│         │         └── bounded commands ────────────┘                       │
│         └──► servos, ESCs, engine / propulsor, lift motors                  │
│                                      │              ▲                       │
│  independent FTS / termination output│    ┌─────────┴──────────┐            │
│  (own safety logic, position, power)  │    │ Payload            │────────────┤
│                                      │    │ EO/IR, SIGINT, etc.│ video/data │
│                                      │    └────────────────────┘ to GCS     │
│  PLATFORM SERVICES: airframe / structure · propulsion · fuel / energy       │
│  electrical generation and distribution · thermal management · networks    │
│  protected FCC supply · isolated mission/payload supplies · load shedding  │
└──────────────────────────────────────────────────────────────────────────────┘

External interfaces: GNSS satellites → GNSS receiver; weather and airspace
constraints → mission planning / operating limits. The C2 link carries commands
and telemetry; the separate payload link carries video or sensor products.
System support also includes antennas, launch/recovery equipment, maintenance,
test equipment, crew training, procedures and range / airspace coordination.
```

**Abbreviations:** **C2** = command and control; **ESC** = electronic speed controller; **EO/IR** = electro-optical / infrared; **FCC** = flight control computer; **FTS** = flight termination system; **GCS** = ground control station; **GNSS** = Global Navigation Satellite System; **IMU** = inertial measurement unit; **SC3** = Callen-Lenz ground-control / mission-management system; **SIGINT** = signals intelligence.

**Say:** "I split the UAS into the air vehicle, ground/support segment, communications links and operating environment. Inside the air vehicle, the FCC closes the flight-control loops using flight sensors and commands the actuators. The mission computer handles route and mission autonomy; it gets validated state data and can send only bounded commands. The payload has its own interfaces and isolated power/data paths. I would also show the platform services that every subsystem depends on: structure, propulsion, energy, electrical distribution, thermal management and networks. Finally, the independent safety functions and ground crew procedures need to be included in the system boundary, not treated as afterthoughts."

### 12.11 Lost-link state machine
**When:** "Design the lost-link behaviour" / "Draw a degraded-mode state machine."

```
┌───────────┐ link lost   ┌────────────────┐ timeout T1     ┌──────────────────────┐
│ NOMINAL   │────────────►│ LINK-LOSS      │───────────────►│ LOST-LINK PROCEDURE  │
│ mission   │◄────────────│ debounce, hold │ (e.g. 5–10 s)  │ climb, fly to rally  │
└─────┬─────┘ link back   └────────────────┘                │ point, loiter for T2 │
      ▲                                                     └─────┬─────────┬──────┘
      │                     link back during procedure            │         │
      └───────────────────────────────────────────────────────────┘         │ T2 over,
                                                                            │ no link
                                                                            ▼
                                                              ┌──────────────────────┐
                                                              │ AUTO RECOVERY        │
                                                              │ land at planned site │
                                                              └──────────────────────┘

 At ANY state: geofence breach or flyaway → independent FLIGHT TERMINATION (FTS).
 Verify: cut the link in EVERY phase (launch, transition, cruise, landing, near the geofence).
```

**Say:** "Don't react to a single dropped packet: **debounce** first. Then a **pre-planned, predictable** procedure the operator already knows. If the link comes back, return to the mission. If not, recover automatically. And there's always an **independent** termination layer. It's the same discipline as the degraded and fail-safe states I drew for the radar features at JLR."

### 12.12 The verification ladder: what's real at each step
**When:** "What's your V&V strategy?" / "How do you balance simulation and flight test?"

```
                    REAL in this test                    SIMULATED in this test
 Analysis / model   –                                    everything
 SIL                flight software                      computer, sensors, aero, actuators, RF
 HiL / Iron Bird    + FCC, wiring loom, loaded servos    aero, sensor inputs, RF propagation
 Ground / CST       + whole aircraft, radios, engine,    flight loads, airflow, altitude
                      real EMI
 Flight test        everything                           nothing (envelope opened step by step)

   ▲ towards the top: more tests per day, cheaper, safer
   ▼ towards the bottom: more realism, more cost and risk per test
```

**Say:** "Use simulation for **coverage** and flight for **credibility**. Each step down removes a layer of emulation, and anything still emulated is unproven. That's my RCTA lesson. Never jump straight to flight: a crash destroys the evidence."

### 12.13 The ICD stack
**When:** "What goes into an ICD for a new payload?"

```
 ┌────────────────────────────────────────────────────────────────────┐
 │ 1 MECHANICAL   mass, CG, mounts, FOV clearance, vibration          │
 ├────────────────────────────────────────────────────────────────────┤
 │ 2 ELECTRICAL   voltage, peak/inrush, enable/kill, fuse, ground     │
 ├────────────────────────────────────────────────────────────────────┤
 │ 3 DATA/TIMING  bus, messages, units, rate, endianness, validity,   │
 │                init values, time sync (PPS / PTP)                  │
 ├────────────────────────────────────────────────────────────────────┤
 │ 4 ENVIRONMENT  temperature, cooling, EMC limits near GNSS / C2     │
 ├────────────────────────────────────────────────────────────────────┤
 │ + BEHAVIOUR    what it does on power loss, link loss, load shed    │
 └────────────────────────────────────────────────────────────────────┘
```

**Say:** "Four layers plus behaviour. Most integration problems I've seen were in **layer 3**: units, rates, validity flags and timestamps. At JLR that was my signal-list work, every input and output traced to the state machine."

### 12.14 Runtime assurance: how to fly AI safely
**When:** "How would you make AI-based autonomy safe?" (Applied Intuition partnership.)

```
            ┌────────────────────────────┐
 sensors ──►│ ADVANCED controller (AI)   │───────────────┐
            │ powerful, hard to verify   │               │
            └────────────────────────────┘               │
                                                         │
                                                         ▼
            ┌────────────────────────────┐          ┌────────┐        ┌──────────┐
 sensors ──►│ SAFE backup controller     │─────────►│ SWITCH │───────►│ aircraft │
            │ simple, fully verified     │          └────────┘        └──────────┘
            └────────────────────────────┘               ▲
                                                         │  selects BACKUP if the AI's
                                                         │  command would leave the
            ┌────────────────────────────┐               │  safe envelope
 state   ──►│ SAFETY MONITOR             │───────────────┘
            │ verified, watches envelope │
            └────────────────────────────┘

 You don't have to prove the AI is always right: you prove the MONITOR and the BACKUP.
 Standard to name: ASTM F3269 (run-time assurance for aircraft systems with complex functions).
```

**Say:** "Let the AI do the clever work, but put it inside a **verified envelope**. A simple monitor checks every command, and if it would leave the safe envelope, a simple, proven backup takes over. That way the safety argument rests on parts you **can** verify."

### 12.15 ALARP and the risk matrix (UK defence)
**When:** "How do you decide a risk is acceptable?" / "What's ALARP?"

```
 RISK
  ▲
  │ ┌──────────────────────────┐
  │ │ INTOLERABLE              │ can't be justified → redesign
  │ ├──────────────────────────┤
  │ │ TOLERABLE only if ALARP  │ reduce until further reduction costs are grossly
  │ │                          │ out of proportion to the benefit; Duty Holder accepts
  │ ├──────────────────────────┤
  │ │ BROADLY ACCEPTABLE       │ keep it there, keep monitoring
  │ └──────────────────────────┘
```

```
               LIKELIHOOD →
 SEVERITY ↓    Improbable  Remote   Occasional  Probable  Frequent
 Catastrophic  M           H        H           H         H
 Critical      L           M        H           H         H
 Marginal      L           L        M           M         H
 Negligible    L           L        L           L         M

 Illustrative only: each programme / Duty Holder sets its own matrix and bands.
```

**Say:** "Risk is severity times likelihood. In the UK you don't stop at 'acceptable': you reduce it **ALARP**, and the **Duty Holder** formally accepts what's left, with the safety case as the evidence."

### 12.16 Defence in depth (Swiss cheese) for a flyaway
**When:** "What stops the aircraft leaving the range if the autopilot fails?"

```
  hazard: flyaway
      │
      ▼   Layer 1  good design + qualified autopilot         (prevent)
      ▼   Layer 2  CBIT detects fault → mode change / RTB    (detect + respond)
      ▼   Layer 3  soft geofence → hold or return            (contain)
      ▼   Layer 4  independent FTS at the hard boundary      (terminate)
      ▼   Layer 5  operating area + buffer, no people below  (limit harm)
      ▼
  harm only if a hole lines up in EVERY layer → layers must be INDEPENDENT
```

**Say:** "No single layer is perfect, so you stack **independent** ones. The flight termination system mustn't share power, software or sensors with the autopilot it's protecting against."

### 12.17 Traceability
**When:** "Why does traceability matter?" / "How do you handle a change request?"

```
  Need ◄─► System req ◄─► Subsystem req ◄─► Design / ICD ◄─► Test case ◄─► Result

  Trace DOWN → coverage:      every need is designed and tested
  Trace UP   → justification: every requirement and test exists for a reason
  Sideways   → impact:        a change request shows exactly what to redo and re-test
```

**Say:** "Traceability is what lets you answer two questions fast: **have we tested everything?** and **what does this change break?** I kept it in DOORS and MKS Integrity at JLR."

### 12.18 Troubleshooting flow
**When:** any "it works here but fails there" question (e.g. GNSS drops when the payload transmits).

```
  CONTAIN ─►  CAPTURE ─►   COMPARE ─►    REPRODUCE ─►  FIX ─►       PREVENT
  make it     time-sync    good run vs   on bench /    root         add to test plan,
  safe first  all the logs bad run: what ground first  cause,       ICD, checklist
                           is different?               not symptom
```

**Say:** "First make it safe, then get evidence before opinions. The best clue is always **what's different** between where it works and where it fails. Finish by making sure it **can't come back**: a test, an ICD limit or a checklist item."

---

## 13. HARA refresher (ISO 26262 Hazard Analysis and Risk Assessment)

### 13.1 What it is, in one breath
> "The HARA is the first safety analysis in ISO 26262, in Part 3, the concept phase. You take the item's functions, imagine each one **malfunctioning at vehicle level**, put that malfunction into every relevant **driving situation**, and rate the risk with **Severity, Exposure and Controllability**. That gives an **ASIL** for each hazardous event and the top-level **safety goals**. Everything else in the safety lifecycle flows from those goals."

Four things that make a HARA a HARA:
- **Top-down, at vehicle level.** "Unintended braking", not "radar ECU fails".
- **Early.** Done on the item definition, before the design exists.
- **No causes.** Why it malfunctions comes later (FMEA, FTA).
- **Rated as if the item had no safety mechanisms of its own.** Otherwise you'd be using the fix to justify a lower requirement for the fix.

> [!IMPORTANT]
> **Your honest line.** Your notes confirm you **wrote ISO 26262 requirements for a lane change feature**, took part in its **FMEA**, and were **trained in ISO 26262 and SOTIF**. They don't say you took part in the HARA. Unless you did: *"I worked from the HARA's safety goals and ASILs when I wrote the requirements. I didn't lead the HARA itself, but I know how it's built."*

### 13.2 The HARA flow
**When:** "Walk me through a HARA."

```
┌───────────────────┐     ┌────────────────────┐     ┌───────────────────┐     ┌────────────────────┐
│ ITEM DEFINITION   │     │ SITUATION ANALYSIS │     │ HAZARD ID         │     │ HAZARDOUS EVENTS   │
│ function, bounds, │────►│ road, speed,       │────►│ malfunctions at   │────►│ hazard × situation │
│ interfaces, modes │     │ weather, traffic   │     │ vehicle level     │     │                    │
└───────────────────┘     └────────────────────┘     └───────────────────┘     └──────────┬─────────┘
                                                                                          │
                                                                                          ▼
                          ┌────────────────────┐     ┌───────────────────┐     ┌────────────────────┐
                          │ FUNCTIONAL SAFETY  │◄────│ SAFETY GOALS      │◄────│ RATE S, E, C       │
                          │ CONCEPT (FSRs,     │     │ + ASIL, safe      │     │ → ASIL per event   │
                          │ allocation)        │     │ state, FTTI       │     └────────────────────┘
                          └────────────────────┘     └───────────────────┘
 Guide words help find hazards (13.6). A safety goal takes the HIGHEST ASIL of its events.
```

**Say:** "Define the item, list the situations it'll be used in, find the vehicle-level malfunctions, combine them into hazardous events, rate S, E and C, and turn the result into **safety goals** with an ASIL, a **safe state** and a **fault tolerant time interval**."

### 13.3 Key terms
| Term | Meaning | Lane change example |
|---|---|---|
| **Item** | The system or function you're analysing, with its boundary | Automatic lane change on motorways |
| **Malfunctioning behaviour** | The item not doing what it should, at its output | Steers without a request |
| **Hazard** | A potential source of harm caused by the malfunction (vehicle-level behaviour) | **Unintended lateral movement** |
| **Operational situation** | Where and when: road, speed, traffic, weather, driver state | Motorway at 110 km/h, adjacent lane occupied |
| **Hazardous event** | **Hazard × operational situation**: this is what gets rated | Unintended lateral movement at 110 km/h **with a car alongside** |
| **Safety goal** | Top-level safety requirement that prevents or mitigates the hazardous event(s); carries the ASIL | "Avoid unintended lateral movement of the vehicle" – ASIL D |
| **Safe state** | Operating mode with no unreasonable risk to go to when a fault is detected | Function off, steering smoothly handed back, driver warned |
| **FTTI** (fault tolerant time interval) | Time from a fault to a possible hazardous event, if no safety mechanism acts. Detection + reaction must fit inside it. | A few hundred ms for unintended steering at speed (illustrative) |
| **ASIL** | Automotive Safety Integrity Level QM, A–D: how much rigour the development needs | – |

**Hazard vs hazardous event** (a favourite question): "Unintended braking" is the **hazard**. "Unintended braking at 110 km/h on a motorway **with a vehicle close behind**" is the **hazardous event**. Same hazard, very different risk in a car park.

### 13.4 Rating S, E and C

| Severity | Meaning (injuries) |
|---|---|
| **S0** | No injuries |
| **S1** | Light and moderate injuries |
| **S2** | Severe and life-threatening injuries (survival probable) |
| **S3** | Life-threatening injuries (survival uncertain), fatal injuries |

| Exposure | Meaning | By duration (share of driving time) | By frequency |
|---|---|---|---|
| **E0** | Incredible | – | – |
| **E1** | Very low probability | – | Rarer than E2 (unusual situations) |
| **E2** | Low probability | < 1 % | A few times a year or less |
| **E3** | Medium probability | 1–10 % | Once a month or more |
| **E4** | High probability | > 10 % | Almost every drive |

| Controllability | Meaning |
|---|---|
| **C0** | Controllable in general |
| **C1** | Simply controllable: **99 %** or more of drivers / road users avoid the harm |
| **C2** | Normally controllable: **90 %** or more avoid the harm |
| **C3** | Difficult to control or uncontrollable: fewer than 90 % |

**How to rate each one well:**
- **S:** from the **likely accident** and its injuries (e.g. side impact at motorway speed vs a car-park bump). Include **everyone at risk**: occupants, other drivers, pedestrians. Use the realistic worst case, not the absolute worst.
- **E:** how often or how long the **situation** occurs, **not** how likely the failure is. Use duration for long situations (motorway driving), frequency for short ones (reversing out of a space, overtaking).
- **C:** can a normal, attentive driver or other road user avoid the harm? Write the assumption down (hands on the wheel? speed range? how much steering torque can they overcome?). No driver (L4) → usually **C3**, unless others can avoid it.

### 13.5 The ASIL table
**When:** "How do you get from S, E, C to an ASIL?"

```
               C1     C2     C3
  S1    E1     QM     QM     QM
        E2     QM     QM     QM
        E3     QM     QM     A
        E4     QM     A      B

  S2    E1     QM     QM     QM
        E2     QM     QM     A
        E3     QM     A      B
        E4     A      B      C

  S3    E1     QM     QM     A
        E2     QM     A      B
        E3     A      B      C
        E4     B      C      D

  Shortcut: S + E + C  = 10 → D,  9 → C,  8 → B,  7 → A,  6 or less → QM
            Any S0, E0 or C0 → no ASIL (QM).
```

**Say:** "You only get **ASIL D** with the worst of everything: **S3, E4, C3**. Drop any one by a step and it falls to C. Add the numbers: 10 is D, 9 is C, 8 is B, 7 is A, anything lower is QM."

The ASIL then drives **how** you develop: methods and independence of reviews, hardware metrics (for D: SPFM ≥ 99 %, LFM ≥ 90 %, PMHF < 10 FIT), and testing rigour. It can later be split across redundant channels with **ASIL decomposition** (see 6.1).

### 13.6 Finding hazards: guide words on each function
Apply each guide word to each function's output. Then keep only the results that are **vehicle-level behaviours**.

| Guide word | Lane change result | Hazard (vehicle level) |
|---|---|---|
| **No / loss** | Lane change not performed when requested | Vehicle stays in lane (often **no harm**) |
| **Unintended** | Steers without a request | Unintended lateral movement |
| **More** | Too much steering torque / lateral acceleration | Excessive lateral movement, loss of stability |
| **Less** | Too little steering, stops mid-manoeuvre | Vehicle left straddling two lanes |
| **Early** | Starts before the target lane is confirmed free | Lane change into an occupied lane |
| **Late** | Abort comes too late when a fast car approaches | Lane change into an occupied lane |
| **Wrong direction** | Steers to the wrong side | Unintended lateral movement |
| **Stuck / won't stop** | Doesn't hand back when the driver steers | Driver can't override |

### 13.7 Worked example 1: automatic lane change (motorway, driver supervising)
**Illustrative ratings: a reasonable answer, not the JLR or AVL figures.** Interviewers care about the **reasoning**, not the exact letter.

| ID | Hazardous event (hazard + situation) | S | E | C | ASIL | Reasoning |
|---|---|---|---|---|---|---|
| H1 | **Unintended lateral movement** at 110 km/h, vehicle in the adjacent lane | S3 | E4 | C3 | **D** | High-speed side collision or loss of control; motorway driving is > 10 % of time; sudden strong steering is hard to correct in time |
| H1b | Same, but the item definition **limits steering torque** so a driver can always override | S3 | E4 | C2 | **C** | Same S and E. C drops only if the authority limit is part of the **intended function**, written in the item definition |
| H2 | **Lane change into an occupied lane** (target lane not free) in dense traffic | S3 | E3 | C2 | **B** | Driver is supervising and usually sees and stops it; dense traffic with a car in the blind spot is "monthly or more" |
| H3 | **Abort too late** when a fast vehicle approaches in the target lane | S3 | E2 | C2 | **A** | Fast approaching car during the few seconds of a manoeuvre is rare |
| H4 | **Lane change not performed** when requested | S0 | – | – | **QM** | Vehicle simply stays in lane: no harm, so no ASIL |

Resulting safety goals:
- **SG1:** Avoid unintended lateral movement of the vehicle. **ASIL D** (from H1). Safe state: function off, steering handed back smoothly, driver warned.
- **SG2:** Avoid an automated lane change into an occupied lane. **ASIL B** (from H2 and H3; it takes the highest).

**Talking points:**
- "**Loss of an assistance function is often QM**, because the driver is still in charge. The **unintended action** is what carries the high ASIL."
- "Controllability is where HARA reviews argue most. Write down the assumption: what steering torque can a driver overcome, are hands on the wheel?"
- "At **L3 or L4** there's no supervising driver, so C goes up, usually to **C3**, and H2 becomes C or D. That's why higher automation is so much harder."

### 13.8 Worked example 2: RCTA with braking (your feature)
**Illustrative only. Don't present these as JLR's real ASILs.**

| ID | Hazardous event | S | E | C | ASIL | Reasoning |
|---|---|---|---|---|---|---|
| R1 | **Unintended automatic braking** while reversing out of a parking space at walking pace, car behind | S1 | E3 | C1 | **QM** | Low-speed bump at worst; the driver easily handles a short stop |
| R2 | **Brake not released**: car held stationary **in the path** of crossing traffic (reversing out onto a road) | S3 | E2 | C2 | **A** | A side impact at road speed could be serious; reversing onto a live road is uncommon; most drivers can still pull away or warn |
| R3 | **No braking** when a vehicle or pedestrian crosses behind | S2 | E3 | C1–C2 | **QM–A** | It's an **assistance** feature: the driver is still responsible for looking. The debate is how much the driver relies on it |

**The link to your SOTIF story (say this!):**
> "R3 is the hazard from my RCTA story. The **HARA identifies the hazard once**. **ISO 26262** then deals with the *fault* causes, like the radar losing power. **SOTIF** deals with the *non-fault* causes, like targets near the edge of the field of view being picked up late. Same hazard, two different standards for two different kinds of cause."

### 13.9 Worked example 3: the same thinking on a UAS (aerospace FHA)
Aerospace doesn't use S × E × C. Its equivalent is the **Functional Hazard Assessment (FHA)** from ARP4761:
- For each **function**, in each **flight phase**, list the **failure conditions**: **loss**, **partial loss**, **erroneous (undetected)**, **inadvertent**.
- Classify the **effect**: **Catastrophic, Hazardous, Major, Minor, No safety effect**. Each class has a probability target and sets the **DAL**.
- The "situation" is the **flight phase and operating area**. The "controllability" is folded into the effect: what the crew, operator or an automatic response can still do.
- On a UAS there's no crew or passengers. Harm is mostly to **people on the ground**, **other airspace users** and the **aircraft** itself, so **where you fly** (population below, airspace) matters a lot.
- **Detected vs undetected** is huge: a detected navigation loss triggers a fallback; an *erroneous* position that nobody notices can cause a flyaway.

**Illustrative FHA rows for a Koios-type VTOL ISR aircraft** (classes depend on the operating area):

| Function | Failure condition | Flight phase | Effect | Class |
|---|---|---|---|---|
| Attitude control | Loss | Any | Uncontrolled descent; people below at risk | Catastrophic |
| Navigation (position) | **Erroneous, undetected** | Cruise | Flies off route, may leave the safe area (flyaway) | Hazardous – Catastrophic |
| Navigation (position) | Loss, **detected** | Cruise | Dead reckoning, return to base | Major |
| C2 link | Loss, detected | Cruise | Lost-link procedure, automatic RTB (12.11) | Minor – Major |
| Lift motor (1 of 8) | Loss | VTOL hover / transition | Less control margin, precautionary landing | Major (if designed for motor-out) |
| Flight termination | **Inadvertent** | Any | Aircraft lost; falls inside the range | Major – Hazardous |
| Payload video | Loss | On station | Mission degraded only | No safety effect |

**Say:** "It's the same top-down question as a HARA: what happens if this function fails, in this phase, and how bad is it? Then you design so the bad ones are rare enough and independent protections exist, like the flight termination system."

### 13.10 HARA, FHA, SORA and the UK military: side by side
| | ISO 26262 **HARA** | Aerospace **FHA** (ARP4761) | Civil UAS **SORA** (JARUS) | UK military (MAA / Def Stan 00-56) |
|---|---|---|---|---|
| Looks at | Item functions | Aircraft / system functions | The whole **operation** | Hazards of the system in use |
| Situation | Operational situation (E) | Flight phase, environment | Population below, airspace | Operating context |
| How bad | S0–S3 | Catastrophic … No safety effect | Ground risk class, air risk class | Severity in a risk matrix (12.15) |
| Avoidance | C0–C3 (driver) | Crew / operator action, in the effect | Mitigations (e.g. parachute, emergency response plan, strategic air-risk mitigations) | Controls in the hazard log |
| Output | **ASIL + safety goals** | **Class + probability target + DAL** | **SAIL I–VI** + operational safety objectives | **Hazard log**, risk reduced **ALARP**, Duty Holder accepts **Risk to Life** |

For SORA, know the name and shape only: it's the civil "specific category" risk method. Callen-Lenz's military work will mainly follow MAA rules and the safety case approach.

### 13.11 HARA vs FMEA vs SOTIF hazard analysis
| | **HARA** | **FMEA** | **SOTIF hazard analysis** |
|---|---|---|---|
| Direction | Top-down | Bottom-up | Top-down, then into triggering conditions |
| Level | Vehicle / function | Component / function | Function + sensors / algorithms |
| Asks | What malfunctions are hazardous, and how bad? | How can each part fail, and what happens? | Can the function be unsafe **without a fault**? |
| Causes? | **No** | **Yes** | Yes: insufficiencies + triggering conditions |
| Rates | S, E, C → **ASIL** | S, O, D → AP / RPN | S, C (reuses HARA hazards; no ASIL) |
| Output | Safety goals | Design actions, tests | Functional modifications, ODD limits, V&V plan |
| When | Concept | Design onwards | Concept onwards |

**One-liner:** "The HARA says **what must never happen and how strictly**. The FMEA checks the **design** can't cause it through a fault. SOTIF checks it can't happen **without a fault**."

### 13.12 Common HARA mistakes
- **Lowering E because "the failure is rare."** E is about the **situation**. Failure rates are handled later by the hardware metrics.
- **"ASIL shopping":** splitting situations ever finer ("motorway, rain, at night, on a Tuesday") to push E down.
- **Counting the item's own safety mechanisms** in C ("the warning will save them", when the warning is part of the item).
- **Writing hazards as component faults** ("radar fails") instead of vehicle behaviour ("unintended braking").
- **Forgetting people outside the vehicle** in S and C (pedestrians, the car behind).
- **Not writing down assumptions** (attentive driver, hands on the wheel, speed range, steering authority).
- **Never updating it** when the item changes (new speed range, new ODD, new market).

### 13.13 Likely HARA questions: answer skeletons
- **"What is a HARA and what comes out of it?"** → 13.1: vehicle-level malfunctions × situations, rated S, E, C → ASIL → safety goals with a safe state and FTTI.
- **"Hazard vs hazardous event?"** → Unintended braking vs unintended braking at 110 km/h with a car close behind.
- **"Why isn't the failure probability part of Exposure?"** → E rates the situation. Rare failures are handled by the ASIL's hardware metrics. Mixing them would count the probability twice and let a team argue its way down.
- **"Why is loss of an assist function often QM, but unintended action ASIL C or D?"** → The driver is still in charge, so losing the assist leaves them where they'd be without it. An unexpected action takes control away from them.
- **"What's a safe state and FTTI for lane change?"** → Function off, steering handed back smoothly, driver warned. FTTI = time from fault to hazardous event (a few hundred ms for unintended steering at speed, illustrative). Detection plus reaction must fit inside it.
- **"How would you do this on a UAS with no driver?"** → Use an FHA: function × flight phase × failure condition → class → DAL. With no on-board pilot and link latency, "controllability" is low, so you rely on **automatic responses** and **independent protections** (geofence, FTS) and on **where you fly**.
- **"How does HARA connect to SOTIF?"** → SOTIF reuses the HARA's hazards and severity/controllability, then asks whether **insufficiencies** can trigger them without a fault.

**Practice (do one out loud, 3 minutes):** run a mini-HARA on an **electric parking brake**. Hint: the hazardous event that matters is *unintended application while driving at motorway speed* (rear wheels lock, risk of losing control). A reasonable answer is **S3, E4, C2–C3 → ASIL C–D**, plus "not releasing when the driver wants to pull away" is **QM–low**. Explain your C assumption.

---

## 14. Designing a UAV feature: state machine + "how do you know it works?"

Expect questions like **"How would you design the state machine for geofencing / VTOL transition / launch / lost link, and how would you make sure it works?"** They're testing whether you **design for failure** and **plan the proof**, not whether you know their exact numbers. All numbers below are **illustrative**.

**Your bridge (true and confirmed):** "At JLR I wrote the use cases, **state diagrams** and requirements for the radar features, the **signal list** for every module traced to the states, and a **test case for each state**. It's the same method; the aircraft just has more phases and tighter margins."

### 14.1 The answer method: "PHISTOV" (use it for any feature)

| Step | Ask yourself | Say something like |
|---|---|---|
| **P**urpose | What's it for, in which flight phases, what's the safe outcome? | "First I'd pin down the CONOPS: which phases, who the operator is, and what 'safe' looks like." |
| **H**azards | What if it **doesn't act** (miss) or **acts wrongly** (false trigger)? How bad? | "A quick FHA: missing a breach is catastrophic, a false breach loses a mission. That sets the integrity level and puts it on the FCC." |
| **I**nputs/outputs | Signals, sources, rates, **validity flags, timeouts** | "Then a signal list: position, uncertainty, velocity, the fence file, each with validity and a timeout." |
| **S**tates | Nominal, degraded, safe. One initial state. No dead ends. | "States: inside, warning, soft breach, terminate, with entry actions for each." |
| **T**ransitions | Event + **guard** + **debounce / hysteresis** + action + **priority** | "Each transition has a trigger, a guard, a debounce, and an action, plus hysteresis so it can't chatter." |
| **O**perator | What's shown, what can be overridden, what needs confirming? | "The operator always sees the mode, and recovery from a latched state needs an acknowledgement." |
| **V**erify | How do I prove every arrow works, and that it **doesn't** fire when it shouldn't? | "Then the proof: a state × event table for completeness, every transition and threshold tested in SIL, fault injection on the Iron Bird, then a build-up flight test." |

### 14.2 Rules for a good state machine (quality checklist)
- **Power-on goes to a safe state** (disarmed). One initial state.
- **Every state** has an entry action, a defined behaviour and at least one exit (except a final safe state like "terminated").
- **Every transition** = event + guard + debounce + action. Write each one as a **testable requirement with numbers**.
- **Hysteresis and minimum dwell time** so it can't toggle: e.g. enter "low fuel" at 20 %, leave only above 25 % for 10 s.
- **Missing or invalid inputs** go somewhere defined (timeouts, validity flags). Never "undefined".
- **Decide what latches.** Some faults need operator acknowledgement to clear; others recover automatically.
- **Phase-dependent behaviour:** the right reaction in cruise can be wrong during launch or landing (e.g. no RTB in the last metres of a VTOL landing).
- **Priorities** when two events arrive together (14.9).
- **Where it runs:** flight-critical logic on the FCC; independent last-ditch protection (FTS) with its **own power and position source**.
- **The operator always knows the mode**, and the aircraft's next move is **predictable**.

### 14.3 The proof: how you make sure it works
**Say:** "I prove it at every level, and I test that it fires when it should **and doesn't fire when it shouldn't**."

| Level | What you do | Finds |
|---|---|---|
| **Review** | Walk through with pilots/operators and safety; fill the **state × event table** so every cell is decided | Missing transitions, wrong assumptions |
| **Model** | Simulink / Stateflow model; optionally formal checks (unreachable states, deadlocks) | Logic errors before code |
| **SIL** | Requirements-based tests: **every transition**, **boundary values** on every threshold and debounce, **parameter sweeps** (wind, speed, approach angle, timing of the event in each phase) | Most logic and threshold bugs, at thousands of runs |
| **HiL / Iron Bird** | Real FCC and wiring; **fault injection**: unplug the C2 radio, GNSS simulator jamming/spoofing, programmable PSU for voltage sags, kill the FCC to prove FTS independence | Timing, interfaces, real hardware behaviour |
| **Ground test** | Whole aircraft, everything running: triggers from the real GCS, EMI on | Integration and RF effects |
| **Flight test** | **Build-up**: benign triggers first (operator-commanded RTB at safe altitude), then real ones (GCS transmitter off over the range) with abort criteria and an independent FTS ready | Real-world dynamics |
| **CI regression** | All SIL tests run automatically on every software change | Things that break later |
| **In service** | Review mode transitions in flight logs; investigate any unexpected one | Unknowns (the SOTIF "Area 3") |

**Test design techniques to name:**
- **Transition coverage** (every arrow) and **state coverage**.
- **Invalid-event tests:** for each state, the events that must be **ignored**. These come straight from the state × event table.
- **Boundary values:** just inside and just outside each threshold (e.g. 199 m and 201 m, debounce 0.9 s and 1.1 s).
- **Timing:** reaction latency, debounce, timeouts.
- **Combinations:** two triggers at once; checks the priority logic.
- **Negative / false-positive tests:** fly along the edge, noisy inputs, single dropouts → **no** transition.
- **Robustness:** sensor noise, frozen values, jumps.
- **Coverage evidence:** a traceability matrix from requirement to test to result (14.10).

> **Your RCTA link:** "This is what I learned from the radar: the HiL passed, the track didn't. So I always ask what each test level **really exercises**, and I run a coarse-to-fine sweep around every boundary."

### 14.4 Worked example A: geofence (soft + hard) with flight termination
**When:** "Design a geofence feature and tell me how you'd make sure it works."

```
   ┌────────────┐  near fence     ┌────────────────┐ crosses soft ┌────────────────┐
──►│ INSIDE     │────────────────►│ WARNING        │─────────────►│ SOFT BREACH    │
   │ normal     │◄────────────────│ alert operator │              │ loiter → RTB   │
   └─────┬──────┘ clear + hyst.   └────────────────┘              └───┬──────┬─────┘
         ▲                                                            │      │
         │          back inside + operator acknowledges               │      │ crosses HARD
         └────────────────────────────────────────────────────────────┘      │ fence (FTS's own
                                                                             │ position)
                                                                             ▼
                                                                    ┌──────────────────┐
                                                                    │ TERMINATE (FTS)  │
                                                                    │ latched, final   │
                                                                    └──────────────────┘

 Any state: position INVALID > 2 s → treat the whole uncertainty area as the position.
 Use PREDICTED position (now + speed × reaction time), not just where the aircraft is now.
```

**State × event table (the completeness check; every cell is a decision):**

| State \ Event | Near fence (predicted) | Clear + hysteresis | Crosses soft | Crosses hard | Position invalid > 2 s | Operator acknowledges |
|---|---|---|---|---|---|---|
| **INSIDE** | → WARNING | ignore | → SOFT BREACH (fast approach or position jump: skips WARNING) | → TERMINATE | use uncertainty area | ignore |
| **WARNING** | ignore | → INSIDE | → SOFT BREACH | → TERMINATE | use uncertainty area | silence alert only |
| **SOFT BREACH** | ignore | stays (latched) | ignore | → TERMINATE | use uncertainty area | → INSIDE, only if back inside |
| **TERMINATE** | ignore | ignore | ignore | ignore | ignore | ignore (final) |

The table forced two decisions you might have missed: **can you jump from INSIDE straight to SOFT BREACH?** (yes: a fast aircraft or a GNSS jump), and **does SOFT BREACH clear on its own?** (no: it's latched until the operator acknowledges).

**Example requirements (testable, illustrative numbers):**
- **GF-1:** When the predicted position (current position + velocity × 5 s) is within 200 m of the soft fence, the system shall alert the operator within 1 s.
- **GF-2:** When the aircraft crosses the soft fence, the FCC shall command loiter within 1 s, and return to base after 30 s unless the operator commands otherwise.
- **GF-3:** The FTS shall terminate flight within 2 s of crossing the hard fence, using its **own** position source and power supply.
- **GF-4:** If the position is invalid for more than 2 s, the system shall use the position uncertainty area for all fence checks.
- **GF-5:** The fence file shall be integrity-checked (CRC) at arming; a mismatch shall prevent arming.

**How you'd prove it (say it in this order):**
1. **Review** the state × event table with operators and safety.
2. **SIL:** every transition; boundary values (199 / 201 m, 0.9 / 1.1 s); **sweeps** of approach angle, speed and wind pushing the aircraft out (the same coarse-to-fine idea as the radar angle matrix); position jumps and drift near the fence; flying **along** the fence inside it → **no breach** (false-positive test).
3. **Iron Bird:** GNSS simulator replays position errors; **kill the FCC's power** and check the FTS still terminates at the hard fence (independence).
4. **Ground:** load a wrong fence file → arming refused.
5. **Flight:** set a **tight soft fence** around a safe area of the range and fly towards it; check alert, loiter and RTB timing. Test the hard-fence FTS command path on the ground, and only terminate in flight where the range allows it.

### 14.5 Worked example B: VTOL transition (Koios-type: lift motors + pusher)
**When:** "Design the transition from hover to forward flight."

```
┌─────────┐ cmd + alt OK + motors OK    ┌──────────────────┐ V ≥ Vtrans 2 s ┌──────────┐
│ HOVER   │────────────────────────────►│ TRANSITION FWD   │───────────────►│ CRUISE   │
│         │◄────────────────────────────│ lift + pusher    │                │          │
└─┬──┬────┘ ABORT: no Vtrans in Tmax,   └──────────────────┘                └────┬─────┘
  │  ▲      attitude limit, motor fault                                          │
  │  │                                                                           │ cmd / RTB
  │  │                                                                           │
  │  │                                                                           ▼
  │  │                                                                  ┌──────────────────┐
  │  └──────────────────────────────────────────────────────────────────│ BACK-TRANSITION  │
  │                 V < V_hover-safe, lift motors confirmed running     │ lift motors up   │
  │                                                                     └──────────────────┘
  ▼
┌────────┐
│ LAND   │
└────────┘
             Airspeed INVALID (blocked pitot) → don't start the transition;
             in cruise, fall back to GNSS ground speed + wind estimate and widen margins.
```

**Key design points:**
- **Guards to enter TRANSITION:** above a minimum transition altitude, all lift motors healthy, pusher thrust confirmed, airspeed sensor valid, wind within limits.
- **Complete only when airspeed ≥ V_trans** (e.g. 1.2 × stall speed) **for 2 s**. Debounce stops a gust from completing it early.
- **Abort back to HOVER** if V_trans isn't reached within T_max, attitude limits are exceeded, height loss > X m, or a lift motor fails. The abort must be safe **at any point** in the transition.
- **Airspeed is the critical input.** A blocked pitot could make the aircraft think it's flying when it isn't, so cross-check it against GNSS speed + wind estimate and refuse to transition if they disagree.

**How you'd prove it:**
- **SIL sweeps:** mass and CG range, wind and gusts, air density (temperature and altitude), and **fault injection at every point** of the transition (motor out at 0 %, 50 %, 90 %), plus airspeed sensor frozen, offset or noisy.
- **Iron Bird:** real FCC, ESC commands and timing; motor-out fault injection.
- **Flight build-up:** tethered hover → free hover → **partial transitions with commanded aborts** → full transition at a safe altitude → back-transition → gusty conditions. Each step has written abort criteria.

### 14.6 Worked example C: arming and catapult launch (Fregata / Nyan-type)
**When:** "Design the arming and launch sequence." (Here a false trigger can hurt the ground crew.)

```
  ┌──────────────────────────────────┐
  │ POWER-ON + PBIT (self-test)      │─► PBIT fail: no arming, fault shown
  └─────────────────┬────────────────┘
                    ▼ PBIT pass
  ┌──────────────────────────────────┐
  │ SAFE: disarmed, engine inhibited │◄─────────────────┐
  └─────────────────┬────────────────┘                  │
                    ▼ operator starts checks            │
  ┌──────────────────────────────────┐                  │
  │ PRE-FLIGHT: checks + checklist   │──────────────────┤ check fails, timeout
  └─────────────────┬────────────────┘                  │ or operator DISARM
                    ▼ all OK + ARM cmd + pin out        │
  ┌──────────────────────────────────┐                  │
  │ ARMED: on launcher, pin out      │──────────────────┘
  └─────────────────┬────────────────┘
                    ▼ launch detected
  ┌──────────────────────────────────┐
  │ LAUNCH: accel > X g for Y ms     │─► no climb / low airspeed → emergency, FTS
  └─────────────────┬────────────────┘
                    ▼ airspeed + climb confirmed
  ┌──────────────────────────────────┐
  │ CLIMB-OUT: fixed climb profile   │─► lost link here = keep climbing, no RTB yet
  └─────────────────┬────────────────┘
                    ▼ safe altitude reached
  ┌──────────────────────────────────┐
  │ MISSION                          │
  └──────────────────────────────────┘

 Arming needs TWO independent conditions: ARM command AND physical pin.
 Launch detection needs accel > X g for > Y ms AND armed: a knock can't trigger it.
 Failsafes are phase-dependent: in launch/climb-out the 'normal' reaction may be wrong.
```

**How you'd prove it:**
- **Interlock tests:** try every way to start the engine or arm with **one** condition missing → it must refuse (negative tests).
- **Launch detection:** drop and knock tests on the ground with the aircraft disarmed and armed-but-pinned; record the accelerometer to set X and Y with margin; SIL with recorded launcher profiles, including a **weak launch**.
- **Iron Bird:** inject a failed PBIT item, lost GNSS during pre-flight and lost link at each phase.
- **Ground crew procedure (PFMEA):** checklist order, pin flag, who's where when it's armed.

### 14.7 Compact examples (know the shape)

**D. GNSS degraded / spoofed navigation** (Nyan-type GNSS-denied operations)

```
┌────────────┐ GNSS vs IMU differ   ┌───────────┐ confirmed > N s     ┌────────────────┐
│ GNSS-AIDED │─────────────────────►│  SUSPECT  │────────────────────►│ DEAD RECKONING │
└──────┬─────┘                      └─────┬─────┘                     └────────┬───────┘
       ▲                                  │                                    │
       └──────────────────────────────────┘                                    │ uncert. > limit
          consistent again for M s (hysteresis)                                │
                                                                               ▼
                                              RTB / loiter / land; FTS if the uncertainty area
                                              touches the hard fence
```

Key points: detect by **cross-checking** GNSS against IMU, airspeed and baro, plus signal strength. A **slow drift spoof is the hardest case**, so test it on purpose. Dead reckoning is **time-limited** because the error grows. Prove it with a **GNSS simulator** on the Iron Bird: jamming, sudden jumps and slow drift profiles.

**E. Low fuel / energy: return to base**

```
  energy margin = energy left − (energy to fly home in the CURRENT wind + reserve)

  NORMAL
    │  margin < 0
    ▼
  BINGO → return to base now
          (back to NORMAL only if margin > +hysteresis AND the operator confirms)
    │  can't reach base with the reserve
    ▼
  MIN FUEL → divert to nearest safe landing site
    │  can't reach any site
    ▼
  EMERGENCY → land / terminate inside a safe area
```

Key points: the threshold is **dynamic** (distance and headwind), not a fixed percentage. Filter the fuel sensor (sloshing). Test with **wind sweeps**, fuel-sensor faults and estimate errors in SIL.

**F. Electrical load shedding** (protecting the FCC when the bus voltage sags, e.g. VTOL landing at full lift power)

```
  28 V bus   State            What's switched off
  ≥ 25 V     NORMAL           nothing
  < 25 V     SHED 1           payload heaters, non-essential lights
  < 24 V     SHED 2           payload (video lost), mission computer to low power
  < 23 V     ESSENTIAL ONLY   keep FCC, servos, C2, nav → RTB / land

  Restore one step at a time, only above threshold + 1 V for 10 s (hysteresis + dwell time).
```

Prove it on the Iron Bird with a **programmable power supply**: slow sags, fast dips and oscillation around a threshold (checks the hysteresis).

### 14.8 Lost link: the full treatment
The diagram is in **12.11**. Add these when asked how to make sure it works:
- **Requirements:** debounce time, lost-link altitude, rally point, loiter time, recovery site, all **pre-loaded and checked at arming**.
- **Edge cases:** link lost during **launch, transition, landing**, near the **geofence**, at **low fuel**, or with **GNSS also degraded**; the link **flickers** (comes back for 1 s, goes again).
- **Proof:** SIL with the link cut at **every phase and at random times**; Iron Bird by **pulling the radio connector** or attenuating the RF; flight test by switching off the GCS transmitter at a safe altitude over the range, with a safety link or FTS ready.

### 14.9 When failsafes collide: priority logic
**When:** "What happens if you lose the link and run low on fuel at the same time?"

| Priority | Trigger | Action | Why |
|---|---|---|---|
| 1 | Hard fence crossed | Flight termination (independent FTS) | Protects third parties: last line of defence |
| 2 | Loss of control / critical FCC fault | Land now / terminate in a safe area | Can't fly safely anyway |
| 3 | Energy emergency | Land at nearest safe site | Physics: it will come down soon |
| 4 | Soft fence breach | Loiter, then RTB (route stays inside the fence) | Containment |
| 5 | Navigation degraded | Dead reckoning, RTB within the time limit | Position confidence falling |
| 6 | Lost C2 link | Lost-link procedure | Aircraft can still fly itself |
| 7 | Low energy (bingo) | RTB | Planned margin |

**Illustrative.** The real order comes from the FHA and the operators. **Say:** "The most protective action wins, but actions must be **compatible**: lost link + low fuel means divert to the **nearest** site, not home; any RTB route must **respect the geofence**. I'd write it as a priority table and **test the combinations**, not just each failsafe alone."

### 14.10 Verification matrix (what the evidence looks like)
| Req | Requirement (short) | Method | Level | Test case | Pass criteria |
|---|---|---|---|---|---|
| GF-1 | Alert within 1 s when predicted position within 200 m of soft fence | Test | SIL, then flight | Approach sweep: angles 0–90°, speeds min–max, wind 0–max | Alert ≤ 1 s in all runs; no alert at 201 m |
| GF-2 | Loiter within 1 s of soft breach; RTB after 30 s | Test | SIL, Iron Bird, flight | Breach at each phase; operator override | Timing met; override works |
| GF-3 | FTS terminates within 2 s of hard breach on own position/power | Test + analysis | Iron Bird, ground | FCC powered off, then breach replayed | FTS fires ≤ 2 s; independence analysis passed |
| GF-4 | Invalid position > 2 s → uncertainty area used | Test | SIL, Iron Bird | GNSS dropout and jump near fence | Conservative reaction; no missed breach |
| GF-5 | Fence CRC checked at arming | Test + inspection | Ground | Corrupted fence file | Arming refused, fault shown |

**Say:** "Every requirement has a method, a level, a test and a **numeric pass criterion**. Traceability shows 100 % coverage, and the SIL set runs on every software change."

### 14.11 Flight test card (the final step, done safely)
- **Objective:** e.g. verify GF-2 soft-breach loiter and RTB timing.
- **Preconditions:** weather limits, range clear, fence loaded and checked, **FTS armed**, safety pilot or link ready.
- **Build-up:** start with an operator-commanded RTB, then the real trigger.
- **Sequence:** fly at X m towards the tight test fence at Y m/s.
- **Expected:** alert ≤ 1 s, loiter ≤ 1 s after breach, RTB at 30 s.
- **Abort criteria:** unexpected mode, position error > Z m, link margin < W dB, any warning → operator takes over / RTB.
- **Data:** time-synced logs of mode, position, commands and GCS events. Same as my CANoe logging on the proving ground: **one time-synced record** of everything.

### 14.12 Practice questions (2–3 minutes each, use PHISTOV)
- **"Design an auto-land feature."** Hint: states APPROACH → FINAL → FLARE / VTOL DESCENT → TOUCHDOWN → DISARMED; go-around from APPROACH/FINAL on wind limit, position error or landing-zone blocked; **no go-around below a decision height**; touchdown detection with 2 signals (vertical speed ≈ 0 **and** load or motor-current change) to avoid disarming in the air.
- **"How do you know your state machine is complete?"** → state × event table with every cell decided; reviews with operators; model checks for unreachable states and deadlocks; 100 % transition coverage in test.
- **"What if the sensor that triggers a transition fails?"** → validity flags and timeouts, cross-check with another source, a conservative default (don't start the risky transition; widen margins).
- **"How do you stop it toggling between states?"** → hysteresis on thresholds, debounce on triggers, minimum time in a state, and latching for serious events.
- **"How would you test lost link in flight safely?"** → 14.8: build-up, safe altitude over the range, independent FTS, abort criteria.
- **"Two failsafes at once?"** → 14.9.

### 5.6.1 Automotive FMEA example – lane‑change assist

| Item / function | Failure mode | Effect (vehicle level) | Cause | S | O | D | AP | Suggested action |
|---|---|---|---|---|---|---|---|---|
| Radar‑based target detection | Missed vehicle in blind‑spot | Driver unaware of vehicle → lane‑change collision | Radar aliasing, low‑reflectivity vehicle, weather | **9** (collision) | **3** (moderate) | **4** (some detection) | **H** | Add complementary camera, improve algorithm, increase detection‑confidence threshold, add driver‑alert in ambiguous cases |
| Steering torque request generation | Excessive torque command | Vehicle yaw instability, possible loss of control | Software bug in trajectory planner, wrong speed‑profile lookup | **8** | **2** | **3** | **H** | Insert torque‑limit check, unit‑test planner, add redundancy in command path |
| ECU power supply | Intermittent loss of power to lane‑change ECU | System reverts to open‑loop → unpredictable steering | Connector vibration, corrosion | **10** | **2** | **2** (high detection via watchdog) | **M** | Harden connector, add watchdog reset, isolate power bus with fuse |

**Key take‑aways for interview**:
- Show the three‑step chain (cause → failure mode → effect).
- Emphasise that severity drives the action; even a low‑occurrence issue (O=2) with S=10 must be fixed.
- Mention that detection rating of 2 means the defect is likely to be caught early (good), but the action priority is still high because of severity.
- Point out how the mitigation actions feed back into requirements and test cases (e.g., new camera requirement, torque‑limit verification).

---

## 5.x Distinguishing ASIL, SOTIF, and FMEA

### What each term means
| Term | Standard | Focus | When it is applied | Typical output |
|------|----------|-------|-------------------|----------------|
| **ASIL** (Automotive Safety Integrity Level) | ISO 26262 (functional safety) | **Fault‑driven** hazards caused by hardware or software failures. | Early‑stage design & throughout development of safety‑related functions. | A numeric/alphabetic level (A‑D, with D most stringent) that drives safety goals, verification depth, and required diagnostics. |
| **SOTIF** (Safety Of The Intended Functionality) | ISO 21448 | **Performance‑driven** hazards when the system works *as designed* but the intended function is insufficient – e.g., sensor limits, algorithm gaps, foreseeable misuse. | After the functional safety boundary is established, for advanced driver‑assist / autonomy features that rely on perception. | A risk‑assessment matrix (Severity × Controllability × Exposure) and a set of *triggering conditions* and mitigation actions. |
| **FMEA** (Failure Mode and Effects Analysis) | AIAG & VDA Handbook (automotive) – also MIL‑STD‑1629A for aerospace. | Bottom‑up, **enumerates** how each part/function can fail, the resulting effect, cause, and the three classic ratings **S (O) D**. | Performed on any design artefact (hardware, software, process) to discover failure modes early. | A table of failure‑mode rows with S, O, D scores, **RPN** (legacy) or Action‑Priority (AP), and recommended actions. |

### How they relate
1. **FMEA** is the *technique* used to uncover *failure modes*.
2. The **Severity** rating from FMEA feeds into **ASIL** (via the HARA in ISO 26262) – the higher the severity, the higher the possible ASIL.
3. **SOTIF** uses a *different* risk matrix (Severity × Exposure × Controllability) because the hazard originates from *functional insufficiency*, not a fault.  It does **not** produce an ASIL; instead it yields a safety goal or a requirement to restrict the Operational Design Domain (ODD) or add safeguards.
4. In practice, a feature may have **both** an ASIL (for fault‑related hazards) **and** a SOTIF analysis (for performance‑related hazards).  The two analyses are coordinated but kept separate.

### Concrete automotive examples
#### 1️⃣ Lane‑change assist – fault‑driven (ASIL) & failure‑mode driven (FMEA)
- **FMEA row** (see Section 5.6.1) identified a *radar‑based target‑detection miss* with **S=9, O=3, D=4** → high severity, moderate occurrence, moderate detection.
- The **severity** (S=9) maps to **ASIL C** in the HARA (Severity × Exposure × Controllability).  Because the exposure for lane‑change is *high* and controllability *medium*, the resulting ASIL is **C**.
- **ASIL C** drives requirements: redundant sensor, watchdog, fault‑injection testing, and a diagnostic that raises a *lane‑change not available* flag.

#### 2️⃣ Radar‑based RCTA (Rear‑Cross‑Traffic‑Alert) – performance‑driven (SOTIF)
- The radar **works correctly** (no fault) but its **field‑of‑view edge** causes late detection when a vehicle approaches at ~45°.
- **SOTIF analysis**:
  * **Severity** = 9 (potential collision).
  * **Exposure** = moderate (the scenario occurs on a subset of drives).
  * **Controllability** = low (driver may not be able to react in time).
  * Result: high‑risk *unknown‑unsafe* area (Area 3) → mitigation: add a complementary camera, extend the test matrix to cover 45°‑plus angles, and restrict ODD (no lane‑change at high‑speed cross‑traffic).
- No ASIL is assigned because the hazard is **not** caused by a *fault*; instead the SOTIF process produces a **safety goal** (“detect cross‑traffic within 0.5 s”) and associated verification tasks.

#### 3️⃣ Power‑train brake‑by‑wire – mixed case
- **Fault mode**: loss of brake‑by‑wire actuator power → **ASIL D** (catastrophic loss of braking).
- **Performance mode**: brake‑by‑wire algorithm under extreme hot‑weather conditions may **delay** actuation by 200 ms → **SOTIF** risk (high severity, low exposure, moderate controllability).  The mitigation is a *fallback* to a hydraulic backup and a temperature‑monitoring watchdog.

### Quick cheat‑sheet for the interview
- **ASIL** → *“What can go wrong because something *fails*?”*  Use HARA → ASIL → safety goals → verification.
- **SOTIF** → *“What can go wrong even when nothing has failed?”*  Identify performance limits, misuse, and ODD; produce safety goals and mitigation.
- **FMEA** → *“List every way a part can fail and its effect.”*  Generates S, O, D ratings; feeds severity into ASIL and can also be used to spot SOTIF‑type performance gaps (by asking “what if the sensor is *insufficient* rather than *failed*?”).
- **Remember**: ASIL and SOTIF are *different risk‑assessment families*; they rarely replace each other but often coexist for the same feature.

---

## 15. Systems engineering interview question bank

Use these as answer structures, not scripts. Keep personal examples honest: connect to confirmed automotive experience, then explain how you would apply the same method to a UAS. Aircraft-specific values and state behaviour must come from the programme's requirements and safety assessment.

### 15.1 The systems engineering lifecycle
**When:** "Walk me through systems engineering from a customer need to delivery."

```
 Need / CONOPS / stakeholders
        │ validate the need
        ▼
 System requirements + hazards ◄────► System architecture / trade studies
        │ allocate                         │
        ▼                                  ▼
 Subsystem requirements + ICDs          Safety requirements / interfaces
        │                                  │
        └──────────────┬───────────────────┘
               ▼
           Design and implementation
               ▼
           Integration and V&V
               │
        verify requirements / validate need
               ▼
         Acceptance, operation, feedback

 Throughout: configuration control · traceability · risk management · reviews
```

**Model answer:** "I start with the CONOPS and stakeholder needs, then agree measurable system requirements and identify hazards and constraints. I develop and compare architectures, allocate requirements to subsystems, and define the interfaces. As the design is built, I manage changes and risks, integrate in stages, and verify each requirement with planned evidence. I also validate that the delivered system meets the original operational need. In service, incidents and feedback update the requirements and risk picture."

### 15.2 Requirements and traceability

**Q: "How do you turn a vague request into a good requirement?"**

**Model answer:** "First I clarify the mission and operating conditions with the stakeholder. Then I make the requirement singular, unambiguous and verifiable, with measurable limits and defined conditions. For example, instead of 'long endurance', I would specify a minimum flight duration at a defined payload, speed, altitude, weather condition and reserve. I would record the rationale, owner, verification method and links to the parent need and child requirements. I would leave unknown values as decisions to resolve, not invent them."

**Q: "What does traceability give you?"**

**Model answer:** "Downward traceability shows that every need is addressed by design and verification. Upward traceability shows why each requirement and test exists. When a requirement changes, the links show which architecture elements, interfaces, safety analyses and tests need impact assessment. Traceability is evidence of coverage, but it doesn't replace engineering judgement or test quality."

### 15.3 Architecture, interfaces and trade studies

**Q: "How would you define the system boundary and architecture for a UAS?"**

**Model answer:** "I would include the air vehicle, payload, data links, ground segment, operators, launch and recovery equipment, maintenance and operating environment. Within the aircraft, I would separate flight-critical control from mission autonomy and payload functions, define the information and command paths between them, and identify power, timing, mechanical, thermal and RF interfaces. I would also capture external interfaces such as airspace constraints and GNSS. I would use the architecture in 12.10 as a starting point, then refine it against the actual CONOPS and hazards."

**Q: "How do you choose between two architectures?"**

**Model answer:** "I first agree the evaluation criteria and constraints with stakeholders: safety, performance, mass, power, cost, schedule, maintainability and growth. I identify viable options, assess them consistently with analysis or test evidence, and record assumptions and sensitivities. I don't hide a safety constraint inside a weighted score: an option that fails a mandatory safety requirement is not made acceptable by being cheaper. I document the decision and the risks that remain."

**Q: "What belongs in an interface definition?"**

**Model answer:** "The physical and logical boundary: connector and pinout, power range and peak current, message definitions, units, rates, timing, validity and timeout behaviour, environmental limits, ownership, and behaviour on reset or link loss. For a payload I would also cover mass, centre of gravity, mounting, cooling, EMI and what happens during load shedding. I would assign owners and verification evidence to the interface requirements."

### 15.4 State-machine design

**When:** "How would you design and review an aircraft mode state machine?"

```text
 SAFE / DISARMED
     │ pre-flight checks pass; operator arms
     ▼
   READY / ARMED ───── checks fail / disarm ─────► SAFE
     │ valid launch detected
     ▼
   LAUNCH
     │ climb and navigation confirmed
     ▼
   CLIMB-OUT ───────── safe mission conditions ─► MISSION
     │                                             │
     │ critical fault / lost-link policy           │ mission complete / RTB
     └──────────────────┐                          ▼
              ▼                      RECOVERY
           DEGRADED                         │ landed, disarmed
              │                            ▼
              └── fault cleared /      SAFE
                recovery action

 Illustrative only: real modes, guards, priorities and recovery actions are
 aircraft- and phase-specific. A hard safety action may be an independent path.
```

**Model answer:** "I define the purpose and safe outcome first, then list states, inputs, outputs and failure conditions. Each transition needs a trigger, guard, timing or debounce rule, action and priority. I check invalid inputs, simultaneous events, aborts, latching and operator indications. I review a state-by-event table for completeness, model the logic, then test transitions and non-transitions at boundaries in simulation, on representative hardware and in a controlled flight-test build-up."

**Example state/event table:**

| State | Event | Decision / action |
|---|---|---|
| SAFE | Arm command, checks pass, interlocks valid | Enter READY; otherwise remain SAFE and report the inhibit |
| READY | Launch detected and launch conditions valid | Enter LAUNCH; ignore isolated vibration or invalid sensor data |
| CLIMB-OUT | Link lost | Apply the defined climb-phase lost-link behaviour; don't blindly use the cruise response |
| MISSION | Navigation invalid | Enter the specified degraded mode, alert the operator, and limit operation by the approved policy |
| Any airborne mode | Critical fault | Execute the phase-appropriate safety action; record and report the cause |

**Q: "How do you know the state machine is complete?"**

**Model answer:** "I enumerate every state against every relevant event, including invalid, late, duplicated and simultaneous events. Every cell says transition, ignore, remain, or take a defined fallback action. I then check reachability and dead ends, review it with operators and safety, and measure state, transition, boundary and negative-test coverage."

### 15.5 Verification, validation and integration

**Q: "What's the difference between verification and validation?"**

**Model answer:** "Verification asks whether the system meets its specified requirements: did we build it right? Validation asks whether those requirements and the delivered system meet the operational need: did we build the right thing? I plan both, because a system can pass every test against an incomplete or incorrect requirement set."

**Q: "How would you build a verification strategy?"**

**Model answer:** "For each requirement I choose inspection, analysis, demonstration or test, define pass criteria and identify the required configuration and evidence. I use simulation for breadth, hardware rigs for real interfaces and timing, ground tests for integrated effects, and flight tests for real aircraft behaviour. I state what each stage emulates and what it exercises, then build evidence progressively with safety-approved entry and exit criteria."

| Requirement example | Candidate method | Evidence / pass criterion |
|---|---|---|
| Installed payload mass and centre of gravity | Inspect / measure | Recorded measurements within approved limits |
| C2 link performance | Analysis, then test | Link-budget assumptions confirmed by ground/flight results against agreed limits |
| Lost-link behaviour | Test at each relevant phase | Correct mode and action within approved timing; no unintended transition on brief dropouts |
| Flight-control timing | Analysis and hardware test | Worst-case timing within allocated budget under representative load |

**Q: "A rig passes but the aircraft fails in flight. What do you do?"**

**Model answer:** "First I contain the risk and pause or constrain testing as appropriate. I preserve time-synchronised logs and configuration details, compare a passing rig run with the failing flight, and identify what the rig emulated versus exercised. I form hypotheses from the differences, reproduce them at the safest suitable level, and change one variable at a time where possible. After fixing the cause, I add regression coverage and update requirements, models or procedures so the gap doesn't recur."

### 15.6 Safety, change and working with stakeholders

**Q: "How do safety analyses influence the design?"**

**Model answer:** "I use the functional hazard assessment to understand hazardous failure conditions by function and flight phase. Architecture-level analyses test whether the design can meet the safety objectives; FMEA looks bottom-up at component and interface failures, and fault trees examine combinations leading to a top event. I also consider performance limitations and operating conditions where nothing has failed. The outputs should change requirements, architecture, monitoring, procedures and verification, and remain linked in the hazard log and safety argument."

**Q: "A requirement changes late. What do you do?"**

**Model answer:** "I clarify the reason and urgency, then assess impact through traceability: affected requirements, interfaces, mass/power/performance budgets, safety analyses, software/hardware, test evidence, cost and schedule. I present options and residual risks to the change authority, update the approved baseline if accepted, and plan targeted regression and re-verification. I don't quietly change a downstream design while leaving the requirement baseline untouched."

**Q: "What if two teams disagree about an interface?"**

**Model answer:** "I bring the discussion back to the system requirement, use cases and measurable constraints. I make assumptions and ownership explicit, compare options against agreed criteria, and capture the decision, rationale and verification responsibility in the interface documentation. If it affects safety, certification, cost or schedule beyond my authority, I escalate with evidence and clear choices rather than letting ambiguity persist."

**Q: "How would you approach your first 90 days?"**

**Model answer:** "I would learn the aircraft, CONOPS, safety and assurance approach, requirements and configuration tools, and how the team makes design decisions. I would spend time with software, hardware, flight controls, operators and test teams, and review one system boundary and its open risks. Then I would take ownership of a bounded deliverable, such as an interface, requirement set or verification campaign, and agree what successful completion looks like with my manager."

### 15.7 Quick interview reminders
- Start with the operational need and system boundary; don't jump straight to a component.
- State assumptions, especially where values are illustrative or programme-specific.
- Keep cause, failure mode and effect distinct; distinguish faults from performance limitations.
- Include interfaces, operators, maintenance and environment, not only onboard hardware and software.
- Tie every major design decision to a requirement, risk, trade-off or verification result.
- Be explicit about what you personally did versus what you understand or would do.
