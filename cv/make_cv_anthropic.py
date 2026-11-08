from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable,
                                NextPageTemplate, CondPageBreak)

NAVY = colors.HexColor("#14213D"); ACC = colors.HexColor("#1F7A8C")
GREY = colors.HexColor("#555555"); LIGHT = colors.HexColor("#E8F1F4")
W, H = A4; M = 16*mm; HB = 38*mm

def S(n, **k): return ParagraphStyle(n, fontName=k.pop("f", "Helvetica"), **k)
body = S("b", fontSize=9.2, leading=13, textColor=colors.HexColor("#222222"))
bul = S("bul", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=1.5)
sec = S("sec", f="Helvetica-Bold", fontSize=11.5, leading=14, textColor=NAVY, spaceBefore=9)
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
    c.drawString(M, H-23.5*mm, "Solutions Engineer  |  AI-Enabled Engineering Workflows  |  Autonomous Systems")
    c.setFillColor(colors.white); c.setFont("Helvetica", 8.3)
    c.drawString(M, H-30*mm, "+44 07397791625   |   muhammetcelalgokalp@gmail.com   |   Coventry, CV5 8HN, UK   |   British, Turkish")
    c.drawString(M, H-34*mm, "linkedin.com/in/celal-gökalp-4616ab122")
    c.restoreState()
def later(c, d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, H-8*mm, W, 8*mm, 0, 1)
    c.setFillColor(ACC); c.rect(0, H-9.2*mm, W, 1.2*mm, 0, 1); c.restoreState()

doc = BaseDocTemplate("Muhammet_Celal_Gokalp_CV_Anthropic.pdf", pagesize=A4, title="Muhammet Celal Gokalp - CV",
                      author="Muhammet Celal Gokalp", leftMargin=M, rightMargin=M)
cw = W-2*M
doc.addPageTemplates([
    PageTemplate("first", [Frame(M, 12*mm, cw, H-HB-2*mm-16*mm, 0,0,0,0)], onPage=header),
    PageTemplate("later", [Frame(M, 12*mm, cw, H-9*mm-18*mm, 0,0,0,0)], onPage=later)])

def section(t):
    return [Paragraph(t.upper(), sec), HRFlowable(width="100%", thickness=1.2, color=ACC, spaceBefore=1, spaceAfter=4)]

def head_table(l, r, l2, r2):
    t = Table([[Paragraph(l, role), Paragraph(r, meta)],
               [Paragraph(l2, org), Paragraph(r2, loc)]], colWidths=[cw*0.68, cw*0.32])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    return t

def job(r, o, where, dates, bullets):
    items = [Paragraph(b, bul, bulletText="•") for b in bullets]
    if len(items) <= 2:
        return [KeepTogether([head_table(r, dates, o, where), Spacer(1,2), *items]), Spacer(1,5)]
    return [KeepTogether([head_table(r, dates, o, where), Spacer(1,2), items[0]]), *items[1:], Spacer(1,5)]

def edu(t, d, u, bl):
    return [KeepTogether([head_table(t, d, u, ""), Spacer(1,2)] + [Paragraph(b, bul, bulletText="•") for b in bl]), Spacer(1,5)]


s = []
s += section("Professional Summary")
s.append(Paragraph("Customer-facing engineer with nearly 8 years in automotive and autonomous driving, embedded with OEM and internal customer teams to turn messy requirements into working, verified solutions. At FiveAI / Bosch I built LLM-based agent skills with GitHub Copilot and Copilot CLI that turned regulation and Euro NCAP rules into OpenSCENARIO 2 test scenarios. The approach was adopted across the project and multiplied scenario output from a small set of hand-crafted modular building blocks. I am not a classically trained software engineer. I learned to build and ship tools by working closely with AI, which is why I am good at showing non-specialists how to use it well, with healthy scepticism and careful checking of results.", body))

s += section("Work Experience")
s += job("Lead Application Engineer (Solutions &amp; Integration)", "FiveAI / Bosch", "Cambridge, United Kingdom", "10/2021 – Present", [
 "<b>LLM agent skills for scenario generation:</b> Built AI skills with GitHub Copilot and Copilot CLI that act as an OpenSCENARIO 2 (DSL) helper. Engineers give the agent context such as UN regulation text and Euro NCAP rules, and it composes our hand-crafted modular scenarios into new ones with exact, checkable metrics. Used project-wide, it increased scenario output by an order of magnitude.",
 "<b>Driving AI adoption:</b> Showed engineers and non-software colleagues how to use AI tools in their daily work, including how to give good context, break problems down, and verify outputs rather than trust them.",
 "<b>Domain-specific evaluation:</b> Every generated scenario was checked against its source rules and run in simulation. Defined pass/fail and KPI criteria, such as comfort limits for acceleration and deceleration across 1,000+ hours of test data.",
 "<b>Scenario-based V&amp;V:</b> Built 120+ parameterised OpenSCENARIO 2 scenarios generating thousands of test cases for an L4 automated driving stack, covering Euro NCAP junction tests and UN R79 automatic lane change (ADA project).",
 "<b>Tools &amp; data pipelines:</b> With AI-assisted coding in Python, built internal tools (a GUI for JSON test parameters, a local uploader) and pipelines that send simulation results to front-end dashboards, raising pull requests to the main monorepo and working in its dev container.",
 "<b>Internal customers &amp; integration:</b> On the ADA project, a partnership with Volkswagen Group where FiveAI supplied the simulation tooling, trained partner engineers to use our toolchain. This grew into the Simulation EcoSystem solutions team, where I was a founding member. Ran discovery with users, triaged issues across tools, maps and simulation, and worked with several engineering teams to keep internal and enterprise users running."])
s += job("ADAS Systems Engineer (Feature Owner, client-embedded)", "AVL Powertrain UK", "Coventry, United Kingdom", "11/2018 – 10/2021", [
 "<b>Embedded at the customer:</b> Worked on-site at Jaguar Land Rover for two years as AVL's feature owner for Rear Cross Traffic Alert, Blind Spot Monitor and Rear Pre-Crash. I was the technical link between the OEM, AVL and suppliers.",
 "<b>Discovery to delivery:</b> Turned stakeholder needs into use cases, system state diagrams and requirements in DOORS and MKS Integrity (ASPICE), then verified them on HiL and ViL rigs and on the proving ground.",
 "<b>Problem solving under ambiguity:</b> Found root causes in vehicle network data (Vector CANoe / CANape). For example, an alert triggered late at boundary conditions, and I agreed a sensor field-of-view change with the supplier while keeping false alerts low.",
 "<b>Safety mindset:</b> Wrote ISO 26262 functional safety requirements for a lane change feature. Trained in ISO 26262 and SOTIF (ISO 21448)."])
s += job("Part-Time Teacher and Program Planner", "Space Camp Turkey", "Izmir, Türkiye", "12/2013 – 01/2017", [
 "Taught space technology and science to students aged 9 to 16. This is where I learned to explain complex ideas simply."])

e = [CondPageBreak(60*mm)] + section("Education")
e += edu("MSc in Sustainable Automotive Engineering", "10/2017 – 09/2018", "Warwick Manufacturing Group, Coventry, UK", [
 "<b>Grade:</b> 2:1 (Merit). Dissertation: experimental testing to find the variables of a thermal model of an electric motor stator (MATLAB, Simulink, MotorCAD)."])
e += edu("BSc in Mechanical Engineering", "08/2011 – 02/2017", "Ege University, Izmir, Türkiye", [
 "Dissertation: designed, built and controlled a 6-DOF Stewart motion platform (SolidWorks, MATLAB, Arduino)."])
s += e

rows = [("AI &amp; LLMs","Agent skills and prompting (GitHub Copilot, Copilot CLI), giving domain context to LLMs, AI-assisted coding, checking LLM output against rules and simulation"),
 ("Software","Python (scripting, tools, data pipelines), C++ (reading), OpenSCENARIO 2 DSL, Git / GitHub, monorepo and dev containers, JSON, MATLAB / Simulink"),
 ("Customer &amp; Delivery","On-site client work, requirements discovery, stakeholder management, root cause analysis, training colleagues, Jira / Confluence"),
 ("Domain","L4 autonomous driving, ADAS, scenario-based testing, SIL / HiL / ViL, ISO 26262, SOTIF, UN R79, Euro NCAP"),
 ("Languages","English (C2), Turkish (Native)")]
sk = Table([[Paragraph(f"<b>{a}</b>", body), Paragraph(b, body)] for a,b in rows], colWidths=[cw*0.22, cw*0.78])
sk.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT, colors.white]),
  ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),5)]))
s.append(KeepTogether(section("Skills") + [sk]))
s.insert(0, NextPageTemplate("later"))
doc.build(s)
