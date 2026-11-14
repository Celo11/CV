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
body = S("b", fontSize=7.8, leading=9.8, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.5)
line = S("line", parent=body, spaceAfter=0.7)
sec = S("sec", f="Helvetica-Bold", fontSize=9.6, leading=11.0, textColor=NAVY, spaceBefore=2.1)
role = S("r", f="Helvetica-Bold", fontSize=9.0, leading=10.5, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.3, leading=10.0, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=7.8, leading=10.0, textColor=GREY, alignment=2)
loc = S("l", fontSize=7.8, leading=10.0, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 9.6); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Principal / Lead Systems & Applications Engineer  |  Vehicle Diagnostics, Integration, Toolchains & Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.8)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Woking / relocation)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Hands-on vehicle, lab & factory experience   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_McLaren.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - McLaren Automotive Principal Engineer CV",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.5, spaceAfter=1.3)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0.4)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,0.6), items[0]]), *items[1:], Spacer(1,1.1)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),1.0),("BOTTOMPADDING",(0,0),(-1,-1),1.0),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Lead Systems &amp; Applications Engineer with 8 years delivering complex automotive electrical/ADAS integration, on-vehicle fault diagnosis, validation toolchains, and configuration-controlled software workflows across premium and low-volume UK OEM environments (Jaguar Land Rover and LEVC via AVL) and the Volkswagen Group ADA programme (at FiveAI / Bosch). Experienced in end-to-end requirements and interface definition (DOORS, MKS Integrity, ASPICE V-model, module signal lists), traceability analysis, structured root-cause investigation (Vector CANoe / CANape, CAN, DTCs, multimeter &amp; bench-supply triage), FMEA / ISO 26262, and leading a 5-person team. Honest on gaps: my delivery experience comes from OEM R&amp;D, prototype commissioning, proving-ground / ViL validation, and factory returned-unit diagnostics rather than owning series-production End-of-Line (EOL) manufacturing systems, PFMEAs / Control Plans, or VP / PP / SOP line introduction, and I have not yet worked with UDS / DoIP, CAN FD, ECU SWDL / OTA, SDV, or cybersecurity (vehicle-level awareness of Automotive Ethernet / FlexRay rather than deep protocol design).", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Toolchain deployment, configuration control &amp; release readiness:</b> Deployed and supported simulation and diagnostic evaluation toolchains (dt_flow, dt_launcher, Docker dev containers, Linux) in a monorepository workspace using Git pull requests and Jira for the Volkswagen Group ADA programme.",
 "<b>Requirements traceability, process documentation &amp; validation evidence:</b> Performed traceability analysis, maintained technical documentation, scoped partner feature requests via one-pagers (and implemented features directly in project tooling), and delivered pass/fail readiness evidence across 1,000+ hours of test data (120+ parameterised OpenSCENARIO 2 scenarios).",
 "<b>Software deployment utilities, coding &amp; structured fault diagnosis:</b> Co-founded the Simulation EcoSystem (SimEco) solutions team; investigated complex cross-system integration faults across APIs, maps (SDB/XODR) and backend logs, and built internal Python tools with AI assistance—including a JSON parameter configuration GUI, a local STAX artefact uploader, and pipelines feeding front-end dashboards.",
 "<b>Technical leadership, supplier/partner alignment &amp; workflow automation:</b> Led a 5-person engineering team for 1 year (technical lead), coordinating deliverables, weekly reviews, and risk escalation; built a project-wide GitHub Copilot / Copilot CLI agent workflow (~10x scenario speedup with automated verification checks)."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Vehicle electrical/system interfaces, requirements &amp; traceability (Jaguar Land Rover):</b> Embedded on-site at JLR for 2 years as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash (plus ACC, LKA, Highway Assist and Lane Change Assist requirements). Defined system state architectures and module input/output signal lists in IBM DOORS and MKS Integrity (ASPICE V-model), managing validation plans, release records and defect closure in RTC / RQM.",
 "<b>Complex electrical, sensor &amp; CAN fault investigation (CANoe / CANape &amp; on-vehicle DTCs):</b> Diagnosed non-activating vehicle modules via DTC reads, fuse checks and a 12 V bench supply. When RCTA passed on the dSPACE HiL rig (run by the HiL team) but fired late (0.5 s vs 2 s target) at 45° on the proving ground, designed a coarse-to-fine boundary test matrix, time-synchronised camera, CAN bus and radar streams in Vector CANoe / CANape, isolated edge-of-FOV radar latency, and verified 3 supplier calibration candidates on site to sign off the corrective action.",
 "<b>Factory fault-diagnosis (LEVC), ViL commissioning &amp; FMEA / safety:</b> At LEVC (London Electric Vehicle Company) factory, inspected ~20 returned faulty range-extender generators—performing multimeter phase-resistance/continuity checks at connector pins, powering electronics with a bench supply to download fault logs from proprietary loggers, and escalating findings to developers and suppliers. Commissioned GNSS ground-truth logging on AVL's DrivingCube ViL rig (HORIBA MIRA / airstrip data, Simulink / IPG CarMaker PID sweeps), authored ISO 26262 requirements, and took part in a feature FMEA."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): taught space technology (ages 9–16); simplified technical concepts and coordinated schedules.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): electric bus powertrain sizing in MATLAB / Simulink and production quality control in a bus manufacturing plant.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). System modelling (Simulink), C++, hybrid/EV systems, Ansys. Dissertation: electric motor stator thermal-network test design (MotorCAD, Portunus, Simulink; test design only—bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart motion platform (SolidWorks, MATLAB state-space, Arduino servo wiring and encoder signal plotting).", line))

s += section("Technical &amp; Process Skills")
s.append(KeepTogether([grid([
 ("Vehicle diagnostics &amp; networks", "CAN bus, Vector CANoe / CANape, DTC fault diagnosis, proprietary logger fault-log downloads (LEVC), multimeter &amp; 12 V bench-supply commissioning, GNSS/ViL logging; vehicle-level exposure to Automotive Ethernet &amp; FlexRay (no deep protocol spec)"),
 ("Requirements, quality &amp; safety", "IBM DOORS, MKS Integrity, ASPICE V-model, module signal lists &amp; interface definition, end-to-end requirements traceability, RTC / RQM defect management, FMEA participation, ISO 26262 &amp; SOTIF training, technical documentation"),
 ("Toolchains &amp; config control", "Python (JSON configuration GUI, STAX uploader, dashboard pipelines built with AI help), Git PRs, monorepo workspace, dt_flow CI pipelines, Jira, Confluence, MATLAB / Simulink, IPG CarMaker, Linux (5 yrs), Docker dev containers (user)"),
 ("Honest technical gaps", "Not yet used/owned: production End-of-Line (EOL) manufacturing test systems, PFMEAs / Control Plans, VP / PP / SOP factory sign-off, UDS / DoIP, CAN FD, ECU SWDL / OTA, SDV or Cybersecurity (and did not operate the dSPACE HiL rig directly)"),
 ("Leadership &amp; work style", "Calm under pressure, hands-on across vehicle/lab/factory sites, 1-yr technical lead for 5 engineers, OEM &amp; Tier 1 supplier alignment, British &amp; Turkish citizen, full UK licence, immediately available")], 0.24)]))

doc.build(s)
