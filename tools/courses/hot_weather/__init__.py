"""Hot Weather Operations refresher (summer season), all fleets. Built from the company Summer and Hot Weather
recurrent training programme (ground training topics and flight safety items), with ICAO Annex 6 and
EASA Part-CAT performance principles. Type values always come from the AFM/FCOM/AOM and QRH."""
from courses.upset_recovery.diagrams import FONT, INK, MUTED, LINE, GREEN, GREEN_D, RED, AMBER, BLUE


def hot_high_diagram():
    bars = [("Sea level, ISA", 1.0, GREEN), ("Sea level, ISA +25 °C", 1.18, AMBER), ("High elevation, ISA", 1.25, AMBER), ("High elevation, ISA +25 °C", 1.5, RED)]
    out = []
    for i, (lab, v, c) in enumerate(bars):
        y = 60 + i * 52
        out.append(f'<text x="20" y="{y+22}" font-weight="600">{lab}</text>'
                   f'<rect x="230" y="{y}" width="{v*280:.0f}" height="32" rx="6" fill="{c}"/>')
    svg = ("".join(out) + f'<text x="230" y="40" fill="{MUTED}">Take-off distance required (illustrative trend only)</text>'
           f'<text x="20" y="290" fill="{MUTED}">Higher temperature and elevation mean lower air density: less thrust and lift, higher true airspeed.</text>')
    return f"""<figure class="diagram"><svg viewBox="0 0 700 300" role="img" aria-label="Hot and high effect"><title>Effect of temperature and elevation on take-off distance</title>
<desc>Bars showing take-off distance increasing with temperature and with aerodrome elevation; illustrative only.</desc>
<g {FONT} font-size="13" fill="{INK}">{"".join(svg)}</g></svg>
<figcaption>Illustrative trend, not performance data. Always use the AFM / performance software, the QRH performance tables or Jetplan for actual values.</figcaption></figure>"""


FLEET = """<div class="table-wrap"><table>
<tr><th>Topic</th><th>Boeing 737-800</th><th>Dash 8-Q400 / Q200</th></tr>
<tr><td>Hot weather procedures</td><td>FCOM Supplementary Procedures — Adverse Weather, hot weather operation (SP 16.17)</td><td>AFM / AOM hot weather and high-temperature limitations</td></tr>
<tr><td>Engine and APU start limits</td><td>FCOM limitations; APU start on battery (SP 7.7)</td><td>AFM engine start and ITT limits; APU / ground power as installed</td></tr>
<tr><td>Bleeds-off operation</td><td>Bleeds-off take-off and landing procedure and performance credit (FCOM / QRH performance)</td><td>Bleed and pack settings for take-off per AFM performance charts</td></tr>
<tr><td>Fuel system checks</td><td>Spar fuel shut-off valve check (SP 12-01)</td><td>AOM fuel system procedures</td></tr>
<tr><td>Performance</td><td>QRH performance inflight / dispatch tables; Jetplan</td><td>AFM performance charts or company performance software; Jetplan</td></tr>
</table></div>"""

LESSONS = [
dict(title="Hot and High: Effects on Performance", minutes=8,
objectives=["Explain how temperature and elevation affect aircraft performance.", "Identify the performance limits that become critical in hot weather.", "Use the performance tools correctly."],
body="""
<h2>Density is everything</h2>
<p>High temperature and high aerodrome elevation both reduce <strong>air density</strong> — expressed as a high <strong>density altitude</strong>. Lower density means:</p>
<ul>
  <li><strong>less thrust or power</strong> from the engines — jets and turboprops alike are flat-rated only up to a certain temperature;</li>
  <li><strong>less lift</strong> at a given true airspeed — so the same indicated airspeed means a <strong>higher true airspeed and ground speed</strong>;</li>
  <li>longer take-off and landing distances, higher tyre speeds, and more energy for the brakes to absorb in a rejected take-off;</li>
  <li>reduced <strong>climb gradient</strong> — the climb limit (weight–altitude–temperature) and obstacle clearance often limit the take-off mass on hot days.</li>
</ul>
""" + hot_high_diagram() + """
<h2>Limits that become critical</h2>
<ul>
  <li><strong>Climb limit</strong> and <strong>obstacle limit</strong> — especially at southern aerodromes with high elevation and temperatures.</li>
  <li><strong>Runway limit</strong> — check NOTAMs for reduced declared distances (for example, a displaced threshold or the first part of a runway unusable).</li>
  <li><strong>Tyre speed limit</strong> and <strong>brake energy limit</strong> — higher ground speeds at high density altitude.</li>
  <li><strong>Landing distance</strong> — higher true airspeed at touchdown; a late or long flare uses runway very quickly.</li>
  <li><strong>Maximum temperature limits</strong> for take-off and landing in the AFM.</li>
</ul>

<h2>Performance tools</h2>
<ul>
  <li>Use the <strong>approved</strong> performance data: AFM / company performance software, QRH performance tables and the Jetplan operational flight plan.</li>
  <li>Enter the <strong>actual</strong> temperature, QNH, wind and runway condition. A few degrees can change the limiting mass.</li>
  <li>Check aerodrome accessibility: take-off alternate, destination alternate and en-route alternates.</li>
  <li>The first officer prepares the performance dispatch; the captain cross-checks it.</li>
</ul>
""",
takeaways=["Heat and elevation reduce density: less thrust and lift, higher true airspeed and ground speed.", "Climb, obstacle, tyre-speed and brake-energy limits become critical.", "Use approved performance data with actual conditions; check NOTAMs for reduced distances."],
check=dict(q="Why does the same indicated airspeed give a higher ground speed at a hot, high aerodrome?", options=["The wind is stronger", "Lower air density means a higher true airspeed for the same indicated airspeed", "The engines produce more thrust", "The runway is longer"], answer=1,
           explain="At low density, a given indicated airspeed corresponds to a higher true airspeed, and therefore a higher ground speed."),
),

dict(title="Engines, APU and Aircraft Systems in Hot Weather", minutes=8,
objectives=["Apply engine and APU limitations in high temperatures.", "Protect brakes, tyres and avionics in hot conditions.", "Use the fleet-specific hot weather procedures."],
body="""
<h2>Engines and APU</h2>
<ul>
  <li>Exhaust gas / inter-turbine temperature margins are smaller in hot air. Monitor starts closely and know the <strong>start limits</strong> and the hot start and hung start procedures.</li>
  <li>Keep engine running time on the ground to a minimum, and avoid using high thrust on the ground for long periods.</li>
  <li>APU limits (EGT, load) are also closer in hot weather. Ground power and conditioned air reduce APU use.</li>
</ul>

<h2>Brakes and tyres</h2>
<ul>
  <li>Brake temperatures rise faster and cool more slowly in hot weather. Respect the minimum <strong>brake cooling times</strong> between flights.</li>
  <li>Avoid riding the brakes during taxi — keep taxi speeds moderate (Lesson 5).</li>
  <li>Tyre pressures increase with temperature; tyres are also stressed by high ground speeds.</li>
</ul>

<h2>Cockpit, cabin and avionics</h2>
<ul>
  <li>Use ground conditioned air or the APU to cool the cabin and avionics before boarding.</li>
  <li>Watch for avionics overheat cautions and equipment cooling failures.</li>
  <li>Protect crew performance: drink water, manage fatigue and heat stress during long ground times.</li>
</ul>

<h2>Fleet-specific procedures</h2>
""" + FLEET + """
<div class="callout"><span class="label">Prepare</span><p>Before the summer recurrent training, review the hot weather supplementary procedures and limitations for your type. The values and the exact procedure always come from your aircraft manuals.</p></div>
""",
takeaways=["Smaller temperature margins on engine and APU starts — know the limits.", "Respect brake cooling times; avoid riding the brakes.", "Cool the aircraft with ground air or APU; watch avionics cooling.", "Use your type's hot weather procedures (B737 FCOM SP 16.17; Dash 8 AFM/AOM)."],
check=dict(q="What is a key consideration for brakes in hot weather?", options=["Brakes need no cooling in summer", "Brake temperatures rise faster and cool more slowly — respect cooling times", "Use maximum braking on every landing", "Set the parking brake during taxi"], answer=1,
           explain="Hot air reduces brake cooling; respect the cooling times between flights."),
),

dict(title="Fuel in Hot Weather", minutes=6,
objectives=["Explain the effect of temperature on fuel density and quantity.", "Apply fuel checks and MEL fuel items.", "Use the operational flight plan fuel figures correctly."],
body="""
<h2>Fuel density</h2>
<ul>
  <li>Hot fuel is <strong>less dense</strong>: the same mass takes up more volume. Uplift is often measured in litres but planned in kilograms — always convert with the <strong>actual density</strong> on the fuel docket.</li>
  <li>Check the <strong>uplift</strong>: the difference between the calculated and the actual uplift must be within the company tolerance.</li>
  <li>Respect any <strong>maximum fuel temperature</strong> limit in the AFM.</li>
</ul>

<h2>Fuel planning</h2>
<ul>
  <li>Use the Jetplan figures: trip fuel, contingency, alternate, final reserve, taxi and any extra fuel. Check the effect of a change of cruise level or take-off mass.</li>
  <li>Hot weather may impose a lower cruise level or a longer climb. Plan for possible weather deviations around convective activity.</li>
  <li>Check the zero fuel weight and fuel entries carefully — incorrect ZFW or fuel entries are a recurring flight safety event (Lesson 5).</li>
</ul>

<h2>Fuel system and MEL</h2>
<ul>
  <li>B737-800: perform the <strong>spar fuel shut-off valve check</strong> when required (FCOM SP 12-01).</li>
  <li>Read MEL fuel items in full, including the <strong>(M) maintenance</strong> and <strong>(O) operational</strong> procedures.</li>
</ul>
<div class="callout info"><span class="label">Example from the company LOFT — B737-800, MEL 28-01-03-01</span>
<p>A main tank aft fuel boost pump may be inoperative provided that: (a) both main tank forward pumps operate normally; (b) at the start of take-off, the fuel quantity in the associated tank is not less than 7,500 lb (3,402 kg); (c) a minimum fuel quantity of 2,500 lb (1,134 kg) is maintained in the associated tank; and (d) the boost pump is deactivated.</p>
<p>Always use the current MEL — this example is for training only.</p></div>
""",
takeaways=["Hot fuel is less dense — convert volume to mass with the actual density.", "Check the uplift and the ZFW / fuel entries carefully.", "Read every MEL item in full, including (M) and (O) procedures."],
check=dict(q="Why must you use the actual fuel density when checking the uplift on a hot day?", options=["Fuel is heavier when hot", "Hot fuel is less dense, so a given volume weighs less", "Density does not matter", "To calculate the cabin temperature"], answer=1,
           explain="Hot fuel occupies more volume for the same mass; the actual density converts litres to kilograms correctly."),
),

dict(title="Sand, Dust and Convective Weather", minutes=7,
objectives=["Recognise the hazards of dust, sand and drifting sand.", "Apply precautions on the ground and in flight.", "Manage convective weather and gusty winds in summer."],
body="""
<h2>Dust and sand</h2>
<ul>
  <li>Watch the reports for <code>DU</code> (dust), <code>SA</code> (sand), <code>DRSA</code> (low drifting sand), <code>BLSA</code> (blowing sand), <code>SS</code> / <code>DS</code> (sandstorm / duststorm). Visibility can fall very quickly.</li>
  <li>During the walk-around in dusty conditions, check pitot probes, static ports, engine inlets, APU inlet and air conditioning inlets. Fit covers when the aircraft is parked.</li>
  <li>Minimise engine and APU running and high thrust on sand-covered surfaces to limit ingestion. Use the procedure for taxi and take-off on contaminated or sandy surfaces if published.</li>
  <li>Sand on the runway reduces braking — treat it like a contaminant and report braking action if worse than expected.</li>
</ul>

<h2>Convective weather and wind</h2>
<ul>
  <li>Summer thunderstorms (<code>CB</code>, <code>TCU</code>) bring gusts, windshear, turbulence and sudden dust storms. Avoid cells by a wide margin.</li>
  <li><strong>Gusty winds</strong> — for example a reported wind of 18 kt gusting 28 kt — require a careful check of the company crosswind limits and the appropriate speed additives.</li>
  <li>Thermal turbulence close to the ground makes approaches less stable — be ready to go around.</li>
  <li>Dust devils and localised strong winds can affect take-off and landing.</li>
</ul>

<h2>Go-around in hot weather</h2>
<p>Climb performance is lower in hot, high conditions. Brief the missed approach, the climb gradient and any obstacles. Know the go-around technique for your type, including engine-out, and practise it in the simulator in hot weather conditions.</p>
""",
takeaways=["DU, SA, DRSA, SS/DS: visibility can collapse — watch the trend.", "Protect inlets and probes; minimise ground running and high thrust on sand.", "Summer CB and gusts: wide avoidance, check crosswind limits and speed additives.", "Lower go-around performance in hot, high conditions — brief it."],
check=dict(q="What does DRSA in a METAR mean?", options=["Dry runway, sand removed", "Low drifting sand", "Drizzle and sand", "Dust storm"], answer=1, explain="DRSA = low drifting sand."),
),

dict(title="Summer Flight Safety Focus Items", minutes=7,
objectives=["Review the flight safety events selected for this season.", "Apply the correct technique to prevent each event.", "Report events through the safety reporting system."],
body="""
<p>The training department has selected the following flight safety items for discussion with the TRI/TRE:</p>
<div class="table-wrap"><table>
<tr><th>Event</th><th>Why it matters</th><th>Prevention</th></tr>
<tr><td><strong>High taxi speed</strong></td><td>Hot brakes, reduced margins on turns and runway crossings, passenger injury.</td><td>Respect the company taxi speeds; use idle thrust and brief, firm braking applications rather than riding the brakes.</td></tr>
<tr><td><strong>Late or long flare</strong></td><td>Each second of float at high ground speed uses a large part of the runway and increases the landing distance.</td><td>Fly a stabilised approach to the aiming point; flare at the normal height; go around if a long landing develops.</td></tr>
<tr><td><strong>Incorrect flap setting, ZFW or fuel entries</strong></td><td>Wrong take-off speeds and trim — tail strike or degraded take-off performance.</td><td>Independent cross-check of performance data, FMS / performance entries and the load sheet by both pilots.</td></tr>
<tr><td><strong>Hard landing</strong></td><td>Structural damage, injuries; often after an unstable approach or late flare.</td><td>Stabilised approach; correct flare; report any suspected hard landing in the technical log.</td></tr>
<tr><td><strong>Bounced landing</strong></td><td>Risk of tail strike, nose gear damage or a second hard landing.</td><td>Apply the company bounced landing recovery technique; go around if in doubt.</td></tr>
<tr><td><strong>Use of reverse and APU</strong></td><td>Covered by the company reminder note (note de rappel).</td><td>Apply the reminder note exactly as published.</td></tr>
</table></div>

<h2>Safety notes and reporting</h2>
<ul>
  <li>Read and discuss the latest company <strong>safety notes</strong> before the simulator session.</li>
  <li><strong>Report events</strong> through the safety reporting system. Reports are used to improve training and procedures, under a just culture.</li>
</ul>
""",
takeaways=["Moderate taxi speeds protect brakes and people.", "A late or long flare at high ground speed eats runway — go around if needed.", "Cross-check flap, ZFW and fuel entries.", "Apply the bounced and hard landing techniques; report every event."],
check=dict(q="What is the most effective prevention for a long landing developing after a floated flare?", options=["Push the nose down to land", "Go around", "Increase reverse thrust only", "Extend the flaps further"], answer=1, explain="If a long landing develops, the safe action is a go-around."),
),

dict(title="MEL, Dispatch and the Summer Simulator Session", minutes=6,
objectives=["Apply the MEL and dispatch criteria for a summer flight.", "Prepare the summer recurrent simulator session.", "Combine hot weather, performance and LOFT topics."],
body="""
<h2>MEL and dispatch</h2>
<ul>
  <li>Check every MEL item for its effect on performance — some items impose mass penalties or limitations that matter more in hot weather.</li>
  <li>Apply the (M) and (O) procedures, the placards and any dispatch conditions.</li>
  <li>The MEL also contains the dispatch requirements for systems that need a specific approval — RVSM, RNAV/PBN and LVO.</li>
</ul>

<h2>The summer recurrent programme</h2>
<ul>
  <li><strong>Day 1 — ground refresher</strong>: engine and APU operation and limitations in hot weather, hot weather procedures, fuel, APU start on battery, bleeds-off take-off and landing, QRH performance, fuel system checks, RVSM, MEL and dispatch.</li>
  <li><strong>Days 2 and 3 — simulator</strong>: LOFT sectors to and from hot, high southern aerodromes with dust and drifting sand, MEL dispatch items, go-arounds and engine failures in hot weather, an RNAV approach briefing including temperature effects, and an LVO approach.</li>
  <li><strong>Mandatory exercises</strong>: upset recovery, windshear identification and escape, TCAS, EGPWS and pilot incapacitation — performed according to company procedures and DACM recommendations.</li>
</ul>

<h2>Preparing</h2>
<ul>
  <li>Prepare the performance dispatch from the Jetplan in the briefing room and discuss it as a crew.</li>
  <li>Review the courses in this academy: CFIT and EGPWS, RVSM, Upset Prevention and Recovery.</li>
</ul>
""",
takeaways=["Check MEL items for performance penalties — critical in hot weather.", "Summer recurrent: ground refresher day, then two simulator days with LOFT and mandatory exercises.", "Prepare performance and review the related academy courses before the session."],
check=dict(q="Which exercises are mandatory in the summer simulator session?", options=["Only engine failure", "Upset recovery, windshear, TCAS, EGPWS and pilot incapacitation", "Only CAT II approaches", "None"], answer=1,
           explain="Upset recovery, windshear, TCAS, EGPWS and pilot incapacitation are mandatory."),
),
]


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


QUESTIONS = [
Q(1, "High temperature and high elevation result in:", ["Higher air density", "Lower air density (high density altitude)", "No change in density", "Higher engine thrust"], 1, "Both reduce air density."),
Q(1, "At a hot, high aerodrome, take-off distances are:", ["Shorter", "Longer", "Unchanged", "Only affected by wind"], 1, "Less thrust and higher true airspeed lengthen distances."),
Q(1, "Which limit frequently restricts take-off mass on hot days?", ["Maximum zero fuel mass", "Climb (WAT) and obstacle limits", "Maximum landing mass", "Cabin altitude"], 1, "Reduced climb gradient makes the climb and obstacle limits critical."),
Q(1, "Which data must be used for take-off performance?", ["Rules of thumb", "Approved AFM data, performance software, QRH tables or Jetplan with actual conditions", "Last flight's figures", "ATC estimates"], 1, "Use approved data with actual conditions."),
Q(2, "Engine start temperature margins in hot weather are:", ["Larger", "Smaller", "Unchanged", "Irrelevant"], 1, "Hot air reduces EGT/ITT margins."),
Q(2, "In hot weather, brakes:", ["Cool faster", "Heat faster and cool more slowly", "Never overheat", "Do not need checking"], 1, "Respect the brake cooling times."),
Q(2, "Where are the B737-800 hot weather procedures found?", ["QRH only", "FCOM Supplementary Procedures — Adverse Weather (SP 16)", "MEL", "Jetplan"], 1, "FCOM SP 16 covers adverse weather, including hot weather."),
Q(3, "Hot fuel is:", ["Denser", "Less dense", "The same density", "Heavier per litre"], 1, "Hot fuel is less dense."),
Q(3, "Why is the ZFW entry important?", ["It sets the cabin temperature", "Wrong ZFW gives wrong take-off speeds and trim", "It is only for statistics", "It sets the fuel density"], 1, "Wrong ZFW leads to wrong speeds and trim."),
Q(3, "In MEL 28-01-03-01 (B737), what minimum fuel must be in the associated tank at the start of take-off?", ["2,500 lb", "5,000 lb", "7,500 lb (3,402 kg)", "No minimum"], 2, "Not less than 7,500 lb (3,402 kg) at the start of take-off."),
Q(4, "What does SS in a METAR mean?", ["Snow showers", "Sandstorm", "Smoke", "Squall"], 1, "SS = sandstorm."),
Q(4, "Why minimise high thrust on sand-covered surfaces?", ["To save fuel", "To limit sand and dust ingestion", "To reduce noise", "To keep brakes cool"], 1, "High thrust ingests sand and dust."),
Q(4, "Reported wind 120/18 gusting 28 kt. What must you check?", ["Only the headwind", "The company crosswind limits and speed additives", "Nothing", "The fuel density"], 1, "Gusts require checking crosswind limits and speed additives."),
Q(5, "What is the main risk of a late or long flare at high ground speed?", ["Hard landing only", "A large increase in landing distance", "Engine overheat", "Tyre underinflation"], 1, "Float at high ground speed uses runway rapidly."),
Q(5, "After a suspected hard landing, the crew should:", ["Do nothing", "Report it in the technical log", "Take off again", "Call ATC"], 1, "Report it so maintenance can inspect."),
Q(5, "Incorrect flap setting or ZFW entries are prevented by:", ["Faster preparation", "Independent cross-checks by both pilots", "Using last flight's data", "ATC confirmation"], 1, "Both pilots cross-check performance data."),
Q(6, "Which systems requiring specific approval have dispatch requirements in the MEL?", ["Galley ovens", "RVSM, RNAV/PBN and LVO", "Reading lights", "Lavatories"], 1, "The MEL includes dispatch requirements for RVSM, RNAV and LVO."),
Q(6, "Which exercises are mandatory in the summer simulator programme?", ["Only stalls", "Upset recovery, windshear, TCAS, EGPWS and pilot incapacitation", "Only circling", "Only engine fire"], 1, "These are the mandatory exercises."),
]

COURSE = dict(
    slug="hot-weather-operations",
    title="Hot Weather Operations",
    header_title="Hot Weather Operations",
    tagline="Summer and hot weather operations for all fleets: hot-and-high performance, engines and systems, fuel, sand and convective weather, flight safety focus items.",
    purpose="Prepare all flight crews (B737-800, Q400 and Q200) to operate safely, effectively and efficiently in a hot weather environment, as the ground part of the summer recurrent training.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Explain hot-and-high performance effects and limits", "Operate engines, APU and systems within limits in hot weather",
                "Manage fuel density, uplift and MEL fuel items", "Handle sand, dust, gusts and summer convective weather",
                "Prevent the selected flight safety events", "Prepare the summer recurrent simulator session"],
    icon="sun", cert_prefix="HWO", quiz_count=10, pass_mark=80,
    group="refresher", season="Summer",
    finale=None,
    modules=[dict(title="Performance and Aircraft Systems", summary="Hot and high performance, engines, APU, systems and fuel", icon="gear", lessons=range(1, 4)),
             dict(title="Weather, Safety and Preparation", summary="Sand, dust, convective weather, flight safety items, MEL and simulator", icon="people", lessons=range(4, 7))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner taking off over a desert aerodrome in the heat", "Hot and high: less density, less thrust, longer distances."),
            2: ("gen", "Airliner on a hot apron with heat haze", "Engines, APU, brakes and avionics all have tighter margins in the heat."),
            3: ("gen", "Airliner cruising over the desert", "Hot fuel is less dense — check the uplift in kilograms."),
            4: ("gen", "Dust storm approaching an aerodrome", "Sand and dust can reduce visibility within minutes."),
            5: ("gen", "Airliner landing on a sunny runway", "Stabilised approach, normal flare — go around if a long landing develops."),
            6: ("gen", "Two pilots on the flight deck at dusk", "Prepare the summer recurrent simulator session as a crew.")},
)
