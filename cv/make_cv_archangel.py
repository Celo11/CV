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
    c.drawString(M, H-23.5*mm, "Field & Test Engineer  |  Autonomous Systems Integration & Support")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Archangel.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Mechanical engineer with nearly 8 years testing, integrating and supporting autonomous and driver assistance systems, from ADAS features at Jaguar Land Rover to an L4 automated driving stack at FiveAI / Bosch. Hands-on with test rigs, vehicle and proving ground testing, sensor issues and fault-finding, and used to being the first point of contact for customers and suppliers when something goes wrong. I have not worked with UAVs, ArduPilot or PX4 yet, but I built and controlled a 6-DOF motion platform at university, repair my own cars, and learn new systems quickly. Full UK driving licence, happy to travel, British national willing to undergo security vetting.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>First-line support:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. First point of contact when users hit problems across the stack, tools, maps (SDB / XODR) and simulation. I take ownership, find the root cause and bring in the right engineering team to fix it.",
 "<b>Testing autonomy in simulation and the real world:</b> Built 120+ parameterised OpenSCENARIO 2 test scenarios for an L4 automated driving stack and analysed results across 1,000+ hours of real-world and simulation data.",
 "<b>Preparing builds for testing:</b> Configured and ran the stack locally in the project's dev container (Linux) and through the CI test pipeline, working with software engineers to get releases ready for testing.",
 "<b>Documentation &amp; knowledge sharing:</b> Wrote guides and coached colleagues on new tools, including AI agent skills (GitHub Copilot) that I built and that were adopted project-wide.",
 "<b>Tools:</b> Built Python tools (a GUI for JSON test parameters, an uploader) and data pipelines to dashboards."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>On-site customer engineer:</b> Based at Jaguar Land Rover for two years as feature owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash (corner radar features). Main technical contact between the OEM, AVL and the sensor supplier.",
 "<b>Ground and vehicle testing:</b> Ran tests on HiL and ViL rigs, in vehicles and on the proving ground, and recorded results and issues through to closure.",
 "<b>Sensor fault-finding:</b> Diagnosed issues from vehicle network logs with Vector CANoe and CANape. For example, I traced a late alert at boundary conditions to radar field of view and agreed a fix with the supplier.",
 "<b>Field diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>Simulation vs real world:</b> Calibrated a Simulink / IPG CarMaker vehicle model against real vehicle data, including steering PID tuning, to compare vehicle, dyno and simulation testing.",
 "<b>Requirements &amp; safety:</b> Wrote requirements and test cases in DOORS and MKS Integrity (ASPICE). Wrote ISO 26262 functional safety requirements; trained in ISO 26262 and SOTIF."])
s += job("Part-Time Teacher and Program Planner", "Space Camp Turkey", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught space technology and flight science to students aged 9 to 16, and planned schedules for groups and teachers."])

s += [CondPageBreak(40*mm)] + section("Hands-on Projects")
s += job("6-DOF Stewart Motion Platform (BSc dissertation)", "Ege University", "Izmir, Türkiye", "2016 – 2017", [
 "Designed the platform in SolidWorks, built the prototype, modelled its motion in MATLAB with state-space equations, and wrote the control code on Arduino."])
s += job("Home Car Repairs &amp; PC Builds", "Personal", "Coventry, United Kingdom", "Ongoing", [
 "Diagnose and repair my own cars using workshop manuals and wiring diagrams. Build and set up my own desktop computers."])

e = [CondPageBreak(50*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental thermal modelling of an electric motor stator, including lab testing (MATLAB / Simulink, MotorCAD)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: 6-DOF Stewart motion platform (see Hands-on Projects)."])
s += e

rows = [("Test &amp; Integration","HiL / ViL rigs, vehicle and proving ground testing, simulation testing, sensor (radar) fault-finding, test records and issue tracking"),
 ("Hands-on","Prototype build (SolidWorks, Arduino), mechanical and electrical diagnosis on vehicles, PC building"),
 ("Software &amp; Tools","Python, C++ (reading), Linux dev containers, Git, MATLAB / Simulink, IPG CarMaker, Vector CANoe / CANape, Jira / Confluence"),
 ("Safety","ISO 26262, SOTIF, ASPICE"),
 ("Other","British national, full UK driving licence, willing to travel 25–50% and undergo security vetting. English (C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
