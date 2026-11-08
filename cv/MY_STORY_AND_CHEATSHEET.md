# My Story (Warwick to today) and Interview Cheat Sheet

## Part 1: The story

**Before Warwick.** I studied Mechanical Engineering at Ege University in Izmir. For my final project our team designed and built a 6-DOF Stewart motion platform: SolidWorks for the design, MATLAB for the modelling, and an Arduino for control. I did the wiring and the Arduino code to command each servo. We got each actuator moving to the angle we commanded, but didn't finish full pose control before the project ended. That's where I learned I like building real things that move. During my degree I did an internship at TEMSA, calculating power and torque for a new electric bus powertrain in MATLAB/Simulink. For about three years I also taught science and space technology part-time at Space Camp Turkey, which taught me to explain technical ideas simply.

**Warwick (2017–2018).** I moved to the UK for an MSc in Sustainable Automotive Engineering at WMG, University of Warwick, and graduated with a 2:1 (Merit). The course covered hybrid and electric vehicle systems, system modelling in Simulink, C++ and Ansys. My dissertation designed a test to find the variables of a thermal model for an electric motor stator: where the thermocouples would go, the enclosure and the method. I used MotorCAD's thermal network to understand the heat paths. The test bench wasn't built within the project.

**AVL (11/2018 – 10/2021).** I joined AVL Powertrain UK in Coventry. AVL is an engineering services company, so they placed me with their client.
- **At Jaguar Land Rover (about 2 years)**, I was feature owner for three corner-radar features: Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. I owned them from requirements to testing:
  - wrote use cases, state diagrams and requirements in DOORS and MKS Integrity (ASPICE V-model), breaking high-level requirements down to low-level ones
  - defined the signal list for every module and traced it against the state machines
  - wrote test cases per state, ran them on HiL and ViL rigs, in vehicles and on the proving ground, and tracked defects in RTC/RQM
  - I was the link between AVL, JLR and the radar supplier.
- **Best story:** an alert was firing late at boundary conditions. I re-ran the tests, analysed the logs in CANoe/CANape and traced the cause to the radar's field of view, since detections get weaker at the edges. I agreed a fix with the supplier without adding false alerts.
- **Other work at AVL:**
  - requirements for ACC, Lane Keep Assist, Highway Assist and Lane Change Assist
  - ISO 26262 safety requirements for a lane change feature; trained in ISO 26262 and SOTIF
  - a Simulink + IPG CarMaker project comparing a real vehicle with a dyno using sensor emulation and with pure simulation. I calibrated the model to real recordings and swept the steering PID values.
- **At the LEVC (London Taxi) factory**, I was the local engineer for returned faulty e-machines. I did multimeter checks, pulled data from proprietary loggers and sent it to the developers and suppliers for root cause analysis.

**FiveAI / Bosch (10/2021 – 11/2026).** I moved to FiveAI in Cambridge (later part of Bosch) as Lead Application Engineer, working on an L4 automated driving system.
- **ADA project with Volkswagen Group.** FiveAI supplied the simulation tooling. I showed and taught partner engineers across the cluster how to use our toolchain. That customer work grew into a **solutions team**, and I was a founding member (Simulation EcoSystem). We diagnosed problems across the partners' shared toolchains, maps (SDB/XODR) and add-on tools, worked out where the fault really was, and got the right team to fix it.
- **Test scenarios.** I wrote 120+ parameterised OpenSCENARIO 2 scenarios that generate thousands of test cases: Euro NCAP junction tests and UN R79 automatic lane change. I set KPI and pass/fail criteria, such as comfort acceleration limits, checked against 1,000+ hours of data. I also made Euro NCAP templates.
- **Team lead (1 year).** I led five engineers on L4 scenario work. I taught them the tools and evaluation logic, and split the work so creation and evaluation ran in parallel. This wasn't formal line management.
- **Tools and AI.** I worked in the project monorepo with a dev container, ran simulations locally and through the dtflow CI pipeline, raised pull requests, and used SSH to reach the GPU cluster. With AI help I built Python tools: a JSON parameter GUI, an uploader, and pipelines into dashboards. I built a Copilot-based helper that turns regulation and NCAP rules into scenarios from modular blocks. It's now used across the project and increased scenario output by about ten times. I teach others to check AI output, not just trust it.

**Now.** I want to get back closer to vehicles and customers and own a feature or test area again, then grow into a lead role. Outside work, I fix my own cars, build my own PCs, and I'm learning applied AI engineering in my own time.

---

## Part 2: Cheat sheet

**Numbers**
- ~8 years experience (since 11/2018)
- 3 radar features owned at JLR
- 120+ scenarios, generating thousands of test cases
- 1,000+ hours of data
- Team of 5, for 1 year
- ~10x scenario output with the AI helper

**Education**
- MSc Sustainable Automotive Eng, WMG Warwick, 2:1: stator thermal model, MotorCAD, Simulink
- BSc Mech Eng, Ege: built a 6-DOF Stewart platform (SolidWorks, MATLAB, Arduino)

**AVL at JLR (11/2018 – 10/2021)**
- Feature owner: RCTA, BSM, Rear Pre-Crash (corner radar)
- Use cases, state diagrams, requirements in DOORS / MKS (ASPICE)
- Signal lists traced to state machines
- Test cases per state; HiL, ViL, vehicle, proving ground
- CANoe / CANape log analysis
- RTC / RQM defects
- Link between AVL, JLR and the supplier
- Story: late alert traced to the radar FOV edge; fix agreed with the supplier
- ACC, LKA, Highway Assist, Lane Change Assist requirements
- ISO 26262 requirements (lane change); trained in ISO 26262 and SOTIF
- CarMaker + Simulink: real vehicle vs dyno vs simulation; PID sweep
- LEVC: faulty e-machine returns, multimeter checks, logger data to suppliers

**FiveAI / Bosch (10/2021 – 11/2026)**
- ADA with Volkswagen Group: trained partner engineers on our toolchain
- Founding member of the solutions team (SimEco): cross-toolchain triage
- 120+ OSC2 scenarios: Euro NCAP, UN R79
- KPI and pass/fail criteria, 1,000+ hours of data
- Led 5 engineers for 1 year (technical lead, not line manager)
- Monorepo, dev container, dtflow CI, PRs, SSH to the GPU cluster
- Python tools with AI: GUI, uploader, dashboards
- Copilot scenario helper used across the project; teach people to check AI output

**Soft skills**
- Always customer-facing; approachable and calm
- Explain clearly (taught at Space Camp)
- Finds the real cause, not the symptom

**Honest gaps**
- No ROS, formal line management, deep FlexRay/Ethernet work, IP networking, oscilloscope use or SQL
- Python: I write it with AI help. C++: I can read it.
- Answer: "Not yet, but I learn fast, for example OSC2 and AI tools."

**Goals**
- Short term: closer to vehicles and customers, owning a feature or test area
- Long term: lead a team or work package; principal or lead systems role
