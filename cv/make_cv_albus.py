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
body = S("b", fontSize=7.65, leading=9.55, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.45)
line = S("line", parent=body, spaceAfter=0.6)
sec = S("sec", f="Helvetica-Bold", fontSize=9.4, leading=10.7, textColor=NAVY, spaceBefore=1.9)
role = S("r", f="Helvetica-Bold", fontSize=8.85, leading=10.3, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.15, leading=9.8, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=7.65, leading=9.8, textColor=GREY, alignment=2)
loc = S("l", fontSize=7.65, leading=9.8, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 9.35); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Principal Systems Test & Automation Engineer  |  Multi-Stage Data Pipelines, Radar/Sensor Systems & AI Testing")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.8)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Oxford hybrid / commute)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   8 yrs Systems V&V, Radar & Test Automation   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_Albus.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Albus Health Principal Systems Test & Automation CV",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.45, spaceAfter=1.15)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0.35)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,0.45), items[0]]), *items[1:], Spacer(1,0.95)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),0.9),("BOTTOMPADDING",(0,0),(-1,-1),0.9),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Hands-on Principal / Lead Systems Test &amp; Automation Engineer with 8 years testing complex, multi-component sensor, algorithm, and data-processing systems across FiveAI / Bosch (autonomous driving scale-up / VW Group ADA programme) and AVL Powertrain UK (2 yrs embedded at Jaguar Land Rover). Specialises in tracing raw sensor and simulation data (radar, camera, CAN, map/model pipelines) through multi-stage processing to isolate subtle data corruption, latency, and algorithm regressions; designing parameterised automated test suites (120+ suites, 1,000+ hrs quantitative KPI evaluation); building practical Python test/data tools and CI/CD workflows (dt_flow, Git PRs); and pioneering AI-assisted test engineering (~10x speedup) backed by strict independent verification. Honest on gaps: regulated V-model background comes from automotive/autonomy (ASPICE V-model, ISO 26262, SOTIF) rather than medical devices (IEC 62304, ISO 13485); not yet administered AWS cloud infrastructure; builds Python tools and pipelines with AI-assisted coding rather than coming from a traditional CS background.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Testing multi-stage data &amp; ML/simulation pipelines (fault isolation):</b> Co-founded the Simulation EcoSystem (SimEco) solutions team on the VW Group ADA programme and tested a local containerised Vision-Language-Action (VLA) ML setup (Docker, ROS 1 Noetic, simulator orchestrator). Traced unexpected outputs across interconnected APIs, OSM-to-OpenDRIVE map converters, simulation stages, and evaluation validators—proving false downstream 'stay in lane' failures stemmed from upstream curve discretisation and adding numeric edge-case checks.",
 "<b>Quantitative acceptance criteria &amp; subtle regression detection:</b> Designed and maintained 120+ parameterised OpenSCENARIO 2 automated test suites integrated into dt_flow CI/CD release workflows in a Linux dev-container monorepo (Git PRs, Jira). Defined quantitative pass/fail KPIs across 1,000+ hours of pipeline data—exposing a subtle road-curvature tracking degradation inside nominal bounds that led to a steering-controller fix.",
 "<b>AI-assisted test automation (~10x speedup) with independent judgement:</b> Built a project-wide GitHub Copilot &amp; Copilot CLI agent skill ingesting UN R79 / Euro NCAP rules, DSL docs, and modular blocks to author and parameterise tests (~1 day to ~1 hr). Enforced a 3-step verification check—manual baseline, automated post-run assertions, and random pass spot-checks to catch silent false passes from missing assertions—and trained peers to verify AI outputs.",
 "<b>Python test tooling, documentation &amp; technical leadership:</b> Built practical Python applications with AI help (JSON parameter configuration GUI, local STAX artefact uploader, and pipelines feeding analysis dashboards). Authored technical documentation, traceability analysis, and feature-request one-pagers (and implemented features in tooling), and led a 5-person team for 1 year (hands-on technical lead)."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Radar data-flow investigation &amp; multi-stage root-cause analysis (Jaguar Land Rover):</b> Embedded 2 years as Feature Owner for 3 radar features (Rear Cross Traffic Alert, Blind Spot Monitor, Rear Pre-Crash). When RCTA passed on the dSPACE HiL rig (run by the HiL team, where synthetic targets bypassed the radar antenna and target-processing stage) yet fired late (0.5 s vs 2 s) at 45° on track, challenged assumptions, designed a coarse-to-fine test matrix, time-synchronised camera, CAN bus and internal radar detection/object logs in Vector CANoe / CANape, isolated FOV-edge latency, and verified 3 supplier calibrations (including false-positive/negative checks).",
 "<b>Systems V-Model, requirements traceability &amp; multi-level verification:</b> Translated use cases into state architectures, module input/output signal lists, low-level requirements, and component/subsystem/system verification plans in IBM DOORS and MKS Integrity (ASPICE V-model), closing defects in RTC / RQM; authored ISO 26262 safety requirements and joined a feature FMEA (SOTIF trained).",
 "<b>Multi-component hardware/software integration (DrivingCube ViL &amp; LEVC):</b> Supported AVL's DrivingCube ViL rig (comparing real vehicle, dyno with sensor emulation, and Simulink + IPG CarMaker pipelines)—commissioning GNSS ground-truth logging, checking logging health, and running PID sweeps. At LEVC, checked ~20 returned generators via multimeter and bench fault-log downloads."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): taught space science (ages 9–16); simplified technical concepts and planned schedules.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): electric bus powertrain sizing in MATLAB / Simulink; production quality control.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). System modelling (MATLAB / Simulink), C++, hybrid/EV systems, Ansys. Dissertation: stator thermal-network test design (MotorCAD, Portunus, Simulink; test design only—bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space modelling, Arduino servo wiring and encoder signal plotting).", line))

s += section("Technical &amp; Test Automation Skills")
s.append(KeepTogether([grid([
 ("Test automation &amp; CI/CD", "Parameterised automated test design (120+ OpenSCENARIO 2 suites), dt_flow CI/CD pipeline execution &amp; failure triage, Python (JSON parameter GUI, STAX uploader, dashboard data pipelines built with AI help), Git PRs, Linux dev-container monorepo (5 yrs)"),
 ("AI-assisted testing", "Intensive GitHub Copilot &amp; Copilot CLI agent workflows (~10x test speedup), 3-stage verification (manual baseline, post-run assertions, silent-pass spot-checks), VLA ML container testing (user-level Docker / ROS 1)"),
 ("Multi-stage data &amp; radar", "End-to-end sensor &amp; data debugging (radar detection/object streams, camera, CAN bus in Vector CANoe / CANape, OSM-to-XODR conversion maths, API &amp; backend logs), 1,000+ hrs KPIs, GNSS correlation"),
 ("V-Model &amp; traceability", "ASPICE V-model, component/subsystem/system test planning, IBM DOORS, MKS Integrity, RTC / RQM, Jira, Confluence, signal lists, traceability analysis, ISO 26262, SOTIF, FMEA participation &amp; technical documentation"),
 ("Honest technical gaps", "Regulated automotive/autonomy background (ISO 26262 / ASPICE) rather than medical devices (IEC 62304 / ISO 13485); not yet administered AWS cloud infrastructure; learned Python via AI-assisted coding rather than pure CS training; did not run dSPACE HiL directly")], 0.23)]))

doc.build(s)
