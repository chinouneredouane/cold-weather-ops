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
