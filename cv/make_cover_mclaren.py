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
    c.drawString(M, H-23.5*mm, "Principal / Lead Systems & Applications Engineer  |  Vehicle Diagnostics, Integration, Toolchains & Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.1)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Woking / relocation)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Hands-on vehicle, lab & factory experience   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_McLaren.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.1, leading=12.8, textColor=colors.HexColor("#222222"), spaceAfter=5.8)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - McLaren Automotive Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Principal Engineer – Process &amp; Systems (McLaren Automotive)</b>",
 "I am applying for the Principal Engineer – Process &amp; Systems role at McLaren Automotive. Over the past eight years I have delivered automotive electrical and ADAS integration, on-vehicle fault diagnosis, configuration-controlled toolchains, and validation evidence across premium and low-volume UK OEM environments—most notably two years embedded on-site at Jaguar Land Rover and hands-on factory diagnostics at LEVC (via AVL Powertrain UK), followed by five years as Lead Application Engineer on FiveAI / Bosch's Volkswagen Group ADA partnership.",
 "Before setting out where I add immediate value, I want to be completely transparent about what I have not yet owned directly. My automotive delivery has been in OEM R&amp;D feature ownership, prototype and proving-ground commissioning, ViL validation, and factory returned-unit triage rather than series-production End-of-Line (EOL) manufacturing systems, PFMEAs / Control Plans, or VP / PP / SOP line introduction. Similarly, I have not yet worked hands-on with UDS / DoIP, CAN FD, ECU software download (SWDL) / OTA, SDV, or automotive cybersecurity, and my exposure to Automotive Ethernet and FlexRay is at whole-vehicle level rather than deep protocol design. Where every role has demanded new toolchains or protocols, however, my foundation—defining clean electrical/system interfaces, tracing requirements through to validation evidence, and systematically isolating vehicle faults under pressure—has enabled me to contribute rapidly.",
 "During my three years with AVL, I worked hands-on across customer sites, vehicles, test beds, and factory floors. Embedded at Jaguar Land Rover for two years as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor, and Rear Pre-Crash, I defined state architectures and module input/output signal lists, maintained full ASPICE V-model traceability in IBM DOORS and MKS Integrity, and managed validation evidence and defect closure in RTC / RQM. In vehicle commissioning and troubleshooting, I isolated non-activating modules using DTC reads, fuse checks, and a 12 V bench supply; and when RCTA passed in HiL testing (run by the HiL team) yet fired late at 45° on the proving ground, I designed a coarse-to-fine test matrix, time-synchronised camera, CAN bus, and radar streams in Vector CANoe / CANape, traced the delay to radar FOV edges, and iterated on site with the Tier 1 supplier across three calibration builds until sign-off. Separately, at the LEVC factory I inspected around 20 returned range-extender generators—running multimeter phase-resistance and continuity checks at connector pins and powering units with a bench supply to extract proprietary fault logs for developers and suppliers—alongside authoring ISO 26262 requirements, taking part in a feature FMEA, and commissioning GNSS logging on AVL's DrivingCube ViL rig.",
 "At FiveAI / Bosch, I co-founded the Simulation EcoSystem solutions team supporting Volkswagen Group partners—leading a five-person engineering team for a year, managing weekly reviews and risk escalation, and keeping toolchains (dt_flow, dt_launcher, Linux dev containers) configuration-controlled in a monorepository workspace with Git PRs and Jira. I authored technical documentation and feature-request one-pagers, built internal Python utilities with AI assistance (a JSON configuration GUI, STAX artefact uploader, and dashboard pipelines), and verified traceability and readiness evidence across 1,000+ hours of test data. Following Volkswagen Group's programme exit, my role ended by redundancy on 6 November 2026; I hold a full UK driving licence, am immediately available, and would be delighted to relocate or commute to Woking to support McLaren's vehicle programmes.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
