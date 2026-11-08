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
    c.drawString(M, H-23.5*mm, "Field & Test Engineer  |  Autonomous Systems Integration & Support")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()
from reportlab.platypus import SimpleDocTemplate
txt = S("t", fontSize=10, leading=14.5, textColor=colors.HexColor("#222222"), spaceAfter=8)
doc = BaseDocTemplate("Muhammet_Celal_Gokalp_Cover_Letter_Archangel.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - Cover Letter", author="Muhammet Celal Gokalp")
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 14*mm, cw, H-HB-2*mm-22*mm, 0,0,0,0)], onPage=header)])

paras = [
 "8 October 2026",
 "Dear Hiring Team,",
 "<b>Re: Field Deployment Engineer, Archangel Autonomy</b>",
 "I am applying for the Field Deployment Engineer role. I have spent nearly eight years testing, integrating and supporting autonomous and driver assistance systems, and I do my best work in the lab and in the field rather than only behind a screen. Archangel's mission of making machines into real teammates for people working in remote and dangerous places is the kind of work I want to be part of.",
 "I will be honest about the gap first: I have not yet worked with UAVs, ArduPilot or PX4. I am ready to learn them quickly, and I plan to start with my own ArduPilot build so I can understand the flight controller, sensors and ground control software hands-on.",
 "What I bring is real experience of getting autonomous systems to work outside the office. At AVL, I was based at Jaguar Land Rover for two years as feature owner for corner radar driver assistance features. I ran tests on HiL and ViL rigs, in vehicles and on the proving ground, and when something went wrong I was the person who found the cause and brought in the right people. For example, I traced a late warning at boundary conditions to the radar's field of view using vehicle network logs, and agreed a fix with the supplier.",
 "At FiveAI / Bosch I work on an L4 automated driving stack. I am the first point of contact when engineers hit problems across the stack, tools, maps and simulation. I take ownership, find the root cause and work with the development teams until it is fixed. I run the stack on Linux in a dev container, write Python tools, and have tested autonomy behaviour across more than 1,000 hours of real-world and simulation data.",
 "Outside work I am always building or fixing something. At university I designed, built and programmed a 6-DOF motion platform, and at home I repair my own cars and build my own computers. I have a full UK driving licence, I am happy to travel 25–50% in the UK and abroad, and as a British national I am willing to undergo security clearance. I would be glad to relocate to Oxford.",
 "Thank you for considering my application. I would welcome the chance to talk about how I can help deploy and support your systems in the field.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
