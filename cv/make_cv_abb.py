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
    c.drawString(M, H-23.5*mm, "Systems & Robotics Engineer  |  Requirements, Verification & Integration")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_ABB.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Mechanical engineer with nearly 8 years in systems engineering and verification, spanning driver assistance features and automated driving systems. Experienced in turning customer and technical requirements into verifiable designs, defining system behaviour through state diagrams and acceptance criteria, and validating solutions through testing across simulation, hardware-in-the-loop and real vehicles. Built and programmed a 6-DOF robotic platform at university. Comfortable collaborating with multidisciplinary teams across mechanical, electrical and software disciplines. Honest about gaps: no PLC programming or SCADA systems experience yet, but strong in requirements engineering, system architecture evaluation, and structured testing methodology.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>System design &amp; requirements:</b> Design test scenarios for an L4 automated driving stack from functional to logical to concrete specifications. Built 120+ parameterised scenarios defining test acceptance criteria, such as comfort limits on acceleration and deceleration across 1,000+ hours of test data.",
 "<b>Requirements &amp; architecture:</b> Contributed to system-level design decisions on simulation strategy, scenario coverage and integration points across multiple tools and teams. Evaluated technical feasibility of new requirements and proposed solutions.",
 "<b>Verification &amp; integration:</b> Ran verification in simulation and CI pipelines, troubleshooting integration issues across the system stack. Triaged problems across tools, maps and simulation with several engineering teams.",
 "<b>Commissioning &amp; handover:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain, then helped diagnose problems across the partners' shared toolchains as a founding member of the solutions team. Built internal tools and data pipelines that send simulation results to dashboards for analysis."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Requirements &amp; design review:</b> Feature owner for three corner radar systems. Wrote use cases and system state diagrams, broke high-level requirements down to component level, and reviewed designs in DOORS and MKS Integrity (ASPICE V-model).",
 "<b>Design evaluation:</b> Assessed technical feasibility of new features and evaluated software architectures using signal lists, state machines and network communication analysis. Traced requirements through to test cases.",
 "<b>Verification &amp; testing:</b> Ran hardware-in-the-loop and vehicle-in-the-loop testing on ViL rigs and in vehicles on the proving ground. Defined test cases and acceptance criteria per system state.",
 "<b>Commissioning &amp; troubleshooting:</b> Used Vector CANoe and CANape to diagnose issues from vehicle network data. Example: when an alert triggered late at boundary conditions, I re-ran tests, found the issue in the logs, and agreed a sensor field-of-view change with the supplier.",
 "<b>Field diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>Safety &amp; requirements:</b> Wrote ISO 26262 functional safety requirements. Trained in ISO 26262 and SOTIF (ISO 21448)."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental testing and modelling of an electric motor stator (MATLAB, Simulink, MotorCAD)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "<b>Robotics project:</b> Designed, built and programmed a 6-DOF Stewart motion platform using SolidWorks, MATLAB and Arduino. Implemented state-space control logic."])
s += e

rows = [("Systems Engineering","Requirements analysis, use cases, system state diagrams, acceptance criteria, traceability, ASPICE V-model, DOORS, MKS Integrity, design review"),
 ("Verification &amp; Testing","Scenario-based testing, SIL / HiL / ViL testing, proving ground testing, simulation, KPI analysis, root cause analysis"),
 ("Safety &amp; Standards","ISO 26262 (requirements written, trained), SOTIF / ISO 21448 (trained)"),
 ("Tools &amp; Software","MATLAB / Simulink, Vector CANoe / CANape, Git, Python (reading / scripting), C++ (reading), OpenSCENARIO 2, Jira"),
 ("Technical Background","Mechanical engineer; hands-on with rig and vehicle testing. Robotics and motion control (Stewart platform). Comfortable reading across system architectures."),
 ("Languages","English (C2), Turkish (Native), Italian (A1–A2)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills & Background") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
