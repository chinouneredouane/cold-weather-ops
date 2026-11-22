#!/usr/bin/env python3
"""Compute, for every lesson MP3, the time at which each slide's narration starts (slide cues).

The slide player uses these cues so that the narration follows the slide on screen: Next / Previous jump the audio
to the slide, and while the narration plays the slides advance with it.

Method: the narration script is built exactly as tools/make_audio.py builds it. For each slide we find where its text
starts in the script, convert that character position to a time (proportional to the text), and snap it to the nearest
pause in the recording (make_audio leaves 0.35 s of silence between sentence groups).

Usage: python3 tools/make_cues.py [course_slug ...]      (default: every course)
Output: courses/<slug>/media/audio/lesson-XX.cues.json  →  {"duration": s, "cues": [t0, t1, ..., null]}
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build  # noqa: E402
import make_audio  # noqa: E402

PKG = {}  # slug -> package name for make_audio.load_course
for name in os.listdir(os.path.join(ROOT, "tools", "courses")):
    init = os.path.join(ROOT, "tools", "courses", name, "__init__.py")
    if os.path.exists(init):
        m = re.search(r'slug="([^"]+)"', open(init, encoding="utf-8").read())
        if m:
            PKG[m.group(1)] = name


def slide_texts(course, n):
    """Speech text of each slide, in the order build_lesson creates the slides (knowledge check: None)."""
    L = course["lessons"][n - 1]
    intro, body = make_audio.slides_mod.body_slides(L["body"])
    first = f"<p>Lesson {n}. {L['title']}.</p><p>Learning objectives. {' '.join(L['objectives'])}</p>{intro}"
    out = [make_audio.to_speech(first)]
    for _t, h in body:
        h = re.sub(r"<h2>[^<]*\(\d+\)</h2>", "", h)
        out.append(make_audio.to_speech(h.replace("<h2>", "<p>").replace("</h2>", "</p>")))
    out.append(make_audio.to_speech("<p>Key takeaways. " + " ".join(L["takeaways"]) + "</p>"))
    out.append(None)
    return out


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip() or 0)


def silences(path, noise="-80dB", d="0.3"):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", f"silencedetect=noise={noise}:d={d}", "-f", "null", "-"],
                       capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]
    return [(s + e) / 2 for s, e in zip(starts, ends)]   # middle of each pause


def norm(t):
    return re.sub(r"[^a-z0-9]", "", t.lower())


def cues_for(course, n, mp3):
    make_audio.load_course(PKG[course["slug"]])
    script = make_audio.lesson_script(n)
    chunks = make_audio.sentences(script)
    texts = slide_texts(course, n)
    total = duration(mp3)
    ns = norm(script)
    # slide start positions in the (normalised) script
    pos, offsets = 0, []
    for t in texts[:-1]:
        key = norm(t)[:30]
        j = ns.find(key, pos) if key else -1
        if j < 0:
            j = pos
        offsets.append(j)
        pos = j + max(1, len(norm(t)) // 2)
    # chunk boundaries in the script and in the recording
    bounds, acc = [], 0
    for ch in chunks:
        bounds.append(acc)
        acc += len(norm(ch))
    pauses = [p for p in silences(mp3) if 0.3 < p < total - 0.3]
    exact = len(pauses) == len(chunks) - 1
    starts = [0.0] + pauses if exact else None          # start time of each chunk
    ends = (pauses + [total]) if exact else None
    loose = silences(mp3, "-38dB", "0.25")
    cues = []
    for k, j in enumerate(offsets):
        if k == 0:
            cues.append(0.0)
            continue
        if exact:
            i = max(x for x in range(len(bounds)) if bounds[x] <= j)
            clen = (bounds[i + 1] if i + 1 < len(bounds) else acc) - bounds[i]
            frac = (j - bounds[i]) / max(1, clen)
            t = starts[i] + frac * (ends[i] - starts[i])
            if frac > 0.02:   # slide starts inside a sentence group: snap to the nearest natural pause
                near = [p for p in loose if abs(p - t) <= 2.5]
                t = min(near, key=lambda p: abs(p - t)) if near else t
        else:
            est = total * j / max(1, len(ns))
            near = [p for p in loose if abs(p - est) <= 5]
            t = min(near, key=lambda p: abs(p - est)) if near else est
        t = max(t, cues[-1] + 0.5)
        cues.append(round(t, 2))
    cues.append(None)   # knowledge check: no narration
    return dict(duration=round(total, 2), cues=cues, exact=exact)


def main():
    wanted = set(sys.argv[1:])
    for c in build.COURSES:
        if wanted and c["slug"] not in wanted:
            continue
        adir = os.path.join(ROOT, "courses", c["slug"], "media", "audio")
        done = exact = 0
        for n in range(1, len(c["lessons"]) + 1):
            mp3 = os.path.join(adir, f"lesson-{n:02d}.mp3")
            if not os.path.exists(mp3):
                continue
            cj = os.path.join(adir, f"lesson-{n:02d}.cues.json")
            if os.path.exists(cj) and json.load(open(cj)).get("source") == "recording":
                done += 1
                exact += 1
                continue
            data = cues_for(c, n, mp3)
            exact += data.pop("exact")
            with open(os.path.join(adir, f"lesson-{n:02d}.cues.json"), "w", encoding="utf-8") as f:
                json.dump(data, f)
            done += 1
        print(f"{c['title']}: cues for {done} lessons ({exact} aligned on recording pauses)")


if __name__ == "__main__":
    main()
