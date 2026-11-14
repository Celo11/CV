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
    c.drawString(M, H-21*mm, "Solutions Engineer  |  Client Engineering Partnerships, Python Tooling & Data Analytics")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.9)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to London)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Immediately available (no notice period)")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_TikTok.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - TikTok Solutions Engineer CV",
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
s.append(Paragraph("Customer-facing Solutions and Applications Engineer with 8 years managing external client engineering partnerships, driving joint roadmaps and building end-to-end technical solutions across the Volkswagen Group ADA programme (at FiveAI / Bosch) and Jaguar Land Rover (via AVL Powertrain UK). Proven in shipping internal Python applications (JSON parameter GUI, STAX uploader, dashboard data pipelines) and a project-wide AI workflow (~10x speedup) via Git pull requests and CI pipelines, diagnosing API and simulation backend logs, analysing 1,000+ hours of large-volume data to influence core product roadmaps, and explaining complex ideas to technical and non-technical audiences. Honest on gaps: my degrees are in Sustainable Automotive Engineering (with C++ coursework) and Mechanical Engineering rather than CS; I build Python tools with AI assistance and read C++ rather than building Go/Java web backends from scratch; and I am new to AdTech / ad sales. British citizen, open to London, immediately available.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Client engineering relationships &amp; joint roadmaps:</b> Managed technical relationships with external client engineering teams across the Volkswagen Group cluster on the ADA programme, and co-founded the Simulation EcoSystem (SimEco) solutions team. Onboarded partner engineers, aligned operational goals with R&amp;D roadmaps and prioritised cross-functional fixes.",
 "<b>Shipping custom end-to-end solutions &amp; Python tools:</b> Built and shipped internal Python products—a user-facing JSON parameter configuration GUI, local STAX uploader, and data pipelines routing metrics to front-end dashboards—plus 120+ modular OpenSCENARIO 2 scenarios, contributing directly via Git PRs, Linux dev containers and dt_flow CI pipelines.",
 "<b>API / backend log diagnosis &amp; product roadmap influence:</b> Diagnosed integration failures across API, map (SDB/XODR) and simulation backend error logs. Analysed 1,000+ hours of large-volume test data against quantitative KPIs (UN R79, Euro NCAP); surfaced a curvature performance drop that influenced the engineering roadmap and led to a steering controller fix.",
 "<b>AI workflow innovation &amp; team leadership:</b> Built and shipped a project-wide GitHub Copilot / Copilot CLI agent workflow composing regulation rules and modular blocks into validated scenarios (~1 day down to ~1 hour, ~10x). Led a 5-person engineering team for 1 year, coordinating parallel delivery, weekly reviews and peer teachbacks."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>On-site client ownership &amp; cross-functional collaboration (JLR):</b> Embedded at Jaguar Land Rover for 2 years as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Acted as technical link between OEM client teams, internal engineering and Tier 1 suppliers, converting client goals into state architectures, signal lists and requirements in DOORS / MKS Integrity (ASPICE V-model).",
 "<b>Data-driven root-cause resolution &amp; custom fix delivery:</b> When RCTA passed in HiL testing (run by the HiL team) but fired late on the proving ground at 45°, designed a coarse-to-fine test matrix, time-synchronised camera, CAN bus and radar streams in Vector CANoe / CANape, isolated the FOV-edge delay, and worked on site with the supplier to test and ship a calibrated fix.",
 "<b>System modelling &amp; hardware diagnostics (DrivingCube &amp; LEVC):</b> Fitted GNSS ground-truth logging on AVL's DrivingCube ViL rig, captured airstrip and HORIBA MIRA data to calibrate a MATLAB / Simulink and IPG CarMaker model via PID sweeps, authored ISO 26262 requirements (and took part in an FMEA), and checked ~20 returned generators at LEVC (multimeter &amp; log downloads)."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): explained space tech clearly to non-technical groups (ages 9–16) and planned schedules.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): electric bus powertrain sizing in MATLAB / Simulink; production quality.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Coursework: Fundamentals of Computing &amp; Programming (C++), System Modelling (MATLAB / Simulink), hybrid/EV systems, Ansys. Dissertation: stator thermal-network test design (MotorCAD, Portunus, Simulink; bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space, Arduino servo wiring &amp; signal plotting).", line))

s += section("Technical &amp; Solutions Skills")
s.append(KeepTogether([grid([
 ("Solutions &amp; clients", "External client engineering partnerships (5 yrs VW Group ADA, 2 yrs on-site JLR), joint roadmap alignment, cross-functional stakeholders, technical lead for 5 engineers (1 yr), non-technical communication (Space Camp)"),
 ("Programming &amp; shipping", "Python (JSON parameter GUI, STAX uploader, dashboard data pipelines built with AI help), C++ (MSc coursework; reading C++), OpenSCENARIO 2 DSL, MATLAB / Simulink, Git / GitHub PRs, Linux dev containers, dt_flow CI"),
 ("Data, APIs &amp; AI tools", "Large-volume data &amp; KPI analytics (1,000+ hrs test data), API / map (SDB/XODR) / simulation backend log diagnosis, GitHub Copilot &amp; Copilot CLI agent skills (~10x workflow speedup), Vector CANoe / CANape"),
 ("Architecture &amp; delivery", "Systems architecture, use cases, state diagrams, signal lists, DOORS, MKS Integrity, RTC / RQM, Jira, Confluence, ASPICE V-model, ISO 26262, FMEA, SOTIF"),
 ("Honest gaps &amp; details", "Automotive / Mechanical Eng degrees (with C++ &amp; modelling) rather than CS; builds Python tools with AI help rather than backend Go/Java/SQL services from scratch; new to AdTech / ad sales. British citizen, open to London, available now")], 0.22)]))

doc.build(s)
