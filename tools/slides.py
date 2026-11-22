"""How a lesson is cut into slides — shared by the page builder (build.py), the narration recorder (make_audio.py)
and the cue tool (make_cues.py), so that the slides on screen and the narration always match.

Rules:
- slide 1: learning objectives (+ any text before the first section heading);
- one slide per <h2> section;
- a section that contains pictures is cut so that EACH PICTURE HAS ITS OWN SLIDE, together with the text that leads to it;
  text after the last picture becomes its own slide;
- then key takeaways, then the knowledge check (no narration).
"""
import re

FIG = re.compile(r"<figure\b.*?</figure>", re.S)


def _has_text(html):
    return len(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()) > 30


def split_section(title, html):
    """Return [(title, html)] for one <h2> section: each picture with the text leading to it; text after the
    last picture becomes a slide of its own, so no slide holds more than one picture or overflows the screen."""
    figs = list(FIG.finditer(html))
    if not figs:
        return [(title, f"<h2>{title}</h2>{html}")]
    out, start = [], 0
    def add(part):
        t = title if not out else f"{title} ({len(out) + 1})"
        out.append((t, f"<h2>{t}</h2>{part}"))
    for m in figs:
        before = html[start:m.start()]
        if "<table" in before and _has_text(before):      # a table and a picture do not fit together: two slides
            add(before)
            add(m.group(0))
        else:
            add(html[start:m.end()])
        start = m.end()
    rest = html[start:]
    if _has_text(rest):
        add(rest)
    elif rest.strip():
        t, h = out[-1]
        out[-1] = (t, h + rest)
    return out


def body_slides(body):
    """(intro_html, [(title, html), ...]) for the lesson body."""
    parts = re.split(r"<h2>(.*?)</h2>", body)
    intro = parts[0].strip()
    slides = []
    for k in range(1, len(parts), 2):
        for t, h in split_section(parts[k], parts[k + 1]):
            slides.append((re.sub(r"<[^>]+>", "", t), h))
    return intro, slides


def caption_speech(fig_html):
    """Text the narrator reads for a picture: its caption without the source credit."""
    m = re.search(r"<figcaption>(.*?)</figcaption>", fig_html, re.S)
    if not m:
        return ""
    cap = re.sub(r'<span class="muted">\s*Source:.*?</span>', "", m.group(1), flags=re.S)
    cap = re.sub(r"Source:.*$", "", re.sub(r"<[^>]+>", " ", cap), flags=re.S).strip()
    return f"<p>In the figure: {cap}</p>" if cap else ""
