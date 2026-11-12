"""W1 — Windshear Recovery and Thunderstorm Avoidance (winter season), all fleets.
Built on ICAO Doc 9817 (Manual on Low-level Wind Shear), ICAO Annex 6 / Annex 3, EASA ORO.FC.230 recurrent
training, and industry windshear training guidance. Type escape procedures come from the QRH/AOM."""
from courses.upset_recovery.diagrams import FONT, INK, MUTED, GREEN, GREEN_D, RED, AMBER, BLUE, windshear


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


def radar_diagram():
    svg = f"""
<path d="M350 300 L60 60 A380 380 0 0 1 640 60 Z" fill="#0c1a12"/>
<g fill="none" stroke="#2f5a3e"><path d="M350 300 L60 60"/><path d="M350 300 L640 60"/><path d="M200 177 A190 190 0 0 1 500 177"/><path d="M130 120 A285 285 0 0 1 570 120"/></g>
<ellipse cx="440" cy="130" rx="70" ry="42" fill="#2fb34a"/><ellipse cx="440" cy="132" rx="45" ry="26" fill="#e6c229"/><ellipse cx="445" cy="134" rx="22" ry="13" fill="#d6342c"/>
<path d="M500 110 Q560 95 600 130" stroke="#d6342c" stroke-width="4" fill="none"/>
<ellipse cx="230" cy="150" rx="55" ry="25" fill="#2fb34a" opacity=".9"/>
<path d="M350 300 L330 70" stroke="#fff" stroke-width="3" stroke-dasharray="8 6"/>
<polygon points="350,300 340,282 360,282" fill="#fff"/>
<text x="470" y="200" fill="#fff" font-size="13">avoid by at least 20 NM</text><text x="470" y="216" fill="#fff" font-size="13">(more downwind of the cell)</text>
<text x="40" y="330" fill="{INK}" font-weight="700">Green → yellow → red: increasing reflectivity. A steep gradient or a “hook” suggests severe turbulence and hail.</text>"""
    return f"""<figure class="diagram"><svg viewBox="0 0 700 345" role="img" aria-label="Weather radar picture"><title>Weather radar: avoiding a cell</title>
<desc>A weather radar display with a strong red cell; the planned track deviates upwind, more than 20 NM from the cell.</desc>
<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg>
<figcaption>Illustrative radar picture. Deviate early, preferably upwind, and remember that radar does not show turbulence in clear air or dry hail outside the cell.</figcaption></figure>"""


LESSONS = [
dict(title="Windshear: Definition, Sources and Effects", minutes=7,
objectives=["Define windshear and microburst.", "Identify the weather situations that produce low-level windshear.", "Explain the effect of windshear on aircraft performance."],
body="""
<h2>Definition</h2>
<p><strong>Windshear</strong> is a change of wind speed and/or direction over a short distance, horizontally or vertically. <strong>Low-level windshear</strong> — below about 1,600 ft above ground — is the most dangerous, because it occurs during take-off and approach, when the aircraft is slow, close to the ground and has little energy margin (ICAO Doc 9817).</p>

<h2>Sources</h2>
<ul>
  <li><strong>Thunderstorms and convective clouds</strong> — downbursts and microbursts, gust fronts and outflow, which can extend well away from the cell.</li>
  <li><strong>Frontal systems</strong> — especially fast-moving cold fronts with strong temperature contrasts.</li>
  <li><strong>Low-level jet streams and temperature inversions</strong> — wind changing sharply in speed or direction across the inversion layer.</li>
  <li><strong>Terrain and obstacles</strong> — strong winds over hills, buildings or hangars near the runway, and sea breezes.</li>
</ul>

<h2>The microburst</h2>
""" + windshear() + """
<p>A <strong>microburst</strong> is a small, intense downdraft — typically less than about 4 km across — that spreads out on reaching the ground. It usually lasts only a few minutes. An aircraft entering it first meets an increasing headwind (performance increase), then a strong downdraft, then a tailwind (performance decrease). The pilot's natural reaction to the first phase — reducing thrust and pitch — leaves the aircraft badly placed for the dangerous second and third phases.</p>

<h2>Effects</h2>
<ul>
  <li>An increasing headwind or decreasing tailwind raises indicated airspeed and lift — the aircraft tends to rise above the path.</li>
  <li>A decreasing headwind or increasing tailwind reduces indicated airspeed and lift — the aircraft sinks below the path.</li>
  <li>A downdraft directly increases the descent rate.</li>
  <li>The combination can exceed the aircraft's climb performance close to the ground.</li>
</ul>
""",
takeaways=["Windshear: change of wind speed or direction over a short distance; most dangerous below about 1,600 ft.", "Sources: convection (microbursts), fronts, inversions and low-level jets, terrain.", "Microburst: headwind gain, then downdraft, then tailwind loss — do not react to the first phase by reducing energy."],
check=dict(q="Entering a microburst on approach, what is usually encountered first?", options=["A tailwind", "An increasing headwind and a performance increase", "A strong downdraft", "No change"], answer=1,
           explain="The first phase is an increasing headwind that raises airspeed and lift — followed by downdraft and tailwind."),
),

dict(title="Avoidance and Recognition", minutes=7,
objectives=["Use weather reports and alerts to avoid windshear.", "Recognise the cues of a windshear encounter.", "Understand predictive and reactive windshear systems."],
body="""
<h2>Avoid — the best defence</h2>
<ul>
  <li>Use the METAR, TAF, SIGMET, ATIS and pilot reports: <code>TS</code>, <code>+TSRA</code>, <code>CB</code>, gusts, <code>WS</code> groups in METARs (e.g. <code>WS R26</code>) and low-level windshear alerts.</li>
  <li>Watch for visual signs: virga, rain shafts, dust rings on the ground, roll clouds and rapidly changing wind socks.</li>
  <li>Delay the take-off or approach when severe windshear or a microburst is reported or forecast, or when a strong thunderstorm is over or near the aerodrome. Hold or divert.</li>
  <li>If windshear is possible: use the maximum take-off thrust or the take-off settings recommended by your FCOM/AOM, consider the longest suitable runway, and brief the escape manoeuvre.</li>
</ul>

<h2>Recognise</h2>
<ul>
  <li>Unexpected <strong>airspeed changes</strong> — typically more than about 15 kt.</li>
  <li><strong>Vertical speed</strong> deviations — for example 500 ft/min or more from normal.</li>
  <li>Pitch attitude changes and deviations from the glide path.</li>
  <li>Unusual thrust lever positions needed to hold the speed.</li>
  <li>Aural and visual windshear warnings.</li>
</ul>

<h2>Windshear systems</h2>
<ul>
  <li><strong>Predictive windshear</strong> (weather radar based, where fitted) looks ahead and alerts before the aircraft enters the windshear — “WINDSHEAR AHEAD” cautions and warnings, depending on the system.</li>
  <li><strong>Reactive windshear</strong> (EGPWS or flight control computer based, where fitted) alerts when the aircraft is already in windshear — “WINDSHEAR, WINDSHEAR, WINDSHEAR”.</li>
  <li>Know which systems your aircraft has and how they are inhibited during certain phases.</li>
</ul>
<div class="callout"><span class="label">Fleet note</span><p>The available windshear warnings differ between the B737-800, the Q400 and the Q200. Check the FCOM / AOM for your aircraft.</p></div>
""",
takeaways=["Avoid first: reports, radar, visual signs; delay or divert.", "Cues: speed changes over about 15 kt, vertical speed deviations of about 500 ft/min, unusual thrust.", "Predictive warns before entry; reactive warns when inside."],
check=dict(q="What is the most effective defence against microburst windshear?", options=["High approach speed", "Avoidance — delay the take-off or approach", "Flaps up landing", "Autopilot off"], answer=1, explain="Avoidance is the most effective defence."),
),

dict(title="The Windshear Escape Manoeuvre", minutes=7,
objectives=["Apply the generic windshear escape principles.", "Explain why configuration must not be changed.", "Recover and report after the encounter."],
body="""
<h2>When to act</h2>
<p>Apply the escape manoeuvre immediately on a windshear warning, or when unacceptable flight path deviations occur — on take-off, initial climb or approach. Do not attempt to land if windshear is encountered on approach.</p>

<h2>Generic escape principles</h2>
<ol class="steps">
  <li><strong>Maximum thrust / power</strong> — go-around or maximum take-off thrust, as your procedure states. Thrust levers may be pushed to the limit if ground contact is imminent, as the type procedure allows.</li>
  <li><strong>Autopilot</strong> — as your procedure states (some types allow the autopilot or the flight director to fly the windshear guidance).</li>
  <li><strong>Wings level, pitch up</strong> to the windshear pitch target or flight director guidance; if needed, increase pitch up to the stick shaker or pitch limit indicator — <strong>respect the stall warning</strong>.</li>
  <li><strong>Do not change the configuration</strong> — no flap or gear changes until clear of the windshear. Retract speedbrakes.</li>
  <li><strong>The pilot monitoring</strong> calls out vertical speed, radio altitude and the trend.</li>
  <li>When clear of windshear: recover to a normal climb, speed and configuration, and <strong>report</strong> to ATC.</li>
</ol>
<div class="callout warn"><span class="label">Type procedure</span><p>The exact escape manoeuvre is a memory item for each fleet: B737-800 QRH Non-Normal Manoeuvres — Windshear Escape; Q400 and Q200 AOM / QRH windshear procedure. This course gives the principles; your manuals give the procedure.</p></div>

<h2>Why no configuration change</h2>
<p>Retracting flaps or gear during the escape reduces lift or adds drag at the worst moment. Gear retraction on some types temporarily increases drag as the doors open. The aircraft stays in its configuration until clear of the windshear.</p>

<h2>Reporting</h2>
<p>Report the windshear to ATC as soon as possible, with location, altitude and the speed gain or loss (e.g. “windshear on final runway 26, loss of 20 kt at 500 ft”). Your report protects the aircraft behind you. File the company report.</p>
""",
takeaways=["Warning or unacceptable deviation: escape immediately; never continue to land.", "Maximum thrust, wings level, pitch to the target / FD, respect the stall warning.", "No configuration change until clear; PM calls vertical speed and radio altitude.", "Report to ATC with location and speed change."],
check=dict(q="During a windshear escape, what should be done with flaps and gear?", options=["Retract both", "Do not change the configuration until clear of the windshear", "Extend more flaps", "Retract gear only"], answer=1, explain="No configuration change until clear of the windshear."),
),

dict(title="Thunderstorm Avoidance and Weather Radar", minutes=8,
objectives=["Plan thunderstorm avoidance on the ground and in flight.", "Use the weather radar correctly.", "Apply the avoidance distances and rules."],
body="""
<h2>Thunderstorm hazards</h2>
<p>Thunderstorms combine severe turbulence, windshear and microbursts, hail, lightning, icing, heavy rain and low visibility. Hazards extend outside the visible cloud and outside the radar echo.</p>

<h2>Weather radar</h2>
""" + radar_diagram() + """
<ul>
  <li><strong>Tilt</strong>: adjust tilt continuously so that the beam scans the storm's most reflective (wet) part; too high and the cell disappears, too low and ground returns hide it.</li>
  <li><strong>Gain</strong>: use the calibrated (preset) gain for cell assessment; manual gain only for analysis.</li>
  <li><strong>Range</strong>: use a long range for strategic planning and a shorter range for tactical avoidance.</li>
  <li><strong>Attenuation</strong>: heavy rain absorbs the beam — the area behind a strong cell may look clear when it is not (“radar shadow”).</li>
  <li>Dry hail, ice crystals and the upper part of a cell reflect weakly — a weak echo at high altitude can still be dangerous.</li>
</ul>

<h2>Avoidance rules (typical guidance)</h2>
<ul>
  <li>Avoid severe echoes by at least <strong>20 NM</strong>, and more on the downwind side and at high altitude.</li>
  <li>Deviate <strong>upwind</strong> where possible; decide early and ask ATC in good time.</li>
  <li>Do not fly <strong>under the anvil</strong> (hail) or between closely spaced cells less than about 40 NM apart.</li>
  <li>Do not attempt to climb over a fast-growing cell.</li>
  <li>On the ground: do not take off or land into a thunderstorm; consider the gust front and its windshear.</li>
</ul>

<h2>If turbulence cannot be avoided</h2>
<ul>
  <li>Fasten seat belts — passengers and crew — and secure the cabin.</li>
  <li>Fly the turbulence penetration speed for your type; keep wings level and hold the <strong>attitude</strong>, not the altitude; avoid large control inputs.</li>
  <li>Use the autopilot as your procedure recommends; engine anti-ice / ignition as required.</li>
</ul>
""",
takeaways=["Thunderstorm hazards extend beyond the cloud and the radar echo.", "Manage tilt, gain and range; beware of attenuation (radar shadow).", "At least 20 NM from severe echoes, upwind, never under the anvil or between close cells.", "In turbulence: seat belts, penetration speed, hold attitude."],
check=dict(q="Why can the area behind a strong radar echo be dangerous even if it looks clear?", options=["The radar is switched off there", "Heavy rain attenuates the beam, creating a radar shadow", "There is no weather behind storms", "Ground returns"], answer=1, explain="Attenuation by heavy rain can hide weather behind a strong cell."),
),

dict(title="Planning, CRM and Lessons Learned", minutes=6,
objectives=["Integrate windshear and thunderstorm threats into planning and briefings.", "Apply decision points and CRM.", "Learn from a classic windshear accident."],
body="""
<h2>Planning and briefing</h2>
<ul>
  <li>Brief convective weather on the route and at destination, alternates, extra fuel for deviations and holding.</li>
  <li>Before take-off or approach in convective weather: brief the windshear escape, the go-around and the decision points (“if windshear is reported on final, we hold / divert”).</li>
  <li>Agree on the callouts for speed and vertical speed deviations.</li>
</ul>

<h2>CRM</h2>
<ul>
  <li>Plan continuation bias is a strong factor in convective weather — “the aircraft ahead landed”. Each aircraft meets a different part of the storm.</li>
  <li>Either pilot can call for the escape manoeuvre; the PF executes immediately.</li>
  <li>Use ATC and other crews' reports, and give your own.</li>
</ul>

<h2>Lesson learned — Delta Air Lines 191 (Dallas/Fort Worth, August 1985)</h2>
<p>A Lockheed L-1011 on approach flew into a microburst from a thunderstorm close to the runway. The aircraft lost airspeed and height and struck the ground short of the runway; 137 people died. The investigation led directly to windshear training programmes and to the development of airborne windshear detection systems.</p>
<div class="callout"><span class="label">Key message</span><p>Do not penetrate a thunderstorm or approach through one. Waiting 20 minutes for a storm to pass costs fuel — never safety.</p></div>
""",
takeaways=["Brief convective threats, the escape manoeuvre and decision points.", "Beware of plan continuation — each aircraft meets a different storm.", "Delta 191 (1985) shaped modern windshear training and detection systems."],
check=dict(q="An aircraft ahead landed without problems in a thunderstorm area. What does this mean for you?", options=["It is safe to land", "Nothing — conditions in a storm change within minutes; apply your decision points", "You should land faster", "You may ignore windshear warnings"], answer=1, explain="Each aircraft meets a different part of a rapidly changing storm."),
),
]

QUESTIONS = [
Q(1, "Low-level windshear is generally considered below about:", ["500 ft", "1,600 ft", "5,000 ft", "10,000 ft"], 1, "Low-level windshear: below about 1,600 ft above ground."),
Q(1, "What is a microburst?", ["A large frontal system", "A small, intense downdraft that spreads out at the ground", "A mountain wave", "A jet stream"], 1, "Microbursts are small, intense, short-lived downdrafts."),
Q(1, "An increasing tailwind on approach causes:", ["A speed increase", "A speed and lift loss — the aircraft sinks below the path", "No change", "A climb"], 1, "Tailwind increase lowers indicated airspeed and lift."),
Q(1, "Which ICAO manual covers low-level windshear?", ["Doc 9817", "Doc 9574", "Doc 9613", "Doc 4444"], 0, "Doc 9817 is the Manual on Low-level Wind Shear."),
Q(2, "Which is a typical windshear recognition cue?", ["Unexpected airspeed changes of more than about 15 kt", "A 2 kt speed change", "Normal thrust settings", "Smooth air"], 0, "Unexpected speed changes over about 15 kt indicate windshear."),
Q(2, "What does a predictive windshear system do?", ["Warns after entering windshear", "Looks ahead and warns before entering windshear", "Records windshear for maintenance", "Controls the thrust"], 1, "Predictive systems look ahead."),
Q(2, "Severe windshear is reported on final. What is the best action?", ["Land quickly", "Delay the approach — hold or divert", "Land with flaps up", "Reduce speed"], 1, "Avoid: delay or divert."),
Q(3, "On a windshear warning during approach, you should:", ["Continue to land", "Apply the windshear escape manoeuvre immediately", "Extend more flaps", "Reduce thrust"], 1, "Escape immediately; do not attempt to land."),
Q(3, "During the escape, how far may pitch be increased?", ["Beyond the stall warning", "Up to the stick shaker / pitch limit, respecting the stall warning", "Never above 5°", "Only to the horizon"], 1, "Pitch up to the target, and up to the stall warning if needed."),
Q(3, "Who calls vertical speed and radio altitude during the escape?", ["ATC", "The pilot monitoring", "Cabin crew", "Nobody"], 1, "The PM calls the trend."),
Q(4, "Why must radar tilt be adjusted continuously?", ["To save power", "To scan the most reflective part of the storm and avoid ground returns", "To heat the antenna", "It does not need adjustment"], 1, "Correct tilt shows the storm's reflective core."),
Q(4, "Typical minimum avoidance distance from severe echoes:", ["5 NM", "10 NM", "20 NM", "50 NM"], 2, "At least 20 NM, more downwind and at altitude."),
Q(4, "Why should you never fly under the anvil?", ["It is cold", "Risk of hail", "Radio interference", "Icing only"], 1, "Hail falls from the anvil."),
Q(4, "In severe turbulence, what should be held?", ["Altitude exactly", "Attitude, at the turbulence penetration speed", "Maximum speed", "Minimum speed"], 1, "Hold attitude, not altitude."),
Q(5, "Which accident led directly to modern windshear training and detection?", ["Delta 191, Dallas/Fort Worth 1985", "Air Florida 90", "Air France 447", "Colgan 3407"], 0, "Delta 191 (L-1011, 1985)."),
]

COURSE = dict(
    slug="windshear-thunderstorm", title="Windshear and Thunderstorm Avoidance", header_title="Windshear and Thunderstorm Avoidance",
    tagline="Low-level windshear and microbursts, recognition and avoidance, the escape manoeuvre, weather radar and thunderstorm avoidance.",
    purpose="Refresh all flight crews' knowledge of windshear and thunderstorm hazards in line with ICAO Doc 9817 and EASA recurrent training requirements.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Explain windshear sources and effects", "Avoid and recognise windshear", "Apply the escape manoeuvre principles", "Use weather radar and avoid thunderstorms", "Brief and manage convective threats as a crew"],
    icon="drop", cert_prefix="WSA", quiz_count=10, pass_mark=80, group="refresher", season="Winter", finale=None,
    modules=[dict(title="Windshear", summary="Sources, effects, avoidance, recognition and the escape manoeuvre", icon="drop", lessons=range(1, 4)),
             dict(title="Thunderstorms and Planning", summary="Weather radar, avoidance, CRM and lessons learned", icon="people", lessons=range(4, 6))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Thunderstorm with a rain shaft near an airport", "Microbursts from convective clouds are the most dangerous windshear."),
            2: ("gen", "Airliner on approach with a storm nearby", "Avoid: delay the approach or divert."),
            3: ("gen", "Airliner climbing away at a high pitch attitude", "Escape: maximum thrust, wings level, pitch to the target."),
            4: ("gen", "Airliner deviating around a large cumulonimbus", "Deviate early — at least 20 NM from severe echoes."),
            5: ("gen", "Two pilots briefing on the flight deck", "Brief the threat and agree the decision points.")},
)
