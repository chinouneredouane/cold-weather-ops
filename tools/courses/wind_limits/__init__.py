"""S3 — Company Wind Limitations (summer season), all fleets. Generic content: ICAO Annex 3 wind reporting,
wind component calculation, AFM demonstrated crosswind and tailwind limits, manufacturer crosswind guidance by
runway condition, and company limits. Actual values: OM B, FCOM / AOM, AFM."""
import math
from courses.upset_recovery.diagrams import FONT, INK, MUTED, GREEN, GREEN_D, RED, AMBER, BLUE, arrow_defs


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


def component_diagram():
    a = math.radians(30)
    L = 220
    wx, wy = 300 + L * math.sin(a), 280 - L * math.cos(a)
    svg = f"""{arrow_defs(11)}
<rect x="280" y="40" width="40" height="250" fill="#3b4540"/><path d="M300 60 L300 280" stroke="#fff" stroke-width="3" stroke-dasharray="14 10"/>
<text x="300" y="32" text-anchor="middle" font-weight="700">RWY 36</text>
<line x1="{wx:.0f}" y1="{wy:.0f}" x2="300" y2="280" stroke="{BLUE}" stroke-width="4" marker-end="url(#ar11)"/>
<text x="{wx+10:.0f}" y="{wy+6:.0f}" fill="{BLUE}" font-weight="700">wind 030° / 20 kt</text>
<line x1="255" y1="{wy:.0f}" x2="255" y2="280" stroke="{GREEN}" stroke-width="4" marker-end="url(#ar11)"/>
<text x="245" y="170" fill="{GREEN_D}" font-weight="700" text-anchor="end">headwind ≈ 17 kt</text>
<line x1="{wx:.0f}" y1="{wy:.0f}" x2="300" y2="{wy:.0f}" stroke="{AMBER}" stroke-width="4" marker-end="url(#ar11)"/>
<text x="{wx+10:.0f}" y="{wy-22:.0f}" fill="{AMBER}" font-weight="700">crosswind = 10 kt</text>
<g font-size="13"><text x="520" y="120" font-weight="700">Rule of thumb (crosswind)</text>
<text x="520" y="145">30° off the runway → ½ of the wind</text><text x="520" y="168">45° → about 0.7 of the wind</text>
<text x="520" y="191">60° → about 0.9 of the wind</text><text x="520" y="214">90° → all of the wind</text>
<text x="520" y="250" fill="{MUTED}">crosswind = wind × sin(angle)</text><text x="520" y="272" fill="{MUTED}">headwind = wind × cos(angle)</text></g>"""
    return f"""<figure class="diagram"><svg viewBox="0 0 800 300" role="img" aria-label="Wind components"><title>Headwind and crosswind components</title>
<desc>A 20 kt wind at 30 degrees to the runway gives about 17 kt of headwind and 10 kt of crosswind.</desc>
<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg>
<figcaption>Always use the gust value when checking a crosswind limit, unless the company procedure states otherwise.</figcaption></figure>"""


COMPANY = ('<div class="callout caution"><span class="label">Company limits</span><p>The actual Domestic Airlines wind limits for each fleet — '
           'crosswind by runway condition, tailwind, gusts, limits for the first officer as pilot flying and for low-visibility / autoland — are in the '
           '<strong>OM B</strong>, the <strong>FCOM / AOM</strong> and the <strong>AFM</strong>. Always use them; the figures in this course are examples only.</p></div>')

LESSONS = [
dict(title="Wind Reports and Wind Components", minutes=6,
objectives=["Interpret wind reports correctly.", "Calculate headwind, tailwind and crosswind components.", "Use gusts correctly."],
body="""
<h2>Wind reports</h2>
<ul>
  <li>In the <strong>METAR</strong>, the wind is a 10-minute mean; in reports for <strong>take-off and landing</strong> from the tower (and ATIS), it is a 2-minute mean for the runway (ICAO Annex 3).</li>
  <li><strong>Gusts</strong> are reported when the maximum wind exceeds the mean by 10 kt or more: <code>27015G28KT</code> = 270°, 15 kt, gusting 28 kt.</li>
  <li>Variable direction: <code>27015KT 240V300</code> — direction varies between 240° and 300°.</li>
  <li>Directions in METAR / TAF are <strong>true</strong>; tower and ATIS winds are <strong>magnetic</strong>.</li>
</ul>

<h2>Components</h2>
""" + component_diagram() + """
<ul>
  <li>Use the FMS / EFB, the wind component chart or the rule of thumb.</li>
  <li>For limits, check the crosswind with the <strong>gust</strong> and the tailwind with the steady wind and the gust as your procedure states.</li>
  <li>With a variable wind direction, use the most unfavourable direction.</li>
</ul>
""",
takeaways=["METAR wind: 10-min mean, true; tower / ATIS: 2-min mean, magnetic.", "Gusts reported when 10 kt or more above the mean.", "Crosswind ≈ wind × sin(angle); use the gust for crosswind limits."],
check=dict(q="Wind 090°/20 kt on runway 06. Approximately what is the crosswind?", options=["5 kt", "10 kt", "17 kt", "20 kt"], answer=1, explain="30° off the runway: half the wind, about 10 kt."),
),

dict(title="Aircraft Wind Limitations", minutes=6,
objectives=["Distinguish demonstrated crosswind from a limitation.", "Apply tailwind limits.", "Use the manufacturer's crosswind guidance by runway condition."],
body="""
<h2>Demonstrated crosswind</h2>
<p>The AFM states the <strong>maximum demonstrated crosswind</strong> — the highest crosswind tested during certification. Unless the AFM says it is a limitation, it is <strong>not</strong> a structural or legal limit — but the company normally turns it, or a lower value, into an operational limit in the OM B.</p>

<h2>Tailwind</h2>
<p>The AFM gives a <strong>maximum tailwind</strong> for take-off and landing (commonly 10 kt; some aircraft are approved for more with specific conditions). This <strong>is</strong> a limitation. Performance must also be calculated with the reported tailwind.</p>

<h2>Crosswind and runway condition</h2>
<ul>
  <li>Manufacturers publish recommended maximum crosswinds that <strong>decrease as the runway condition worsens</strong> — by runway condition code (RWYCC) or braking action.</li>
  <li>On a contaminated runway, use the crosswind for the reported RWYCC (see the Cold Weather Operations course).</li>
</ul>

<h2>Other wind-related limits</h2>
<ul>
  <li><strong>Autoland and low-visibility operations</strong> have their own headwind, tailwind and crosswind limits.</li>
  <li>Doors: maximum wind for opening or closing passenger and cargo doors.</li>
  <li>Engine start in strong tailwind or crosswind (especially for some engines and propellers).</li>
</ul>
""" + COMPANY,
takeaways=["Demonstrated crosswind: tested, not normally a limitation — but the company may make it one.", "Tailwind limit in the AFM is a limitation.", "Crosswind limits reduce with the runway condition; autoland has its own limits."],
check=dict(q="The AFM maximum demonstrated crosswind is:", options=["Always a structural limit", "The highest crosswind tested in certification — not a limitation unless the AFM says so", "The same as the tailwind limit", "Only for take-off"], answer=1, explain="It is a demonstrated value, not a limitation unless stated."),
),

dict(title="Company Limits and Crew Application", minutes=6,
objectives=["Apply company wind limits for each fleet and crew situation.", "Use speed additives and technique for wind.", "Decide when the wind does not allow take-off or landing."],
body="""
<h2>Company limits</h2>
<p>The OM B normally defines, for each fleet:</p>
<ul>
  <li>maximum crosswind for take-off and landing — dry, wet and by RWYCC — including gusts;</li>
  <li>maximum tailwind;</li>
  <li>more restrictive limits when the <strong>first officer is pilot flying</strong> or for crews with limited experience on type;</li>
  <li>limits for low-visibility operations and autoland;</li>
  <li>possible restrictions at specific aerodromes (OM C).</li>
</ul>

<h2>Application</h2>
<ol class="steps">
  <li>Get the latest wind (ATIS / tower) and the runway condition.</li>
  <li>Calculate the components with the gust; check the most restrictive limit that applies (aircraft, company, crew, runway condition, LVO).</li>
  <li>Apply the approach speed wind additive defined in your FCOM / AOM.</li>
  <li>Brief the crosswind technique and the go-around if the limits are exceeded on short final.</li>
</ol>
<div class="callout warn"><span class="label">Decision</span><p>If the wind exceeds a limit, do not take off or land — wait, use another runway or divert. Wind limits are not targets.</p></div>
""" + COMPANY,
takeaways=["Use the most restrictive limit: aircraft, company, crew, runway condition, LVO, aerodrome.", "Calculate with the gust; apply the FCOM / AOM speed additive.", "Above a limit: wait, change runway or divert."],
check=dict(q="Which crosswind limit applies when the first officer is pilot flying on a wet runway?", options=["Always the AFM demonstrated value", "The most restrictive applicable limit in the OM B", "The tailwind limit", "No limit"], answer=1, explain="Apply the most restrictive company limit that applies to the situation."),
),
]

QUESTIONS = [
Q(1, "The wind in a METAR is a mean over:", ["1 minute", "2 minutes", "10 minutes", "1 hour"], 2, "METAR wind: 10-minute mean."),
Q(1, "Wind given by the tower for landing is a mean over:", ["2 minutes", "10 minutes", "30 seconds", "1 hour"], 0, "Take-off and landing reports: 2-minute mean."),
Q(1, "A gust is reported when the maximum exceeds the mean by:", ["5 kt", "10 kt or more", "15 kt", "20 kt"], 1, "10 kt or more."),
Q(1, "Wind 30° off the runway gives a crosswind of about:", ["Half the wind", "The full wind", "A quarter", "None"], 0, "sin 30° = 0.5."),
Q(1, "METAR wind direction is referenced to:", ["Magnetic north", "True north", "The runway", "Grid north"], 1, "METAR / TAF directions are true."),
Q(2, "The AFM tailwind limit is:", ["A recommendation", "A limitation", "Only for take-off", "Not published"], 1, "Tailwind limits are limitations."),
Q(2, "As the runway condition worsens, recommended crosswind limits:", ["Increase", "Decrease", "Stay the same", "Disappear"], 1, "Crosswind limits reduce with worse runway condition."),
Q(2, "Do autoland operations have their own wind limits?", ["No", "Yes", "Only crosswind", "Only on wet runways"], 1, "Autoland has specific wind limits."),
Q(3, "When checking a crosswind limit, which wind value should normally be used?", ["The lowest reported", "Including the gust", "The METAR mean only", "The forecast"], 1, "Include the gust."),
Q(3, "On short final the reported crosswind exceeds the company limit. What do you do?", ["Land carefully", "Go around", "Increase speed and land", "Use more flaps"], 1, "Go around — limits are not targets."),
]

COURSE = dict(
    slug="wind-limitations", title="Wind Limitations", header_title="Wind Limitations",
    tagline="Wind reports and components, AFM demonstrated crosswind and tailwind limits, crosswind by runway condition, and how to apply company limits.",
    purpose="Refresh all flight crews' knowledge of wind reports and wind limitations, and of the application of the company limits in the OM B, FCOM / AOM and AFM.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Interpret wind reports and calculate components", "Distinguish demonstrated crosswind from limitations", "Apply crosswind limits by runway condition", "Apply the most restrictive company limit and decide"],
    icon="runway", cert_prefix="WND", quiz_count=10, pass_mark=80, group="refresher", season="Summer", finale=None,
    modules=[dict(title="Wind and Limitations", summary="Reports, components, aircraft and company limits", icon="runway", lessons=range(1, 4))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner approaching a runway in a crosswind", "Calculate the components with the gust."),
            2: ("gen", "Airliner landing on a wet runway", "Crosswind limits decrease as the runway condition worsens."),
            3: ("gen", "Two pilots briefing the approach", "Use the most restrictive limit that applies.")},
)
