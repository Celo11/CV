from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph

NAVY = colors.HexColor("#14213D"); ACC = colors.HexColor("#1F7A8C")
W, H = A4; M = 16*mm; HB = 38*mm

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 23)
    c.drawString(M, H-17*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 10.0); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-23.5*mm, "Principal / Lead IV&V & Systems Integration Engineer  |  V-Model, Control Systems & Sim/Stim Environments")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.1)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Barrow hybrid / relocation)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   8+ yrs continuous UK residence (since 2017)   |   Full UK driving licence   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_BAE.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.05, leading=12.7, textColor=colors.HexColor("#222222"), spaceAfter=5.6)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - BAE Systems Principal C&I IV&V Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Principal C&amp;I Engineer – Integration (IV&amp;V), SSN AUKUS Platform Complex Systems (Barrow-in-Furness)</b>",
 "I am applying for the Principal C&amp;I Engineer – Integration (IV&amp;V) role within BAE Systems' SSN AUKUS Platform Complex Systems team. Over the past eight years I have delivered full Systems Engineering V-Model integration, control system verification, data interface analysis, and off-platform simulation/stimulation (Sim/Stim) test workflows across Jaguar Land Rover (via AVL Powertrain UK) and FiveAI / Bosch's Volkswagen Group ADA programme. In light of BAE Systems' security and export-control notice, I want to be completely transparent upfront: I am a British citizen with over eight years of continuous UK residence (since 2017) and a full UK driving licence, and I hold dual British and Turkish nationality. I raise this early so your recruitment and security team can verify eligibility against SSN AUKUS programme and National Security Vetting requirements alongside BPSS.",
 "I also want to be candid about where my background differs from marine or industrial C&amp;I. My career has focused on automotive and autonomous control systems (MATLAB / Simulink control modelling, CAN fieldbus analysis, Vehicle-in-the-Loop test beds, and Linux/Python simulation environments) rather than submarine nuclear C&amp;I or industrial PLC fieldbuses (Profibus, Modbus, EtherCAT). Likewise, my test-facility experience stems from commissioning external GNSS logging and verifying simulation readiness on existing ViL rigs, wiring a six-axis actuator rig at university, and designing a stator thermal-network test bench for my MSc (test design only, not physically built), rather than civil facility construction from concept to handover. Across every programme, however, my core contribution has been directly transferable to PCS IV&amp;V: decomposing complex requirements, verifying third-party data interfaces, calibrating Sim/Stim plant models against physical behaviour, and producing clear assurance evidence.",
 "During three years with AVL Powertrain UK, I spent two years embedded at Jaguar Land Rover as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor, and Rear Pre-Crash—decomposing requirements into state architectures, per-state test cases, and module input/output signal lists in IBM DOORS and MKS Integrity (ASPICE V-model), and tracking defects to closure in RTC / RQM. I also supported AVL's DrivingCube ViL Sim/Stim facility, fitting GNSS ground-truth logging, capturing airstrip and HORIBA MIRA reference data, calibrating a Simulink + IPG CarMaker plant model via steering-torque PID sweeps, and checking ViL logging health. When RCTA passed in HiL testing (run by the HiL team, bypassing the radar antenna) but fired late at 45° on the proving ground, I time-synchronised camera, CAN bus, and radar streams in Vector CANoe / CANape to pinpoint radar FOV latency and validate three third-party supplier calibrations—alongside authoring ISO 26262 requirements, joining a feature FMEA, and inspecting ~20 returned generators at LEVC.",
 "At FiveAI / Bosch, I co-founded the Simulation EcoSystem solutions team supporting Volkswagen Group partners—developing and supporting off-vehicle Sim/Stim and evaluation infrastructure (dt_flow, dt_launcher, Linux dev containers) in a monorepo workspace with Git PRs and Jira, debugging third-party API and map interfaces, producing clear technical documentation and feature-request one-pagers, and verifying control behaviour and traceability across 1,000+ hours of closed-loop test data. I built internal Python tools with AI assistance (a JSON parameter GUI, local STAX uploader, and dashboard pipelines), automated scenario verification via GitHub Copilot (~10x faster), and led a five-person engineering team for a year. Following Volkswagen Group's programme exit, my role ended by redundancy on 6 November 2026; I am immediately available and well suited to the Barrow-in-Furness hybrid pattern (two days on site every second week) or relocation.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
