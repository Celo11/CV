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
    c.drawString(M, H-23.5*mm, "Systems Engineer  |  Requirements, Vehicle Systems Integration & Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_AlexanderDennis.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Systems engineer with 8 years in automotive product development, from driver assistance features at Jaguar Land Rover to an L4 automated driving system at FiveAI / Bosch. I have managed requirements from customer needs to verified tests (DOORS, MKS Integrity, ASPICE V-model), worked across mechanical, electrical and software disciplines, and worked closely with suppliers to solve problems. At FiveAI / Bosch I led a team of five and built an AI tool that turns regulation text into test scenarios, now used across the project. My EV background includes an MSc in Sustainable Automotive Engineering and electric bus powertrain work at TEMSA. I'm new to MBSE / SysML tools and keen to learn them.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Requirements to verification:</b> Turned UN R79, Euro NCAP and customer requirements into KPIs and pass/fail criteria for an L4 automated driving system, such as lane-change success and lateral acceleration limits, and checked results across 1,000+ hours of test data. One finding, lane-change success dropping on tighter curves that were still within spec, led to a steering controller fix.",
 "<b>Scenario-based validation:</b> Wrote 120+ parameterised OpenSCENARIO 2 scenarios that generate thousands of test cases, including Euro NCAP junction tests and UN R79 automatic lane change, plus reusable Euro NCAP templates. Compared the same tests across software versions to find the cause of regressions.",
 "<b>AI-enabled engineering process:</b> Built a GitHub Copilot and Copilot CLI helper that turns regulation and Euro NCAP rules into scenarios from reusable blocks, with validation checks that run after each scenario. Used across the project, it cut the time to write a scenario from about a day to about an hour. Taught colleagues to check AI output rather than just trust it.",
 "<b>Integration with partners:</b> On the ADA project with Volkswagen Group, where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. Founding member of the Simulation EcoSystem solutions team, which diagnosed problems across the partners' shared toolchains, maps and add-on tools; read the error logs between APIs and simulation tools to find where a fault really was.",
 "<b>Technical lead:</b> Led five engineers for a year on L4 scenario work (technical lead, not line manager). Taught them the tools and evaluation logic, and split the work so scenario creation and evaluation ran in parallel.",
 "<b>Tools:</b> Built Python tools with AI help: a JSON parameter GUI, an uploader and data pipelines into dashboards. Worked in the project monorepo with a dev container, the dt_flow CI pipeline and pull requests."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Feature owner at the customer:</b> Spent two years on-site at Jaguar Land Rover as feature owner for three corner-radar features: Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Owned them from requirements to testing, as the link between JLR, AVL and the radar supplier.",
 "<b>Requirements management:</b> Wrote use cases, state diagrams and requirements in DOORS and MKS Integrity (ASPICE V-model), breaking high-level requirements down to low-level ones. Defined the input and output signal list for each module and traced it against the state machines.",
 "<b>Verification:</b> Wrote test cases for each system state, traced to the requirements, and ran them on HiL and ViL rigs, in vehicles and on the proving ground. Tracked defects in RTC / RQM.",
 "<b>Root cause with a supplier:</b> Rear Cross Traffic Alert passed every HiL test but fired late, or not at all, on the proving ground. I designed a test matrix and refined it around the failure boundary, synchronised camera, CAN and radar logs in Vector CANoe, and found that targets near the edge of the radar's field of view were picked up late. Ran the boundary tests with the supplier's engineer on site and verified their calibration change on the track and the HiL rig.",
 "<b>Safety:</b> Wrote requirements for ACC, Lane Keep Assist, Highway Assist and Lane Change Assist, including ISO 26262 safety requirements for lane change, and took part in its FMEA. Trained in ISO 26262 and SOTIF.",
 "<b>Model-based work:</b> On a project comparing real-vehicle, vehicle-in-the-loop and pure simulation testing, fitted an external GNSS system to a test car for position ground truth, drove it on an airstrip and at HORIBA MIRA to collect data, and calibrated a Simulink / IPG CarMaker model against the recordings, including steering PID gain sweeps.",
 "<b>Electrified powertrain returns:</b> At the LEVC (London Taxi) factory, checked about 20 returned range-extender generators using a set procedure: multimeter checks at the connector pins, then powering the control unit from a bench supply to download its logs with the supplier's tool. Sent the measurements and logs to the supplier for root cause analysis."])
s += job("Part-Time Teacher and Programme Planner", "Space Camp Turkey", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught science and space technology to students aged 9 to 16, and planned schedules for student groups and teachers. This is where I learned to explain technical ideas simply."])
s += job("Mechanical Engineering Intern", "TEMSA Global (bus and coach manufacturer)", "Adana, Türkiye", "05/2014 – 08/2014", [
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
 ("Systems engineering", "Requirements management and traceability (DOORS, MKS Integrity), use cases, state diagrams, interface signal lists, ASPICE V-model, test cases per system state, defect tracking (RTC / RQM)"),
 ("Safety", "ISO 26262 safety requirements, FMEA (participant), ISO 26262 and SOTIF (trained)"),
 ("Modelling &amp; simulation", "MATLAB / Simulink, IPG CarMaker, MotorCAD, OpenSCENARIO 2, scenario-based testing"),
 ("Test &amp; vehicle", "HiL / ViL, vehicle and proving ground testing, Vector CANoe / CANape, CAN, GNSS ground truth, root cause analysis with suppliers"),
 ("EV &amp; powertrain", "Hybrid and EV systems (MSc), electric bus powertrain sizing (TEMSA), electric motor thermal modelling (MotorCAD), range-extender generator return checks (LEVC)"),
 ("Software &amp; AI", "Python tools and data pipelines (written with AI help), GitHub Copilot and Copilot CLI agent skills, checking AI output, Git, CI pipelines, Linux, VS Code; C++ (reading)"),
 ("Hands-on", "Multimeter and bench power supply fault-finding; wiring and soldering; I repair my own cars and build my own PCs"),
 ("Languages", "English (C2), Turkish (native), Italian (basic)")], 0.22)]))

s += section("Additional Information")
s.append(Paragraph("British citizen with a full UK driving licence. Based in Coventry and willing to relocate to any UK site.", body))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
