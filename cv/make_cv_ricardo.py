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
body = S("b", fontSize=8.3, leading=11.0, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.8)
line = S("line", parent=body, spaceAfter=1.2)
sec = S("sec", f="Helvetica-Bold", fontSize=10.2, leading=12.0, textColor=NAVY, spaceBefore=3.5)
role = S("r", f="Helvetica-Bold", fontSize=9.4, leading=11.3, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.7, leading=10.8, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=8.2, leading=10.8, textColor=GREY, alignment=2)
loc = S("l", fontSize=8.2, leading=10.8, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 10.0); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Test Facility & Systems Engineer  |  BSc Mechanical & MSc Automotive Engineering")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.1)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   20 min from Leamington Spa   |   Immediately available")
    c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Ricardo.pdf", pagesize=A4,
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
s.append(Paragraph("Mechanical and automotive engineer (BSc Mechanical Engineering; MSc Sustainable Automotive Engineering, WMG Warwick) with 8 years in testing, validation and multi-discipline coordination at AVL Powertrain UK and FiveAI / Bosch. I love hands-on work with vehicles, test rigs, instrumentation and mechanical/electrical assemblies, and want to build my career in a test facility role. Experienced with Vehicle-in-the-Loop (DrivingCube) and HiL test beds, electrical and mechanical fault-finding, powertrain modelling, leading a team of 5 engineers, and serving as the primary technical contact across disciplines. I have not yet managed facility H&amp;S or asset maintenance schedules or led heavy driveline rig installations, and I learn new systems and procedures quickly. Based in Coventry (20 minutes from Leamington Spa) and immediately available.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Leading a team &amp; work packages:</b> Led a 5-person engineering team for a year on L4 validation scenarios (technical lead): selected team members, split work packages by experience, held weekly progress meetings, and reviewed deliveries against specifications.",
 "<b>Primary technical contact across disciplines:</b> Founding member of the Simulation EcoSystem solutions team on the Volkswagen Group ADA project. Served as first point of contact for partner engineers, coordinating across multiple engineering teams to diagnose and resolve cross-system faults.",
 "<b>Test planning, KPIs &amp; tooling:</b> Defined pass/fail and KPI criteria across 1,000+ hours of test data, wrote 120+ parameterised test scenarios, and built Python tools and reporting pipelines into dashboards so stakeholders could track test status."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Vehicle-in-the-Loop test bed (AVL DrivingCube) &amp; instrumentation:</b> Supported testing comparing a real vehicle, a chassis dyno with sensor emulation (DrivingCube) and pure simulation (Simulink / IPG CarMaker). Fitted an external GNSS system to the vehicle for position ground truth, drove airstrip and HORIBA MIRA circuit tests to calibrate the simulation PID controller, and monitored logging health and system readiness during test-bed runs.",
 "<b>Factory powertrain fault-finding (LEVC):</b> At the LEVC (London Taxi) factory, inspected ~20 returned faulty range-extender generators following a test procedure: ran multimeter checks at connector pins (phase-to-phase resistance, continuity), powered the control unit from a low-voltage bench supply to download supplier logs, and sent measurements and data to the supplier.",
 "<b>HiL, ViL &amp; vehicle fault-finding:</b> Ran verification on dSPACE HiL and ViL rigs, in vehicles and on the proving ground, using Vector CANoe and CANape and checking control-arm fasteners on a test vehicle with a torque wrench. When a module failed to activate in vehicle tests, read fault codes, checked fuses, and powered modules on a 12 V bench supply to isolate the fault.",
 "<b>Multi-discipline coordination (JLR):</b> Based on-site at Jaguar Land Rover for 2 years as feature owner for three corner-radar features, acting as the technical link between OEM engineering, AVL and the Tier 1 supplier. Synchronised camera, CAN and radar logs to trace a late track alert to the radar's field of view and verified the supplier's fix on site.",
 "<b>Safety &amp; requirements:</b> Wrote requirements and test cases in DOORS and MKS Integrity (ASPICE V-model), wrote ISO 26262 safety requirements for a lane change feature, and took part in its FMEA."])

s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global, 2014: calculated power and torque requirements for a new electric bus powertrain in MATLAB / Simulink, and supported quality work on the bus production line.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Coursework in hybrid and electric vehicle powertrain systems and Simulink modelling. Dissertation: designed a test to find the thermal model variables of an electric motor stator (type-K thermocouple placement, test enclosure and method; MotorCAD, Portunus, Simulink).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Dissertation: team project to design and build a 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino); wired the servo actuators, wrote Arduino code to command each servo to a set angle, and plotted encoder signals.", line))

s += section("Skills &amp; Hands-on Experience")
s.append(KeepTogether([grid([
 ("Test beds &amp; fault-finding", "AVL DrivingCube (ViL dyno test bed), dSPACE HiL and ViL rigs, proving ground testing, GNSS ground-truth fitting, Vector CANoe / CANape, multimeter (resistance / continuity / fuse probing), 12 V bench power supply (all at AVL)"),
 ("Mechanical &amp; hands-on", "SolidWorks &amp; engineering drawings, torque wrench (vehicle repairs &amp; test-vehicle control-arm checks), calipers and micrometers (used to set up and calibrate own tools), soldering, repairs own cars, builds desktop PCs"),
 ("Powertrain &amp; modelling", "Hybrid / EV powertrain systems (MSc &amp; TEMSA electric bus), electric motor stator thermal modelling &amp; thermocouple test design (MotorCAD, Portunus), range-extender generator checks (LEVC), MATLAB / Simulink, IPG CarMaker"),
 ("Coordination &amp; safety", "Technical lead for 5 engineers (FiveAI), 2 years on-site client &amp; supplier coordination (JLR), FMEA &amp; ISO 26262 (AVL), DOORS, RTC / RQM, Jira, Python tools, Linux. English (C2), Turkish (native), full UK driving licence")], 0.23)]))

doc.build(s)

