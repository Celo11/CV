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
body = S("b", fontSize=8.2, leading=10.7, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.75)
line = S("line", parent=body, spaceAfter=1.1)
sec = S("sec", f="Helvetica-Bold", fontSize=10.0, leading=11.6, textColor=NAVY, spaceBefore=3.1)
role = S("r", f="Helvetica-Bold", fontSize=9.3, leading=11.0, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.6, leading=10.6, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=8.1, leading=10.6, textColor=GREY, alignment=2)
loc = S("l", fontSize=8.1, leading=10.6, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 10.0); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Test & Verification Engineer  |  Hardware Testing, Data Analysis & System Qualification")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.0)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Happy to relocate & work extended hours on-site   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_NewOrbit.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - CV", author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.8, spaceAfter=2.0)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0.5)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,1), items[0]]), *items[1:], Spacer(1,2.0)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),1.5),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Mechanical engineer (BSc Mechanical; MSc Sustainable Automotive, WMG Warwick) with 8 years in test campaign planning, hardware and vehicle verification, synchronised data logging, root-cause analysis and traceable documentation at AVL Powertrain UK and FiveAI / Bosch. I do not yet have experience with electric propulsion, RF gridded ion thrusters, vacuum systems, RF or high-voltage power supplies, gas feed hardware, thrust balances or plasma diagnostics. What I bring is rigorous test ownership, hands-on electrical and mechanical fault-finding (multimeter, 12 V bench supply, torque tools, SolidWorks, Arduino actuator wiring), fast feedback from test data to design teams, traceable verification records (DOORS, ASPICE V-model, ISO 26262, RTC / RQM), and MATLAB / Simulink and Python tooling. Having taught space technology part-time for 3 years at Space Camp Turkey, I am keen to move into space propulsion, happy to relocate to Reading and work extended hours on-site, and immediately available.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Test campaign planning &amp; KPI analysis:</b> Planned and wrote 120+ parameterised OpenSCENARIO 2 scenarios generating thousands of test cases (UN R79, Euro NCAP), defined quantitative pass/fail and KPI criteria across 1,000+ hours of test data, and compared runs across software versions to isolate regressions and feed findings back to engineering teams.",
 "<b>Cross-discipline integration &amp; log diagnosis:</b> Led a 5-person engineering team for a year (technical lead) and co-founded the Simulation EcoSystem solutions team on the Volkswagen Group ADA project, diagnosing error logs across APIs, maps and simulation tools.",
 "<b>Python test tools &amp; Linux workflow:</b> Built Python tools with AI help (JSON test-parameter GUI, result uploader, data pipelines into dashboards) and worked daily in Linux within the project monorepo using dev containers, Git and CI test pipelines."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Test campaigns, synchronised logging &amp; rapid design feedback (JLR):</b> Based on-site at Jaguar Land Rover for 2 years owning verification for three corner-radar features across mechanical, electrical and software teams. When an alert passed in HiL testing (where simulated objects bypassed the radar antenna) but fired late on the track at 45°, designed a coarse-to-fine test matrix, synchronised camera, CAN and proprietary radar logs on one PC in Vector CANoe / CANape, traced the delay to the field-of-view edge, and verified the supplier's calibration fix on site.",
 "<b>Test-bed instrumentation &amp; MATLAB / Simulink correlation (AVL DrivingCube):</b> On AVL's Vehicle-in-the-Loop dyno test bed, fitted an external GNSS ground-truth system to the vehicle, captured airstrip and HORIBA MIRA test data, monitored logging health and system readiness during test-bed runs, and swept PID gains in MATLAB / Simulink and IPG CarMaker to calibrate the steering controller.",
 "<b>Hardware inspection &amp; bench fault-finding (LEVC &amp; JLR):</b> Inspected ~20 returned faulty range-extender generators at the LEVC factory per test procedure: multimeter checks at connector pins (phase-to-phase resistance, continuity) and powering the control unit from a low-voltage bench supply to download fault logs for supplier analysis. Isolated non-activating vehicle modules via fault codes, fuse checks and a 12 V bench supply, and checked test-vehicle control-arm fasteners with a torque wrench.",
 "<b>Traceable verification &amp; configuration records:</b> Wrote state diagrams, module input/output signal lists, requirements and per-state test cases in DOORS and MKS Integrity (ASPICE V-model), recorded test configurations and defects to closure in RTC / RQM, wrote ISO 26262 safety requirements, and took part in an FMEA."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Program Planner</b>, Space Camp Turkey (12/2013 – 01/2017): taught space technology and flight science (ages 9–16).", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (2014): electric bus powertrain sizing in MATLAB / Simulink and production quality.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Dissertation: designed an experimental test setup to identify thermal-network variables of an electric motor stator (type-K thermocouple placement, enclosure and test method; MotorCAD, Portunus, MATLAB / Simulink; test design only, physical bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Dissertation: team project to design and build a 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space, Arduino); wired 6 servo actuators, commanded set angles, and plotted encoder signals.", line))

s += section("Skills &amp; Hands-on Experience")
s.append(KeepTogether([grid([
 ("Testing &amp; data logging", "Test campaign planning, boundary testing, AVL DrivingCube (ViL dyno test bed), vehicle &amp; track testing, time-synchronised camera / CAN / sensor logging in Vector CANoe &amp; CANape, GNSS ground-truth fitting (all at AVL); KPI &amp; regression analysis on 1,000+ hrs data (FiveAI)"),
 ("Hardware &amp; bench work", "Multimeter diagnostics (resistance, continuity, fuse probing), 12 V / low-voltage bench supply checks, torque wrench, calipers &amp; micrometers, soldering motor cables to a PCB, 6-DOF servo wiring (Arduino), stator thermocouple test design (MSc), PC builds &amp; car repairs"),
 ("Verification &amp; traceability", "Requirements-to-test traceability, configuration &amp; defect records (DOORS, MKS Integrity, RTC / RQM, ASPICE V-model, ISO 26262, FMEA — all at AVL); Jira, Confluence, technical lead for 5 engineers (FiveAI)"),
 ("Scripting &amp; modelling", "MATLAB / Simulink (PID gain sweeps, model calibration, signal plotting), Python (test GUIs, uploaders &amp; dashboard pipelines built with AI help), Linux (daily workstation for 5 years), Git, SolidWorks; C++ (reading)"),
 ("Gaps &amp; availability", "Not yet used: vacuum systems (pumps/gauges/valves), RF generators, high-voltage supplies, mass flow controllers, thrust balances, plasma probes (Langmuir / RPA). British &amp; Turkish citizen, full UK licence, immediately available, happy to relocate &amp; work extended hours on-site")], 0.22)]))

doc.build(s)
