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
    c.drawString(M, H-23.5*mm, "System & Software Test Engineer  |  Bench / Vehicle Testing, CAN Diagnostics & Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Immediately available")
    c.restoreState()

txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.6, leading=13.8, textColor=colors.HexColor("#222222"), spaceAfter=7.5)
doc = BaseDocTemplate("Muhammet_Celal_Gokalp_Cover_Letter_System_Test_Engineer.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - Cover Letter", author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 12*mm, cw, H-HB-2*mm-18*mm, 0,0,0,0)], onPage=header)])

paras = [
 "6 November 2026",
 "Dear Hiring Team,",
 "<b>Re: System &amp; Software Test Engineer (Nuneaton) – iO Advanced Mobility / Precision Resource Group</b>",
 "I am applying for the System &amp; Software Test Engineer role supporting advanced suspension and seating systems in Nuneaton. I have eight years in automotive systems, software testing and validation, hold a BSc in Mechanical Engineering and an MSc in Sustainable Automotive Engineering from WMG, University of Warwick, and live in Coventry, 15 minutes from Nuneaton.",
 "When I started my career at AVL, I did not choose ADAS; a project needed people, and I am a man of duty who does what the project needs. The ADAS team liked my work, kept me, and sent me on-site to Jaguar Land Rover for two years. That is where I saw that test engineers get to work hands-on with real cars and test beds, which I loved. I owned three corner-radar features from requirements in IBM DOORS and MKS Integrity (ASPICE V-model) through to writing test cases for each system state and running verification in vehicles and on the proving ground, working daily between the OEM and Tier 1 suppliers. I used Vector CANoe and CANape to log and analyse vehicle CAN communication, trace data and investigate fault codes (DTCs); when a module failed to activate in vehicle tests, I checked fuses and powered modules on a 12 V bench supply to find the cause. When a feature passed in HiL testing (where simulated objects bypassed the radar antenna) but fired late on the track, I synchronised camera, CAN and radar logs in CANoe, traced the issue to the edge of the radar's field of view, and verified the supplier's calibration fix on site. I also wrote ISO 26262 safety requirements, took part in an FMEA, checked returned range-extender generators with a multimeter at the LEVC factory, and drove a circuit at HORIBA MIRA in Nuneaton to capture vehicle dynamics data for an IPG CarMaker / Simulink PID controller.",
 "I joined FiveAI (later part of Bosch) because I was promised I would stay hands-on, though in practice I was thrown into test software development. Once there, I saw how much we could achieve by making simulation evaluation clean and efficient. I learned Python, built internal test tools and data pipelines, and learned to read and diagnose error logs between APIs, maps and simulation tools across more than 1,000 hours of test data. Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy today, so I am immediately available with no notice period.",
 "Now I want to get back into the lab and build my career around hands-on system and hardware testing. To be honest about the gaps in the specification: I have not worked on active suspension or seating systems yet (though for my BSc project our team designed, built and wired a 6-DOF Stewart motion platform in SolidWorks, MATLAB and Arduino), and while I have written test cases, worked on AVL's DrivingCube ViL test bed and analysed CAN logs in Vector CANoe / CANape, I was not the one who operated the HiL rig myself and have not used NI VeriStand / TestStand, CAPL, Jama or Polarion. As my move into test software showed, I learn new tools and rigs quickly.",
 "As a British citizen living in Coventry with a full UK driving licence and no sponsorship required, I can start immediately. Thank you for reading, and I would welcome the chance to talk about the role.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
