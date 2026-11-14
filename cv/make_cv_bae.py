from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable)

NAVY = colors.HexColor("#14213D"); ACC = colors.HexColor("#1F7A8C")
GREY = colors.HexColor("#555555"); LIGHT = colors.HexColor("#E8F1F4")
W, H = A4; M = 14*mm; HB = 34*mm

def S(n, **k): return ParagraphStyle(n, fontName=k.pop("f", "Helvetica"), **k)
body = S("b", fontSize=7.75, leading=9.7, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.48)
line = S("line", parent=body, spaceAfter=0.65)
sec = S("sec", f="Helvetica-Bold", fontSize=9.5, leading=10.8, textColor=NAVY, spaceBefore=2.0)
role = S("r", f="Helvetica-Bold", fontSize=8.9, leading=10.4, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.2, leading=9.9, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=7.75, leading=9.9, textColor=GREY, alignment=2)
loc = S("l", fontSize=7.75, leading=9.9, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 9.6); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Principal / Lead IV&V & Systems Integration Engineer  |  V-Model, Control Systems & Sim/Stim Environments")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.8)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Barrow hybrid / relocation)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   8+ yrs continuous UK residence (since 2017)   |   Full UK driving licence   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_BAE.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - BAE Systems Principal C&I IV&V CV",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.5, spaceAfter=1.2)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0.4)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,0.5), items[0]]), *items[1:], Spacer(1,1.0)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),0.95),("BOTTOMPADDING",(0,0),(-1,-1),0.95),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Lead IV&amp;V and Systems Integration Engineer with 8 years delivering complex control and sensing systems across the full Systems Engineering V-Model—from requirements and interface definition through off-platform Sim/Stim and Vehicle-in-the-Loop (ViL) test environments to final acceptance (2 yrs at Jaguar Land Rover via AVL; 5 yrs supporting Volkswagen Group on ADA at FiveAI / Bosch). Experienced in control system modelling and PID calibration (MATLAB / Simulink, IPG CarMaker, state-space), data interface analysis (module signal lists, CAN bus in Vector CANoe / CANape), third-party interface testing, requirements traceability (IBM DOORS, MKS Integrity, RTC / RQM, Jira), and technical documentation. Honest on gaps &amp; vetting: background is automotive/autonomous systems (CAN fieldbus, Simulink, ViL rigs, simulation toolchains) rather than naval/submarine C&amp;I or industrial PLC fieldbuses (Profibus / Modbus / EtherCAT), and facility work covers ViL instrumentation commissioning and university rig design/wiring rather than civil facility construction. British citizen (British &amp; Turkish dual national) with 8+ years continuous UK residence since 2017—flagged upfront for BPSS / National Security Vetting and AUKUS export-control checks.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Off-platform Sim/Stim environment &amp; third-party interface testing:</b> Primary integration engineer supporting Volkswagen Group partner teams on ADA, and Simulation EcoSystem (SimEco) co-founder. Supported closed-loop Sim/Stim toolchains (dt_flow, dt_launcher, Linux dev containers) in a monorepo (Git PRs, Jira) and diagnosed third-party API, map (SDB/XODR) and backend log faults.",
 "<b>V-Model verification, acceptance evidence &amp; control analysis:</b> Defined quantitative KPIs and acceptance criteria across 1,000+ hours of closed-loop test data (120+ parameterised OpenSCENARIO 2 scenarios). Performed requirements traceability analysis and control-behaviour evaluation—identifying a road-curvature drop inside spec that drove a steering-controller fix.",
 "<b>Technical documentation, engineering assurance &amp; Python tools:</b> Authored technical documentation, scoped customer feature requests via one-pagers (and implemented features directly in project tooling), and built internal Python utilities with AI assistance—a JSON parameter GUI, local STAX uploader, and pipelines feeding front-end evaluation dashboards.",
 "<b>Team leadership &amp; automated verification workflows:</b> Led a 5-person engineering team for 1 year (technical lead), driving IV&amp;V deliverables and weekly reviews; built a project-wide GitHub Copilot / Copilot CLI agent workflow (~10x faster scenario authoring with post-run verification checks)."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Full V-Model lifecycle, data interface analysis &amp; acceptance (Jaguar Land Rover):</b> Embedded on-site at JLR for 2 years as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash (plus ACC, LKA, Highway Assist and Lane Change Assist requirements). Decomposed use cases into state architectures, low-level requirements and per-state test cases in IBM DOORS and MKS Integrity (ASPICE V-model), defined every module input/output in signal lists, and managed defect closure in RTC / RQM.",
 "<b>Sim/Stim Plant environment calibration &amp; ViL test-bed runs (AVL DrivingCube):</b> Supported Sim/Stim correlation on AVL's DrivingCube Vehicle-in-the-Loop (ViL) test bed comparing physical vehicle, chassis dyno with sensor emulation, and MATLAB / Simulink + IPG CarMaker simulation. Fitted external GNSS ground-truth logging, captured airstrip and HORIBA MIRA reference data, calibrated the plant steering model via PID parameter sweeps, and monitored ViL logging health and simulation readiness.",
 "<b>Interface testing, Sim/Stim vs. hardware root-cause &amp; electrical checks:</b> When RCTA passed on dSPACE HiL (run by the HiL team, where injected targets bypassed the radar antenna) but fired late (0.5 s vs 2 s) at 45° on track, ran a boundary test matrix, time-synchronised camera, CAN bus and radar streams in Vector CANoe / CANape, isolated edge-of-FOV radar latency, and verified 3 third-party supplier calibrations. Authored ISO 26262 requirements, joined a feature FMEA, checked JLR modules via DTCs/fuses/12 V bench supply, and inspected ~20 returned generators at LEVC (multimeter pin checks and bench fault-log downloads)."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): taught space technology (ages 9–16); simplified technical concepts and planned schedules.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): electric bus powertrain sizing in MATLAB / Simulink; production quality.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). System modelling (MATLAB / Simulink), C++, hybrid/EV systems, Ansys. Dissertation: designed a stator thermal-network identification test rig (MotorCAD, Portunus, Simulink, type-K thermocouple layout; test design only—bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart motion platform (SolidWorks, state-space control modelling in MATLAB, Arduino servo wiring and encoder signal plotting).", line))

s += section("Technical &amp; IV&amp;V Skills")
s.append(KeepTogether([grid([
 ("V-Model IV&amp;V &amp; assurance", "Full lifecycle requirements-to-acceptance (ASPICE V-model), IBM DOORS, MKS Integrity, RTC / RQM, Jira, Confluence, traceability analysis, technical documentation, feature-request one-pagers, ISO 26262, SOTIF, FMEA participation"),
 ("Control systems &amp; Sim/Stim", "MATLAB / Simulink, IPG CarMaker, plant model calibration &amp; steering PID sweeps, state-space modelling, AVL DrivingCube ViL Sim/Stim runs, OpenSCENARIO 2 (120+ scenarios, 1,000+ hrs KPI checks), dt_flow CI"),
 ("Interfaces &amp; fieldbus", "Module input/output signal lists, CAN bus analysis &amp; time-sync (Vector CANoe / CANape), DTC triage, third-party API / map (SDB/XODR) debugging, multimeter &amp; 12 V bench commissioning, GNSS logging; vehicle-level FlexRay &amp; Ethernet exposure"),
 ("Honest technical gaps", "Automotive/ADAS background rather than submarine/naval C&amp;I or PLC fieldbuses (Profibus, Modbus, EtherCAT); facility work covers ViL instrumentation &amp; academic rig design (MSc bench not built) rather than civil construction; did not run dSPACE HiL directly"),
 ("Vetting, leadership &amp; hybrid", "British &amp; Turkish dual national (British citizen, 8+ yrs continuous UK residence since 2017—flagged upfront for AUKUS export-control / vetting checks), 1-yr technical lead for 5 engineers, full UK licence, immediately available for Barrow hybrid")], 0.23)]))

doc.build(s)
