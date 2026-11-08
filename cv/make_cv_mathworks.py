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
    c.drawString(M, H-23.5*mm, "Application Engineer  |  Modelling, Simulation & Automotive Systems")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_MathWorks.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Automotive engineer with an MSc in Sustainable Automotive Engineering and nearly 8 years working with OEM and internal engineering teams on ADAS and automated driving. I have used MATLAB and Simulink for vehicle modelling and control: calibrating a Simulink and CarMaker vehicle model, including steering torque PID control, against real vehicle data; electric machine thermal modelling in my MSc; and state-space modelling and control of a 6-DOF motion platform in my BSc. I spend much of my time helping engineers adopt new tools and workflows, and I build AI-assisted tools that make teams more productive.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Workflow adoption with AI tools:</b> Built LLM agent skills with GitHub Copilot and Copilot CLI that help engineers write OpenSCENARIO 2 test scenarios from regulation and Euro NCAP rules. They were adopted project-wide and increased scenario output by an order of magnitude. I coached colleagues on using AI well and checking its output.",
 "<b>Simulation-based verification:</b> Built 120+ parameterised scenarios generating thousands of test cases for an L4 automated driving stack (UN R79 lane change, Euro NCAP junction tests). Defined KPI criteria and analysed results across 1,000+ hours of test data.",
 "<b>Toolchain &amp; DevOps:</b> Worked in the project monorepo and its dev container, ran simulations locally and through the CI test pipeline (dtflow), and raised pull requests in Git. Wrote Python tools and data pipelines that send simulation results to dashboards.",
 "<b>Supporting engineering teams:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Analysed users' workflows, triaged problems across tools, maps and simulation, and worked with developers to fix the root causes."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Vehicle model calibration (Simulink / CarMaker):</b> On a project comparing three test methods (real vehicle, dyno with sensor emulation from recorded data, and pure simulation), calibrated a Simulink and IPG CarMaker vehicle model against real vehicle recordings. Ran parameter sweeps on the steering torque PID gains and vehicle dynamics parameters until the simulated response matched the real vehicle.",
 "<b>Customer-embedded engineering:</b> Based at Jaguar Land Rover as feature owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Main technical link between the OEM, AVL and suppliers.",
 "<b>Requirements to verification:</b> Wrote use cases, system state diagrams and requirements in DOORS and MKS Integrity (ASPICE V-model), and verified them on HiL and ViL rigs and on the proving ground, using Vector CANoe and CANape for analysis.",
 "<b>Field diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>Safety:</b> Wrote ISO 26262 functional safety requirements for a lane change feature. Trained in ISO 26262 and SOTIF."])
s += job("Mechanical Engineering Intern", "TEMSA Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Calculated power and torque requirements for a new electric bus powertrain using MATLAB / Simulink."])
s += job("Part-Time Teacher and Program Planner", "Space Camp Turkey", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught space technology and science to students aged 9 to 16, explaining complex ideas simply."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental testing to find the variables of a thermal model of an electric motor stator. Modelled electric machines for hybrid and electric vehicles (thermal, mechanical, electromagnetic) with MotorCAD, Portunus and MATLAB / Simulink.",
 "Coursework: System Modelling and Simulation (MATLAB / Simulink), Systems for Hybrid and Electric Vehicles, Fundamentals of Computing and Programming (C++)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: designed and built a 6-DOF Stewart motion platform. Modelled its motion in MATLAB using state-space equations and developed the control algorithms, implemented on Arduino."])
s += e

rows = [("Modelling &amp; Control","MATLAB, Simulink, IPG CarMaker, vehicle dynamics model calibration, PID tuning by parameter sweeps, state-space modelling, MotorCAD, Portunus"),
 ("Software &amp; DevOps","Python, C++ (reading, MSc coursework), Git / GitHub, CI test pipelines, monorepo and dev containers, OpenSCENARIO 2"),
 ("AI Tools","Agent skills and prompting with GitHub Copilot and Copilot CLI, AI-assisted coding, coaching teams on AI adoption"),
 ("Automotive","ADAS and L4 automated driving, SIL / HiL / ViL, CANoe / CANape, DOORS, ASPICE, ISO 26262, SOTIF, Euro NCAP, UN R79"),
 ("Languages","English (C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
