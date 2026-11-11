#!/usr/bin/env python3
"""Render the closing case-study video (narrated slides) to courses/<slug>/media/video/finale.mp4.

Needs: the Kokoro TTS setup described in tools/make_audio.py, ffmpeg, and Node.js with Playwright.
Usage:
    .tts/bin/python tools/make_case_video.py --model kokoro.onnx --voices voices.bin [--voice af_heart]
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from case_video.dryden import SLIDES  # noqa: E402
from courses.cold_weather import COURSE  # noqa: E402

G, GD, GDEEP, RED, AMBER = "#1d7a3e", "#125a2b", "#0c3d1e", "#c8102e", "#d08a00"

ART = {
"route": f"""<svg viewBox="0 0 400 300"><path d="M60 200 Q200 90 340 170" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="10 9" opacity=".7"/>
<circle cx="60" cy="200" r="13" fill="#fff"/><circle cx="205" cy="128" r="16" fill="{AMBER}"/><circle cx="340" cy="170" r="13" fill="#fff"/>
<g font-family="Inter,Segoe UI,Arial" font-size="20" font-weight="700" fill="#fff" text-anchor="middle"><text x="60" y="240">Winnipeg</text><text x="205" y="96">Dryden</text><text x="340" y="210">Thunder Bay</text></g>
<path d="M300 150 l-22 -3 l9 -9 z" fill="#fff"/></svg>""",
"apu": f"""<svg viewBox="0 0 300 300"><rect x="70" y="90" width="160" height="120" rx="18" fill="none" stroke="#fff" stroke-width="10"/>
<path d="M150 112 l-26 48 h28 l-10 38 l34 -54 h-28 l12 -32z" fill="#fff"/><path d="M60 250 L240 50" stroke="{RED}" stroke-width="16" stroke-linecap="round"/></svg>""",
"snow": """<svg viewBox="0 0 300 300"><g stroke="#fff" stroke-width="12" stroke-linecap="round" fill="none">
<path d="M150 40v220M55 95l190 110M55 205l190-110M150 70l-22-22M150 70l22-22M150 230l-22 22M150 230l22 22"/></g></svg>""",
"stop": f"""<svg viewBox="0 0 300 300"><path d="M100 30h100l70 70v100l-70 70H100l-70-70V100z" fill="{RED}" stroke="#fff" stroke-width="8"/>
<text x="150" y="140" font-family="Inter,Segoe UI,Arial" font-size="40" font-weight="800" fill="#fff" text-anchor="middle">NO</text>
<text x="150" y="190" font-family="Inter,Segoe UI,Arial" font-size="34" font-weight="800" fill="#fff" text-anchor="middle">DE-ICE</text></svg>""",
"cabin": f"""<svg viewBox="0 0 300 300"><rect x="60" y="40" width="180" height="220" rx="80" fill="#cfe6f5" stroke="#fff" stroke-width="12"/>
<path d="M60 200 L240 150 L240 185 L60 235z" fill="#e9eef1"/><path d="M70 196 l40 -11 l8 7 l-40 11z M130 180 l35 -10 l6 6 l-35 10z" fill="#fff"/>
<circle cx="110" cy="80" r="5" fill="#fff"/><circle cx="170" cy="110" r="5" fill="#fff"/><circle cx="140" cy="140" r="5" fill="#fff"/><circle cx="200" cy="70" r="5" fill="#fff"/>
<text x="150" y="290" font-family="Inter,Segoe UI,Arial" font-size="26" font-weight="800" fill="{AMBER}" text-anchor="middle">?</text></svg>""",
"takeoff": f"""<svg viewBox="0 0 400 300"><rect x="10" y="230" width="230" height="22" fill="#3b4540"/><g fill="#fff"><rect x="30" y="239" width="24" height="4"/><rect x="80" y="239" width="24" height="4"/><rect x="130" y="239" width="24" height="4"/><rect x="180" y="239" width="24" height="4"/></g>
<path d="M60 236 Q200 230 240 200 Q300 165 380 70" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="8 8" opacity=".6"/>
<path d="M60 236 Q190 232 250 205 Q300 190 330 225" fill="none" stroke="{AMBER}" stroke-width="7" stroke-linecap="round"/>
<g fill="#0a2f17">{''.join(f'<path d="M{x} 255 l14 -40 l14 40z"/>' for x in range(270, 400, 22))}</g>
<text x="370" y="60" font-family="Inter,Segoe UI,Arial" font-size="16" fill="#fff" text-anchor="end">normal climb</text></svg>""",
"report": """<svg viewBox="0 0 300 300"><rect x="70" y="30" width="160" height="230" rx="10" fill="#fff"/>
<g stroke="#9fb5a8" stroke-width="8" stroke-linecap="round"><path d="M100 80h100M100 110h100M100 140h80M100 170h100M100 200h60"/></g>
<circle cx="205" cy="225" r="34" fill="#c8102e"/><text x="205" y="234" font-family="Inter,Segoe UI,Arial" font-size="24" font-weight="800" fill="#fff" text-anchor="middle">191</text></svg>""",
}

CSS = f"""
*{{box-sizing:border-box}}html,body{{margin:0;width:1280px;height:720px;overflow:hidden;font-family:Inter,"Segoe UI",Roboto,Arial,sans-serif}}
.slide{{position:relative;width:1280px;height:720px;color:#fff;background:linear-gradient(120deg,{GDEEP} 0%,{GD} 50%,#2a8a50 100%);padding:70px 80px}}
.slide::after{{content:"";position:absolute;inset:0;background:radial-gradient(900px 400px at 90% 0%,rgba(255,255,255,.13),transparent 60%)}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:64px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 40px;z-index:2;border-top:5px solid {G}}}
.bar img{{height:38px}}.bar span{{color:{GD};font-weight:700;font-size:17px}}
.kicker{{font-size:20px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#bfe3cb;margin-bottom:14px}}
h1{{font-size:76px;line-height:1.05;margin:0 0 18px}}h2{{font-size:50px;line-height:1.1;margin:0 0 30px}}
.sub{{font-size:30px;color:#dff0e5;margin:0}}
.title{{display:flex;flex-direction:column;justify-content:center;padding-bottom:120px}}
.content{{position:relative;z-index:1}}
.split .content{{width:760px}}
ul{{margin:0;padding:0;list-style:none}}ul li{{font-size:27px;line-height:1.35;margin:0 0 20px;padding-left:34px;position:relative;color:#eef7f1}}
ul li::before{{content:"";position:absolute;left:0;top:13px;width:14px;height:14px;border-radius:50%;background:{AMBER}}}
b{{color:#fff}}
.art{{position:absolute;right:70px;top:150px;width:360px;height:360px;z-index:1;display:flex;align-items:center;justify-content:center}}
.art svg{{width:100%;height:100%}}
ol.chain{{margin:0;padding:0;list-style:none;counter-reset:c}}
ol.chain li{{counter-increment:c;font-size:23px;line-height:1.35;margin:0 0 16px;padding:12px 18px 12px 70px;position:relative;background:rgba(255,255,255,.09);border-radius:12px;color:#eef7f1}}
ol.chain li::before{{content:counter(c);position:absolute;left:16px;top:50%;transform:translateY(-50%);width:38px;height:38px;border-radius:50%;background:#fff;color:{GDEEP};font-weight:800;display:grid;place-items:center;font-size:20px}}
ol.chain li span{{float:right;font-size:17px;font-weight:700;color:#bfe3cb;margin-left:16px;padding-top:5px}}
ol.chain.q li{{font-size:26px;padding-top:16px;padding-bottom:16px}}
ol.chain.two{{columns:2;column-gap:24px}}ol.chain.two li{{break-inside:avoid;font-size:27px;font-weight:600}}
.snowfx{{position:absolute;inset:0;z-index:0;opacity:.18;background-image:radial-gradient(#fff 1.6px,transparent 2px),radial-gradient(#fff 1.2px,transparent 1.6px);background-size:90px 90px,55px 55px;background-position:0 0,30px 40px}}
"""


def slide_html(s, logo):
    art = f'<div class="art">{ART[s["art"]]}</div>' if s.get("art") else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="slide {s['kind']}"><div class="snowfx"></div><div class="content">{s['html']}</div>{art}
<div class="bar"><img src="{logo}" alt=""><span>Cold Weather Operations · Case study</span></div></div></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--voices", required=True)
    ap.add_argument("--voice", default="af_heart")
    a = ap.parse_args()

    import numpy as np
    import soundfile as sf
    from kokoro_onnx import Kokoro
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    from make_audio import to_speech, sentences

    work = tempfile.mkdtemp(prefix="casevid-")
    logo = "file://" + os.path.join(ROOT, "assets", "img", "logo.png")
    pages = []
    for i, s in enumerate(SLIDES):
        p = os.path.join(work, f"s{i:02d}.html")
        with open(p, "w", encoding="utf-8") as f:
            f.write(slide_html(s, logo))
        pages.append(p)

    # Screenshots (1920x1080 via device scale 1.5)
    shot_js = os.path.join(work, "shot.js")
    with open(shot_js, "w") as f:
        f.write("""const { chromium } = require('playwright');
(async () => { const pages = JSON.parse(process.argv[2]); const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1.5 });
for (const f of pages) { await p.goto('file://' + f); await p.waitForTimeout(150); await p.screenshot({ path: f.replace('.html', '.png') }); }
await b.close(); })();""")
    subprocess.run(["node", shot_js, json.dumps(pages)], check=True)

    k = Kokoro(a.model, a.voices)
    segs = []
    for i, s in enumerate(SLIDES):
        pieces = [np.zeros(int(24000 * 0.6), dtype=np.float32)]
        for chunk in sentences(to_speech(f"<p>{s['say']}</p>")):
            samples, sr = k.create(chunk, voice=a.voice, speed=0.97, lang="en-us")
            pieces += [samples.astype(np.float32), np.zeros(int(sr * 0.3), dtype=np.float32)]
        pieces.append(np.zeros(int(24000 * 0.9), dtype=np.float32))
        wav = os.path.join(work, f"s{i:02d}.wav")
        sf.write(wav, np.concatenate(pieces), 24000)
        dur = sum(len(x) for x in pieces) / 24000
        mp4 = os.path.join(work, f"s{i:02d}.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "25", "-i", pages[i].replace(".html", ".png"),
                        "-i", wav, "-t", f"{dur:.2f}",
                        "-vf", f"scale=1920:1080,format=yuv420p,fade=t=in:st=0:d=0.5,fade=t=out:st={dur-0.5:.2f}:d=0.5",
                        "-af", f"afade=t=in:st=0:d=0.3,afade=t=out:st={dur-0.4:.2f}:d=0.4",
                        "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage", "-crf", "26",
                        "-c:a", "aac", "-b:a", "96k", "-ar", "44100", "-ac", "1", mp4], check=True)
        segs.append(mp4)
        print(f"slide {i+1}/{len(SLIDES)}: {dur:.1f}s", flush=True)

    lst = os.path.join(work, "list.txt")
    with open(lst, "w") as f:
        f.write("".join(f"file '{p}'\n" for p in segs))
    outdir = os.path.join(ROOT, "courses", COURSE["slug"], "media", "video")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "finale.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy",
                    "-movflags", "+faststart", "-metadata", "title=Case Study — Air Ontario Flight 1363",
                    "-metadata", "artist=Domestic Airlines Training", out], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", pages[0].replace(".html", ".png"), "-vf", "scale=1280:720",
                    os.path.join(outdir, "finale-poster.jpg")], check=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
