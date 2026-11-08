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
    c.drawString(M, H-21*mm, "Field Support & Test / Validation Engineer  |  Hands-on Hardware, Linux & Customer Sites")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.1)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Happy to travel UK & abroad   |   Immediately available")
    c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Synopsys.pdf", pagesize=A4,
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
s.append(Paragraph("Mechanical engineer with 8 years in test, validation and customer-facing support: 2 years on-site at Jaguar Land Rover with AVL, then 5 years on an L4 automated driving system at FiveAI / Bosch. I love hands-on work with hardware, test rigs and mechanical/electrical assemblies, and want to build my career in that direction. I have used Linux as my main workstation for 5 years, build Python tools, and diagnose faults from logs and with a multimeter and bench power supply. I have not yet worked with semiconductor emulation or prototyping hardware, or written bash / tcsh scripts beyond everyday Linux terminal use, and I learn new hardware and tools quickly. Immediately available and happy to travel in the UK and internationally.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Customer support &amp; adoption:</b> Trained Volkswagen Group partner engineers on FiveAI's simulation toolchain (ADA project) and was a founding member of the Simulation EcoSystem solutions team.",
 "<b>Log diagnosis &amp; issue resolution:</b> Diagnosed problems across partners' toolchains, maps and add-on tools by reading error logs between APIs and simulation tools, found where the fault lay, and worked with the right engineering team to fix it.",
 "<b>Linux, Python tools &amp; reporting:</b> Used Linux as my daily workstation in the project monorepo with a dev container, ran simulations through the dtflow CI pipeline, and used SSH to reach the GPU cluster. Built Python tools with AI help (JSON parameter GUI, uploader, data pipelines into dashboards) and tracked KPIs across 1,000+ hours of test data."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>On-site at customer site:</b> Based at Jaguar Land Rover for 2 years as feature owner for three corner-radar features (Rear Cross Traffic Alert, Blind Spot Monitor, Rear Pre-Crash); technical link between JLR, AVL and the hardware supplier.",
 "<b>Factory hardware inspection (LEVC):</b> At the LEVC (London Taxi) factory, inspected ~20 returned faulty range-extender generators following a test procedure: multimeter checks at connector pins (phase-to-phase resistance, continuity), powered the control unit from a low-voltage bench supply to download logs with the supplier's logging tool, and sent the data and reports to the supplier for root cause analysis.",
 "<b>Vehicle &amp; rig fault-finding:</b> Ran verification on dSPACE HiL and ViL rigs, in vehicles and on the proving ground, using Vector CANoe and CANape and tracking defects in RTC / RQM. When a module did not activate in vehicle tests, read the fault codes, checked fuses for voltage or communication faults, and powered modules on a 12 V bench supply to check them.",
 "<b>Hardware-software root cause:</b> An alert passed on the HiL rig (where simulated objects bypassed the radar antenna) but fired late on the track. Synchronised camera, CAN and radar logs in CANoe, traced the cause to the edge of the radar's field of view, and verified the supplier's calibration fix on site.",
 "<b>Fitting test hardware:</b> On AVL's DrivingCube ViL project, fitted an external GNSS system to the test vehicle for position ground truth and monitored logging health during test runs."])

s.append(Paragraph("<b>Part-Time Teacher</b>, Space Camp Turkey, 2013 – 2017: taught science and space technology to students aged 9 to 16.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global, 2014: supported quality work on the bus production line and sized an electric bus powertrain in MATLAB / Simulink.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Dissertation: designed a test to find the thermal model variables of an electric motor stator (thermocouple placement, enclosure, method; MotorCAD, Portunus, Simulink).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Dissertation: team project to design and build a 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino); wired the servo actuators, wrote Arduino code to command each servo to a set angle, and plotted encoder signals.", line))

s += section("Skills &amp; Hands-on Experience")
s.append(KeepTogether([grid([
 ("Hands-on &amp; hardware", "Builds own desktop PCs (chassis, board mounting, cabling), repairs own cars (traced a parasitic battery drain on a Mercedes V12 by multimeter probing across fuses; torque wrench, calipers, micrometers), wired car audio, soldered motor cables to a PCB, 12 V bench supply checks"),
 ("Test &amp; diagnostics", "dSPACE HiL and ViL rigs, vehicle testing, Vector CANoe / CANape, fault-code reading, RTC / RQM defect tracking (all at AVL); API and simulation error-log diagnosis, KPI reporting across 1,000+ hours of data (FiveAI)"),
 ("Linux &amp; software", "Linux (main workstation for 5 years), Python (tools built with AI help), Git, dev containers, CI pipelines, basic SSH; C++ (reading), MATLAB / Simulink, SolidWorks"),
 ("Customer &amp; travel", "2 years on-site at JLR, training and supporting Volkswagen Group partner engineers, supplier coordination. British &amp; Turkish citizen, full UK driving licence, immediately available, happy to travel domestically and internationally")], 0.22)]))

doc.build(s)
