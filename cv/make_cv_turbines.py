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
    c.drawString(M, H-21*mm, "Mechanical, Systems & Test Engineer  |  Rotating Machinery, Controls & Test-Bed Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.1)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   DOB: 12/04/1993   |   Full UK driving licence   |   Immediately available")
    c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Turbines.pdf", pagesize=A4,
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
s.append(Paragraph("Mechanical engineer (BSc Mechanical Engineering; MSc Sustainable Automotive Engineering, WMG Warwick) with 8 years in systems engineering, control validation, test-bed / vehicle testing and fault-finding at AVL Powertrain UK and FiveAI / Bosch. My background includes stator thermal modelling and thermocouple test design for rotating electrical machines (MotorCAD, Portunus, Simulink), hands-on electrical checks on returned range-extender generators at the LEVC factory, PID controller calibration on AVL's DrivingCube dyno test bed, and requirements/safety engineering (DOORS, ASPICE V-model, ISO 26262, FMEA). I have not yet worked on gas, steam or wind turbines, and I am keen to move from automotive into the turbine and energy sector. I love hands-on work with hardware and test beds, learn new systems quickly, and am immediately available in Coventry.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Leading a team &amp; work packages:</b> Led a 5-person engineering team for a year (technical lead): selected team members, split work packages by tool experience, held weekly progress meetings, and reviewed deliveries against specifications.",
 "<b>Performance KPIs &amp; root cause analysis:</b> Defined pass/fail and performance KPI criteria across 1,000+ hours of test data, wrote 120+ parameterised test scenarios, and diagnosed errors from logs between APIs and simulation tools across partner teams (Volkswagen Group ADA project).",
 "<b>Python tools &amp; data pipelines:</b> Built Python tools with AI help (JSON parameter GUI, uploader, data pipelines into dashboards) and worked in Linux in the project monorepo with a dev container and CI test pipeline."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Generator &amp; rotating-machine fault-finding (LEVC factory):</b> Inspected ~20 returned faulty range-extender generators at the London Taxi factory following a test procedure: performed multimeter checks at specified connector pins (phase-to-phase resistance, continuity), powered the control unit from a low-voltage bench supply to download fault logs with the supplier's logging tool, and sent measurements and data to the supplier for root cause analysis.",
 "<b>Dyno test bed &amp; PID calibration (AVL DrivingCube):</b> Compared a real system, a chassis dyno with sensor emulation and a MATLAB / Simulink + IPG CarMaker model. Fitted external ground-truth instrumentation (GNSS), captured test data at HORIBA MIRA and on the airstrip, calibrated the model and swept PID controller gains, and monitored logging health during test-bed runs.",
 "<b>Requirements, state machines &amp; safety:</b> Based on-site at Jaguar Land Rover for 2 years as feature owner for three safety-related features. Wrote use cases, system state diagrams, module input/output signal lists and high- to low-level requirements in DOORS and MKS Integrity (ASPICE V-model). Wrote ISO 26262 safety requirements and took part in an FMEA.",
 "<b>Verification &amp; supplier root cause:</b> Wrote test cases for each system state and ran verification in vehicles and on the proving ground, using Vector CANoe and CANape and tracking defects in RTC / RQM. Synchronised camera, bus and sensor logs to trace a boundary timing fault and verified the supplier's calibration fix on site. Diagnosed module faults via fault codes, fuse checks and a 12 V bench supply."])

s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global, 2014: calculated power and torque requirements for a new electric bus powertrain in MATLAB / Simulink, and supported quality work on the production line.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Dissertation: designed a test to find the unknown values of a thermal model of an electric motor stator (type-K thermocouple placement, enclosure, method) using MotorCAD's thermal network, Portunus and MATLAB / Simulink.", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Dissertation: team project to design and build a 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space model, Arduino); wired the 6 servo actuators, wrote Arduino code to command set angles, and plotted encoder feedback signals.", line))

s += section("Skills &amp; Hands-on Experience")
s.append(KeepTogether([grid([
 ("Rotating machines &amp; thermal", "Electric motor stator thermal network modelling &amp; thermocouple test design (MotorCAD, Portunus, Simulink – MSc); range-extender generator resistance, continuity &amp; log checks (LEVC); powertrain sizing (TEMSA)"),
 ("Testing, test beds &amp; controls", "AVL DrivingCube (ViL dyno test bed), vehicle &amp; proving ground testing, PID gain sweeps, MATLAB / Simulink, Vector CANoe / CANape, multimeter &amp; 12 V bench supply fault-finding (all at AVL); KPI &amp; log analysis (AVL &amp; FiveAI)"),
 ("Systems &amp; safety", "Requirements decomposition, state diagrams, module signal lists, DOORS, MKS Integrity, RTC / RQM, ASPICE V-model, FMEA &amp; ISO 26262 (all at AVL); Jira, Confluence, technical lead for 5 engineers (FiveAI)"),
 ("Software &amp; hands-on", "Python (tools and pipelines built with AI help), Linux (5 years), Git, SolidWorks. Hands-on: repairs own cars (multimeter fuse probing, torque wrench, calipers, micrometers), soldered motor cables to a PCB, builds PCs"),
 ("Languages &amp; details", "English (C2), Turkish (native). British citizen, full UK driving licence, based in Coventry (close to Warwick / Rugby / Derby), immediately available")], 0.24)]))

doc.build(s)
