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
    c.drawString(M, H-23.5*mm, "Forward-Deployed Engineer  |  Automated Driving, Simulation & Test Automation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_FDE.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Engineer with nearly 8 years in automotive, working directly with customers and users of safety-related driver assistance and automated driving systems. For two years I worked on-site at Jaguar Land Rover as the technical link between the customer, my company and suppliers. At FiveAI / Bosch I help users get value from an L4 simulation and test toolchain: I build test scenarios, fix integration problems, write Python tools and data pipelines, and explain results to non-specialists. I am not a classically trained software engineer. I learned most of my software skills on the job and with AI-assisted coding, and I check AI output carefully before relying on it.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Customer and user support:</b> Technical link between the core engineering teams and the people using our simulation tools. On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Triage tool, map (SDB/XODR) and simulation problems across several engineering teams so users can keep working.",
 "<b>Scenario design:</b> Write test scenarios in OpenSCENARIO 2 for an L4 automated driving stack, from functional to logical to concrete. Built 120+ parameterised scenarios that generate thousands of test cases, including Euro NCAP junction tests and UN R79 automatic lane change. Created reusable Euro NCAP templates for other projects.",
 "<b>Results and KPIs:</b> Defined pass/fail and KPI criteria, such as comfort limits for acceleration and deceleration across 1,000+ hours of test data. Checked thousands of simulation results against them and reported findings to the development teams.",
 "<b>Tools and data pipelines:</b> Write Python scripts to validate the stack on both simulation and real-world drive data. Built internal tools (a GUI for JSON test parameters, a local STAX uploader) and pipelines that send simulation results to front-end dashboards. Work in the project monorepo with its dev container and CI test pipeline (dtflow), and raise pull requests to the main code base.",
 "<b>AI-assisted workflows:</b> Built AI agent skills with GitHub Copilot that help engineers write scenarios from regulation text and existing scenario building blocks. Generated scenarios are checked against the source rules and run in simulation. Showed colleagues how to use AI tools and verify the output."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Embedded at the customer:</b> Worked on-site at Jaguar Land Rover for two years as feature owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. I was the technical link between the OEM, AVL and suppliers.",
 "<b>Requirements to test:</b> Wrote use cases, system state diagrams and performance requirements from customer needs. Also worked on feature design for Adaptive Cruise Control, Lane Keep Assist, Highway Assist and Lane Change Assist. Broke requirements down and wrote test cases for each system state, traced back to requirements (DOORS, MKS Integrity, ASPICE V-model).",
 "<b>Testing:</b> Ran verification on Hardware-in-the-Loop (HiL) and Vehicle-in-the-Loop (ViL) rigs and on the proving ground.",
 "<b>Fault-finding:</b> Used Vector CANoe and CANape to read vehicle network data and find root causes. For example, when an alert triggered late at boundary conditions, I found the cause in the logs and agreed a sensor field-of-view change with the supplier while keeping false alerts low. Tracked defects in Rational Team Concert (RTC/RQM).",
 "<b>Field diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>Safety:</b> Wrote ISO 26262 functional safety requirements for a lane change feature. Trained in ISO 26262 and SOTIF (ISO 21448)."])
s += job("Part-Time Teacher and Program Planner", "Space Camp Turkey (associated with NASA)", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught space technology, physics, chemistry and biology to students aged 9 to 16, and planned schedules for student groups and teachers. This is where I learned to explain technical topics simply."])
s += job("Mechanical Engineer Internship", "Temsa Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Calculated power and torque requirements for a new electric bus powertrain in MATLAB/Simulink, and supported quality work on the production line."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). <b>Dissertation:</b> lab testing to find the variables of a thermal model of an electric motor stator, with modelling in MotorCAD, Portunus and MATLAB/Simulink.",
 "<b>Coursework:</b> Systems for Hybrid and Electric Vehicle Applications; System Modelling and Simulation (MATLAB/Simulink); Fundamentals of Computing and Programming (C++)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "<b>Dissertation:</b> designed, built and controlled a 6-DOF Stewart motion platform: modelled in MATLAB and ran the control code on an Arduino Uno."])
s += e

s += section("Skills")
s.append(KeepTogether([grid([
 ("Customer-facing", "On-site client work (2 years), requirements discovery, supplier and stakeholder coordination, root cause analysis, technical explanations and training"),
 ("Software", "Python (test automation, data analysis with pandas, tooling), C++ (reading, coursework), Git / GitHub, monorepo and dev containers, JSON, MATLAB / Simulink"),
 ("Simulation &amp; Test", "L4 automated driving, OpenSCENARIO 2, scenario-based testing, SIL / HiL / ViL, KPI analysis, regression testing, map formats (SDB / XODR), CarMaker, Vector CANoe / CANape, CAN, CAN FD, Ethernet"),
 ("Engineering Tools", "MATLAB / Simulink, MotorCAD, Portunus, Ansys Mechanical, SolidWorks, Arduino"),
 ("AI Tools", "GitHub Copilot and Copilot CLI, agent skills, AI-assisted coding, checking AI output against rules and simulation"),
 ("Process &amp; Safety", "Agile and V-model / ASPICE, ISO 26262 and SOTIF (trained), Euro NCAP, UN R79, DOORS, MKS Integrity, Rational Team Concert (RTC/RQM), Jira, Confluence"),
 ("Hands-on", "I build and repair my own desktop computers and cars at home"),
 ("Languages", "English (C2), Turkish (Native)")], 0.22)]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
