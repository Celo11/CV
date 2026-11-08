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
    c.drawString(M, H-23.5*mm, "Systems & Test Engineer  |  Diagnostics, Field Testing & Customer Support")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_EngineeredArts.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s += section("Profile")
s.append(Paragraph("Mechanical engineer with nearly 8 years in automotive testing and diagnostics. Most of that time I have worked close to the customer: on-site at Jaguar Land Rover and at the LEVC (London Taxi) factory for AVL, and at FiveAI / Bosch training and supporting Volkswagen Group engineers on our simulation tools. My job has usually been to work out why something isn't behaving as it should, find the real cause and get it fixed with the right people. Customers and colleagues find me easy to approach, and I stay calm and friendly when things go wrong. I enjoy hands-on work. I built a 6-DOF motion platform for my degree, I repair my own cars and I build my own PCs. British passport holder with a full UK driving licence, happy to travel.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, I trained engineers across the partner organisations to use our toolchain. I ran demos, answered their questions and helped them get their own tests running.",
 "This customer work grew into a solutions team, and I was a founding member. We diagnosed problems across the shared toolchains and add-on tools of all the partners. I reproduced each issue, worked out whether it was in the test, the map or the software, and got the right team to fix it.",
 "Led a team of five engineers for a year. I taught them our tools and how to check results, and split the work so tests were written and reviewed in parallel.",
 "Wrote 120+ parameterised OpenSCENARIO 2 test scenarios (Euro NCAP, UN R79) and set pass/fail criteria, checked against more than 1,000 hours of driving data.",
 "Write Python scripts and small tools, such as a GUI for test parameters, an uploader and pipelines that feed results into dashboards. Showed colleagues how to use AI coding tools and, more importantly, how to check what they produce."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "Based at Jaguar Land Rover as owner of three radar-based driver assistance features: Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. I was the main contact between AVL, JLR and the radar supplier.",
 "Tested the features on HiL and ViL rigs, in vehicles and on the proving ground, reading vehicle network data with Vector CANoe and CANape.",
 "One example: an alert was firing late at the edge of its coverage. I re-ran the tests, found the cause in the logs (the radar's field of view) and agreed a fix with the supplier that didn't add false alerts.",
 "At the LEVC (London Taxi) factory, inspected returned faulty e-machines. Did multimeter checks, downloaded data from proprietary loggers and sent it to the developers and suppliers for root cause analysis.",
 "Wrote requirements, state diagrams and test cases in DOORS and MKS Integrity, and tracked defects in RTC / RQM."])
s += job("Mechanical Engineering Intern", "TEMSA Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Worked on a new electric bus powertrain, calculating power and torque requirements in MATLAB / Simulink, and on improvements to the production line."])
s += job("Part-time Teacher and Programme Planner", "Space Camp Turkey", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught space technology, physics, chemistry and biology to visiting groups aged 9 to 16, explaining technical ideas to people with no technical background.",
 "Planned daily programmes for student groups and teachers."])

e = [CondPageBreak(50*mm)] + section("Education")
e += edu("MSc Sustainable Automotive Engineering", "10/2017 – 09/2018", "WMG, University of Warwick, Coventry, UK", [
 "2:1 (Merit). Dissertation: lab testing to find the variables of a thermal model for an electric motor stator (MotorCAD, MATLAB / Simulink)."])
e += edu("BSc Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: designed, built and programmed a 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino)."])
s += e

rows = [("Diagnostics","Root cause analysis, multimeter, data loggers, vehicle network logs (Vector CANoe / CANape), HiL / ViL rigs"),
 ("Hands-on","Mechanical assembly (Stewart platform build), car repairs, PC builds"),
 ("Software","Python scripting, Linux command line, SSH (GPU cluster), Git, MATLAB / Simulink, Jira, Confluence"),
 ("Networks","Vehicle networks (CAN, FlexRay, Automotive Ethernet)"),
 ("Travel","British passport, full UK driving licence, happy to travel"),
 ("Languages","English (C2), Turkish (native), Italian (basic)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.18, cw*0.82])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
