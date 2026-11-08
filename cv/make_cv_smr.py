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
    c.drawString(M, H-23.5*mm, "Systems Integration & Requirements Engineer  |  Safety-Related Systems")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_SMR.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Systems engineer with nearly 8 years on safety-related automotive systems, from driver assistance features at Jaguar Land Rover to an L4 automated driving stack at FiveAI / Bosch. My work is requirements, integration and verification across several disciplines: turning customer specifications into requirements, breaking them down for lower-level systems, tracing tests back to them, and resolving issues that cross system and supplier boundaries. I was feature owner for three driver assistance features at a customer site, and I am used to explaining technical issues to customer engineering teams. At FiveAI I led a scenario creation effort with a team of 5 people in India and trained junior engineers. <b>I have not been a formal line manager. I have not worked in nuclear or power generation, and I have not used MBSE tools such as Capella.</b> I am moving sector from automotive and I learn new domains quickly.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Leading work through others:</b> Led a scenario creation effort with a team of 5 people based in India. I chose the team members, split the work according to each person's experience with the tools, held weekly progress meetings, and reviewed deliveries to make sure they met the specification.",
 "<b>Cross-system integration:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Triage problems that cross tools, maps (SDB/XODR) and simulation, working with several engineering teams to find the cause and the owner so users can keep working.",
 "<b>Requirements to test:</b> Turned regulation text and test protocols (UN R79 automatic lane change, Euro NCAP junction tests) into test scenarios and acceptance criteria for an L4 automated driving stack. Built 120+ parameterised OpenSCENARIO 2 scenarios that generate thousands of test cases.",
 "<b>Performance attributes:</b> Defined pass/fail and KPI criteria, such as comfort limits for acceleration and deceleration across 1,000+ hours of test data. Checked thousands of simulation results against them and reported findings to the development teams.",
 "<b>Planning and delivery:</b> Plan and run large simulation test campaigns through the CI test pipeline (dtflow). Built Python tools and pipelines that send results to front-end dashboards so stakeholders can see status, and raise pull requests to the main monorepo.",
 "<b>Coaching:</b> Trained junior engineers on applications and methods. Showed engineers and non-software colleagues how to use AI tools in their daily work, including how to give good context and check the output rather than trust it. Built AI agent skills (GitHub Copilot) that help engineers write scenarios from regulation text."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Product-level ownership:</b> Worked on-site at Jaguar Land Rover for two years as feature owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. I was the technical link between the OEM, AVL and suppliers.",
 "<b>Requirements decomposition:</b> Translated customer specifications into use cases, system state diagrams and performance requirements. Broke high-level requirements down into low-level ones and wrote test cases for each system state, traced back to the requirements (DOORS, MKS Integrity, ASPICE V-model). Also worked on the feature design of Adaptive Cruise Control, Lane Keep Assist, Highway Assist and Lane Change Assist.",
 "<b>Integration and verification:</b> Ran verification on Hardware-in-the-Loop (HiL) and Vehicle-in-the-Loop (ViL) rigs and on the proving ground. Used Vector CANoe and CANape to read vehicle network data and find root causes. Tracked defects in Rational Team Concert (RTC/RQM).",
 "<b>Field diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>Cross-system issue and trade-off:</b> When an alert triggered late at boundary conditions, I found the cause in the logs and worked with the subsystem engineers and the supplier to agree a sensor field-of-view change, balancing earlier detection against more false alerts.",
 "<b>Safety:</b> Wrote ISO 26262 functional safety requirements for a lane change feature. Trained in ISO 26262 and SOTIF (ISO 21448)."])
s += job("Part-Time Teacher and Program Planner", "Space Camp Turkey (associated with NASA)", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught space technology, physics, chemistry and biology to students aged 9 to 16, and planned schedules for student groups and teachers."])
s += job("Mechanical Engineer Internship", "Temsa Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Calculated power and torque requirements for a new electric bus powertrain in MATLAB/Simulink, and supported quality work on the production line."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). <b>Dissertation:</b> lab testing to find the variables of a thermal model of an electric motor stator, with modelling in MotorCAD, Portunus and MATLAB/Simulink.",
 "<b>Coursework:</b> Systems for Hybrid and Electric Vehicle Applications; System Modelling and Simulation (MATLAB/Simulink)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "<b>Dissertation:</b> designed, built and controlled a 6-DOF Stewart motion platform: modelled in MATLAB and ran the control code on an Arduino Uno."])
s += e

s += [CondPageBreak(60*mm)] + section("How My Experience Maps to This Role")
s.append(grid([
 ("Requirements flow-down", "High-level to low-level requirements with traceable tests for each system state (DOORS, MKS Integrity, ASPICE V-model)"),
 ("Multi-discipline integration", "Worked with subsystem engineers, suppliers and software teams, on HiL / ViL rigs, the proving ground and in simulation"),
 ("Trade-offs and cross-system issues", "Sensor field of view against false alerts; tool, map and simulation triage at FiveAI"),
 ("Plant-level performance", "Defined and tracked performance KPIs across 1,000+ hours of data (automotive, not power output)"),
 ("Ownership and stakeholders", "Feature owner for three features, specification to verification, 2 years on-site with an OEM and its suppliers"),
 ("Leading and coaching", "Led a scenario creation effort with a team of 5 in India (chose people, split work by tool experience, weekly progress meetings, reviewed deliveries against the spec). Trained junior engineers on tools and methods.")], 0.27))
s.append(Spacer(1, 3))
s.append(Paragraph("<b>Not yet:</b> formal line management of engineers, nuclear or power station design, and MBSE tools such as Capella.", body))

s += section("Skills")
s.append(KeepTogether([grid([
 ("Systems Engineering", "Requirements decomposition and flow-down, traceability, use cases, system state diagrams, V-model / ASPICE, ISO 26262 and SOTIF (trained), DOORS, MKS Integrity, Jira, Confluence"),
 ("Integration &amp; Verification", "SIL / HiL / ViL, proving ground and scenario-based testing, KPI and root cause analysis, Vector CANoe / CANape, CAN, Ethernet, defect management (RTC / RQM), UN R79, Euro NCAP"),
 ("Software &amp; Tools", "Python (automation, pandas, tooling), Git / GitHub, C++ (reading), MATLAB / Simulink, MotorCAD, SolidWorks, GitHub Copilot"),
 ("Languages &amp; Eligibility", "English (C2), Turkish (Native). British national, UK resident 8+ years, willing to undergo BPSS, DBS and financial probity checks. Based in Coventry; Derby is the nearest site.")], 0.22)]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
