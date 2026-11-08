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
    c.drawString(M, H-23.5*mm, "Test & Verification Engineer  |  Systems Integration")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Leidos.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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
s.append(Paragraph("Test and verification engineer with nearly 8 years in automotive, working on safety-related driver assistance and automated driving systems. Experienced across the full test lifecycle: writing requirements and test specifications, building test scenarios and test data, running integration, system, and regression tests on simulation, HiL/ViL rigs and real vehicles, and tracing results back to requirements. Comfortable in both V-model (waterfall) and agile teams. I write Python to automate tests and build small test tools, and I pick up new tools quickly. British national, UK resident for 8+ years, and willing to undergo SC clearance.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Test design:</b> Write test scenarios in OpenSCENARIO 2 for an L4 automated driving stack, from functional to logical to concrete. Built 120+ parameterised scenarios that generate thousands of test cases, including Euro NCAP junction tests and UN R79 lane change compliance tests.",
 "<b>Test execution &amp; regression:</b> Run simulation test suites through the test pipeline (dtflow), check results against pass/fail and KPI criteria, and raise defects with the development teams.",
 "<b>Performance testing:</b> Evaluated performance KPIs, such as comfort limits for acceleration and deceleration, across 1,000+ hours of test data, and reported violations to the development teams.",
 "<b>Test automation &amp; tools:</b> Write Python scripts to validate the stack on both simulation and real-world drive data. Built internal test tools, such as a GUI for JSON test parameters and a local uploader, using AI-assisted coding, and raised pull requests to the main code base.",
 "<b>Test data &amp; reporting:</b> Built data pipelines that move simulation results into front-end dashboards so stakeholders can see test status and performance.",
 "<b>Test standards:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Created reusable Euro NCAP test templates and helped triage tool and map integration issues (SDB/XODR)."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Requirements &amp; traceability:</b> Based at Jaguar Land Rover. Broke high-level requirements down into low-level ones in DOORS and MKS Integrity within an ASPICE V-model process, and wrote test cases for each system state, traced back to the requirements.",
 "<b>Integration &amp; system test:</b> Ran verification and validation of ADAS features (Rear Cross Traffic Alert, Blind Spot Monitor, Rear Pre-Crash) on Hardware-in-the-Loop (HiL) and Vehicle-in-the-Loop (ViL) rigs and on the proving ground.",
 "<b>Fault-finding:</b> Used Vector CANoe and CANape to read vehicle network data and find the root cause of failures.",
 "<b>Field diagnostics:</b> At the LEVC (London Taxi) factory, inspected returned faulty e-machines: multimeter checks, downloading data from proprietary loggers and sending it to developers and suppliers for root cause analysis.",
 "<b>Defect management:</b> Logged and tracked defects in Rational Team Concert (RTC/RQM). For example, when an alert triggered late at boundary conditions, I re-ran the tests, analysed the logs, and worked with the supplier to change the sensor field of view while keeping false alerts low.",
 "<b>Safety-related work:</b> Wrote ISO 26262 functional safety requirements for a lane change feature. Trained in ISO 26262 and SOTIF (ISO 21448)."])
s += job("Mechanical Engineer Intern", "Temsa Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Calculated power and torque needs for a new electric bus powertrain in MATLAB/Simulink, and supported quality work on the production line."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental testing to find the variables of a thermal model of an electric motor stator (MATLAB, Simulink, MotorCAD)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: designed, built and tested a 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino)."])
s += e

s += section("Skills")
rows = [("Testing","Test specifications, test scripts and scenarios, integration / system / regression testing, performance KPI testing, verification &amp; validation, acceptance criteria, HiL / ViL / SIL"),
 ("Requirements","DOORS, MKS Integrity, requirements traceability, ASPICE V-model, ISO 26262 and SOTIF (trained)"),
 ("Automation &amp; Tools","Python, OpenSCENARIO 2, test pipelines, Git / GitHub, Vector CANoe / CANape, MATLAB / Simulink"),
 ("Delivery","Agile (Jira, Confluence), V-model / waterfall, defect management (RTC / RQM)"),
 ("Other","English (C2), Turkish (Native); British national, UK resident 8+ years, willing to undergo SC clearance")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether([sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
