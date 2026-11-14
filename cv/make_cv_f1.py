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
body = S("b", fontSize=7.9, leading=10.1, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.55)
line = S("line", parent=body, spaceAfter=0.8)
sec = S("sec", f="Helvetica-Bold", fontSize=9.7, leading=11.2, textColor=NAVY, spaceBefore=2.4)
role = S("r", f="Helvetica-Bold", fontSize=9.1, leading=10.7, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=8.4, leading=10.2, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=7.9, leading=10.2, textColor=GREY, alignment=2)
loc = S("l", fontSize=7.9, leading=10.2, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 21)
    c.drawString(M, H-15*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 9.8); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-21*mm, "Senior Applications & Systems Engineer  |  On-Vehicle Telemetry, Trackside Testing & V&V")
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.9)
    c.drawString(M, H-26.8*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Biggin Hill)   |   British & Turkish citizen")
    c.drawString(M, H-30.8*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Ready for up to 70% international travel   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_F1.pdf")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Formula 1 Senior Applications Engineer CV",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 6*mm, cw, H-HB-2*mm-8*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.6, spaceAfter=1.5)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0.4)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,0.7), items[0]]), *items[1:], Spacer(1,1.4)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),1.1),("BOTTOMPADDING",(0,0),(-1,-1),1.1),("LEFTPADDING",(0,0),(-1,-1),4)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Senior Applications and Systems Engineer (BSc Mechanical; MSc Sustainable Automotive Engineering, WMG Warwick) with 8 years supporting complex on-vehicle electronics, telemetry and validation across automotive customers, suppliers and engineering teams (2 years on-site at Jaguar Land Rover, HORIBA MIRA circuit &amp; LEVC factory with AVL; 5 years on the VW Group ADA programme at FiveAI / Bosch). Proven in systems architecture, requirements analysis, system modelling, validation &amp; verification (V&amp;V), on-car bus/sensor logging (Vector CANoe / CANape, CAN, GNSS ground truth, synchronised camera/radar streams), test-event preparation, issue prioritisation to resolution, and bridging R&amp;D with live track operations. Honest on scope: my 8 years of on-car and trackside work come from automotive OEM proving grounds/circuits rather than F1 or competitive motorsport, and I have not yet worked directly with RF telemetry links, H.264 / MPEG-TS video encoding, or RS-232 / IP network configuration. Dual British/Turkish citizen, immediately available, ready to commute/relocate near Biggin Hill and travel up to 70% internationally.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – 11/2026", [
 "<b>Stakeholder point of contact &amp; bridging R&amp;D with operations:</b> Primary Applications Engineer supporting Volkswagen Group partner teams on the ADA programme, and founding member of the Simulation EcoSystem solutions team. Aligned operational testing needs with R&amp;D paths, represented services in technical debriefs, and guided workflow and architectural enhancements.",
 "<b>Issue management, prioritisation &amp; resource allocation:</b> Triaged and tracked cross-system issues to resolution (Jira, Confluence, Git CI pipelines) by diagnosing error logs across APIs, maps and simulation tools. Led a 5-person engineering team for 1 year—prioritising issues, allocating resources across parallel work packages, running weekly reviews and upholding process best practices.",
 "<b>Performance &amp; reliability data analysis:</b> Monitored and analysed 1,000+ hours of test data against quantitative quality, performance and reliability KPIs (UN R79, Euro NCAP), authored 120+ parameterised OpenSCENARIO 2 scenarios, isolated regressions across releases, and built Python tools and dashboard data pipelines."])

s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Product Owner oversight &amp; trackside / proving-ground test operations (JLR):</b> Embedded on-site at Jaguar Land Rover for 2 years as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. Prepared vehicles, logging and test plans for proving-ground sessions, coordinated OEM R&amp;D, ops and Tier 1 electronics suppliers, and tracked defects to closure in RTC / RQM.",
 "<b>On-car telemetry analysis &amp; root-cause troubleshooting:</b> Monitored and analysed live and logged vehicle CAN bus and sensor streams in Vector CANoe and CANape. When RCTA passed in HiL testing (run by the HiL team; simulated objects bypassed the radar antenna) but fired late on track at 45°, time-synchronised camera video, CAN and proprietary radar logs on one PC, traced the fault to late confidence at the radar FOV edge, and oversaw supplier calibration testing on site to sign off the fix.",
 "<b>On-car instrumentation, commissioning &amp; system modelling (AVL DrivingCube &amp; HORIBA MIRA):</b> Installed and commissioned an external GNSS ground-truth system on the test car, monitored logging health and system readiness during ViL dyno runs, captured live vehicle telemetry on an airstrip and at the HORIBA MIRA circuit, and calibrated a MATLAB / Simulink and IPG CarMaker system model via PID gain sweeps.",
 "<b>Systems architecture, V&amp;V documentation &amp; on-car electronics diagnostics (JLR &amp; LEVC):</b> Authored comprehensive technical documentation—use cases, system state diagrams, module signal lists, requirement specifications, per-state test plans and test reports—in DOORS and MKS Integrity (ASPICE V-model), plus ISO 26262 safety requirements and FMEA participation. Diagnosed non-activating on-car modules via fault codes (DTCs), fuse checks and a 12 V bench supply; at the LEVC factory, inspected ~20 returned range-extender generators (multimeter pin resistance/continuity checks, bench-powered ECU log downloads)."])

s.append(Paragraph("<b>Part-Time Teacher &amp; Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): taught space tech (ages 9–16); coordinated group/staff schedules and clear multi-audience technical communication.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global (05/2014 – 08/2014): calculated power/torque requirements for an electric bus powertrain in MATLAB / Simulink; supported production quality.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018 (2:1 Merit). Hybrid/EV electronics &amp; powertrain systems, C++, Simulink system modelling, Ansys. Dissertation: designed an experimental stator thermal-characterisation test (type-K thermocouple placement, enclosure, method; MotorCAD, Portunus, Simulink; test design only, bench not built).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017. Team project: 6-DOF Stewart mechatronic platform (SolidWorks, MATLAB state-space, Arduino); wired 6 servo actuators, commanded set angles, and plotted encoder signals.", line))

s += section("Technical Skills")
s.append(KeepTogether([grid([
 ("Systems &amp; V&amp;V processes", "Systems architecture, state diagrams, module signal lists, requirements analysis, system modelling, validation &amp; verification (V&amp;V), requirement specs, test plans &amp; test reports, DOORS, MKS Integrity, ASPICE V-model, ISO 26262, FMEA, SOTIF"),
 ("Telemetry &amp; on-car test", "Vector CANoe &amp; CANape, CAN bus telemetry (vehicle platforms also used FlexRay &amp; Automotive Ethernet), time-synchronised camera / CAN / radar logging, GNSS ground-truth commissioning, proving-ground &amp; HORIBA MIRA track testing"),
 ("Hardware &amp; diagnostics", "On-car electronic module fault-finding (DTCs, fuse checks, 12 V bench supply), LEVC generator multimeter checks (resistance, continuity) &amp; bench log retrieval, Arduino servo wiring, stator thermocouple test design, torque wrench, calipers"),
 ("Event ops, software &amp; tools", "Issue prioritisation &amp; tracking (RTC / RQM, Jira, Confluence), technical debriefs, resource allocation (led 5 engineers), stakeholder &amp; supplier liaison, Python tools &amp; data pipelines, MATLAB / Simulink, IPG CarMaker, Linux (5 yrs), Git"),
 ("Transferable scope &amp; gaps", "8 yrs automotive OEM &amp; track testing (not prior F1 / motorsport); no direct RF telemetry link design, H.264 / MPEG-TS video encoding, or RS-232 / IP network configuration. Dual British/Turkish citizen, full UK licence, ready for 70% international travel, immediately available")], 0.22)]))

doc.build(s)
