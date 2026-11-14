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
    c.drawString(M, H-23.5*mm, "Forward Deployed Engineer & Technical Lead  |  Client Delivery, AI Workflows & Data Pipelines")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.2)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Bristol, London & Manchester)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   8+ yrs UK residence   |   Happy to travel on-site with clients   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_APBG.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.2, leading=13.0, textColor=colors.HexColor("#222222"), spaceAfter=6.2)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - APBG Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Forward Deployed Engineer – Manager (Accenture Palantir Business Group – London, Manchester, Bristol)</b>",
 "I am applying for the Forward Deployed Engineer – Manager role in the Accenture Palantir Business Group (APBG). Over the past eight years I have worked directly alongside client teams in 'boots on the ground' applications and systems roles—first embedded for two years at Jaguar Land Rover (via AVL Powertrain UK), and then as Lead Application Engineer on FiveAI / Bosch's Volkswagen Group partnership. I want to flag my citizenship status transparently at the outset: I am a British citizen with over eight years of continuous UK residence (since 2017) and a full UK driving licence, and I hold dual British and Turkish nationality. I am raising this upfront so we can confirm whether commercial or non-sole-national programmes within APBG fit alongside the clearance rules stated in the advert.",
 "APBG's emphasis on decomposing messy client problems, presenting clear demos and having the humility to know what you do not yet know matches how I work. To be candid about my technical gaps: I am not a classically trained software engineer—I learned Python on the job with AI-assisted coding—and I have not yet used Palantir (Foundry, Gotham or AIP), PySpark, SQL, TypeScript or React. Likewise, my year leading a five-person engineering team was hands-on technical leadership rather than formal HR line management. Whenever a role has placed me in a new stack, however, I have learned quickly by building working tools and testing them carefully.",
 "At AVL I joined a team that needed engineers on site at Jaguar Land Rover, and stayed for two years as Feature Owner for three safety-related corner-radar features. Sitting alongside customer engineers and Tier 1 suppliers, I translated vague operational goals into use cases, system state architectures, signal lists and verified requirements in DOORS and MKS Integrity (ASPICE V-model). When a feature passed in HiL testing but reacted late on the proving ground, I designed a coarse-to-fine test matrix, unified and time-synchronised camera, CAN bus and radar data streams in Vector CANoe / CANape to pinpoint the delay at the radar's field-of-view edge, and iterated with the supplier on site until we signed off a calibrated fix.",
 "At FiveAI / Bosch I co-founded the Simulation EcoSystem solutions team supporting Volkswagen Group partner engineers across the ADA L4 programme—resolving customer issues, scoping feature requests via one-pagers (and implementing requests directly in our tooling), diagnosing cross-system errors across APIs, maps and simulation tools, and maintaining documentation and traceability across a monorepo workspace with Jira. I led a five-person team for a year through daily tasking, weekly reviews and 'show and tell' teachbacks, and built internal Python applications with AI assistance (a JSON parameter GUI, a local STAX uploader, and data pipelines feeding front-end analysis dashboards across 1,000+ hours of test data). To create compounding internal value, I made intensive daily use of GitHub Copilot and AI agent workflows—building a project-wide Copilot CLI skill that turns regulation rules and modular blocks into validated scenarios roughly ten times faster—and trained colleagues to verify AI output carefully rather than trust it blindly. Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy on 6 November 2026, so I am immediately available for London, Manchester, Bristol or client sites.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
