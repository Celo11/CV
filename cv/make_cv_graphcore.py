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
body = S("b", fontSize=7.6, leading=9.5, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.45)
line = S("line", parent=body, spaceAfter=0.6)
sec = S("sec", f="Helvetica-Bold", fontSize=9.4, leading=10.7, textColor=NAVY, spaceBefore=1.9)
role = S("r", f="Helvetica-Bold", fontSize=8.85, leading=10.3, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.15, leading=9.8, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=7.6, leading=9.8, textColor=GREY, alignment=2)
loc = S("l", fontSize=7.6, leading=9.8, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 9.6); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Staff / Lead Systems & Hardware Test Engineer  |  Diagnostics, Test Automation, Linux & Root-Cause Debug")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.8)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Bristol / UK hybrid or relocation)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   8 yrs Systems Test, Diagnostics & Automation   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_Graphcore.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Graphcore Staff Hardware System Test CV",
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
s.append(Paragraph("Hands-on Lead Systems &amp; Hardware Test Engineer with 8 years driving fault diagnosis, test coverage, and automated test toolchains across complex hardware/software systems at FiveAI / Bosch (VW Group ADA programme) and AVL Powertrain UK (embedded at Jaguar Land Rover and the LEVC factory). Proven individual-contributor technical leader (led 5 engineers for 1 yr without HR line management, co-founded SimEco diagnosis team, owned 3 JLR radar features), combining 5 years on Linux with Python test tooling, CI automation (dt_flow), data-driven false-fail reduction, ~10x test authoring speedup, and lab/factory bench debug (multimeter pin checks, 12 V bench bring-up, proprietary fault-log extraction, custom PC builds). Honest on gaps: hardware test background comes from automotive ECUs, radar sensors, ViL test beds, and factory returned e-machine generators rather than AI accelerator silicon, Host Processor Modules, server blades, multi-node racks, or OpenBMC; builds Python test tools via AI-assisted coding rather than pure CS training.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>IC technical leadership &amp; cross-functional diagnosis (no HR line management):</b> Led a 5-person engineering team for 1 year (technical lead) and co-founded the Simulation EcoSystem (SimEco) diagnosis team supporting VW Group partners. Collaborated across software, platform, and test teams in a Linux (5 yrs), Docker dev-container, Git PR, and Jira monorepo (with basic SSH GPU-cluster use) to isolate cross-system API, map (SDB/XODR) and backend log faults.",
 "<b>Test time optimisation (~10x), false-fail reduction &amp; coverage:</b> Built a project-wide GitHub Copilot &amp; Copilot CLI agent skill ingesting UN R79 / Euro NCAP rules and modular blocks to cut test authoring time from ~1 day to ~1 hour (~10x), enforcing a 3-step verification check (manual baseline, automated post-run assertions, random pass spot-checks). Eliminated false downstream 'stay in lane' test failures by tracing them to upstream OSM-to-OpenDRIVE curve discretisation and adding numeric edge-case validation.",
 "<b>Python test infrastructure, diagnostics &amp; KPI analytics:</b> Built internal Python test tools with AI help—a JSON parameter configuration GUI, local STAX artefact uploader, and pipelines feeding diagnostic dashboards—and integrated 120+ parameterised test suites into dt_flow CI/CD workflows across 1,000+ hours of data (exposing a subtle road-curvature regression inside nominal limits).",
 "<b>Testability requirements, feature requests &amp; documentation:</b> Authored technical documentation, traceability analysis, and feature-request one-pagers (and implemented features directly in project tooling) to improve diagnosability and reporting."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Factory returned-hardware diagnostics &amp; bench fault-log extraction (LEVC):</b> At the LEVC (London Electric Vehicle Company) factory, inspected ~20 returned faulty range-extender generators following manufacturing/quality triage procedures—running multimeter phase-resistance and continuity checks at specified connector pins, powering control units from a bench supply to connect proprietary loggers and extract fault logs, and reporting evidence to engineering and supplier teams.",
 "<b>Lab/vehicle hardware bring-up, root-cause debug &amp; false-positive/negative testing (Jaguar Land Rover):</b> Embedded 2 years as Feature Owner for 3 radar features (RCTA, BSM, Rear Pre-Crash). Isolated non-activating ECUs during bring-up via DTC reads, fuse checks, and 12 V bench supplies. When RCTA passed on dSPACE HiL (run by the HiL team) yet fired late (0.5 s vs 2 s) at 45° on track, ran a boundary matrix, time-synchronised camera, CAN bus and radar logs in Vector CANoe / CANape, isolated FOV-edge latency, and verified 3 supplier calibrations (including false-positive and false-negative checks).",
 "<b>Test-bed commissioning, FMEA &amp; systems test coverage (DrivingCube ViL):</b> Commissioned external GNSS ground-truth logging on AVL's DrivingCube ViL rig, checked real-time logging health, ran Simulink / IPG CarMaker PID sweeps, joined a feature FMEA (ISO 26262 / SOTIF), and defined module signal lists and test cases in IBM DOORS, MKS Integrity and RTC / RQM (ASPICE V-model)."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): taught space tech (ages 9–16); simplified complex topics and planned schedules.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): electric bus powertrain sizing in MATLAB / Simulink; production quality control.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). System modelling (Simulink), C++, hybrid/EV systems, Ansys. Dissertation: stator thermal-network test design (MotorCAD, Portunus, Simulink; test design only—bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space, Arduino servo wiring &amp; encoder plotting); builds own desktop PCs, PCB motor soldering &amp; fuse-level parasitic drain debug.", line))

s += section("Technical &amp; Hardware Test Skills")
s.append(KeepTogether([grid([
 ("Hardware debug &amp; bench", "Factory returned-unit triage (~20 LEVC generators), multimeter pin resistance/continuity checks, 12 V bench bring-up &amp; fault-log downloads, DTC &amp; fuse-level fault isolation, Vector CANoe / CANape time-sync, PCB cable soldering, custom PC builds"),
 ("Linux, Python &amp; CI", "Linux workstation (5 yrs), Python test tooling (JSON config GUI, STAX uploader, dashboard pipelines built with AI help), dt_flow CI/CD pipelines, Git PRs, monorepo, Docker dev containers (user), basic SSH GPU-cluster use, GitHub Copilot / CLI (~10x speedup)"),
 ("Coverage, false fails &amp; KPIs", "False-fail &amp; false-positive/negative reduction (OSM-to-XODR numeric checks, radar sweeps), 120+ OpenSCENARIO 2 suites, 1,000+ hrs KPIs, FMEA, DOORS, MKS Integrity, RTC / RQM, Jira"),
 ("IC technical leadership", "1-yr technical lead for 5 engineers (non-HR), SimEco cross-team diagnosis co-founder, 2-yr OEM Feature Owner (JLR), feature-request one-pagers &amp; tooling implementation, technical documentation &amp; traceability"),
 ("Honest technical gaps", "Hardware test experience is automotive ECUs/radars/e-machines &amp; custom PCs rather than datacentre servers, GPU/AI accelerator silicon, Host Processor Modules, multi-node racks, high-speed interconnects or OpenBMC; Python via AI coding; did not run dSPACE HiL directly")], 0.22)]))

doc.build(s)
