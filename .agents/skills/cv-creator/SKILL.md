---
name: cv-creator
description: >-
  Create tailored, honest, ATS-ready A4 PDF CVs and cover letters for Muhammet Celal Gokalp
  using his confirmed work history, stories, ReportLab house templates, visual PDF verification,
  and CANDIDATE_PROFILE_NOTES.md updates.
---

# CV & Cover Letter Creator (Celal Gokalp)

Use this skill whenever asked to draft, tailor, or update a CV or cover letter for Muhammet Celal Gokalp.

## 1. Mandatory Source-of-Truth Reading (Always Read First)
Before writing a single line of copy or code, read:
1. `/home/muhammet-celal-gokalp/CV-1/cv/CANDIDATE_PROFILE_NOTES.md`
2. `/home/muhammet-celal-gokalp/CV-1/cv/MY_STORY_AND_CHEATSHEET.md`

Also inspect a relevant existing house script in `/home/muhammet-celal-gokalp/CV-1/cv/`:
- **1-page CV templates:** `make_cv_neworbit.py`, `make_cv_f1.py`, `make_cv_tiktok.py`
- **2-page CV template (only when requested or long format fits better):** `make_cv_alexander_dennis.py`
- **1-page Cover Letter templates:** `make_cover_tiktok.py`, `make_cover_ricardo.py`

---

## 2. Hard Truth & Honesty Rules (Never Violate)
1. **Never fabricate or overstate any skill, tool, qualification, or date.** Every factual claim must trace to `CANDIDATE_PROFILE_NOTES.md` or `MY_STORY_AND_CHEATSHEET.md`.
2. **Confirmed employment & education timeline:**
   - **FiveAI / Bosch**, Cambridge — *Lead Application Engineer (Solutions & Integration)*: `10/2021 – 11/2026` (redundancy ended **6 November 2026** due to VW Group withdrawal; **immediately available, no notice period**).
   - **AVL Powertrain UK**, Coventry — *ADAS Systems Engineer (Feature Owner)*: **`11/2018 – 10/2021`** (including **2 years** embedded on-site at Jaguar Land Rover; ~20 returned range-extender generators inspected at LEVC factory; DrivingCube ViL chassis dyno & HORIBA MIRA / airstrip testing). Total experience: **8 years**.
   - **TEMSA Global**, Adana — *Mechanical Engineering Intern*: `05/2014 – 08/2014` (`2014`).
   - **Space Camp Turkey**, Izmir — *Part-Time Teacher & Programme Planner*: `12/2013 – 01/2017`.
   - **MSc Sustainable Automotive Engineering**, WMG, University of Warwick: `10/2017 – 09/2018` (`2:1 Merit`).
   - **BSc Mechanical Engineering**, Ege University, Izmir: `08/2011 – 02/2017`.
3. **Mandatory accuracy guardrails:**
   - **dSPACE HiL:** Celal did **NOT** operate the dSPACE HiL rig himself (it was run by the HiL team). He wrote per-state test cases, tested in vehicles / proving grounds, worked on AVL's DrivingCube ViL test bed, and debugged why RCTA passed on HiL (simulated objects bypassed the radar antenna) vs. failed late on track at 45°.
   - **MSc dissertation:** Designed the stator thermal-network experimental test setup (`MotorCAD`, `Portunus`, `Simulink`, type-K thermocouple placement, enclosure, method); **test design only—the physical bench was NOT built and no tests were run**.
   - **BSc dissertation:** Team 6-DOF Stewart motion platform (`SolidWorks`, `MATLAB` state-space, `Arduino`); wired 6 servo actuators, wrote Arduino angle commands, plotted encoder signals; project unfinished before full pose control.
   - **Team lead (FiveAI):** Led **5 engineers for 1 year** as **technical lead, not formal HR line management**.
   - **Software & AI honesty:** Not a classically trained software engineer; builds Python tools/GUIs/uploaders/pipelines with AI-assisted coding and checks AI outputs carefully; `C++` reading & MSc coursework only; `ROS 1 Noetic` and `Docker` at user level only; Linux workstation user (5 years, not sysadmin).
   - **Vehicle networks:** Worked with `CAN` in `Vector CANoe / CANape`; vehicles also used FlexRay & Automotive Ethernet, but he did **no deep spec/design work** on FlexRay or Ethernet.
   - **Never claim (unless explicitly confirmed later):** ROS 2, DDS, RTOS, SQL, Go, Java, TypeScript, React, PySpark, Palantir (Foundry/Gotham/AIP), MBSE/SysML (Cameo/Capella), Jama, Polarion, NI VeriStand/TestStand, CAPL, CATIA, GD&T specifying, LabVIEW, VectorCAST, TeamCity, SQL, TCP/IP network administration, oscilloscope use, four-post shaker rigs / strain-gauge RLD, RF link design, UAV flight testing, hydrogen/cryogenic systems, FHA/FTA, or Excel/PowerPoint without flagging them for user confirmation.
4. **Proactive gap & clearance disclosures:**
   - Put missing "essential" or "preferred" requirements transparently in **three places** when applying to stretch roles: (a) brief honest sentence in the **Professional Summary**, (b) explicit row in the **Skills table** (pairing ATS keywords truthfully with "Not yet used: ..."), and (c) dedicated paragraph in the **Cover Letter**, bridged immediately by adjacent proven strengths and fast learning examples (`OSC2`, `Python`, `GitHub Copilot` workflow).
   - **Nationality & Clearance:** British citizen (**British and Turkish dual national**), continuous UK resident since **2017 (8+ years)**, full UK driving licence, no current security clearance. On **any** role mentioning `SC`, `DV`, `UK Eyes Only`, `BPSS`, or `no dual nationality`, flag his dual nationality explicitly upfront on the application/notes AND warn Celal in the final response.

---

## 3. Core Stories to Pull From (Match to Role)
Pick and frame the strongest 2–4 confirmed stories for each job advert:
- **S1 – RCTA Proving Ground vs. HiL Root Cause (JLR / AVL):** Passed HiL (objects bypassed radar antenna), failed/late (`0.5s` vs `2s` req) at `45°` on proving ground → coarse-to-fine multi-factor matrix (`30/45/60°`, `10–40 mph`, ego reverse up to `10 mph`) → synchronised camera, CAN and radar logs in `Vector CANoe` → isolated edge-of-FOV latency → tested 3 calibration candidates (incl. false positives) on site with supplier to sign off fix.
- **S2 – Volkswagen Group Solutions & SimEco (FiveAI / Bosch):** Showed and taught VW Group partner engineers across the cluster → co-founded Simulation EcoSystem (`SimEco`) solutions team → resolved customer problems and handled customer feature requests (authoring one-pagers to scope requests and implementing requests directly via project tooling where appropriate) → diagnosed cross-system errors across APIs, maps (`SDB/XODR`), and backend simulation logs → compared stack versions on regressions.
- **S3 – AI Agent Workflow (~10x Speedup) & Reliable Verification (FiveAI / Bosch):** Intensive daily use of GitHub Copilot & AI agent workflows → built Copilot / Copilot CLI agent skill ingesting `UN R79`, `Euro NCAP`, `OpenSCENARIO 2` DSL docs, and golden modular blocks → cut scenario authoring from ~1 day to ~1 hour (`~10x`), added post-run automated checks, ran teachbacks on verifying AI output.
- **S4 – Python Tooling, Traceability, KPIs & Roadmap Influence (FiveAI / Bosch):** Worked in a monorepository-type workspace using `Jira`, Git PRs, dev containers, and `dt_flow` CI → authored technical documentation and performed requirements traceability analysis → built internal Python JSON parameter GUI, local STAX uploader, and data pipelines feeding front-end dashboards → analysed **1,000+ hrs** across **120+ parameterised scenarios** → surfaced a road-curvature drop inside spec that led to a steering controller fix → led 5 engineers for 1 year.
- **S5 – DrivingCube ViL & HORIBA MIRA Correlation (AVL):** Fitted external GNSS ground truth → drove airstrip steering-torque injection & HORIBA MIRA circuit → calibrated `MATLAB / Simulink` + `IPG CarMaker` model via steering PID gain sweeps → monitored test-bed logging health.
- **S6 – Hands-On Hardware & Field Diagnostics (LEVC / JLR / University / Personal):** Inspected ~20 returned range-extender generators at LEVC (`multimeter` phase resistance & continuity + low-voltage bench supply fault-log download); isolated non-activating JLR modules via DTCs, fuse checks, and 12 V bench supply; torque wrench control-arm checks; MSc stator thermal network test design (`MotorCAD`/`Portunus`); BSc 6-DOF Stewart platform servo wiring; Space Camp Turkey (3 yrs teaching science/space ages 9–16).

---

## 4. House Design & Formatting Standards
1. **Visual design:** Navy (`#14213D`) + Teal (`#1F7A8C`) header banner on A4 (`595.276 x 841.89 pts`), `LIGHT = #E8F1F4` zebra Skills table, Helvetica / Helvetica-Bold fonts via `reportlab`.
2. **Strict section order (1-page default):**
   - Header banner (name, role-aligned subtitle, contact/location/citizenship/travel/availability)
   - `PROFESSIONAL SUMMARY`
   - `WORK EXPERIENCE` (strictly reverse chronological order: FiveAI / Bosch → AVL Powertrain UK → Space Camp Turkey & TEMSA Global 1-liners; NEVER insert a Skills section between employers)
   - `EDUCATION` (MSc WMG Warwick → BSc Ege University)
   - `TECHNICAL SKILLS` (2-column zebra table after Education)
3. **ReportLab safety & typography:**
   - Escape `&` as `&amp;` inside every `Paragraph(...)` string (`drawString(...)` in canvas header uses literal `&`). Never leave raw Markdown backticks in ReportLab strings.
   - Tune `fontSize` (`7.9–8.3`), `leading` (`10.0–11.0`), and wording so the CV fits cleanly on **1 A4 page** with zero orphan single-word wrapped lines and ~10–25 mm comfortable bottom whitespace. Keep Cover Letters to **1 A4 page** as well.
   - Place scripts in `/home/muhammet-celal-gokalp/CV-1/cv/make_cv_<target>.py` and `make_cover_<target>.py`, writing PDFs next to the script via `Path(__file__).resolve().parent`.

---

## 5. Mandatory Build, Visual QA & Logging Workflow
After writing the Python generator script(s):
1. Build with the project virtualenv:
   `/home/muhammet-celal-gokalp/CV-1/cv/.venv/bin/python /home/muhammet-celal-gokalp/CV-1/cv/<script>.py`
2. Verify exact page count (`Pages: 1`) using `pdfinfo`.
3. Render to PNG at 150 DPI via `pdftoppm -png -r 150 <pdf> /tmp/<name>` and **inspect every rendered page visually using `read_file`**. Fix any overflow, clipping, or single-word orphan wraps and re-verify.
4. Append a concise summary entry under `### Confirmed update - <date>` in `/home/muhammet-celal-gokalp/CV-1/cv/CANDIDATE_PROFILE_NOTES.md`.
5. In the final reply to Celal, provide clickable `file://` links, summarise the requirement-to-evidence mapping, list all honest gap disclosures, and flag any eligibility/clearance/unconfirmed items for review before applying.
