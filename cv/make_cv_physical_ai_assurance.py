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


body = style("body", fontSize=8.05, leading=10.3, textColor=colors.HexColor("#222222"))
bullet = style("bullet", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.55)
line = style("line", parent=body, spaceAfter=0.7)
section_style = style(
    "section",
    font="Helvetica-Bold",
    fontSize=9.8,
    leading=11.2,
    textColor=NAVY,
    spaceBefore=2.5,
)
role_style = style(
    "role", font="Helvetica-Bold", fontSize=9.0, leading=10.5, textColor=colors.black
)
org_style = style(
    "org", font="Helvetica-Bold", fontSize=8.3, leading=10.0, textColor=ACC
)
meta_style = style(
    "meta", font="Helvetica-Oblique", fontSize=7.8, leading=10.0, textColor=GREY, alignment=2
)
location_style = style(
    "location", fontSize=7.8, leading=10.0, textColor=GREY, alignment=2
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
    canvas.setFont("Helvetica", 9.7)
    canvas.setFillColor(colors.HexColor("#A8D5E2"))
    canvas.drawString(
        M, H - 21 * mm, "Physical AI Assurance  |  Robotics, Validation & Test Automation"
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
        "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   English (C2)",
    )
    canvas.restoreState()


OUT = Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_Physical_AI_Assurance.pdf"
CONTENT_WIDTH = W - 2 * M
doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    title="Muhammet Celal Gokalp - Physical AI Assurance Engineer CV",
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
        HRFlowable(width="100%", thickness=1.0, color=ACC, spaceBefore=0.7, spaceAfter=1.6),
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
        KeepTogether([heading(role, dates, organisation, location), Spacer(1, 0.7), items[0]]),
        *items[1:],
        Spacer(1, 1.2),
    ]


def skills_table(rows):
    table = Table(
        [[Paragraph(f"<b>{label}</b>", body), Paragraph(detail, body)] for label, detail in rows],
        colWidths=[CONTENT_WIDTH * 0.24, CONTENT_WIDTH * 0.76],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [LIGHT, colors.white]),
                ("TOPPADDING", (0, 0), (-1, -1), 1.1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.1),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


content = []
content += section("Profile")
content.append(
    Paragraph(
        "Validation and systems engineer with nearly 8 years assessing complex, safety-related "
        "ADAS and automated-driving behaviour. Experienced in designing scenario-based tests, "
        "defining KPIs and pass/fail criteria, analysing large test datasets, investigating "
        "boundary failures and turning findings into engineering actions. Currently exploring "
        "Physical AI through a personal home-tidying robot project using an LLM/VLA-based learned "
        "system. Combines practical robotics curiosity with structured automotive assurance, "
        "Python-assisted tooling and technical coaching.",
        body,
    )
)

content += section("Robotics & Physical AI Project")
content.append(
    Paragraph(
        "<b>Home-tidying robot | Personal project | Recent two-week project:</b> Exploring how an "
        "LLM/VLA-based learned system can be applied to a home-tidying robot. Building practical "
        "understanding of Physical AI behaviour and the challenges of evaluating an AI-driven "
        "system in a real-world task context.",
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
        "<b>Scenario-based validation:</b> Created 120+ parameterised OpenSCENARIO 2 scenarios "
        "generating thousands of test cases for an L4 automated-driving stack; defined KPIs and "
        "pass/fail criteria and analysed more than 1,000 hours of system data.",
        "<b>Test automation & benchmarks:</b> Built Python tools with AI assistance, including a "
        "JSON parameter GUI, uploader and dashboard pipelines, to make test evidence and "
        "performance results more repeatable and accessible.",
        "<b>AI and simulation integration:</b> Worked with the project simulation toolchain and "
        "triaged faults across APIs, maps, tools and simulation. At user level, ran a ROS 1 "
        "Noetic setup with a VLA model in Docker, rosbridge and an orchestrator/simulator "
        "interface; did not write ROS nodes.",
        "<b>Technical coaching:</b> Led five engineers for a year as technical lead, teaching "
        "evaluation methods and reviewing work. Trained Volkswagen Group partner engineers on "
        "the simulation toolchain.",
    ],
)
content += job(
    "ADAS Systems Engineer (Feature Owner)",
    "AVL Powertrain UK",
    "Jaguar Land Rover, UK",
    "11/2018 – 10/2021",
    [
        "<b>System safety & test design:</b> Owned validation for three corner-radar features; "
        "translated customer needs into use cases, system states, requirements and test cases "
        "using DOORS and MKS Integrity.",
        "<b>Failure investigation:</b> When Rear Cross Traffic Alert passed HiL testing but "
        "triggered late on the proving ground, designed boundary tests, synchronised camera, "
        "CAN and radar logs in Vector CANoe / CANape, worked with the supplier and verified "
        "its calibration change on site.",
        "<b>Validation & safety practice:</b> Verified features in vehicles and on proving "
        "grounds, supported AVL's DrivingCube ViL test bed, tracked defects in RTC / RQM, "
        "wrote ISO 26262 safety requirements and took part in an FMEA.",
    ],
)

content += section("Education")
content.append(
    Paragraph(
        "<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick (2017–2018, "
        "2:1 Merit). <b>BSc Mechanical Engineering</b>, Ege University (2011–2017). BSc team "
        "project built a 6-DOF Stewart platform with servo wiring and Arduino control.",
        line,
    )
)

content += section("Skills")
content.append(
    KeepTogether(
        [
            skills_table(
                [
                    (
                        "Assurance & validation",
                        "Scenario design, requirements traceability, test cases, KPIs, performance benchmarking, "
                        "regression analysis, boundary testing, root-cause investigation",
                    ),
                    (
                        "Robotics & AI",
                        "LLM/VLA-based personal robot project; user-level ROS 1, Docker, rosbridge and "
                        "simulator/orchestrator integration; no ROS node development",
                    ),
                    (
                        "Automation & analysis",
                        "Python (AI-assisted tools), OpenSCENARIO 2, MATLAB / Simulink, Vector CANoe / CANape, "
                        "IPG CarMaker, KPI dashboards",
                    ),
                    (
                        "Safety & teamwork",
                        "ISO 26262 safety requirements, FMEA participation, safety-related automotive systems, "
                        "technical mentoring, customer and cross-functional collaboration",
                    ),
                    (
                        "Additional",
                        "English (C2), Turkish (native), British citizen, full UK driving licence",
                    ),
                ]
            )
        ]
    )
)

doc.build(content)
