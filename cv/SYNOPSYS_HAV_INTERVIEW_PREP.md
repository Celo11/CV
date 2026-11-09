# Synopsys HAV (Hardware-Assisted Verification) — Field Support & Validation Interview Prep

> **Role Context:** Field Support & Test / Validation Engineer in the **Hardware-Assisted Verification (HAV)** team (supporting Synopsys's emulation and prototyping hardware systems at customer sites).  
> **Core Job Profile:** On-site customer installation and maintenance of hardware systems, preparing chassis, mounting mechanical parts on electronic boards, wiring cabling, collaborating with hardware engineering and manufacturing on failure analysis and corrective actions, Linux use, and domestic/international travel.

---

## 1. 90-Second Introduction (Say it naturally, don't read)

"I'm Celal. I'm a mechanical engineer with eight years in test, validation and customer-facing support, and I want to build the next stage of my career around hands-on hardware work at customer sites.

At AVL I spent two years based on-site at Jaguar Land Rover as feature owner for three corner-radar features, running tests in vehicles and on the proving ground, supporting AVL's DrivingCube ViL test bed, and working between the customer, AVL and the hardware supplier. When modules failed to activate in vehicle tests, I read fault codes, checked fuses, and powered modules from a 12 V bench supply to find the cause. At the LEVC London Taxi factory, I also inspected about 20 returned faulty range-extender generators, carrying out multimeter checks at connector pins, powering the control unit from a bench supply to download logs with the supplier's tool, and sending the data and reports to the supplier for root cause analysis.

For the last five years at FiveAI, now part of Bosch, I trained Volkswagen Group partner engineers on our simulation toolchain and was a founding member of our solutions team. I used Linux as my main workstation, diagnosed errors from logs between APIs and simulation tools, and built Python utilities and reporting pipelines. Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy today, so I am immediately available and happy to travel across the UK and internationally."

---

## 2. How to Handle the Key Questions Honestly

### Q1: "You haven't worked with semiconductor emulation or prototyping hardware, or written bash / tcsh scripts. How will you get up to speed?"
> "I'll be completely honest about that: my background is in automotive electronic systems, test rigs and simulation rather than semiconductor emulation boxes, and while I have used Linux as my main workstation for five years and write Python tools, I haven't written bash or tcsh scripts beyond everyday terminal use.
> 
> What I bring is the hands-on foundation:
> - **Mechanical and electrical integration:** I have a mechanical engineering degree, build my own desktop PCs (chassis prep, board mounting, cabling), repair my own cars with a multimeter and workshop manuals, wired a 6-DOF motion platform at university, and soldered motor drive cables onto a PCB.
> - **Methodical hardware checks and reporting:** At LEVC I followed a test procedure across ~20 returned generators—multimeter checks across connector pins, bench-powering the control unit to download logs, and sending clean reports to the supplier.
> - **Learning quickly:** When I moved from hands-on vehicle testing at AVL into test software development on Linux at FiveAI, I picked up Python, dev containers and log diagnosis on the job. I learn fastest when I can get hands-on with the hardware."

---

### Q2: "Tell me about a hardware or system failure you analysed with a supplier."
> **Story 1 (LEVC factory returns):**
> - Inspected about 20 returned faulty range-extender generators at the LEVC factory following a predefined test procedure.
> - Performed multimeter checks at specified connector pins (phase-to-phase resistance, continuity), powered the control unit from a low-voltage bench supply so the supplier's logging device could connect and download the fault logs, and sent the measurements and logs to the supplier's engineering team for root cause analysis.
> 
> **Story 2 (JLR corner radar boundary failure):**
> - Rear Cross Traffic Alert passed all tests in HiL testing (where simulated objects bypassed the radar antenna), but gave no alert or alerted late (~0.5 s vs 2 s requirement) on the proving ground at a 45° approach.
> - Designed a coarse-to-fine test matrix, synchronised camera timestamps, CAN global time and the radar module counter in CANoe, and showed that targets near the edge of the radar's field of view reached high confidence late.
> - A supplier engineer came on site, we ran the boundary tests together, and we verified a calibration fix across three candidate calibrations without adding false alerts.

---

### Q3: "Tell me about supporting customers when their tools or systems fail."
> - On the ADA project with Volkswagen Group, FiveAI supplied the simulation toolchain. I trained partner engineers across the cluster on how to use it, which grew into the Simulation EcoSystem solutions team where I was a founding member.
> - When partner engineers hit failures across shared toolchains, maps (SDB/XODR) and add-on tools, I read the error logs between APIs and simulation tools, isolated which component or team owned the fault, and worked with the right development team until the user was unblocked.

---

## 3. Questions to Ask the Synopsys Interviewers

1. *"What does the training and shadowing process look like for a new field engineer learning the ZeBu and HAPS hardware platforms?"*
2. *"What are the most common hardware or cabling issues your team sees when installing or maintaining systems at customer sites?"*
3. *"How is the role split between customer-site travel and working with manufacturing / hardware engineering at the home site?"*
