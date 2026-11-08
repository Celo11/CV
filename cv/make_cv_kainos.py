from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable)

NAVY = colors.HexColor("#14213D"); ACC = colors.HexColor("#1F7A8C")
GREY = colors.HexColor("#555555"); LIGHT = colors.HexColor("#E8F1F4")
W, H = A4; M = 16*mm; HB = 38*mm

def S(n, **k): return ParagraphStyle(n, fontName=k.pop("f", "Helvetica"), **k)
body = S("b", fontSize=9.0, leading=12.4, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=1)
line = S("line", parent=body, spaceAfter=2)
sec = S("sec", f="Helvetica-Bold", fontSize=11.5, leading=14, textColor=NAVY, spaceBefore=7)
role = S("r", f="Helvetica-Bold", fontSize=10.3, leading=13, textColor=colors.black)
org = S("o", f="Helvetica-Bold", fontSize=9.5, leading=12, textColor=ACC)
meta = S("m", f="Helvetica-Oblique", fontSize=8.8, leading=12, textColor=GREY, alignment=2)
loc = S("l", fontSize=8.8, leading=12, textColor=GREY, alignment=2)

def header(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-HB, W, HB, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-HB-2*mm, W, 2*mm, 0, 1)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 23)
    c.drawString(M, H-17*mm, "Muhammet Celal Gokalp")
    c.setFont("Helvetica", 10.5); c.setFillColor(colors.HexColor("#A8D5E2"))
    c.drawString(M, H-23.5*mm, "Forward Deployed Engineer  |  Customer Deployments, AI Agent Skills & Python Tools")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 7397 791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British citizen")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Kainos.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
                      author="Muhammet Celal Gokalp", leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([PageTemplate("first", [Frame(M, 8*mm, cw, H-HB-2*mm-12*mm, 0,0,0,0)], onPage=header)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.2, color=ACC, spaceBefore=1, spaceAfter=3)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,2), items[0]]), *items[1:], Spacer(1,4)]

def grid(rows, w1):
    t = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a, b in rows], colWidths=[cw*w1, cw*(1-w1)])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
      ("TOPPADDING",(0,0),(-1,-1),2.5),("BOTTOMPADDING",(0,0),(-1,-1),2.5),("LEFTPADDING",(0,0),(-1,-1),5)]))
    return t

s = []
s += section("Professional Summary")
s.append(Paragraph("Engineer with 8 years in customer-facing technical roles: a consultant embedded at Jaguar Land Rover, then helping Volkswagen Group partner engineers adopt FiveAI / Bosch's simulation toolchain. I fix integration problems, build Python tools and AI agent skills, and check AI output carefully before relying on it. I learned Python on the job with AI-assisted coding, pick up new technology quickly, and I'm keen to learn Azure and Microsoft 365.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>Customer adoption:</b> Trained Volkswagen Group partner engineers on our simulation toolchain (ADA project) and was a founding member of the Simulation EcoSystem solutions team.",
 "<b>Integration issues:</b> Diagnosed problems across partners' toolchains, maps and add-on tools from the error logs between APIs and simulation tools, and got the right team to fix them.",
 "<b>AI agent skills:</b> Built a GitHub Copilot / Copilot CLI helper that turns regulation and Euro NCAP rules into test scenarios. Used project-wide, it cut scenario writing from about a day to about an hour.",
 "<b>Reliable AI output:</b> Gave the agent golden examples and a rules file, checked its output by hand and added validation checks that run after each scenario. Taught colleagues to check AI output, not just trust it.",
 "<b>Python tools:</b> Built tools with AI help (JSON parameter GUI, uploader, data pipelines into dashboards). Work in the project monorepo with a dev container, CI pipeline and pull requests.",
 "<b>Requirements to results:</b> Turned UN R79, Euro NCAP and customer requirements into KPIs across 1,000+ hours of test data, and wrote 120+ parameterised scenarios plus reusable Euro NCAP templates.",
 "<b>Team lead:</b> Led five engineers for a year (technical lead, not line manager) and taught them our tools."])
s += job("ADAS Systems Engineer (Feature Owner)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Client-embedded consulting:</b> Two years at Jaguar Land Rover as feature owner for three radar features (Rear Cross Traffic Alert, Blind Spot Monitor, Rear Pre-Crash); link between JLR, AVL and the supplier.",
 "<b>Requirements to tests:</b> Turned customer needs into use cases and requirements (DOORS, MKS Integrity, ASPICE) and tested them on HiL / ViL rigs, in vehicles and on the proving ground.",
 "<b>Issue resolution:</b> An alert passed on the rigs but fired late on the track. Using synchronised camera, CAN and radar logs, I traced it to the edge of the radar's field of view and verified the supplier's fix.",
 "<b>Also:</b> Checked returned range-extender generators at the LEVC factory for supplier root cause analysis; wrote ISO 26262 requirements for a lane change feature and took part in its FMEA."])
s.append(Paragraph("<b>Part-Time Teacher</b>, Space Camp Turkey, 2013 – 2017: taught science and space technology to students aged 9 to 16.", line))
s.append(Paragraph("<b>Mechanical Engineering Intern</b>, TEMSA Global, 2014: electric bus powertrain sizing in MATLAB / Simulink.", line))

s += section("Education")
s.append(Paragraph("<b>MSc Sustainable Automotive Engineering</b>, WMG, University of Warwick, 2017 – 2018. Grade: 2:1 (Merit).", line))
s.append(Paragraph("<b>BSc Mechanical Engineering</b>, Ege University, Izmir, 2011 – 2017.", line))

s += section("Skills")
s.append(KeepTogether([grid([
 ("AI", "GitHub Copilot and Copilot CLI agent skills, AI-assisted coding, checking AI output against rules and test results, running a VLA model locally in Docker (user level)"),
 ("Software", "Python (written with AI help), JSON, Git and pull requests, CI pipelines, dev containers, Linux (main workstation for 5 years), VS Code; C++ (reading)"),
 ("Customer &amp; delivery", "On-site client work, training users, requirements gathering, supplier coordination, root cause and log analysis (Vector CANoe / CANape)"),
 ("Domain", "Automated driving simulation (OpenSCENARIO 2), HiL / ViL and vehicle testing, Euro NCAP, UN R79, ISO 26262 and SOTIF (trained), MATLAB / Simulink"),
 ("Other", "English (C2), Turkish (native); full UK driving licence; happy to travel and relocate in the UK")], 0.2)]))
doc.build(s)
