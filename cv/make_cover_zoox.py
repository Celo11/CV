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
    c.drawString(M, H-23.5*mm, "Systems & Validation Engineer  |  L4 Autonomy, Steering / Braking Features & HiL / Vehicle Test")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence (commutable to Banbury)   |   Immediately available")
    c.restoreState()

txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.6, leading=13.8, textColor=colors.HexColor("#222222"), spaceAfter=7.5)
doc = BaseDocTemplate("Muhammet_Celal_Gokalp_Cover_Letter_Zoox.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - Cover Letter", author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 12*mm, cw, H-HB-2*mm-18*mm, 0,0,0,0)], onPage=header)])

paras = [
 "6 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Staff Engineer – Chassis Actuators (Steering &amp; Braking Systems), Zoox</b>",
 "I am applying for the Chassis Actuators role on your Steering and Braking Systems team. I hold a BSc in Mechanical Engineering and an MSc in Sustainable Automotive Engineering from WMG, University of Warwick, and have eight years of experience sitting between physical vehicle systems and autonomous execution—two years on-site at Jaguar Land Rover with AVL, followed by five years working on an L4 automated driving system at FiveAI / Bosch.",
 "I want to be transparent about my gaps upfront so you can assess where I fit best: I have eight years of industry experience rather than 12+, and my background is on the systems, requirements, Tier 1 supplier coordination, dSPACE HiL / vehicle validation, CAN signal analysis and L4 autonomy side of this role rather than designing and releasing production steer-by-wire or brake-by-wire mechanical parts in CATIA with ASME Y14.5 GD&amp;T (my CAD work has been in SolidWorks). As your posting notes that candidates do not need to match every expectation and that levelling is flexible, I would welcome consideration at the level you find appropriate.",
 "When I started at AVL, a project needed people in ADAS, and as a man of duty who does what the project needs, I stepped in and was placed on-site at Jaguar Land Rover for two years. That is where I found how much I loved hands-on work with real vehicles and test rigs. I owned three corner-radar features (including Rear Cross Traffic Alert with a braking request) from requirements in DOORS and MKS Integrity (ASPICE V-model) through to validation on dSPACE HiL and ViL rigs and on the proving ground, working daily with the Tier 1 supplier and using Vector CANoe and CANape for CAN signal analysis. I also wrote requirements for Lane Keep Assist, Lane Change Assist, Highway Assist and ACC, wrote ISO 26262 safety requirements for a lane change feature and took part in its FMEA. On AVL's DrivingCube ViL project, I built Simulink / IPG CarMaker scenarios to find the steering-wheel torque needed at each turn radius, fitted an external GNSS for ground truth during airstrip steering-torque injection tests, drove a circuit at HORIBA MIRA to capture vehicle data, and ran parameter sweeps to calibrate the simulation steering torque PID controller.",
 "I joined FiveAI (later part of Bosch) hoping to stay hands-on, though the role evolved into test software development for an L4 stack. There I turned UN R79 (automatic steering / lane change) and Euro NCAP requirements into KPIs (lateral acceleration, longitudinal accel/decel limits, road curvature) across 1,000+ hours of data—identifying a curvature-related drop in lane-change success that led to a steering controller fix—and learned Python and error-log diagnosis across APIs and simulation tools. Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy today, so I am immediately available and keen to get back to hands-on hardware and vehicle testing. Living in Coventry with a full UK driving licence, Banbury is an easy commute for me with no relocation needed.",
 "Thank you for reading. I would welcome the chance to discuss how I can contribute to Zoox.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
