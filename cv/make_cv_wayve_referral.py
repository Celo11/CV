"""Build the two-page referral PDF from the editable Markdown beside this script."""

from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Muhammet_Celal_Gokalp_CV_Wayve_Referral.md"
OUTPUT = SOURCE.with_suffix(".pdf")
NAVY = colors.HexColor("#14213D")
TEAL = colors.HexColor("#1F7A8C")
GREY = colors.HexColor("#555555")
WIDTH, HEIGHT = A4
MARGIN = 16 * mm

BODY = ParagraphStyle(
    "Body",
    fontName="Helvetica",
    fontSize=9.6,
    leading=13.2,
    textColor=colors.HexColor("#222222"),
    spaceAfter=4,
)
NAME = ParagraphStyle(
    "Name",
    parent=BODY,
    fontName="Helvetica-Bold",
    fontSize=23,
    leading=28,
    textColor=NAVY,
    spaceAfter=4,
)
SUBTITLE = ParagraphStyle(
    "Subtitle",
    parent=BODY,
    fontSize=10.2,
    leading=14,
    textColor=TEAL,
)
CONTACT = ParagraphStyle(
    "Contact",
    parent=BODY,
    fontSize=9,
    leading=12,
    textColor=GREY,
    spaceAfter=2,
)
SECTION = ParagraphStyle(
    "Section",
    parent=BODY,
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=14,
    textColor=NAVY,
    spaceBefore=9,
    spaceAfter=3,
    keepWithNext=True,
)
ROLE = ParagraphStyle(
    "Role",
    parent=BODY,
    fontName="Helvetica-Bold",
    fontSize=10,
    leading=13,
    spaceBefore=4,
    spaceAfter=1,
    keepWithNext=True,
)
EMPLOYER = ParagraphStyle(
    "Employer",
    parent=BODY,
    fontSize=9.1,
    leading=12,
    textColor=TEAL,
    spaceAfter=4,
    keepWithNext=True,
)
BULLET = ParagraphStyle(
    "Bullet",
    parent=BODY,
    leftIndent=10,
    bulletIndent=0,
    spaceAfter=4,
    alignment=TA_LEFT,
)


def markup(text: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escape(text))


def page_details(canvas: Canvas, document: SimpleDocTemplate) -> None:
    canvas.saveState()
    if document.page > 1:
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(GREY)
        canvas.drawString(
            MARGIN, HEIGHT - 11 * mm, "Muhammet Celal Gokalp"
        )
    canvas.setStrokeColor(TEAL)
    canvas.setLineWidth(0.6)
    canvas.line(MARGIN, 13 * mm, WIDTH - MARGIN, 13 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawRightString(
        WIDTH - MARGIN, 9 * mm, f"{document.page} / 2"
    )
    canvas.restoreState()


def build() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    if sum(line == "---" for line in lines) != 1:
        raise ValueError("The CV must have exactly one explicit page break.")

    story = []
    in_header = True
    for line in lines:
        if not line.strip():
            continue
        if line == "---":
            story.append(PageBreak())
        elif line.startswith("# "):
            story.append(Paragraph(markup(line[2:]), NAME))
        elif line.startswith("## "):
            if in_header:
                story.append(Spacer(1, 3))
            in_header = False
            story.append(Paragraph(markup(line[3:].upper()), SECTION))
            story.append(
                HRFlowable(
                    width="100%",
                    thickness=0.8,
                    color=TEAL,
                    spaceAfter=5,
                )
            )
        elif line.startswith("### "):
            story.append(Paragraph(markup(line[4:]), ROLE))
        elif line.startswith("- "):
            story.append(Paragraph(markup(line[2:]), BULLET, bulletText="-"))
        elif in_header:
            if line.startswith("linkedin.com/"):
                url = escape("https://" + line, quote=True)
                story.append(
                    Paragraph(f'<link href="{url}">{escape(line)}</link>', CONTACT)
                )
            elif line.startswith("ADAS &"):
                story.append(Paragraph(markup(line), SUBTITLE))
            else:
                story.append(Paragraph(markup(line), CONTACT))
        elif line.startswith("**") and line.endswith("**"):
            story.append(Paragraph(markup(line), EMPLOYER))
        else:
            story.append(Paragraph(markup(line), BODY))

    document = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        title="Muhammet Celal Gokalp - ADAS and Automated Driving",
        author="Muhammet Celal Gokalp",
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=16 * mm,
        bottomMargin=18 * mm,
        pageCompression=1,
    )
    document.build(story, onFirstPage=page_details, onLaterPages=page_details)
    if document.page != 2:
        raise ValueError(f"Expected two pages, generated {document.page}.")
    print(f"Created {OUTPUT} ({document.page} A4 pages)")


if __name__ == "__main__":
    build()
