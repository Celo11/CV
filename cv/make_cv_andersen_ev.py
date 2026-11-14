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
        M, H - 21 * mm, "Hardware Test & Validation Engineer  |  EV Systems, Diagnostics & Test"
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
        "linkedin.com/in/celal-gökalp-4616ab122   |   Full UK driving licence   |   Immediately available",
    )
    canvas.restoreState()


OUT = Path(__file__).resolve().parent / "Muhammet_Celal_Gokalp_CV_Andersen_EV.pdf"
CONTENT_WIDTH = W - 2 * M
doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    title="Muhammet Celal Gokalp - Andersen EV Hardware Test Engineer CV",
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
        HRFlowable(width="100%", thickness=1.1, color=ACC, spaceBefore=0.8, spaceAfter=2),
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
        colWidths=[CONTENT_WIDTH * 0.24, CONTENT_WIDTH * 0.76],
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
content += section("Professional Profile")
content.append(
    Paragraph(
        "Mechanical engineer with 8 years in automotive systems testing, hardware diagnostics "
        "and structured fault investigation at AVL Powertrain and FiveAI / Bosch. Hands-on "
        "experience includes multimeter checks on returned range-extender generators, low-voltage "
        "bench-supply diagnostics, vehicle and test-bed verification, and time-aligned sensor/CAN "
        "log analysis. Holds an MSc in Sustainable Automotive Engineering, including the design "
        "of an electric-motor stator thermal-characterisation test. Practical, methodical and keen "
        "to apply this experience to EV charging product verification and manufacturing quality.",
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
        "<b>Test analysis & regression:</b> Defined measurable pass/fail criteria and KPIs, "
        "analysed results across 1,000+ hours of system data, and compared software versions to "
        "identify regressions and report findings.",
        "<b>Structured fault investigation:</b> Diagnosed issues across partner toolchains, APIs, "
        "maps and simulation by tracing logs and evidence to isolate the responsible subsystem; "
        "coordinated corrective actions with engineering teams.",
        "<b>Test tools & technical leadership:</b> Built Python tools with AI assistance for test "
        "parameters, data upload and dashboard pipelines. Led five engineers for a year as a "
        "technical lead, teaching evaluation methods and reviewing work against requirements.",
    ],
)
content += job(
    "ADAS Systems Engineer (Feature Owner)",
    "AVL Powertrain UK",
    "Jaguar Land Rover, UK",
    "11/2018 – 10/2021",
    [
        "<b>Vehicle and system verification:</b> Owned three corner-radar features from "
        "requirements through test cases and vehicle/proving-ground validation. Worked across "
        "customer, supplier and mechanical, electrical and software teams.",
        "<b>Root-cause investigation:</b> When an alert passed HiL testing but triggered late on "
        "the proving ground, planned boundary tests and synchronised camera, CAN and radar logs "
        "in Vector CANoe / CANape; worked with the supplier and verified its calibration fix on site.",
        "<b>Returned-product diagnostics:</b> At the LEVC factory, inspected about 20 returned "
        "range-extender generators, performed connector multimeter checks and used a low-voltage "
        "bench supply to retrieve controller logs. Sent the measurements and evidence to developers "
        "and suppliers for root-cause investigation.",
        "<b>Test setup & traceability:</b> Fitted external GNSS for ground-truth logging on AVL's "
        "DrivingCube vehicle-in-the-loop test bed. Authored requirements, system states and test "
        "cases in DOORS / MKS Integrity; recorded defects in RTC / RQM and contributed to FMEA.",
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
        "2:1 Merit). Designed an experimental method and thermocouple layout to characterise an "
        "electric-motor stator's thermal model (MotorCAD, MATLAB / Simulink); the physical test "
        "bench was not built.",
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

content += section("Relevant Skills")
content.append(
    KeepTogether(
        [
            skills_table(
                [
                    (
                        "Hardware diagnostics",
                        "Multimeter (resistance, continuity, fuse checks); low-voltage / 12 V bench supplies; "
                        "returned generator and vehicle-module investigations",
                    ),
                    (
                        "Test & data",
                        "Vehicle, proving-ground and AVL DrivingCube ViL testing; boundary tests; Vector "
                        "CANoe / CANape; synchronised sensor logs; test evidence and defect records",
                    ),
                    (
                        "Engineering tools",
                        "Python tools (AI-assisted), MATLAB / Simulink, IPG CarMaker, Arduino, SolidWorks, "
                        "DOORS, MKS Integrity, RTC / RQM",
                    ),
                    (
                        "Electrical / EV",
                        "Electric-bus powertrain sizing; electric-motor stator thermal test design; practical "
                        "low-voltage diagnostics. No direct PCB assembly test, oscilloscope, ICT, mains-power "
                        "or EV-charger compliance experience",
                    ),
                    (
                        "Additional",
                        "British citizen with full UK driving licence; immediately available; English (C2), "
                        "Turkish (native)",
                    ),
                ]
            )
        ]
    )
)

doc.build(content)
