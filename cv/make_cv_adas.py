from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable)

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
    c.drawString(M, H-23.5*mm, "ADAS Systems Engineer  |  Product Feature Owner")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_ADAS.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
                      author="Muhammet Celal Gokalp", leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([
    PageTemplate("first", [Frame(M, 12*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header),
    PageTemplate("later", [Frame(M, 12*mm, cw, H-9*mm-18*mm, 0,0,0,0)], onPage=later)])
from reportlab.platypus import NextPageTemplate

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.2, color=ACC, spaceBefore=1, spaceAfter=4)]

def job(r, o, where, dates, bullets):
    t = Table([[Paragraph(r, role), Paragraph(dates, meta)],
               [Paragraph(o, org), Paragraph(where, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([t, Spacer(1,2), items[0]]), *items[1:], Spacer(1,5)]

def job(r, o, where, dates, bullets):
    t = Table([[Paragraph(r, role), Paragraph(dates, meta)],
               [Paragraph(o, org), Paragraph(where, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([t, Spacer(1,2), items[0]]), *items[1:], Spacer(1,5)]

s = []
s += section("Professional Summary")
s.append(Paragraph("Product Feature Owner and ADAS Systems Engineer with extensive experience managing the end-to-end delivery of active safety features from concept to production. Proven track record embedded at major automotive OEMs, acting as the central liaison between engineering teams, suppliers, and product stakeholders to align technical capabilities with customer requirements. Deeply experienced in vehicle-level validation, proving ground testing, and authoring system requirements (including UN Reg 79 compliance). Experienced in developing and evaluating simulation scenarios for ADAS features, including Automatic Lane Change and Euro NCAP junction handling. Adept at building efficient AI workflows and custom tooling to scale simulation ecosystems and accelerate test automation.", body))
s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>ADAS Scenario Development &amp; Evaluation:</b> Developed and evaluated test scenarios for ADAS features, including Automatic Lane Change on the ADA project, where the rules and scenarios were built directly for compliance with UN Regulation No. 79. Also created Euro NCAP junction-handling scenarios, using OpenSCENARIO 2 (OSC2) and evaluating results against strict validation and KPI criteria.",
 "<b>Customer training &amp; solutions:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member, diagnosing problems across the partners' shared toolchains, maps (SDB/XODR) and add-on tools.",
 "<b>Efficient AI Workflows &amp; Tooling:</b> Leveraged AI workflows to streamline QA and test tooling, rapidly prototyping custom internal utilities (e.g., local STAX uploader, JSON parameter GUI) to improve test efficiency and support the core engineering team.",
 "<b>Data-Driven Product Alignment:</b> Evaluated thousands of high-level simulation results against strict validation and KPI criteria, engineering pipelines to route complex data to frontend analysis pages and translating system behaviours into actionable design improvements.",
 "<b>Automotive Standards Standardization:</b> Engineered modular EuroNCAP Simax test scenario templates (including crossing-path junction scenarios) for Core projects, bridging prior real-world ADAS testing expertise with virtual simulation pipelines to scale development capacity."])
s += job("ADAS Feature Owner / Systems Engineer", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Feature Ownership &amp; Delivery:</b> Embedded directly at Jaguar Land Rover, taking end-to-end responsibility for specific ADAS active safety features including Rear Cross Traffic Alert, Blind Spot Monitor, and Rear Pre-Crash.",
 "<b>Homologation &amp; Requirements:</b> Authored use cases, system state diagrams, and key performance requirements using DOORS and MKS Integrity. Contributed directly to the vehicle homologation process for the Rear Cross Traffic Alert feature, ensuring system performance metrics aligned with UN Regulation No. 79 standards.",
 "<b>Hands-on Testing &amp; Validation:</b> Actively engaged in feature evaluation by interfacing with the vehicle's CAN network through central mirror cameras using Vector tools (CANoe and CANape), executing rigorous proving ground tests, and interpreting complex data logs.",
 "<b>Field diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>Risk Mitigation &amp; Defect Resolution:</b> Led cross-functional defect resolution when boundary-condition testing revealed delayed trigger alerts; collaborated with subsystem engineers and suppliers to adjust sensor Field of View (FOV) parameters, carefully balancing detection improvements against false-positive risks. Managed defect tracking through Rational Team Concert (RTC/RQM)."])
s += job("Mechanical Engineer Internship", "Temsa Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Supported continuous improvement initiatives, defect tracking, and quality optimization directly on the manufacturing production line.",
 "Validated power and torque hardware requirements utilizing MATLAB/Simulink for electric bus powertrains."])

def edu(t, d, u, bl):
    tb = Table([[Paragraph(t, role), Paragraph(d, meta)],[Paragraph(u, org), ""]], colWidths=[cw*0.68, cw*0.32])
    tb.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    return [KeepTogether([tb, Spacer(1,2)] + [Paragraph(b, bul, bulletText="•") for b in bl]), Spacer(1,5)]
from reportlab.platypus import CondPageBreak
e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit)",
 "<b>Dissertation:</b> Experimental determination of variables in a thermal model of a wound stator, utilizing MATLAB, Simulink, and MotorCAD for complex system modelling."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "<b>Dissertation:</b> Manufactured and modelled a physical prototype 6-Degree of Freedom Stewart Simulation System. Designed hardware via SolidWorks, modelled movements in MATLAB, and built control algorithms in Arduino Uno."])
s += e
s += section("Technical Skills")
rows = [("ADAS &amp; Standards","Feature Concept to Production, V-Model Validation, UN Reg 79, Homologation, EuroNCAP Standards, Proving Ground Testing"),
 ("Networks &amp; Engineering Tools","Vector CANoe, CANape, standard automotive CAN, CAN FD, Ethernet, MATLAB, Simulink, CarMaker, Hardware-in-the-Loop (HiL)"),
 ("Management &amp; Requirements","RMDV2 DOORS, MKS Integrity, Rational Team Concert (RTC/RQM), Atlassian Stack (Jira, Confluence)"),
 ("Software &amp; Workflows","Python, OpenSCENARIO (OSC2) DSL, Efficient AI Workflows for Test Automation"),
 ("Languages","English (Fluent/C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.25, cw*0.75])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether([sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
