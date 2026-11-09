# Zoox — Staff / Senior Engineer, Chassis Actuators (Steering & Braking Systems) Interview Prep

> **Company / Location:** Zoox (Amazon subsidiary) — Banbury, Oxfordshire (easy commute down the M40 from Coventry CV5, no relocation needed)  
> **Team:** Chassis Actuator Team (Steering & Braking Systems for Zoox's bidirectional autonomous Robotaxi)  
> **Note on Levelling & Honesty:** Zoox explicitly states that candidates do not need to match every expectation, that the posting covers a range of levels, and that they use AI tools to check for consistency across application materials. Keep every answer 100% grounded in your confirmed facts.

---

## 1. 90-Second Introduction (Say it naturally, don't read)

"I'm Celal. I'm a mechanical and automotive engineer—I did my BSc in Mechanical Engineering and my MSc in Sustainable Automotive Engineering at WMG, University of Warwick—and I have eight years of experience sitting right between physical vehicle systems and autonomous driving. I live in Coventry, so Banbury is an easy commute for me down the M40.

At AVL I spent two years based on-site at Jaguar Land Rover as feature owner for three corner-radar features, including Rear Cross Traffic Alert with a braking request, and also wrote requirements for Lane Keep Assist, Lane Change Assist, Highway Assist and ACC. I managed requirements in DOORS and MKS Integrity under the ASPICE V-model, wrote ISO 26262 safety requirements and took part in a lane-change FMEA, worked daily with the Tier 1 supplier, and ran validation in vehicles and on the proving ground using Vector CANoe and CANape on CAN. On AVL's DrivingCube ViL project, I also built Simulink and IPG CarMaker scenarios to find the steering-wheel torque needed across turn radii, captured vehicle data on the airstrip and at HORIBA MIRA, and calibrated the simulation steering torque PID controller.

For the last five years at FiveAI, now part of Bosch, I worked on an L4 automated driving stack, turning UN R79 automatic steering and Euro NCAP requirements into KPIs across 1,000+ hours of test data—including finding a curvature-related drop in lane-change success that led to a steering controller fix. Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy, so I am immediately available and keen to get back to hands-on hardware and vehicle testing."

---

## 2. How to Handle the Core Gaps Upfront

### Q1: "You haven't released 3D CAD / 2D GD&T drawings in CATIA for production steer-by-wire or brake-by-wire actuators, and you have 8 years of experience rather than 12+. Where do you see yourself fitting on the team?"
> "I wanted to be completely upfront about that in my CV and cover letter. I haven't designed production steer-by-wire or brake-by-wire mechanical hardware in CATIA or authored ASME Y14.5 GD&T production drawings—my CAD work has been in SolidWorks, and I'm just starting to learn the basics of GD&T. And I have eight years of experience rather than twelve, so I'm completely open to whichever level—such as Senior Engineer—you find appropriate.
> 
> Where I add immediate value is on the other half of this role's scope:
> 1. **Bridging physical chassis behaviour and L4 autonomy:** I've worked on both sides—calibrating steering torque PID controllers on AVL's DrivingCube ViL test bed and evaluating L4 UN R79 steering KPIs across 1,000+ hours of data at FiveAI.
> 2. **Requirements, ISO 26262 & Tier 1 supplier management:** I spent two years on-site at JLR decomposing system-to-component requirements in DOORS, defining module signal lists, writing ISO 26262 requirements, and driving supplier fixes.
> 3. **Vehicle validation & Vector CANoe/CANape:** I'm hands-on in the vehicle and on the track—setting up test matrices, synchronising CAN and sensor logs in CANoe, and isolating whether a fault is in the hardware, calibration, or autonomy stack."

---

## 3. Key Technical Stories for Zoox

### Story 1: Steering Torque PID & Vehicle-in-the-Loop Correlation (AVL DrivingCube)
- **Goal:** Compare real vehicle behaviour, a chassis dyno with sensor emulation (DrivingCube), and pure simulation (Simulink / IPG CarMaker).
- **What you did:**
  - Built CarMaker scenarios with the ego driving on circles of parameterised radius to determine the steering-wheel torque required at each radius.
  - Fitted an external GNSS system to the vehicle for position ground truth during airstrip tests.
  - Drove the car on the airstrip while a colleague on the logger injected steering torque at set speeds to record the vehicle's response, and drove a circuit at HORIBA MIRA whose corners provided the data to calibrate the PID controller on the simulation side.
  - Ran parameter sweeps on the steering torque PID gains in Simulink/CarMaker to correlate the model to real vehicle recordings, and monitored logging health during DrivingCube runs.

### Story 2: L4 Steering / Lane-Change KPIs & Curvature Finding (FiveAI / Bosch)
- **Goal:** Validate L4 automatic lane change and steering behaviour against UN R79, Euro NCAP, and customer requirements across 1,000+ hours of data.
- **What you did:**
  - Wrote 120+ parameterised OpenSCENARIO 2 scenarios generating thousands of test cases.
  - Defined pass/fail and KPI criteria including lane-change success/failure counts, lateral acceleration, longitudinal comfort accel/decel limits, and recorded road curvature as a metric.
  - Found that lane-change success dropped above a certain road curvature that was still within the operational specification, which led to a steering controller fix by the controls team.

### Story 3: Braking Request / Corner Radar Boundary Fix with Tier 1 Supplier (AVL at JLR)
- **Goal:** Rear Cross Traffic Alert with a braking request had to alert at least 2.0 s before collision.
- **What you did:**
  - In HiL testing (run by the HiL team, where simulated objects were fed to the ECUs on the vehicle CAN bus, bypassing the radar antenna), all tests passed.
  - On the proving ground at a 45° parking approach, the system either failed to alert/brake or triggered only ~0.5 s before impact.
  - Designed a coarse-to-fine test matrix across approach angles (30/45/60°), target speeds (10–40 mph), and ego reversing speeds (up to 10 mph in 2 mph steps).
  - Synchronised camera timestamps, CAN global time, and the radar module counter in a Vector CANoe layout, proving that targets near the edge of the radar's field of view reached high confidence too late.
  - Ran boundary tests on site with the Tier 1 supplier engineer and verified a calibration fix across three candidate calibrations without introducing false positives.

---

## 4. Questions to Ask the Zoox Interviewers

1. *"Since Zoox's vehicle is bidirectional with four-wheel steering and redundant by-wire braking, how is the responsibility split between the Chassis Actuator team in the UK and the controls / autonomy teams in Foster City?"*
2. *"How much of this role focuses on Tier 1 supplier management, requirements, and HiL / vehicle validation versus in-house mechanical CAD design?"*
3. *"What does the first 12 months in the UK office look like before the relocation to Foster City?"*
