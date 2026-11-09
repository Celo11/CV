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
    c.drawString(M, H-23.5*mm, "Test Facility & Systems Engineer  |  BSc Mechanical & MSc Automotive Engineering")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   20 min from Leamington Spa   |   Immediately available")
    c.restoreState()

txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.6, leading=13.8, textColor=colors.HexColor("#222222"), spaceAfter=7.5)
doc = BaseDocTemplate("Muhammet_Celal_Gokalp_Cover_Letter_Ricardo.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - Cover Letter", author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 12*mm, cw, H-HB-2*mm-18*mm, 0,0,0,0)], onPage=header)])

paras = [
 "6 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Test Facility Engineer (Role ID: 2025-3164) – Midlands Technical Centre, Leamington Spa</b>",
 "I am applying for the Test Facility Engineer role in your Test Operations Department at Leamington Spa. I hold a BSc in Mechanical Engineering and an MSc in Sustainable Automotive Engineering from WMG, University of Warwick, have eight years in automotive testing, validation and multi-discipline coordination, and live in Coventry, 20 minutes from the Midlands Technical Centre.",
 "My academic and early career roots are in powertrain and mechanical testing: at TEMSA I calculated power and torque requirements for an electric bus powertrain, and for my Warwick MSc dissertation I designed a test to find the thermal model variables of an electric motor stator, specifying type-K thermocouple placement, the test enclosure and the test method using MotorCAD and Simulink. When I joined AVL Powertrain UK, a project needed people in ADAS, and as a man of duty who does what the project needs, I stepped in and spent two years on-site at Jaguar Land Rover. That is where I saw how much I loved hands-on work with real vehicles and test beds. Alongside vehicle and proving-ground testing, I worked on AVL's DrivingCube Vehicle-in-the-Loop dyno test bed—fitting an external GNSS system to the vehicle for position ground truth, driving airstrip and HORIBA MIRA circuit tests to calibrate the simulation PID controller, and monitoring logging health during test-bed runs. At the LEVC (London Taxi) factory I carried out multimeter checks (phase-to-phase resistance, continuity) on about 20 returned faulty range-extender generators and powered the control unit from a bench supply to download supplier logs.",
 "I joined FiveAI (later part of Bosch) because I was promised I would stay hands-on, though the role became test software development. Once there, I learned Python, built internal test tools and reporting pipelines, led a team of five engineers for a year—splitting work packages, holding weekly progress meetings and reviewing deliveries—and served as a founding member of our solutions team supporting Volkswagen Group partner engineers across disciplines. Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy today, so I am immediately available with no notice period.",
 "Now I want to get back to physical test facilities, rigs and hardware. Outside work I repair my own cars, use a multimeter, torque wrench, calipers and micrometers, and at university our team designed, built and wired a 6-DOF motion platform in SolidWorks, MATLAB and Arduino. I will be honest about my gaps: I have not yet managed facility H&amp;S or periodic asset maintenance schedules, or led mechanical installations of driveline and transmission rigs. I learn new systems and procedures quickly, work well across engineering and technician teams, and would be proud to support Ricardo's test operations in Leamington Spa.",
 "Thank you for reading. I would welcome the chance to talk about the role.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])

