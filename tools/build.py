#!/usr/bin/env python3
"""Build the Domestic Airlines Training Academy static site.

Usage:  python3 tools/build.py

Reads course definitions from tools/courses/ and writes HTML into the repository
root (index.html) and courses/<slug>/. Uses only the Python standard library.
To add a course: create tools/courses/<name>/ with a COURSE dict (see cold_weather)
and add it to COURSES below.
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

from courses.cold_weather import COURSE as COLD_WEATHER  # noqa: E402
from courses.upset_recovery import COURSE as UPSET_RECOVERY  # noqa: E402
from courses.rvsm import COURSE as RVSM  # noqa: E402
from courses.cfit import COURSE as CFIT  # noqa: E402
from courses.hot_weather import COURSE as HOT_WEATHER  # noqa: E402
from courses.cpdlc import COURSE as CPDLC  # noqa: E402
from handbook import build_print  # noqa: E402

COURSES = [COLD_WEATHER, UPSET_RECOVERY, RVSM, CFIT, HOT_WEATHER, CPDLC]

# Courses shown on the portal as "in preparation" (no pages yet).
UPCOMING = []

# Ground Refresher Training Follow-up Sheet — the same 12 subjects every year, for all fleets.
# (code, title, link or None, note)
REFRESHER = {
    "Winter season": [
        ("W1", "Windshear Recovery and Thunderstorm Avoidance", None, ""),
        ("W2", "Cold Weather Operations and Contaminated Runways (GRF)", "courses/cold-weather-operations/index.html", "Cold Weather Operations — Module 4"),
        ("W3", "PBN Refresher", None, ""),
        ("W4", "De-icing and Anti-icing", "courses/cold-weather-operations/index.html", "Cold Weather Operations — Modules 2 and 3"),
        ("W5", "Operations Manual (MANEX) and Regulations", None, "Company documents needed"),
        ("W6", "MEL", None, "Company documents needed"),
    ],
    "Summer season": [
        ("S1", "EGPWS / TAWS and CFIT Prevention", "courses/cfit-egpws-refresher/index.html", ""),
        ("S2", "RVSM (B737-800; awareness for Dash 8)", "courses/rvsm-refresher/index.html", ""),
        ("S3", "Company Wind Limitations (OM B, FCOM, AFM)", None, "Company documents needed"),
        ("S4", "Approaches Authorised by the DACM — Ceiling and Visibility (AOC)", None, "Company documents needed"),
        ("S5", "Allowances for Inoperative Ground Equipment (OM A)", None, "Company documents needed"),
        ("S6", "Hot Weather Operations", "courses/hot-weather-operations/index.html", ""),
    ],
    "Additional recurrent courses": [
        ("+", "CPDLC — Controller-Pilot Data Link", "courses/cpdlc/index.html", ""),
        ("+", "Upset Prevention and Recovery (UPRT)", "courses/upset-prevention-recovery/index.html", ""),
    ],
}

# Courses built outside this generator and copied into courses/<folder>/ as they are.
EXTERNAL = [
    dict(title="Command Upgrade", href="courses/command-upgrade/index.html", cover="slate", icon="people",
         tagline="The 20 practical briefings (PL 01 to PL 20) of the command upgrade course: operations, flight preparation, "
                 "in-flight management, abnormal operations and severe emergencies.",
         meta="20 briefings · knowledge check after each · certificate"),
]

ACADEMY = "Training"
ARABIC = "الخطوط الجوية الداخلية"
YEAR = "2026"

ICONS = {
    "snow": '<path d="M50 6v88M12 28l76 44M12 72l76-44M50 18l-9-9M50 18l9-9M50 82l-9 9M50 82l9 9M21 33l-12 3M21 33l-3-12M79 67l12-3M79 67l3 12M21 67l-3 12M21 67l-12-3M79 33l3-12M79 33l12 3" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>',
    "drop": '<path d="M50 8C38 30 22 46 22 64a28 28 0 0 0 56 0C78 46 62 30 50 8z" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/><path d="M36 66a14 14 0 0 0 14 14" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>',
    "search": '<circle cx="42" cy="42" r="26" fill="none" stroke="currentColor" stroke-width="7"/><path d="M62 62l26 26" stroke="currentColor" stroke-width="9" stroke-linecap="round"/>',
    "runway": '<path d="M34 92L44 8h12l10 84z" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/><path d="M50 20v10M50 42v10M50 64v10" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>',
    "gear": '<circle cx="50" cy="50" r="15" fill="none" stroke="currentColor" stroke-width="7"/><path d="M50 8v14M50 78v14M8 50h14M78 50h14M20 20l10 10M70 70l10 10M80 20L70 30M30 70L20 80" stroke="currentColor" stroke-width="8" stroke-linecap="round"/><circle cx="50" cy="50" r="30" fill="none" stroke="currentColor" stroke-width="6"/>',
    "plane": '<path d="M50 8c5 0 7 6 7 12v22l33 18v9l-33-9v20l10 8v7l-17-5-17 5v-7l10-8V60l-33 9v-9l33-18V20c0-6 2-12 7-12z" fill="none" stroke="currentColor" stroke-width="5" stroke-linejoin="round"/>',
    "sun": '<circle cx="50" cy="50" r="18" fill="none" stroke="currentColor" stroke-width="6"/><path d="M50 8v14M50 78v14M8 50h14M78 50h14M20 20l10 10M70 70l10 10M80 20L70 30M30 70L20 80" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>',
    "people": '<circle cx="34" cy="32" r="13" fill="none" stroke="currentColor" stroke-width="6"/><circle cx="68" cy="36" r="11" fill="none" stroke="currentColor" stroke-width="6"/><path d="M10 86c2-18 12-28 24-28s22 10 24 28M54 86c1-14 7-22 14-22s14 8 16 22" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>',
}


def icon(name, cls="", size=None):
    attrs = f' class="{cls}"' if cls else ""
    if size:
        attrs += f' width="{size}" height="{size}"'
    return f'<svg viewBox="0 0 100 100"{attrs} aria-hidden="true" focusable="false">{ICONS[name]}</svg>'


def esc(s):
    return html.escape(str(s), quote=True)


def lesson_file(n):
    return f"lesson-{n:02d}.html"


# --------------------------------------------------------------------------- shell

def page(*, title, description, root, course=None, active=None, body_attrs="", main="", scripts=()):
    """Common page shell. The header markup is kept identical to the original course."""
    header_en = f"DOMESTIC AIRLINES — {course['header_title']}" if course else f"DOMESTIC AIRLINES — {ACADEMY}"
    if course:
        c = course["_base"]
        nav_items = [("home", f"{c}index.html", "Home"), ("quiz", f"{c}quiz.html", "Quiz")]
        if course.get("finale"):
            nav_items.append(("finale", f"{c}finale.html", "Final Video"))
        brand_href = f"{c}index.html"
    else:
        nav_items = [("home", "index.html", "Home")]
        brand_href = "index.html"
    current = ' aria-current="page"'
    nav = "\n      ".join(
        f'<a href="{href}"{current if key == active else ""}>{label}</a>' for key, href, label in nav_items
    )
    script_tags = "\n".join(f'<script src="{s}"></script>' for s in scripts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}" />
  <meta name="theme-color" content="#125a2b" />
  <link rel="icon" type="image/png" href="{root}assets/img/logo.png" />
  <link rel="stylesheet" href="{root}assets/css/academy.css" />
</head>
<body {body_attrs}>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="topbar">
    <div class="brand">
      <a href="{brand_href}"><img src="{root}assets/img/logo.png" alt="Domestic Airlines Logo" class="logo" /></a>
      <div class="brand-text">
        <div class="ar">{ARABIC}</div>
        <div class="en">{esc(header_en)}</div>
      </div>
    </div>
    <nav aria-label="Main">
      {nav}
    </nav>
  </header>
  <div class="progress" aria-hidden="true"><div id="progressBar"></div></div>
  <main id="main">
{main}
  </main>
  <footer class="bottombar">
    <img src="{root}assets/img/logo.png" alt="Domestic Airlines Logo" class="logo small" />
    <div class="copy">&copy; {YEAR} Domestic Airlines — Training</div>
    <a href="{root}index.html">All courses</a>
    <p class="disclaimer">Training material only. It does not replace the Aircraft Flight Manual, FCOM, QRH, MEL or the Domestic Airlines Operations Manual, which always take precedence.</p>
  </footer>
{script_tags}
</body>
</html>
"""


def course_attrs(course, lesson=0, extra=""):
    a = f'data-course="{course["slug"]}" data-total="{len(course["lessons"])}"'
    if lesson:
        a += f' data-lesson="{lesson}"'
    return (a + " " + extra).strip()


# --------------------------------------------------------------------------- portal

def refresher_html():
    out = []
    for season, items in REFRESHER.items():
        rows = []
        for code, title, link, note in items:
            if link:
                rows.append(f'<a class="ref-item" href="{link}"><span class="ref-code">{esc(code)}</span><span class="ref-title">{esc(title)}'
                            f'{f"<small>{esc(note)}</small>" if note else ""}</span><span class="pill">Available</span></a>')
            else:
                rows.append(f'<div class="ref-item soon"><span class="ref-code">{esc(code)}</span><span class="ref-title">{esc(title)}'
                            f'{f"<small>{esc(note)}</small>" if note else ""}</span><span class="pill red">In preparation</span></div>')
        out.append(f'<div class="card ref-season"><h3>{esc(season)}</h3>{"".join(rows)}</div>')
    return f'<div class="ref-grid">{"".join(out)}</div>'


def build_portal():
    cards = []
    for c in [c for c in COURSES if c.get("group") != "refresher"]:
        n = len(c["lessons"])
        mins = sum(l["minutes"] for l in c["lessons"])
        cards.append(f"""
      <a class="card course-card" href="courses/{c['slug']}/index.html">
        <div class="cover">{icon(c['icon'])}<span class="pill">Available</span></div>
        <div class="body">
          <h3>{esc(c['title'])}</h3>
          <p class="muted">{esc(c['tagline'])}</p>
          <div class="meta">{n} lessons · about {round(mins / 60 * 2) / 2:g} hours · final quiz</div>
        </div>
      </a>""")
    for x in EXTERNAL:
        cards.append(f"""
      <a class="card course-card" href="{x['href']}">
        <div class="cover {x['cover']}">{icon(x['icon'])}<span class="pill">Available</span></div>
        <div class="body">
          <h3>{esc(x['title'])}</h3>
          <p class="muted">{esc(x['tagline'])}</p>
          <div class="meta">{esc(x['meta'])}</div>
        </div>
      </a>""")
    for u in UPCOMING:
        cards.append(f"""
      <div class="card course-card soon">
        <div class="cover {u['cover']}">{icon(u['icon'])}<span class="pill red">In preparation</span></div>
        <div class="body">
          <h3>{esc(u['title'])}</h3>
          <p class="muted">{esc(u['tagline'])}</p>
          <div class="meta">Coming soon</div>
        </div>
      </div>""")
    main = f"""
    <section class="hero">
      {icon('snow', 'hero-art')}
      <div class="wrap">
        <div class="eyebrow">Domestic Airlines</div>
        <h1>Training Academy</h1>
        <p class="lede">Self-paced e-learning courses for Domestic Airlines crews and operations staff. Choose a course to begin — your progress is saved in this browser.</p>
      </div>
    </section>
    <div class="wrap">
      <h2>Courses</h2>
      <div class="course-grid">{''.join(cards)}
      </div>
      <h2 id="refresher">Ground Refresher Training</h2>
      <p class="muted">The seasonal ground refresher programme for all fleets — Boeing 737-800, Dash 8-Q400 and Dash 8-Q200 — following the Ground Refresher Training Follow-up Sheet. The same subjects are repeated every year.</p>
      {refresher_html()}
    </div>"""
    out = page(title="Training Academy — Domestic Airlines", description="Domestic Airlines e-learning courses for crews and operations staff.",
               root="", main=main, active="home")
    write("index.html", out)


# --------------------------------------------------------------------------- course pages

def module_of(course, n):
    for i, m in enumerate(course["modules"]):
        if n in m["lessons"]:
            return i, m
    raise ValueError(n)


def build_course_home(course):
    lessons = course["lessons"]
    total_min = sum(l["minutes"] for l in lessons)
    hours = round(total_min / 60 * 2) / 2
    mods = []
    for i, m in enumerate(course["modules"]):
        nums = list(m["lessons"])
        items = "".join(
            f'<li><a href="lessons/{lesson_file(n)}" data-lesson-link="{n}"><span class="state" aria-hidden="true"></span>'
            f'<span class="num">{n:02d}</span><span class="t">{esc(lessons[n-1]["title"])}</span>'
            f'<span class="dur">{lessons[n-1]["minutes"]} min</span></a></li>'
            for n in nums)
        mods.append(f"""
        <details class="card module"{' open' if i == 0 else ''}>
          <summary>
            <span class="mod-num">{i+1}</span>
            <span class="mod-title"><b>Module {i+1} — {esc(m['title'])}</b><span>{esc(m['summary'])}</span></span>
            <span class="mod-progress" data-module-progress="{','.join(map(str, nums))}">0 / {len(nums)}</span>
            <svg class="chev" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
          </summary>
          <ul class="lesson-list">{items}</ul>
        </details>""")

    objectives = course["objectives"]
    main = f"""
    <section class="hero">
      {icon(course['icon'], 'hero-art')}
      <div class="wrap">
        <div class="eyebrow">Domestic Airlines e-learning</div>
        <h1>{esc(course['title'])}</h1>
        <p class="lede">{esc(course['tagline'])}</p>
        <div class="btn-row">
          <a class="btn primary" id="resumeBtn" href="lessons/{lesson_file(1)}">Start Course</a>
          <a class="btn" href="#syllabus">View Syllabus</a>
          <a class="btn" href="pdf/handbook.pdf" download>⬇ Course handbook (PDF)</a>
        </div>
      </div>
    </section>
    <div class="wrap">
      <div class="facts">
        <div class="card fact"><b>{len(lessons)}</b><span>lessons in {len(course['modules'])} modules</span></div>
        <div class="card fact"><b>≈ {hours:g} h</b><span>total duration</span></div>
        <div class="card fact"><b>{course['quiz_count']}</b><span>quiz questions from a bank of {len(course['questions'])}</span></div>
        <div class="card fact"><b>{course['pass_mark']} %</b><span>pass mark · certificate</span></div>
      </div>

      <div class="two-col" style="margin-top:28px">
        <div>
          <div class="card panel">
            <h2>Purpose</h2>
            <p>{esc(course['purpose'])}</p>
            <h3>Who should take this course</h3>
            <p>{esc(course['audience'])}</p>
            <h3>What you will be able to do</h3>
            <ul class="checklist">{''.join(f'<li>{esc(o)}</li>' for o in objectives)}</ul>
          </div>
        </div>
        <aside class="card panel">
          <h2>Your progress</h2>
          <div class="ring">
            <svg width="64" height="64" viewBox="0 0 64 64" aria-hidden="true">
              <circle cx="32" cy="32" r="26" fill="none" stroke="#e6efe9" stroke-width="8"/>
              <circle id="progressRing" cx="32" cy="32" r="26" fill="none" stroke="#1d7a3e" stroke-width="8" stroke-linecap="round" transform="rotate(-90 32 32)" stroke-dasharray="163.4" stroke-dashoffset="163.4"/>
            </svg>
            <div><b data-progress-pct>0%</b><div class="muted" data-progress-text>0 of {len(lessons)} lessons completed</div></div>
          </div>
          <p id="quizStatus" class="muted" style="margin-top:14px"></p>
          <div class="btn-row"><a class="btn" href="quiz.html">Final Quiz</a><a class="btn ghost" href="certificate.html">Certificate</a></div>
          <p class="muted" style="font-size:13.5px;margin-top:14px">Progress is saved in this browser on this device. Each lesson has narration — press <em>Listen</em>.</p>
        </aside>
      </div>

      <section id="syllabus">
        <h2>Course Syllabus</h2>
        {''.join(mods)}
      </section>
    </div>"""
    out = page(title=f"{course['title']} — Domestic Airlines", description=course["tagline"],
               root="../../", course=course, active="home", body_attrs=course_attrs(course), main=main,
               scripts=["../../assets/js/course.js"])
    write(f"courses/{course['slug']}/index.html", out)


def sidebar(course, current):
    parts = ['<nav class="card sidebar" id="courseContents" aria-label="Course contents">']
    for i, m in enumerate(course["modules"]):
        parts.append(f'<h2>Module {i+1} · {esc(m["title"])}</h2><ul>')
        for n in m["lessons"]:
            cur = ' aria-current="page"' if n == current else ""
            parts.append(f'<li><a href="{lesson_file(n)}" data-lesson-link="{n}"{cur}><span class="state" aria-hidden="true"></span>'
                         f'<span>{n:02d}. {esc(course["lessons"][n-1]["title"])}</span></a></li>')
        parts.append("</ul>")
    parts.append("</nav>")
    return "".join(parts)


def build_lesson(course, n):
    L = course["lessons"][n - 1]
    total = len(course["lessons"])
    mi, mod = module_of(course, n)
    objectives = "".join(f"<li>{esc(o)}</li>" for o in L["objectives"])
    takeaways = "".join(f"<li>{esc(t)}</li>" for t in L["takeaways"])
    chk = L["check"]
    opts = "".join(f'<button type="button" class="opt" aria-pressed="false">{esc(o)}</button>' for o in chk["options"])
    prev_btn = (f'<a class="btn" href="{lesson_file(n-1)}">◀ Previous<small>{esc(course["lessons"][n-2]["title"])}</small></a>'
                if n > 1 else '<a class="btn" href="../index.html">◀ Course home</a>')
    next_btn = (f'<a class="btn primary" id="nextLesson" href="{lesson_file(n+1)}">Next ▶<small>{esc(course["lessons"][n]["title"])}</small></a>'
                if n < total else '<a class="btn primary" id="nextLesson" href="../quiz.html">Take the Final Quiz ▶</a>')
    audio_src = f"../media/audio/lesson-{n:02d}.mp3"
    img = course.get("images", {}).get(n)
    picture = (f'<figure class="lesson-figure"><img src="../media/images/lesson-{n:02d}.jpg" alt="{esc(img[1])}" loading="lazy" decoding="async">'
               f'<figcaption>{esc(img[2])}</figcaption></figure>') if img else ""

    main = f"""
    <div class="lesson-layout">
      <div>
        <button class="btn ghost sidebar-toggle" aria-controls="courseContents" aria-expanded="false">Show course contents</button>
        {sidebar(course, n)}
      </div>
      <article class="lesson">
        <header class="lesson-head">
          {icon(mod['icon'], 'art')}
          <div class="eyebrow">Module {mi+1} · {esc(mod['title'])}</div>
          <h1>Lesson {n:02d}: {esc(L['title'])}</h1>
          <div class="meta"><span>Lesson {n} of {total}</span><span>≈ {L['minutes']} min</span><a class="pdf-link" href="../pdf/lesson-{n:02d}.pdf" download>⬇ Download PDF</a></div>
        </header>
        <div class="card lesson-body">
          <div class="audio-block">
            <span class="label">Lesson narration</span>
            <audio controls preload="metadata" style="display:none"><source src="{audio_src}" type="audio/mpeg"></audio>
            <button type="button" class="btn primary" data-tts style="display:none">Listen</button>
            <button type="button" class="btn ghost" data-tts-stop style="display:none">Stop</button>
            <div class="audio-status" aria-live="polite">Checking for narration…</div>
          </div>
          <section class="objectives" data-narrate>
            <h2>Learning objectives</h2>
            <ul>{objectives}</ul>
          </section>
          {picture}
          <div data-narrate>
{L['body']}
          </div>
          <section class="takeaways" data-narrate>
            <h2>Key takeaways</h2>
            <ul>{takeaways}</ul>
          </section>
          <section class="kc" data-answer="{chk['answer']}" data-explain="{esc(chk['explain'])}">
            <h2>Knowledge check</h2>
            <p class="q">{esc(chk['q'])}</p>
            <div class="opts">{opts}</div>
            <div class="fb" aria-live="polite"></div>
          </section>
          <div class="lesson-end"></div>
        </div>
        <nav class="lesson-nav" aria-label="Lesson navigation">{prev_btn}{next_btn}</nav>
      </article>
    </div>"""
    out = page(title=f"Lesson {n:02d}: {L['title']} — {course['title']}", description=L["objectives"][0],
               root="../../../", course=dict(course, _base="../"), active=None,
               body_attrs=course_attrs(course, n), main=main, scripts=["../../../assets/js/course.js"])
    write(f"courses/{course['slug']}/lessons/{lesson_file(n)}", out)
    write_narration(course, n, L)


def write_narration(course, n, L):
    """Plain-text narration script for recording a voice-over MP3."""
    text = re.sub(r"<figure.*?</figure>", "", L["body"], flags=re.S)
    text = re.sub(r'<div class="dialog".*?</div>', "", text, flags=re.S)
    text = re.sub(r"</(p|li|h2|h3|tr|div)>", "\n", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = "\n".join(re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines())
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    script = (f"Domestic Airlines — {course['title']}\nLesson {n}: {L['title']}\n\n"
              "Learning objectives:\n" + "\n".join(f"- {o}" for o in L["objectives"]) +
              "\n\n" + text + "\n\nKey takeaways:\n" + "\n".join(f"- {t}" for t in L["takeaways"]) + "\n")
    write(f"courses/{course['slug']}/narration/lesson-{n:02d}.txt", script)


def build_quiz(course):
    main = f"""
    <div class="content">
      <div class="card quiz-intro">
        <div class="eyebrow">{esc(course['title'])}</div>
        <h1>Final Quiz</h1>
        <p>{course['quiz_count']} questions are drawn at random from a bank of {len(course['questions'])}. Answer every question, then submit. You need <strong>{course['pass_mark']} %</strong> to pass. Each attempt uses a new set of questions, and the answer order is shuffled.</p>
        <div id="quizGate" class="callout"></div>
      </div>
      <div id="quizResult" aria-live="polite"></div>
      <form id="quizForm" novalidate></form>
      <div class="quiz-bar">
        <span id="answeredCount" class="muted">0 answered</span>
        <div class="btn-row">
          <button class="btn primary" id="submitQuiz" type="button">Submit Quiz</button>
          <button class="btn" id="retryQuiz" type="button" style="display:none">Try a new set of questions</button>
        </div>
      </div>
    </div>"""
    out = page(title=f"Final Quiz — {course['title']}", description=f"Final quiz for {course['title']}.",
               root="../../", course=dict(course, _base=""), active="quiz",
               body_attrs=course_attrs(course, extra=f'data-quiz-count="{course["quiz_count"]}" data-pass="{course["pass_mark"]}" data-finale="{1 if course.get("finale") else 0}"'),
               main=main, scripts=["../../assets/js/course.js", "data/questions.js", "../../assets/js/quiz.js"])
    write(f"courses/{course['slug']}/quiz.html", out)
    data = json.dumps(course["questions"], ensure_ascii=False, indent=1)
    write(f"courses/{course['slug']}/data/questions.js",
          f"/* {course['title']} — question bank ({len(course['questions'])} questions). Generated by tools/build.py. */\n"
          f"window.QUESTION_BANK = {data};\n")


def build_finale(course):
    fin = course["finale"]
    further = "".join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a></li>' for t, u in fin.get("further", []))
    yt = course.get("finale_youtube")  # YouTube video ID: embed instead of hosting a copy
    if yt:
        main = f"""
    <section class="content">
      <div class="eyebrow">{esc(course['title'])}</div>
      <h1>Closing Video</h1>
      <p>{esc(fin['intro'])}</p>
      <div class="video-wrap">
        <iframe src="https://www.youtube-nocookie.com/embed/{esc(yt)}?rel=0" title="Closing video" style="width:100%;height:100%;border:0"
          allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen loading="lazy"></iframe>
      </div>
      <p class="muted" style="text-align:center;font-size:13.5px">Video embedded from YouTube; all rights belong to its creator.</p>
      <div class="btn-row" style="justify-content:center;margin-top:20px">
        <a class="btn" href="index.html">Back to course home</a>
        <a class="btn" href="quiz.html">Go to quiz</a>
        <a class="btn primary" href="certificate.html">Certificate</a>
      </div>
    </section>"""
        out = page(title=f"Closing Video — {course['title']}", description=f"Closing video for {course['title']}.",
                   root="../../", course=dict(course, _base=""), active="finale", body_attrs=course_attrs(course),
                   main=main, scripts=["../../assets/js/course.js"])
        write(f"courses/{course['slug']}/finale.html", out)
        return
    main = f"""
    <section class="content">
      <div class="eyebrow">{esc(course['title'])}</div>
      <h1>{esc(fin['title'])}</h1>
      <p>{esc(fin['intro'])}</p>
      <div class="video-wrap">
        <video id="finaleVideo" controls playsinline preload="metadata" poster="media/video/finale-poster.jpg">
          <source src="media/video/finale.mp4" type="video/mp4">
        </video>
        <div id="videoPlaceholder" class="placeholder">
          <div><p><strong>The closing video is not available yet.</strong></p><p>Add the file <code>media/video/finale.mp4</code> to this course folder to enable playback.</p></div>
        </div>
      </div>
      <div class="card panel" style="margin-top:20px">
        <h2 style="margin-top:0;font-size:19px">Further reading</h2>
        <ul>
          {further}
        </ul>
      </div>
      <div class="btn-row" style="justify-content:center;margin-top:20px">
        <a class="btn" href="index.html">Back to course home</a>
        <a class="btn" href="quiz.html">Go to quiz</a>
        <a class="btn primary" href="certificate.html">Certificate</a>
      </div>
    </section>
    <script>
      (function () {{
        var v = document.getElementById('finaleVideo');
        var ph = document.getElementById('videoPlaceholder');
        var shown = false;
        function show() {{ ph.classList.add('show'); v.removeAttribute('controls'); shown = true; }}
        v.querySelector('source').addEventListener('error', show);
        v.addEventListener('error', show);
        v.addEventListener('loadedmetadata', function () {{ ph.classList.remove('show'); v.setAttribute('controls', ''); }});
        setTimeout(function () {{ if (!shown && v.readyState === 0 && v.networkState === 3) show(); }}, 2000);
      }})();
    </script>"""
    out = page(title=f"Closing Video — {course['title']}", description=f"Closing video for {course['title']}.",
               root="../../", course=dict(course, _base=""), active="finale", body_attrs=course_attrs(course),
               main=main, scripts=["../../assets/js/course.js"])
    write(f"courses/{course['slug']}/finale.html", out)


def build_certificate(course):
    main = f"""
    <section class="content">
      <div id="certLocked" class="card panel" style="display:none;text-align:center">
        <h1>Certificate</h1>
        <p>Your certificate becomes available after you pass the final quiz with {course['pass_mark']} % or more.</p>
        <a class="btn primary" href="quiz.html">Go to the final quiz</a>
      </div>
      <div id="certReady" style="display:none">
        <div class="cert-form no-print">
          <label for="learnerName" class="muted" style="flex-basis:100%">Enter your full name as it should appear on the certificate:</label>
          <input id="learnerName" type="text" autocomplete="name" placeholder="Full name" maxlength="80" />
          <button class="btn primary" id="printCert" type="button">Print / Save as PDF</button>
        </div>
        <div class="cert">
          <img src="../../assets/img/logo.png" alt="Domestic Airlines" class="logo" />
          <div class="eyebrow">Domestic Airlines — Training</div>
          <h1>Certificate of Completion</h1>
          <p class="muted">This is to certify that</p>
          <div class="name" id="certName">&nbsp;</div>
          <p class="muted">has successfully completed the e-learning course</p>
          <div class="course">{esc(course['title'])}</div>
          <div class="row">
            <div><b id="certDate">—</b>Date of completion</div>
            <div><b id="certScore">—</b>Final quiz score</div>
            <div><b id="certId">—</b>Certificate reference</div>
          </div>
        </div>
        <p class="muted no-print" style="text-align:center;font-size:13.5px">This certificate records completion of self-paced training. Record it in your training file as the Operations Manual requires.</p>
      </div>
    </section>
    <script>
      (function () {{
        function ready(fn) {{ document.readyState !== 'loading' ? fn() : document.addEventListener('DOMContentLoaded', fn); }}
        ready(function () {{
          var api = window.DACourse; var st = api ? api.state() : {{}};
          var q = st.quiz;
          if (!q || !q.passed) {{ document.getElementById('certLocked').style.display = ''; return; }}
          document.getElementById('certReady').style.display = '';
          var d = new Date(q.date);
          document.getElementById('certDate').textContent = d.toLocaleDateString('en-GB', {{ day: 'numeric', month: 'long', year: 'numeric' }});
          document.getElementById('certScore').textContent = q.pct + ' %';
          var ref = '{course.get("cert_prefix", "DA")}-' + d.getFullYear() + String(d.getMonth() + 1).padStart(2, '0') + String(d.getDate()).padStart(2, '0') + '-' + String(d.getTime()).slice(-5);
          document.getElementById('certId').textContent = ref;
          var input = document.getElementById('learnerName');
          var out = document.getElementById('certName');
          input.value = st.name || '';
          function upd() {{ out.textContent = input.value.trim() || '\\u00a0'; }}
          upd();
          input.addEventListener('input', function () {{ upd(); api.saveName(input.value.trim()); }});
          document.getElementById('printCert').addEventListener('click', function () {{
            if (!input.value.trim()) {{ input.focus(); return; }}
            window.print();
          }});
        }});
      }})();
    </script>"""
    out = page(title=f"Certificate — {course['title']}", description=f"Certificate of completion for {course['title']}.",
               root="../../", course=dict(course, _base=""), active=None, body_attrs=course_attrs(course),
               main=main, scripts=["../../assets/js/course.js"])
    write(f"courses/{course['slug']}/certificate.html", out)


def build_media_readme(course):
    write(f"courses/{course['slug']}/media/README.md", f"""# Media for {course['title']}

## Lesson narration (optional)
Put one MP3 per lesson in `audio/`, named `lesson-01.mp3` … `lesson-{len(course['lessons']):02d}.mp3`.
When a file is present, the lesson page plays it. Otherwise the page reads the lesson aloud with the browser's text-to-speech voice.
Scripts for recording are in `../narration/`. To regenerate the neural-voice MP3s, use `tools/make_audio.py`.

## Closing video (optional)
Put the closing video at `video/finale.mp4` (H.264/AAC MP4 recommended, ideally under 50 MB).
""")


# --------------------------------------------------------------------------- utils

def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def validate(course):
    errs = []
    covered = sorted(n for m in course["modules"] for n in m["lessons"])
    if covered != list(range(1, len(course["lessons"]) + 1)):
        errs.append("modules do not cover every lesson exactly once")
    for i, L in enumerate(course["lessons"], 1):
        for k in ("title", "minutes", "objectives", "body", "takeaways", "check"):
            if k not in L:
                errs.append(f"lesson {i} missing {k}")
        c = L.get("check", {})
        if not 0 <= c.get("answer", -1) < len(c.get("options", [])):
            errs.append(f"lesson {i} knowledge check answer out of range")
    for i, q in enumerate(course["questions"], 1):
        if not 0 <= q["answer"] < len(q["options"]):
            errs.append(f"question {i} answer out of range")
        if not 1 <= q["lesson"] <= len(course["lessons"]):
            errs.append(f"question {i} lesson out of range")
    if len(course["questions"]) < course["quiz_count"]:
        errs.append("question bank smaller than quiz size")
    if errs:
        raise SystemExit(f"{course['slug']}: " + "; ".join(errs))


def main():
    build_portal()
    for c in COURSES:
        validate(c)
        c = dict(c, _base="")
        build_course_home(c)
        for n in range(1, len(c["lessons"]) + 1):
            build_lesson(c, n)
        build_quiz(c)
        if c.get("finale"):
            build_finale(c)
        build_certificate(c)
        build_media_readme(c)
        build_print(c, module_of, write)
        print(f"Built {c['title']}: {len(c['lessons'])} lessons, {len(c['questions'])} questions")


if __name__ == "__main__":
    main()
