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
    c.drawString(M, H-23.5*mm, "Lead Application Engineer  |  Autonomous Systems, Validation & Customer Applications")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Applications_Product_Lead.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - CV", author="Muhammet Celal Gokalp", leftMargin=M, rightMargin=M)
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
s.append(Paragraph("Engineer with 8 years in automated driving and driver assistance, working between customers, suppliers and engineering teams. When someone makes a technical claim, my instinct is to ask how we prove it. At AVL, on-site at Jaguar Land Rover, I owned three radar-based features from customer needs to proving-ground tests. When one passed every rig test but failed on the track, I designed the tests that traced it to the edge of the radar's field of view. At FiveAI / Bosch I trained Volkswagen Group partner engineers on our L4 simulation toolchain, was a founding member of the team that solved their integration problems, and set the KPIs that show whether the system meets UN R79 and Euro NCAP. I enjoy building practical tools and learning new technology, and I'm keen to learn navigation and advanced sensing in depth.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Customer work:</b> On the ADA project with Volkswagen Group, where FiveAI supplied the simulation tools, trained partner engineers on our toolchain. This grew into the Simulation EcoSystem solutions team; I was a founding member.",
 "<b>Problem-solving:</b> Diagnosed problems across the partners' shared toolchains, maps and add-on tools. Read the error logs between APIs and simulation tools to see where a fault really was, and got the right team to fix it.",
 "<b>Proving performance:</b> Turned UN R79, Euro NCAP and customer requirements into KPIs and pass/fail criteria, such as lane-change success and lateral acceleration limits, and checked results across 1,000+ hours of test data. One finding, lane-change success dropping on tighter curves that were still within spec, led to a steering controller fix. Compared the same tests across software versions to find the cause of regressions.",
 "<b>Test methods at scale:</b> Wrote 120+ parameterised OpenSCENARIO 2 scenarios that generate thousands of test cases, including Euro NCAP junction tests and UN R79 automatic lane change, plus reusable Euro NCAP templates.",
 "<b>From prototype to project tool:</b> Built a GitHub Copilot helper that turns regulation and Euro NCAP rules into scenarios from reusable blocks. Checked its output in stages: errors, then failures, then spot-checks of passing runs to catch missing checks. It is now used across the project and cut the time to write a scenario from about a day to about an hour.",
 "<b>Team lead:</b> Led five engineers for a year on L4 scenario work (technical lead, not line manager). Taught them the tools and evaluation logic, and split the work so scenario creation and evaluation ran in parallel.",
 "<b>Tools and software:</b> Built Python tools with AI help: a JSON parameter GUI, an uploader and data pipelines into dashboards. Work in the project monorepo with a dev container, the dt_flow CI pipeline and pull requests; visualise results in Foxglove. Run a ROS 1 setup locally at user level: a VLA model in Docker with rosbridge and a simulator interface."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Embedded with the customer:</b> Two years at Jaguar Land Rover as feature owner for three corner-radar features: Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Link between JLR, AVL and the radar supplier.",
 "<b>Customer needs to engineering work:</b> Turned customer needs into use cases, state diagrams and requirements (DOORS, MKS Integrity, ASPICE V-model), defined the signal list for each module, and wrote test cases for each system state. Tested on HiL and ViL rigs, in vehicles and on the proving ground, and tracked defects in RTC / RQM.",
 "<b>Checking a sensor's real performance:</b> Rear Cross Traffic Alert passed every HiL test, where simulated objects bypassed the radar's own detection, but fired late or not at all on the proving ground. I designed a test matrix (approach angle, target type and speed, vehicle speed), ran a coarse grid, then finer steps at the failure boundary. For ground truth, we marked positions on the ground when the alert fired and cross-checked the timing against the logs.",
 "<b>Root cause and fix:</b> Synchronised camera, CAN and radar data in Vector CANoe and compared failing runs with the nearest passing ones: targets near the edge of the radar's field of view were picked up late. Ran the boundary tests with the supplier's engineer on site, and verified their calibration change on the track and the HiL rig.",
 "<b>Comparing test methods:</b> On a project comparing real-vehicle, vehicle-in-the-loop (dyno with sensor emulation) and pure simulation testing, fitted an external GNSS system to a test car for position ground truth and drove it on an airstrip and at HORIBA MIRA to collect data. Checked the set-up and logging before each vehicle-in-the-loop run, and calibrated a Simulink / IPG CarMaker model against the recordings, including sweeps of the steering PID gains.",
 "<b>Field returns:</b> At the LEVC (London Taxi) factory, checked about 20 returned range-extender generators with multimeter checks and bench-powered log downloads, and sent the data to the supplier for root cause analysis.",
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
 "<b>Final-year team project:</b> a 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino). I did the wiring and the Arduino code to drive each servo to a commanded angle, and plotted the signals to check them."])
s += e

s += section("Skills")
s.append(KeepTogether([grid([
 ("Validation &amp; test design", "Test matrix design (coarse grid, then finer steps around the boundary), ground-truth measurement, KPI and pass/fail criteria, scenario-based testing (OpenSCENARIO 2, Euro NCAP, UN R79), regression checks across software versions; HiL / ViL, vehicle and proving ground testing (AVL)"),
 ("Sensors &amp; data", "Corner radar features and field-of-view limits; time-synchronised camera, CAN and radar logs in Vector CANoe / CANape; external GNSS for position ground truth; Foxglove; reading XODR and OSM maps"),
 ("Autonomy &amp; simulation", "L4 automated driving simulation toolchain (dt_flow, dt_launcher), IPG CarMaker, MATLAB / Simulink; ROS 1 and Docker at user level"),
 ("Software", "Python tools and data pipelines (written with AI help), JSON, Git and pull requests, CI pipelines, dev containers, GitHub Copilot and Copilot CLI; C++ (reading); Linux as my main workstation for 5 years; VS Code"),
 ("Customer &amp; team", "Two years on-site at a customer (JLR); training partner engineers; supplier coordination; turning customer needs into requirements and tests (DOORS, MKS Integrity, ASPICE V-model); technical lead for five engineers"),
 ("Hands-on", "Multimeter and bench power supply fault-finding; fitting GNSS to a test car; wiring and soldering; I repair my own cars and build my own PCs"),
 ("Languages", "English (C2), Turkish (native), Italian (basic)")], 0.22)]))

s += section("Additional Information")
s.append(Paragraph("British citizen with a full UK driving licence. No current security clearance; willing to undergo vetting. Based in Coventry and willing to relocate to Bristol. Outside work I'm learning applied AI engineering in my own time.", body))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
