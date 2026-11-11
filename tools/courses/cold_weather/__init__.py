"""Cold Weather Operations course definition."""
from .lessons_a import LESSONS_A
from .lessons_b import LESSONS_B
from .lessons_c import LESSONS_C
from .questions import QUESTIONS

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
)
