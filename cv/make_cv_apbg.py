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
    c.drawString(M, H-21*mm, "Forward Deployed Engineer & Technical Lead  |  Client Delivery, AI Workflows & Data Pipelines")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.9)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Bristol, London & Manchester)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   8+ yrs UK residence   |   Happy to travel on-site with clients   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_APBG.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - APBG Forward Deployed Engineer CV",
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
s.append(Paragraph("Client-embedded Forward Deployed / Applications Engineer and technical lead with 8 years decomposing complex use cases into delivered solutions across Jaguar Land Rover (via AVL) and the Volkswagen Group ADA partnership (at FiveAI / Bosch). Proven in end-to-end client delivery, high-EQ stakeholder advisory, leading a 5-person engineering team through a 'show and tell' teachback culture, embedding project-wide AI workflows (~10x scenario speedup), and building Python tools, user-facing GUIs and data pipelines into front-end dashboards across 1,000+ hours of data. Honest on gaps: I am not a classically trained software engineer (learned Python via AI-assisted coding), have not yet used Palantir (Foundry, Gotham, AIP), PySpark, SQL, TypeScript or React, and my 1-year team lead role was technical rather than formal line management. British &amp; Turkish dual national (British citizen, 8+ years continuous UK residence since 2017; flagged upfront for sole-national SC / DV rules), immediately available for London, Manchester or Bristol.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Client advisory, feature requests &amp; issue ownership:</b> Primary customer-facing engineer supporting Volkswagen Group partner teams on ADA, and Simulation EcoSystem co-founder. Resolved customer problems, scoped feature requests via one-pagers (and built requested features directly in project tooling), diagnosed API/map (SDB/XODR)/log faults, and led client demos.",
 "<b>Team leadership, tasking &amp; 'show and tell' teachbacks:</b> Led a 5-person engineering team for 1 year (technical lead): drove day-to-day tasking across scenario creation and evaluation, ran weekly progress and technical reviews, mentored peers via hands-on teachbacks and supported users across internal support channels.",
 "<b>Intensive AI workflows &amp; internal assets:</b> Heavy daily user of GitHub Copilot and AI agent workflows; built a project-wide Copilot CLI skill ingesting UN R79 / Euro NCAP rules, DSL documentation and modular blocks to build and validate OpenSCENARIO 2 scenarios (~10x faster, ~1 day to ~1 hr) and turned learnings into documentation and reusable templates.",
 "<b>End-to-end data pipelines &amp; monorepo delivery:</b> Performed traceability analysis and defined KPIs across 1,000+ hours of data (120+ scenarios); built Python apps with AI help—a JSON parameter GUI, local STAX uploader, and pipelines feeding front-end analysis dashboards—shipping via Jira, Git PRs and dt_flow CI in a Linux dev-container monorepo."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Boots-on-the-ground client ownership (Jaguar Land Rover):</b> Embedded on-site at JLR for 2 years as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Owned OEM and Tier 1 supplier links, decomposed use cases into state architectures, signal lists and DOORS / MKS Integrity traceability (ASPICE), and closed RTC / RQM defects.",
 "<b>Data-driven root-cause resolution &amp; rapid client iteration:</b> When RCTA passed in HiL testing (run by the HiL team) but fired late on the proving ground at 45°, designed a coarse-to-fine boundary test matrix, unified and time-synchronised camera, CAN bus and radar streams in Vector CANoe / CANape, isolated the FOV-edge delay, and iterated on site with the supplier across 3 calibration candidates to sign off the fix.",
 "<b>Cross-system modelling &amp; field hardware triage (DrivingCube &amp; LEVC):</b> Fitted GNSS ground-truth logging on AVL's DrivingCube ViL rig, captured airstrip and HORIBA MIRA data to calibrate a Simulink / IPG CarMaker model via PID sweeps, authored ISO 26262 requirements (and took part in a feature FMEA), and inspected ~20 returned generators at LEVC (multimeter checks and bench-powered fault-log downloads)."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): taught space tech (ages 9–16); simplified technical concepts for non-specialists and planned schedules.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): electric bus powertrain sizing in MATLAB / Simulink; production quality.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). System modelling (Simulink), C++, hybrid/EV systems, Ansys. Dissertation: stator thermal-network test design (MotorCAD, Portunus, Simulink; bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space, Arduino servo wiring and encoder signal plotting).", line))

s += section("Technical &amp; Consulting Skills")
s.append(KeepTogether([grid([
 ("Client &amp; team leadership", "Boots-on-the-ground client embedding (2 yrs JLR, 5 yrs VW Group ADA), technical lead for 5 engineers (1 yr), customer problems &amp; feature-request one-pagers, demos, teachbacks, supplier triage"),
 ("AI workflows &amp; data tools", "Intensive GitHub Copilot &amp; AI agent workflows (~10x speedup), AI output verification, Python (JSON GUI, STAX uploader, dashboard pipelines via AI help), KPIs on 1,000+ hrs data"),
 ("Engineering &amp; architecture", "Technical documentation, traceability analysis, monorepo workspace, Jira, Confluence, DOORS, MKS Integrity, RTC / RQM, Git PRs, dt_flow CI, Docker dev containers (user), Linux, Simulink"),
 ("Honest technical gaps", "Not yet used: Palantir (Foundry, Gotham, AIP Logic / Analysts / AIFDE), PySpark, SQL, TypeScript or React; learned Python via AI-assisted coding; 1-yr team lead was technical (non-HR)"),
 ("Clearance &amp; mobility", "British &amp; Turkish dual national (British citizen, 8+ yrs continuous UK residence since 2017; flagged upfront re: sole-national DV/SC rules), full UK licence, immediately available, flexible for London / Manchester / Bristol &amp; client sites")], 0.22)]))

doc.build(s)
