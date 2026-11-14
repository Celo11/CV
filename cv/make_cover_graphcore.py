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
    c.setFont("Helvetica", 9.8); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-23.5*mm, "Staff / Lead Systems & Hardware Test Engineer  |  Diagnostics, Test Automation, Linux & Root-Cause Debug")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.1)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK (open to Bristol / UK hybrid or relocation)   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   8 yrs Systems Test, Diagnostics & Automation   |   Immediately available")
    c.restoreState()

OUT = str(Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_Cover_Letter_Graphcore.pdf")
txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.0, leading=12.6, textColor=colors.HexColor("#222222"), spaceAfter=5.5)
doc = BaseDocTemplate(OUT, pagesize=A4,
                      title="Muhammet Celal Gokalp - Graphcore Staff Hardware System Test Cover Letter",
                      author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 11*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header)])

paras = [
 "14 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Staff Hardware System Test Engineer (Graphcore – Product Test &amp; Diagnosis)</b>",
 "I am applying for the Staff Hardware System Test Engineer role in Graphcore's Product Test and Diagnosis team. Over the past eight years across FiveAI / Bosch (supporting the Volkswagen Group ADA programme) and AVL Powertrain UK (embedded at Jaguar Land Rover and the LEVC factory), I have built my career around solving complex hardware and software boundary failures through data, structured root-cause investigation, and individual-contributor technical leadership.",
 "Because Graphcore values direct technical honesty, I want to state upfront where my background differs from your essential silicon and datacentre manufacturing criteria. My hardware test and diagnostic experience comes from automotive ECUs, radar sensors, Vehicle-in-the-Loop rigs, factory returned range-extender generators (at LEVC), and building and troubleshooting my own desktop PCs—not manufacturing test for AI accelerator silicon, Host Processor Modules, server blades, multi-node racks, high-speed board interconnects, or OpenBMC. Likewise, I am not a classically trained software engineer: I build and maintain Python test utilities using AI-assisted coding backed by strict verification, and I did not operate the dSPACE HiL rig directly. What transfers directly is how I work: taking technical ownership without line-management overhead, working daily on Linux (five years), and relentlessly isolating the true cause of system defects and false failures.",
 "On the hardware and factory side, I inspected around 20 returned faulty range-extender generators at the LEVC factory following structured triage procedures—performing multimeter phase-to-phase resistance and continuity checks at specified connector pins, powering control units from a bench supply to extract proprietary fault logs, and feeding diagnostic evidence back to engineering and supplier teams. Embedded at Jaguar Land Rover, I isolated non-activating modules during bring-up via DTC reads, fuse checks, and 12 V bench supplies. When Rear Cross Traffic Alert passed on HiL (where synthetic targets bypassed the radar antenna) yet reacted late at 45° on track, I time-synchronised camera, CAN bus, and radar logs in Vector CANoe / CANape to pinpoint FOV-edge latency and verified three supplier calibrations—including systematic false-positive and false-negative boundary tests.",
 "In Linux-based software and test infrastructure at FiveAI / Bosch, I worked inside a Docker dev-container monorepo with Git PRs, dt_flow CI/CD pipelines, and Jira (including basic SSH GPU-cluster runs). As hands-on technical lead for five engineers for a year—with no formal HR line management—and co-founder of the Simulation EcoSystem (SimEco) diagnosis group, I coordinated cross-team root-cause work across APIs, maps, and backend logs. I built Python utilities with AI help (a JSON configuration GUI, local STAX artefact uploader, and pipelines feeding diagnostic dashboards), cut test authoring time ~10x via a verified GitHub Copilot / Copilot CLI workflow, and eliminated false downstream 'stay in lane' test failures by tracing them to upstream OSM-to-OpenDRIVE curve discretisation and adding numeric edge-case checks. Immediately available following my 6 November 2026 Bosch redundancy, I would welcome the chance to bring that diagnostic ownership to Graphcore in Bristol or across your UK sites.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
