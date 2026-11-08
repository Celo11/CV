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
    c.setFont("Helvetica", 10.5); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-23.5*mm, "Systems Engineer  |  Requirements, Vehicle Systems Integration & Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()

txt = ParagraphStyle("t", fontName="Helvetica", fontSize=10, leading=14.5, textColor=colors.HexColor("#222222"), spaceAfter=8)
doc = BaseDocTemplate("Muhammet_Celal_Gokalp_Cover_Letter_AlexanderDennis.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - Cover Letter", author="Muhammet Celal Gokalp")
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 14*mm, cw, H-HB-2*mm-22*mm, 0,0,0,0)], onPage=header)])

paras = [
 "3 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Lead Engineer – Vehicle Systems, Alexander Dennis</b>",
 "I am applying for the Lead Engineer – Vehicle Systems role in your Advanced Engineering &amp; Concepts team. I am a systems engineer with eight years in automotive product development, and sustainable public transport is where I want to use that experience. My first engineering work was an internship at TEMSA, a bus and coach maker, sizing a new electric bus powertrain, and my MSc at Warwick was in Sustainable Automotive Engineering.",
 "At AVL I spent two years on-site at Jaguar Land Rover as feature owner for three radar-based driver assistance features, from requirements to testing. I wrote use cases, state diagrams and requirements in DOORS and MKS Integrity under the ASPICE V-model, broke them down from high to low level, defined each module's signal list and traced test cases to every system state. I tested on HiL and ViL rigs, in vehicles and on the proving ground, and was the link between JLR, AVL and the radar supplier. When a feature passed every rig test but fired late on the track, I designed the tests that traced it to the edge of the radar's field of view and verified the supplier's fix. I also wrote ISO 26262 safety requirements and took part in an FMEA.",
 "At FiveAI / Bosch I work on an L4 automated driving system. I turn UN R79, Euro NCAP and customer requirements into KPIs and pass/fail criteria, checked across more than 1,000 hours of test data, and I led a team of five engineers for a year. I also built an AI helper with GitHub Copilot that turns regulation text into test scenarios. It is used across the project and cut the time to write a scenario from about a day to about an hour. I taught colleagues to check AI output rather than just trust it, which is how I think AI belongs in engineering processes.",
 "I will be honest that I have not yet used MBSE tools or SysML. My model-based work so far has been in MATLAB / Simulink and IPG CarMaker. I learn new tools quickly, as I did with OpenSCENARIO 2 and Python, and I would be keen to build MBSE skills in your team.",
 "Your values of safety, quality and teamwork match how I like to work, and helping public transport become cleaner is work I would be proud of. I am based in Coventry and happy to work from any UK site. Thank you for your time. I would welcome the chance to talk about how I can contribute.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
