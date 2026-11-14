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
    canvas.setFont("Helvetica", 9.7)
    canvas.setFillColor(colors.HexColor("#A8D5E2"))
    canvas.drawString(
        M, H - 21 * mm, "Senior Test & Validation Engineer  |  Sensor Systems & Test Automation"
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


OUT = (
    Path(__file__).resolve().parent
    / "Muhammet_Celal_Gokalp_CV_Senior_Test_Validation.pdf"
)
CONTENT_WIDTH = W - 2 * M
doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    title="Muhammet Celal Gokalp - Senior Test and Validation Engineer CV",
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
        colWidths=[CONTENT_WIDTH * 0.24, CONTENT_WIDTH * 0.76],
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
        "Test and validation engineer with 8 years defining and executing system-level "
        "verification across sensor-based ADAS and automated-driving systems. Experienced in "
        "turning requirements into structured test cases, analysing synchronised sensor and "
        "vehicle data, finding boundary-condition failures and feeding evidence back to design "
        "and supplier teams. Built Python-assisted test and reporting tools, set KPIs across "
        "1,000+ hours of data, and coached engineers in test methods. Mechanical engineering "
        "background with an MSc project designing an electric-motor stator thermal test.",
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
        "<b>Structured validation:</b> Created 120+ parameterised OpenSCENARIO 2 scenarios "
        "generating thousands of test cases; defined KPIs and pass/fail criteria and analysed "
        "results across 1,000+ hours of data.",
        "<b>Test automation & reporting:</b> Built Python tools with AI assistance, including a "
        "JSON parameter GUI, uploader and dashboard data pipelines, making test execution and "
        "results more repeatable and accessible.",
        "<b>Regression and root-cause analysis:</b> Compared results across software versions "
        "and traced integration faults across APIs, maps, simulation and partner tools, "
        "coordinating fixes with engineering teams.",
        "<b>Coaching & collaboration:</b> Led five engineers for a year as technical lead, "
        "teaching evaluation methods and reviewing test work; trained Volkswagen Group partner "
        "engineers on the simulation toolchain.",
    ],
)
content += job(
    "ADAS Systems Engineer (Feature Owner)",
    "AVL Powertrain UK",
    "Jaguar Land Rover, UK",
    "11/2018 – 10/2021",
    [
        "<b>System-level test design:</b> Owned validation for three corner-radar features. "
        "Converted customer needs into use cases, system states, requirements and test cases "
        "for each operating state using DOORS and MKS Integrity.",
        "<b>Sensor performance investigation:</b> When Rear Cross Traffic Alert passed HiL "
        "testing but triggered late on the proving ground, designed coarse-to-fine boundary "
        "tests and synchronised camera, CAN and radar logs in Vector CANoe / CANape. Identified "
        "the field-of-view boundary issue, worked with the supplier and verified its calibration "
        "change on site.",
        "<b>Test execution & system correlation:</b> Verified features in vehicles and on "
        "proving grounds, and supported AVL's DrivingCube vehicle-in-the-loop test bed. Fitted "
        "external GNSS for ground truth and used MATLAB / Simulink and IPG CarMaker to compare "
        "vehicle, dyno and simulation results.",
        "<b>Hardware returns & documentation:</b> Inspected about 20 returned LEVC "
        "range-extender generators using multimeter checks and low-voltage bench-supply log "
        "retrieval. Authored requirements and test records, tracked defects in RTC / RQM and "
        "contributed to ISO 26262 requirements and FMEA.",
    ],
)
content.append(
    Paragraph(
        "<b>Mechanical Engineering Intern</b>, TEMSA Global (2014): calculated power and torque "
        "requirements for an electric-bus powertrain using MATLAB / Simulink.",
        line,
    )
)

content += section("Education")
content.append(
    Paragraph(
        "<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick (2017–2018, "
        "2:1 Merit). Designed an experimental method and thermocouple layout for electric-motor "
        "stator thermal characterisation (MotorCAD, MATLAB / Simulink); physical test bench not "
        "built.",
        line,
    )
)
content.append(
    Paragraph(
        "<b>BSc Mechanical Engineering</b>, Ege University (2011–2017). Team-designed and built "
        "a 6-DOF Stewart platform; wired servo actuators and used Arduino to command and check "
        "signals.",
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
                        "Test & validation",
                        "Test plans and cases, boundary testing, system validation, regression analysis, "
                        "requirements-to-test traceability, defect reporting",
                    ),
                    (
                        "Sensors & analysis",
                        "Corner radar, synchronised camera/CAN/radar logs, GNSS ground truth, Vector CANoe / "
                        "CANape, MATLAB / Simulink, IPG CarMaker",
                    ),
                    (
                        "Automation & leadership",
                        "Python (AI-assisted tools), parameterised scenarios, KPI dashboards, technical "
                        "coaching, cross-functional and supplier collaboration",
                    ),
                    (
                        "Engineering background",
                        "Mechanical systems, vehicle electronics, electric-motor thermal test design, "
                        "multimeter and low-voltage bench supply",
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
