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
    c.drawString(M, H-23.5*mm, "Autonomy Systems Engineer  |  Safety, Verification & Integration")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Autonomy_Maritime.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Systems engineer with nearly 8 years on safety-related autonomous and driver assistance systems, from ADAS features at Jaguar Land Rover to an L4 automated driving stack at FiveAI / Bosch. I take operational needs and regulation and turn them into system requirements, state logic, degraded and fail-safe behaviour, and clear acceptance criteria, then prove them through simulation (SIL), HiL / ViL rigs and real-world testing. Used to being the technical link between customers, internal teams and suppliers. British national, full UK driving licence, willing to travel to trial sites and to undergo UK security vetting.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Verification strategy:</b> Design scenario-based verification for an L4 automated driving system, from functional to logical to concrete scenarios in OpenSCENARIO 2. Built 120+ parameterised scenarios generating thousands of test cases, covering UN R79 automatic lane change (ADA project) and Euro NCAP junction tests.",
 "<b>Acceptance benchmarks:</b> Defined pass/fail and KPI criteria, such as comfort limits for acceleration and deceleration, and analysed results across 1,000+ hours of real-world and simulation data.",
 "<b>SIL &amp; automated test suites:</b> Ran simulations locally in the project's dev container and at scale through the CI test pipeline (dtflow). Read Python and C++ code to trace stack behaviour and failures.",
 "<b>Cross-system integration:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Triaged defects across tools, maps (SDB / XODR), data formats and simulation, working with several engineering teams to find root causes.",
 "<b>Tooling &amp; data:</b> Built AI-assisted agent skills (GitHub Copilot) that turn regulation and test protocol text into scenarios, adopted project-wide. Built data pipelines that send results to dashboards for engineers and stakeholders."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>State logic &amp; degraded modes:</b> Feature owner at Jaguar Land Rover for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Defined system state diagrams, including available, active, degraded and fault states, and the transitions and driver handover between them.",
 "<b>Requirements &amp; traceability:</b> Wrote use cases and performance requirements and broke them down from system to component level in DOORS and MKS Integrity (ASPICE V-model). Wrote test cases for each state, traced to requirements.",
 "<b>HiL, ViL &amp; field testing:</b> Ran verification on HiL and ViL rigs and on the proving ground. Calibrated a Simulink / IPG CarMaker vehicle model against real vehicle data to compare real, dyno and simulation testing.",
 "<b>Supplier &amp; interface management:</b> Main technical link between the OEM, AVL and sensor suppliers. For example, when an alert triggered late at boundary conditions, I found the cause in CANoe / CANape logs and agreed a sensor field-of-view change with the supplier while keeping false alerts low.",
 "<b>Safety:</b> Wrote ISO 26262 functional safety requirements for a lane change feature. Trained in ISO 26262 and SOTIF (ISO 21448)."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental testing to find the variables of a thermal model of an electric motor stator (MATLAB, Simulink, MotorCAD)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: designed, built and controlled a 6-DOF Stewart motion platform, a small robotic system (state-space modelling in MATLAB, control on Arduino)."])
s += e

rows = [("Systems Engineering","Requirements decomposition, system state and mode logic, degraded / fail-safe behaviour, acceptance criteria, traceability, V-model / ASPICE, DOORS, MKS Integrity"),
 ("Verification","Scenario-based testing, SIL, HiL / ViL, proving ground and real-world testing, KPI analysis, regression in CI"),
 ("Safety","ISO 26262 (requirements written, trained), SOTIF / ISO 21448 (trained)"),
 ("Software &amp; Tools","Python, C++ (reading), OpenSCENARIO 2, Git, monorepo and dev containers, MATLAB / Simulink, IPG CarMaker, Vector CANoe / CANape, Jira / Confluence"),
 ("Other","British national, full UK driving licence, willing to travel and undergo security vetting. English (C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
