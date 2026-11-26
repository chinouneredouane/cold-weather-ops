"""Shared helpers for the aircraft performance courses (B737-800 NG, Dash 8-Q400, Dash 8-Q200)."""


def fig(img, caption, src):
    """A picture from the course material in media/images/<img>.jpg."""
    return (f'<figure class="lesson-figure"><img src="../media/images/{img}.jpg" alt="{caption}" loading="lazy">'
            f'<figcaption>{caption} <span class="muted">Source: {src}.</span></figcaption></figure>')


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


REGS = ("EASA CS-25 (CS 25.101–25.125, 25.149), Part-CAT Subpart C Section 1 (CAT.POL.A.200–A.240), AMC 25-13 "
        "(reduced and derated take-off thrust), ICAO Annex 6 Part I and Annex 14")
