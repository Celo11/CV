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
    c.drawString(M, H-23.5*mm, "Customer Solutions Engineer  |  Technical Investigation, Integration & Training")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_EDMI.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Engineer with 8 years of customer-facing work in automotive driver assistance and automated driving. I moved into this field because my first employer's projects needed me there; my studies and personal interests are in electrification and clean energy. At Jaguar Land Rover I was the technical link between the customer, AVL and the radar supplier. At FiveAI / Bosch I trained Volkswagen Group partner engineers to use our simulation toolchain and was a founding member of the solutions team that diagnosed their integration problems. I enjoy investigating problems: reading logs, comparing failing and passing cases, and finding the real cause rather than the symptom. I explain technical ideas simply, a skill I first learned teaching science at Space Camp Turkey. Smart metering is new to me, and I am keen to learn it from the ground up and help EDMI's customers deploy it successfully.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Customer integration support:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member.",
 "<b>Technical investigation:</b> Diagnosed problems across the partners' shared toolchains, maps (SDB / XODR) and add-on tools. Read the error logs between APIs and simulation tools to work out where a fault really was, then got the right team to fix it.",
 "<b>Data analysis:</b> Set pass/fail and KPI criteria from UN R79, Euro NCAP and customer requirements, such as comfort limits on acceleration, and checked results across 1,000+ hours of test data. When results changed between software versions, compared the same tests across versions to find the cause. One finding, lane-change success dropping on tighter curves that were still within spec, led to a steering controller fix.",
 "<b>Test scenarios:</b> Wrote 120+ parameterised OpenSCENARIO 2 scenarios that generate thousands of test cases, including Euro NCAP junction tests and UN R79 automatic lane change, plus reusable Euro NCAP templates.",
 "<b>Team lead and training:</b> Led five engineers for a year on L4 scenario work (technical lead, not line manager). Taught them the tools and evaluation logic, and split the work so scenario creation and evaluation ran in parallel.",
 "<b>Improving the process:</b> Built a GitHub Copilot helper that turns regulation and Euro NCAP rules into scenarios from reusable blocks. It is used across the project and cut the time to write a scenario from about a day to about an hour. I reviewed its output in order: errors, then failures, then spot-checks of passing runs to catch missing checks.",
 "<b>Tools:</b> Built Python tools with AI help: a JSON parameter GUI, an uploader and pipelines that feed results into dashboards. Worked in the project monorepo with a dev container, the dt_flow CI pipeline and pull requests. Taught colleagues to use AI tools and to check their output rather than just trust it."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>On-site with the customer:</b> Spent two years at Jaguar Land Rover as feature owner for three corner-radar features: Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. I was the link between JLR, AVL and the radar supplier.",
 "<b>Root cause analysis:</b> An alert passed every HiL test but fired late, or not at all, on the proving ground. I designed a test matrix and refined it around the failure boundary, synchronised camera, CAN and radar logs in Vector CANoe, and compared failing runs with the nearest passing ones. Targets near the edge of the radar's field of view were being picked up late. I ran the boundary tests with the supplier's engineer on site and verified their calibration fix on the track and the HiL rig.",
 "<b>Requirements and testing:</b> Wrote use cases, state diagrams and requirements in DOORS and MKS Integrity (ASPICE V-model), defined the signal list for each module, and wrote test cases for each system state. Tested on HiL and ViL rigs, in vehicles and on the proving ground, and tracked defects in RTC / RQM.",
 "<b>Field returns:</b> At the LEVC (London Taxi) factory, checked about 20 returned range-extender generators using a set procedure: multimeter checks at the connector pins, then powering the control unit from a bench supply to download its logs with the supplier's tool. Sent the measurements and logs to the supplier's engineering team for root cause analysis.",
 "<b>Vehicle data and simulation:</b> On a vehicle-in-the-loop project, fitted GNSS to a test car, drove it on an airstrip and at HORIBA MIRA to collect data, checked the logging and set-up before each run, and calibrated a Simulink / IPG CarMaker model against the recordings.",
 "<b>Other features and safety:</b> Wrote requirements for ACC, Lane Keep Assist, Highway Assist and Lane Change Assist, including ISO 26262 safety requirements for lane change, and took part in its FMEA. Trained in ISO 26262 and SOTIF."])
s += job("Part-Time Teacher and Programme Planner", "Space Camp Turkey", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught science and space technology to students aged 9 to 16, and planned schedules for student groups and teachers. This is where I learned to explain technical ideas simply."])
s += job("Mechanical Engineering Intern", "TEMSA Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Calculated power and torque requirements for a new electric bus powertrain in MATLAB / Simulink."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "WMG, University of Warwick, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). <b>Coursework:</b> hybrid and electric vehicle systems, system modelling and simulation (MATLAB / Simulink), programming (C++), Ansys.",
 "<b>Dissertation:</b> designed a test to find the unknown values of a thermal model of an electric motor stator (thermocouple placement, enclosure and method), using MotorCAD's thermal network to understand the heat paths."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "<b>Final-year team project:</b> a 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino). I did the wiring and the Arduino code to drive each servo to a commanded angle."])
s += e

s += section("Skills")
s.append(KeepTogether([grid([
 ("Customer work", "Two years on-site at a customer (JLR); training partner engineers on a toolchain; working between customers, suppliers and engineering teams; explaining technical results simply"),
 ("Investigation", "Root cause analysis; log analysis in Vector CANoe / CANape (AVL) and simulation and API error logs (FiveAI); test matrix design; comparing failing and passing runs; regression checks across software versions; field-return checks"),
 ("Data &amp; software", "Python tools and data pipelines (written with AI help), JSON, Git and pull requests, CI pipelines, dev containers, Foxglove, MATLAB / Simulink; C++ (reading); Linux as my main workstation for 5 years; VS Code"),
 ("Test &amp; process", "HiL / ViL, vehicle and proving ground testing (AVL); simulation testing with OpenSCENARIO 2 and KPIs (FiveAI); requirements and traceability (DOORS, MKS Integrity, ASPICE V-model); defect tracking (RTC / RQM); FMEA; ISO 26262 and SOTIF (trained)"),
 ("AI tools", "GitHub Copilot and Copilot CLI, agent skills, checking AI output against the source rules and test results"),
 ("Energy &amp; electrification", "Hybrid and EV systems (MSc), electric bus powertrain sizing (TEMSA), electric motor thermal modelling (MotorCAD), range-extender generator returns (LEVC). New to smart metering and keen to learn"),
 ("Hands-on", "Multimeter and bench power supply fault-finding; traced a car's parasitic battery drain by measuring across each fuse, then replaced the faulty module; I repair my own cars and build my own PCs"),
 ("Languages", "English (C2), Turkish (native), Italian (basic)")], 0.22)]))

s += section("Additional Information")
s.append(Paragraph("British citizen with a full UK driving licence. Based in Coventry and willing to relocate within the UK. Interests: clean energy (solar and hydrogen), car repair, PC building and applied AI.", body))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
