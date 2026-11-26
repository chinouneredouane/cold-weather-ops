"""Dash 8-Q400 Performance — 8 lessons following the standard type-rating performance syllabus
(environmental factors, definitions, chart technique, take-off, climb and obstacles, en-route, landing, abnormal situations)
and the Q400 performance lesson used in type-rating training (AFM Section 5 charts and worked exercises).

Sources: Dash 8-400 AFM Section 5 (Performance) charts reproduced from the type-rating course; EASA CS-25, Part-CAT
CAT.POL.A; ICAO Annex 6. Operational values always come from the approved AFM, the company runway analysis / performance
tool, the QRH and OM B."""
from courses.perf_common import fig, Q, REGS

_AFM = "Dash 8-400 AFM, Section 5 (type-rating course material) — for training only, use the current AFM"


def f(img, caption):
    return fig("q400-" + img, caption, _AFM)


LESSONS = [
# 1
dict(title="Environmental Factors and Performance Definitions", minutes=9,
objectives=["Explain how pressure altitude, temperature, wind, runway condition and slope affect performance.", "Define the Q400 performance speeds.",
            "Define the declared distances and the field length requirements."],
body="""
<h2>Five environmental factors</h2>
<ul>
  <li><strong>Pressure altitude</strong> — higher aerodromes: less dense air, less power and lift, longer distances.</li>
  <li><strong>Temperature</strong> — hot air is less dense. The PW150A is flat rated: torque is available up to a limiting temperature, then decreases.</li>
  <li><strong>Wind</strong> — headwind shortens, tailwind lengthens the ground distances. AFM charts use 50 % of the headwind and 150 % of the tailwind.</li>
  <li><strong>Runway condition</strong> — wet or contaminated surfaces degrade braking and may add drag.</li>
  <li><strong>Runway slope</strong> — uphill lengthens the take-off and shortens the stop; downhill the opposite.</li>
</ul>
<h2>Performance speeds</h2>
<table><thead><tr><th>Speed</th><th>Meaning</th></tr></thead><tbody>
<tr><td>V1</td><td>Take-off decision speed: the maximum speed for the first stopping action and the minimum speed to continue after an engine failure</td></tr>
<tr><td>VR</td><td>Rotation speed</td></tr>
<tr><td>V2</td><td>Take-off safety speed at 35 ft with one engine inoperative</td></tr>
<tr><td>VMCG</td><td>Minimum control speed on the ground (rudder only)</td></tr>
<tr><td>VMCA</td><td>Minimum control speed in the air (≤ 5° bank)</td></tr>
<tr><td>VMCL</td><td>Minimum control speed in the landing configuration</td></tr>
<tr><td>VREF</td><td>Reference landing speed at 50 ft</td></tr>
</tbody></table>
<h2>Declared distances</h2>
<ul>
  <li><strong>TORA</strong> — take-off run available (runway).</li>
  <li><strong>ASDA</strong> — TORA + stopway.</li>
  <li><strong>TODA</strong> — TORA + clearway.</li>
  <li><strong>LDA</strong> — landing distance available; it begins at a <strong>displaced threshold</strong> when one exists.</li>
</ul>
<h2>Field requirements</h2>
<p>For every take-off the aeroplane must meet three requirements: the <strong>take-off run required</strong> (TORR) ≤ TORA, the <strong>take-off distance required</strong> (TODR) ≤ TODA and the <strong>accelerate-stop distance required</strong> (ASDR) ≤ ASDA (CAT.POL.A.205). Each is the longer of the engine-failure case and 115 % of the all-engines case (for distance and run).</p>
""",
takeaways=["Altitude and temperature reduce density: less power and lift, longer distances.", "Charts use 50 % headwind and 150 % tailwind.",
           "TORR ≤ TORA, TODR ≤ TODA, ASDR ≤ ASDA."],
check=dict(q="ASDA equals:", options=["TORA + clearway", "TORA + stopway", "LDA + stopway", "TODA − TORA"], answer=1, explain="Accelerate-stop distance available = runway + stopway."),
),
# 2
dict(title="Reading AFM Performance Charts", minutes=8,
objectives=["Describe the layout of a carpet-type AFM chart.", "Use reference lines and guide lines correctly.",
            "Read the normal take-off power torque setting."],
body="""
<h2>How the charts are built</h2>
<p>AFM Section 5 charts are "carpet" charts: several panels side by side, each adding one variable. A typical take-off chart starts with <strong>OAT</strong> and <strong>pressure altitude</strong>, then moves to <strong>weight</strong>, then to <strong>wind</strong> and <strong>slope</strong> corrections, and ends on the result scale.</p>
<h2>Reference lines and guide lines</h2>
<ol>
  <li>Enter the first panel with the first variable and move to the line of the second variable.</li>
  <li>Move horizontally to the <strong>reference line</strong> of the next panel.</li>
  <li>From the reference line, follow the <strong>guide lines</strong> (parallel to the nearest curve) until you reach the value of the new variable — then continue horizontally.</li>
  <li>At the last panel, read the result on the scale. Use a sharp pencil and a straight edge: a few millimetres can mean hundreds of feet or pounds.</li>
</ol>
<div class="callout caution"><span class="label">Watch the limits</span><p>Hatched or shaded areas, "structural limit" lines and "maximum" annotations are limits, not suggestions. Never extrapolate outside the chart.</p></div>
<h2>Take-off power</h2>
<p>The first step of every take-off computation is the <strong>normal take-off power torque</strong> for the OAT and pressure altitude (propeller 1020 rpm, bleeds and de-icing as indicated on the chart). Below a certain temperature the torque is constant (flat rated); above it, the torque decreases with temperature.</p>
""" + f("takeoff-torque", "Normal take-off power torque setting (ground), propeller 1020 rpm, de-icing on or off, bleeds off: enter OAT, move to the pressure altitude, read the torque.") + """
<div class="callout info"><span class="label">In the line</span><p>The company runway analysis and the EFB performance tool use the same AFM data. Learning the charts explains <em>why</em> the numbers change — and lets you catch an input error.</p></div>
""",
takeaways=["Carpet charts add one variable per panel.", "At each reference line follow the guide lines to the new value.", "Always start with the take-off power torque for OAT and pressure altitude."],
check=dict(q="At a reference line, how do you correct for the next variable?", options=["Move vertically down", "Follow the guide lines to the value, then continue horizontally", "Read the result directly", "Ignore the line"], answer=1,
           explain="Guide lines carry the value from the reference line to the actual value of the variable."),
),
# 3
dict(title="Take-off Weight Limits — the WAT Limit", minutes=8,
objectives=["List the factors that can limit the take-off weight.", "Explain the WAT (weight–altitude–temperature) limit.",
            "Read the maximum permissible take-off weight chart."],
body="""
<h2>What can limit the take-off weight?</h2>
<ul>
  <li>The <strong>structural</strong> maximum take-off weight.</li>
  <li>The <strong>WAT limit</strong> — climb performance with one engine inoperative.</li>
  <li>The <strong>field lengths</strong>: take-off run, take-off distance, accelerate-stop distance.</li>
  <li><strong>Obstacles</strong> in the take-off flight path (runway analysis).</li>
  <li>Brake energy, the landing weight at destination (plus trip fuel), and MEL/CDL penalties.</li>
</ul>
<h2>The WAT limit</h2>
<p>The <strong>WAT limit</strong> is the maximum permissible take-off weight for the aerodrome <strong>altitude and temperature</strong> that still gives the minimum climb gradients with one engine inoperative (second segment 2.4 %, final segment 1.2 % gross for a twin — CS 25.121). It does not depend on runway length: on a hot, high aerodrome the aeroplane can be WAT-limited on a very long runway.</p>
""" + f("wat-takeoff", "Maximum permissible take-off weight (WAT limit), take-off flap 15°: enter OAT, move to the pressure altitude, read the weight — never above the structural limit.") + """
<h2>Exercise approach</h2>
<p>The type-rating exercise plans a departure from a short runway (Toronto City Centre, runway 08: elevation 251 ft, 4,000 ft, no clearway or stopway, slope −0.02 %). The questions to ask are always the same:</p>
<ol>
  <li>What sources do I need? — AFM / runway analysis, weather, NOTAMs, aerodrome chart.</li>
  <li>What do I need about the airport? — elevation, runway length, slope, clearway, stopway, line-up allowance, obstacles.</li>
  <li>What weather affects the calculation? — OAT, QNH (pressure altitude), wind (head/tail and crosswind components), runway condition.</li>
  <li>What is the take-off torque? Is the aeroplane WAT-limited?</li>
  <li>What weight do the TOR, TOD and ASD allow?</li>
</ol>
""",
takeaways=["The lowest of structural, WAT, field, obstacle, brake and landing limits applies.", "The WAT limit protects the one-engine-inoperative climb gradients.",
           "A long runway does not remove the WAT limit."],
check=dict(q="What does the WAT limit protect?", options=["The accelerate-stop distance", "The minimum one-engine-inoperative climb gradients", "The brake energy", "The tyre speed"], answer=1,
           explain="Weight–altitude–temperature limit: the heaviest weight that still meets the OEI climb gradients."),
),
# 4
dict(title="Take-off Field Lengths — TOR, TOD and ASD", minutes=10,
objectives=["Correct the available distances for wind and slope.", "Find the weight allowed by the take-off run, take-off distance and accelerate-stop distance.",
            "Identify the limiting requirement."],
body="""
<h2>Wind and slope correction</h2>
<p>The field length charts are drawn for <strong>zero wind and zero slope</strong>. The first step converts the actual distance available into an equivalent zero-wind, zero-slope distance using the wind and slope correction charts.</p>
""" + f("tor-tod-wind", "Take-off run and take-off distance required — wind and runway slope correction, flap 15°.") + """
<h2>Take-off run and take-off distance</h2>
<p>With the corrected distance, the TOR and TOD charts give the maximum weight for the OAT and pressure altitude. In the exercise, the 4,000 ft runway corrected to about <strong>3,200 ft</strong>: the take-off run allows about <strong>56,200 lb</strong> and the take-off distance about <strong>55,000 lb</strong>.</p>
""" + f("tor", "Take-off run required — zero wind, zero runway slope, flap 15°.") + f("tod", "Take-off distance required — zero wind, zero runway slope, flap 15°.") + """
<h2>Accelerate-stop distance</h2>
<p>The ASDA is corrected the same way (4,000 ft became about <strong>3,300 ft</strong>), then the accelerate-stop chart gives the weight: about <strong>49,000 lb</strong>.</p>
""" + f("asd-wind", "Accelerate-stop distance required — wind and runway slope correction, flap 15°.") + f("asd", "Accelerate-stop distance required — zero wind, zero runway slope, flap 15°.") + """
<h2>The limiting requirement</h2>
<table><thead><tr><th>Requirement</th><th>Weight allowed (exercise)</th></tr></thead><tbody>
<tr><td>Take-off run</td><td>56,200 lb</td></tr>
<tr><td>Take-off distance</td><td>55,000 lb</td></tr>
<tr><td>Accelerate-stop distance</td><td><strong>49,000 lb — limiting</strong></td></tr>
</tbody></table>
<p>On a short runway without stopway, the accelerate-stop distance is often limiting. The next lesson shows how a V1 reduction (V1/VR split) recovers weight.</p>
<div class="callout warn"><span class="label">Training values</span><p>The figures above are a classroom exercise from the type-rating course. In operation use the company runway analysis or EFB tool with the actual conditions.</p></div>
""",
takeaways=["Correct distances for wind and slope first.", "Read the weight from the TOR, TOD and ASD charts; the lowest limits.",
           "Short runway without stopway: often ASD-limited."],
check=dict(q="In the exercise, which requirement limited the take-off weight?", options=["Take-off run", "Take-off distance", "Accelerate-stop distance", "WAT"], answer=2,
           explain="The ASD allowed 49,000 lb, lower than the TOR (56,200 lb) and TOD (55,000 lb)."),
),
# 5
dict(title="V1 Reductions and Take-off Speeds", minutes=8,
objectives=["Explain how a V1/VR split changes TOR, TOD and ASD.", "Use the V1/VR ratio in the AFM.",
            "Read VR and V1 from the rotation speed chart."],
body="""
<h2>Splitting V1 and VR</h2>
<p>When V1 is reduced below VR (V1/VR ratio below 1.0):</p>
<ul>
  <li>The <strong>accelerate-stop distance decreases</strong> — the stop starts at a lower speed.</li>
  <li>The <strong>take-off distance increases</strong> — after an engine failure at the lower V1, the aeroplane accelerates longer on one engine to VR.</li>
  <li>The <strong>take-off run</strong> also increases slightly.</li>
</ul>
<p>When the take-off is ASD-limited and there is spare take-off distance, a V1 reduction moves the take-off towards balance and allows a higher weight.</p>
<h2>Exercise result</h2>
<p>At 49,000 lb with a reduced V1/VR ratio, the exercise gave a take-off run of about <strong>2,800 ft</strong>, a take-off distance of about <strong>3,100 ft</strong> and an accelerate-stop distance of about <strong>2,800 ft</strong> — all within the corrected distances.</p>
<h2>Rotation speed and V1</h2>
<p>The rotation speed chart gives <strong>VR</strong> from OAT, pressure altitude and weight, then converts VR to <strong>V1</strong> with the V1/VR ratio. In the exercise, VR was about <strong>102 KIAS</strong>. The chart also shows the minimum VR (based on VMCA) and the minimum V1 (VMCG).</p>
""" + f("v1-vr", "Rotation speed VR and conversion of VR and V1/VR ratio to V1, flap 15°: minimum VR and minimum V1 limits are marked.") + """
<h2>Sanity check of the speeds</h2>
<p>Always check: V1 ≤ VR ≤ V2. A set such as V1 120, VR 128, V2 138 is consistent; V1 above VR, or V2 below VR, is not.</p>
<div class="callout info"><span class="label">Wet or contaminated runways</span><p>Use the AFM supplement data: V1 is reduced, the screen height is lower and the take-off weight may be restricted. Reduced take-off power is not used on contaminated runways.</p></div>
""",
takeaways=["V1/VR split: ASD down, TOD and TOR up.", "Use it when ASD-limited with spare TODA.", "Always V1 ≤ VR ≤ V2; V1 ≥ VMCG."],
check=dict(q="How does a V1/VR split affect the TOD and ASD?", options=["Both decrease", "TOD increases, ASD decreases", "TOD decreases, ASD increases", "No effect"], answer=1,
           explain="A lower V1 means an earlier, shorter stop, but a longer one-engine acceleration to VR."),
),
# 6
dict(title="Climb Segments and Runway Analysis", minutes=9,
objectives=["Describe the take-off climb segments of the Q400.", "Read a runway analysis page and its limit codes.",
            "Explain the engine failure procedure (special departure)."],
body="""
<h2>Climb segments</h2>
<table><thead><tr><th>Segment</th><th>From – to</th><th>Configuration</th><th>Minimum gross gradient (twin)</th></tr></thead><tbody>
<tr><td>1st</td><td>35 ft – gear retracted</td><td>Take-off flap, gear retracting, V2</td><td>Positive</td></tr>
<tr><td>2nd</td><td>Gear up – acceleration altitude (min 400 ft)</td><td>Take-off flap, V2, take-off power</td><td>2.4 %</td></tr>
<tr><td>3rd</td><td>Acceleration</td><td>Level acceleration, flap retraction</td><td>—</td></tr>
<tr><td>4th</td><td>Flaps retracted – 1,500 ft</td><td>Clean, maximum continuous power, final climb speed</td><td>1.2 %</td></tr>
</tbody></table>
<p>The net flight path (gross − 0.8 %) must clear obstacles by 35 ft (CAT.POL.A.210). Obstacles are handled by the <strong>runway analysis</strong>.</p>
<h2>Reading a runway analysis page</h2>
<p>A runway analysis page is produced for one runway and one aeroplane / engine type (DHC-8-402, PW150A). It shows:</p>
<ul>
  <li>The aerodrome and runway, elevation, length, line-up shift, clearway, stopway and slope.</li>
  <li>Any <strong>special engine-failure procedure</strong>: "climb at … via … reaching … or … turn …", the flap retraction height and any hold.</li>
  <li>Conditions: flap, bleeds, anti-ice.</li>
  <li>For each temperature and wind: the maximum weight, with a <strong>limit code</strong> (for example field, climb, obstacle, brake energy, structural) and the V-speeds.</li>
</ul>
<div class="callout caution"><span class="label">Read the limit code</span><p>A "climb limit" (dry runway) code means more runway will not help; only a lower temperature, less weight, or a different flap setting will. A field-limit code means distance is the problem.</p></div>
<h2>Engine failure procedures</h2>
<p>If an obstacle is critical, the company publishes a special procedure for an engine failure after V1. Brief it before every take-off: the turn point or altitude, the track, the acceleration altitude and where to hold.</p>
""",
takeaways=["Twin gradients: 2nd segment 2.4 %, 4th (final) 1.2 % gross; net = gross − 0.8 %.", "The runway analysis gives the maximum weight, the limit code and the special procedure.",
           "Brief the engine failure procedure before every take-off."],
check=dict(q="The runway analysis shows a climb limit. Will a longer runway increase the weight?", options=["Yes", "No — the limit is the climb gradient, not distance", "Only with a tailwind", "Only on a wet runway"], answer=1,
           explain="A climb limit depends on altitude, temperature, configuration and weight, not on runway length."),
),
# 7
dict(title="En-route Performance and Driftdown", minutes=7,
objectives=["Describe the one-engine-inoperative en-route requirements.", "Explain the driftdown speed and altitude.",
            "Use the en-route data in the AOM/FCOM."],
body="""
<h2>Engine failure in cruise</h2>
<p>After an engine failure at cruise level the remaining engine at <strong>maximum continuous power</strong> cannot hold altitude: the aeroplane drifts down to the altitude where power equals drag.</p>
<ul>
  <li><strong>Driftdown speed</strong>: the speed for the best lift-to-drag ratio — the shallowest descent and highest level-off altitude.</li>
  <li><strong>Driftdown altitude (ceiling)</strong>: where level flight can be maintained with one engine at MCP.</li>
</ul>
<h2>Rules</h2>
<p>CAT.POL.A.215: the net flight path (gross reduced by 1.1 % for a twin) must clear the terrain by 2,000 ft while descending and 1,000 ft in level flight, within 5 NM of the track (10 NM without the navigation accuracy), and allow a landing at a suitable aerodrome.</p>
<h2>Cruise data</h2>
<p>The AOM/FCOM gives tables for maximum cruise power, long-range cruise, maximum endurance and single-engine cruise at maximum continuous power, with torque, fuel flow and TAS for weight, altitude and ISA deviation. The Q200 course shows how these tables are read; the Q400 method is identical.</p>
<div class="callout info"><span class="label">Icing</span><p>Ice protection on and ice accretion reduce the single-engine ceiling: use the icing performance data in mountainous areas.</p></div>
""",
takeaways=["Engine failure in cruise: MCP, best L/D speed, drift down to the ceiling.", "Net path = gross − 1.1 %; 2,000 ft / 1,000 ft clearance within 5 NM.",
           "Icing lowers the single-engine ceiling."],
check=dict(q="What speed gives the highest level-off altitude after an engine failure in cruise?", options=["VMO", "Best lift-to-drag (driftdown) speed", "V2", "VREF"], answer=1,
           explain="The best L/D speed gives the shallowest descent and the highest driftdown ceiling."),
),
# 8
dict(title="Landing Performance and Abnormal Landing Factors", minutes=10,
objectives=["Find the landing WAT limit.", "Compute the unfactored and factored landing field length.",
            "Apply the abnormal landing distance factors (example: hydraulic system failure)."],
body="""
<h2>Landing WAT limit</h2>
<p>The <strong>maximum permissible landing weight (WAT limit)</strong> ensures the approach climb gradient (one engine, approach flap: 2.1 %) and the landing climb gradient (all engines, landing flap: 3.2 %) for the aerodrome altitude and temperature.</p>
""" + f("wat-landing-15", "Maximum permissible landing weight (WAT limit), landing flap 15°, approach flap 10°.") + f("wat-landing-35", "Maximum permissible landing weight (WAT limit), landing flap 35°, approach flap 15°.") + """
<h2>Worked example</h2>
<p>Aerodrome elevation 1,217 ft, runway 21, wind 220/09G14 (headwind 9 kt, crosswind 2 kt), temperature 26 °C, landing weight 59,000 lb.</p>
""" + f("unfactored-ld-15", "Unfactored landing distance, flap 15°: weight, airfield altitude, wind and slope — about 2,600 ft in the example.") + """
<h2>From unfactored to factored distance</h2>
<p>The unfactored distance is what a test pilot achieves. The operating rules require the aeroplane to stop within a fraction of the LDA. For turboprops, CAT.POL.A.230 requires a full stop within <strong>70 %</strong> of the LDA (factor 1/0.7 ≈ <strong>1.43</strong>); with the 60 % rule the factor is 1.67. On a wet runway the result is increased by a further 15 %.</p>
""" + f("landing-field-length", "Landing field length required: the unfactored distance multiplied by the operational landing field length factor.") + """
<table><thead><tr><th>Flap</th><th>Unfactored</th><th>× 1.43 (70 % rule)</th><th>× 1.67 (60 % rule)</th></tr></thead><tbody>
<tr><td>15°</td><td>2,600 ft</td><td>3,718 ft</td><td>4,342 ft</td></tr>
<tr><td>35°</td><td>2,300 ft</td><td>3,289 ft</td><td>3,841 ft</td></tr>
</tbody></table>
""" + f("unfactored-ld-35", "Unfactored landing distance, flap 35°: about 2,300 ft in the same example.") + """
<h2>Abnormal landing factors</h2>
<p>For a failure that affects landing (for example a <strong>hydraulic system failure</strong>, QRH), the unfactored landing distance in abnormal configurations is the normal unfactored distance multiplied by the <strong>abnormal landing distance factor</strong>, with further increases for a wet runway and/or a higher approach speed (VREF + 10).</p>
""" + f("abnormal-ld", "Unfactored landing distance in abnormal configurations: in the example, about 6,100 ft for a wet runway AND VREF + 10.") + """
<div class="callout warn"><span class="label">In flight</span><p>Before the approach, compare the abnormal landing distance with the LDA (CAT.OP.MPA.300). If it does not fit, divert to a longer runway.</p></div>
<h2>Review</h2>
<ul>
  <li>TORA is the runway length declared available for the take-off run.</li>
  <li>The WAT limit is the maximum weight for altitude and temperature.</li>
  <li>A V1/VR split increases the TOD and reduces the ASD.</li>
  <li>Crosswind and tailwind limits are in the AFM and OM B (tailwind 10 kt unless approved otherwise).</li>
</ul>
""",
takeaways=["Landing WAT: approach climb 2.1 % (OEI) and landing climb 3.2 % (AEO).", "Turboprop dispatch: stop within 70 % of LDA (factor 1.43); wet +15 %.",
           "Abnormal configurations: apply the AFM/QRH factors and check against the LDA before the approach."],
check=dict(q="For a turboprop, a full stop must be achieved within what part of the LDA (dry, dispatch)?", options=["50 %", "60 %", "70 %", "85 %"], answer=2,
           explain="CAT.POL.A.230(a)(2): turbo-propeller aeroplanes — 70 % of the LDA."),
),
]

QUESTIONS = [
Q(1, "AFM charts account for wind by using:", ["100 % head and tail wind", "50 % of the headwind and 150 % of the tailwind", "No wind", "Only the crosswind"], 1, "Regulatory wind factoring."),
Q(1, "An uphill slope on take-off:", ["Shortens the take-off distance", "Lengthens the take-off distance", "Has no effect", "Reduces V1"], 1, "Uphill reduces the acceleration."),
Q(1, "TODA equals:", ["TORA + stopway", "TORA + clearway", "LDA", "ASDA − TORA"], 1, "Clearway is added to TORA."),
Q(1, "VMCL is the minimum control speed:", ["On the ground", "In the landing configuration", "With both engines", "At V2"], 1, "Approach/landing configuration."),
Q(2, "At a reference line on a carpet chart you should:", ["Move vertically", "Follow the guide lines to the value of the new variable", "Stop", "Extrapolate"], 1, "Guide lines carry the correction."),
Q(2, "The first value computed for the take-off is usually:", ["VREF", "The normal take-off power torque", "The landing distance", "The driftdown speed"], 1, "Torque from OAT and pressure altitude."),
Q(2, "May you extrapolate outside an AFM chart?", ["Yes", "No", "Only for weight", "Only in cold weather"], 1, "Never extrapolate."),
Q(3, "The WAT limit stands for:", ["Wind–Altitude–Temperature", "Weight–Altitude–Temperature", "Wet–Asphalt–Take-off", "Weight–Area–Thrust"], 1, "Maximum weight for altitude and temperature."),
Q(3, "Can a very long runway remove a WAT limitation?", ["Yes", "No", "Only with clearway", "Only at night"], 1, "The WAT limit is a climb limit."),
Q(3, "Which is NOT a take-off weight limit?", ["Structural", "WAT", "Accelerate-stop distance", "Cabin altitude"], 3, "Cabin altitude is not a take-off weight limit."),
Q(4, "Field length charts are drawn for:", ["Actual wind", "Zero wind and zero slope", "Wet runway", "ISA only"], 1, "Correct for wind and slope first."),
Q(4, "In the exercise the TOR allowed 56,200 lb, the TOD 55,000 lb and the ASD 49,000 lb. The field-limited weight is:", ["56,200 lb", "55,000 lb", "49,000 lb", "The average"], 2, "The lowest limit applies."),
Q(4, "On a short runway without stopway, which requirement is often limiting?", ["Take-off run", "Accelerate-stop distance", "Landing distance", "Cruise"], 1, "ASD."),
Q(5, "A lower V1/VR ratio:", ["Increases the ASD", "Reduces the ASD and increases the TOD", "Reduces both", "Has no effect"], 1, "Earlier stop, longer one-engine acceleration."),
Q(5, "Which set of speeds is correct?", ["V1 130, VR 128, V2 138", "V1 120, VR 128, V2 124", "V1 126, VR 125, V2 130", "V1 120, VR 128, V2 138"], 3, "V1 ≤ VR ≤ V2."),
Q(5, "V1 may not be lower than:", ["VREF", "VMCG", "V2", "VMO"], 1, "Directional control on the ground after an engine failure."),
Q(6, "The 2nd segment minimum gross gradient for a twin is:", ["1.2 %", "2.1 %", "2.4 %", "3.2 %"], 2, "CS 25.121(b)."),
Q(6, "The 2nd segment ends at:", ["35 ft", "Gear retraction", "The acceleration altitude (minimum 400 ft)", "1,500 ft"], 2, "Then the level acceleration begins."),
Q(6, "Where do you find the special engine failure procedure for a runway?", ["The METAR", "The runway analysis / company engine-out procedures", "The MEL", "The NOTAM only"], 1, "Published with the runway analysis."),
Q(6, "The net take-off flight path must clear obstacles by at least:", ["15 ft", "35 ft", "1,000 ft", "2,000 ft"], 1, "CAT.POL.A.210."),
Q(7, "After an engine failure in cruise, set:", ["Take-off power", "Maximum continuous power", "Flight idle", "Maximum cruise power"], 1, "MCP on the remaining engine."),
Q(7, "During driftdown the net path must clear terrain by:", ["35 ft", "500 ft", "2,000 ft", "5,000 ft"], 2, "2,000 ft while descending."),
Q(8, "The approach climb gradient (OEI) for a twin is:", ["1.2 %", "2.1 %", "2.4 %", "3.2 %"], 1, "CS 25.121(d)."),
Q(8, "An unfactored landing distance of 2,600 ft with factor 1.43 gives:", ["2,600 ft", "3,718 ft", "4,342 ft", "1,820 ft"], 1, "2,600 × 1.43 ≈ 3,718 ft."),
Q(8, "On a wet runway, the dry landing field length is increased by:", ["5 %", "15 %", "43 %", "67 %"], 1, "CAT.POL.A.235: 115 %."),
Q(8, "After a hydraulic failure, the landing distance is found with:", ["The normal chart only", "The abnormal landing distance factors (AFM/QRH)", "A guess", "The take-off chart"], 1, "Abnormal configuration factors."),
Q(8, "The landing WAT limit protects:", ["The landing distance", "The approach and landing climb gradients", "The tyre speed", "The fuel reserve"], 1, "Climb gradients for a go-around."),
]

COURSE = dict(
    slug="q400-performance",
    title="Dash 8-Q400 Performance",
    header_title="Dash 8-Q400 Performance",
    tagline="Dash 8-Q400 performance with the AFM charts: environmental factors, chart technique, WAT limit, take-off field lengths, V1 reductions, runway analysis, en-route and landing, abnormal landing factors.",
    purpose="Give Q400 flight crew the ability to compute and understand take-off, climb, en-route and landing performance with the AFM Section 5 charts, the runway analysis and the QRH, in line with EASA CS-25 and Part-CAT.",
    audience="Dash 8-Q400 flight crew (type rating and recurrent).",
    objectives=["Explain the environmental factors and definitions", "Read AFM carpet charts", "Find the WAT limit and the field-limited weight",
                "Use V1 reductions", "Read a runway analysis", "Plan for an engine failure en route", "Compute normal and abnormal landing distances"],
    icon="plane", cert_prefix="Q4P", quiz_count=15, pass_mark=80,
    group="refresher", season="Performance",
    finale=None,
    modules=[dict(title="Basics and Chart Technique", summary="Environmental factors, definitions and AFM chart reading", icon="search", lessons=range(1, 3)),
             dict(title="Take-off and Climb", summary="WAT limit, field lengths, V1 reductions, climb segments and runway analysis", icon="runway", lessons=range(3, 7)),
             dict(title="En-route and Landing", summary="Driftdown, landing WAT limit, landing field length and abnormal factors", icon="plane", lessons=range(7, 9))],
    lessons=LESSONS, questions=QUESTIONS,
    references=REGS,
    images={1: ("gen", "Turboprop airliner on a sunny apron", "Altitude, temperature, wind, runway and slope."),
            2: ("gen", "Flight deck with performance documents", "Reference line, guide lines, result."),
            3: ("gen", "Turboprop lined up on a hot runway", "Is the aircraft WAT limited?"),
            4: ("gen", "Short runway seen from the threshold", "TOR, TOD, ASD — the lowest weight wins."),
            5: ("gen", "Turboprop accelerating on the runway", "V1 ≤ VR ≤ V2."),
            6: ("gen", "Turboprop climbing away over hills", "Read the limit code."),
            7: ("gen", "Turboprop cruising over mountains", "MCP and best L/D speed."),
            8: ("gen", "Turboprop on final approach", "70 % of the LDA for a turboprop.")},
)
