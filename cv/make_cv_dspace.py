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
    c.drawString(M, H-23.5*mm, "Technical Application Engineer  |  Simulation, SIL / HiL & Model-Based Development")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_dSPACE.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Customer-facing application engineer with nearly 8 years in safety-critical automotive systems, from ADAS features at Jaguar Land Rover to an L4 automated driving stack at FiveAI / Bosch. Hands-on across the validation lifecycle: requirements, model-based work in MATLAB / Simulink and IPG CarMaker, SIL simulation, and HiL / ViL and vehicle testing. Much of my work is helping engineers adopt new simulation tools and workflows, so I am comfortable explaining technical capability in terms of customer value. I want to move into a technical sales role and bring my automotive validation experience to aerospace customers.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Simulation product adoption:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Understood users' workflows and pain points, onboarded teams onto the simulation toolchain, and triaged issues across tools, maps and data with several engineering teams.",
 "<b>SIL verification at scale:</b> Built 120+ parameterised OpenSCENARIO 2 scenarios generating thousands of test cases for an L4 driving stack (UN R79 lane change, Euro NCAP junction tests), run locally in a dev container and through the CI test pipeline.",
 "<b>Safety-critical evidence:</b> Defined pass/fail and KPI criteria and analysed results across 1,000+ hours of test data, giving clear findings to engineering and stakeholders.",
 "<b>Demonstrating new methods:</b> Built AI-assisted agent skills (GitHub Copilot) that turn regulation and test protocols into scenarios. I demonstrated them and coached colleagues until they were adopted across the project, increasing scenario output by an order of magnitude.",
 "<b>Tools &amp; dashboards:</b> Built Python tools and data pipelines that present simulation results on dashboards for engineers and decision-makers."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Model-based simulation (Simulink / CarMaker):</b> On a project comparing real vehicle, dyno with sensor emulation from recorded data, and pure simulation testing, calibrated a Simulink and IPG CarMaker vehicle model against real vehicle data, including parameter sweeps on steering torque PID gains.",
 "<b>HiL &amp; ViL validation:</b> Led verification of ADAS features on HiL and ViL rigs and on the proving ground, analysing ECU and network data with Vector CANoe and CANape.",
 "<b>Field diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>Customer-embedded:</b> Based at Jaguar Land Rover as feature owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Main technical link between the OEM, AVL and suppliers, presenting findings and agreeing solutions.",
 "<b>Safety-critical process:</b> Wrote requirements and test cases with traceability in DOORS and MKS Integrity (ASPICE V-model). Wrote ISO 26262 requirements for a lane change feature; trained in ISO 26262 and SOTIF."])
s += job("Part-Time Teacher and Program Planner", "Space Camp Turkey", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught space technology, physics and science to students aged 9 to 16, explaining complex aerospace topics simply."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental thermal modelling of an electric motor stator. Coursework included System Modelling and Simulation (MATLAB / Simulink) and Programming (C++)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: designed, built and controlled a 6-DOF Stewart motion platform, of the kind used in flight simulators (state-space modelling in MATLAB, control on Arduino)."])
s += e

rows = [("Simulation &amp; Validation","SIL, HiL / ViL, model calibration against real data, scenario-based testing, regression in CI, KPI analysis"),
 ("Model-Based Tools","MATLAB / Simulink, IPG CarMaker, MotorCAD, OpenSCENARIO 2"),
 ("Safety-Critical","ISO 26262, SOTIF, ASPICE V-model, requirements traceability (DOORS, MKS Integrity)"),
 ("Software &amp; Tools","Python, C++ (reading), Git, dev containers, Vector CANoe / CANape, Jira / Confluence, GitHub Copilot"),
 ("Customer Skills","Workflow discovery, demonstrations, onboarding and training, supplier and OEM liaison. English (C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
