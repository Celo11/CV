# Interview Prep: System & Software Test Engineer (Suspension & Seating) — Nuneaton

> **Agency / Client:** Precision Resource Group : iO Advanced Mobility  
> **Location:** Nuneaton, Warwickshire (15–20 mins drive from Coventry CV5)  
> **Salary Range:** £60,000 – £70,000 / year  
> **Core Domain:** Automotive suspension and seating systems, bench and HiL testing, diagnostics (fault codes / DTCs, CAN), and requirements-based verification.

---

## 1. 90-Second Introduction (Say it naturally, don't read)

"I'm Celal. I'm a mechanical engineer with eight years in automotive systems, software testing and validation, and I live locally in Coventry, about 15 minutes from Nuneaton.

When I started at AVL, a project needed people in ADAS, and after joining the team they sent me on-site to Jaguar Land Rover for two years as feature owner for three corner-radar features. That is where I found how much I enjoy hands-on testing with real vehicles and test beds. I took features from requirements in DOORS and MKS Integrity under the ASPICE V-model through to writing test cases per state and testing in vehicles and on the proving ground, using Vector CANoe and CANape on CAN and working daily between JLR and the Tier 1 radar supplier. I also drove a circuit at HORIBA MIRA in Nuneaton to capture vehicle dynamics data for AVL's DrivingCube ViL project.

For the last five years at FiveAI, now part of Bosch, my role moved into test software development for an L4 automated driving system. I learned Python, built internal test tools and pipelines, and diagnosed error logs between APIs and simulation tools across more than 1,000 hours of test data. With Volkswagen Group withdrawing from the project, my role at Bosch ended by redundancy today, so I am immediately available.

Now I want to get back into the lab and build my career around hands-on system and hardware testing, which is why this role in Nuneaton really appeals to me."

---

## 2. How Your Experience Maps to the Job Specification

| Role Requirement | Your Confirmed Experience |
| :--- | :--- |
| **Test Beds & Vehicle Verification** | Wrote test cases per system state and ran vehicle / proving-ground verification at JLR, plus worked on AVL's **DrivingCube** vehicle-in-the-loop dyno test bed (GNSS ground truth, airstrip & HORIBA MIRA runs, monitoring logging health). *(Note: you did not operate the dSPACE HiL rig yourself; the HiL team ran those tests.)* |
| **Diagnostics & Bus Tools** | **Vector CANoe** and **CANape** on vehicle CAN: synchronising camera timestamps, CAN global time and radar module counters in a CANoe layout to compare failing and passing runs. Reading fault codes (DTCs) when modules failed to activate, checking fuses, and powering modules from a 12 V bench supply. |
| **Root Cause Analysis** | **RCTA boundary story:** Passed in HiL testing (where simulated objects bypassed the radar antenna) but gave no alert or alerted late (~0.5 s vs 2 s requirement) on the proving ground at a 45° approach. Designed a coarse-to-fine test matrix (30/45/60°, 10–40 mph target, ego reversing up to 10 mph in 2 mph steps), traced the delay to low target confidence near the edge of the radar's field of view in CANoe, and ran boundary tests on site with the supplier to verify a calibration fix. |
| **Standards & Requirements** | **ASPICE V-model**, high- to low-level requirements decomposition and state diagrams in **IBM DOORS** and **MKS Integrity**, module input/output signal lists, defect tracking in **RTC / RQM**, and **ISO 26262** safety requirements + **FMEA** for a lane change feature. |
| **Scripting** | **Python** tools built with AI help at FiveAI (JSON parameter GUI, STAX uploader, data pipelines into dashboards) and 5 years using Linux as your main workstation. |
| **Honest Gaps (State Upfront)** | Have not worked on active suspension or seating systems yet (though your BSc team built and wired a **6-DOF Stewart motion platform** in SolidWorks, MATLAB and Arduino, and you calibrated a **Simulink / IPG CarMaker** vehicle dynamics model using data driven at HORIBA MIRA). Did not operate the HiL rig yourself at JLR, and have not used **NI VeriStand / TestStand, CAPL, Jama or Polarion** yet, having used CANoe/CANape, DOORS and Python. |

---

## 3. Questions to Ask the Recruiter / Interviewer

1. *"Which company is the end client in Nuneaton (e.g. at MIRA Technology Park), and are the systems active suspension, seating, or both?"*
2. *"Which HiL and bench platforms does the team use day to day (e.g. dSPACE, NI VeriStand, or custom benches)?"*
3. *"How is the role split between setting up and running tests on the bench/HiL versus writing test cases and analysing logs?"*
