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
        M, H - 21 * mm, "Senior Applications Engineer  |  Electrification Systems & Integration"
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
        "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Available for UK and international travel",
    )
    canvas.restoreState()


OUT = Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_Evolito.pdf"
CONTENT_WIDTH = W - 2 * M
doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    title="Muhammet Celal Gokalp - Evolito Senior Applications Engineer CV",
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
        "Mechanical engineer with 8 years delivering complex systems across customer, supplier and "
        "cross-functional engineering teams. At AVL, owned three radar-feature integrations at "
        "Jaguar Land Rover, translating needs into requirements and coordinating development, "
        "calibration and vehicle test. At FiveAI / Bosch, trained customer engineers, resolved "
        "integration issues and led a five-person technical team. Brings a strong analytical and "
        "test-led approach, with an MSc project in electric-motor stator thermal characterisation "
        "and earlier electric-bus powertrain sizing. No direct product-development experience with "
        "high-voltage propulsion motors, inverters or battery systems.",
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
        "<b>Technical focal point & customer delivery:</b> Trained Volkswagen Group partner "
        "engineers on the ADA simulation toolchain; co-founded the Simulation EcoSystem solutions "
        "team and acted as a bridge between customer and internal engineering teams.",
        "<b>Cross-functional problem solving:</b> Traced integration issues across APIs, maps, "
        "simulation and partner tools from logs and test evidence, coordinated fixes with the "
        "appropriate teams, and communicated progress and findings.",
        "<b>Technical leadership & delivery:</b> Led five engineers for a year, taught evaluation "
        "methods, coordinated parallel work, and tracked performance and regressions across "
        "1,000+ hours of test data.",
        "<b>Engineering tools:</b> Built Python tools with AI assistance, including a parameter "
        "interface, uploader and dashboard data pipelines; converted requirements into measurable "
        "KPIs and verification scenarios.",
    ],
)
content += job(
    "ADAS Systems Engineer (Feature Owner)",
    "AVL Powertrain UK",
    "Jaguar Land Rover, UK",
    "11/2018 – 10/2021",
    [
        "<b>System requirements & coordination:</b> Owned three corner-radar features, working "
        "between customer, supplier and mechanical, electrical and software teams. Turned customer "
        "needs into use cases, system states, interface signals and traceable requirements.",
        "<b>Development, calibration & test:</b> Authored per-state test cases and verified features "
        "in vehicles, on proving grounds and in collaboration with the HiL team. When a radar alert "
        "passed HiL but triggered late on track, designed boundary tests, synchronised camera, CAN "
        "and radar logs in Vector CANoe / CANape, and verified the supplier's calibration fix.",
        "<b>Test setup & hardware diagnostics:</b> Fitted external GNSS for ground-truth logging "
        "on AVL's DrivingCube vehicle-in-the-loop test bed; performed multimeter checks and "
        "low-voltage bench-supply diagnostics on about 20 returned LEVC generators and provided "
        "evidence to suppliers.",
        "<b>System safety & documentation:</b> Produced use cases, state diagrams, interface "
        "definitions, requirements and test records in DOORS / MKS Integrity; managed defects "
        "through RTC / RQM and contributed to ISO 26262 requirements and FMEA.",
    ],
)
content.append(
    Paragraph(
        "<b>Mechanical Engineering Intern</b>, TEMSA Global (2014): sized power and torque needs "
        "for an electric-bus powertrain using MATLAB / Simulink; supported production quality.",
        line,
    )
)
content.append(
    Paragraph(
        "<b>Part-Time Teacher & Programme Planner</b>, Space Camp Turkey (12/2013 – 01/2017): "
        "taught science and space technology to students aged 9–16.",
        line,
    )
)

content += section("Education & Relevant Project Work")
content.append(
    Paragraph(
        "<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick (2017–2018, "
        "2:1 Merit). Designed an experimental test to characterise an electric-motor stator's "
        "thermal model, including thermocouple placement, enclosure and test method "
        "(MotorCAD, MATLAB / Simulink).",
        line,
    )
)
content.append(
    Paragraph(
        "<b>BSc Mechanical Engineering</b>, Ege University (2011–2017). Team-built a 6-DOF "
        "Stewart platform; wired servo actuators and used Arduino to command and check signals.",
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
                        "Systems & delivery",
                        "System requirements, interfaces, functional states, traceability, cross-functional "
                        "coordination, customer and supplier communication, technical leadership",
                    ),
                    (
                        "Mechatronics & test",
                        "Mechanical/electrical integration, sensor systems, calibration support, test planning, "
                        "data acquisition and analysis, multimeter, low-voltage bench supply, GNSS setup",
                    ),
                    (
                        "Tools",
                        "Python (AI-assisted tooling), MATLAB / Simulink, Vector CANoe / CANape, IPG CarMaker, "
                        "Arduino, DOORS, MKS Integrity, Linux, Git",
                    ),
                    (
                        "Electrification",
                        "Electric-bus powertrain sizing and electric-motor stator thermal test design; no direct "
                        "industry development of HV motors, inverters or battery systems",
                    ),
                    (
                        "Additional",
                        "British citizen, full UK driving licence, available for UK and international travel; "
                        "English (C2), Turkish (native)",
                    ),
                ]
            )
        ]
    )
)

doc.build(content)
