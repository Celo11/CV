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
    c.drawString(M, H-23.5*mm, "Systems Engineer  |  Autonomy, Requirements, Interfaces & Verification")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_ShieldAI.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Systems engineer with nearly 8 years developing, integrating and verifying software-intensive autonomous and driver assistance systems, from ADAS features at Jaguar Land Rover to an L4 automated driving stack at FiveAI / Bosch. I translate customer needs and regulation into system and subsystem requirements, define module interfaces and state logic, and build verification strategies across simulation (SIL), HiL / ViL and real-world testing, with full traceability. I use logs, simulation and data to diagnose failures, and write Python tools to solve integration problems. British national with 8+ years' UK residence, willing to undergo security vetting.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Autonomy verification strategy:</b> Design scenario-based verification for an L4 automated driving stack (planning and decision-making behaviour), from functional to logical to concrete OpenSCENARIO 2 scenarios. Built 120+ parameterised scenarios generating thousands of test cases, traced to UN R79 lane change (ADA project) and Euro NCAP requirements.",
 "<b>Requirements to software behaviour:</b> Defined pass/fail and KPI criteria, such as comfort limits on acceleration and deceleration, and analysed results across 1,000+ hours of real-world and simulation data to show whether the stack met its requirements.",
 "<b>SIL integration &amp; failure diagnosis:</b> Ran simulations locally in the project's dev container and at scale through the CI test pipeline (dtflow). Read Python and C++ code, logs and simulation output to trace stack behaviour and find root causes.",
 "<b>Cross-team integration:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Triaged integration issues across the stack, tools, maps (SDB / XODR), data formats and simulation, working with several engineering teams to agree ownership and fixes.",
 "<b>Engineering tools:</b> Built Python tools (a GUI for JSON test parameters, an uploader) and data pipelines to dashboards. Built LLM agent skills (GitHub Copilot) that turn regulation text into scenarios, adopted project-wide."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Requirements decomposition &amp; traceability:</b> Feature owner at Jaguar Land Rover for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash (corner radar based). Wrote use cases and performance requirements and broke them down from system to component level in DOORS and MKS Integrity (ASPICE V-model), with test cases traced to each system state.",
 "<b>Interface definition:</b> Defined and reviewed the full input and output signal lists for each module around my features, mapped to the state machines, so every signal could be traced during integration and diagnosis.",
 "<b>System states &amp; functional design:</b> Designed system state diagrams and functional behaviour for driver assistance features, including Adaptive Cruise Control, Lane Keep Assist, Highway Assist and Lane Change Assist.",
 "<b>HiL, ViL &amp; vehicle testing:</b> Ran verification on HiL and ViL rigs and on the proving ground, diagnosing issues from CAN data with Vector CANoe and CANape. For example, I traced a late alert at boundary conditions to sensor field of view and agreed a fix with the radar supplier.",
 "<b>Simulation correlation &amp; safety:</b> Calibrated a Simulink / IPG CarMaker vehicle model against real vehicle data. Wrote ISO 26262 functional safety requirements for a lane change feature; trained in ISO 26262 and SOTIF."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental thermal modelling of an electric motor stator. Coursework included System Modelling and Simulation and Programming in C++."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: designed, built and controlled a 6-DOF Stewart motion platform, a small robotic system (state-space modelling and control in MATLAB, implemented on Arduino)."])
s += e

rows = [("Systems Engineering","Requirements decomposition, allocation and traceability, functional design, system state logic, interface definition (signal lists), verification strategy, V-model / ASPICE, DOORS, MKS Integrity"),
 ("Integration &amp; Test","SIL, HiL / ViL, proving ground and real-world testing, CI regression, log and telemetry analysis, KPI analysis"),
 ("Autonomy","L4 automated driving, planning behaviour validation, ADAS, corner radar features, OpenSCENARIO 2"),
 ("Software &amp; Tools","Python (tools, data pipelines), C++ (reading, MSc coursework), Git, monorepo and dev containers, MATLAB / Simulink, IPG CarMaker, CANoe / CANape, Jira / Confluence"),
 ("Safety &amp; Other","ISO 26262, SOTIF. British national, full UK driving licence. English (C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
