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
    c.setFont("Helvetica", 9.6); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-23.5*mm, "Lead Automotive Application & Systems Engineer  |  OEM Design-In, ISO 26262 / ASPICE, EV Systems & Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.0)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to UK relocation & global travel)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   MSc Sustainable Automotive Engineering (WMG)   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_Dukosi.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.0, leading=12.6, textColor=colors.HexColor("#222222"), spaceAfter=5.5)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Dukosi Application Engineer Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Application Engineer (Dukosi)</b>",
 "I am applying for the Application Engineer role at Dukosi. Enabling safer, more sustainable electric vehicles and energy storage aligns closely with why I studied Sustainable Automotive Engineering (MSc, WMG, University of Warwick) and began my engineering internships in electric bus powertrain sizing at TEMSA. Over the past eight years across FiveAI / Bosch (supporting the Volkswagen Group ADA programme) and AVL Powertrain UK (embedded on-site at Jaguar Land Rover and supporting LEVC's electric taxi factory), I have owned strategic OEM and Tier 1 technical relationships, translated customer needs into system architectures and product roadmaps, and led root-cause validation across complex automotive programmes.",
 "Before detailing those programmes, I want to be completely transparent about where my background differs from a semiconductor hardware specialist. My degrees are in Sustainable Automotive Engineering (MSc) and Mechanical Engineering (BSc) rather than Electronic or Electrical Engineering, and I have not worked directly on semiconductor IC development, analogue or mixed-signal circuits, Battery Management Systems (BMS) or high-voltage battery packs, AEC-Q100 qualification, EMC compliance testing, Altium PCB layout, or CAN FD / SPI / I<super>2</super>C (and I did not operate the dSPACE HiL rig directly). Similarly, my technical writing covers internal specs, documentation, and feature one-pagers rather than external conference white papers or patents. What transfers immediately, however, is proven customer ownership in safety-critical automotive programmes: guiding OEMs and suppliers through ASPICE and ISO 26262 architectures, solving tough cross-system faults, and feeding frontline insight back into product strategy.",
 "During five years at FiveAI / Bosch, I served as primary customer-facing Application Engineer for Volkswagen Group partner teams and co-founded the Simulation EcoSystem (SimEco) solutions team. I delivered hands-on toolchain training across the customer cluster, owned technical escalations across APIs, maps, and backend logs, and led a five-person engineering team for a year as technical lead. Directly relevant to Dukosi's Product and Technology Strategy duties, I captured partner requirements via concise feature-request one-pagers (building requested features directly in project tooling where appropriate) and analysed 1,000+ hours of automated test KPIs (120+ parameterised suites in Python/CI) to uncover a subtle curvature-tracking issue that reshaped our steering controller—alongside building Python utilities and a verified GitHub Copilot workflow (~10x faster test creation).",
 "At AVL Powertrain UK, I spent two years embedded on-site at Jaguar Land Rover as Feature Owner for Rear Cross Traffic Alert, Blind Spot Monitor, and Rear Pre-Crash—leading technical reviews with OEM and Tier 1 engineers, defining state architectures and module signal lists in IBM DOORS and MKS Integrity (ASPICE V-model), authoring ISO 26262 safety requirements, and joining a feature FMEA. When RCTA passed in HiL testing yet fired late at 45° on track, I time-synchronised camera, CAN bus, and radar logs in Vector CANoe / CANape and iterated with the supplier across three calibrations to sign off the fix. Alongside JLR, I inspected ~20 returned range-extender generators at LEVC (multimeter pin checks and bench-powered fault-log downloads), and my MSc dissertation designed a stator thermal-network identification test using MotorCAD, Portunus, and Simulink (test design only, bench not built). Immediately available following my 6 November 2026 Bosch redundancy, I hold a full UK driving licence and am ready to relocate or travel globally for Dukosi.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
