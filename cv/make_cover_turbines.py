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
    c.drawString(M, H-23.5*mm, "Mechanical, Systems & Test Engineer  |  Rotating Machinery, Controls & HiL Validation")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Immediately available")
    c.restoreState()

txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.6, leading=13.8, textColor=colors.HexColor("#222222"), spaceAfter=7.5)
doc = BaseDocTemplate("Muhammet_Celal_Gokalp_Cover_Letter_Turbines.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - Cover Letter", author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 12*mm, cw, H-HB-2*mm-18*mm, 0,0,0,0)], onPage=header)])

paras = [
 "8 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Mechanical, Systems &amp; Test Engineering Application</b>",
 "I am applying to join your engineering team. I hold a BSc in Mechanical Engineering and an MSc in Sustainable Automotive Engineering from WMG, University of Warwick, and have eight years of experience in systems engineering, control validation, HiL / test-bed testing and hands-on fault-finding. I am moving from automotive into the turbine and energy sector, and live in Coventry with immediate availability.",
 "I will be honest about my gap first: my industry experience so far is in automotive powertrains, rotating electrical machines, control systems and test rigs rather than gas, steam or wind turbines. However, the core engineering work is what I have done throughout my degree and career. For my Warwick MSc dissertation I designed a test to find the thermal model variables of an electric motor stator—specifying type-K thermocouple placement, the test enclosure and the test method—and used MotorCAD's thermal network, Portunus and MATLAB / Simulink to model the heat paths. At the LEVC (London Taxi) factory with AVL, I inspected about 20 returned faulty range-extender generators, carrying out multimeter checks at connector pins (phase-to-phase resistance, continuity), powering the control unit from a bench supply to download fault logs via the supplier's tool, and sending the measurements and data to the supplier for root cause analysis.",
 "At AVL I also spent two years on-site at Jaguar Land Rover as feature owner for three safety-related features, writing use cases, system state diagrams, module input/output signal lists and requirements in DOORS and MKS Integrity (ASPICE V-model), writing ISO 26262 safety requirements, taking part in an FMEA, and validating on dSPACE HiL and ViL rigs. On AVL's DrivingCube dyno test-bed project, I calibrated a MATLAB / Simulink model against real recordings and swept PID controller gains. At FiveAI / Bosch I led a team of five engineers for a year, defined performance KPIs across 1,000+ hours of test data, diagnosed error logs across APIs and simulation tools, and built Python tools and reporting pipelines. Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy, so I am immediately available with no notice period.",
 "Outside work I repair my own cars, use a multimeter, torque wrench, calipers and micrometers, and at university our team designed, built and wired a 6-DOF motion platform in SolidWorks, MATLAB and Arduino. I love hands-on engineering, learn new systems quickly, and would welcome the chance to talk about how I can contribute to your team.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
