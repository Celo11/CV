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
    c.drawString(M, H-23.5*mm, "Systems Engineer  |  Requirements, Verification & Safety")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()
from reportlab.platypus import SimpleDocTemplate
txt = S("t", fontSize=10, leading=14.5, textColor=colors.HexColor("#222222"), spaceAfter=8)
doc = BaseDocTemplate("Muhammet_Celal_Gokalp_Cover_Letter_ZeroAvia.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - Cover Letter", author="Muhammet Celal Gokalp")
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 14*mm, cw, H-HB-2*mm-22*mm, 0,0,0,0)], onPage=header)])

paras = [
 "8 October 2026",
 "Dear Hiring Team,",
 "<b>Re: Hydrogen Fuel Systems Engineer, ZeroAvia</b>",
 "I am applying for the Hydrogen Fuel Systems Engineer role because hydrogen is the field I want to build my career in. I am a mechanical engineer with an MSc in Sustainable Automotive Engineering and nearly eight years of experience in safety-related vehicle systems.",
 "My interest in hydrogen is personal. For years I have had a dream of building solar power plants at sea, where the energy could be used either to make clean drinking water or to produce hydrogen. Hydrogen is the most abundant element in the universe, and it gives us a way to store clean energy and move it to where it is needed. Aviation is one of the hardest sectors to decarbonise, and ZeroAvia is one of the few companies actually flying hydrogen-electric aircraft and working through certification. That is the kind of real engineering I want to be part of.",
 "I will be honest: I have not yet worked with hydrogen or cryogenic systems. What I bring is the systems engineering around them. At AVL, based at Jaguar Land Rover, I owned three driver assistance features. I wrote requirements and system state diagrams, broke them down from system to component level in DOORS and MKS Integrity, and acted as the technical link with suppliers. I wrote test cases traced to those requirements and ran verification on HiL and ViL rigs and on the proving ground. I also wrote ISO 26262 functional safety requirements and am trained in safety standards, so a structured, safety-first approach is how I already work.",
 "At FiveAI / Bosch I plan and run verification for an L4 automated driving system. I turn regulation and test protocols into measurable test conditions, and I analyse results across large datasets. Regulation, evidence and traceability are everyday work for me, and I know they are just as central to aircraft certification.",
 "On the technical side, my MSc dissertation was experimental thermal modelling of an electric machine, and my BSc gave me a base in thermodynamics and fluid mechanics. I also worked on an electric bus powertrain during my internship at TEMSA. I am ready to learn hydrogen storage, distribution and conditioning in depth, and if this role needs more hydrogen experience than I have today, I would be glad to be considered for a systems, test or verification role in your team.",
 "Thank you for your time. I would welcome the chance to talk about how I can contribute to ZeroAvia.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
