"""Original lesson illustrations for the ground refresher courses (SVG scenes, rendered to JPG by tools/make_pictures.py)."""
from courses.upset_recovery.pictures import (W, H, sky, stars, cloud, cumulonimbus, mountains, ground, aircraft,
                                             cockpit, adi_inset, pilots, card)


def sun(x=1300, y=170, r=90):
    return (f'<circle cx="{x}" cy="{y}" r="{r*2.2}" fill="#fff3c4" opacity=".35"/><circle cx="{x}" cy="{y}" r="{r*1.5}" fill="#ffe08a" opacity=".5"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffd24a"/>')


def desert(y=620):
    return (f'<rect x="0" y="{y}" width="{W}" height="{H-y}" fill="#d9a85f"/>'
            f'<path d="M0 {y+40} Q300 {y-30} 640 {y+30} T1280 {y+20} T1700 {y}" fill="#c99448"/>'
            f'<path d="M0 {y+110} Q400 {y+50} 820 {y+110} T1700 {y+90} V800 H0z" fill="#b98340"/>')


def haze(y=600):
    return "".join(f'<path d="M0 {y-k*14} Q200 {y-k*14-10} 400 {y-k*14} T800 {y-k*14} T1200 {y-k*14} T1600 {y-k*14}" stroke="#fff" stroke-width="3" fill="none" opacity="{.25-k*.05:.2f}"/>' for k in range(4))


def dust_wall(x=900):
    return (f'<path d="M{x} 800 Q{x-60} 420 {x+120} 300 Q{x+300} 200 1700 260 V800z" fill="#b4793f" opacity=".85"/>'
            f'<path d="M{x+80} 800 Q{x+40} 500 {x+200} 380 Q{x+380} 300 1700 330 V800z" fill="#9c6533" opacity=".8"/>')


def runway(x=760, y=620, w=80):
    return (f'<path d="M{x} 800 L{x+w} 800 L{x+w/2+12} {y} L{x+w/2-12} {y}z" fill="#3b4540"/>'
            f'<path d="M{x+w/2} 790 L{x+w/2} {y+10}" stroke="#fff" stroke-width="4" stroke-dasharray="22 18"/>')


def levels():
    return "".join(f'<line x1="0" y1="{y}" x2="1600" y2="{y}" stroke="#fff" stroke-width="2" stroke-dasharray="14 12" opacity=".55"/>'
                   f'<text x="30" y="{y-10}" font-family="Arial" font-size="30" font-weight="700" fill="#fff" opacity=".85">FL{fl}</text>'
                   for y, fl in ((230, 360), (420, 350), (610, 340)))


def datalink(x1, y1, x2, y2):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#ffd24a" stroke-width="6" stroke-dasharray="18 14"/>'
            f'<g transform="translate({x2} {y2})"><rect x="-30" y="0" width="60" height="140" fill="#4b5d6b"/><rect x="-55" y="-40" width="110" height="50" rx="8" fill="#cfd8dc"/>'
            f'<rect x="-45" y="-30" width="90" height="25" fill="#1f5f99"/></g>')


def cdu():
    keys = "".join(f'<rect x="{x}" y="{y}" width="58" height="34" rx="6" fill="#30383f"/>' for y in (520, 566, 612, 658) for x in (500, 572, 644, 716, 788, 860, 932, 1004, 1076))
    return ('<rect x="440" y="120" width="720" height="640" rx="26" fill="#20262b" stroke="#0d1114" stroke-width="8"/>'
            '<rect x="500" y="160" width="600" height="330" rx="8" fill="#05090c"/>'
            '<g font-family="Courier New, monospace" font-weight="700" font-size="30">'
            '<text x="640" y="205" fill="#fff">ATC UPLINK</text>'
            '<text x="520" y="260" fill="#38d36b">CLIMB TO FL360</text>'
            '<text x="520" y="310" fill="#9fd8ff">REPORT LEVEL FL360</text>'
            '<text x="520" y="460" fill="#fff">&lt;REJECT</text><text x="880" y="460" fill="#fff">ACCEPT&gt;</text></g>' + keys)


def scene(slug, n):
    s = None
    if slug == "rvsm-refresher":
        s = {
            1: lambda: sky("high") + levels() + cloud(300, 720, 1.4) + cloud(1300, 740, 1.3) + aircraft(1000, 420, 0.75, 0) + aircraft(560, 230, 0.75, 0, flip=True),
            2: lambda: cockpit(470, 0, "dusk", extra=sun(1200, 470, 60) + cloud(500, 380, 1.0, "#f1c1a6")),
            3: lambda: sky("high") + levels() + cloud(800, 740, 1.6) + aircraft(800, 420, 1.0, 0),
            4: lambda: (sky("high") + '<g fill="#fff" opacity=".95"><ellipse cx="420" cy="260" rx="260" ry="30"/><ellipse cx="1220" cy="220" rx="240" ry="28"/></g>'
                        + mountains(800, "#4b5d6b", "#6c7f8c", seed=5) + aircraft(820, 420, 0.85, 0)),
            5: lambda: sky("high") + levels() + aircraft(1050, 420, 0.75, 0) + aircraft(500, 600, 0.75, 6) + cloud(300, 760, 1.2),
            6: lambda: cockpit(440, 0, "dusk", extra=cloud(500, 380, 1.2, "#f1c1a6") + cloud(1200, 360, 1.0, "#f1c1a6")) + pilots(),
        }
    elif slug == "cfit-egpws-refresher":
        s = {
            1: lambda: sky("cloud") + mountains(700, "#3e5a4a", "#5d7b67", seed=3) + cloud(500, 300, 2.0, "#e5eaee", .9) + aircraft(1050, 420, 0.7, -4, flip=True),
            2: lambda: cockpit(520, 0, "day", extra=mountains(600, "#3e5a4a", "#5d7b67", seed=8)) + adi_inset(-3, 0),
            3: lambda: cockpit(440, 0, "dusk", extra=mountains(560, "#5b4a5e", "#7a6a80", seed=2)) + pilots(),
            4: lambda: (sky("day") + ground(560, 0, "land") + runway() + mountains(620, "#3e5a4a", "#5d7b67", seed=11)
                        + '<path d="M1500 150 L800 600" stroke="#ffd24a" stroke-width="6" stroke-dasharray="18 12"/>' + aircraft(1200, 340, 0.6, -3, flip=True)),
            5: lambda: cockpit(560, 0, "night", extra=mountains(600, "#0d1a2b", "#15263c", seed=6), ground_style="night") + adi_inset(-4, 0),
            6: lambda: sky("day") + mountains(780, "#3e5a4a", "#5d7b67", seed=12) + aircraft(800, 420, 1.0, 22),
            7: lambda: sky("dusk") + mountains(760, "#4a3b4e", "#6d5b70", seed=4) + aircraft(820, 360, 0.95, 12),
        }
    elif slug == "hot-weather-operations":
        s = {
            1: lambda: sky("day") + sun() + desert(600) + haze(600) + runway(700, 600, 120) + aircraft(760, 420, 0.95, 10),
            2: lambda: sky("day") + sun(250, 160, 80) + desert(640) + haze(640) + '<rect x="0" y="600" width="1600" height="80" fill="#8a8f93"/>' + aircraft(820, 540, 1.1, 0),
            3: lambda: sky("high") + sun(1350, 150, 70) + desert(700) + aircraft(800, 380, 1.0, 0),
            4: lambda: sky("storm") + desert(640) + dust_wall(700) + cumulonimbus(1250, 300, 0.8) + aircraft(420, 360, 0.7, 2),
            5: lambda: sky("day") + sun(1300, 140, 70) + desert(560) + runway(720, 560, 160) + aircraft(800, 470, 0.8, 4, flip=True),
            6: lambda: cockpit(440, 0, "dusk", extra=sun(1100, 450, 50) + desert(500)) + pilots(),
        }
    elif slug == "cpdlc":
        s = {
            1: lambda: sky("high") + cloud(400, 700, 1.5) + cloud(1200, 720, 1.3) + aircraft(560, 300, 0.8, 0) + datalink(760, 320, 1300, 560),
            2: lambda: cockpit(440, 0, "high", extra=cloud(500, 400, 1.2)),
            3: lambda: sky("high") + cloud(800, 720, 1.8) + aircraft(800, 380, 1.0, 0),
            4: lambda: cockpit(440, 0, "dusk", extra=cloud(500, 380, 1.2, "#f1c1a6")) + pilots(),
            5: lambda: '<rect width="1600" height="800" fill="#2a3139"/>' + cdu(),
            6: lambda: sky("dusk") + cloud(300, 650, 1.4, "#f1c1a6", .9) + aircraft(800, 380, 1.0, 0),
        }
    if not s or n not in s:
        raise KeyError((slug, n))
    return card(s[n]())
