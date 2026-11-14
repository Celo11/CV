from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable)

NAVY = colors.HexColor("#14213D"); ACC = colors.HexColor("#1F7A8C")
GREY = colors.HexColor("#555555"); LIGHT = colors.HexColor("#E8F1F4")
W, H = A4; M = 14*mm; HB = 34*mm

def S(n, **k): return ParagraphStyle(n, fontName=k.pop("f", "Helvetica"), **k)
body = S("b", fontSize=7.9, leading=10.0, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.55)
line = S("line", parent=body, spaceAfter=0.8)
sec = S("sec", f="Helvetica-Bold", fontSize=9.7, leading=11.1, textColor=NAVY, spaceBefore=2.3)
role = S("r", f="Helvetica-Bold", fontSize=9.1, leading=10.6, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.4, leading=10.1, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=7.9, leading=10.1, textColor=GREY, alignment=2)
loc = S("l", fontSize=7.9, leading=10.1, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 9.8); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Field Application Engineer  |  OEM Design-In, Customer Training & Hands-On Troubleshooting")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.9)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Hook, 3+ days/wk)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Ready for EMEA & international travel   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_Neutrik.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Neutrik Field Application Engineer CV",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.6, spaceAfter=1.4)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0.4)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,0.7), items[0]]), *items[1:], Spacer(1,1.3)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),1.0),("BOTTOMPADDING",(0,0),(-1,-1),1.0),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Mechanical and automotive engineer (BSc Mechanical; MSc Sustainable Automotive Engineering, WMG Warwick) with 8 years in customer-facing Application and Systems Engineering—serving as first point of contact for technical troubleshooting, leading OEM design-in integrations (2 years on-site at Jaguar Land Rover with AVL), teaching customer engineers (5 years on the VW Group ADA partnership at FiveAI / Bosch), and performing hands-on connector-pin, harness and electronics checks (LEVC returned generators, car audio wiring, PCB motor soldering, 6-DOF servo wiring). Honest on gaps: my OEM design-in and wiring experience is in automotive and mechatronics rather than commercial pro audio/video/broadcast connectors or optical fibre markets, and I have used engineering tracking tools (DOORS, RTC/RQM, Jira, Confluence) rather than sales CRM systems. Dual British/Turkish citizen, fluent English (C2) + native Turkish + basic Italian, ready for Hook (3+ days/wk) and EMEA/international travel.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>First point of contact &amp; customer troubleshooting:</b> Primary Application Engineer supporting Volkswagen Group OEM partner engineers on the ADA programme, and founding member of the Simulation EcoSystem (SimEco) solutions team. Answered technical questions, diagnosed integration issues from API, map and simulation logs, and coordinated fixes with product teams.",
 "<b>Customer &amp; internal training:</b> Showed and taught external Volkswagen Group partner engineers across the cluster how to use the FiveAI simulation toolchain. Led a 5-person engineering team for 1 year (technical lead), teaching tools and evaluation logic, splitting work packages and holding weekly progress reviews.",
 "<b>Custom solutions &amp; analytical insights:</b> Built custom Python tools (JSON parameter GUI, STAX uploader, dashboard data pipelines) and a project-wide GitHub Copilot / Copilot CLI helper (~10x scenario speedup). Analysed 1,000+ hours of test data against UN R79 and Euro NCAP KPIs, feeding measured insights back to developers."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>OEM design-in projects &amp; feasibility (Jaguar Land Rover):</b> Embedded on-site at JLR for 2 years as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Led the technical side of OEM feature integration across customer, internal and Tier 1 supplier teams—turning customer needs into use cases, state diagrams, module signal lists and specs in DOORS / MKS Integrity (ASPICE V-model).",
 "<b>Connector-pin diagnostics &amp; hardware troubleshooting (LEVC &amp; JLR):</b> At the LEVC (London Taxi) factory, inspected ~20 returned faulty range-extender generators per procedure: ran multimeter checks at specified connector pins (phase resistance, continuity) and bench-powered control units to download fault logs for supplier investigation. In vehicle tests, traced non-activating modules via DTCs, fuse checks and a 12 V bench supply.",
 "<b>On-site deployment support &amp; boundary troubleshooting:</b> When RCTA passed in HiL testing (run by the HiL team) but fired late on the proving ground at 45°, designed a coarse-to-fine test matrix, synchronised camera, CAN bus and radar streams in Vector CANoe / CANape, traced the delay to the radar FOV edge, and ran boundary tests on site with the supplier to verify the fix.",
 "<b>Test instrumentation &amp; documentation:</b> Fitted external GNSS ground-truth logging on AVL's DrivingCube ViL rig, captured airstrip and HORIBA MIRA data to calibrate a Simulink / IPG CarMaker model, authored ISO 26262 safety requirements (and took part in an FMEA), and tracked defects in RTC / RQM."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): taught space tech simply (ages 9–16); planned schedules.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): electric bus powertrain sizing in MATLAB / Simulink; production quality.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Hybrid/EV electrical &amp; powertrain systems, Simulink, C++, Ansys. Dissertation: stator thermal test design with type-K thermocouples (MotorCAD, Portunus, Simulink; bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino); wired 6 servo actuators and encoder cables, commanded angles, plotted signals.", line))

s += section("Technical &amp; Application Engineering Skills")
s.append(KeepTogether([grid([
 ("Application &amp; OEM support", "First-line technical customer support, OEM design-in integration (2 yrs JLR, 5 yrs VW Group), customer &amp; team teaching, feasibility &amp; root-cause troubleshooting, technical lead for 5 engineers (1 yr)"),
 ("Connectors, wiring &amp; bench", "Connector-pin multimeter checks (resistance, continuity, fuse probing – LEVC &amp; JLR), 12 V / low-voltage bench supply testing, car audio wiring, PCB motor cable soldering, 6-DOF servo &amp; encoder wiring, PC builds"),
 ("Documentation &amp; tools", "Technical specs, interface signal lists, state diagrams &amp; test plans (DOORS, MKS Integrity, RTC / RQM, Jira, Confluence), Vector CANoe / CANape (CAN; platforms also used FlexRay &amp; Ethernet), Python, Simulink"),
 ("Honest gaps", "Automotive / mechatronics background rather than commercial pro audio/video/broadcast connectors or optical fibre; engineering lifecycle tools rather than sales CRM systems; no commercial user manuals authored yet"),
 ("Languages &amp; travel", "English (C2 fluent), Turkish (native), Italian (basic A1–A2; no German/Spanish/French). Dual British/Turkish citizen, full UK licence, ready for EMEA &amp; international travel (incl. India) and Hook (3+ days/wk), available now")], 0.22)]))

doc.build(s)
