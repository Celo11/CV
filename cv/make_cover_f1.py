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
    c.setFont("Helvetica", 10.2); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-23.5*mm, "Senior Applications & Systems Engineer  |  On-Vehicle Telemetry, Trackside Testing & V&V")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.2)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Biggin Hill)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Ready for up to 70% international travel   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_F1.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.3, leading=13.2, textColor=colors.HexColor("#222222"), spaceAfter=6.5)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Formula 1 Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Senior Applications Engineer – Telemetry, On-car &amp; Trackside Services (Technical Division, Biggin Hill)</b>",
 "I am applying for the Senior Applications Engineer role supporting Telemetry, On-car and Trackside Services at Formula 1. I am a mechanical and automotive engineer (BSc Mechanical Engineering; MSc Sustainable Automotive Engineering, WMG, University of Warwick) with eight years supporting on-vehicle electronics, telemetry analysis, systems architecture and multi-stakeholder applications across Jaguar Land Rover, AVL Powertrain UK and FiveAI / Bosch. As a dual British and Turkish citizen with a full UK driving licence and no notice period, I am immediately available, open to relocating or commuting near Biggin Hill, and excited to attend up to 70% of F1 events internationally to install, commission and operate trackside systems.",
 "I want to be direct about where my background matches and where I have gaps to bridge: my trackside and on-car engineering experience comes from automotive OEM proving grounds, airstrips and the HORIBA MIRA circuit rather than Formula 1 or competitive motorsport. Likewise, while I have worked extensively with vehicle CAN telemetry, time-synchronised camera/sensor logging and radar field-of-view propagation effects, I have not yet worked directly with trackside RF telemetry links, H.264 video encoding / MPEG-TS transmission or RS-232 / IP network configuration. What I bring is eight years of doing the exact applications, systems engineering, event preparation and calm trackside problem-solving at the core of this role—and a proven record of learning new domains quickly.",
 "When I started my career at AVL, I did not pick ADAS; a project needed engineers, and as someone who steps up to whatever the mission demands, I took it on and spent two years embedded on-site at Jaguar Land Rover as Feature Owner (Product Owner) for three corner-radar features. Ahead of proving-ground sessions I prepared vehicles, instrumentation and test plans, authored comprehensive technical documentation—use cases, system state diagrams, module signal lists, requirement specifications, test plans and test reports—in IBM DOORS and MKS Integrity (ASPICE V-model), and tracked issues to resolution in RTC / RQM between OEM R&amp;D, track operations and Tier 1 suppliers. Hands-on, I fitted and commissioned external GNSS ground-truth logging on AVL's DrivingCube test bed, monitored logging health during dyno and HORIBA MIRA circuit runs to calibrate a Simulink / CarMaker system model, diagnosed non-activating on-car electronics via fault codes, fuse checks and a 12 V bench supply, and inspected ~20 returned generators at the LEVC factory using a multimeter and bench supply. When a safety feature passed in HiL testing but fired late on the proving ground, I time-synchronised camera, CAN and radar telemetry in Vector CANoe / CANape, traced the delay to the radar's field-of-view edge, and oversaw supplier calibration testing on site to verify the fix.",
 "At FiveAI / Bosch I served as Lead Application Engineer on the Volkswagen Group L4 automated driving programme and co-founded our Simulation EcoSystem solutions team—acting as primary technical point of contact for partner engineers, aligning R&amp;D development paths with operational needs, triaging cross-system faults from error logs across 1,000+ hours of data, and building Python diagnostic and dashboard tools. I also led a five-person engineering team for a year, prioritising issues, allocating resources across parallel work packages and representing our services in technical debriefs. Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy on 6 November 2026, making me immediately available. I would welcome the opportunity to discuss how my applications, systems and on-car telemetry background can support Formula 1's trackside engineering team.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
