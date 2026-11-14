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


body = style("body", fontSize=8.1, leading=10.4, textColor=colors.HexColor("#222222"))
bullet = style("bullet", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.6)
line = style("line", parent=body, spaceAfter=0.8)
section_style = style(
    "section",
    font="Helvetica-Bold",
    fontSize=9.9,
    leading=11.4,
    textColor=NAVY,
    spaceBefore=2.8,
)
role_style = style(
    "role", font="Helvetica-Bold", fontSize=9.1, leading=10.7, textColor=colors.black
)
org_style = style(
    "org", font="Helvetica-Bold", fontSize=8.4, leading=10.2, textColor=ACC
)
meta_style = style(
    "meta", font="Helvetica-Oblique", fontSize=7.9, leading=10.2, textColor=GREY, alignment=2
)
location_style = style(
    "location", fontSize=7.9, leading=10.2, textColor=GREY, alignment=2
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
    canvas.setFont("Helvetica", 9.8)
    canvas.setFillColor(colors.HexColor("#A8D5E2"))
    canvas.drawString(
        M, H - 21 * mm, "EV & Automotive Systems  |  Engineering Delivery & Operations"
    )
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 8.0)
    canvas.drawString(
        M,
        H - 26.8 * mm,
        "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, UK   |   British citizen",
    )
    canvas.drawString(
        M,
        H - 30.8 * mm,
        "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Available for travel",
    )
    canvas.restoreState()


OUT = (
    Path(__file__).resolve().parent
    / "Muhammet_Celal_Gokalp_CV_Waymo_Charging_Infrastructure.pdf"
)
CONTENT_WIDTH = W - 2 * M
doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    title="Muhammet Celal Gokalp - Waymo Charging Infrastructure CV",
    author="Muhammet Celal Gokalp",
    leftMargin=M,
    rightMargin=M,
)
doc.addPageTemplates(
    [
        PageTemplate(
            "first",
            [Frame(M, 6 * mm, CONTENT_WIDTH, H - HB - 2 * mm - 8 * mm, 0, 0, 0, 0)],
            onPage=header,
        )
    ]
)


def section(title):
    return [
        Paragraph(title.upper(), section_style),
        HRFlowable(width="100%", thickness=1.0, color=ACC, spaceBefore=0.7, spaceAfter=1.8),
    ]


def heading(role, dates, organisation, location):
    table = Table(
        [
            [Paragraph(role, role_style), Paragraph(dates, meta_style)],
            [Paragraph(organisation, org_style), Paragraph(location, location_style)],
        ],
        colWidths=[CONTENT_WIDTH * 0.68, CONTENT_WIDTH * 0.32],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.4),
            ]
        )
    )
    return table


def job(role, organisation, location, dates, bullets):
    items = [Paragraph(text, bullet, bulletText="•") for text in bullets]
    return [
        KeepTogether([heading(role, dates, organisation, location), Spacer(1, 0.8), items[0]]),
        *items[1:],
        Spacer(1, 1.5),
    ]


def skills_table(rows):
    table = Table(
        [[Paragraph(f"<b>{label}</b>", body), Paragraph(detail, body)] for label, detail in rows],
        colWidths=[CONTENT_WIDTH * 0.25, CONTENT_WIDTH * 0.75],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [LIGHT, colors.white]),
                ("TOPPADDING", (0, 0), (-1, -1), 1.2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


content = []
content += section("Profile")
content.append(
    Paragraph(
        "Mechanical and automotive engineer with 8 years coordinating technical delivery, "
        "validation and supplier/customer issue resolution across AVL Powertrain and FiveAI / "
        "Bosch. Led a five-engineer technical team, built KPI reporting from 1,000+ hours of "
        "system data, and supported electric-vehicle-related work through electric-bus powertrain "
        "sizing, electric-motor thermal-test design and returned-generator diagnostics. Brings "
        "structured project execution, cross-functional coordination and a strong sustainability "
        "interest. Experience is adjacent to EV infrastructure: no direct DC fast-charger "
        "deployment, utility interconnection, permitting or charging-network operations.",
        body,
    )
)

content += section("Experience")
content += job(
    "Lead Application Engineer (Solutions & Integration)",
    "FiveAI / Bosch",
    "Cambridge, UK",
    "10/2021 – 11/2026",
    [
        "<b>Technical delivery & coordination:</b> Led five engineers for a year (technical lead, "
        "not line manager), dividing work between scenario development and evaluation, teaching "
        "the team and reviewing outcomes against requirements.",
        "<b>Cross-functional and customer interface:</b> Trained Volkswagen Group partner "
        "engineers on the ADA simulation toolchain and helped form the Simulation EcoSystem "
        "solutions team. Triaged issues across partner tools, maps, APIs and simulation, "
        "coordinating with the engineering teams responsible for fixes.",
        "<b>Performance reporting:</b> Defined KPIs and pass/fail criteria, analysed 1,000+ hours "
        "of data, and compared software versions to find regressions and report technical status.",
        "<b>Process improvement:</b> Built Python tools with AI assistance, including an uploader "
        "and data pipelines into dashboards, to make test evidence and results easier to use.",
    ],
)
content += job(
    "ADAS Systems Engineer (Feature Owner)",
    "AVL Powertrain UK",
    "Jaguar Land Rover, UK",
    "11/2018 – 10/2021",
    [
        "<b>Programme and supplier coordination:</b> Owned three corner-radar features, acting "
        "between JLR, AVL and the Tier 1 radar supplier. Translated customer needs into "
        "requirements, system states, interface signals and traceable test cases.",
        "<b>Operational problem-solving:</b> When an alert passed HiL but triggered late on the "
        "proving ground, planned boundary tests, synchronised camera, CAN and radar logs in "
        "Vector CANoe / CANape, agreed a supplier calibration change and verified it on site.",
        "<b>Field equipment diagnostics:</b> At the LEVC factory, inspected about 20 returned "
        "range-extender generators using multimeter checks and low-voltage bench-supply log "
        "retrieval; provided results to developers and suppliers for investigation.",
        "<b>System controls & records:</b> Authored requirements, state diagrams, interface "
        "definitions and test cases in DOORS / MKS Integrity; tracked defects in RTC / RQM and "
        "contributed to ISO 26262 requirements and FMEA.",
    ],
)
content.append(
    Paragraph(
        "<b>Mechanical Engineering Intern</b>, TEMSA Global (2014): calculated power and torque "
        "requirements for an electric-bus powertrain using MATLAB / Simulink; supported production "
        "quality.",
        line,
    )
)

content += section("Education & Relevant Project Work")
content.append(
    Paragraph(
        "<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick (2017–2018, "
        "2:1 Merit). Coursework included hybrid and electric vehicle systems. Dissertation: "
        "designed a test method and thermocouple layout for electric-motor stator thermal "
        "characterisation (MotorCAD, MATLAB / Simulink).",
        line,
    )
)
content.append(
    Paragraph(
        "<b>BSc Mechanical Engineering</b>, Ege University (2011–2017). Team-designed and built "
        "a 6-DOF Stewart platform; wired servo actuators and used Arduino for commanded movement.",
        line,
    )
)

content += section("Relevant Skills")
content.append(
    KeepTogether(
        [
            skills_table(
                [
                    (
                        "Delivery & leadership",
                        "Technical work planning, cross-functional coordination, customer and supplier liaison, "
                        "team mentoring, status and KPI reporting",
                    ),
                    (
                        "EV & equipment",
                        "Electric-bus powertrain sizing, electric-motor thermal test design, generator fault "
                        "inspection, multimeter, low-voltage bench supply",
                    ),
                    (
                        "Data & engineering",
                        "Python (AI-assisted tools), MATLAB / Simulink, Vector CANoe / CANape, IPG CarMaker, "
                        "DOORS, MKS Integrity, RTC / RQM, Linux, Git",
                    ),
                    (
                        "Infrastructure scope",
                        "No direct DCFC deployment, utility interconnection, permitting, charging asset "
                        "maintenance or capital-budget ownership",
                    ),
                    (
                        "Additional",
                        "British citizen, full UK driving licence, available for travel; English (C2), Turkish (native)",
                    ),
                ]
            )
        ]
    )
)

doc.build(content)
