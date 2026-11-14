from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

NAVY = colors.HexColor("#14213D")
ACC = colors.HexColor("#1F7A8C")
GREY = colors.HexColor("#555555")
LIGHT = colors.HexColor("#E8F1F4")
W, H = A4
M = 14 * mm
HB = 34 * mm


def style(name, **kwargs):
    return ParagraphStyle(name, fontName=kwargs.pop("font", "Helvetica"), **kwargs)


body = style("body", fontSize=8.2, leading=10.6, textColor=colors.HexColor("#222222"))
bullet = style("bullet", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.7)
line = style("line", parent=body, spaceAfter=1.0)
section_style = style(
    "section",
    font="Helvetica-Bold",
    fontSize=10.0,
    leading=11.6,
    textColor=NAVY,
    spaceBefore=3.0,
)
role_style = style(
    "role", font="Helvetica-Bold", fontSize=9.2, leading=10.8, textColor=colors.black
)
org_style = style(
    "org", font="Helvetica-Bold", fontSize=8.5, leading=10.4, textColor=ACC
)
meta_style = style(
    "meta", font="Helvetica-Oblique", fontSize=8.0, leading=10.4, textColor=GREY, alignment=2
)
location_style = style(
    "location", fontSize=8.0, leading=10.4, textColor=GREY, alignment=2
)


def header(canvas, _doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, H - HB, W, HB, 0, 1)
    canvas.setFillColor(ACC)
    canvas.rect(0, H - HB - 2 * mm, W, 2 * mm, 0, 1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 21)
    canvas.drawString(M, H - 15 * mm, "Muhammet Celal Gokalp")
    canvas.setFont("Helvetica", 10)
    canvas.setFillColor(colors.HexColor("#A8D5E2"))
    canvas.drawString(
        M, H - 21 * mm, "Senior Applications Engineer  |  Customer Integration & Hardware Validation"
    )
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 8.0)
    canvas.drawString(
        M,
        H - 26.8 * mm,
        "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK   |   British & Turkish citizen",
    )
    canvas.drawString(
        M,
        H - 30.8 * mm,
        "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Available for international travel",
    )
    canvas.restoreState()


OUT = Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_Senior_Applications_Engineer.pdf"
MARGIN_WIDTH = W - 2 * M
doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    title="Muhammet Celal Gokalp - Senior Applications Engineer CV",
    author="Muhammet Celal Gokalp",
    leftMargin=M,
    rightMargin=M,
)
doc.addPageTemplates(
    [
        PageTemplate(
            "first",
            [Frame(M, 6 * mm, MARGIN_WIDTH, H - HB - 2 * mm - 8 * mm, 0, 0, 0, 0)],
            onPage=header,
        )
    ]
)


def section(title):
    return [
        Paragraph(title.upper(), section_style),
        HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.8, spaceAfter=2),
    ]


def heading(role, dates, organisation, location):
    table = Table(
        [
            [Paragraph(role, role_style), Paragraph(dates, meta_style)],
            [Paragraph(organisation, org_style), Paragraph(location, location_style)],
        ],
        colWidths=[MARGIN_WIDTH * 0.68, MARGIN_WIDTH * 0.32],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
            ]
        )
    )
    return table


def job(role, organisation, location, dates, bullets):
    items = [Paragraph(text, bullet, bulletText="•") for text in bullets]
    return [
        KeepTogether([heading(role, dates, organisation, location), Spacer(1, 1), items[0]]),
        *items[1:],
        Spacer(1, 2),
    ]


def skills_table(rows):
    table = Table(
        [[Paragraph(f"<b>{label}</b>", body), Paragraph(detail, body)] for label, detail in rows],
        colWidths=[MARGIN_WIDTH * 0.24, MARGIN_WIDTH * 0.76],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [LIGHT, colors.white]),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


content = []
content += section("Professional Summary")
content.append(
    Paragraph(
        "Customer-facing applications and systems engineer with 8 years supporting complex product "
        "integration across automotive customers, suppliers and engineering teams. At Jaguar Land "
        "Rover, owned three radar-feature integrations from requirements through vehicle validation; "
        "at FiveAI / Bosch, trained Volkswagen Group partner engineers, diagnosed cross-toolchain "
        "issues and led a five-engineer technical team. Hands-on in test setup, sensor-data analysis "
        "and fault-finding, with practical Python tooling and a track record of turning customer "
        "evidence into engineering actions.",
        body,
    )
)

content += section("Work Experience")
content += job(
    "Lead Application Engineer (Solutions & Integration)",
    "FiveAI / Bosch",
    "Cambridge, United Kingdom",
    "10/2021 – 11/2026",
    [
        "<b>Customer integration & enablement:</b> Trained Volkswagen Group partner engineers on "
        "FiveAI's simulation toolchain for the ADA project; helped establish the Simulation EcoSystem "
        "solutions team as a founding member.",
        "<b>Technical issue ownership:</b> Diagnosed integration problems across partner toolchains, "
        "maps, APIs and simulation by tracing error logs to their source and coordinating fixes with "
        "the responsible engineering teams.",
        "<b>Technical leadership:</b> Led five engineers for a year, teaching tools and evaluation "
        "methods and coordinating parallel delivery; compared results across software versions to "
        "identify regressions and report status and findings.",
        "<b>Tools & product feedback:</b> Built Python tools with AI assistance (a JSON parameter GUI, uploader and "
        "dashboard data pipelines) and defined customer and regulatory KPIs against 1,000+ hours of "
        "test data, feeding measured performance issues back to developers.",
    ],
)
content += job(
    "ADAS Systems Engineer (Feature Owner)",
    "AVL Powertrain UK",
    "Jaguar Land Rover, UK",
    "11/2018 – 10/2021",
    [
        "<b>Customer-facing design-in:</b> Owned integration of three corner-radar features—Rear "
        "Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash—and acted as the technical link "
        "between JLR, AVL and the radar supplier.",
        "<b>Integration & root-cause analysis:</b> Converted customer needs into requirements, "
        "system states, signal lists and per-state tests. When an alert passed HiL but triggered late "
        "on the proving ground, designed boundary tests, synchronised camera, CAN and radar logs in "
        "Vector CANoe / CANape, and verified the supplier's calibration fix on site.",
        "<b>Hardware test setups & diagnostics:</b> Fitted external GNSS for ground-truth logging "
        "on AVL's DrivingCube vehicle-in-the-loop test bed. At the LEVC factory, inspected about 20 "
        "returned generators using a multimeter and low-voltage bench supply, retrieved logs and "
        "sent evidence to suppliers for investigation.",
        "<b>Development & documentation:</b> Authored use cases, interface definitions, requirements "
        "and test cases in DOORS / MKS Integrity; managed defects through RTC / RQM and contributed "
        "to ISO 26262 safety requirements and FMEA.",
    ],
)
content.append(
    Paragraph(
        "<b>Part-Time Teacher & Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): "
        "taught science and space technology to students aged 9–16, adapting technical explanations "
        "to different audiences.",
        line,
    )
)
content.append(
    Paragraph(
        "<b>Mechanical Engineering Intern</b>, TEMSA Global (2014): supported production quality "
        "and sized an electric-bus powertrain using MATLAB / Simulink.",
        line,
    )
)

content += section("Education")
content.append(
    Paragraph(
        "<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick (2017–2018, "
        "2:1 Merit). Designed an experimental thermal-characterisation test for an electric-motor "
        "stator, including thermocouple placement, enclosure and method.",
        line,
    )
)
content.append(
    Paragraph(
        "<b>BSc Mechanical Engineering</b>, Ege University (2011–2017). Team-designed and built a "
        "6-DOF Stewart platform; wired servo actuators and used Arduino to command and check signals.",
        line,
    )
)

content += section("Technical Skills")
content.append(
    KeepTogether(
        [
            skills_table(
                [
                    (
                        "Customer applications",
                        "Customer and supplier liaison, design-in support, integration triage, technical training, "
                        "cross-team coordination and mentoring",
                    ),
                    (
                        "Hardware & test",
                        "Radar and vehicle systems, sensor logging, GNSS test setup, multimeter, low-voltage "
                        "bench supply, prototype wiring, test planning and validation",
                    ),
                    (
                        "Software & analysis",
                        "Python tooling (AI-assisted), MATLAB / Simulink, Arduino, Vector CANoe / CANape, IPG CarMaker, "
                        "Git, Linux, API/log diagnosis",
                    ),
                    (
                        "Engineering practice",
                        "Requirements, interfaces and traceability; DOORS, MKS Integrity, RTC / RQM; "
                        "ASPICE V-model, ISO 26262, FMEA, customer-facing documentation",
                    ),
                    (
                        "Additional",
                        "English (C2), Turkish (native); British citizen; full UK driving licence; "
                        "available for international travel",
                    ),
                ]
            )
        ]
    )
)

doc.build(content)
