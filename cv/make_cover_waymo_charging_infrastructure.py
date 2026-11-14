from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
)

NAVY = colors.HexColor("#14213D")
ACC = colors.HexColor("#1F7A8C")
GREY = colors.HexColor("#555555")
W, H = A4
M = 22 * mm
HEADER_HEIGHT = 35 * mm


def style(name, **kwargs):
    return ParagraphStyle(name, fontName=kwargs.pop("font", "Helvetica"), **kwargs)


body = style("body", fontSize=10.2, leading=15.2, textColor=colors.HexColor("#222222"), spaceAfter=11)
contact = style("contact", fontSize=8.5, leading=12, textColor=GREY)
date_style = style("date", fontSize=9.5, leading=13, textColor=GREY)
subject = style(
    "subject",
    font="Helvetica-Bold",
    fontSize=12,
    leading=16,
    textColor=NAVY,
    alignment=TA_LEFT,
    spaceBefore=5,
    spaceAfter=14,
)


def header(canvas, _doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, H - HEADER_HEIGHT, W, HEADER_HEIGHT, 0, 1)
    canvas.setFillColor(ACC)
    canvas.rect(0, H - HEADER_HEIGHT - 2 * mm, W, 2 * mm, 0, 1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 20)
    canvas.drawString(M, H - 15 * mm, "Muhammet Celal Gokalp")
    canvas.setFont("Helvetica", 9.5)
    canvas.setFillColor(colors.HexColor("#A8D5E2"))
    canvas.drawString(M, H - 22 * mm, "EV & Automotive Systems  |  Engineering Delivery & Operations")
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 8.2)
    canvas.drawString(M, H - 29 * mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK")
    canvas.restoreState()


OUT = (
    Path(__file__).resolve().parent
    / "Muhammet_Celal_Gokalp_Cover_Letter_Waymo_Charging_Infrastructure.pdf"
)
doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    title="Muhammet Celal Gokalp - Waymo Cover Letter",
    author="Muhammet Celal Gokalp",
    leftMargin=M,
    rightMargin=M,
    topMargin=HEADER_HEIGHT + 10 * mm,
    bottomMargin=20 * mm,
)
doc.addPageTemplates(
    [
        PageTemplate(
            "letter",
            [Frame(M, 20 * mm, W - 2 * M, H - HEADER_HEIGHT - 10 * mm - 20 * mm, 0, 0, 0, 0)],
            onPage=header,
        )
    ]
)

story = [
    Paragraph("11 November 2026", date_style),
    Spacer(1, 7 * mm),
    Paragraph("Re: EV Charging Infrastructure Deployment and Operations", subject),
    Paragraph("Dear Waymo Hiring Team,", body),
    Paragraph(
        "Waymo’s mission to make mobility safer and more accessible depends not only on capable "
        "vehicles, but also on dependable infrastructure behind them. I am interested in bringing "
        "my experience coordinating complex automotive engineering work, resolving supplier and "
        "customer issues, and turning operational data into clear performance measures to this "
        "infrastructure role.",
        body,
    ),
    Paragraph(
        "Across eight years at AVL Powertrain and FiveAI / Bosch, I have worked across customer, "
        "supplier and mechanical, electrical and software teams. At Jaguar Land Rover, I owned "
        "three radar-feature workstreams from requirements through vehicle testing. When a system "
        "passed rig testing but behaved differently on the proving ground, I designed boundary "
        "tests, synchronised camera, CAN and radar logs, coordinated a supplier calibration change "
        "and verified the result on site. At the LEVC factory, I also inspected returned generators, "
        "performed multimeter and low-voltage bench checks, and provided evidence to suppliers for "
        "investigation.",
        body,
    ),
    Paragraph(
        "At FiveAI / Bosch, I trained Volkswagen Group partner engineers, helped establish a "
        "cross-functional solutions team and led five engineers as a technical lead. I defined "
        "KPIs and pass/fail criteria, analysed more than 1,000 hours of system data, and built "
        "Python-assisted reporting tools. My electrification background includes electric-bus "
        "powertrain sizing at TEMSA and an MSc project designing a thermal-characterisation test "
        "for an electric-motor stator.",
        body,
    ),
    Paragraph(
        "I want to be transparent that I have not led DC fast-charger deployments, utility "
        "interconnections, permitting, charging-network maintenance or capital-budget ownership. "
        "My experience is adjacent: engineering delivery, evidence-led problem solving, technical "
        "coordination and EV-related systems work. I would bring those strengths, a sustainability "
        "motivation and a disciplined approach to learning the infrastructure-specific standards "
        "and delivery processes.",
        body,
    ),
    Paragraph(
        "I am a British citizen, hold a full UK driving licence and am available to travel. I would "
        "welcome the opportunity to discuss how my automotive engineering and technical delivery "
        "experience could contribute to Waymo’s charging infrastructure programme.",
        body,
    ),
    Paragraph("Yours sincerely,", body),
    Spacer(1, 5 * mm),
    Paragraph("<b>Muhammet Celal Gokalp</b>", body),
]

doc.build(story)
