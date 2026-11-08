from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable,
                                NextPageTemplate, CondPageBreak)

NAVY = colors.HexColor("#14213D"); ACC = colors.HexColor("#1F7A8C")
GREY = colors.HexColor("#555555"); LIGHT = colors.HexColor("#E8F1F4")
W, H = A4; M = 16*mm; HB = 38*mm

def S(n, **k): return ParagraphStyle(n, fontName=k.pop("f", "Helvetica"), **k)
body = S("b", fontSize=9.2, leading=13, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=1.5)
sec = S("sec", f="Helvetica-Bold", fontSize=11.5, leading=14, textColor=NAVY, spaceBefore=9)
role = S("r", f="Helvetica-Bold", fontSize=10.3, leading=13, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=9.5, leading=12, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=8.8, leading=12, textColor=GREY, alignment=2)
loc = S("l", fontSize=8.8, leading=12, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 23)
    c.drawString(M, H-17*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 10.5); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-23.5*mm, "Test & Verification Engineer  |  Systems Integration")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()
from reportlab.platypus import SimpleDocTemplate
txt = S("t", fontSize=10, leading=14.5, textColor=colors.HexColor("#222222"), spaceAfter=8)
doc = BaseDocTemplate("Muhammet_Celal_Gokalp_Cover_Letter_Leidos.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - Cover Letter", author="Muhammet Celal Gokalp")
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 14*mm, cw, H-HB-2*mm-22*mm, 0,0,0,0)], onPage=header)])

paras = [
 "6 October 2026",
 "Dear Hiring Team,",
 "<b>Re: Test Engineer (R-00187297), Leidos UK</b>",
 "I am applying for the Test Engineer role. I have spent nearly eight years testing safety-related automotive systems, first driver assistance features at Jaguar Land Rover and now an automated driving stack at FiveAI / Bosch. Most of my work has been end-to-end verification and validation of complex systems with large requirement sets, which is what this role is about.",
 "At AVL, based at Jaguar Land Rover, I worked within an ASPICE V-model process. I broke high-level requirements down into low-level ones in DOORS and MKS Integrity, wrote test cases for each system state, and traced them back to the requirements. I then ran integration and system tests on HiL and ViL rigs and on the proving ground, used Vector CANoe and CANape to find root causes, and managed defects in RTC/RQM through to closure.",
 "At FiveAI / Bosch, I design and run large simulation test suites. I have built 120+ parameterised scenarios that generate thousands of test cases, run regression through our test pipeline, and checked results against pass/fail and performance KPIs, such as comfort limits on acceleration and deceleration across more than 1,000 hours of test data. I write Python to automate validation, and I have built internal test tools and data pipelines so the wider team can see results more easily. I work in agile teams day to day, having come from a V-model background.",
 "I should be honest about the gaps. I have not used Robot Framework or Selenium in a project, and I have not worked with Model-Based Systems Engineering. I learn new tools quickly; at FiveAI I picked up OpenSCENARIO 2 and a new simulation toolchain and was soon writing scenarios used across the team. With my Python background, I expect to become productive in Robot Framework and Selenium quickly.",
 "I am a British national and have lived in the UK for over eight years, and I am willing to undergo SC clearance. I would welcome the chance to discuss how I can support your test programmes.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
