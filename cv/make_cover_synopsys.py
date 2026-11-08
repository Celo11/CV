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
    c.drawString(M, H-23.5*mm, "Field Support & Test / Validation Engineer  |  Hands-on Hardware, Linux & Customer Sites")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British & Turkish citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122   |   Happy to travel UK & abroad   |   Immediately available")
    c.restoreState()

txt = ParagraphStyle("t", fontName="Helvetica", fontSize=9.8, leading=14.2, textColor=colors.HexColor("#222222"), spaceAfter=8)
doc = BaseDocTemplate("Muhammet_Celal_Gokalp_Cover_Letter_Synopsys.pdf", pagesize=A4,
                      title="Muhammet Celal Gokalp - Cover Letter", author="Muhammet Celal Gokalp",
                      leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 12*mm, cw, H-HB-2*mm-18*mm, 0,0,0,0)], onPage=header)])

paras = [
 "6 November 2026",
 "Dear Hiring Team,",
 "<b>Re: Field Support / Test &amp; Validation Engineer (Hardware-Assisted Verification), Synopsys</b>",
 "I am applying for the Field Support role in your Hardware-Assisted Verification (HAV) team. I am a mechanical engineer with eight years in test, validation and customer-facing support, and I want to build the next stage of my career around hands-on hardware work at customer sites.",
 "I will be honest about my gaps first: my experience so far is in automotive electronics, test rigs and automated driving simulation rather than semiconductor emulation or prototyping hardware, and while I have used Linux as my main workstation for five years and write Python tools, I have not written bash or tcsh scripts beyond everyday terminal use. I learn new hardware and tools quickly, and I enjoy getting into the lab to understand how a system fits together.",
 "At AVL I spent two years on-site at Jaguar Land Rover as feature owner for three corner-radar features, running tests on dSPACE HiL and ViL rigs, in vehicles and on the proving ground, and working between the customer, AVL and the hardware supplier. When a module failed to activate in vehicle tests, I read the fault codes, checked fuses, and powered modules on a 12 V bench supply to find the cause. At the LEVC (London Taxi) factory I inspected about 20 returned faulty range-extender generators, carrying out multimeter checks at connector pins, powering the control unit from a bench supply to download logs with the supplier's tool, and sending the data and reports to the supplier for root cause analysis.",
 "At FiveAI / Bosch I trained Volkswagen Group partner engineers on our simulation toolchain and was a founding member of the Simulation EcoSystem solutions team. I diagnosed problems across partners' toolchains and tools from the error logs between APIs and simulation, worked in Linux in a dev container, used SSH to reach our GPU cluster, and built Python tools and reporting pipelines across more than 1,000 hours of test data. Outside work I build my own desktop PCs (chassis prep, mounting boards and parts, cabling), repair my own cars with a multimeter and workshop manuals, and at university our team designed, built and wired a 6-DOF motion platform in SolidWorks, MATLAB and Arduino.",
 "Following Volkswagen Group's withdrawal from the project, my role at Bosch ended by redundancy today, so I am immediately available. I hold British and Turkish citizenship, have a full UK driving licence, and am happy to travel across the UK and internationally. Thank you for reading, and I would welcome the chance to talk about the role.",
 "Yours sincerely,",
 "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(p, txt) for p in paras])
