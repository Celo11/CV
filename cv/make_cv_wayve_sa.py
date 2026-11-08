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
    c.drawString(M, H-23.5*mm, "Systems & Integration Engineer  |  ADAS / Automated Driving  |  OEM & Tier 1 Interface")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Wayve_Solution_Architect.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Systems engineer with nearly 8 years at the boundary between automated driving software and vehicle programmes. For two years I worked on-site at Jaguar Land Rover as the feature owner between the OEM, AVL and sensor suppliers, turning customer needs into requirements, system states and verifiable tests. Since 2021 I have worked on an L4 automated driving stack at FiveAI / Bosch, building scenario-based validation tied to regulation and supporting several engineering teams with integration issues. I am good at turning unclear discussions into clear requirements, owners and open decisions, and at making sure every requirement can be tested.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Validation-ready requirements:</b> Turned regulation (UN R79 automatic lane change on the ADA project) and Euro NCAP protocols into measurable test conditions and 120+ parameterised OpenSCENARIO 2 scenarios, generating thousands of test cases.",
 "<b>Acceptance criteria:</b> Defined pass/fail and KPI criteria, such as comfort limits on acceleration and deceleration, and analysed results across 1,000+ hours of real-world and simulation data.",
 "<b>Integration across teams:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Triaged integration issues across the stack, tools, maps (SDB / XODR), data formats and simulation, and agreed who owned each fix with the engineering teams involved.",
 "<b>Working in the stack:</b> Worked in the project monorepo and its dev container, ran simulations locally and through the CI test pipeline (dtflow), and read Python and C++ code to trace stack behaviour.",
 "<b>Generative AI in engineering:</b> Built LLM agent skills with GitHub Copilot and Copilot CLI that turn regulation text into scenarios. They were adopted project-wide and increased scenario output by an order of magnitude."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>OEM-embedded feature owner:</b> Based at Jaguar Land Rover as owner of Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Main technical link between the OEM, AVL and the sensor supplier, aligning requirements, risks and fixes for the corner radar based features.",
 "<b>Interface definition &amp; review:</b> Defined and reviewed the full input and output signal lists for each module around my features, mapping them to the state machines so every signal could be traced during diagnosis, in the same way as a Simulink model.",
 "<b>Requirements &amp; system states:</b> Wrote use cases, system state diagrams and performance requirements, and broke them down from system to component level in DOORS and MKS Integrity (ASPICE V-model), with test cases traced to each state.",
 "<b>Vehicle network &amp; sensor debugging:</b> Analysed CAN data with Vector CANoe and CANape on HiL and ViL rigs and in vehicles. Worked with corner radar object detections, where missed detections become more likely towards the edges of range and field of view. For example, when an alert triggered late at boundary conditions, I found the cause in the logs and agreed a sensor field-of-view change with the supplier while keeping false alerts low.",
 "<b>Feature design:</b> Wrote use cases and requirements for Adaptive Cruise Control, Lane Keep Assist, Highway Assist and Lane Change Assist.",
 "<b>Simulation correlation:</b> Calibrated a Simulink / IPG CarMaker vehicle model against real vehicle data to compare vehicle, dyno with sensor emulation, and simulation testing.",
 "<b>Safety:</b> Wrote ISO 26262 functional safety requirements for a lane change feature. Trained in ISO 26262 and SOTIF (ISO 21448)."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental thermal modelling of an electric motor stator (MATLAB, Simulink, MotorCAD)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: designed, built and controlled a 6-DOF Stewart motion platform (state-space modelling in MATLAB, control on Arduino)."])
s += e

rows = [("Systems &amp; Integration","Requirements and decomposition, system states, ownership and dependency tracking, validation-ready requirements, traceability, V-model / ASPICE, DOORS, MKS Integrity"),
 ("Vehicle &amp; Network","Signal lists and interface review, corner radar (BSM / RCTA), CAN (analysis); vehicle platform also used FlexRay and Automotive Ethernet, Vector CANoe / CANape, HiL / ViL rigs, in-vehicle and proving ground testing, sensor supplier integration"),
 ("Safety &amp; Regulation","ISO 26262 (requirements written, trained), SOTIF / ISO 21448, UN R79, Euro NCAP"),
 ("Software &amp; AI","Python, C++ (reading), OpenSCENARIO 2, Git, monorepo and dev containers, CI pipelines, MATLAB / Simulink, IPG CarMaker, GitHub Copilot agent skills"),
 ("Languages","English (C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
