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
    c.drawString(M, H-23.5*mm, "Systems Engineer  |  Requirements, Verification & Safety  |  MSc Sustainable Automotive")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_ZeroAvia.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Mechanical engineer (BSc) with an MSc in Sustainable Automotive Engineering and nearly 8 years in safety-related vehicle systems. My work covers the full systems engineering cycle: writing requirements, defining interfaces and system states, working with suppliers, and planning and running verification on rigs, in simulation and on real vehicles. My MSc dissertation was experimental thermal modelling of an electric machine, and I have a solid base in thermodynamics and heat transfer. I have not worked with hydrogen systems yet. I want to move into zero-emission propulsion and would bring a disciplined requirements, safety and test approach while I build hydrogen-specific knowledge.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Verification &amp; validation:</b> Plan and build scenario-based verification for an L4 automated driving system. Created 120+ parameterised OpenSCENARIO 2 scenarios generating thousands of test cases, linked to regulation (UN R79) and Euro NCAP requirements.",
 "<b>Performance analysis:</b> Defined pass/fail and KPI criteria and analysed results across 1,000+ hours of test data, feeding clear findings back to development teams.",
 "<b>Regulation into tests:</b> Turned regulation text and test protocols into precise, measurable test conditions. Built AI-assisted tools, adopted across the project, that greatly increased how many scenarios the team could create.",
 "<b>Tools &amp; data:</b> Wrote Python tools and data pipelines that process simulation results and present them on dashboards for engineering teams.",
 "<b>Cross-team integration:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member, triaging integration issues across tools and teams."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Requirements &amp; architecture:</b> Based at Jaguar Land Rover as feature owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Wrote use cases, system state diagrams and requirements, and broke them down from system to component level in DOORS and MKS Integrity (ASPICE V-model).",
 "<b>Supplier technical oversight:</b> Main technical contact between the OEM, AVL and suppliers. For example, when an alert triggered late at boundary conditions, I found the cause in test logs and agreed a sensor change with the supplier while keeping false alerts low.",
 "<b>Testing:</b> Wrote test cases traced to requirements and ran verification on HiL and ViL rigs and on the proving ground. Managed defects through to closure.",
 "<b>E-machine diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>System safety:</b> Wrote ISO 26262 functional safety requirements for a lane change feature. Trained in ISO 26262 and SOTIF (ISO 21448)."])
s += job("Mechanical Engineering Intern", "TEMSA Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Worked on the R&amp;D of an electric bus powertrain, calculating power and torque requirements in MATLAB / Simulink.",
 "Supported quality improvements on the production line."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental testing to find the variables of a thermal model of an electric motor stator. Modelled thermal, mechanical and electromagnetic behaviour of electric machines (MotorCAD, Portunus, MATLAB / Simulink).",
 "Coursework: Systems for Hybrid and Electric Vehicles, System Modelling and Simulation, Lightweight Materials and Structures (Ansys)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Core mechanical engineering, including thermodynamics and fluid mechanics. Dissertation: designed, built and controlled a 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino)."])
s += e

rows = [("Systems Engineering","Requirements and decomposition, interfaces, system state diagrams, traceability, V-model / ASPICE, DOORS, MKS Integrity"),
 ("Verification &amp; Test","Test planning, rig testing (HiL / ViL), proving ground, simulation, KPI and data analysis, defect management"),
 ("Safety","ISO 26262 (requirements written, trained), SOTIF / ISO 21448 (trained)"),
 ("Engineering Tools","MATLAB / Simulink, MotorCAD, Ansys, SolidWorks, Python, Vector CANoe / CANape, Git, Jira"),
 ("Languages","English (C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
