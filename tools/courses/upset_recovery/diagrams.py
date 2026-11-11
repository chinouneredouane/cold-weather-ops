"""Original SVG diagrams for the Upset Prevention and Recovery course (generated, no external images)."""
import math

INK, MUTED, LINE = "#24342b", "#5b6b62", "#dbe5df"
GREEN, GREEN_D, RED, AMBER, BLUE = "#1d7a3e", "#125a2b", "#c8102e", "#c76a00", "#1f5f99"
SKY, SKY_D, GROUND, GROUND_D = "#5aa6e0", "#2f7fc0", "#a0693a", "#7a4c26"
FONT = 'font-family="system-ui,Segoe UI,Arial,sans-serif"'


def fig(svg, caption, title, desc, vb, maxw=None):
    style = f' style="max-width:{maxw}px;margin:0 auto"' if maxw else ""
    return f"""
<figure class="diagram">
<svg viewBox="{vb}"{style} role="img" aria-label="{title}"><title>{title}</title><desc>{desc}</desc>
<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg>
<figcaption>{caption}</figcaption>
</figure>
"""


def arrow_defs(i):
    return (f'<defs><marker id="ar{i}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="context-stroke"/></marker></defs>')


# ------------------------------------------------------------------ attitude indicator
def adi(pitch, bank, cx=150, cy=150, r=120, uid="a", label=None):
    """Attitude indicator showing pitch (deg, + nose up) and bank (deg, + right wing down)."""
    ppd = 4.2  # pixels per degree of pitch
    parts = [f'<defs><clipPath id="clip{uid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath></defs>']
    g = [f'<g clip-path="url(#clip{uid})"><g transform="rotate({-bank} {cx} {cy}) translate(0 {pitch*ppd})">',
         f'<rect x="{cx-3*r}" y="{cy-3*r-200}" width="{6*r}" height="{3*r+200}" fill="{SKY}"/>',
         f'<rect x="{cx-3*r}" y="{cy}" width="{6*r}" height="{3*r+200}" fill="{GROUND}"/>',
         f'<line x1="{cx-3*r}" y1="{cy}" x2="{cx+3*r}" y2="{cy}" stroke="#fff" stroke-width="2.5"/>']
    for d in range(-90, 91, 5):
        if d == 0:
            continue
        y = cy - d * ppd
        w = 34 if d % 10 == 0 else 16
        g.append(f'<line x1="{cx-w}" y1="{y}" x2="{cx+w}" y2="{y}" stroke="#fff" stroke-width="2"/>')
        if d % 10 == 0:
            g.append(f'<text x="{cx+w+6}" y="{y+5}" fill="#fff" font-size="13" font-weight="700">{abs(d)}</text>'
                     f'<text x="{cx-w-6}" y="{y+5}" fill="#fff" font-size="13" font-weight="700" text-anchor="end">{abs(d)}</text>')
    g.append('</g></g>')
    parts += g
    # bank scale (fixed) and sky pointer (moves with bank)
    for a in (-60, -45, -30, -20, -10, 0, 10, 20, 30, 45, 60):
        ang = math.radians(a - 90)
        r1, r2 = r - 4, r - (18 if a in (0, 30, 60, -30, -60) else 11)
        parts.append(f'<line x1="{cx+r1*math.cos(ang):.1f}" y1="{cy+r1*math.sin(ang):.1f}" x2="{cx+r2*math.cos(ang):.1f}" '
                     f'y2="{cy+r2*math.sin(ang):.1f}" stroke="#fff" stroke-width="2.5"/>')
    parts.append(f'<g transform="rotate({-bank} {cx} {cy})"><path d="M{cx} {cy-r+20} l-9 15 h18 z" fill="#ffd24a" stroke="#333" stroke-width="1"/></g>')
    parts.append(f'<path d="M{cx} {cy-r+6} l-8 -12 h16 z" fill="#fff"/>')
    # fixed aircraft symbol
    parts.append(f'<g fill="#ffd24a" stroke="#222" stroke-width="1.2"><rect x="{cx-70}" y="{cy-4}" width="44" height="8" rx="2"/>'
                 f'<rect x="{cx+26}" y="{cy-4}" width="44" height="8" rx="2"/><rect x="{cx-5}" y="{cy-5}" width="10" height="10"/></g>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1e2a24" stroke-width="7"/>')
    if label:
        parts.append(f'<text x="{cx}" y="{cy+r+30}" text-anchor="middle" font-weight="700" font-size="15">{label}</text>')
    return "".join(parts)


def upset_envelope():
    svg = adi(0, 0, cx=170, cy=160, r=130, uid="env")
    ppd = 4.2
    svg += (f'<line x1="60" y1="{160-25*ppd}" x2="280" y2="{160-25*ppd}" stroke="{RED}" stroke-width="3" stroke-dasharray="7 5"/>'
            f'<line x1="60" y1="{160+10*ppd}" x2="280" y2="{160+10*ppd}" stroke="{RED}" stroke-width="3" stroke-dasharray="7 5"/>')
    for a in (-45, 45):
        ang = math.radians(a - 90)
        svg += (f'<line x1="170" y1="160" x2="{170+150*math.cos(ang):.1f}" y2="{160+150*math.sin(ang):.1f}" stroke="{RED}" stroke-width="3" stroke-dasharray="7 5"/>')
    svg += f"""
<g font-size="15">
<text x="330" y="60" font-weight="700" fill="{RED}">Pitch more than 25° nose-up</text>
<text x="330" y="110" font-weight="700" fill="{RED}">Bank more than 45°</text>
<text x="330" y="{160+10*ppd+5}" font-weight="700" fill="{RED}">Pitch more than 10° nose-down</text>
<text x="330" y="262" font-weight="700" fill="{INK}">…or airspeed inappropriate</text>
<text x="330" y="282" fill="{INK}">for the conditions, within these limits</text>
</g>"""
    return fig(svg, "The upset thresholds used in ICAO Doc 10011 and the industry training aid. They describe an upset — they are not targets or limits for normal flight.",
               "Upset thresholds on an attitude indicator", "Red lines at 25 degrees nose-up, 10 degrees nose-down and 45 degrees of bank.", "0 0 620 330")


def attitudes():
    svg = adi(35, 0, cx=150, cy=140, r=105, uid="nh", label="Nose-high, wings level")
    svg += adi(-20, 75, cx=450, cy=140, r=105, uid="nl", label="Nose-low, high bank")
    return fig(svg, "Recognise the upset from the attitude indicator first. Left: about 35° nose-up. Right: about 20° nose-down with about 75° of right bank — the sky pointer points to the sky, so roll towards it.",
               "Two attitude indicators: nose-high and nose-low high-bank", "Two example upsets as they appear on the attitude indicator.", "0 0 600 290")


# ------------------------------------------------------------------ aerodynamics
def angles():
    vx, vy = 250, 210
    def pt(deg, r):
        a = math.radians(deg)
        return vx + r * math.cos(a), vy - r * math.sin(a)
    def arc(d1, d2, r, col, w=2.5):
        x1, y1 = pt(d1, r); x2, y2 = pt(d2, r)
        return f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 0 {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="{w}"/>'
    th, ga = 15, 5
    cx1, cy1 = pt(th, 360); fx1, fy1 = pt(ga, 380)
    tx, ty = pt(th / 2 + 6, 175); gx, gy = pt(ga / 2, 140); ax, ay = pt((th + ga) / 2, 228)
    svg = f"""{arrow_defs(1)}
<line x1="30" y1="{vy}" x2="680" y2="{vy}" stroke="{MUTED}" stroke-dasharray="6 5"/><text x="680" y="{vy+20}" text-anchor="end" fill="{MUTED}">horizon</text>
<g transform="rotate({-th} {vx} {vy})">
  <path d="M{vx-120} {vy} Q{vx-100} {vy-14} {vx} {vy-12} L{vx+130} {vy-8} Q{vx+150} {vy-4} {vx+130} {vy+4} L{vx} {vy+12} Q{vx-100} {vy+14} {vx-120} {vy}z" fill="#e9eef1" stroke="{INK}" stroke-width="2"/>
  <path d="M{vx-100} {vy-4} L{vx-130} {vy-40} L{vx-112} {vy-40} L{vx-68} {vy-6}z" fill="#e9eef1" stroke="{INK}" stroke-width="2"/>
</g>
<line x1="{vx}" y1="{vy}" x2="{cx1:.1f}" y2="{cy1:.1f}" stroke="{BLUE}" stroke-width="2.5"/>
<line x1="{vx}" y1="{vy}" x2="{fx1:.1f}" y2="{fy1:.1f}" stroke="{GREEN}" stroke-width="3" marker-end="url(#ar1)"/>
{arc(0, th, 175, BLUE)}{arc(0, ga, 140, GREEN)}{arc(ga, th, 228, AMBER, 4)}
<text x="{cx1+8:.1f}" y="{cy1+4:.1f}" fill="{BLUE}" font-weight="700">wing chord / pitch attitude</text>
<text x="{fx1+8:.1f}" y="{fy1+5:.1f}" fill="{GREEN}" font-weight="700">flight path (relative airflow)</text>
<text x="{tx+6:.1f}" y="{ty:.1f}" fill="{BLUE}" font-weight="800" font-size="15">θ</text>
<text x="{gx+6:.1f}" y="{gy+2:.1f}" fill="{GREEN}" font-weight="800" font-size="15">γ</text>
<text x="{ax+8:.1f}" y="{ay+4:.1f}" fill="{AMBER}" font-weight="800" font-size="16">α</text>
<text x="30" y="34" font-size="15" font-weight="700">Pitch attitude = flight path angle + angle of attack (θ = γ + α)</text>
<text x="30" y="56" fill="{MUTED}">Angle of attack is measured between the wing chord and the relative airflow — not the horizon.</text>"""
    return fig(svg, "The attitude indicator shows pitch, not angle of attack. An aircraft can be nose-up and still descending at a very high angle of attack.",
               "Pitch attitude, flight path angle and angle of attack", "The aircraft pitch attitude equals flight path angle plus angle of attack.", "0 0 860 250")


def lift_curve():
    svg = f"""
<line x1="70" y1="280" x2="640" y2="280" stroke="{MUTED}" stroke-width="1.5"/><line x1="70" y1="280" x2="70" y2="30" stroke="{MUTED}" stroke-width="1.5"/>
<text x="355" y="315" text-anchor="middle">Angle of attack →</text><text x="28" y="155" text-anchor="middle" transform="rotate(-90 28 155)">Lift coefficient →</text>
<rect x="110" y="34" width="210" height="246" fill="{GREEN}" opacity=".08"/><text x="215" y="270" text-anchor="middle" fill="{GREEN_D}" font-weight="700">normal operating range</text>
<path d="M70 262 L420 70 Q470 40 500 52 Q540 70 600 160" fill="none" stroke="{GREEN}" stroke-width="4"/>
<line x1="492" y1="34" x2="492" y2="280" stroke="{RED}" stroke-width="2" stroke-dasharray="6 5"/>
<text x="500" y="232" fill="{RED}" font-weight="700">critical angle</text><text x="500" y="249" fill="{RED}">of attack: STALL</text>
<line x1="430" y1="34" x2="430" y2="280" stroke="{AMBER}" stroke-width="2" stroke-dasharray="4 4"/>
<text x="424" y="200" text-anchor="end" fill="{AMBER}" font-weight="700">stall warning</text><text x="424" y="216" text-anchor="end" fill="{AMBER}">(stick shaker)</text>
"""
    return fig(svg, "A wing stalls at its critical angle of attack — at any airspeed, attitude or power setting. Stall warning activates a few degrees earlier.",
               "Lift coefficient against angle of attack", "Lift rises with angle of attack up to the critical angle, then falls.", "0 0 680 330")


def load_factor():
    pts, pts2 = [], []
    for b in range(0, 76):
        n = 1 / math.cos(math.radians(b))
        x = 70 + b * 7
        pts.append(f"{x:.1f},{280 - (n - 1) * 70:.1f}")
        pts2.append(f"{x:.1f},{280 - (math.sqrt(n) - 1) * 70 * 2:.1f}")
    svg = f"""
<line x1="70" y1="280" x2="610" y2="280" stroke="{MUTED}" stroke-width="1.5"/><line x1="70" y1="280" x2="70" y2="20" stroke="{MUTED}" stroke-width="1.5"/>
{''.join(f'<line x1="{70+b*7}" y1="280" x2="{70+b*7}" y2="286" stroke="{MUTED}"/><text x="{70+b*7}" y="302" text-anchor="middle" font-size="12">{b}°</text>' for b in range(0, 76, 15))}
{''.join(f'<text x="60" y="{284-(n-1)*70}" text-anchor="end" font-size="12">{n:g} g</text><line x1="70" y1="{280-(n-1)*70}" x2="610" y2="{280-(n-1)*70}" stroke="{LINE}"/>' for n in (1, 2, 3, 4))}
<polyline points="{' '.join(pts)}" fill="none" stroke="{BLUE}" stroke-width="4"/>
<polyline points="{' '.join(pts2)}" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 5"/>
<circle cx="{70+60*7}" cy="{280-70}" r="6" fill="{BLUE}"/><text x="{70+60*7-10}" y="{280-70-12}" text-anchor="end" fill="{BLUE}" font-weight="700">60° bank = 2 g</text>
<circle cx="{70+60*7}" cy="{280-(math.sqrt(2)-1)*140:.1f}" r="6" fill="{RED}"/><text x="{70+60*7+12}" y="{280-(math.sqrt(2)-1)*140+18:.1f}" fill="{RED}" font-weight="700">stall speed +41 %</text>
<text x="340" y="325" text-anchor="middle">Bank angle in a level turn →</text>
<text x="90" y="40" fill="{BLUE}" font-weight="700">Load factor n = 1 / cos(bank)</text>
<text x="90" y="60" fill="{RED}" font-weight="700">Stall speed rises with √n</text>"""
    return fig(svg, "In a level turn, load factor rises steeply above 45° of bank, and the stall speed rises with it. Unloading (reducing g) lowers the stall speed again.",
               "Load factor and stall speed against bank angle", "Load factor equals one over the cosine of bank angle.", "0 0 640 340")


def coffin_corner():
    svg = f"""
<line x1="70" y1="290" x2="620" y2="290" stroke="{MUTED}" stroke-width="1.5"/><line x1="70" y1="290" x2="70" y2="20" stroke="{MUTED}" stroke-width="1.5"/>
<text x="345" y="325" text-anchor="middle">Speed (Mach) →</text><text x="28" y="160" text-anchor="middle" transform="rotate(-90 28 160)">Altitude →</text>
<path d="M120 290 Q200 160 330 62" fill="none" stroke="{RED}" stroke-width="4"/>
<path d="M560 290 Q500 160 360 62" fill="none" stroke="{AMBER}" stroke-width="4"/>
<path d="M120 290 Q200 160 330 62 L345 52 L360 62 Q500 160 560 290 z" fill="{GREEN}" opacity=".1"/>
<circle cx="345" cy="54" r="7" fill="{INK}"/><text x="360" y="40" font-weight="700">“coffin corner”</text>
<text x="80" y="110" fill="{RED}" font-weight="700">low-speed buffet / stall</text>
<text x="452" y="110" fill="{AMBER}" font-weight="700">high-speed (Mach) buffet</text>
<text x="350" y="240" text-anchor="middle" fill="{GREEN_D}" font-weight="700">usable speed range</text>
<line x1="232" y1="150" x2="470" y2="150" stroke="{INK}" stroke-width="2" marker-end="url(#ar2)" marker-start="url(#ar2)"/>{arrow_defs(2)}
<text x="350" y="174" text-anchor="middle" font-size="12">margin shrinks with altitude, weight and g</text>"""
    return fig(svg, "At high altitude the margin between low-speed buffet and Mach buffet becomes small. Higher weight, turbulence or bank (more g) reduce it further.",
               "Buffet boundaries and the coffin corner", "Low-speed and high-speed buffet boundaries converge at high altitude.", "0 0 640 340")


def stability():
    def bowl(x, kind):
        if kind == "stable":
            path = f"M{x-70} 70 Q{x} 190 {x+70} 70"
            ball = f'<circle cx="{x}" cy="117" r="13" fill="{GREEN}"/>'
        elif kind == "neutral":
            path = f"M{x-70} 130 L{x+70} 130"
            ball = f'<circle cx="{x}" cy="117" r="13" fill="{AMBER}"/>'
        else:
            path = f"M{x-70} 150 Q{x} 30 {x+70} 150"
            ball = f'<circle cx="{x}" cy="77" r="13" fill="{RED}"/>'
        return f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="4"/>{ball}'
    svg = (bowl(110, "stable") + bowl(320, "neutral") + bowl(530, "unstable") +
           f'<g text-anchor="middle" font-weight="700"><text x="110" y="200">Positive (stable)</text><text x="320" y="200">Neutral</text><text x="530" y="200">Negative (unstable)</text></g>'
           f'<g text-anchor="middle" fill="{MUTED}"><text x="110" y="220">returns after a disturbance</text><text x="320" y="220">stays where it is put</text><text x="530" y="220">moves further away</text></g>')
    return fig(svg, "Static stability describes the first tendency after a disturbance. Transport aeroplanes are certified with positive stability, but it reduces as the centre of gravity moves aft.",
               "Static stability: stable, neutral and unstable", "A ball in a bowl, on a flat surface and on a hill.", "0 0 640 240")


def pitch_power():
    svg = f"""{arrow_defs(3)}
<path d="M90 160 Q110 140 200 140 L520 146 Q560 150 520 166 L200 176 Q110 178 90 160z" fill="#e9eef1" stroke="{INK}" stroke-width="2"/>
<path d="M500 148 L560 90 L585 90 L560 150z" fill="#e9eef1" stroke="{INK}" stroke-width="2"/>
<rect x="250" y="186" width="90" height="30" rx="14" fill="#cfd8d3" stroke="{INK}" stroke-width="2"/>
<circle cx="320" cy="158" r="8" fill="{INK}"/><text x="332" y="130" font-weight="700">CG</text>
<line x1="250" y1="201" x2="110" y2="201" stroke="{AMBER}" stroke-width="5" marker-end="url(#ar3)"/>
<text x="100" y="232" fill="{AMBER}" font-weight="700">thrust line below the CG</text>
<path d="M235 100 A95 95 0 0 1 365 100" fill="none" stroke="{RED}" stroke-width="4" marker-end="url(#ar3)"/>
<text x="300" y="34" text-anchor="middle" fill="{RED}" font-weight="700">nose-up pitching moment when thrust increases</text>
<path d="M60 120 l-14 -26" stroke="{RED}" stroke-width="3" marker-end="url(#ar3)"/><text x="30" y="84" fill="{RED}" font-size="12">nose</text>"""
    return fig(svg, "With engines mounted below the wing, adding thrust pitches the nose up and reducing thrust pitches it down. At low speed, with little elevator authority, this coupling can be strong.",
               "Pitch-power coupling with underwing engines", "Thrust line below the centre of gravity gives a nose-up moment.", "0 0 640 250")


def energy():
    svg = f"""{arrow_defs(4)}
<rect x="60" y="60" width="170" height="90" rx="12" fill="{BLUE}" opacity=".15" stroke="{BLUE}" stroke-width="2"/>
<text x="145" y="98" text-anchor="middle" font-weight="800" fill="{BLUE}">Potential energy</text><text x="145" y="120" text-anchor="middle">altitude</text>
<rect x="410" y="60" width="170" height="90" rx="12" fill="{GREEN}" opacity=".15" stroke="{GREEN}" stroke-width="2"/>
<text x="495" y="98" text-anchor="middle" font-weight="800" fill="{GREEN_D}">Kinetic energy</text><text x="495" y="120" text-anchor="middle">airspeed</text>
<path d="M235 90 L405 90" stroke="{INK}" stroke-width="2.5" marker-end="url(#ar4)"/><path d="M405 125 L235 125" stroke="{INK}" stroke-width="2.5" marker-end="url(#ar4)"/>
<text x="320" y="80" text-anchor="middle" font-size="12">descend → gain speed</text><text x="320" y="145" text-anchor="middle" font-size="12">climb → lose speed</text>
<rect x="235" y="190" width="170" height="70" rx="12" fill="{AMBER}" opacity=".15" stroke="{AMBER}" stroke-width="2"/>
<text x="320" y="220" text-anchor="middle" font-weight="800" fill="{AMBER}">Thrust − drag</text><text x="320" y="242" text-anchor="middle">adds or removes total energy</text>
<path d="M290 190 L180 154" stroke="{AMBER}" stroke-width="2" marker-end="url(#ar4)"/><path d="M350 190 L460 154" stroke="{AMBER}" stroke-width="2" marker-end="url(#ar4)"/>"""
    return fig(svg, "Total energy is altitude plus speed. Pitch exchanges one for the other; only thrust and drag change the total. Know which state you are in before you act.",
               "Energy management: potential, kinetic, thrust and drag", "Altitude and airspeed can be exchanged; thrust minus drag changes total energy.", "0 0 640 280")


def cg_effects():
    svg = f"""
<path d="M60 130 Q80 110 170 110 L520 116 Q560 120 520 136 L170 146 Q80 148 60 130z" fill="#e9eef1" stroke="{INK}" stroke-width="2"/>
<rect x="230" y="160" width="200" height="12" fill="{LINE}"/><rect x="250" y="160" width="160" height="12" fill="{GREEN}" opacity=".5"/>
<line x1="250" y1="150" x2="250" y2="182" stroke="{BLUE}" stroke-width="3"/><line x1="410" y1="150" x2="410" y2="182" stroke="{RED}" stroke-width="3"/>
<text x="250" y="200" text-anchor="middle" fill="{BLUE}" font-weight="700">forward limit</text><text x="410" y="200" text-anchor="middle" fill="{RED}" font-weight="700">aft limit</text>
<g font-size="13"><text x="60" y="235" fill="{BLUE}" font-weight="700">Forward CG</text>
<text x="60" y="255">more stable, heavier pitch forces,</text><text x="60" y="273">higher stall speed, more elevator to rotate and flare</text>
<text x="400" y="235" fill="{RED}" font-weight="700">Aft CG</text>
<text x="400" y="255">less stable, lighter pitch forces,</text><text x="400" y="273">easy to over-control, less nose-down authority</text></g>"""
    return fig(svg, "The CG must stay within its certified limits. Loading errors outside the envelope can leave too little control authority to prevent or recover from an upset.",
               "Effects of centre of gravity position", "Forward and aft centre of gravity effects.", "0 0 700 290")


def windshear():
    svg = f"""{arrow_defs(5)}
<path d="M220 30 Q320 0 420 30 Q460 40 450 60 L190 60 Q180 40 220 30z" fill="#c9d3da"/>
{''.join(f'<path d="M{x} 70 L{x} 190" stroke="{BLUE}" stroke-width="3" marker-end="url(#ar5)"/>' for x in (270, 320, 370))}
<path d="M300 200 Q200 220 80 215" stroke="{BLUE}" stroke-width="3" fill="none" marker-end="url(#ar5)"/>
<path d="M340 200 Q440 220 560 215" stroke="{BLUE}" stroke-width="3" fill="none" marker-end="url(#ar5)"/>
<line x1="30" y1="240" x2="610" y2="240" stroke="{GROUND}" stroke-width="6"/>
<path d="M600 120 Q470 128 400 150 Q330 175 260 200 Q190 222 120 232" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6"/>
<g font-weight="700"><text x="630" y="105" text-anchor="end" fill="{GREEN_D}">1. headwind: speed and climb increase</text>
<text x="160" y="130" fill="{AMBER}">2. downdraft</text><text x="30" y="275" fill="{RED}">3. tailwind: speed and lift lost</text></g>"""
    return fig(svg, "A microburst first gives a performance-increasing headwind, then a downdraft and a performance-decreasing tailwind. Avoid it; if caught, apply the windshear escape manoeuvre.",
               "Microburst windshear on approach", "Headwind, downdraft and tailwind phases of a microburst.", "0 0 640 290")


def wake():
    svg = f"""
<path d="M40 120 Q60 106 140 106 L250 110 Q270 114 250 124 L140 132 Q60 134 40 120z" fill="#e9eef1" stroke="{INK}" stroke-width="2"/>
<path d="M150 112 L120 40 L140 40 L190 110z M150 128 L120 200 L140 200 L190 130z" fill="#e9eef1" stroke="{INK}" stroke-width="2"/>
{''.join(f'<ellipse cx="{x}" cy="{48+i*4}" rx="{14+i*3}" ry="{10+i*2}" fill="none" stroke="{BLUE}" stroke-width="2.5" opacity="{1-i*0.13}"/><ellipse cx="{x}" cy="{192+i*4}" rx="{14+i*3}" ry="{10+i*2}" fill="none" stroke="{BLUE}" stroke-width="2.5" opacity="{1-i*0.13}"/>' for i, x in enumerate(range(260, 620, 60)))}
<text x="330" y="125" font-weight="700" fill="{BLUE}">counter-rotating vortices from each wing tip —</text>
<text x="330" y="145" fill="{BLUE}">they sink and drift with the wind</text>"""
    return fig(svg, "Wake vortices can roll a following aircraft faster than its ailerons can counter. Respect wake separation, and stay at or above the preceding aircraft's flight path.",
               "Wake vortices behind an aircraft", "Two vortices trail from the wing tips.", "0 0 640 240")


def somatogravic():
    svg = f"""{arrow_defs(6)}
<circle cx="200" cy="80" r="26" fill="#f1d7bd" stroke="{INK}" stroke-width="2"/><rect x="180" y="106" width="40" height="70" rx="12" fill="#cfd8d3" stroke="{INK}" stroke-width="2"/>
<line x1="200" y1="160" x2="200" y2="260" stroke="{INK}" stroke-width="3" marker-end="url(#ar6)"/><text x="210" y="250">gravity</text>
<line x1="200" y1="160" x2="80" y2="160" stroke="{AMBER}" stroke-width="3" marker-end="url(#ar6)"/><text x="40" y="128" fill="{AMBER}">inertia from</text><text x="40" y="146" fill="{AMBER}">acceleration</text>
<line x1="200" y1="160" x2="95" y2="262" stroke="{RED}" stroke-width="4" marker-end="url(#ar6)"/>
<text x="20" y="290" fill="{RED}" font-weight="700">resultant feels like “down” → false sensation of nose-up</text>
<text x="360" y="90" font-weight="700" font-size="15">Somatogravic illusion</text>
<text x="360" y="115">Strong forward acceleration — a go-around,</text><text x="360" y="134">a take-off in darkness — feels like pitching up.</text>
<text x="360" y="162">The natural reaction is to push the nose down,</text><text x="360" y="181">towards the ground.</text>
<text x="360" y="215" fill="{GREEN_D}" font-weight="700">Countermeasure: believe the attitude indicator.</text>"""
    return fig(svg, "Vestibular illusions are strongest without visual references. Several go-around accidents at night followed exactly this pattern.",
               "Somatogravic illusion", "Acceleration combined with gravity feels like a nose-up attitude.", "0 0 680 300")


def recovery_priority():
    svg = f"""{arrow_defs(7)}
<g font-weight="700" text-anchor="middle">
<rect x="20" y="40" width="140" height="70" rx="12" fill="{BLUE}"/><text x="90" y="72" fill="#fff">Recognise</text><text x="90" y="92" fill="#fff" font-weight="400">and confirm</text>
<rect x="180" y="40" width="140" height="70" rx="12" fill="{AMBER}"/><text x="250" y="72" fill="#fff">Stalled?</text><text x="250" y="92" fill="#fff" font-weight="400">reduce AoA first</text>
<rect x="340" y="40" width="140" height="70" rx="12" fill="{GREEN}"/><text x="410" y="72" fill="#fff">Recover</text><text x="410" y="92" fill="#fff" font-weight="400">nose-high / nose-low</text>
<rect x="500" y="40" width="120" height="70" rx="12" fill="{GREEN_D}"/><text x="560" y="72" fill="#fff">Stabilise</text><text x="560" y="92" fill="#fff" font-weight="400">safe flight path</text>
</g>
<path d="M160 75 L178 75" stroke="{INK}" stroke-width="3" marker-end="url(#ar7)"/><path d="M320 75 L338 75" stroke="{INK}" stroke-width="3" marker-end="url(#ar7)"/><path d="M480 75 L498 75" stroke="{INK}" stroke-width="3" marker-end="url(#ar7)"/>
<text x="20" y="145" fill="{MUTED}">Throughout: communicate (PF/PM callouts), avoid excessive g,</text><text x="20" y="163" fill="{MUTED}">and follow the manufacturer's procedures.</text>"""
    return fig(svg, "Stall recovery always takes priority: you cannot recover attitude while the wing is stalled.",
               "Upset recovery sequence", "Recognise, deal with any stall, recover, stabilise.", "0 0 640 170")
