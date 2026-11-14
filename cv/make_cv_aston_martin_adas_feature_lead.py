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


body = style("body", fontSize=8.15, leading=10.5, textColor=colors.HexColor("#222222"))
bullet = style("bullet", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=0.65)
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
        M, H - 21 * mm, "ADAS Feature Lead  |  Feature Ownership, Requirements & Validation"
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


OUT = (
    Path(__file__).resolve().parent
    / "Muhammet_Celal_Gokalp_CV_Aston_Martin_ADAS_Feature_Lead.pdf"
)
CONTENT_WIDTH = W - 2 * M
doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    title="Muhammet Celal Gokalp - Aston Martin ADAS Feature Lead CV",
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
        "ADAS feature owner and systems engineer with 8 years delivering driver-assistance and "
        "automated-driving features across customer, supplier and engineering teams. At AVL, "
        "owned three corner-radar features at Jaguar Land Rover from customer needs, use cases "
        "and requirements through system-state test definition and vehicle validation. At "
        "FiveAI / Bosch, translated customer and regulatory expectations into KPIs, led a "
        "five-engineer technical team and supported Volkswagen Group partner engineers. Strong "
        "in requirements traceability, supplier problem-solving and keeping feature decisions "
        "grounded in measurable customer and system behaviour.",
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
        "<b>Feature targets & performance:</b> Translated customer requirements, UN R79 and "
        "Euro NCAP expectations into measurable KPIs and pass/fail criteria; analysed more than "
        "1,000 hours of test data and compared software versions to identify regressions.",
        "<b>Technical coordination:</b> Led five engineers for a year as technical lead, teaching "
        "evaluation methods and coordinating scenario creation and assessment. Worked across "
        "engineering teams to resolve integration issues on the Volkswagen Group ADA project.",
        "<b>Customer and partner engagement:</b> Trained Volkswagen Group partner engineers on "
        "FiveAI's simulation toolchain and became a founding member of the Simulation EcoSystem "
        "solutions team, diagnosing issues across shared tools, maps, APIs and simulation.",
        "<b>Verification methods:</b> Created 120+ parameterised OpenSCENARIO 2 scenarios "
        "generating thousands of test cases for UN R79 automatic lane change and Euro NCAP "
        "junction testing; built Python-assisted tooling and dashboard pipelines to support "
        "repeatable analysis.",
    ],
)
content += job(
    "ADAS Systems Engineer (Feature Owner)",
    "AVL Powertrain UK",
    "Jaguar Land Rover, UK",
    "11/2018 – 10/2021",
    [
        "<b>End-to-end feature ownership:</b> Feature owner for Rear Cross Traffic Alert, Blind "
        "Spot Monitor and Rear Pre-Crash corner-radar functions. Main technical link between "
        "JLR, AVL and the radar supplier, working across mechanical, electrical and software "
        "disciplines.",
        "<b>Customer experience to requirements:</b> Turned customer needs into use cases and "
        "system-state diagrams; decomposed requirements in DOORS and MKS Integrity, defined "
        "module input/output signal lists, and traced requirements to per-state test cases "
        "within the ASPICE V-model.",
        "<b>Technical issue ownership:</b> When Rear Cross Traffic Alert passed HiL testing but "
        "triggered late at the proving-ground boundary, designed coarse-to-fine tests, "
        "synchronised camera, CAN and radar logs in Vector CANoe / CANape, agreed a supplier "
        "calibration change and verified the result on site.",
        "<b>Validation & safety:</b> Supported verification across vehicle, proving-ground and "
        "AVL DrivingCube ViL testing; tracked defects in RTC / RQM. Wrote ISO 26262 safety "
        "requirements for a lane-change feature and took part in its FMEA.",
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
        "2:1 Merit). Coursework included hybrid and electric vehicle systems; dissertation "
        "designed an experimental thermal-characterisation method for an electric-motor stator.",
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
                        "Feature delivery",
                        "Feature ownership, customer use cases, KPIs, requirements decomposition, interfaces, "
                        "traceability, test definition and issue resolution",
                    ),
                    (
                        "ADAS & regulation",
                        "Corner-radar ADAS; RCTA, BSM, Rear Pre-Crash; ACC, LKA, HWA, LCA requirements; "
                        "UN R79, Euro NCAP; ISO 26262 and SOTIF training",
                    ),
                    (
                        "Tools & methods",
                        "IBM DOORS, MKS Integrity, RTC / RQM, Vector CANoe / CANape, MATLAB / Simulink, "
                        "IPG CarMaker, OpenSCENARIO 2, Python (AI-assisted tools)",
                    ),
                    (
                        "Safety & leadership",
                        "ISO 26262 safety requirements; FMEA participation (not specifically DFMEA ownership); "
                        "technical lead for five engineers; customer and Tier 1 supplier coordination",
                    ),
                    (
                        "Additional",
                        "British citizen, full UK driving licence, immediately available; English (C2), Turkish (native)",
                    ),
                ]
            )
        ]
    )
)

doc.build(content)
