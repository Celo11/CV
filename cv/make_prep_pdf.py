"""Convert an interview-prep Markdown file to a clean A4 PDF using reportlab only.

Usage:
    .venv/bin/python make_prep_pdf.py CALLEN_LENZ_INTERVIEW_PREP.md [output.pdf]

Supports the Markdown used in the prep files: headings, paragraphs, nested bullet and
numbered lists, pipe tables, fenced code blocks, blockquotes, GitHub alerts
(> [!NOTE] etc.), horizontal rules, <details>/<summary>, and inline **bold**, *italic*,
`code` and [links](url).
"""
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, ListFlowable, ListItem, Paragraph,
                                Preformatted, SimpleDocTemplate, Spacer, Table,
                                TableStyle)
from reportlab.platypus.flowables import HRFlowable

# ---------- fonts (DejaVu covers arrows, Greek letters, box drawing) ----------
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("Body", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("Body-Bold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Mono", str(FONT_DIR / "DejaVuSansMono.ttf")))
pdfmetrics.registerFont(TTFont("Mono-Bold", str(FONT_DIR / "DejaVuSansMono-Bold.ttf")))
from reportlab.pdfbase.pdfmetrics import registerFontFamily  # noqa: E402

# No DejaVu Sans oblique is installed, so italics map to the upright face.
registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body", boldItalic="Body-Bold")
registerFontFamily("Mono", normal="Mono", bold="Mono-Bold", italic="Mono", boldItalic="Mono-Bold")

# ---------- colours and styles ----------
NAVY = colors.HexColor("#1F3A5F")
TEAL = colors.HexColor("#2A8C82")
GREY = colors.HexColor("#555555")
LIGHT = colors.HexColor("#EEF3F7")
CODE_BG = colors.HexColor("#F4F4F4")
ALERT = {
    "NOTE": colors.HexColor("#2F6DB5"),
    "TIP": colors.HexColor("#2E8B57"),
    "IMPORTANT": colors.HexColor("#7B4FC4"),
    "WARNING": colors.HexColor("#C77700"),
    "CAUTION": colors.HexColor("#C0392B"),
}

PAGE_W, PAGE_H = A4
MARGIN = 16 * mm
USABLE_W = PAGE_W - 2 * MARGIN


def style(name, **kw):
    base = dict(fontName="Body", fontSize=9.5, leading=13, textColor=colors.black,
                alignment=TA_LEFT, spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    "h1": style("h1", fontName="Body-Bold", fontSize=18, leading=22, textColor=NAVY, spaceAfter=6, keepWithNext=1),
    "h2": style("h2", fontName="Body-Bold", fontSize=13.5, leading=17, textColor=NAVY,
                spaceBefore=10, spaceAfter=5, keepWithNext=1),
    "h3": style("h3", fontName="Body-Bold", fontSize=11, leading=14, textColor=TEAL,
                spaceBefore=7, spaceAfter=3, keepWithNext=1),
    "h4": style("h4", fontName="Body-Bold", fontSize=10, leading=13, textColor=NAVY,
                spaceBefore=5, spaceAfter=2, keepWithNext=1),
    "body": style("body"),
    "quote": style("quote", textColor=colors.HexColor("#222222"), spaceAfter=2),
    "cell": style("cell", fontSize=8, leading=10, spaceAfter=0),
    "cell_h": style("cell_h", fontName="Body-Bold", fontSize=8, leading=10, spaceAfter=0,
                    textColor=colors.white),
    "list": style("list", spaceAfter=1),
}


# ---------- inline markdown -> reportlab mini-HTML ----------
def inline(text):
    codes = []

    def keep_code(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\\\$", "$", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<link href="\2" color="#2F6DB5">\1</link>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])",
                  r'<font color="#555555">\1</font>', text)

    def put_code(m):
        c = codes[int(m.group(1))]
        c = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'<font name="Mono" size="8" color="#9C2E2E">{c}</font>'

    return re.sub(r"\x00(\d+)\x00", put_code, text)


def para(text, st):
    return Paragraph(inline(text), st)


# ---------- block builders ----------
def build_table(rows):
    def split(row):
        row = row.strip().strip("|")
        return [c.strip() for c in re.split(r"(?<!\\)\|", row)]

    header = split(rows[0])
    body = [split(r) for r in rows[2:]]
    ncol = len(header)
    body = [(r + [""] * ncol)[:ncol] for r in body]

    small = ncol >= 7
    fs = 6.5 if ncol >= 10 else 7 if small else 8
    cell_st = style("c2", fontSize=fs, leading=fs * 1.25, spaceAfter=0)
    head_st = style("ch2", fontName="Body-Bold", fontSize=fs, leading=fs * 1.25, spaceAfter=0,
                    textColor=colors.white)

    # Column widths: weight by content length, but never narrower than the longest word
    # (measured in the bold font so headers and bold words don't split).
    weights, mins = [], []
    for j in range(ncol):
        col = [header[j]] + [r[j] for r in body]
        plain = [re.sub(r"[*`]", "", c) for c in col]
        words = [w for c in plain for w in c.split()] or ["x"]
        longest_w = max(pdfmetrics.stringWidth(w, "Body-Bold", fs) for w in words)
        avg = sum(len(c) for c in plain) / len(plain)
        weights.append(max(avg, len(max(words, key=len)) * 1.1, 2))
        mins.append(longest_w + 7)
    if sum(mins) > USABLE_W:
        mins = [m * USABLE_W / sum(mins) for m in mins]
    total = sum(weights)
    widths = [USABLE_W * w / total for w in weights]
    # enforce minimums, then rescale the remaining columns
    for _ in range(3):
        short = [j for j in range(ncol) if widths[j] < mins[j]]
        if not short:
            break
        fixed = sum(mins[j] for j in short)
        rest = [j for j in range(ncol) if j not in short]
        rest_w = sum(weights[j] for j in rest) or 1
        for j in short:
            widths[j] = mins[j]
        for j in rest:
            widths[j] = (USABLE_W - fixed) * weights[j] / rest_w

    data = [[para(h, head_st) for h in header]] + [[para(c, cell_st) for c in r] for r in body]
    t = Table(data, colWidths=widths, repeatRows=1)
    ts = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#B8C4CE")),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            ts.append(("BACKGROUND", (0, i), (-1, i), LIGHT))
    t.setStyle(TableStyle(ts))
    return [t, Spacer(1, 5)]


def build_code(lines):
    longest = max((len(l) for l in lines), default=1)
    size = max(5.5, min(8.0, USABLE_W / (longest * 0.62 + 4)))
    # Tight leading for box-drawing art so vertical lines join up.
    box_art = any(ch in "│┌┐└┘├┤┬┴┼║═╔╗╚╝" for l in lines for ch in l)
    st = ParagraphStyle("code", fontName="Mono", fontSize=size,
                        leading=size * (1.17 if box_art else 1.3))
    pre = Preformatted("\n".join(lines), st)
    box = Table([[pre]], colWidths=[USABLE_W])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return [box, Spacer(1, 5)]


def build_quote(lines):
    kind = None
    m = re.match(r"\s*\[!(\w+)\]\s*$", lines[0]) if lines else None
    if m and m.group(1).upper() in ALERT:
        kind = m.group(1).upper()
        lines = lines[1:]
    inner = parse_blocks(lines, quote=True)
    bar = ALERT.get(kind, TEAL)
    content = []
    if kind:
        content.append(Paragraph(f'<font color="{bar.hexval().replace("0x", "#")}"><b>{kind}</b></font>',
                                 S["quote"]))
    content.extend(inner)
    box = Table([[content]], colWidths=[USABLE_W - 4])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F6F9FB") if not kind else
         colors.HexColor("#FBF8F1") if kind == "WARNING" else colors.HexColor("#F5F5FB")),
        ("LINEBEFORE", (0, 0), (0, -1), 3, bar),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return [box, Spacer(1, 5)]


LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")


def build_list(lines, base_style):
    """lines: list items with their indentation; continuation lines are attached to the item."""
    items = []  # (indent, ordered, text, children_lines)
    first = LIST_RE.match(lines[0])
    base_indent = len(first.group(1))
    ordered = first.group(2)[0].isdigit()
    start = int(first.group(2)[:-1]) if ordered else 1
    cur = None
    for line in lines:
        m = LIST_RE.match(line)
        if m and len(m.group(1)) <= base_indent + 1:
            num = int(m.group(2)[:-1]) if m.group(2)[0].isdigit() else None
            cur = [m.group(3), [], num]
            items.append(cur)
        elif cur is not None:
            cur[1].append(line)
    flow_items = []
    for text, children, num in items:
        parts = [para(text, base_style)]
        # continuation text (not a nested list) joins the item
        child_list, extra_text = [], []
        for c in children:
            if LIST_RE.match(c) or child_list:
                child_list.append(c)
            else:
                extra_text.append(c.strip())
        if extra_text:
            parts = [para(text + " " + " ".join(extra_text), base_style)]
        if child_list:
            parts.extend(parse_blocks([c[base_indent + 2:] if c.startswith(" " * (base_indent + 2))
                                       else c.lstrip() for c in child_list], nested=True))
        if ordered and num is not None:
            flow_items.append(ListItem(parts, leftIndent=18, value=num))
        else:
            flow_items.append(ListItem(parts, leftIndent=12))
    if ordered:
        return [ListFlowable(flow_items, bulletType="1", start=start, leftIndent=18,
                             bulletFontName="Body-Bold", bulletFontSize=9, bulletColor=NAVY),
                Spacer(1, 3)]
    return [ListFlowable(flow_items, bulletType="bullet", start="•", leftIndent=12,
                         bulletFontSize=9, bulletColor=TEAL), Spacer(1, 3)]


def parse_blocks(lines, quote=False, nested=False):
    out = []
    i, n = 0, len(lines)
    body_st = S["quote"] if quote else S["body"]
    list_st = S["quote"] if quote else S["list"]
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("```"):
            j = i + 1
            code = []
            while j < n and not lines[j].strip().startswith("```"):
                code.append(lines[j].rstrip())
                j += 1
            out += build_code(code)
            i = j + 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            lvl = len(m.group(1))
            out.append(para(m.group(2), S[f"h{lvl}"]))
            if lvl == 2:
                hr = HRFlowable(width="100%", thickness=0.8, color=TEAL, spaceBefore=0, spaceAfter=4)
                hr.keepWithNext = 1  # keep the heading + rule with the first block below
                out.append(hr)
            i += 1
            continue
        if re.match(r"^-{3,}$", stripped):
            out.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#BBBBBB"),
                                  spaceBefore=4, spaceAfter=4))
            i += 1
            continue
        if stripped.startswith("<details"):
            i += 1
            continue
        if stripped.startswith("</details"):
            i += 1
            continue
        m = re.match(r"^<summary>(.*)</summary>$", stripped)
        if m:
            out.append(para(m.group(1), S["h4"]))
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            j = i
            rows = []
            while j < n and lines[j].strip().startswith("|"):
                rows.append(lines[j])
                j += 1
            out += build_table(rows)
            i = j
            continue
        if stripped.startswith(">"):
            j = i
            q = []
            while j < n and lines[j].strip().startswith(">"):
                q.append(re.sub(r"^\s*>\s?", "", lines[j]))
                j += 1
            out += build_quote(q)
            i = j
            continue
        if LIST_RE.match(line):
            j = i
            block = []
            while j < n:
                l = lines[j]
                if not l.strip():
                    # a blank line ends the list unless the next line is still part of it
                    if j + 1 < n and (LIST_RE.match(lines[j + 1]) or lines[j + 1].startswith("  ")):
                        j += 1
                        continue
                    break
                if (LIST_RE.match(l) or l.startswith(" ")) and not l.strip().startswith(("```", "|", ">")):
                    block.append(l)
                    j += 1
                else:
                    break
            out += build_list(block, list_st)
            i = j
            continue
        # paragraph: join until a blank line or another block starts
        j = i
        buf = []
        while j < n and lines[j].strip() and not re.match(r"^(#{1,4}\s|```|\||>|-{3,}$|<)", lines[j].strip()) \
                and not (buf and LIST_RE.match(lines[j])):
            buf.append(lines[j].strip())
            j += 1
        joined = " ".join(buf)
        # "When:" lines and short bold lead-ins introduce what follows: keep them together.
        lead_in = joined.startswith("**When:**") or (joined.startswith("**") and len(joined) < 150)
        st = style("body_keep", keepWithNext=1) if lead_in and not quote else body_st
        out.append(para(joined, st))
        i = j
    return out


def on_page(canvas, doc, title):
    canvas.saveState()
    canvas.setFont("Body", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(MARGIN, 9 * mm, title)
    canvas.drawRightString(PAGE_W - MARGIN, 9 * mm, f"Page {doc.page}")
    canvas.setStrokeColor(TEAL)
    canvas.setLineWidth(0.6)
    canvas.line(MARGIN, 12 * mm, PAGE_W - MARGIN, 12 * mm)
    canvas.restoreState()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".pdf")
    lines = src.read_text(encoding="utf-8").splitlines()
    title = next((l.lstrip("# ").strip() for l in lines if l.startswith("# ")), src.stem)
    story = parse_blocks(lines)
    doc = SimpleDocTemplate(str(dst), pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                            topMargin=14 * mm, bottomMargin=16 * mm, title=title,
                            author="Muhammet Celal Gokalp")
    doc.build(story, onFirstPage=lambda c, d: on_page(c, d, title),
              onLaterPages=lambda c, d: on_page(c, d, title))
    print(f"Wrote {dst}")


if __name__ == "__main__":
    main()
