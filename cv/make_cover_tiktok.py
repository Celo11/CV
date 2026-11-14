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
    c.drawString(M, H-23.5*mm, "Solutions Engineer  |  Client Engineering Partnerships, Python Tooling & Data Analytics")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.2)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to London)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Immediately available (no notice period)")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_TikTok.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.3, leading=13.1, textColor=colors.HexColor("#222222"), spaceAfter=6.4)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - TikTok Solutions Engineer Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Solutions Engineer – TikTok (London, UK)</b>",
 "I am applying for the Solutions Engineer role at TikTok in London. Over the past eight years I have worked in customer-facing solutions, applications and systems engineering—managing client engineering relationships, diagnosing cross-platform API and simulation issues, building custom Python tools and data pipelines, and influencing product roadmaps across the Volkswagen Group L4 automated driving partnership (at FiveAI / Bosch) and Jaguar Land Rover (via AVL Powertrain UK). As a British citizen with no notice period, I am immediately available and ready to work from London.",
 "In the spirit of TikTok's 'Always Day 1' mindset, I want to be upfront about where my background differs from the job description: my degrees are an MSc in Sustainable Automotive Engineering from WMG, University of Warwick (which included computing, C++ programming and system modelling) and a BSc in Mechanical Engineering rather than Computer Science. I am an applications and solutions engineer who builds and ships Python tools, GUIs and dashboard data pipelines with AI-assisted coding—and reads C++—rather than a classically trained backend engineer building distributed Go or Java web services from scratch, and my large-volume analytics experience comes from enterprise automotive partnerships rather than advertising technology (AdTech). Throughout my career, I have repeatedly stepped into unfamiliar software ecosystems and delivered working tools fast.",
 "At FiveAI / Bosch I served as Lead Application Engineer on the Volkswagen Group ADA partnership and co-founded our Simulation EcoSystem (SimEco) solutions team. Working alongside partner engineers, I managed external client engineering relationships, diagnosed cross-system errors across APIs, maps (SDB/XODR) and backend simulation logs, and coordinated joint fixes across internal product teams. To solve recurring workflow bottlenecks, I built and shipped custom Python applications into our monorepo via Git pull requests, Linux dev containers and dt_flow CI pipelines—including a JSON parameter configuration GUI, a local STAX uploader, and data pipelines routing metrics from 1,000+ hours of test data to front-end analysis dashboards. Analysing those high-volume KPIs also enabled me to surface a road-curvature drop that directly influenced our core steering controller roadmap, while a project-wide GitHub Copilot / Copilot CLI workflow I built cut scenario authoring from ~1 day to ~1 hour (~10x). I also led a five-person engineering team for a year. Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy on 6 November 2026.",
 "Earlier, at AVL, I spent two years embedded on-site at Jaguar Land Rover as Feature Owner for three corner-radar safety features—owning client and supplier alignment end-to-end and tracing a late proving-ground trigger to the radar's field-of-view edge via synchronised camera, CAN and radar logs. Combined with three years teaching science and space technology to 9–16-year-olds at Space Camp Turkey, I am used to translating complex technical problems cleanly for non-technical stakeholders and diverse partner groups. Thank you for reading, and I would welcome the chance to discuss how I can support TikTok's client engineering teams.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
