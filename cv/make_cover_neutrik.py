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
    c.drawString(M, H-23.5*mm, "Field Application Engineer  |  OEM Design-In, Customer Training & Hands-On Troubleshooting")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.2)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Hook, 3+ days/wk)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Ready for EMEA & international travel   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_Neutrik.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.2, leading=13.0, textColor=colors.HexColor("#222222"), spaceAfter=6.2)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Neutrik Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Field Application Engineer – Neutrik EMEA Sales (Hook, UK)</b>",
 "I am applying for the Field Application Engineer role at Neutrik in Hook. I am a mechanical and automotive engineer (BSc Mechanical Engineering; MSc Sustainable Automotive Engineering, WMG, University of Warwick) with eight years in customer-facing application and systems engineering—leading OEM design-in projects at Jaguar Land Rover (via AVL Powertrain UK), supporting and teaching external partner engineers on the Volkswagen Group partnership (at FiveAI / Bosch), and performing hands-on connector-pin, wiring and electronics troubleshooting. As a dual British and Turkish citizen with a full UK driving licence and no notice period, I am immediately available, happy to relocate to work from your Hook office at least three days a week, and ready for EMEA and international travel (including India).",
 "I want to be direct about where my experience comes from and what is new to me: my eight years of OEM design-in work and hardware diagnostics come from automotive electronics and autonomous systems rather than commercial pro audio, video, broadcast connectors or the optical fibre market. Likewise, I have used engineering lifecycle tools (DOORS, MKS Integrity, RTC / RQM, Jira and Confluence) rather than commercial sales CRM systems, and my languages are fluent English (C2), native Turkish and basic Italian (rather than German, Spanish or French). At the same time, I love hands-on wiring and hardware work—at the LEVC factory I inspected ~20 returned generators via multimeter checks at specified connector pins (phase resistance and continuity) and bench-powered fault-log downloads, and outside software I have wired my own car sound system, soldered motor drive cables onto a PCB, wired six servos and encoders on a 6-DOF motion platform, and built my own desktop PCs.",
 "At AVL I spent two years embedded on-site at Jaguar Land Rover as Feature Owner for three corner-radar safety features—serving as the technical link between OEM engineering teams, AVL and the Tier 1 supplier. I led feasibility and integration from customer requirements through interface signal lists, system state diagrams and specifications in DOORS and MKS Integrity, diagnosed non-activating vehicle modules via fault codes, fuses and a 12 V bench supply, and handled on-site troubleshooting. When a braking alert passed in HiL testing (run by the HiL team) but triggered late on the proving ground, I synchronised camera, CAN and radar logs in Vector CANoe / CANape, traced the delay to the radar's field-of-view edge, and ran boundary tests on site with the supplier to verify the fix.",
 "At FiveAI / Bosch I worked as Lead Application Engineer on the Volkswagen Group L4 partnership and co-founded our Simulation EcoSystem solutions team—acting as first point of contact for technical questions, diagnosing cross-system errors from API and simulation logs, teaching external partner engineers how to use our toolchain, leading a five-person engineering team for a year, and building Python tools and analytics pipelines across 1,000+ hours of test data (alongside three years teaching science and space technology simply to ages 9–16 at Space Camp Turkey). Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy on 6 November 2026. Thank you for reading, and I would welcome the chance to discuss how I can support Neutrik's customers.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
