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
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.45)
line = S("line", parent=body, spaceAfter=0.6)
sec = S("sec", f="Helvetica-Bold", fontSize=9.35, leading=10.6, textColor=NAVY, spaceBefore=1.85)
role = S("r", f="Helvetica-Bold", fontSize=8.8, leading=10.2, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.1, leading=9.7, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=7.55, leading=9.7, textColor=GREY, alignment=2)
loc = S("l", fontSize=7.55, leading=9.7, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 9.4); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Lead Automotive Application & Systems Engineer  |  OEM Design-In, ISO 26262 / ASPICE, EV Systems & Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.7)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to UK relocation & global travel)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   MSc Sustainable Automotive Engineering (WMG)   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_Dukosi.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Dukosi Application Engineer CV",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.45, spaceAfter=1.1)]

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
      ("TOPPADDING",(0,0),(-1,-1),0.9),("BOTTOMPADDING",(0,0),(-1,-1),0.9),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Lead Automotive Application &amp; Systems Engineer with 8 years guiding global OEM and Tier 1 engineering programmes from concept and architecture definition through validation and sign-off (5 yrs as Lead Application Engineer supporting Volkswagen Group on ADA at FiveAI / Bosch; 3 yrs at AVL Powertrain UK, incl. 2 yrs embedded at Jaguar Land Rover and EV factory diagnostics at LEVC). Combines OEM customer ownership, technical training, roadmap influence (feature-request one-pagers, KPI-driven improvements), ASPICE V-model (DOORS, MKS Integrity), ISO 26262 / SOTIF / FMEA, and Python / MATLAB test automation with an MSc in Sustainable Automotive Engineering (hybrid/EV systems, electric-motor stator thermal-network test design, TEMSA electric bus sizing). Honest on gaps: degrees are Sustainable Automotive (MSc) and Mechanical Engineering (BSc) rather than Electronic/Electrical Engineering; automotive hardware/systems background is vehicle ECUs, sensors, and e-machines rather than semiconductor IC / analogue / mixed-signal design, BMS cell monitoring / HV battery packs, AEC-Q100, EMC, Altium / PCB layout, or CAN FD / SPI / I<super>2</super>C.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Strategic OEM customer engagement, escalations &amp; training:</b> Primary customer-facing Application Engineer supporting Volkswagen Group partner teams across ADA, and Simulation EcoSystem (SimEco) co-founder. Built trusted OEM relationships, showed and taught partner engineers across the cluster how to use the toolchain, and led escalation root-cause resolution across APIs, maps (SDB/XODR) and backend logs.",
 "<b>Product &amp; roadmap strategy via feedback &amp; KPI analytics:</b> Captured customer feature requests and authored concise one-pagers to scope requirements with core engineering (and built features directly in project tooling). Defined KPIs across 1,000+ hours of test data (120+ OpenSCENARIO 2 suites), surfacing a subtle road-curvature drop inside nominal spec that influenced the roadmap (steering-controller fix).",
 "<b>Python test automation, documentation &amp; AI workflows:</b> Built Python utilities with AI help (JSON configuration GUI, local STAX uploader, dashboard pipelines) in a Linux dev-container monorepo (dt_flow CI/CD, Git PRs, Jira). Authored technical documentation and traceability analysis, built a GitHub Copilot / CLI workflow (~10x speedup with 3-step verification), and led 5 engineers for 1 year (technical lead)."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>OEM design-in ownership, system architecture &amp; ASPICE / ISO 26262 (Jaguar Land Rover):</b> Embedded 2 years on-site at JLR as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash (plus ACC, LKA, Highway Assist and Lane Change Assist requirements). Led OEM and Tier 1 supplier technical reviews, defined state architectures, module signal lists and requirements in IBM DOORS and MKS Integrity (ASPICE V-model), authored ISO 26262 requirements, and joined a feature FMEA (SOTIF trained).",
 "<b>Advanced debugging, failure analysis &amp; validation:</b> Isolated non-activating ECUs via DTC reads, fuse checks and a 12 V bench supply. When RCTA passed on dSPACE HiL (run by the HiL team) yet fired late (0.5 s vs 2 s) at 45° on track, ran a boundary matrix, time-synchronised camera, CAN bus and radar streams in Vector CANoe / CANape, isolated FOV-edge latency, and iterated on site with the Tier 1 supplier across 3 calibrations.",
 "<b>EV factory diagnostics (LEVC) &amp; MATLAB / Simulink validation (DrivingCube ViL):</b> At LEVC factory, inspected ~20 returned faulty range-extender generators—running multimeter phase-resistance/continuity checks at connector pins and powering units with a bench supply to download proprietary fault logs for developers and suppliers. Commissioned GNSS logging on DrivingCube ViL and calibrated a Simulink / CarMaker model via PID sweeps."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): delivered technical training (ages 9–16); simplified complex topics and planned schedules.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): electric bus powertrain sizing in MATLAB / Simulink; production quality control.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Hybrid/EV systems, Simulink modelling, C++, Ansys. Dissertation: electric motor stator thermal-network modelling &amp; test design (MotorCAD, Portunus, Simulink, type-K thermocouple layout; test design only—bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space, Arduino servo wiring &amp; encoder plotting); PCB motor-cable soldering, multimeter fuse-drain debug &amp; custom PC builds.", line))

s += section("Technical &amp; Application Engineering Skills")
s.append(KeepTogether([grid([
 ("Customer &amp; product strategy", "Global OEM &amp; Tier 1 engagement (5 yrs VW Group ADA, 2 yrs on-site JLR), customer training, feature-request one-pagers &amp; roadmap influence, escalation root cause, 1-yr technical lead for 5 engineers (non-HR)"),
 ("Automotive safety &amp; ASPICE", "ASPICE V-model, ISO 26262 requirements authoring, SOTIF, FMEA participation, state diagrams, module signal lists, end-to-end traceability (IBM DOORS, MKS Integrity, RTC / RQM, Jira, Confluence), technical documentation"),
 ("EV, thermal &amp; diagnostics", "Hybrid/EV powertrain modelling (MSc WMG, TEMSA electric bus), stator thermal-network test design (MotorCAD, Portunus, Simulink), LEVC generator checks (multimeter &amp; bench fault logs), CAN bus (CANoe / CANape), DTCs, vehicle-level Ethernet &amp; FlexRay"),
 ("Python, MATLAB &amp; automation", "Python (JSON config GUI, STAX uploader, dashboard pipelines built with AI help), MATLAB / Simulink, IPG CarMaker, 120+ OpenSCENARIO 2 suites (1,000+ hrs KPIs), dt_flow CI/CD, Git PRs, Linux (5 yrs), GitHub Copilot / CLI (~10x speedup)"),
 ("Honest technical gaps", "Sustainable Automotive (MSc) &amp; Mechanical (BSc) degrees rather than Electronic/Electrical Eng; no semiconductor IC / analogue / mixed-signal design, BMS cell monitoring / HV battery packs, AEC-Q100, EMC, Altium / PCB layout, CAN FD, SPI, I<super>2</super>C, conference white papers/patents, or operating dSPACE HiL directly")], 0.23)]))

doc.build(s)
