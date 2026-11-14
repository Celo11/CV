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
body = S("b", fontSize=7.55, leading=9.45, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.42)
line = S("line", parent=body, spaceAfter=0.6)
sec = S("sec", f="Helvetica-Bold", fontSize=9.35, leading=10.6, textColor=NAVY, spaceBefore=1.8)
role = S("r", f="Helvetica-Bold", fontSize=8.8, leading=10.2, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.1, leading=9.7, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=7.55, leading=9.7, textColor=GREY, alignment=2)
loc = S("l", fontSize=7.55, leading=9.7, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 9.5); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Principal Implementation & Solutions Engineer  |  Agentic AI Workflows, System Architecture & Client Delivery")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.7)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Remote & Fitzrovia, London)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   8 yrs Client Implementation, Architecture & QA   |   Full UK driving licence   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_Xiatech.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Xiatech Principal Implementation Engineer CV",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.4, spaceAfter=1.1)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0.35)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,0.45), items[0]]), *items[1:], Spacer(1,0.9)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),0.85),("BOTTOMPADDING",(0,0),(-1,-1),0.85),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Client-facing Principal / Lead Implementation &amp; Applications Engineer with 8 years architecting and delivering end-to-end technical solutions, use-case designs, and data pipelines in consulting and enterprise platform settings (5 yrs as Lead Application Engineer on the Volkswagen Group ADA platform at FiveAI / Bosch; 3 yrs at AVL Powertrain UK, incl. 2 yrs on-site at Jaguar Land Rover). Platform super user and technical lead (led 5 engineers for 1 yr; SimEco solutions co-founder) who acts as the 'Voice of the Customer'—authoring feature-request one-pagers to fold recurring client needs into the core roadmap, building Agentic AI workflows with strict guardrails (~10x speedup), and writing practical Python tools (JSON GUI, STAX uploader, data pipelines into analysis dashboards). Honest on gaps: complex-domain experience is automotive/autonomy rather than Retail or commercial iPaaS (Boomi / Mulesoft / Shopify); has not yet used SQL, Power BI, or administered public cloud infra (worked instead with JSON / XODR / signal-list data models, custom web dashboards, Docker dev containers, and dt_flow CI); builds Python tools via AI-assisted coding.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Platform super user, client advisory &amp; 'Voice of the Customer':</b> Primary customer-facing engineer supporting VW Group partner teams on the ADA simulation/data platform, and SimEco solutions co-founder. Analysed client use cases, debugged cross-system API and map (SDB/XODR) integration faults, and acted as the Voice of the Customer—authoring concise feature-request one-pagers to fold client needs into the core roadmap (and implementing features directly in tooling).",
 "<b>Agentic AI orchestration, guardrails &amp; standard-first templates:</b> Built a project-wide GitHub Copilot &amp; Copilot CLI agentic workflow ingesting UN R79 / Euro NCAP rules, DSL docs, and reusable standard-first modular templates (EuroNCAP Simax) to configure test workflows—cutting authoring from ~1 day to ~1 hr (~10x). Enforced AI guardrails (manual baseline run, post-run assertions, random pass spot-checks) and taught colleagues to verify AI output critically.",
 "<b>Python tooling, data pipelines to dashboards &amp; rigorous QA:</b> Built practical Python apps with AI help—a JSON parameter configuration GUI, local STAX uploader, and pipelines feeding front-end analysis dashboards—shipped via Git PRs and dt_flow CI in a Linux Docker dev-container monorepo (Jira). Validated 1,000+ hours of outputs (120+ suites), catching upstream OSM-to-OpenDRIVE conversion distortions and subtle curvature regressions.",
 "<b>Team leadership, coaching &amp; documentation:</b> Led 5 engineers for 1 year (technical lead), coaching peers to get the most from the platform, reviewing configs and evaluations, authoring technical documentation and traceability analysis, and teaching VW Group partner engineers."])

s += job("ADAS Systems Engineer (Feature Owner — Consulting Delivery)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Consulting discovery, business analysis &amp; high/low-level design (Jaguar Land Rover):</b> Embedded 2 years on-site at JLR within AVL's engineering consultancy as Feature Owner for 3 safety-critical systems (RCTA, BSM, Rear Pre-Crash). Captured stakeholder requirements, ran use-case analysis, and defined conceptual state architectures, low-level specs and module signal lists (input/output data models) in IBM DOORS and MKS Integrity (ASPICE V-model), reviewing signal/state alignment and closing defects in RTC / RQM.",
 "<b>Multi-source data validation &amp; stakeholder management:</b> Unified and time-synchronised camera, CAN bus and radar object streams in Vector CANoe / CANape to isolate a 45° boundary delay missed by synthetic HiL tests (run by the HiL team), guiding OEM and Tier 1 supplier teams across 3 calibration releases.",
 "<b>System modelling, ViL integration &amp; triage (DrivingCube &amp; LEVC):</b> Commissioned GNSS ground-truth logging on AVL's DrivingCube ViL platform (MATLAB / Simulink + IPG CarMaker PID sweeps), authored ISO 26262 specs (FMEA participant), and inspected ~20 returned generators at LEVC (bench fault-log downloads)."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): taught space science (ages 9–16); simplified technical topics for non-specialists and planned schedules.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): electric bus powertrain modelling in MATLAB / Simulink; production quality control.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). System modelling (MATLAB / Simulink), C++, hybrid/EV systems, Ansys. Dissertation: stator thermal-network model &amp; test design (MotorCAD, Portunus, Simulink; test design only—bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space, Arduino servo wiring and encoder signal plotting).", line))

s += section("Technical &amp; Implementation Skills")
s.append(KeepTogether([grid([
 ("Agentic AI &amp; guardrails", "Intensive GitHub Copilot &amp; Copilot CLI agent workflows (~10x speedup), AI guardrails (3-stage verification: manual baselines, post-run assertions, silent-pass spot-checks), VLA ML container testing (user-level Docker / ROS 1)"),
 ("Architecture &amp; BA", "Use-case &amp; business analysis, conceptual state diagrams, high/low-level specs, standard-first modular templates, module signal lists &amp; data schemas (JSON, XODR, SDB, OSM), IBM DOORS, MKS Integrity, Jira, Confluence"),
 ("Python, data &amp; QA", "Practical Python (JSON parameter GUI, STAX uploader, pipelines feeding analysis dashboards built with AI help), API &amp; data-transformation debugging, 1,000+ hrs KPIs (Foxglove, CANoe), dt_flow CI/CD, Git PRs, Linux (5 yrs)"),
 ("Leadership &amp; consulting", "2 yrs on-site consulting at JLR (AVL), 5 yrs VW Group platform delivery, 1-yr technical lead for 5 engineers (non-HR), 'Voice of the Customer' feature-request one-pagers, client &amp; peer training, technical documentation"),
 ("Honest technical gaps", "Complex domain is automotive/autonomy rather than Retail; not yet used SQL, Power BI, commercial iPaaS (Boomi / Mulesoft / Shopify), or administered public cloud infra (used Docker dev containers &amp; basic SSH GPU cluster); Python via AI coding")], 0.22)]))

doc.build(s)
