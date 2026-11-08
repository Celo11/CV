from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable,
                                NextPageTemplate, CondPageBreak)

NAVY = colors.HexColor("#14213D"); ACC = colors.HexColor("#1F7A8C")
GREY = colors.HexColor("#555555"); LIGHT = colors.HexColor("#E8F1F4")
W, H = A4; M = 16*mm; HB = 38*mm

def S(n, **k): return ParagraphStyle(n, fontName=k.pop("f", "Helvetica"), **k)
body = S("b", fontSize=9.2, leading=13, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=1.5)
sec = S("sec", f="Helvetica-Bold", fontSize=11.5, leading=14, textColor=NAVY, spaceBefore=9)
role = S("r", f="Helvetica-Bold", fontSize=10.3, leading=13, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=9.5, leading=12, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=8.8, leading=12, textColor=GREY, alignment=2)
loc = S("l", fontSize=8.8, leading=12, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 23)
    c.drawString(M, H-17*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 10.5); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-23.5*mm, "Application Engineer  |  Hands-on Vehicle & Hardware Systems")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Formlabs.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
                      author="Muhammet Celal Gokalp", leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([
    PageTemplate("first", [Frame(M, 12*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header),
    PageTemplate("later", [Frame(M, 12*mm, cw, H-9*mm-18*mm, 0,0,0,0)], onPage=later)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.2, color=ACC, spaceBefore=1, spaceAfter=4)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    if len(items) <= 2:
        return [KeepTogether([head_table(r, dates, o, where), Spacer(1,2), *items]), Spacer(1,5)]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,2), items[0]]), *items[1:], Spacer(1,5)]

def edu(t, d, u, bl):
    return [KeepTogether([head_table(t, d, u, ""), Spacer(1,2)] + [Paragraph(b, bul, bulletText="•") for b in bl]), Spacer(1,5)]

s = []
s += section("Professional Summary")
s.append(Paragraph("Mechanical engineer with nearly 8 years in automotive engineering, including 2 years based at a customer site (Jaguar Land Rover). Comfortable with hands-on work: testing in vehicles and on test rigs, finding faults on the vehicle network, and working with suppliers to fix them. Outside work, I built a 6-DOF motion platform at university and I repair my own cars at home. I enjoy explaining technical topics simply, from teaching science at Space Camp Turkey to supporting engineers at customers. I learn new systems quickly and I am happy to travel for on-site work.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "Technical link between the core engineering teams and enterprise customers using our simulation tools for automated driving.",
 "On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member; triage and fix toolchain and map integration issues (SDB/XODR) so customers can keep working without interruption.",
 "Build small internal tools (e.g. a GUI for JSON parameter set-up and a local STAX uploader) that make day-to-day work faster for the wider team.",
 "Write and run test scenarios (OpenSCENARIO 2, Euro NCAP, UN R79 lane change) and review the results to find and report issues."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "Based at the Jaguar Land Rover site for 2 years as AVL's technical contact for ADAS features (Rear Cross Traffic Alert, Blind Spot Monitor, Rear Pre-Crash).",
 "Tested features in vehicles on the proving ground and on Hardware-in-the-Loop (HiL) and Vehicle-in-the-Loop (ViL) rigs.",
 "Found faults by connecting to the vehicle CAN network with Vector CANoe and CANape and reading the data logs.",
 "At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "Worked with suppliers and engineers to fix defects, e.g. adjusting a sensor's field of view when an alert triggered late, and tracked fixes in Rational Team Concert.",
 "Wrote requirements and test cases in DOORS and MKS Integrity within an ASPICE V-model process."])
s += job("Mechanical Engineer Intern", "Temsa Global (bus manufacturer)", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Worked on quality improvements on the bus production line.",
 "Calculated power and torque needs for a new electric bus powertrain in MATLAB/Simulink."])
s += job("Part-Time Teacher and Program Planner", "Space Camp Turkey (associated with NASA)", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught space technology, physics, chemistry, and biology to students aged 9 to 16, using simple, hands-on explanations.",
 "Planned daily schedules for student groups and teachers."])

s += [CondPageBreak(50*mm)] + section("Hands-on Projects")
s += job("6-DOF Stewart Motion Platform (BSc dissertation)", "Ege University", "Izmir, Türkiye", "2016 – 2017", [
 "Designed the platform in SolidWorks, built the physical prototype, modelled its movement in MATLAB, and wrote the control code on Arduino."])
s += job("Home Car Repairs", "Personal", "Coventry, United Kingdom", "Ongoing", [
 "Buy, diagnose, and repair my own cars at home (including a Peugeot 306 HDi and a Ford Focus), using workshop manuals and wiring diagrams."])

e = [CondPageBreak(50*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation on the thermal model of an electric motor stator, including lab testing; MATLAB, Simulink, MotorCAD."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: 6-DOF Stewart motion platform (see Hands-on Projects)."])
s += e

s += section("Skills")
rows = [("Hands-on &amp; Diagnostics","Fault-finding, vehicle testing, HiL/ViL test rigs, Vector CANoe / CANape, prototype build, home mechanical repairs"),
 ("Customer &amp; Communication","On-site customer work (2 years at JLR), supplier coordination, teaching and explaining technical topics"),
 ("Software &amp; CAD","Python, MATLAB / Simulink, SolidWorks, Git, Jira, Confluence"),
 ("Languages","English (C2), Turkish (Native)"),
 ("Other","Full UK driving licence; happy to travel")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.25, cw*0.75])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether([sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
