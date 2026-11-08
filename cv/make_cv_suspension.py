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
    c.drawString(M, H-21*mm, "System & Software Test Engineer  |  HiL / Bench Testing, CAN Diagnostics & Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.1)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Immediately available")
    c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_System_Test_Engineer.pdf", pagesize=A4,
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
s.append(Paragraph("Mechanical engineer with 8 years in automotive systems, software testing and validation: 2 years on-site at Jaguar Land Rover with AVL, then 5 years on an L4 automated driving system at FiveAI / Bosch. I enjoy hands-on work with vehicles, test rigs and hardware, and want to build my career in that direction. My background covers dSPACE HiL and ViL testing, vehicle and proving ground testing, Vector CANoe and CANape on CAN, fault-code and fuse checks, DOORS, ASPICE and ISO 26262, plus Python tools and log diagnosis. I have not yet worked on active suspension or seating systems, or used NI VeriStand / TestStand or CAPL, and I learn new tools and systems quickly. Based in Coventry (15 minutes from Nuneaton) and immediately available.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Test scenarios &amp; KPIs:</b> Wrote 120+ parameterised OpenSCENARIO 2 scenarios generating thousands of test cases (UN R79 lane change, Euro NCAP), and defined pass/fail and KPI criteria such as comfort acceleration limits across 1,000+ hours of test data.",
 "<b>Log diagnosis &amp; cross-team support:</b> Founding member of the Simulation EcoSystem solutions team on the Volkswagen Group ADA project. Diagnosed errors from logs between APIs, maps and simulation tools, compared failing runs across software versions to find regressions, and worked with development teams to fix them.",
 "<b>Python tools &amp; workflow:</b> Built Python tools with AI help (JSON parameter GUI, uploader, data pipelines into dashboards) and a GitHub Copilot helper that turns regulation text into test scenarios. Worked in Linux in the project monorepo with a dev container and CI test pipeline."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>OEM &amp; Tier 1 interaction:</b> Based on-site at Jaguar Land Rover for 2 years as feature owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash; main technical link between JLR, AVL and the Tier 1 radar supplier.",
 "<b>HiL, ViL &amp; vehicle testing:</b> Wrote test cases for each system state and ran verification on dSPACE HiL and ViL rigs, in vehicles and on the proving ground. Used Vector CANoe and CANape to monitor CAN bus signals and log data, and tracked defects in RTC / RQM.",
 "<b>Root cause from logs:</b> An alert passed on the dSPACE HiL rig (where simulated objects bypassed the radar antenna) but fired late on the proving ground at a 45° approach. Designed a coarse-to-fine test matrix, synchronised camera, CAN and radar logs in CANoe, showed that targets near the edge of the field of view reached high confidence late, and ran boundary tests on site with the supplier to verify a calibration fix.",
 "<b>Hands-on fault-finding:</b> When a module did not activate during vehicle tests, read fault codes, checked fuses for voltage or communication faults, and powered modules from a 12 V bench supply to test them. At the LEVC factory, ran multimeter checks (phase-to-phase resistance, continuity) on ~20 returned range-extender generators and powered the control unit from a bench supply to download supplier logs.",
 "<b>Vehicle dynamics &amp; HORIBA MIRA (Nuneaton):</b> On AVL's DrivingCube ViL project, built Simulink / IPG CarMaker scenarios, fitted an external GNSS for position ground truth on airstrip tests, drove a circuit at HORIBA MIRA (Nuneaton) to capture data to calibrate the simulation PID controller, and monitored logging health during runs.",
 "<b>Requirements &amp; safety:</b> Wrote use cases, state diagrams, module signal lists and high- to low-level requirements in DOORS and MKS Integrity (ASPICE V-model). Wrote ISO 26262 safety requirements for a lane change feature and took part in its FMEA; trained in ISO 26262 and SOTIF."])

s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global, 2014: electric bus powertrain power and torque calculations in MATLAB / Simulink.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Dissertation: designed a test to find the thermal model variables of an electric motor stator (thermocouple placement, enclosure, method; MotorCAD, Portunus, Simulink).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Dissertation: team project to design and build a 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino); wired the servo actuators, wrote Arduino code to command each servo to a set angle, and plotted encoder signals.", line))

s += section("Skills &amp; Hands-on Experience")
s.append(KeepTogether([grid([
 ("Testing &amp; diagnostics", "dSPACE HiL and ViL rigs, vehicle and proving ground testing, Vector CANoe and CANape, CAN, fault-code reading, multimeter and 12 V bench supply checks (all at AVL); KPI and log analysis (AVL &amp; FiveAI)"),
 ("Standards &amp; tools", "ASPICE V-model, ISO 26262 and FMEA, SOTIF (trained), DOORS, MKS Integrity, RTC / RQM (all at AVL); Jira, Confluence, Git, CI pipelines"),
 ("Software &amp; simulation", "Python (tools and scripts built with AI help), Linux (main workstation for 5 years), MATLAB / Simulink, IPG CarMaker, OpenSCENARIO 2; C++ (reading)"),
 ("Hands-on &amp; personal", "Repairs own cars (traced a parasitic battery drain on a Mercedes V12 to a faulty module by multimeter probing across fuses; torque wrench, calipers, micrometers), wired car audio, soldered motor cables to a PCB, builds desktop PCs"),
 ("Languages &amp; details", "English (C2), Turkish (native). British citizen, full UK driving licence, based in Coventry (15 min from Nuneaton), immediately available")], 0.22)]))

doc.build(s)
