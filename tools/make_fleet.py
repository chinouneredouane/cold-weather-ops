#!/usr/bin/env python3
"""Generate the fleet illustrations used as the rotating background of the academy home page.

Usage: python3 tools/make_fleet.py      (needs Node.js with Playwright)
Writes assets/img/fleet/fleet-1.jpg … To use real photos instead, replace those files (1600 × 700 px, JPG)
— or list your own files in FLEET in tools/build.py.
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from courses.upset_recovery.pictures import sky, cloud, mountains, card  # noqa: E402
from courses.refresher_pictures import desert, sun  # noqa: E402

GREEN, RED, DARK = "#1d7a3e", "#c8102e", "#2b3a44"


def jet(x, y, s=1.0, pitch=0):
    """Boeing 737-800 side view: low wing, underwing engine, winglet, conventional tail."""
    return (f'<g transform="translate({x} {y}) rotate({-pitch}) scale({s})">'
            '<path d="M-330 -12 Q-338 -26 -306 -28 L200 -28 Q270 -28 318 -6 Q330 4 314 12 Q262 28 200 28 L-280 24 Q-330 20 -330 -12z" fill="#f6f8f9" stroke="#2b3a44" stroke-width="3"/>'
            '<path d="M-250 -26 L-322 -160 L-282 -160 L-186 -26z" fill="#f6f8f9" stroke="#2b3a44" stroke-width="3"/>'
            '<path d="M-318 -150 L-282 -160 L-262 -120 L-300 -112z" fill="' + GREEN + '"/>'
            '<path d="M-288 0 L-366 -12 L-356 6 L-276 14z" fill="#f6f8f9" stroke="#2b3a44" stroke-width="3"/>'
            '<path d="M-30 12 L-150 74 L-112 76 L64 16z" fill="#dfe4e8" stroke="#2b3a44" stroke-width="3"/>'
            '<path d="M-150 74 L-162 46 L-146 46 L-136 72z" fill="' + GREEN + '"/>'
            '<path d="M-58 32 Q-60 64 -10 66 L52 66 Q70 64 70 49 Q70 34 52 32z" fill="#cfd6db" stroke="#2b3a44" stroke-width="3"/>'
            f'<path d="M-306 -4 L250 -4" stroke="{GREEN}" stroke-width="8"/><path d="M-306 8 L230 8" stroke="{RED}" stroke-width="4"/>'
            '<path d="M268 -20 L302 -10 L292 -4 L262 -8z" fill="#1d2a33"/>'
            + "".join(f'<circle cx="{wx}" cy="-15" r="5" fill="#1d2a33"/>' for wx in range(-230, 230, 30)) +
            '<path d="M-100 -12 l12 0 l0 24 l-12 0z M190 -18 l16 0 l0 30 l-16 0z" fill="#9aa5ad"/></g>')


def turboprop(x, y, s=1.0, length=1.0, pitch=0):
    """Dash 8 side view: high wing, T-tail, nacelle with propeller. length 1.0 = Q400, about 0.8 = Q200."""
    L = 300 * length
    return (f'<g transform="translate({x} {y}) rotate({-pitch}) scale({s})">'
            f'<path d="M{-L} -8 Q{-L-6} -24 {-L+26} -26 L{L*0.62} -26 Q{L*0.86} -26 {L+12} -4 Q{L+20} 6 {L+4} 12 Q{L*0.8} 26 {L*0.62} 26 L{-L+40} 22 Q{-L} 18 {-L} -8z" fill="#f6f8f9" stroke="#2b3a44" stroke-width="3"/>'
            f'<path d="M{-L+40} -24 L{-L+4} -170 L{-L+40} -170 L{-L+110} -24z" fill="#f6f8f9" stroke="#2b3a44" stroke-width="3"/>'
            f'<path d="M{-L-40} -176 L{-L+80} -176 L{-L+80} -162 L{-L-40} -164z" fill="#f6f8f9" stroke="#2b3a44" stroke-width="3"/>'
            f'<path d="M{-L+8} -160 L{-L+40} -168 L{-L+52} -120 L{-L+24} -112z" fill="{GREEN}"/>'
            f'<path d="M{-L*0.15} -30 L{L*0.32} -30 L{L*0.32} -40 L{-L*0.15} -40z" fill="#dfe4e8" stroke="#2b3a44" stroke-width="3"/>'
            f'<path d="M{L*0.02} -34 Q{L*0.02} 14 {L*0.12} 18 L{L*0.36} 18 Q{L*0.46} 10 {L*0.46} -34z" fill="#cfd6db" stroke="#2b3a44" stroke-width="3"/>'
            f'<ellipse cx="{L*0.48}" cy="-8" rx="10" ry="70" fill="#1d2a33" opacity=".35"/><circle cx="{L*0.48}" cy="-8" r="9" fill="#1d2a33"/>'
            f'<path d="M{-L+20} -4 L{L*0.9} -4" stroke="{GREEN}" stroke-width="8"/><path d="M{-L+20} 8 L{L*0.84} 8" stroke="{RED}" stroke-width="4"/>'
            f'<path d="M{L-14} -18 L{L+8} -8 L{L} -2 L{L-20} -6z" fill="#1d2a33"/>'
            + "".join(f'<rect x="{wx:.0f}" y="-17" width="9" height="12" rx="3" fill="#1d2a33"/>' for wx in [(-L + 70) + k * 27 for k in range(int((1.55 * L) / 27))]) +
            f'<path d="M{L*0.2} 22 l0 34 M{-L+90} 22 l0 26" stroke="#2b3a44" stroke-width="6"/><circle cx="{L*0.2}" cy="60" r="10" fill="#1d2a33"/><circle cx="{-L+90}" cy="52" r="9" fill="#1d2a33"/></g>')


SCENES = [
    ("Boeing 737-800", lambda: sky("day") + cloud(260, 560, 1.6) + cloud(1350, 610, 1.3) + mountains(820, "#5d7b67", "#7f9a87", seed=21) + jet(820, 330, 1.2, 6)),
    ("Dash 8-Q400", lambda: sky("dusk") + sun(1320, 470, 70) + desert(600) + turboprop(760, 330, 1.25, 1.0, 3)),
    ("Dash 8-Q200", lambda: sky("high") + cloud(300, 640, 1.5) + cloud(1300, 660, 1.4) + turboprop(800, 360, 1.3, 0.8, 0)),
]


def main():
    work = tempfile.mkdtemp(prefix="fleet-")
    for i, (_, fn) in enumerate(SCENES, 1):
        with open(os.path.join(work, f"fleet-{i}.svg"), "w", encoding="utf-8") as f:
            f.write(card(fn()))
    out = os.path.join(ROOT, "assets", "img", "fleet")
    subprocess.run(["node", os.path.join(ROOT, "tools", "make_pictures.js"), work, out], check=True)
    print("wrote", len(SCENES), "fleet pictures to", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
