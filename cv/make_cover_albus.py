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
    c.setFont("Helvetica", 9.65); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-23.5*mm, "Principal Systems Test & Automation Engineer  |  Multi-Stage Data Pipelines, Radar/Sensor Systems & AI Testing")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.1)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Oxford hybrid / commute)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   8 yrs Systems V&V, Radar & Test Automation   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_Albus.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.0, leading=12.6, textColor=colors.HexColor("#222222"), spaceAfter=5.5)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Albus Health Principal Systems Test Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Principal Systems Test &amp; Automation Engineer (Albus Health – Oxford, Hybrid)</b>",
 "I am applying for the Principal Systems Test &amp; Automation Engineer role at Albus Health. What excites me most about Albus Home is the core technical test problem: validating an international, contactless multisensory platform—spanning radar and audio data capture, connected devices, and multi-stage signal-processing and machine-learning pipelines—where subtle failures can be introduced or masked between processing stages. Over the past eight years at FiveAI / Bosch (autonomous driving scale-up / Volkswagen Group ADA partnership) and AVL Powertrain UK (two years embedded on-site at Jaguar Land Rover), I have specialised in following sensor and software data end to end to expose hidden failure modes and build automated test frameworks that catch them before release.",
 "To be completely transparent about where my background differs from your desirable or cloud-ops items: my regulated V-model verification experience comes from safety-critical automotive and autonomous systems (ASPICE V-model, ISO 26262, SOTIF) rather than biomedical devices or medical software standards (IEC 62304, ISO 13485). Likewise, while I have tested containerised ML components (user-level Docker / ROS 1), local artefact uploaders, and CI/CD data pipelines, I have not directly administered AWS cloud infrastructure, and I build and maintain Python tools and test automation using AI-assisted coding rather than coming from a traditional software-engineering degree. Across every role, however, my strength has been acting as an investigative systems engineer—challenging test assumptions, verifying AI outputs independently, and tracing unexpected results across interconnected stages.",
 "Three examples illustrate how I investigate multi-stage data and sensor pipelines. First, as Feature Owner for Jaguar Land Rover's radar features (Rear Cross Traffic Alert, Blind Spot Monitor, Rear Pre-Crash), RCTA passed every HiL test (run by the HiL team, where synthetic targets entered the ECU bypassing the radar antenna and target-processing stage) yet reacted late at 45° on track; I designed a coarse-to-fine matrix, time-synchronised camera, CAN bus, and internal radar detection/object streams in Vector CANoe / CANape, isolated late confidence build-up at the radar FOV edge, and verified three supplier calibrations (including false-positive and false-negative checks). Second, at FiveAI / Bosch, when an OpenDRIVE evaluation validator reported false 'stay in lane' failures, I traced the fault upstream to an OSM-to-OpenDRIVE map converter turning curves into coarse straight segments—and replaced visual spot-checks with numeric hard-case validation. Third, across 1,000+ hours of multi-stage evaluation (120+ parameterised OpenSCENARIO 2 suites in dt_flow CI/CD), I surfaced a road-curvature tracking degradation hidden inside nominal pass criteria, prompting a steering-controller fix.",
 "I also build practical test infrastructure and apply AI-assisted testing with strict engineering judgement: writing internal Python tools (a JSON parameter GUI, local STAX uploader, and dashboard data pipelines), running a project-wide GitHub Copilot / Copilot CLI test-authoring workflow (~10x faster) backed by a three-stage verification check (manual baselines, automated post-run assertions, and random pass spot-checks to catch silent false passes), maintaining documentation and traceability in Jira / DOORS, and leading a five-person test team for a year as hands-on technical lead. Following Volkswagen Group's programme exit, my role ended by redundancy on 6 November 2026; based in Coventry with a full UK driving licence, I am immediately available and ready to commute into your Oxford office for hybrid collaboration.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
