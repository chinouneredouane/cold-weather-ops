"""Cold Weather Operations course definition."""
from .lessons_a import LESSONS_A
from .lessons_b import LESSONS_B
from .lessons_c import LESSONS_C
from .questions import QUESTIONS
from .images import IMAGES

COURSE = dict(
    slug="cold-weather-operations",
    title="Cold Weather Operations",
    header_title="Cold Weather Operations",  # shown in the header after "DOMESTIC AIRLINES —"
    tagline="Aircraft ground operations in cold weather: contamination, de-icing and anti-icing, "
            "holdover times and performance on contaminated runways.",
    purpose="Provide Domestic Airlines crews with an understanding of aircraft ground operations in cold "
            "weather conditions, and address aircraft contamination, de-icing and anti-icing, and "
            "performance on contaminated runways.",
    audience="Flight crew (primary). Also suitable for cabin crew, flight dispatchers and ground operations staff.",
    icon="snow",
    cert_prefix="CWO",
    objectives=[
        "Identify contamination and icing hazards and their effect on performance",
        "Apply the Clean Aircraft Concept and the ground de-icing/anti-icing programme",
        "Use holdover time guidelines and pre-take-off checks correctly",
        "Interpret runway condition reports and assess contaminated runway performance",
        "Operate aircraft systems safely after cold soak and in icing conditions",
        "Apply cold temperature altimeter corrections",
        "Use CRM and TEM to resist time pressure in winter operations",
    ],
    finale=dict(
        title="Closing Case Study: Air Ontario Flight 1363",
        intro="Thank you for completing the Cold Weather Operations course. This closing video revisits the 1989 Dryden accident "
              "step by step, links each link in the accident chain to the lessons you have studied, and ends with three questions "
              "to discuss with your crew or instructor. Duration: about 6 minutes.",
        further=[
            ("FAA Lessons Learned — Air Ontario Flight 1363 (C-FONF)", "https://www.faa.gov/lessons_learned/transport_airplane/accidents/C-FONF"),
            ("Government of Canada — Final response to the Commission of Inquiry into the Air Ontario Crash at Dryden", "https://publications.gc.ca/site/eng/9.896149/publication.html"),
            ("NASA — A Pilot's Guide to Ground Icing (interactive course)", "https://aircrafticing.grc.nasa.gov/2_5_2_1.html"),
        ],
    ),
    finale_youtube="",  # e.g. "dQw4w9WgXcQ" — the ID from a YouTube link; leave empty to use media/video/finale.mp4
    quiz_count=20,
    pass_mark=80,
    modules=[
        dict(title="Foundations", summary="Weather, contaminants, icing and the Clean Aircraft Concept", icon="snow", lessons=range(1, 6)),
        dict(title="De-icing and Anti-icing", summary="Methods, fluids, holdover times, preparation and communication", icon="drop", lessons=range(6, 12)),
        dict(title="Inspections", summary="Clear ice, post-treatment checks and pre-take-off checks", icon="search", lessons=range(12, 14)),
        dict(title="Runways and Performance", summary="Contaminated runways, GRF reporting, take-off, landing and taxi", icon="runway", lessons=range(14, 19)),
        dict(title="Aircraft Systems in the Cold", summary="Cold soak, engines, systems, fuel, flight controls and in-flight icing", icon="gear", lessons=range(19, 24)),
        dict(title="Operations and Human Factors", summary="Altimetry, dispatch, cabin, CRM, emergencies, regulation and accident lessons", icon="people", lessons=range(24, 31)),
    ],
    lessons=LESSONS_A + LESSONS_B + LESSONS_C,
    questions=QUESTIONS,
    images=IMAGES,
)


# ---------------------------------------------------------------------------------------------------------------
# Real pictures (public domain, US Federal Aviation Administration). Each picture is placed after the first paragraph
# (or list) of the named section, so the picture slide holds the text that introduces it.
_WX = "FAA Aviation Weather Handbook FAA-H-8083-28B"
_PHAK = "FAA Pilot's Handbook of Aeronautical Knowledge FAA-H-8083-25C"
_AC = "FAA Advisory Circular AC 91-74B, Pilot Guide: Flight in Icing Conditions"
FAA_FIGS = {
    2: [("Precipitation types that matter", "faa-icing-fronts", "Icing with fronts: supercooled droplets above the frontal surface; freezing rain and ice pellets fall into the cold air below.", f"{_WX}, Figure 20-1"),
        ("Temperature inversions", "faa-warm-front", "A warm front: warm air rises over cold air. Rain falling from the warm layer into sub-zero air becomes freezing rain.", f"{_AC}, Figure 2-1")],
    4: [("In-flight icing", "faa-ice-types", "The forms of structural icing: clear ice, clear ice with horns, rime ice and mixed ice.", f"{_AC}, Figures 3-1 to 3-4"),
        ("In-flight icing", "faa-inflight-ice", "In-flight ice formation on a leading edge.", f"{_PHAK}, Figure 5-40"),
        ("In-flight icing", "faa-icing-mountains", "Icing with mountains: upslope lift on the windward side gives the most severe icing zone above the ridge.", f"{_WX}, Figure 20-2")],
    5: [("What contamination does", "faa-ice-lift-drag", "Ice on the wing: maximum lift falls and the wing stalls at a lower angle of attack, while drag rises sharply.", f"{_AC}, Figures 3-5 and 3-6")],
    20: [("Turboprops and propellers", "faa-propeller-ice-sld", "Propeller ice accretion during a supercooled large droplet (SLD) encounter.", f"{_AC}, Figure 3-10")],
    23: [("Ice protection systems", "faa-wing-boot", "Pneumatic de-icing boots (as on the Dash 8): tubes deflated in normal flight, inflated to crack off the ice.", f"{_AC}, Figure 3-7"),
         ("Tailplane icing", "faa-tailplane-stall", "Tailplane stall: the tail down-force balances the nose-down moment; if the iced tailplane stalls, the nose pitches down.", f"{_AC}, Figures 3-8 and 3-9")],
    24: [("Why cold air is dangerous for terrain clearance", "faa-cold-altimeter", "In air colder than standard, the aircraft is lower than the altimeter indicates.", f"{_PHAK}, Figure 8-3")],
}


def _faa_figure(img, caption, src):
    return (f'<figure class="lesson-figure"><img src="../media/images/{img}.jpg" alt="{caption}" loading="lazy">'
            f'<figcaption>{caption} <span class="muted">Source: {src} (public domain).</span></figcaption></figure>')


def _insert_after_first_block(body, h2, html):
    import re as _re
    tag = f"<h2>{h2}</h2>"
    assert tag in body, h2
    i = body.index(tag) + len(tag)
    nxt = body.find("<h2>", i)
    nxt = len(body) if nxt < 0 else nxt
    # end of the first top-level block after the heading (tags nested inside it are skipped)
    at, depth = nxt, 0
    for m in _re.finditer(r"<(/?)(p|ul|ol|div|table|figure)\b[^>]*>", body[i:nxt]):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            at = i + m.end()
            break
    return body[:at] + "\n" + html + "\n" + body[at:]


for _n, _figs in FAA_FIGS.items():
    _b = COURSE["lessons"][_n - 1]["body"]
    _done = {}
    for _h2, _img, _cap, _src in _figs:
        # several pictures in one section: each goes after the previous one
        if _h2 in _done:
            _at = _b.index(_done[_h2]) + len(_done[_h2])
            _html = _faa_figure(_img, _cap, _src)
            _b = _b[:_at] + "\n" + _html + _b[_at:]
            _done[_h2] = _html
        else:
            _html = _faa_figure(_img, _cap, _src)
            _b = _insert_after_first_block(_b, _h2, _html)
            _done[_h2] = _html
    COURSE["lessons"][_n - 1]["body"] = _b
