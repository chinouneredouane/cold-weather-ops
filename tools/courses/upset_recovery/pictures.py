"""Original lesson illustrations, drawn as SVG scenes and rendered to JPG by tools/make_pictures.py."""
import math
import random

W, H = 1600, 800


def sky(style):
    stops = {
        "day": ("#2f7fc0", "#8cc4ef", "#d9eefb"),
        "dusk": ("#2b2d5c", "#c0587a", "#f4b26b"),
        "night": ("#050b1a", "#0e1d3a", "#1f3557"),
        "storm": ("#2a3442", "#4c5a6b", "#7d8b99"),
        "high": ("#071d4a", "#1f57a8", "#7fb6ea"),
        "cloud": ("#8c9aa6", "#b7c2cb", "#dfe5ea"),
    }[style]
    return (f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{stops[0]}"/>'
            f'<stop offset=".6" stop-color="{stops[1]}"/><stop offset="1" stop-color="{stops[2]}"/></linearGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')


def stars(n=120, seed=3):
    r = random.Random(seed)
    return "".join(f'<circle cx="{r.uniform(0, W):.0f}" cy="{r.uniform(0, H*0.6):.0f}" r="{r.uniform(.8, 2.2):.1f}" fill="#fff" opacity="{r.uniform(.4, 1):.2f}"/>' for _ in range(n))


def cloud(x, y, s=1.0, col="#ffffff", op=0.95):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="{col}" opacity="{op}">'
            '<ellipse cx="0" cy="0" rx="120" ry="42"/><ellipse cx="-70" cy="8" rx="80" ry="34"/><ellipse cx="80" cy="10" rx="90" ry="32"/>'
            '<ellipse cx="-10" cy="-30" rx="70" ry="45"/><ellipse cx="50" cy="-22" rx="55" ry="36"/></g>')


def cumulonimbus(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M-260 260 Q-250 120 -150 90 Q-160 -20 -60 -40 Q-40 -150 60 -130 Q150 -170 190 -80 Q300 -60 280 60 Q330 120 300 260z" fill="#5b6876"/>'
            '<path d="M-330 -150 Q0 -220 360 -150 Q200 -120 0 -125 Q-200 -120 -330 -150z" fill="#6f7c8a"/>'
            '<path d="M-40 120 l-30 70 l26 -6 l-36 80 l70 -96 l-28 6 l30 -54z" fill="#ffe680"/></g>')


def mountains(y, col="#3e5a4a", col2="#5d7b67", seed=1):
    r = random.Random(seed)
    pts, x = [f"0,{H}"], 0
    while x < W + 200:
        pts.append(f"{x},{y - r.uniform(60, 220):.0f}")
        x += r.uniform(140, 260)
        pts.append(f"{x},{y - r.uniform(0, 40):.0f}")
        x += r.uniform(80, 140)
    pts.append(f"{W},{H}")
    back = " ".join(f"{p.split(',')[0]},{float(p.split(',')[1]) + 40:.0f}" for p in pts)
    return f'<polygon points="{back}" fill="{col2}" opacity=".7" transform="translate(-90 -60)"/><polygon points="{" ".join(pts)}" fill="{col}"/>'


def ground(horizon_y, tilt=0, style="land"):
    fill = {"land": "#6b8f5a", "sea": "#1c4f7a", "night": "#0a1426", "desert": "#c79a5b", "snow": "#e8eef3"}[style]
    return (f'<g transform="rotate({tilt} {W/2} {horizon_y})"><rect x="-{W}" y="{horizon_y}" width="{3*W}" height="{2*H}" fill="{fill}"/>'
            f'<rect x="-{W}" y="{horizon_y}" width="{3*W}" height="6" fill="#fff" opacity=".25"/></g>')


def aircraft(x, y, s=1.0, pitch=0, col="#f4f6f8", accent="#1d7a3e", flip=False):
    """Side view of a generic twin-engine airliner, nose to the right; pitch + = nose up."""
    sx = -s if flip else s
    return (f'<g transform="translate({x} {y}) rotate({-pitch if not flip else pitch}) scale({sx} {s})">'
            '<path d="M-300 -10 Q-310 -22 -280 -26 L190 -26 Q260 -26 300 -4 Q310 4 296 10 Q250 26 190 26 L-250 22 Q-300 18 -300 -10z" fill="' + col + '" stroke="#334" stroke-width="3"/>'
            '<path d="M-230 -24 L-300 -140 L-262 -140 L-170 -24z" fill="' + col + '" stroke="#334" stroke-width="3"/>'
            '<path d="M-260 0 L-330 -12 L-320 4 L-250 12z" fill="' + col + '" stroke="#334" stroke-width="3"/>'
            '<path d="M-20 10 L-130 70 L-95 72 L70 14z" fill="#d9dee3" stroke="#334" stroke-width="3"/>'
            '<rect x="-40" y="30" width="90" height="34" rx="16" fill="#c7ced4" stroke="#334" stroke-width="3"/>'
            f'<path d="M-280 -6 L240 -6" stroke="{accent}" stroke-width="7"/>'
            '<path d="M250 -18 L282 -10 L274 -4 L246 -8z" fill="#1d2a33"/>'
            + "".join(f'<circle cx="{wx}" cy="-14" r="5" fill="#1d2a33"/>' for wx in range(-200, 200, 34)) + '</g>')


def airflow(x0, y0, length=900, n=6, gap=34, separate_at=None):
    out = []
    for i in range(n):
        y = y0 + i * gap
        if separate_at and i < 3:
            # relative airflow comes from the nose (right); it separates over the wing and becomes turbulent behind it
            sx = x0 + separate_at
            out.append(f'<path d="M{x0+length} {y} L{sx} {y}" stroke="#fff" stroke-width="3" opacity=".75" fill="none"/>')
            for k in range(3):
                cx, cy = sx - 60 - k * 90, y - 20 + k * 6
                out.append(f'<path d="M{cx-30} {cy} q15 -28 32 -6 q14 18 -8 26 q-18 4 -18 -12" stroke="#fff" stroke-width="3" fill="none" opacity=".7"/>')
        else:
            out.append(f'<path d="M{x0} {y} C{x0+length*0.4} {y-14} {x0+length*0.6} {y+14} {x0+length} {y}" stroke="#fff" stroke-width="3" opacity=".6" fill="none"/>')
    return "".join(out)


def adi_inset(pitch, bank, x=1330, y=560, r=170, uid="i"):
    ppd = 5.5
    parts = [f'<defs><clipPath id="c{uid}"><circle cx="{x}" cy="{y}" r="{r}"/></clipPath></defs>',
             f'<circle cx="{x}" cy="{y}" r="{r+16}" fill="#1b232a" stroke="#000" stroke-width="4"/>',
             f'<g clip-path="url(#c{uid})"><g transform="rotate({-bank} {x} {y}) translate(0 {pitch*ppd})">',
             f'<rect x="{x-4*r}" y="{y-4*r-300}" width="{8*r}" height="{4*r+300}" fill="#3a8fd6"/>',
             f'<rect x="{x-4*r}" y="{y}" width="{8*r}" height="{4*r+300}" fill="#9a6435"/>',
             f'<line x1="{x-4*r}" y1="{y}" x2="{x+4*r}" y2="{y}" stroke="#fff" stroke-width="4"/>']
    for d in range(-80, 81, 10):
        if d:
            parts.append(f'<line x1="{x-44}" y1="{y-d*ppd}" x2="{x+44}" y2="{y-d*ppd}" stroke="#fff" stroke-width="3"/>')
            parts.append(f'<line x1="{x-22}" y1="{y-(d-5)*ppd}" x2="{x+22}" y2="{y-(d-5)*ppd}" stroke="#fff" stroke-width="2"/>')
    parts.append('</g></g>')
    parts.append(f'<g transform="rotate({-bank} {x} {y})"><path d="M{x} {y-r+24} l-13 22 h26 z" fill="#ffd24a"/></g>')
    parts.append(f'<g fill="#ffd24a" stroke="#111" stroke-width="2"><rect x="{x-100}" y="{y-6}" width="62" height="12" rx="3"/>'
                 f'<rect x="{x+38}" y="{y-6}" width="62" height="12" rx="3"/><rect x="{x-7}" y="{y-7}" width="14" height="14"/></g>')
    return "".join(parts)


def cockpit(horizon_y=420, bank=0, outside="day", ground_style="land", extra=""):
    """View through a windshield: tilted horizon outside, glare shield and window frames."""
    inner = sky(outside) + (stars() if outside == "night" else "") + extra + ground(horizon_y, bank, ground_style)
    frame = ('<path d="M0 0 H1600 V800 H0z M120 90 L760 60 L760 520 L60 560z M840 60 L1480 90 L1540 560 L840 520z" fill="#1a2026" fill-rule="evenodd"/>'
             '<path d="M0 560 Q800 470 1600 560 L1600 800 L0 800z" fill="#262e35"/>'
             '<rect x="300" y="610" width="300" height="170" rx="10" fill="#0d1114" stroke="#3a444c" stroke-width="4"/>'
             '<rect x="1000" y="610" width="300" height="170" rx="10" fill="#0d1114" stroke="#3a444c" stroke-width="4"/>')
    return inner + frame


def pilots():
    def pilot(x):
        return (f'<g transform="translate({x} 520)"><ellipse cx="0" cy="0" rx="70" ry="80" fill="#2b2f36"/>'
                f'<path d="M-150 280 Q-140 110 0 90 Q140 110 150 280z" fill="#e8ecef"/>'
                f'<path d="M-40 100 L0 240 L40 100z" fill="#1d2a33"/><path d="M-120 140 L-60 120 L-70 160z M120 140 L60 120 L70 160z" fill="#c9a227"/>'
                f'<path d="M-72 -20 Q0 -110 72 -20" fill="none" stroke="#111" stroke-width="12"/><rect x="-86" y="-28" width="22" height="40" rx="8" fill="#111"/></g>')
    return pilot(470) + pilot(1130)


def card(svg):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{svg}</svg>'


def scene(n):
    if n == 1:
        s = sky("day") + cloud(300, 220, 1.4) + cloud(1250, 160, 1.1) + ground(650, 0, "land") + aircraft(820, 420, 1.35, 8)
    elif n == 2:
        s = cockpit(380, -50, "day", extra=cloud(400, 250, 1.0) + cloud(1200, 300, 0.8)) + adi_inset(-8, 50)
    elif n == 3:
        s = sky("storm") + cumulonimbus(1050, 380, 1.3) + ground(700, 0, "sea") + aircraft(470, 380, 1.0, 4) + cloud(250, 600, 1.2, "#8c98a4", .8)
    elif n == 4:
        s = sky("day") + airflow(80, 300, 1450, 7, 40) + aircraft(820, 420, 1.3, 6) + ground(720, 0, "land")
    elif n == 5:
        s = sky("day") + cloud(260, 640, 1.3) + aircraft(760, 430, 1.25, 18) + airflow(80, 250, 1400, 6, 42, separate_at=650)
    elif n == 6:
        s = cockpit(400, 60, "day", extra=cloud(300, 300, .9) + cloud(1300, 260, 1.1)) + adi_inset(2, 60)
    elif n == 7:
        s = (sky("high") + '<path d="M-200 820 Q800 520 1800 820z" fill="#dff1ff" opacity=".9"/>' + cloud(400, 700, 1.5) + cloud(1200, 720, 1.4)
             + '<path d="M0 330 L560 360" stroke="#fff" stroke-width="10" opacity=".6"/>' + aircraft(860, 360, 1.15, 2))
    elif n == 8:
        s = (sky("day") + ground(620, 0, "sea") + '<path d="M60 360 Q300 240 540 360 T1020 360 T1500 360" stroke="#fff" stroke-width="6" stroke-dasharray="20 14" fill="none"/>'
             + aircraft(1150, 330, 0.9, -6))
    elif n == 9:
        s = (sky("dusk") + cloud(300, 620, 1.6, "#f1c1a6", .9) + cloud(1300, 640, 1.4, "#f1c1a6", .9)
             + '<path d="M240 560 Q400 160 800 140 Q1200 160 1360 560" stroke="#fff" stroke-width="6" stroke-dasharray="16 12" fill="none" opacity=".8"/>'
             + aircraft(800, 380, 1.1, 0))
    elif n == 10:
        s = (sky("day") + mountains(740, seed=4) + '<path d="M80 200 Q600 230 900 420 T1520 600" stroke="#fff" stroke-width="7" stroke-dasharray="22 14" fill="none"/>'
             + aircraft(820, 380, 1.0, -10))
    elif n == 11:
        s = (sky("day") + ground(640, 0, "land") + '<rect x="0" y="640" width="1600" height="160" fill="#5d6770"/>'
             + aircraft(800, 520, 1.25, 0) + '<path d="M680 640 L800 600 L920 640z" fill="#c76a00"/><rect x="420" y="604" width="760" height="14" rx="6" fill="#c76a00" transform="rotate(-3 800 610)"/>')
    elif n == 12:
        s = (sky("day") + '<g fill="#fff" opacity=".95"><ellipse cx="420" cy="230" rx="260" ry="34"/><ellipse cx="420" cy="205" rx="180" ry="22"/>'
             '<ellipse cx="1180" cy="180" rx="240" ry="30"/><ellipse cx="1180" cy="158" rx="160" ry="18"/></g>'
             + mountains(760, "#4b5d6b", "#6c7f8c", seed=7) + '<path d="M0 420 Q200 330 400 420 T800 420 T1200 420 T1600 420" stroke="#ffffff" stroke-width="4" fill="none" opacity=".6"/>'
             + aircraft(860, 360, 0.9, 3))
    elif n == 13:
        s = cockpit(430, -8, "day", extra=cloud(500, 320, 1.1)) + (
            '<g font-family="Arial" font-weight="700" font-size="34"><text x="330" y="660" fill="#38d36b">SPEED</text><text x="460" y="660" fill="#38d36b">ALT</text>'
            '<text x="1030" y="660" fill="#f4c542">A/P OFF</text><text x="1030" y="720" fill="#ff5050">CAUTION</text></g>')
    elif n == 14:
        s = cockpit(520, -12, "night", ground_style="night") + adi_inset(-12, 25)
    elif n == 15:
        s = cockpit(440, 0, "dusk", extra=cloud(500, 380, 1.2, "#f1c1a6") + cloud(1200, 360, 1.0, "#f1c1a6")) + pilots()
    elif n == 16:
        s = (sky("day") + ground(560, 0, "land") + '<path d="M760 800 L840 800 L820 560 L780 560z" fill="#3b4540"/>'
             '<path d="M800 790 L800 570" stroke="#fff" stroke-width="5" stroke-dasharray="26 22"/>'
             '<path d="M1500 140 L840 548" stroke="#ffd24a" stroke-width="5" stroke-dasharray="18 12"/>' + aircraft(1220, 300, 0.7, -3, flip=True))
    elif n == 17:
        s = cockpit(300, 35, "cloud") + adi_inset(-15, 35)
    elif n == 18:
        s = (sky("cloud") + cloud(300, 300, 1.8, "#e8edf1") + cloud(1250, 520, 2.0, "#e8edf1")
             + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#fff"/>' for x, y in ((200, 120), (520, 600), (900, 160), (1400, 240), (1100, 700), (700, 420)))
             + aircraft(800, 420, 1.2, 2)
             + '<g transform="translate(1180 300)"><circle r="120" fill="#fff" stroke="#1d7a3e" stroke-width="8"/>'
               '<rect x="-80" y="-14" width="120" height="28" rx="10" fill="#9aa4ab"/><path d="M40 -14 L90 -6 L90 6 L40 14z" fill="#9aa4ab"/>'
               '<path d="M-90 -40 l20 10 M-60 -60 l10 20 M-20 -70 l0 22" stroke="#7fc6ff" stroke-width="8" stroke-linecap="round"/>'
               '<path d="M70 -12 q14 12 0 24" stroke="#7fc6ff" stroke-width="10" fill="none"/></g>')
    elif n == 19:
        s = cockpit(260, -70, "day", extra=cloud(800, 300, 1.4)) + adi_inset(-5, 70)
    elif n == 20:
        s = (sky("day") + cloud(1200, 650, 1.5) + aircraft(720, 420, 1.2, 22) + airflow(100, 250, 1300, 5, 44, separate_at=600)
             + '<path d="M1300 160 Q1420 260 1360 380" stroke="#ffd24a" stroke-width="16" fill="none"/><path d="M1330 370 L1360 410 L1390 362z" fill="#ffd24a"/>')
    elif n == 21:
        s = sky("high") + cloud(300, 680, 1.4) + cloud(1300, 700, 1.3) + aircraft(800, 430, 1.15, 40)
    elif n == 22:
        s = (sky("day") + '<g transform="rotate(-25 800 420)">' + ground(360, 0, "land") + mountains(560, seed=9) + '</g>'
             + aircraft(820, 380, 1.1, -30))
    elif n == 23:
        s = sky("night") + stars(80, 9) + cumulonimbus(1150, 420, 1.2) + ground(660, 0, "night") + aircraft(520, 400, 0.85, 2)
    elif n == 24:
        s = sky("dusk") + cloud(250, 640, 1.5, "#f1c1a6", .9) + cloud(1350, 660, 1.3, "#f1c1a6", .9) + aircraft(800, 380, 1.15, 3)
    else:
        raise ValueError(n)
    return card(s)
