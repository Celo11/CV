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
    c.drawString(M, H-23.5*mm, "Verification & Validation Lead  |  ADAS & Automated Driving Systems")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_ABDynamics.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Verification and validation engineer with nearly 8 years on ADAS and automated driving systems, and one year leading a team of five engineers. I have planned and run functional, performance and safety testing across HiL and ViL rigs, simulation and the proving ground, managed requirements and traceability in DOORS and MKS Integrity, and built tools that automate test creation and analysis. At FiveAI / Bosch I led a five-person scenario development team, training them on our tooling and evaluation logic and splitting the work between scenario creation and evaluation. I am ready to step up into a formal team lead role.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Team leadership:</b> Led a team of five engineers for a year on scenario development for an L4 automated driving system. Trained them on FiveAI's tooling and evaluation logic, planned and allocated work across scenario creation and evaluation, and reviewed their output.",
 "<b>Test planning &amp; execution:</b> Built 120+ parameterised OpenSCENARIO 2 scenarios generating thousands of test cases, covering Euro NCAP junction tests and UN R79 automatic lane change (ADA project), from functional to logical to concrete scenarios.",
 "<b>Performance &amp; safety evaluation:</b> Defined pass/fail and KPI criteria, such as comfort limits on acceleration and deceleration, and analysed results across 1,000+ hours of real-world and simulation data.",
 "<b>Automated test environments:</b> Ran regression through the CI test pipeline (dtflow) and in the project's dev container. Built LLM agent skills (GitHub Copilot) that generate scenarios from regulation text, adopted project-wide and increasing scenario output by an order of magnitude.",
 "<b>Tools &amp; collaboration:</b> Built Python tools (a GUI for JSON test parameters, an uploader) and pipelines to results dashboards. On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member, working across several engineering teams to resolve integration issues."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Hardware and software validation:</b> Led verification of corner radar ADAS features (Rear Cross Traffic Alert, Blind Spot Monitor, Rear Pre-Crash) on HiL and ViL rigs, in vehicles and on the proving ground, working on-site at Jaguar Land Rover for two years as feature owner.",
 "<b>Requirements validation &amp; traceability:</b> Wrote use cases, system state diagrams and requirements, broke them down from system to component level, and traced test cases to each state in DOORS and MKS Integrity (ASPICE V-model). Managed defects in RTC / RQM through to closure.",
 "<b>Supporting system design:</b> Wrote use cases and requirements for Adaptive Cruise Control, Lane Keep Assist, Highway Assist and Lane Change Assist, and reviewed module input and output signal lists against the state machines.",
 "<b>Root cause &amp; calibration:</b> Diagnosed issues from CAN data with Vector CANoe and CANape. Traced a late alert at boundary conditions to radar field of view and agreed a fix with the supplier. Calibrated a Simulink / IPG CarMaker vehicle model against real vehicle data.",
 "<b>Field diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>Safety:</b> Wrote ISO 26262 functional safety requirements for a lane change feature; trained in ISO 26262 and SOTIF."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental thermal modelling of an electric motor stator, including lab testing (MATLAB / Simulink, MotorCAD)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: designed, built and controlled a 6-DOF Stewart motion platform (SolidWorks, state-space modelling in MATLAB, Arduino control)."])
s += e

rows = [("Leadership","Led a team of five engineers for one year: training, work allocation, output review"),
 ("V&amp;V","Test planning, functional, performance and safety testing, HiL / ViL, simulation, proving ground and track testing, CI regression, KPI analysis"),
 ("Requirements","DOORS, MKS Integrity, RTC / RQM, traceability, ASPICE V-model, ISO 26262, SOTIF"),
 ("Tools","Python, Vector CANoe / CANape, MATLAB / Simulink, IPG CarMaker, OpenSCENARIO 2, Git, Jira / Confluence, C++ (reading)"),
 ("Other","Full UK driving licence, willing to travel. English (C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
