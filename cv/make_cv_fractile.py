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
    c.drawString(M, H-23.5*mm, "Verification & Test Engineer  |  Python, Simulation & Hardware-in-the-Loop")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Fractile.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
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

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Verification and test engineer with nearly 8 years on safety-related automotive systems. I write test plans from specifications, build the stimulus (parameterised simulation scenarios), define pass/fail checks, automate the runs in Python, and find the root cause of failures in logs and signal traces. I have done this on Hardware-in-the-Loop (HiL) rigs and vehicles at Jaguar Land Rover, and in simulation for an L4 automated driving stack at FiveAI / Bosch. <b>I have not worked in semiconductors yet and have not written RTL.</b> I want to move out of automotive into silicon, I learn new tools quickly, and I am ready to learn SystemVerilog and the chip verification flow.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Test plans from specifications:</b> Turned regulation text and test protocols (UN R79 automatic lane change, Euro NCAP junction tests) into test scenarios and acceptance criteria for an L4 automated driving stack.",
 "<b>Stimulus:</b> Built 120+ parameterised OpenSCENARIO 2 scenarios that generate thousands of test variations, from functional to logical to concrete scenarios.",
 "<b>Checks and analysis:</b> Defined pass/fail and KPI criteria, such as comfort limits for acceleration and deceleration across 1,000+ hours of test data. Checked thousands of simulation results against them and reported failures to the development teams.",
 "<b>Software environment:</b> Worked in the project monorepo with its dev container and CI test pipeline. Read Python and C++ to understand why tests failed, and raised pull requests for internal tools.",
 "<b>Tooling and data pipelines:</b> Built Python tools (a GUI for JSON test parameters, a local result uploader) and pipelines that send simulation results to front-end dashboards, using AI-assisted coding. Also built AI agent skills (GitHub Copilot) that help engineers write scenarios from regulation text and existing building blocks.",
 "<b>Cross-team triage:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Triaged problems across tools, maps and simulation with several engineering teams."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Requirements and traceability:</b> Based at Jaguar Land Rover for two years as feature owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Wrote use cases, system state diagrams and performance requirements, broke them down into low-level requirements, and wrote test cases for each system state traced back to requirements (DOORS, MKS Integrity, ASPICE V-model).",
 "<b>Hardware-in-the-Loop testing:</b> Ran verification on HiL and Vehicle-in-the-Loop (ViL) rigs and on the proving ground.",
 "<b>Debugging from signal traces:</b> Used Vector CANoe and CANape to read vehicle network (CAN) signals. For example, when an alert triggered late at boundary conditions, I found the cause in the logs and agreed a sensor field-of-view change with the supplier, while keeping false alerts low.",
 "<b>Safety:</b> Wrote ISO 26262 functional safety requirements for a lane change feature. Trained in ISO 26262 and SOTIF (ISO 21448). Tracked defects in Rational Team Concert (RTC/RQM)."])
s += job("Mechanical Engineer Internship", "Temsa Global", "Adana, Türkiye", "05/2014 – 08/2014", [
 "Calculated power and torque requirements for a new electric bus powertrain in MATLAB/Simulink, and supported quality work on the production line."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). <b>Dissertation:</b> lab testing to find the variables of a thermal model of an electric motor stator, with modelling in MotorCAD, Portunus and MATLAB/Simulink.",
 "<b>Coursework:</b> Systems for Hybrid and Electric Vehicle Applications; System Modelling and Simulation (MATLAB/Simulink); Fundamentals of Computing and Programming (C++)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "<b>Dissertation:</b> designed, built and controlled a 6-DOF Stewart motion platform: modelled in MATLAB and ran the control code on an Arduino Uno."])
s += e

s += [CondPageBreak(60*mm)] + section("How My Experience Maps to Chip Verification")
s.append(grid([
 ("Verification plan from spec", "Requirements to test cases with traceability (DOORS, ASPICE V-model), 2 years at JLR"),
 ("Stimulus creation", "Parameterised OpenSCENARIO 2 scenarios that generate thousands of variations"),
 ("Checkers", "Pass/fail and KPI criteria evaluated automatically over thousands of results"),
 ("Debugging from traces", "Time-series signal logs in Vector CANoe / CANape and simulation outputs"),
 ("Regression and CI", "Test pipelines, Git and dev containers in a monorepo shared with software teams"),
 ("Hardware in the loop", "Test rigs where real hardware runs against a simulated environment")], 0.27))
s.append(Spacer(1, 3))
s.append(Paragraph("<b>Not yet:</b> SystemVerilog / RTL, UVM, cocotb and EDA tools. I have no hands-on experience with these.", body))

s += section("Technical Skills")
s.append(KeepTogether([grid([
 ("Software", "Python (test automation, pandas, pytest, tooling), C++ (reading, university coursework), Git / GitHub, monorepo and dev containers, JSON, MATLAB / Simulink"),
 ("Verification &amp; Test", "Scenario-based testing, requirements-based test design, HiL / ViL, regression testing, KPI analysis, root cause analysis, OpenSCENARIO 2 DSL"),
 ("Hardware &amp; Networks", "Vector CANoe / CANape, CAN, CAN FD, Ethernet, Arduino. I also build and fix my own desktop computers."),
 ("Process &amp; Safety", "ASPICE V-model, ISO 26262 and SOTIF (trained), DOORS, MKS Integrity, Jira, Confluence"),
 ("Languages", "English (C2), Turkish (Native)")], 0.22)]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
