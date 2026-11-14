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
    c.drawString(M, H-23.5*mm, "Principal Implementation & Solutions Engineer  |  Agentic AI Workflows, System Architecture & Client Delivery")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.0)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Remote & Fitzrovia, London)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   8 yrs Client Implementation, Architecture & QA   |   Full UK driving licence   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_Xiatech.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=8.95, leading=12.5, textColor=colors.HexColor("#222222"), spaceAfter=5.4)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Xiatech Principal Implementation Engineer Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Abbi and the Xiatech Hiring Team,",
 "<b>Re: Principal Implementation Engineer – Xfuze Agentic Orchestration Platform</b>",
 "I am applying for the Principal Implementation Engineer role at Xiatech. What resonates strongly with me about Xfuze—combining composable integration, unified data views, analytics, and Agentic AI orchestration—alongside your emphasis on architectural judgement and willingness to learn, matches how I have worked for the past eight years delivering complex technical solutions directly for enterprise clients across FiveAI / Bosch (the Volkswagen Group ADA platform) and AVL Powertrain UK (embedded on-site within Jaguar Land Rover).",
 "Before sharing how I deliver client solutions, I want to be completely transparent about where my stack differs from a traditional Retail SaaS consultant. My deep domain experience is in automotive and autonomous systems rather than Retail or commercial iPaaS tools (Boomi, Mulesoft, Shopify), and I have not yet used SQL, Power BI, or administered public cloud infrastructure—having worked instead with structured JSON, OpenDRIVE, and module signal-list data schemas, custom Python pipelines feeding web analysis dashboards, Docker dev containers, and dt_flow CI pipelines. Similarly, I am a systems and implementation engineer who builds practical Python tools via AI-assisted coding rather than a classically trained software engineer, and my year leading five engineers was hands-on technical leadership rather than formal HR line management.",
 "During five years at FiveAI / Bosch, I operated as our go-to platform super user for Volkswagen Group partner teams and co-founded the Simulation EcoSystem (SimEco) solutions team. Beyond diagnosing cross-system faults across APIs, maps, and backend logs, I trained customer engineers across the VW Group cluster and led a five-person engineering team for a year—coaching peers, reviewing configs and evaluations, and keeping quality high. Championing a standard-first mindset with reusable modular blocks and EuroNCAP Simax templates, I acted as the 'Voice of the Customer' by scoping recurring needs via feature-request one-pagers so core teams could fold them into the platform roadmap (and implementing requested features directly in tooling). I also built a project-wide GitHub Copilot / Copilot CLI agentic workflow (~10x faster test authoring) protected by clear AI guardrails—manual baseline runs, automated post-run assertions, and random pass spot-checks—alongside Python tools including a JSON configuration GUI, local STAX uploader, and pipelines feeding analysis dashboards across 1,000+ hours of KPI data.",
 "At AVL Powertrain UK, I spent two years embedded on-site at Jaguar Land Rover within an engineering consultancy environment as Feature Owner for three safety-critical systems—running stakeholder discovery and use-case analysis, authoring conceptual state architectures, low-level designs, and structured module signal lists in IBM DOORS and MKS Integrity (ASPICE V-model), and validating unified camera, CAN bus, and radar data streams in Vector CANoe / CANape to deliver fixes across OEM and Tier 1 teams. As a British citizen (dual national) ready for right-to-work and basic DBS checks, and immediately available following my 6 November 2026 Bosch redundancy, I would love to help Xiatech's clients and implementation engineers unlock Xfuze—remotely and in your Fitzrovia office.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
