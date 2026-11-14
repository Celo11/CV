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
body = S("b", fontSize=8.0, leading=10.2, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.6)
line = S("line", parent=body, spaceAfter=0.9)
sec = S("sec", f="Helvetica-Bold", fontSize=9.8, leading=11.3, textColor=NAVY, spaceBefore=2.6)
role = S("r", f="Helvetica-Bold", fontSize=9.2, leading=10.8, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.5, leading=10.3, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=8.0, leading=10.3, textColor=GREY, alignment=2)
loc = S("l", fontSize=8.0, leading=10.3, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 9.8); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Vehicle Test, Durability & Robustness Engineer  |  Proving Ground, ViL Rigs & Data-Driven Sign-Off")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.0)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Immediately available (no notice period)")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_DR.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - CV", author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.7, spaceAfter=1.6)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0.4)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,0.8), items[0]]), *items[1:], Spacer(1,1.6)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),1.2),("BOTTOMPADDING",(0,0),(-1,-1),1.2),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Mechanical and automotive engineer (BSc Mechanical; MSc Sustainable Automotive Engineering, WMG Warwick) with 8 years in vehicle engineering, validation and sign-off: 3 years at AVL Powertrain UK (2 years on-site at Jaguar Land Rover, HORIBA MIRA / airstrip testing and LEVC factory inspections), followed by 5 years on the VW Group ADA L4 programme at FiveAI / Bosch. Strengths in data-driven attribute targets and KPIs, proving-ground and ViL rig testing, real-world vehicle data capture for model correlation, structured multi-factor test matrices and parameter sweeps, FMEA / ISO 26262 requirements, and mechanical/electrical fault-finding. Honestly noting gaps: my vehicle and rig work focused on functional robustness, ViL dyno correlation and e-machine returns rather than structural four-post shaker rigs or strain-gauge / wheel-force Road Load Data (RLD) acquisition (and the dSPACE HiL rig was operated by the HiL team). Based in Coventry, full UK driving licence, immediately available.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Data-driven attribute targets &amp; KPI sign-off:</b> Turned UN R79, Euro NCAP and customer specs into quantitative attribute targets and pass/fail KPIs (comfort accel/decel limits, lateral acceleration, lane-change success vs. curvature) across 1,000+ hours of test data; surfaced a curvature performance drop within spec that led to a steering controller fix.",
 "<b>Structured parameter sweeps (DoE at scale) &amp; regression troubleshooting:</b> Built 120+ parameterised OpenSCENARIO 2 scenarios sweeping multi-factor parameter spaces across thousands of edge-case runs; compared runs across stack releases and diagnosed API, map and simulation logs to isolate regressions.",
 "<b>Project management &amp; reporting:</b> Led a 5-person engineering team for 1 year (scoped work packages, assigned tasks, ran weekly progress reviews, verified deliveries), co-founded the Simulation EcoSystem solutions team supporting VW Group engineers, and built Python data pipelines alongside Excel and PowerPoint reporting."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Vehicle testing, proving-ground sign-off &amp; OEM/supplier management (JLR):</b> Embedded at Jaguar Land Rover for 2 years as Feature Owner for RCTA (with braking request), BSM and Rear Pre-Crash. Planned, implemented and conducted vehicle and proving-ground verification/sign-off across whole-vehicle mechanical, electrical and software interfaces as technical link between JLR, AVL and the Tier 1 supplier.",
 "<b>Structured test matrices (DoE) &amp; analytical troubleshooting:</b> When RCTA passed in HiL testing (run by the HiL team; simulated objects bypassed the radar antenna) but fired late on track at 45°, designed a coarse-to-fine multi-factor test matrix (approach angles 30/45/60°, targets 10–40 mph, near/far side, ego reverse speeds). Synchronised camera, CAN and radar logs in Vector CANoe / CANape, traced the delay to the FOV edge, and tested 3 calibration candidates (incl. false-positive checks) on site to sign off the fix.",
 "<b>ViL rig testing &amp; real-world track data application (AVL DrivingCube &amp; HORIBA MIRA):</b> On AVL's Vehicle-in-the-Loop chassis dyno test bed, fitted an external GNSS ground-truth system to the test vehicle, drove airstrip steering-torque injection tests and a HORIBA MIRA circuit to capture real-world response data, applied recordings to calibrate a MATLAB / Simulink and IPG CarMaker model via steering PID gain sweeps, and monitored logging health during runs.",
 "<b>FMEA, requirements &amp; field hardware robustness (LEVC &amp; JLR):</b> Authored state diagrams, module signal lists and requirements in DOORS and MKS Integrity (ASPICE V-model), tracked defects in RTC / RQM, wrote ISO 26262 safety requirements for Lane Change Assist and took part in its FMEA (trained in ISO 26262 and SOTIF). At LEVC, inspected ~20 returned range-extender generators (multimeter resistance/continuity, bench-powered log downloads), checked test-vehicle control-arm fasteners with a torque wrench, and traced non-activating modules via DTCs, fuses and a 12 V bench supply."])

s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (2014): electric bus powertrain power/torque sizing in MATLAB / Simulink and production quality.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Coursework: hybrid/EV systems, Ansys Mechanical, C++, Simulink. Dissertation: designed an experimental test setup and method for electric motor stator thermal variables (type-K thermocouples, enclosure, MotorCAD, Portunus, Simulink; test design only, bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Dissertation: team project on a 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space, Arduino); wired 6 servo actuators, commanded set angles, and plotted encoder signals.", line))

s += section("Skills &amp; Hands-on Experience")
s.append(KeepTogether([grid([
 ("Vehicle &amp; rig testing", "Proving ground &amp; vehicle sign-off (JLR, HORIBA MIRA, airstrip – 3 yrs at AVL), AVL DrivingCube ViL chassis dyno, track data capture &amp; model correlation, GNSS ground truth, Vector CANoe / CANape (CAN)"),
 ("FMEA, DoE &amp; analysis", "FMEA participant &amp; ISO 26262 requirements (AVL), SOTIF (trained), structured multi-factor test matrices &amp; coarse-to-fine boundary testing, parameter sweeps (Simulink PID &amp; 120+ OSC2 scenarios), stator test design (MSc), log root-cause analysis"),
 ("Whole-vehicle &amp; hardware", "BSc Mechanical &amp; MSc Automotive (hybrid/EV powertrains, MotorCAD, Ansys), ADAS braking/steering integration, LEVC generator checks, multimeter, 12 V bench supply, torque wrench (control-arm checks &amp; car repairs), calipers &amp; micrometers"),
 ("Project &amp; office tools", "DOORS, MKS Integrity, RTC / RQM, ASPICE V-model, Microsoft Excel &amp; PowerPoint (data analysis, test matrices &amp; reporting), Word, Jira, Confluence, Miro, Python (data pipelines), MATLAB / Simulink, IPG CarMaker, SolidWorks, Git, Linux"),
 ("Gaps &amp; availability", "Not yet used: four-post structural shaker rigs, strain-gauge / wheel-force Road Load Data (RLD) sensors, or Minitab statistical DoE (dSPACE HiL run by HiL team). British citizen, full UK driving licence, Coventry, immediately available")], 0.22)]))

doc.build(s)
