from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer

NAVY = colors.HexColor("#14213D")
ACC = colors.HexColor("#1F7A8C")
W, H = A4
M = 16 * mm
HEADER_HEIGHT = 38 * mm


def header(canvas, _doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, H - HEADER_HEIGHT, W, HEADER_HEIGHT, 0, 1)
    canvas.setFillColor(ACC)
    canvas.rect(0, H - HEADER_HEIGHT - 2 * mm, W, 2 * mm, 0, 1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 23)
    canvas.drawString(M, H - 17 * mm, "Muhammet Celal Gokalp")
    canvas.setFont("Helvetica", 10.2)
    canvas.setFillColor(colors.HexColor("#A8D5E2"))
    canvas.drawString(
        M, H - 23.5 * mm, "ADAS Feature Lead  |  Feature Ownership, Requirements & Validation"
    )
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 8.3)
    canvas.drawString(
        M,
        H - 30 * mm,
        "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK",
    )
    canvas.drawString(
        M,
        H - 34 * mm,
        "linkedin.com/in/celal-gökalp-4616ab122   |   British citizen   |   Immediately available",
    )
    canvas.restoreState()


letter_style = ParagraphStyle(
    "letter",
    fontName="Helvetica",
    fontSize=9.6,
    leading=13.8,
    textColor=colors.HexColor("#222222"),
    spaceAfter=8,
)

OUT = (
    Path(__file__).resolve().parent
    / "Muhammet_Celal_Gokalp_Cover_Letter_Aston_Martin_ADAS_Feature_Lead.pdf"
)
doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    title="Muhammet Celal Gokalp - Aston Martin ADAS Feature Lead Cover Letter",
    author="Muhammet Celal Gokalp",
    leftMargin=M,
    rightMargin=M,
    topMargin=HEADER_HEIGHT + 2 * mm,
    bottomMargin=14 * mm,
)
doc.addPageTemplates(
    [
        PageTemplate(
            "letter",
            [
                Frame(
                    M,
                    14 * mm,
                    W - 2 * M,
                    H - HEADER_HEIGHT - 2 * mm - 14 * mm,
                    0,
                    0,
                    0,
                    0,
                )
            ],
            onPage=header,
        )
    ]
)

paragraphs = [
    "12 November 2026",
    Spacer(1, 4 * mm),
    "<b>Re: ADAS Feature Lead Engineer</b>",
    "Dear Hiring Team,",
    "I am excited to apply for the ADAS Feature Lead Engineer role. Aston Martin is one of the "
    "world’s most beautiful and distinctive car manufacturers, and the opportunity to help shape "
    "the advanced technology behind its future vehicles is especially compelling to me. I would "
    "bring eight years of ADAS and automated-driving experience, with a strong focus on feature "
    "ownership, customer expectations and safe, measurable behaviour.",
    "At AVL, I was the feature owner for three corner-radar functions at Jaguar Land Rover. I "
    "turned broad customer needs into use cases, system-state diagrams, traceable requirements "
    "and test cases in DOORS and MKS Integrity. I also used market research and accumulated "
    "knowledge of customer expectations to help reason about how features should behave and feel, "
    "while keeping safety central. When Rear Cross Traffic Alert behaved differently on the "
    "proving ground than in rig testing, I designed boundary tests, analysed synchronised logs, "
    "worked with the supplier on a calibration change and verified the result on the vehicle.",
    "At FiveAI / Bosch, I translated customer and regulatory expectations into KPIs, supported "
    "Volkswagen Group partner engineers and led a five-person technical team. I enjoy working "
    "across disciplines, resolving difficult delivery issues and keeping decisions tied to "
    "evidence and the end-user experience. My background in ISO 26262 requirements and FMEA "
    "participation further supports my safety-focused approach.",
    "I would be proud to bring this experience and my enthusiasm for Aston Martin to the team, "
    "helping deliver ADAS features that are safe, intuitive and worthy of the vehicles they serve. "
    "Thank you for considering my application. I would welcome the opportunity to discuss my "
    "suitability.",
    "Yours sincerely,",
    "<b>Muhammet Celal Gokalp</b>",
]
doc.build([Paragraph(item, letter_style) if isinstance(item, str) else item for item in paragraphs])
