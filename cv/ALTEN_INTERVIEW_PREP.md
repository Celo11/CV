# ALTEN Interview Prep

> **Check first:** the CV you sent ALTEN (`CV_Alten.pdf`) says AVL **12/2017**. The real start date is **11/2018**, and you were at JLR for 2 years. Correct this early in the interview, for example: "One correction to my CV: I joined AVL in November 2018, not 2017. It was an error on my part."
> Also, I don't know the exact role. This prep assumes an **ADAS / systems engineering consultant** role, based on how that CV was pitched.

---

## 1. Introduction (about 90 seconds, say it, don't read it)

"I'm Celal. I'm a mechanical engineer with nearly eight years in ADAS and automated driving, mostly in requirements, testing and finding the root cause of problems.

I started at AVL, working on-site at Jaguar Land Rover as feature owner for three radar features: Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. I wrote the requirements and state diagrams, tested on HiL and ViL rigs and on the proving ground, and I was the link between AVL, JLR and the radar supplier.

For the last four years I've been at FiveAI, now part of Bosch, working on an L4 automated driving system. I write test scenarios in OpenSCENARIO 2 for Euro NCAP and UN R79. On the ADA project with Volkswagen Group I trained partner engineers on our simulation tools, and that turned into a solutions team I helped start. For a year I also led a team of five.

My strengths are taking ownership of a feature, getting to the real cause of a problem, and working well with customers.

Short term, I want to get back closer to vehicles and customers, on an OEM programme where I can own a feature or a test area again. Long term, I'd like to lead technical teams or a work package, and grow into a principal or lead systems role."

**Tip:** your AVL time *was* a consultancy model: an engineering services company placing you at an OEM. Say that clearly, because it's exactly what ALTEN does.

---

## 2. ALTEN: key facts

| | |
|---|---|
| What they do | Engineering and technology consultancy (ER&D services). They supply engineers and run projects for clients' R&D and IT teams. |
| Founded | 1988 in France by three engineers (Simon Azoulay is still CEO / chairman). Headquarters in Boulogne-Billancourt, Paris. Listed on Euronext Paris. |
| Size | About **57,400 employees** and **€4.1bn revenue** (2025). |
| Reach | About **30 countries** across Europe, North America, Asia and others. More than half of revenue is from outside France. |
| Sectors | Automotive, aerospace, defence, rail, energy (including nuclear), life sciences, telecoms, finance and IT. |
| Ways of working | (1) Technical assistance: consultants placed at the client. (2) Work packages: ALTEN delivers a defined scope. (3) Outsourced projects from their own delivery centres. |
| UK | ALTEN Ltd. Acquired **Quick Release** (automotive PLM / BOM consultancy, Midlands) in 2019. Big UK clients are in automotive, aerospace and defence, and energy. |
| Other group companies | MI-GSO / PCUBED (programme management), Atexis (technical documentation and support), Calsoft and Volansys (software / IoT). |

**Check before the interview:** look at ALTEN UK's LinkedIn and website for current UK news, office locations (Midlands, Bristol, etc.) and automotive clients. Mention one specific thing you found.

**Why ALTEN (have this ready):**
"I've already worked in this model at AVL and enjoyed it: being on-site, part of the client's team, but bringing an outside view. ALTEN's size means work across many OEMs and sectors, so I can keep learning. ADAS and autonomy are growing fast, and clients need people who've done both real-vehicle testing and simulation. I've done both."

---

## 3. In-depth questions: answers from your real experience

Use the STAR format, but keep each answer to about 1 to 1.5 minutes: **Situation, Task, Action, Result**.

**"Tell me about a difficult technical problem you solved."**
At JLR, an alert was triggering late at boundary conditions. I re-ran the tests and checked the logs in CANoe/CANape, and found the cause was the radar's field of view. Radar detections are less reliable at the edges of range and FOV. I agreed a change with the supplier that fixed the timing without adding false alerts.

**"How did you work with customers / stakeholders?"**
At JLR I was the main contact between AVL, JLR and the radar supplier. At FiveAI, on the ADA project with Volkswagen Group, I trained partner engineers on our toolchain with demos and Q&A, and helped them get their own tests running. That became the solutions team: we found problems across the partners' toolchains and got the right team to fix them.

**"Walk me through how you wrote requirements."**
I started from use cases and broke them down into system-level and then low-level requirements in DOORS and MKS Integrity, following ASPICE. I drew state diagrams for each feature, defined the signal list for each module (every input and output) and traced it against the state machine. I wrote test cases per state and traced them back to requirements. Defects went into RTC/RQM.

**"Tell me about leading a team."**
For a year I led five engineers on L4 scenario development. I taught them the tools and our evaluation logic, and split the work so scenario creation and evaluation ran in parallel. *It wasn't formal line management. Say "technical lead" if asked.*

**"What's the difference between functional, logical and concrete scenarios?"**
Functional: a scenario described in words ("ego car turns left at a junction, an oncoming car approaches"). Logical: the same scenario with parameter ranges (speed 30–50 km/h, gap 2–5 s). Concrete: one exact set of values you can run. I built 120+ parameterised scenarios that generate thousands of concrete tests.

**"ISO 26262 vs SOTIF?"**
ISO 26262 covers failures, when something breaks. SOTIF (ISO 21448) covers hazards when nothing is broken but the system's performance isn't good enough, for example a sensor limitation like a radar's FOV edge. I wrote ISO 26262 requirements for a lane change feature and I'm trained in both.

**"How do you use AI in your work?"**
I built a helper with GitHub Copilot that creates OpenSCENARIO scenarios from modular blocks, using regulation and NCAP rules as context. It increased our scenario output a lot. I also taught colleagues to check its output rather than trust it.

**"HiL vs ViL vs SIL?"**
SIL: software only, in simulation. HiL: real ECU with a simulated environment. ViL: real vehicle with simulated targets or a simulated environment. I've done all three, plus proving ground testing.

**"Simulation vs real-world testing?"**
In the CarMaker/Simulink project we compared a real vehicle, a dyno with sensor emulation, and pure simulation. I calibrated the vehicle model to real recordings and ran parameter sweeps on the steering PID. Simulation gives you coverage and repeatability; real testing proves it.

**"Why are you leaving Bosch?"**
"I'd like to get closer to vehicles and customers again. I've built strong simulation skills and now want to combine them with hands-on OEM work." *Stay positive. Never criticise Bosch.*

**"Are you OK with client sites, travel and relocation?"**
Yes. Full UK licence, British passport, willing to relocate within the UK.

**"Salary?"**
Let them give a range first. If pushed: "I'm currently at £70k. I'm flexible for the right role and would look at the full package." Your floor is £55–60k; don't say it first.

**Gaps, answered honestly if asked:**
- No ROS, no formal line management, and no deep FlexRay or Ethernet spec work.
- Python: I write tools with AI help. C++: I can read it.
- "I haven't done X yet, but I've picked up Y quickly, for example OpenSCENARIO 2."

---

## 4. Questions to ask them (pick 2–3)

1. Which client and project is this role for, and is it on-site, hybrid or at an ALTEN centre?
2. Is it technical assistance or a work package that ALTEN owns?
3. What does a successful first 6 months look like?
4. How does ALTEN support training and moving between projects or sectors?
5. What happens between client projects?

---

## 5. On the day

- Speak at a calm pace. Give a short answer first, then detail if they want it.
- Have numbers ready: nearly 8 years, 3 features, 120+ scenarios, 1,000+ hours of data, team of 5.
- Have your CV open, but don't read from it.
- Correct the AVL date early.
