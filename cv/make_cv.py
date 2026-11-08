from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable)

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
    c.drawString(M, H-23.5*mm, "Solutions / Forward-Deployed Engineer  |  L4 Autonomous Driving & Simulation")
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 8.3)
    c.drawString(M, H-30*mm, "Immediately Available (No Notice Period)   |   +44 07397791625   |   muhammetcelalgokalp@gmail.com")
    c.setFont("Helvetica", 8.1)
    c.drawString(M, H-34*mm, "Coventry, CV5 8HN, UK   |   British & Turkish Citizen   |   linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
                      author="Muhammet Celal Gokalp", leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([
    PageTemplate("first", [Frame(M, 12*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header),
    PageTemplate("later", [Frame(M, 12*mm, cw, H-9*mm-18*mm, 0,0,0,0)], onPage=later)])
from reportlab.platypus import NextPageTemplate

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.2, color=ACC, spaceBefore=1, spaceAfter=4)]

def job(r, o, where, dates, bullets):
    t = Table([[Paragraph(r, role), Paragraph(dates, meta)],
               [Paragraph(o, org), Paragraph(where, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([t, Spacer(1,2), items[0]]), *items[1:], Spacer(1,5)]

s = []
s += section("Professional Summary")
s.append(Paragraph("Solutions / Forward-Deployed Engineer specializing in bridging complex autonomous systems and simulation software with end-user requirements. Proven track record of managing end-to-end workflows, collaborating with cross-functional stakeholders, and architecting data pipelines that turn raw simulation data into actionable frontend insights. Expertise in L4 autonomous driving stacks, OpenSCENARIO, Python, and translating cutting-edge R&amp;D into highly reliable, scalable solutions for major automotive OEMs and AI platforms.", body))
s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Customer training &amp; solutions:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member, diagnosing problems across the partners' shared toolchains, maps (SDB/XODR) and add-on tools.",
 "<b>Scalable Scenario Architecture:</b> Architected 120+ foundational concrete test scenarios using OpenSCENARIO 2 (OSC2) modular syntax, parameterizing them to generate thousands of complex edge-case variations for rigorous L4 stack validation.",
 "<b>AI-Driven Tooling &amp; Automation:</b> Leveraged agentic AI workflows to rapidly prototype and deploy custom internal tools, including a GUI for JSON parameter configuration and a local STAX uploader, enabling direct Pull Request (PR) contributions to core software repositories.",
 "<b>Data Pipeline &amp; Analytics Integration:</b> Evaluated thousands of high-level simulation results against strict validation and KPI criteria, engineering pipelines to route complex data to frontend analysis pages and translating system behaviours into actionable design improvements.",
 "<b>Standardization &amp; Compliance:</b> Engineered modular EuroNCAP Simax test scenario templates for Core projects, bridging prior real-world ADAS testing expertise with virtual simulation pipelines to scale the team's development capacity."])
s += job("ADAS Systems / Solutions Engineer", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "Embedded with the client as ADAS Feature Owner at Jaguar Land Rover (Rear Cross Traffic Alert, Blind Spot Monitor, Rear Pre Crash), serving as the primary technical bridge between AVL and OEM stakeholders.",
 "Led validation and verification of ADAS features on Hardware-in-the-Loop (HiL) and Vehicle-in-the-Loop (ViL) testing platforms.",
 "At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "Designed ADAS features (Intelligent Adaptive Cruise Control, Lane Keep Assist, Highway Assist, Lane Change Assist) by authoring use cases, key performance requirements, system state diagrams, and test cases in DOORS and MKS Integrity.",
 "Managed and triaged critical system defects using Rational Team Concert (RTC and RQM), ensuring swift resolution and deployment for client projects."])
s += job("Mechanical Engineer Internship", "Temsa Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Participated in R&amp;D of a new electric bus powertrain, calculating power and torque requirements using MATLAB/Simulink.",
 "Contributed to quality improvements and optimization of the manufacturing production line."])
s += job("Part-Time Teacher and Program Planner", "Space Camp Turkey (associated with NASA)", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught space technologies, physics, chemistry, and biology to students aged 9 to 16.",
 "Managed complex program schedules for student groups and assigned teachers."])

def edu(t, d, u, bl):
    tb = Table([[Paragraph(t, role), Paragraph(d, meta)],[Paragraph(u, org), ""]], colWidths=[cw*0.68, cw*0.32])
    tb.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    return [KeepTogether([tb, Spacer(1,2)] + [Paragraph(b, bul, bulletText="•") for b in bl]), Spacer(1,5)]
from reportlab.platypus import CondPageBreak
e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit)",
 "<b>Dissertation:</b> Experimental Determination of Variables in a Thermal Model of a Wound Stator; modelled electric machines for hybrid and electric vehicles (thermal, mechanical, electromagnetic) via MotorCAD and Portunus.",
 "<b>Coursework:</b> Systems for Hybrid and Electric Vehicle Applications; System Modelling and Simulation (MATLAB/Simulink); Fundamentals of Computing and Programming (C++, Visual Studio); Lightweight Materials and Structure (Ansys Mechanical)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "<b>Dissertation:</b> Manufacturing a Prototype 6-Degree of Freedom Stewart Simulation System; modelled platform movements in MATLAB using state-space equations and developed control algorithms using the Arduino Uno."])
s += e
s += section("Technical Skills")
rows = [("Programming &amp; Scripting","Python (Advanced Data Analytics), MATLAB &amp; Simulink, C++, OpenSCENARIO (OSC2) DSL"),
 ("Tools &amp; Platforms","Git (GitHub), Atlassian Stack (Jira, Confluence), Vector CANoe / CANape, MKS Integrity, RMDV2 DOORS, Rational Team Concert"),
 ("Engineering &amp; Simulation","HiL/ViL Testing, L4 Automated Driving Systems, Automated Data Analysis, MotorCAD, Ansys Mechanical"),
 ("Languages","English (C2 Proficient), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.25, cw*0.75])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether([sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
