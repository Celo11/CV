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
body = S("b", fontSize=8.3, leading=10.9, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.8)
line = S("line", parent=body, spaceAfter=1.2)
sec = S("sec", f="Helvetica-Bold", fontSize=10.1, leading=11.8, textColor=NAVY, spaceBefore=3.2)
role = S("r", f="Helvetica-Bold", fontSize=9.4, leading=11.2, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.7, leading=10.8, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=8.2, leading=10.8, textColor=GREY, alignment=2)
loc = S("l", fontSize=8.2, leading=10.8, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 10.0); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Systems & Validation Engineer  |  L4 Autonomy, Steering / Braking Features & Vehicle Test")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.0)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence (commutable to Banbury)   |   Immediately available")
    c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Zoox.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - CV", author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.8, spaceAfter=2)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0.5)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,1), items[0]]), *items[1:], Spacer(1,2)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),1.5),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Mechanical and automotive engineer (BSc Mechanical; MSc Sustainable Automotive, WMG Warwick) with 8 years bridging physical vehicle systems and autonomous driving: 2 years on-site at Jaguar Land Rover with AVL managing features, requirements, Tier 1 suppliers and vehicle / proving-ground testing, followed by 5 years on an L4 automated driving stack at FiveAI / Bosch. My strengths are on the systems integration, requirements, supplier coordination, steering/braking feature validation, CAN signal analysis and L4 autonomy side of this role. I have not designed production steer-by-wire or brake-by-wire mechanical hardware in CATIA or released 2D drawings with ASME Y14.5 GD&amp;T (my CAD work is in SolidWorks), and with 8 years of experience I am open to the level Zoox finds appropriate. Based in Coventry (commutable to Banbury) and immediately available.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>L4 steering &amp; braking KPIs:</b> Turned UN R79 (automatic steering / lane change), Euro NCAP and customer requirements into KPIs and pass/fail criteria (lateral acceleration, longitudinal comfort accel/decel limits, road curvature metrics) across 1,000+ hours of test data; identified a drop in lane-change success above a curvature threshold that led to a steering controller fix.",
 "<b>Scenario validation &amp; tooling:</b> Wrote 120+ parameterised OpenSCENARIO 2 scenarios generating thousands of test cases, built a GitHub Copilot helper that cut scenario creation from ~1 day to ~1 hour, and built Python tools and pipelines into dashboards.",
 "<b>Cross-functional &amp; partner leadership:</b> Led 5 engineers for a year on L4 scenario validation; founding member of the Simulation EcoSystem solutions team on the Volkswagen Group ADA project, diagnosing errors across APIs, maps and simulation tools."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>OEM &amp; Tier 1 supplier management:</b> Based on-site at Jaguar Land Rover for 2 years as feature owner for Rear Cross Traffic Alert (with braking request), Blind Spot Monitor and Rear Pre-Crash; main technical link between JLR, AVL and the Tier 1 radar supplier.",
 "<b>Steering torque PID &amp; ViL correlation (AVL DrivingCube):</b> Built Simulink / IPG CarMaker scenarios on circles of parameterised radius to find the steering-wheel torque needed at each radius. Fitted an external GNSS for position ground truth, captured vehicle response during airstrip steering-torque injection tests and HORIBA MIRA circuit runs, and ran parameter sweeps to calibrate the simulation steering torque PID controller.",
 "<b>Requirements &amp; functional safety (steering &amp; longitudinal features):</b> Wrote use cases, state diagrams, module input/output signal lists and high- to low-level requirements in DOORS and MKS Integrity (ASPICE V-model), including requirements for Lane Keep Assist, Lane Change Assist, Highway Assist and ACC. Wrote ISO 26262 safety requirements for a lane change feature and took part in its FMEA.",
 "<b>Vehicle testing &amp; CAN analysis:</b> Wrote test cases per system state and executed validation in vehicles and on the proving ground using Vector CANoe and CANape. When RCTA braking/alerting fired late on the track at a 45° approach, designed a coarse-to-fine test matrix, synchronised camera, CAN and radar logs in CANoe, traced the delay to the edge of the radar's field of view, and verified the supplier's calibration fix on site.",
 "<b>Electromechanical &amp; vehicle fault-finding:</b> Inspected ~20 returned range-extender generators at the LEVC factory (multimeter phase-to-phase resistance and continuity checks, bench-powering the control unit to download supplier logs). Checked test-vehicle control-arm fasteners with a torque wrench, and diagnosed vehicle module faults via DTCs, fuse checks and a 12 V bench supply."])

s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global, 2014: electric bus powertrain power and torque calculations in MATLAB / Simulink.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Dissertation: designed a test to find the thermal model variables of an electric motor stator (type-K thermocouple placement, enclosure, method; MotorCAD thermal network, Portunus, Simulink).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Dissertation: team project to design and build a 6-DOF Stewart motion platform (SolidWorks 3D CAD, MATLAB state-space model, Arduino); wired the 6 servo actuators, wrote Arduino code to command set angles, and plotted encoder signals.", line))

s += section("Skills &amp; Hands-on Experience")
s.append(KeepTogether([grid([
 ("Testing, CAN &amp; rigs", "AVL DrivingCube (ViL dyno test bed), proving ground &amp; vehicle testing, Vector CANoe and CANape, CAN signal analysis, GNSS ground truth, multimeter &amp; 12 V bench supply (all at AVL)"),
 ("Systems &amp; safety", "Technical requirements authoring &amp; decomposition, module signal lists, DOORS, MKS Integrity, RTC / RQM, ASPICE V-model, ISO 26262 &amp; FMEA, SOTIF (trained) (all at AVL); Jira, Confluence, UN R79, Euro NCAP"),
 ("Software &amp; modelling", "MATLAB / Simulink, IPG CarMaker, MotorCAD, SolidWorks (BSc), OpenSCENARIO 2, Python (tools built with AI help), Linux (5 years), Git, CI pipelines; C++ (reading). Not yet used: CATIA / 3DX, Polarion, ASME Y14.5 GD&amp;T"),
 ("Hands-on &amp; details", "Repairs own cars (multimeter fuse probing, torque wrench, calipers, micrometers), soldered motor cables to a PCB, builds PCs. British citizen, full UK driving licence, based in Coventry (commutable to Banbury), immediately available")], 0.22)]))

doc.build(s)
