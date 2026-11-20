"""Algerian Regulations and Duty Time (recurrent, all fleets).

Source: the national "Algerian Regulation Course" presentation provided by the training department (regulation is
national: laws, decrees, ANAC circulars, AIP Algeria GEN 1.7), completed with ICAO references. Duty time rules:
Law 90-11, Law 98-06, Decrees 02-89, 04-414, 10-140. The company OM A (FTL chapter) applies; where it differs,
the most restrictive rule applies.

Lesson 7 contains an interactive duty time calculator and practice exercises (plain JavaScript, no server).
"""
from courses.upset_recovery.diagrams import FONT, INK, MUTED, LINE, GREEN, GREEN_D, RED, AMBER, BLUE

ARROW = ('<defs><marker id="{id}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         '<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker></defs>')


def fig(svg, caption, title, vb="0 0 700 320", maxw=None):
    st = f' style="max-width:{maxw}px;margin:0 auto;display:block"' if maxw else ""
    return (f'<figure class="diagram"><svg viewBox="{vb}"{st} role="img" aria-label="{title}"><title>{title}</title>'
            f'<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg><figcaption>{caption}</figcaption></figure>')


def box(x, y, w, h, text, fill="#fff", stroke=GREEN, color=INK, bold=False, size=13, sub=None):
    t = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
    cy = y + h / 2 + (-4 if sub else 5)
    t += f'<text x="{x + w / 2}" y="{cy}" text-anchor="middle" fill="{color}" font-size="{size}"{" font-weight=\"700\"" if bold else ""}>{text}</text>'
    if sub:
        t += f'<text x="{x + w / 2}" y="{cy + 17}" text-anchor="middle" fill="{MUTED}" font-size="11.5">{sub}</text>'
    return t


def arrow(x1, y1, x2, y2, mid="a1", color=MUTED, w=2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="{w}" fill="none" marker-end="url(#{mid})"/>'


# ------------------------------------------------------------------ diagrams
def hierarchy():
    rows = [("CONSTITUTION", "fundamental law + international conventions", GREEN_D, "#fff"),
            ("LAWS", "voted by the Assembly · Official Journal", GREEN, "#fff"),
            ("DECREES", "signed by the President or Prime Minister", "#2f8f52", "#fff"),
            ("ORDERS (ARRÊTÉS)", "administrative decisions", "#6fae84", "#fff"),
            ("CIRCULARS", "explain how to apply the texts above", "#cfe5d6", INK)]
    svg = ARROW.format(id="h1", c=MUTED)
    for i, (t, s, f, c) in enumerate(rows):
        w = 220 + i * 60
        x = 290 - w / 2
        y = 20 + i * 58
        svg += f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="6" fill="{f}"/><text x="{x + w / 2}" y="{y + 27}" text-anchor="middle" fill="{c}" font-weight="700">{t}</text>'
        svg += f'<text x="{x + w + 14}" y="{y + 27}" fill="{MUTED}" font-size="12">{s}</text>'
    svg += f'<path d="M24 300 L24 30" stroke="{RED}" stroke-width="3" marker-end="url(#h1)"/><text x="14" y="200" fill="{RED}" font-size="12" text-anchor="middle" transform="rotate(-90 14 200)">higher authority</text>'
    return fig(svg, "The hierarchy of Algerian legal texts: each level must respect the levels above it. A circular cannot change a decree; it only explains how to apply it.",
               "Hierarchy of legal texts", "0 0 860 320")


def icao_map():
    left = [("ICAO Annex 6", "Operation of aircraft"), ("ICAO Annex 8 / Annex 6 Ch. 8", "Airworthiness, maintenance"),
            ("ICAO Annex 1", "Personnel licensing"), ("ICAO Annex 14", "Aerodromes"), ("Safety management", "SMS")]
    right = [("Executive Decrees 09-206, 09-207, 09-208", "Instruction 771/DACM · Circular 1830/DACM"),
             ("Executive Decrees 04-108, 05-163", "Instruction 771/DACM · Circular 1830/DACM (AOC)"),
             ("Executive Decrees 04-414, 09-206", "Circulars 1820, 2455 · Instruction 3062/DACM"),
             ("Circular 3538 · Executive Decree 02-88", "obstacle limitation surfaces"),
             ("DACM Circulars 2693, 2694, 2695", "safety management systems")]
    svg = ARROW.format(id="m1", c=GREEN)
    for i, ((a, b), (c, d)) in enumerate(zip(left, right)):
        y = 14 + i * 60
        svg += box(10, y, 230, 48, a, "#eef6f1", GREEN, bold=True, sub=b)
        svg += arrow(244, y + 24, 318, y + 24, "m1", GREEN, 2.5)
        svg += box(322, y, 368, 48, c, "#fff", GREEN, sub=d, size=12.5)
    return fig(svg, "Where the ICAO standards are found in Algerian regulation. ICAO Annexes apply in Algeria except where a difference is published (AIP Algeria GEN 1.7).",
               "ICAO annexes and Algerian texts", "0 0 700 320")


def fuel_diagram():
    parts = [("Taxi", 24, "#9fb3a7"), ("Trip fuel (AFM)", 90, "#5d8f71"), ("Contingency 5 % of trip", 28, "#3d7a55"), ("Alternate / diversion (AFM)", 52, "#2f6b49"),
             ("Final reserve at 1,500 ft", 44, RED), ("Additional (if required)", 24, AMBER), ("Extra (commander)", 24, BLUE)]
    svg = ARROW.format(id="f1", c=RED)
    y = 290
    for t, h, c in parts:
        y -= h
        svg += f'<rect x="60" y="{y}" width="120" height="{h}" fill="{c}" stroke="#fff"/><text x="194" y="{y + h / 2 + 5}" font-size="12.5">{t}</text>'
    fy = 290 - 24 - 90 - 28 - 52 - 22
    svg += arrow(380, fy, 460, 70, "f1", RED) + arrow(380, fy, 460, 190, "f1", RED)
    svg += box(466, 40, 220, 60, "JET aircraft (B737-800)", "#fdecee", RED, bold=True, sub="final reserve 30 minutes")
    svg += box(466, 160, 220, 60, "PROP aircraft (Q400, Q200)", "#fdecee", RED, bold=True, sub="final reserve 45 minutes")
    svg += f'<text x="60" y="312" fill="{MUTED}" font-size="12">Fuel calculation (Algerian regulation)</text>'
    return fig(svg, "Fuel calculation summary. Algeria has a difference on the final reserve: 30 minutes for jets and 45 minutes for propeller aircraft. The company fuel policy (OM A) applies.",
               "Fuel calculation and final reserve", "0 0 700 320")


def night_diagram():
    svg = ARROW.format(id="n1", c=MUTED)
    svg += '<rect x="40" y="90" width="620" height="60" rx="6" fill="#e9f2fb"/>'
    svg += '<rect x="190" y="90" width="320" height="60" fill="#0f2742"/>'
    svg += '<rect x="150" y="90" width="40" height="60" fill="#f2a65a"/><rect x="510" y="90" width="40" height="60" fill="#f2c27a"/>'
    svg += f'<text x="350" y="126" text-anchor="middle" fill="#fff" font-weight="700">NIGHT</text>'
    for x, t, s in ((150, "Sunset", "sun at the horizon"), (190, "End of civil twilight", "≈ sunset + 30 min (sun 6° below)"),
                    (510, "Civil dawn", "≈ sunrise − 30 min"), (550, "Sunrise", "")):
        svg += f'<path d="M{x} 86 L{x} 160" stroke="{INK}" stroke-width="1.5"/>'
    svg += f'<text x="150" y="70" text-anchor="middle" font-size="12">Sunset</text><text x="196" y="186" text-anchor="middle" font-size="12" font-weight="700">End of civil twilight</text><text x="196" y="202" text-anchor="middle" font-size="11.5" fill="{MUTED}">≈ sunset + 30 min</text>'
    svg += f'<text x="504" y="186" text-anchor="middle" font-size="12" font-weight="700">Civil dawn</text><text x="504" y="202" text-anchor="middle" font-size="11.5" fill="{MUTED}">≈ sunrise − 30 min</text><text x="550" y="70" text-anchor="middle" font-size="12">Sunrise</text>'
    svg += box(40, 230, 620, 64, "Night VFR: IFR-rated pilots · approved public aerodromes only", "#fff", GREEN, bold=True,
               sub="visibility ≥ 8 km · no cloud below 1,500 ft (vicinity) / 1,500 m (navigation) · flight plan required")
    svg += arrow(350, 156, 350, 226, "n1")
    return fig(svg, "Night is the period between the end of civil twilight and civil dawn. Sunrise and sunset times are in the AIP ephemerides.",
               "Definition of night and night VFR", "0 0 700 310")


def dtp_timeline():
    svg = ARROW.format(id="t1", c=GREEN) + ARROW.format(id="t2", c=BLUE)
    svg += f'<line x1="30" y1="150" x2="680" y2="150" stroke="{LINE}" stroke-width="3"/>'
    pts = [(60, "CHECK-IN", "report time"), (150, "1st TAKE-OFF", ""), (235, "leg 1", ""), (320, "leg 2", ""), (405, "leg 3 …", ""), (500, "LAST LANDING", ""), (620, "CHECK-OUT", "")]
    for x, t, s in pts:
        svg += f'<circle cx="{x}" cy="150" r="7" fill="{GREEN if t.isupper() else "#fff"}" stroke="{GREEN}" stroke-width="2"/>'
        svg += f'<text x="{x}" y="{132 if t.isupper() else 178}" text-anchor="middle" font-size="12" font-weight="{"700" if t.isupper() else "400"}">{t}</text>'
    for x1, x2 in ((150, 230), (240, 315), (325, 400), (410, 495)):
        svg += f'<path d="M{x1} 150 Q{(x1 + x2) / 2} 105 {x2} 150" stroke="{BLUE}" stroke-width="1.5" fill="none" stroke-dasharray="5 4"/>'
    svg += f'<text x="105" y="200" text-anchor="middle" fill="{MUTED}" font-size="11.5">1 h before</text><text x="560" y="200" text-anchor="middle" fill="{MUTED}" font-size="11.5">30 min after</text>'
    svg += f'<path d="M60 230 L620 230" stroke="{GREEN}" stroke-width="3" marker-start="url(#t1)" marker-end="url(#t1)"/>'
    svg += f'<text x="335" y="252" text-anchor="middle" fill="{GREEN_D}" font-weight="700">DUTY TIME PERIOD (DTP) — from check-in to check-out</text>'
    svg += f'<path d="M614 290 L690 290" stroke="{BLUE}" stroke-width="3" marker-end="url(#t2)"/><text x="610" y="282" fill="{BLUE}" font-size="12" font-weight="700">then REST</text>'
    svg += f'<text x="30" y="40" font-size="14" font-weight="700">Two pilots: DTP up to 13 h per 24 h · single pilot: 12 h per 24 h</text>'
    svg += f'<text x="30" y="62" fill="{MUTED}" font-size="12">Positioning (as passenger) counts in the DTP but is not a leg.</text>'
    return fig(svg, "The duty time period starts at check-in and ends at check-out. In the course examples, check-in is 1 hour before the first take-off and check-out 30 minutes after the last landing — use the report times in your OM A.",
               "Duty time period timeline", "0 0 700 310")


def legs_staircase():
    svg = ARROW.format(id="s1", c=RED)
    vals = [(1, 780), (2, 780), (3, 750), (4, 720), (5, 690), (6, 660), (7, 660), (8, 660)]
    base_y, scale = 280, 0.3
    for i, (legs, m) in enumerate(vals):
        x = 70 + i * 76
        h = (m - 480) * scale * 2.2
        col = GREEN if legs <= 2 else (AMBER if m > 660 else RED)
        svg += f'<rect x="{x}" y="{base_y - h}" width="52" height="{h}" rx="4" fill="{col}"/>'
        svg += f'<text x="{x + 26}" y="{base_y - h - 8}" text-anchor="middle" font-weight="700" font-size="13">{m // 60}h{m % 60:02d}</text>'
        svg += f'<text x="{x + 26}" y="{base_y + 20}" text-anchor="middle" font-size="12">{legs}{"+" if legs == 8 else ""} leg{"s" if legs > 1 else ""}</text>'
    svg += f'<text x="70" y="30" font-weight="700" font-size="14">Maximum DTP, two pilots, by number of legs</text>'
    svg += f'<text x="70" y="50" fill="{MUTED}" font-size="12">From the 3rd leg (included): − 30 min per leg · maximum reduction 2 h</text>'
    svg += arrow(250, 66, 470, 96, "s1", RED, 2.5)
    svg += f'<text x="480" y="100" fill="{RED}" font-size="12" font-weight="700">− 30 min per leg (max − 2 h)</text>'
    return fig(svg, "Leg reduction: 13 h for 1 or 2 legs, then 30 minutes less for each leg from the third, down to a maximum reduction of 2 hours (11 h for two pilots, 10 h for a single pilot).",
               "Leg reduction staircase", "0 0 700 310")


def wocl_diagram():
    svg = ARROW.format(id="w1", c=RED)
    x0, x1 = 40, 680
    def hx(h):
        return x0 + (x1 - x0) * h / 24
    svg += f'<rect x="{x0}" y="70" width="{x1 - x0}" height="40" rx="5" fill="#eef3f0"/>'
    svg += f'<rect x="{hx(2)}" y="70" width="{hx(6) - hx(2)}" height="40" fill="#1b2a44"/><text x="{(hx(2) + hx(6)) / 2}" y="95" text-anchor="middle" fill="#fff" font-weight="700" font-size="12">WOCL</text><text x="{hx(6) + 8}" y="95" fill="{INK}" font-size="12">02:00–05:59 local</text>'
    for h in range(0, 25, 2):
        svg += f'<text x="{hx(h)}" y="128" text-anchor="middle" fill="{MUTED}" font-size="11">{h:02d}</text>'
    svg += f'<text x="{x0}" y="50" font-weight="700" font-size="14">Window of circadian low (local time)</text>'
    # case A
    svg += f'<rect x="{hx(5)}" y="160" width="{hx(16.5) - hx(5)}" height="22" rx="4" fill="{GREEN}" opacity=".85"/><rect x="{hx(5)}" y="160" width="{hx(6) - hx(5)}" height="22" fill="{RED}"/>'
    svg += f'<text x="{hx(16.5) + 8}" y="176" font-size="12" font-weight="700">STARTS in WOCL → reduce by 100 % of the time in WOCL (max 2 h)</text>'.replace(f'x="{hx(16.5) + 8}"', f'x="{hx(5)}"').replace('y="176"', 'y="200"')
    svg += f'<text x="{hx(5) + 4}" y="176" fill="#fff" font-size="11">1 h</text>'
    # case B
    svg += f'<rect x="{hx(16)}" y="235" width="{hx(24) - hx(16)}" height="22" rx="4" fill="{GREEN}" opacity=".85"/><rect x="{hx(0)}" y="235" width="{hx(4) - hx(0)}" height="22" rx="4" fill="{GREEN}" opacity=".85"/>'
    svg += f'<rect x="{hx(2)}" y="235" width="{hx(4) - hx(2)}" height="22" fill="{AMBER}"/><text x="{hx(2) + 6}" y="251" fill="#fff" font-size="11">2 h</text>'
    svg += f'<text x="{hx(0)}" y="276" font-size="12" font-weight="700">ENDS in WOCL or INCLUDES it → reduce by 50 % of the time in WOCL</text>'
    svg += f'<text x="{hx(16)}" y="228" fill="{MUTED}" font-size="11">duty continues past midnight →</text>'
    return fig(svg, "The WOCL reduction depends on where the duty time period starts. Red: a duty starting at 05:00 has 1 h in the WOCL — reduce the DTP by 1 h (100 %). Amber: a duty ending at 04:00 has 2 h in the WOCL — reduce by 1 h (50 %).",
               "WOCL reductions", "0 0 700 300")


def extension_flow():
    svg = ARROW.format(id="e1", c=MUTED) + ARROW.format(id="e2", c=RED) + ARROW.format(id="e3", c=GREEN)
    svg += box(240, 8, 220, 40, "Need +1 h of DTP?", "#eef6f1", GREEN, bold=True)
    q = [("More than 6 legs?", 70), ("More than 2 h in WOCL AND more than 4 legs?", 140), ("Already 2 extensions in 7 days?", 210)]
    svg += arrow(350, 48, 350, 66)
    for i, (t, y) in enumerate(q):
        svg += box(180, y, 340, 44, t, "#fff", AMBER)
        svg += arrow(520, y + 22, 580, y + 22, "e2", RED) + f'<text x="530" y="{y + 15}" fill="{RED}" font-size="11">YES</text>'
        svg += box(584, y + 4, 106, 36, "NOT allowed", "#fdecee", RED, bold=True, size=12)
        svg += arrow(350, y + 44, 350, y + 66 if i < 2 else y + 66, "e3", GREEN) + f'<text x="358" y="{y + 60}" fill="{GREEN}" font-size="11">NO</text>'
    svg += box(130, 276, 440, 40, "Extension allowed: DTP + 1 h", "#e7f4ec", GREEN, bold=True)
    svg += box(10, 100, 160, 120, "", "#fff", LINE)
    for k, t in enumerate(["With an extension:", "• rest before and after", "  + 2 h", "• or rest after + 4 h", "  (see OM A)"]):
        svg += f'<text x="20" y="{122 + k * 20}" font-size="12"{" font-weight=\"700\"" if k == 0 else ""}>{t}</text>'
    return fig(svg, "Extension of the DTP by 1 hour. A DTP that follows an extension and starts between 22:00 and 04:59 is limited to 11 h 45. Medevac and emergency flights are exempt from these restrictions.",
               "Extension decision flow", "0 0 700 325")


def rest_diagram():
    svg = ARROW.format(id="r1", c=BLUE)
    svg += box(20, 20, 200, 60, "DTP executed", "#e7f4ec", GREEN, bold=True)
    svg += arrow(220, 50, 290, 50, "r1", BLUE, 2.5) + arrow(220, 50, 290, 140, "r1", BLUE, 2.5)
    svg += box(294, 22, 390, 56, "Rest at HOME BASE ≥ DTP executed", "#e9f1fa", BLUE, bold=True, sub="and never less than 12 h")
    svg += box(294, 112, 390, 56, "Rest AWAY from base ≥ DTP executed", "#e9f1fa", BLUE, bold=True, sub="and never less than 10 h")
    svg += box(20, 200, 664, 50, "Every 7 days: 36 consecutive hours of rest, including 2 consecutive nights", "#fff", BLUE, bold=True)
    svg += f'<text x="20" y="282" font-size="12" fill="{MUTED}">Cumulative limits: FDP 60 h / week · 190 h / 28 consecutive days — flight hours 100 h / 28 days · 900 h / year</text>'
    return fig(svg, "Minimum rest depends on the DTP actually flown and on where the rest is taken.", "Rest rules", "0 0 700 300")


def example_timeline(title, ci, to, ll, co, nci, wocl_note=""):
    """Times in minutes from 00:00 of day 1 (can exceed 1440)."""
    x0, x1 = 30, 680
    span0, span1 = (min(ci, 0) // 1440) * 1440, 48 * 60
    def X(m):
        return x0 + (x1 - x0) * (m - span0) / (span1 - span0)
    def hm(m):
        m %= 1440
        return f"{m // 60:02d}:{m % 60:02d}"
    svg = ARROW.format(id="x1", c=GREEN)
    for d in (0, 1440):
        svg += f'<rect x="{X(d + 120)}" y="60" width="{X(d + 360) - X(d + 120)}" height="70" fill="#1b2a44" opacity=".18"/>'
    svg += f'<text x="{X(240)}" y="56" text-anchor="middle" fill="{MUTED}" font-size="10.5">WOCL</text><text x="{X(1680)}" y="56" text-anchor="middle" fill="{MUTED}" font-size="10.5">WOCL</text>'
    svg += f'<rect x="{X(ci)}" y="80" width="{X(co) - X(ci)}" height="30" rx="5" fill="{GREEN}"/><text x="{(X(ci) + X(co)) / 2}" y="100" text-anchor="middle" fill="#fff" font-weight="700" font-size="12">DTP {(co - ci) // 60}h{(co - ci) % 60:02d}</text>'
    svg += f'<rect x="{X(co)}" y="80" width="{X(nci) - X(co)}" height="30" rx="5" fill="{BLUE}" opacity=".85"/><text x="{(X(co) + X(nci)) / 2}" y="100" text-anchor="middle" fill="#fff" font-weight="700" font-size="12">REST {(nci - co) // 60}h{(nci - co) % 60:02d}</text>'
    for m, lab, yy in ((ci, "check-in", 150), (to, "take-off", 170), (ll, "last landing", 150), (co, "check-out", 170), (nci, "next check-in", 150)):
        svg += f'<path d="M{X(m)} 112 L{X(m)} {yy - 12}" stroke="{INK}" stroke-width="1"/><text x="{X(m)}" y="{yy}" text-anchor="middle" font-size="11">{lab} {hm(m)}</text>'
    for h in range(0, 49, 6):
        svg += f'<text x="{X(h * 60)}" y="135" text-anchor="middle" fill="{MUTED}" font-size="10">{h % 24:02d}</text>'
    svg += f'<text x="30" y="30" font-size="13.5" font-weight="700">{title}</text>'
    if wocl_note:
        svg += f'<text x="30" y="200" font-size="12" fill="{RED}">{wocl_note}</text>'
    return fig(svg, "", title, "0 0 700 210")


# ------------------------------------------------------------------ interactive calculator (lesson 7)
CALC = r"""
<figure class="diagram dtcalc" id="dtcalc">
<style>
.dtcalc .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin-bottom:14px}
.dtcalc label{display:block;font-size:.85rem;color:var(--muted,#5b6b62);margin-bottom:4px;font-weight:600}
.dtcalc input,.dtcalc select{width:100%;padding:9px 10px;border:1px solid #cfdcd4;border-radius:8px;font-size:1rem;background:#fff;color:#24342b}
.dtcalc .chk{display:flex;align-items:center;gap:8px;font-size:.9rem;margin-top:24px}
.dtcalc .chk input{width:auto}
.dtcalc table{width:100%;border-collapse:collapse;margin:10px 0}
.dtcalc td{padding:7px 8px;border-bottom:1px solid #e3ebe6;font-size:.95rem}
.dtcalc td.v{text-align:right;font-weight:700;white-space:nowrap}
.dtcalc tr.tot td{background:#e7f4ec;font-size:1.05rem}
.dtcalc .warn{background:#fdecee;border-left:4px solid #c8102e;padding:8px 12px;border-radius:6px;margin:6px 0;font-size:.92rem}
.dtcalc .ok{background:#e7f4ec;border-left:4px solid #1d7a3e;padding:8px 12px;border-radius:6px;margin:6px 0;font-size:.92rem}
.dtcalc .btn{margin:4px 6px 4px 0}
.dtcalc svg text{font-family:system-ui,Segoe UI,Arial,sans-serif}
</style>
<h3 style="margin-top:0">Duty time calculator</h3>
<div class="grid">
  <div><label for="dt-crew">Flight crew</label><select id="dt-crew"><option value="780">Two pilots (13 h)</option><option value="720">Single pilot (12 h)</option></select></div>
  <div><label for="dt-legs">Number of legs</label><input id="dt-legs" type="number" min="1" max="12" value="4"></div>
  <div><label for="dt-to">First take-off (local time)</label><input id="dt-to" type="time" value="08:15"></div>
  <div><label for="dt-rep">Check-in before take-off (min)</label><input id="dt-rep" type="number" min="0" max="180" value="60"></div>
  <div><label for="dt-post">Check-out after landing (min)</label><input id="dt-post" type="number" min="0" max="120" value="30"></div>
  <div><label for="dt-rest">Rest taken</label><select id="dt-rest"><option value="720">At home base (min 12 h)</option><option value="600">Away from base (min 10 h)</option></select></div>
  <div><label for="dt-land">Planned last landing (optional)</label><input id="dt-land" type="time" value=""></div>
  <div class="chk"><input id="dt-ext" type="checkbox"><label for="dt-ext" style="margin:0">Use a 1 h extension</label></div>
  <div class="chk"><input id="dt-prevext" type="checkbox"><label for="dt-prevext" style="margin:0">Previous DTP was extended</label></div>
</div>
<div id="dt-out"></div>
<div id="dt-svg"></div>
<p class="muted" style="font-size:.85rem">Calculation tool for training, based on the Algerian regulation as taught in this course. It does not replace the OM A FTL chapter or the crew planning system; where rules differ, the most restrictive applies.</p>
<hr style="border:none;border-top:1px solid #e3ebe6;margin:18px 0">
<h3>Practice exercises</h3>
<p id="ex-q" style="font-size:1rem"></p>
<div class="grid">
  <div><label for="ex-dtp">Maximum DTP (h:mm)</label><input id="ex-dtp" placeholder="e.g. 11:30"></div>
  <div><label for="ex-co">Latest check-out (hh:mm)</label><input id="ex-co" placeholder="e.g. 17:00"></div>
  <div><label for="ex-nci">Earliest next check-in after max DTP (hh:mm)</label><input id="ex-nci" placeholder="e.g. 05:00"></div>
</div>
<button type="button" class="btn primary" id="ex-check">Check my answer</button><button type="button" class="btn" id="ex-new">New exercise</button><button type="button" class="btn" id="ex-show">Show the solution</button>
<div id="ex-res"></div>
<script>
(function(){
  var W0=120, W1=360;                       // WOCL 02:00-05:59 local
  function pad(n){return (n<10?'0':'')+n}
  function hm(m){m=((Math.round(m)%1440)+1440)%1440;return pad(Math.floor(m/60))+':'+pad(m%60)}
  function dur(m){m=Math.round(m);var s=m<0?'-':'';m=Math.abs(m);return s+Math.floor(m/60)+'h'+pad(m%60)}
  function parseT(v){if(!v)return null;var p=v.split(':');if(p.length<2)return null;return (+p[0])*60+(+p[1])}
  function parseD(v){if(!v)return null;v=v.replace('h',':').replace('H',':');var p=v.split(':');return (+p[0])*60+(+(p[1]||0))}
  function woclOverlap(a,b){var t=0;for(var d=-1440;d<=2880;d+=1440){var s=Math.max(a,d+W0),e=Math.min(b,d+W1);if(e>s)t+=e-s}return t}
  function inWocl(m){m=((m%1440)+1440)%1440;return m>=W0&&m<W1}
  function compute(o){
    var r={steps:[],warn:[],info:[]};
    var base=o.base, legRed=Math.min(Math.max(o.legs-2,0)*30,120), avail=base-legRed;
    r.steps.push(['Basic limit ('+(base==780?'two pilots':'single pilot')+')',dur(base)]);
    r.steps.push(['Leg reduction: '+o.legs+' leg'+(o.legs>1?'s':'')+(o.legs>2?' → '+(o.legs-2)+' × 30 min'+(legRed==120?' (max 2 h)':''):' (none for 1–2 legs)'),legRed?'− '+dur(legRed):'0']);
    var S=o.ci, wred=0, D=avail, wtxt='';
    if(inWocl(S)){
      var start=((S%1440)+1440)%1440, inside=Math.min(W1-start, D);
      wred=Math.min(inside,120); D=avail-wred;
      wtxt='Starts in the WOCL: '+dur(inside)+' inside × 100 %'+(inside>120?' (max 2 h)':'');
    } else {
      for(var i=0;i<200;i++){var ov=woclOverlap(S,S+D);var nd=avail-ov/2;if(Math.abs(nd-D)<1e-6){D=nd;break}D=nd}
      D=Math.round(D); wred=avail-D; var ov2=woclOverlap(S,S+D);
      wtxt=ov2>0?'Ends in / includes the WOCL: '+dur(ov2)+' inside × 50 %':'No WOCL in the duty';
    }
    r.steps.push(['WOCL reduction — '+wtxt, wred?'− '+dur(wred):'0']);
    var ovFinal=woclOverlap(S,S+D);
    if(o.ext){
      var bad=[];
      if(o.legs>6)bad.push('more than 6 legs');
      if(ovFinal>120&&o.legs>4)bad.push('more than 2 h in the WOCL with more than 4 legs');
      if(bad.length){r.warn.push('Extension NOT permitted: '+bad.join(' and ')+'.')}
      else{D+=60;r.steps.push(['Extension (+1 h): rest before and after + 2 h (or rest after + 4 h — see OM A); max 2 per 7 days','+ 1h00'])}
    }
    var st=((S%1440)+1440)%1440;
    if(o.prevext&&(st>=1320||st<300)&&D>705){r.steps.push(['Previous DTP extended and this one starts 22:00–04:59 → limit 11 h 45','− '+dur(D-705)]);D=705}
    r.D=D; r.co=S+D; r.ll=r.co-o.post;
    var actual=D;
    if(o.land!=null){var L=o.land; while(L<o.to)L+=1440; actual=L+o.post-S; r.actual=actual;
      if(actual>D)r.warn.push('Planned duty '+dur(actual)+' EXCEEDS the maximum '+dur(D)+' by '+dur(actual-D)+'.');
      else r.info.push('Planned duty '+dur(actual)+' is within the maximum (margin '+dur(D-actual)+').')}
    var rest=Math.max(actual,o.restMin); r.rest=rest; r.nci=S+actual+rest;
    r.restTxt='Minimum rest = DTP flown ('+dur(actual)+') but not less than '+dur(o.restMin)+(o.restMin==720?' (home base)':' (away)')+' → '+dur(rest);
    return r;
  }
  function read(){
    var to=parseT(document.getElementById('dt-to').value)||0, rep=+document.getElementById('dt-rep').value||0;
    return {base:+document.getElementById('dt-crew').value, legs:Math.max(1,+document.getElementById('dt-legs').value||1), to:to, ci:to-rep,
      post:+document.getElementById('dt-post').value||0, restMin:+document.getElementById('dt-rest').value, land:parseT(document.getElementById('dt-land').value),
      ext:document.getElementById('dt-ext').checked, prevext:document.getElementById('dt-prevext').checked};
  }
  function timeline(o,r){
    var a=Math.floor(o.ci/1440)*1440-0, span=2880, X=function(m){return 20+660*(m-a)/span};
    var s='<svg viewBox="0 0 700 150" role="img" aria-label="Duty and rest timeline">';
    for(var d=a;d<a+span;d+=1440){s+='<rect x="'+X(d+W0)+'" y="30" width="'+(X(d+W1)-X(d+W0))+'" height="60" fill="#1b2a44" opacity=".18"/><text x="'+X(d+240)+'" y="26" text-anchor="middle" font-size="10" fill="#5b6b62">WOCL</text>'}
    var end=o.ci+(r.actual!=null?r.actual:r.D);
    s+='<rect x="'+X(o.ci)+'" y="40" width="'+Math.max(2,X(o.ci+r.D)-X(o.ci))+'" height="16" rx="3" fill="#cfe5d6"/>';
    s+='<rect x="'+X(o.ci)+'" y="58" width="'+Math.max(2,X(end)-X(o.ci))+'" height="22" rx="4" fill="'+(r.actual!=null&&r.actual>r.D?'#c8102e':'#1d7a3e')+'"/>';
    s+='<rect x="'+X(end)+'" y="58" width="'+Math.max(2,X(r.nci)-X(end))+'" height="22" rx="4" fill="#1f5f99" opacity=".85"/>';
    s+='<text x="'+X(o.ci)+'" y="104" font-size="11" text-anchor="middle">check-in '+hm(o.ci)+'</text>';
    s+='<text x="'+X(o.ci+r.D)+'" y="36" font-size="11" text-anchor="middle" fill="#125a2b">max '+hm(o.ci+r.D)+'</text>';
    s+='<text x="'+X(end)+'" y="120" font-size="11" text-anchor="middle">check-out '+hm(end)+'</text>';
    s+='<text x="'+X(r.nci)+'" y="104" font-size="11" text-anchor="middle" fill="#1f5f99">next check-in '+hm(r.nci)+'</text>';
    for(var h=0;h<=48;h+=6)s+='<text x="'+X(a+h*60)+'" y="142" font-size="10" text-anchor="middle" fill="#5b6b62">'+pad(h%24)+'</text>';
    s+='<text x="20" y="14" font-size="11" fill="#5b6b62">light green = maximum DTP · green = DTP planned · blue = minimum rest</text>';
    return s+'</svg>';
  }
  function render(){
    var o=read(), r=compute(o), h='<table>';
    h+='<tr><td>Check-in</td><td class="v">'+hm(o.ci)+'</td></tr>';
    r.steps.forEach(function(s){h+='<tr><td>'+s[0]+'</td><td class="v">'+s[1]+'</td></tr>'});
    h+='<tr class="tot"><td>MAXIMUM DTP</td><td class="v">'+dur(r.D)+'</td></tr>';
    h+='<tr><td>Latest check-out</td><td class="v">'+hm(r.co)+'</td></tr>';
    h+='<tr><td>Latest last landing (check-out − '+o.post+' min)</td><td class="v">'+hm(r.ll)+'</td></tr>';
    h+='<tr><td>'+r.restTxt+'</td><td class="v">'+dur(r.rest)+'</td></tr>';
    h+='<tr><td>Earliest next check-in</td><td class="v">'+hm(r.nci)+'</td></tr></table>';
    r.warn.forEach(function(w){h+='<div class="warn">'+w+'</div>'});
    r.info.forEach(function(w){h+='<div class="ok">'+w+'</div>'});
    if(o.ext)h+='<div class="ok">With an extension the rest before and after the flight increases (see Lesson 5 and the OM A).</div>';
    document.getElementById('dt-out').innerHTML=h;
    document.getElementById('dt-svg').innerHTML=timeline(o,r);
  }
  ['dt-crew','dt-legs','dt-to','dt-rep','dt-post','dt-rest','dt-land','dt-ext','dt-prevext'].forEach(function(id){var e=document.getElementById(id);e.addEventListener('input',render);e.addEventListener('change',render)});
  render();
  // ---- practice exercises
  var ex=null;
  function newEx(){
    var legs=1+Math.floor(Math.random()*6), slots=[300,330,360,390,420,480,540,600,720,900,1020,1080,1140];
    var to=slots[Math.floor(Math.random()*slots.length)], home=Math.random()<.6;
    ex={base:780,legs:legs,to:to,ci:to-60,post:30,restMin:home?720:600,land:null,ext:false,prevext:false};
    ex.r=compute(ex);
    document.getElementById('ex-q').innerHTML='<strong>Exercise:</strong> two-pilot crew, <strong>'+legs+' leg'+(legs>1?'s':'')+'</strong>, first take-off <strong>'+hm(to)+'</strong> local, check-in 1 h before, check-out 30 min after the last landing, rest '+(home?'at home base':'away from base')+'. Find the maximum DTP, the latest check-out and the earliest next check-in if the maximum DTP is flown.';
    ['ex-dtp','ex-co','ex-nci'].forEach(function(i){document.getElementById(i).value=''});
    document.getElementById('ex-res').innerHTML='';
  }
  function solution(){var r=ex.r;return 'Solution: '+r.steps.map(function(s){return s[0]+' '+s[1]}).join(' · ')+' → <strong>maximum DTP '+dur(r.D)+'</strong>; check-in '+hm(ex.ci)+' → latest check-out <strong>'+hm(r.co)+'</strong>; '+r.restTxt+' → next check-in <strong>'+hm(r.nci)+'</strong>.'}
  document.getElementById('ex-new').onclick=newEx;
  document.getElementById('ex-show').onclick=function(){document.getElementById('ex-res').innerHTML='<div class="ok">'+solution()+'</div>'};
  document.getElementById('ex-check').onclick=function(){
    var r=ex.r, a=parseD(document.getElementById('ex-dtp').value), b=parseT(document.getElementById('ex-co').value), c=parseT(document.getElementById('ex-nci').value);
    var ok=function(x,y){return x!=null&&Math.abs(((x-y)%1440+1440+720)%1440-720)<=5};
    var res=[(ok(a,r.D)?'✔':'✘')+' Maximum DTP', (ok(b,r.co)?'✔':'✘')+' Latest check-out', (ok(c,r.nci)?'✔':'✘')+' Next check-in'];
    var all=ok(a,r.D)&&ok(b,r.co)&&ok(c,r.nci);
    document.getElementById('ex-res').innerHTML='<div class="'+(all?'ok':'warn')+'">'+res.join(' &nbsp; ')+(all?' — well done!':'')+'</div>'+(all?'':'<div class="ok">'+solution()+'</div>');
  };
  newEx();
})();
</script>
</figure>
"""

LESSONS = [
dict(title="The Algerian Legal Framework and the ANAC", minutes=8,
objectives=["Rank the Algerian legal texts from the Constitution to circulars.", "Describe the role of the civil aviation authority (ANAC).", "Locate the ICAO standards in Algerian laws, decrees and circulars."],
body="""
<h2>Algeria and international aviation law</h2>
<p>The People's Democratic Republic of Algeria applies the ICAO Standards and Recommended Practices (SARPs). The ICAO Annexes are in force <strong>except where a difference is published</strong>. PANS-OPS (Doc 8168 Volumes I and II), the Regional Supplementary Procedures (Doc 7030) and Doc 4444 are also used.</p>
<div class="table-wrap"><table>
<tr><th>Convention or treaty</th><th>Signed by Algeria</th></tr>
<tr><td>ICAO</td><td>07/05/1963</td></tr><tr><td>Chicago</td><td>06/06/1963</td></tr><tr><td>Rome</td><td>12/07/1964</td></tr>
<tr><td>Warsaw</td><td>31/08/1964</td></tr><tr><td>Geneva</td><td>08/11/1964</td></tr><tr><td>Montreal</td><td>29/11/1965</td></tr>
</table></div>

<h2>The hierarchy of texts</h2>
""" + hierarchy() + """
<ul>
  <li><strong>Law</strong> — voted by the Assembly, applicable as soon as it is published in the Official Journal.</li>
  <li><strong>Decree</strong> — a government act, without consultation of the Assembly, signed by the President or the Prime Minister.</li>
  <li><strong>Order (arrêté)</strong> — an administrative decision; it can be specific to an activity or a geographical area.</li>
  <li><strong>Circular</strong> — the lowest level; in principle it has no legal value of its own and only explains how laws, decrees and orders apply.</li>
</ul>

<h2>The authority: ANAC</h2>
<p>The <strong>ANAC</strong> (Agence Nationale de l'Aviation Civile — National Civil Aviation Agency) is the civil aviation authority in Algeria. Texts issued under the former authority keep their original references, for example <em>Instruction 771/DACM</em> or <em>Circular 1830/DACM</em>. The ANAC:</p>
<ul>
  <li>applies in Algeria the international conventions and treaties signed by the government;</li>
  <li>applies the laws and executes the decrees, and supervises and controls all air transport activities;</li>
  <li>issues and controls flight crew licences, in accordance with ICAO Annex 1 and national regulation.</li>
</ul>
<div class="callout info"><span class="label">ANAC website</span><p>Regulations, circulars, forms and news of the Algerian civil aviation authority: <a href="https://www.anac.dz/fr/accueil-2/" target="_blank" rel="noopener">www.anac.dz</a> (opens in a new tab).</p></div>
<p>The main reference laws are <strong>Laws 98-06, 64-166, 08-02 and 15-14</strong>, together with their decrees. Aeronautical information is published by the AIS (SIA) of Algeria.</p>

<h2>Where the ICAO standards are found</h2>
""" + icao_map() + """
<div class="callout"><span class="label">Most restrictive rule</span><p>Algerian laws and decrees also affect foreign operators in Algeria. When the Algerian rule and another regulation (European or foreign) differ, <strong>the most restrictive one applies</strong>.</p></div>
""",
takeaways=["Constitution → laws → decrees → orders → circulars.", "ICAO Annexes apply unless a difference is published (AIP GEN 1.7).", "The ANAC supervises air transport and issues licences.", "Annex 6 standards: Executive Decrees 09-206/207/208, Instruction 771, Circular 1830."],
check=dict(q="Which text has the lowest level in the Algerian hierarchy?", options=["Decree", "Order (arrêté)", "Circular", "Law"], answer=2, explain="A circular only explains how the higher texts apply."),
),

dict(title="Differences from ICAO Standards", minutes=9,
objectives=["Find where the Algerian differences are published.", "Apply the main differences to Annexes 1, 2, 4, 9, 10, 11, 12, 13 and 15.", "Apply the differences to Doc 4444 and Doc 8400."],
body="""
<h2>Where to find them</h2>
<p>The differences from ICAO SARPs are published in <strong>AIP Algeria GEN 1.7</strong> and in the <strong>Jeppesen Airway Manual</strong> (Air Traffic Control — State Rules and Procedures — Africa). Annex 6 (Operation of Aircraft): no difference. The national texts are on the ANAC website: <a href="https://www.anac.dz/fr/accueil-2/" target="_blank" rel="noopener">www.anac.dz</a>.</p>

<h2>Annex 2 — Rules of the Air</h2>
<div class="table-wrap"><table>
<tr><th>Subject</th><th>Algerian rule</th></tr>
<tr><td>Fitness to fly</td><td>A crew member who feels unfit to fly shall not act as a pilot or crew member.</td></tr>
<tr><td>Minimum height</td><td>Except over cities, assemblies of people or dense constructions: not below <strong>150 m (500 ft)</strong> above ground, water or the highest obstacle.</td></tr>
<tr><td>IFR minimum height</td><td>At least <strong>1,500 ft (450 m)</strong> above the highest obstacle within <strong>8 km (4.3 NM)</strong> of the estimated position.</td></tr>
<tr><td>Prohibited area entered</td><td>Advise ATC, leave the area and land as soon as possible at the nearest aerodrome — or the aircraft may be forced to land by the military.</td></tr>
<tr><td>Flight plan</td><td>Required for <strong>all IFR flights</strong> and for every flight (VFR or IFR) <strong>over desert areas and the sea</strong>.</td></tr>
<tr><td>ETD in the flight plan</td><td>The time the aircraft is ready to leave the parking stand.</td></tr>
</table></div>

<h2>Other Annexes</h2>
<div class="table-wrap"><table>
<tr><th>Reference</th><th>Algerian difference</th></tr>
<tr><td>Annex 1 — Licensing</td><td>Algeria does not apply the <strong>multi-crew pilot licence (MPL)</strong>.</td></tr>
<tr><td>Annex 4 — Charts</td><td>Some 1:500,000 charts published in Algeria do not conform to Chapter 10 and are not labelled ICAO.</td></tr>
<tr><td>Annex 9 — Facilitation</td><td>No crew member certificate to the Appendix 7 model; crews not on regular international services need a valid passport and possibly a visa.</td></tr>
<tr><td>Annex 10 — Communications</td><td>Conform to the SARPs; Annex 10 Volume II procedures apply with the Algerian authority.</td></tr>
<tr><td>Annex 11 — ATS</td><td>Alerting (emergency phases) in the Algiers FIR follows a specific instruction, with delays adapted to desert and maritime areas.</td></tr>
<tr><td>Annex 12 — SAR</td><td>Foreign SAR teams need a special permission.</td></tr>
<tr><td>Annexes 13 and 15</td><td>Applicable; some aeronautical publications may be without English translation; international NOTAMs are translated into English as far as possible.</td></tr>
<tr><td>Doc 8400 — Abbreviations</td><td>QAN (wind direction) is referenced to <strong>true north</strong>; QNH is never given in inches of mercury.</td></tr>
<tr><td>Doc 4444 — ATM</td><td>Minimum obstacle clearance <strong>1,500 ft (450 m)</strong> instead of 1,000 ft; special VFR not authorised below 1.5 km visibility (except helicopters); flight plan changes take effect only when acknowledged by ATC.</td></tr>
</table></div>
""",
takeaways=["Differences: AIP Algeria GEN 1.7 and Jeppesen State Rules.", "IFR minimum height 1,500 ft within 8 km; minimum height 500 ft.", "Flight plan for all IFR flights and any flight over desert or sea.", "No MPL in Algeria; QNH never in inches."],
check=dict(q="What is the minimum obstacle clearance for IFR flight in Algeria?", options=["1,000 ft within 5 NM", "1,500 ft (450 m) within 8 km (4.3 NM)", "2,000 ft within 5 NM", "500 ft within 8 km"], answer=1, explain="Algeria requires 1,500 ft above the highest obstacle within 8 km of the estimated position."),
),

dict(title="Flight Procedures, VFR and Fuel", minutes=9,
objectives=["Apply the Algerian holding speeds, airspace, altimeter and communication rules.", "State the night VFR conditions.", "Calculate the fuel with the Algerian final reserve for jets and propeller aircraft."],
body="""
<h2>Flight procedures</h2>
<ul>
  <li><strong>Holding speeds</strong>: in accordance with Doc 8168 (table below).</li>
  <li><strong>Instrument approaches</strong>: PANS-OPS Doc 8168 Volume II. Algeria publishes state aerodrome operating minima for landing and take-off.</li>
  <li><strong>Airspace</strong>: only classes <strong>A, D and E</strong> are used.</li>
  <li><strong>Altimeter settings</strong>: international aerodromes give QNH and QFE; <strong>domestic aerodromes give QFE only</strong> (QNH on request).</li>
  <li><strong>121.5 MHz</strong>: listening watch outside controlled airspace and within 27 NM of restricted, prohibited or danger areas, especially near the FIR boundary.</li>
  <li><strong>ACAS II</strong>: required for turbine aircraft of 5,700 kg MTOW or more, or authorised to carry more than 19 passengers (version 7.1 in EU airspace).</li>
  <li><strong>CPDLC</strong>: log on to <strong>DAAA</strong> 15–30 minutes before entering the Algiers FIR (flight ID and registration as in the flight plan); log off 5 minutes after leaving it.</li>
  <li><strong>Flight plans to Europe</strong>: IFPS/CFMU addressing (AFTN EUCHZMFP, EUCBZMFP; SITA BRUEP7X, PAREP7X).</li>
</ul>
<div class="table-wrap"><table>
<tr><th>Levels</th><th>Normal conditions</th><th>Turbulence</th></tr>
<tr><td>Up to 14,000 ft inclusive</td><td>230 kt (170 kt CAT A/B)</td><td>280 kt (170 kt CAT A/B)</td></tr>
<tr><td>Above 14,000 to 34,000 ft</td><td>240 kt</td><td>280 kt or M0.80, whichever is less</td></tr>
<tr><td>Above 34,000 ft</td><td>M0.83</td><td>M0.83</td></tr>
</table></div>
<p class="muted">Turbulence holding speeds only with ATC clearance unless the published holding allows them.</p>

<h2>VFR and night VFR</h2>
<ul>
  <li>Special VFR is <strong>not allowed</strong> for fixed-wing aircraft.</li>
  <li>VFR is prohibited in class A airspace, above FL195 and whenever ATC suspends VFR.</li>
</ul>
""" + night_diagram() + """
<ul>
  <li>Cruise: at least 650 m above the highest obstacle within 8 km (450 m in some cases); semicircular levels above 900 m MSL or 650 m AGL.</li>
  <li>Not inside airways without ATC authorisation; published tracks in other controlled airspace; flight plan filed 30 minutes before ETD; continuous VHF watch.</li>
</ul>

<h2>Fuel</h2>
""" + fuel_diagram() + """
""",
takeaways=["Airspace classes A, D, E only; domestic aerodromes give QFE.", "CPDLC: log on DAAA 15–30 min before the Algiers FIR, log off 5 min after.", "Night = end of civil twilight to civil dawn; night VFR only for IFR-rated pilots.", "Final reserve: jets 30 min, propeller aircraft 45 min."],
check=dict(q="What is the Algerian final reserve fuel for a Dash 8-Q400?", options=["30 minutes", "45 minutes", "60 minutes", "5 % of trip fuel"], answer=1, explain="Propeller aircraft: 45 minutes; jets: 30 minutes."),
),

dict(title="Duty Time: References, Limits and Legs", minutes=8,
objectives=["Name the legal references of Algerian duty time.", "Apply the basic DTP limits and the leg reduction.", "State the cumulative flight duty and flight time limits."],
body="""
<h2>References</h2>
<p>Constitution (articles 85-3° and 125); Law 90-11 of 21/04/1990 (amended); Law 98-06 of 27/06/1998; Decree 02-89; Decree 04-414 of 20/12/2004; Decree 10-140 of 23/05/2010. The company OM A FTL chapter applies these rules; where rules differ, the most restrictive applies.</p>

<h2>The duty time period (DTP)</h2>
""" + dtp_timeline() + """
<h2>Leg reduction</h2>
""" + legs_staircase() + """
<div class="callout info"><span class="label">How to calculate</span><p>Maximum DTP = basic limit (13 h two pilots / 12 h single pilot) − 30 min × (legs − 2), with a maximum reduction of 2 h. Example: 4 legs, two pilots → 13 h − 1 h = <strong>12 h</strong>.</p></div>

<h2>Cumulative limits</h2>
<div class="table-wrap"><table>
<tr><th>Limit</th><th>Flight duty (FDP)</th><th>Flight hours</th></tr>
<tr><td>7 days (week)</td><td>60 h</td><td>—</td></tr>
<tr><td>28 consecutive days</td><td>190 h</td><td>100 h</td></tr>
<tr><td>Year</td><td>—</td><td>900 h</td></tr>
</table></div>
""",
takeaways=["DTP runs from check-in to check-out: 13 h two pilots, 12 h single pilot.", "From the 3rd leg: −30 min per leg, maximum −2 h.", "Positioning counts in the DTP but not as a leg.", "60 h / week and 190 h / 28 days duty; 100 h / 28 days and 900 h / year flight time."],
check=dict(q="A two-pilot crew plans 5 legs. What is the maximum DTP before any WOCL reduction?", options=["13h00", "12h00", "11h30", "11h00"], answer=2, explain="13 h − 3 × 30 min = 11 h 30."),
),

dict(title="Window of Circadian Low, Extensions and the Commander's Authority", minutes=9,
objectives=["Apply the WOCL reductions for duties that start in, end in or include the WOCL.", "Decide whether a 1 h extension is permitted.", "Describe the commander's authority and the waivers."],
body="""
<h2>The window of circadian low (WOCL)</h2>
<p>The WOCL is the period from <strong>02:00 to 05:59 local time</strong>, when the body is least alert.</p>
""" + wocl_diagram() + """
<ol class="steps">
  <li><strong>DTP starts in the WOCL</strong> → reduce by <strong>100 %</strong> of the time spent in the WOCL, up to <strong>2 h</strong>. Check-in 05:30 → 30 min in the WOCL → −30 min.</li>
  <li><strong>DTP ends in the WOCL, or includes all of it</strong> → reduce by <strong>50 %</strong> of the time spent in the WOCL. Check-out 04:00 → 2 h in the WOCL → −1 h.</li>
</ol>
<div class="callout info"><span class="label">Tip</span><p>When the duty ends in the WOCL, the reduction changes the end time, which changes the time in the WOCL. Work it out step by step — or use the calculator in Lesson 7, which solves it for you.</p></div>

<h2>Extension of the DTP</h2>
""" + extension_flow() + """
<ul>
  <li>When extensions are used on two consecutive DTPs, the rest due before and after the flight is taken in a row.</li>
  <li>All these restrictions are cancelled for <strong>medevac and emergency flights</strong>.</li>
</ul>

<h2>Commander's authority</h2>
<ul>
  <li>After consulting the crew and with their agreement, the commander may increase the DTP by up to <strong>2 h</strong> (crew not reinforced).</li>
  <li>If, on the last leg, unforeseen conditions after take-off would exceed the authorised extension, the flight may continue to the destination or the alternate.</li>
  <li>The commander may reduce or extend the DTP, or extend the rest, in case of severe crew fatigue.</li>
  <li>When a DTP or a rest is extended or reduced by 1 h, a copy of the commander's report is sent to the Authority within <strong>28 days</strong>.</li>
</ul>

<h2>Waivers by the Authority</h2>
<p>Urgent (SAR) flights, rescue flights for aircraft maintenance, finishing a flight after unforeseen conditions, national interest or defence flights, and high company workload — provided the DTP limit is not exceeded by more than 20 h in 28 days and 100 h in a year.</p>
""",
takeaways=["WOCL = 02:00–05:59 local.", "Starts in WOCL: −100 % of the time inside (max 2 h); ends in / includes WOCL: −50 %.", "+1 h extension: not with more than 6 legs, nor with more than 2 h in WOCL and more than 4 legs; max 2 per 7 days.", "Commander: up to +2 h with crew agreement; report to the Authority within 28 days."],
check=dict(q="A duty starts at 05:00 local. How much WOCL reduction applies?", options=["None", "30 min (50 % of 1 h)", "1 h (100 % of 1 h)", "2 h"], answer=2, explain="It starts in the WOCL: 05:00–06:00 = 1 h inside, reduced by 100 % = 1 h."),
),

dict(title="Rest Periods and Worked Examples", minutes=9,
objectives=["Calculate the minimum rest at home base and away from base.", "Apply the weekly rest rule.", "Work through complete duty and rest examples."],
body="""
<h2>Rest rules</h2>
""" + rest_diagram() + """
<h2>Example 1 — day duty, 4 legs</h2>
<p>Two pilots, first take-off 08:15, 4 legs. Maximum DTP: 13 h − 1 h (4 legs) = <strong>12 h</strong>. Check-in 07:15 → latest check-out 19:15 → latest last landing 18:45. Rest at base: 12 h → next check-in 07:15.</p>
""" + example_timeline("Example 1 — take-off 08:15, 4 legs: DTP 12h00", 435, 495, 1125, 1155, 1875) + """
<h2>Example 2 — early start in the WOCL, 4 legs</h2>
<p>First take-off 06:30, check-in 05:30 → 30 min in the WOCL × 100 % = −30 min. Maximum DTP: 12 h (4 legs) − 30 min = <strong>11 h 30</strong>. Latest check-out 17:00 → latest last landing 16:30. Rest at base 12 h → next check-in 05:00.</p>
""" + example_timeline("Example 2 — take-off 06:30, 4 legs: DTP 11h30", 330, 390, 990, 1020, 1740, "Check-in 05:30 is inside the WOCL: −100 % of 30 min") + """
<h2>Example 3 — night duty ending in the WOCL, 3 legs</h2>
<p>VIP flight with 3 legs, landing at 03:30, check-out 04:00 → 2 h in the WOCL × 50 % = −1 h. Maximum DTP: 12 h 30 (3 legs) − 1 h = <strong>11 h 30</strong>. Check-in 16:30, take-off 17:30. Rest 12 h → next check-in 16:00.</p>
""" + example_timeline("Example 3 — take-off 17:30, 3 legs, landing 03:30: DTP 11h30", 990, 1050, 1650, 1680, 2400, "Check-out 04:00 is inside the WOCL: −50 % of 2 h") + """
""",
takeaways=["Rest at base ≥ DTP flown, minimum 12 h; away ≥ DTP flown, minimum 10 h.", "Every 7 days: 36 consecutive hours including 2 nights.", "Method: basic limit → legs → WOCL → extension → check-out → rest."],
check=dict(q="A crew finishes an 11 h 30 duty away from base. What is the minimum rest?", options=["10h00", "11h30", "12h00", "36h00"], answer=1, explain="Rest away from base ≥ DTP flown (11 h 30), and not less than 10 h."),
),

dict(title="Interactive Duty Time Calculator", minutes=12,
objectives=["Calculate a maximum DTP for any number of legs and start time.", "Check a planned duty and the rest that follows.", "Practise with exercises until the method is automatic."],
body="""
<h2>Use the calculator</h2>
<p>Enter the crew, the number of legs and the first take-off time. The calculator applies the leg reduction, the WOCL reduction and the extension rules step by step, then draws the duty and rest on a timeline. Change the values and watch the result change.</p>
<ol class="steps">
  <li>Try the three examples of Lesson 6 and check that you obtain the same results.</li>
  <li>Move the first take-off from 08:00 to 05:00 with 4 legs and watch the WOCL reduction appear.</li>
  <li>Enter a planned last landing to check whether a roster respects the limit.</li>
</ol>
""" + CALC + """
<h2>Remember the method</h2>
<ol class="steps">
  <li><strong>Basic limit</strong>: 13 h (two pilots) or 12 h (single pilot).</li>
  <li><strong>Legs</strong>: −30 min per leg from the third, maximum −2 h.</li>
  <li><strong>WOCL</strong>: −100 % of the time inside if the duty starts in the WOCL (max 2 h); −50 % if it ends in or includes it.</li>
  <li><strong>Extension</strong>: +1 h only if permitted.</li>
  <li><strong>Check-out and rest</strong>: rest ≥ DTP flown, minimum 12 h at base or 10 h away.</li>
</ol>
""",
takeaways=["Basic limit → legs → WOCL → extension → rest.", "Use the calculator to check rosters; the OM A and the crew planning system remain the reference."],
check=dict(q="Two pilots, 6 legs, take-off 09:00, check-in 08:00. Maximum DTP?", options=["13h00", "11h30", "11h00", "10h00"], answer=2, explain="13 h − 4 × 30 min = 11 h; no WOCL in the duty."),
),
]


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


QUESTIONS = [
Q(1, "What is the highest legal text in Algeria?", ["The ANAC circular", "The Constitution", "The decree", "The law"], 1, "The Constitution, with the international conventions and treaties."),
Q(1, "Who signs a decree?", ["The Assembly", "The President or the Prime Minister", "The ANAC", "The airline"], 1, "A decree is a government act signed by the President or the Prime Minister."),
Q(1, "Which body is the Algerian civil aviation authority?", ["The AIS", "The ANAC", "The airport operator", "ICAO"], 1, "The ANAC."),
Q(1, "When an Algerian rule and a foreign rule differ, which applies?", ["The foreign one", "The Algerian one always", "The most restrictive one", "The operator chooses"], 2, "The most restrictive rule applies."),
Q(2, "Where are the Algerian differences from ICAO published?", ["AIP Algeria GEN 1.7 (and Jeppesen State Rules)", "Annex 6", "The OM B", "The NOTAM only"], 0, "AIP GEN 1.7 and the Jeppesen Airway Manual."),
Q(2, "A flight plan is required in Algeria for:", ["IFR flights only", "All IFR flights and any flight over desert or sea", "International flights only", "Night flights only"], 1, "All IFR flights and every flight over desert areas and the sea."),
Q(2, "Does Algeria apply the multi-crew pilot licence (MPL)?", ["Yes", "No", "Only for the B737", "Only for cadets"], 1, "Algeria does not apply the MPL."),
Q(3, "Which airspace classes are used in Algeria?", ["A, B, C", "A, D, E", "C, D, G", "All classes"], 1, "Only classes A, D and E."),
Q(3, "At a domestic Algerian aerodrome, which altimeter setting is given?", ["QNH only", "QFE only (QNH on request)", "QNE", "Inches of mercury"], 1, "Domestic aerodromes give QFE; QNH on request."),
Q(3, "When do you log on to CPDLC with DAAA?", ["At engine start", "15 to 30 minutes before entering the Algiers FIR", "After entering the FIR", "Never"], 1, "15–30 min before entering the FIR; log off 5 min after leaving it."),
Q(3, "Final reserve fuel for the B737-800 under Algerian regulation:", ["30 minutes", "45 minutes", "60 minutes", "10 % of trip"], 0, "Jets: 30 min; propeller aircraft: 45 min."),
Q(3, "What is the contingency fuel?", ["3 % of trip", "5 % of trip fuel", "10 % of trip", "15 minutes"], 1, "5 % of the trip fuel."),
Q(4, "Basic maximum DTP for a two-pilot crew:", ["12 h", "13 h", "14 h", "11 h"], 1, "13 h per 24 h (12 h single pilot)."),
Q(4, "From which leg does the leg reduction start?", ["The 2nd", "The 3rd (included)", "The 4th", "The 5th"], 1, "From the third leg included: −30 min per leg."),
Q(4, "What is the maximum leg reduction?", ["1 h", "1 h 30", "2 h", "3 h"], 2, "A maximum of 2 h."),
Q(4, "Does positioning as a passenger count as a leg?", ["Yes", "No, but it counts in the DTP", "It does not count at all", "Only at night"], 1, "Positioning is part of the DTP but is not a leg."),
Q(4, "Maximum flight duty in 28 consecutive days:", ["100 h", "190 h", "60 h", "900 h"], 1, "190 h of FDP in 28 days (flight hours: 100 h)."),
Q(5, "The WOCL is:", ["00:00–04:00", "02:00–05:59 local", "22:00–06:00", "03:00–07:00 UTC"], 1, "02:00 to 05:59 local time."),
Q(5, "A DTP ends at 04:00 local. What WOCL reduction applies?", ["2 h", "1 h (50 % of 2 h)", "None", "30 min"], 1, "Ends in the WOCL: 50 % of the 2 h inside = 1 h."),
Q(5, "When is a 1 h extension NOT permitted?", ["With 4 legs by day", "With more than 6 legs", "With 2 legs", "After 10 h of rest"], 1, "Not with more than 6 legs, nor with more than 2 h in the WOCL and more than 4 legs."),
Q(5, "How many extensions are allowed per 7 consecutive days?", ["1", "2", "3", "Unlimited"], 1, "A maximum of two per seven consecutive days."),
Q(5, "Within how many days must the commander's report on a 1 h DTP change reach the Authority?", ["7", "14", "28", "90"], 2, "28 days."),
Q(6, "Minimum rest at home base:", ["10 h", "≥ DTP flown, never less than 12 h", "8 h", "36 h"], 1, "At least equal to the DTP flown and never less than 12 h."),
Q(6, "Minimum rest away from base before a new DTP:", ["≥ DTP flown, never less than 10 h", "12 h always", "8 h", "24 h"], 0, "At least equal to the DTP flown and never less than 10 h."),
Q(6, "The weekly rest requirement is:", ["24 h every 7 days", "36 consecutive hours including 2 nights every 7 days", "48 h every 14 days", "12 h every day"], 1, "36 consecutive hours including two consecutive nights every seven days."),
Q(6, "Take-off 06:30, check-in 05:30, 4 legs, two pilots. Maximum DTP?", ["12h00", "11h30", "11h00", "13h00"], 1, "12 h (4 legs) − 30 min (100 % of 30 min in the WOCL) = 11 h 30."),
Q(7, "Two pilots, 3 legs, duty from 16:30 ending 04:00. Maximum DTP?", ["12h30", "11h30", "11h00", "10h30"], 1, "12 h 30 − 1 h (50 % of 2 h in the WOCL) = 11 h 30."),
Q(7, "Two pilots, 2 legs, check-in 07:00, no WOCL. Latest check-out?", ["19:00", "20:00", "18:30", "21:00"], 1, "13 h DTP → 20:00."),
]

COURSE = dict(
    slug="algerian-regulations", title="Algerian Regulations and Duty Time", header_title="Algerian Regulations",
    tagline="Algerian aviation law and the ANAC, differences from ICAO, flight procedures and fuel, and the duty time rules — with an interactive duty time calculator and practice exercises.",
    purpose="Refresh flight crew knowledge of the Algerian regulation applicable to Domestic Airlines operations and train pilots to calculate duty time, WOCL reductions, extensions and rest.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Rank the Algerian legal texts and describe the role of the ANAC", "Apply the Algerian differences from ICAO", "Apply the flight procedures, night VFR and fuel rules",
                "Calculate the maximum duty time period with legs and WOCL", "Apply extensions, the commander's authority and waivers", "Calculate rest periods", "Use the duty time calculator"],
    icon="people", cert_prefix="ALREG", quiz_count=15, pass_mark=80, group="refresher", season="Winter", finale=None,
    modules=[dict(title="Algerian Regulation", summary="Legal framework, ANAC, differences from ICAO, procedures and fuel", icon="search", lessons=range(1, 4)),
             dict(title="Duty Time and Rest", summary="DTP, legs, WOCL, extensions, rest, examples and the interactive calculator", icon="people", lessons=range(4, 8))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner over the coast at dusk", "Algeria applies the ICAO standards, with published differences."),
            2: ("gen", "Flight deck view over the desert", "Know the differences: flight plans over desert and sea, 1,500 ft obstacle clearance."),
            3: ("gen", "Airliner in a holding pattern above clouds", "Holding speeds, airspace classes and fuel reserves."),
            4: ("gen", "Two pilots on the flight deck at dawn", "Duty time starts at check-in and ends at check-out."),
            5: ("gen", "Night flight deck with stars", "The window of circadian low: 02:00 to 05:59 local."),
            6: ("gen", "Airliner parked at night", "Rest is part of flight safety."),
            7: ("gen", "Flight deck at sunrise", "Calculate it — then check it.")},
)
