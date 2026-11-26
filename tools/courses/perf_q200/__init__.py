"""Dash 8-Q200 Performance — 11 lessons following the company Q200 performance course syllabus:
definitions and environmental factors; speeds and runway distances; segments and climb/descent types; take-off speeds and WAT;
take-off gradients and field lengths; climb and cruise; descent and landing; go-around; icing; brake energy and turnaround;
abnormal situations.

Sources: Domestic Airlines Q200 performance course (diagrams); Dash 8 Series 200 AFM and Operating Data Manual charts and tables
reproduced from that course; EASA CS-25, Part-CAT CAT.POL.A; ICAO Annex 6 and 14. Operational values always come from the
current AFM, Operating Data Manual / AOM, QRH, the company runway analysis and OM B."""
from courses.perf_common import fig, Q, REGS

_C = "Domestic Airlines Q200 performance course"
_AFM = "Dash 8 Series 200 AFM / Operating Data Manual (from the company Q200 course) — for training only, use the current documents"


def c(img, caption):
    return fig("q200-" + img, caption, _C)


def a(img, caption):
    return fig("q200-" + img, caption, _AFM)


LESSONS = [
# 1
dict(title="Environmental Factors and Performance", minutes=9,
objectives=["Define pressure altitude and density altitude.", "Explain the effect of temperature, wind, runway condition and slope on performance.",
            "Define wet and contaminated runways."],
body="""
<h2>Pressure altitude and density altitude</h2>
<p><strong>Pressure altitude</strong> is the altitude read with 1013 hPa set — the value transmitted by the transponder and used for flight levels. <strong>Density altitude</strong> is pressure altitude corrected for the temperature deviation from ISA, and it is what the aeroplane "feels": all performance computations depend on it.</p>
<ul>
  <li>Standard day: density altitude = pressure altitude.</li>
  <li>Warm day: density altitude <strong>higher</strong> than pressure altitude.</li>
  <li>Cold day: density altitude <strong>lower</strong> than pressure altitude.</li>
</ul>
""" + c("density-warm", "Warm day: the aeroplane behaves as if it were higher than its true altitude.") + c("density-cold", "Cold day: the aeroplane behaves as if it were lower than its true altitude.") + """
<h2>High density altitude = less performance</h2>
<p>A high density altitude reduces engine power, propeller thrust and lift: take-off and landing distances increase and the rate of climb decreases. A low density altitude gives the opposite. <strong>Temperature</strong> has the same effect: high temperature — less performance.</p>
""" + c("temperature", "At sea level and normal temperature the aeroplane climbs steeply; in hot and high conditions the take-off run is longer and the climb shallower.") + """
<h2>Wind</h2>
<p>A headwind gives a shorter take-off distance and a lower ground speed for the same airspeed; a tailwind gives a longer distance and a higher ground speed. In flight, wind changes the ground speed and the drift.</p>
""" + c("wind-ground", "Head wind: shorter take-off distance, lower ground speed. Tail wind: longer take-off distance, higher ground speed — the airspeed is the same.") + c("wind-triangle", "Effect of wind in flight: the wind triangle (heading, track, drift angle).") + """
<h2>Runway condition</h2>
<p>A runway is <strong>wet</strong> when its surface is reflective with water, but without significant standing water. It is <strong>contaminated</strong> when more than 25 % of the surface in use is covered by water, slush or loose snow deeper than 3 mm (water equivalent), compacted snow or ice. Contaminants increase the wheel drag (longer acceleration) and degrade braking (longer stop and landing).</p>
<h2>Runway slope</h2>
<p>A downslope helps the acceleration and shortens the take-off distance but lengthens the stop; an upslope does the opposite.</p>
""",
takeaways=["Density altitude decides the performance: hot and high = less performance.", "Headwind shortens, tailwind lengthens the ground distances.",
           "Contaminated: > 25 % covered, > 3 mm water/slush/loose snow, compacted snow or ice.", "Downslope helps take-off acceleration but hurts stopping."],
check=dict(q="On a warm day, density altitude is:", options=["Equal to pressure altitude", "Higher than pressure altitude", "Lower than pressure altitude", "Zero"], answer=1,
           explain="Warm air is less dense: the aeroplane performs as if it were higher."),
),
# 2
dict(title="Speeds and Runway Distances", minutes=9,
objectives=["Define V1, VEF, VR, VLOF, V2, VREF, VS, VMCA and VMCG.", "Define TORA, TODA, ASDA, clearway and stopway.",
            "Define take-off distance, take-off run, LDA and LDR."],
body="""
<h2>Speed definitions</h2>
<ul>
  <li><strong>VEF</strong> — speed at which the critical engine is assumed to fail.</li>
  <li><strong>V1</strong> — decision speed: beyond it the take-off should no longer be rejected.</li>
  <li><strong>VR</strong> — rotation speed; <strong>VLOF</strong> — lift-off speed.</li>
  <li><strong>V2</strong> — take-off safety speed: safe climb with one engine inoperative.</li>
  <li><strong>VREF</strong> — reference landing (threshold) speed.</li>
  <li><strong>VS</strong> — stall speed.</li>
  <li><strong>VMCA</strong> / <strong>VMCG</strong> — minimum control speeds in the air / on the ground with the critical engine inoperative.</li>
</ul>
<h2>Runway distances</h2>
<p><strong>TORA</strong> is the runway length available for the take-off run. <strong>TODA</strong> is TORA plus clearway. <strong>ASDA</strong> is TORA plus stopway.</p>
<ul>
  <li><strong>Clearway</strong> — an area beyond the runway, under airport control, at least 152 m wide, with no object above a plane rising at 1.25 %.</li>
  <li><strong>Stopway</strong> — an area beyond the runway, at least as wide as the runway, able to support the aeroplane during a rejected take-off.</li>
</ul>
""" + c("runway-distances", "Declared distances: (A) runway only, (B) with clearway, (C) with stopway, (D) and (E) with displaced thresholds.") + """
<h2>Take-off distance and take-off run</h2>
<table><thead><tr><th></th><th>Take-off distance</th><th>Take-off run</th></tr></thead><tbody>
<tr><td>All engines</td><td>115 % of the distance to 35 ft</td><td>115 % of the distance to the mid-point between lift-off and 35 ft</td></tr>
<tr><td>Engine failure, dry</td><td>Distance to 35 ft, failure recognised at V1</td><td>Distance to the mid-point between lift-off and 35 ft</td></tr>
<tr><td>Engine failure, wet</td><td colspan="2">Distance to 15 ft, failure recognised at V1</td></tr>
</tbody></table>
<p>The longer of the cases is used.</p>
<h2>LDA and LDR</h2>
<p>The <strong>LDA</strong> is declared by the authority. The <strong>LDR</strong> is calculated by the crew from the AFM with landing mass, wind, temperature, elevation, slope and surface condition — and includes the regulatory safety factor.</p>
""" + c("landing-distances", "Landing distances: calculated landing distance plus the safety factor gives the LDR, which must not exceed the LDA."),
takeaways=["V1 = decision speed; V2 = one-engine safe climb speed.", "TODA = TORA + clearway; ASDA = TORA + stopway.",
           "TOD = longer of 115 % all-engine distance and engine-failure distance (35 ft dry, 15 ft wet).", "LDR (with safety factor) ≤ LDA."],
check=dict(q="The minimum width of a clearway is:", options=["30 m", "152 m (500 ft)", "Runway width", "300 m"], answer=1, explain="Clearway: at least 152 m wide, centred on the extended centreline."),
),
# 3
dict(title="Segments, Climb and Descent Types, Driftdown", minutes=8,
objectives=["Describe the take-off segments and the approach segments.", "Name the three climb types and three descent types.",
            "Define driftdown speed and driftdown altitude."],
body="""
<h2>Take-off segments</h2>
""" + c("takeoff-segments", "Take-off segments: start, thrust, speed, gear, flaps and minimum gradients for 2, 3 and 4 engines. Net flight path = gross flight path decreased by 0.8 % (twin).") + """
<p>For a twin: 1st segment positive gradient (gear retracting), 2nd segment at least 2.4 % (gear up, take-off flap, V2), 3rd segment level acceleration, final segment at least 1.2 % (clean, MCP).</p>
<h2>Approach segments</h2>
""" + c("approach-segments", "Instrument approach segments: arrival, initial, intermediate, final and missed approach.") + """
<h2>Types of climb</h2>
<p>The Dash 8 offers three climb schedules: <strong>Type I</strong> (high speed, about 210 kt), <strong>Type II</strong> (intermediate, about 170 kt) and <strong>Type III</strong> (low speed, about 130 kt) — speeds decrease with altitude per the chart.</p>
""" + a("climb-speeds", "Climb speeds — Types I, II and III (IAS versus altitude), applicable to all weights and temperatures.") + """
<h2>Types of descent</h2>
<p>Similarly, three descent types: <strong>Type I</strong> high speed, <strong>Type II</strong> intermediate and <strong>Type III</strong> low speed, each with its own torque setting.</p>
<h2>Driftdown</h2>
<ul>
  <li><strong>Driftdown speed (DDS)</strong> — the speed for the minimum drag and the best air distance per unit of height lost.</li>
  <li><strong>Driftdown altitude</strong> — the altitude to which the aeroplane descends to sustain level flight after the failure of one engine.</li>
</ul>
""" + a("driftdown-speed", "Driftdown speed, one engine inoperative, flap 0°: IAS versus weight."),
takeaways=["Twin: 2nd segment 2.4 %, final 1.2 %; net = gross − 0.8 %.", "Climb types I (fast), II, III (slow); descent types I, II, III.",
           "Driftdown speed = minimum drag; driftdown altitude = one-engine ceiling."],
check=dict(q="Which climb type is the slowest?", options=["Type I", "Type II", "Type III", "All the same"], answer=2, explain="Type III is the low speed climb (about 130 kt)."),
),
# 4
dict(title="Take-off Speeds and WAT Limit", minutes=9,
objectives=["Find VR, V1 (V1/VR ratio), V2 and the climb speed from the AFM charts.", "Apply the V1 correction for a wet or contaminated runway.",
            "Find the maximum permissible take-off weight (WAT limit)."],
body="""
<h2>V1 and VR</h2>
""" + a("v1-vr", "Rotation speed VR and conversion of VR and V1/VR ratio to V1, flap 5°.") + """
<h2>V2</h2>
""" + a("v2", "Take-off safety speed V2, flap 5°: OAT, pressure altitude and weight, with the minimum V2 marked.") + """
<h2>Final take-off climb speed</h2>
""" + a("vclimb", "Final take-off climb speed, flap 0°, versus weight.") + """
<h2>V1 on a wet or contaminated runway</h2>
<p>When the runway is wet or contaminated, <strong>V1 is reduced</strong> according to the AFM supplement: in the company course the reduction is about <strong>8 kt</strong>, adjusted for the wind — slightly less with a headwind, more with a tailwind. Always use the current supplement and the runway analysis for the actual condition.</p>
<h2>WAT limit</h2>
<p>The <strong>maximum permissible take-off weight (WAT limit)</strong> gives the minimum one-engine-inoperative climb gradients for the aerodrome altitude and temperature.</p>
""" + a("wat-takeoff", "Maximum permissible take-off weight (WAT limit), take-off flap 5°, with the structural limit."),
takeaways=["Find VR first, then V1 from the V1/VR ratio, then V2.", "Wet/contaminated: reduce V1 per the AFM supplement (about 8 kt, wind-corrected).",
           "The WAT limit depends on altitude and temperature, not runway length."],
check=dict(q="On a wet runway, V1 is:", options=["Increased", "Reduced per the AFM supplement", "Unchanged", "Set to V2"], answer=1,
           explain="Braking is worse, so the stop must start earlier."),
),
# 5
dict(title="Take-off Climb Gradients and Field Lengths", minutes=10,
objectives=["Find the second-segment and final-segment gradients with one engine inoperative.", "Find the take-off run, take-off distance and accelerate-stop distance required.",
            "Apply wind and slope corrections."],
body="""
<h2>Second segment gradient</h2>
""" + a("second-segment", "Second segment take-off gross climb gradient, one engine inoperative, flap 5°.") + """
<h2>Final segment gradient</h2>
""" + a("final-segment", "Final take-off gross climb gradient, one engine inoperative, flap 0°.") + """
<h2>Take-off run and distance</h2>
""" + a("tor", "Take-off run required — zero wind, zero runway slope, flap 5°.") + a("tod", "Take-off distance required — zero wind, zero runway slope, flap 5°.") + a("tor-tod-wind", "Take-off run or take-off distance required — wind and runway slope correction, flap 5°.") + """
<h2>Accelerate-stop distance</h2>
""" + a("asd", "Accelerate-stop distance required — zero wind, zero runway slope, flap 5°.") + a("asd-wind", "Accelerate-stop distance required — wind and runway slope correction, flap 5°.") + """
<div class="callout info"><span class="label">Method</span><p>Compute each requirement, correct for wind and slope, compare with TORA, TODA and ASDA. The lowest weight from field length, WAT, obstacles, brake energy and structure is the maximum take-off weight.</p></div>
""",
takeaways=["2nd segment ≥ 2.4 %, final ≥ 1.2 % gross (one engine inoperative).", "TOR, TOD and ASD are read at zero wind/slope, then corrected.",
           "The most limiting weight applies."],
check=dict(q="The field length charts are drawn for:", options=["Actual wind and slope", "Zero wind and zero slope — a correction chart follows", "Wet runway", "Flap 0°"], answer=1,
           explain="The wind and slope correction chart converts the result."),
),
# 6
dict(title="Climb and Cruise Performance", minutes=9,
objectives=["Read the climb speed and torque tables (900 and 1050 rpm).", "Read maximum climb and maximum cruise power tables.",
            "Compare long range cruise, maximum endurance and single-engine cruise, and choose the cruise altitude."],
body="""
<h2>Climb tables</h2>
<p>For each climb type, the Operating Data Manual gives the speed and torque setting at propeller 900 rpm and 1050 rpm, with time, fuel and distance to climb.</p>
""" + a("climb-type1-900", "Type I climb (high speed): speed and torque setting, propeller 900 rpm.") + a("max-climb-power", "Maximum climb power: torque setting and fuel flow, propeller 900 rpm, ISA.") + """
<h2>Cruise</h2>
<ul>
  <li><strong>Maximum cruise power</strong> — highest cruise speed.</li>
  <li><strong>Long range cruise</strong> — the best distance per unit of fuel (range is fuel used over distance).</li>
  <li><strong>Maximum endurance</strong> — the least fuel per hour (endurance is fuel used over time): for holding.</li>
  <li><strong>Single-engine cruise at maximum continuous power</strong> — after an engine failure.</li>
</ul>
""" + a("max-cruise-power", "Maximum cruise power: torque setting and fuel flow, propeller 900 rpm.") + a("lrc", "Long range cruise: speed and torque setting, propeller 1050 rpm.") + a("max-endurance", "Maximum endurance: speed and torque setting, propeller 900 rpm.") + a("se-cruise-mcp", "Single-engine cruise at maximum continuous power: speed and torque setting, propeller 1200 rpm.") + """
<h2>Choosing the cruise altitude</h2>
<p>The best altitude depends on the stage length and the winds: on short sectors the climb and descent dominate. The minimum block time table gives the cruise altitude and technique for the shortest block time.</p>
""" + a("optimum-altitude", "Minimum block time technique: recommended cruise altitude for the stage length."),
takeaways=["Each climb type has tables at 900 and 1050 rpm.", "Range = distance per fuel (LRC); endurance = time per fuel (holding).",
           "Single-engine cruise uses MCP at 1200 rpm."],
check=dict(q="Which cruise schedule should be used for holding?", options=["Maximum cruise power", "Long range cruise", "Maximum endurance", "Single-engine MCP"], answer=2,
           explain="Endurance minimises the fuel used per hour."),
),
# 7
dict(title="Descent and Landing Performance", minutes=9,
objectives=["Use the descent type tables.", "Find the approach, landing and go-around speeds.",
            "List the four limits on the maximum permissible landing weight."],
body="""
<h2>Descent</h2>
<p>The three descent types (I high, II intermediate, III low speed) each have a table of speed and torque, with time, fuel and distance to descend.</p>
""" + a("descent-type1", "Type I descent (high speed): speed and torque setting, propeller 900 rpm.") + """
<h2>Approach, landing and go-around speeds</h2>
""" + a("landing-speeds", "Landing speeds: approach and go-around speed (flap 5°) and VREF (flap 15°) versus weight.") + """
<h2>Maximum permissible landing weight</h2>
<p>The landing weight must not exceed:</p>
<ol>
  <li>the <strong>structural</strong> maximum landing weight;</li>
  <li>the <strong>WAT limit</strong> for altitude and temperature (approach and landing climb gradients);</li>
  <li>the weight allowed by the <strong>landing field length</strong> available (for a turboprop, stop within 70 % of the LDA — CAT.POL.A.230; wet +15 %);</li>
  <li>the weight for which the <strong>brake energy</strong> does not exceed the limit.</li>
</ol>
""" + a("wat-landing-15", "Maximum permissible landing weight (WAT limit), landing flap 15°, approach flap 5°.") + a("wat-landing-35", "Maximum permissible landing weight (WAT limit), landing flap 35°, approach flap 15°."),
takeaways=["Descent types I, II, III each with speed and torque tables.", "Landing weight: structural, WAT, field length (70 % LDA for turboprops), brake energy.",
           "Flap 35 gives shorter landings but a lower WAT limit than flap 15."],
check=dict(q="Which is NOT one of the four limits on the landing weight?", options=["Structural", "WAT", "Landing field length", "Cruise altitude"], answer=3,
           explain="The four limits are structural, WAT, field length and brake energy."),
),
# 8
dict(title="Go-around Performance", minutes=7,
objectives=["Define the approach climb and balked landing climb requirements.", "Read the approach gross climb gradient (one engine) and balked landing gradient (both engines) charts."],
body="""
<h2>Two go-around cases</h2>
<ul>
  <li><strong>Approach climb</strong> — one engine inoperative, approach flap, gear up: at least <strong>2.1 %</strong> gross for a twin (CS 25.121(d)).</li>
  <li><strong>Balked landing (landing climb)</strong> — both engines, landing configuration, gear down: at least <strong>3.2 %</strong> (CS 25.119).</li>
</ul>
<p>These requirements are the basis of the landing WAT limit. In operation, the published missed approach may need a higher gradient (2.5 % or more): check it with the charts below.</p>
""" + a("approach-climb-5", "Approach gross climb gradient — one engine inoperative, flap 5°.") + a("approach-climb-15", "Approach gross climb gradient — one engine inoperative, flap 15°.") + a("balked-landing-15", "Balked landing gross climb gradient — both engines operating, flap 35°.") + """
<div class="callout caution"><span class="label">Briefing</span><p>When the missed approach requires more than the standard gradient, compare the chart gradient with the procedure — at high temperature or with ice the aeroplane may not achieve it with one engine.</p></div>
""",
takeaways=["Approach climb (OEI) ≥ 2.1 %; balked landing (AEO) ≥ 3.2 %.", "Check the published missed approach gradient on hot days and in icing."],
check=dict(q="The balked landing climb is computed with:", options=["One engine, clean", "Both engines, landing configuration, gear down", "One engine, gear up", "Both engines, flaps up"], answer=1,
           explain="CS 25.119: all engines, landing configuration."),
),
# 9
dict(title="Performance in Icing Conditions", minutes=8,
objectives=["Distinguish the three icing performance cases.", "Apply the icing corrections to take-off, en-route and landing data."],
body="""
<h2>Why ice changes the numbers</h2>
<p>Ice on the unprotected surfaces and between boot cycles increases drag and raises the stall speed. The engine intakes and bleeds used for ice protection reduce the power available. Speeds increase, gradients decrease and distances increase.</p>
""" + c("icing-photo", "Ice accretion on an unprotected surface.") + """
<h2>1 — Before entering icing conditions</h2>
<p>Take-off performance data with <strong>ice protection ON and no ice accumulation</strong>; ice accumulation is assumed for the fourth (final) segment gradient in the net flight path.</p>
""" + a("icing-before", "Performance corrections before entering icing conditions (ice protection systems ON).") + """
<h2>2 — In icing conditions</h2>
<p>En-route and landing data with <strong>ice protection ON</strong> and ice on unprotected surfaces plus ice build-up on protected surfaces between boot cycles.</p>
""" + a("icing-in", "Performance corrections in icing conditions (ice protection systems ON).") + """
<h2>3 — After flight in icing conditions</h2>
<p>En-route and landing data with <strong>ice protection OFF</strong> and ice suspected on unprotected surfaces.</p>
""" + a("icing-after", "Performance corrections after flight in icing conditions with suspected ice accumulation on unprotected surfaces (ice protection systems OFF).") + """
<div class="callout warn"><span class="label">Remember</span><p>Use the increased (icing) speeds and the corrected landing distance. Never take off with ice, frost or snow on the aeroplane — see the Cold Weather Operations course.</p></div>
""",
takeaways=["Three cases: before icing (ON, no ice), in icing (ON, ice), after icing (OFF, suspected ice).", "Icing: higher speeds, lower gradients, longer distances."],
check=dict(q="Which data apply after leaving icing conditions with ice suspected on unprotected surfaces?", options=["Normal data", "Ice protection OFF with suspected ice accumulation", "Take-off data", "No correction"], answer=1,
           explain="The third case: protection off, ice suspected on unprotected surfaces."),
),
# 10
dict(title="Brake Energy and Minimum Turnaround Time", minutes=8,
objectives=["Explain why brake energy limits rejected take-offs and quick turnarounds.", "Read the brake energy and minimum turnaround time charts."],
body="""
<h2>Energy into heat</h2>
<p>During a rejected take-off or a landing, most of the aeroplane's kinetic energy becomes heat in the brakes. Too much heat can melt the <strong>fusible plugs</strong> of the wheels: the tyres deflate to prevent a burst. The brakes then need time to cool before another take-off can be made safely.</p>
""" + c("brake-photo", "Hot brakes after a heavy stop.") + """
<h2>Rejected take-off</h2>
""" + a("brake-energy-rto", "Brake energy in accelerate-stop — zero wind, zero runway slope, flap 5° (pre-mod 8/2484 aeroplanes, AFM amendment 1).") + a("turnaround", "Minimum turnaround time from the brake energy level for a landing or a prior accelerate-stop, versus OAT.") + """
<h2>Landing</h2>
""" + a("brake-energy-landing", "Brake energy in landing — zero wind, zero runway slope, flap 15°.") + """
<div class="callout caution"><span class="label">Hot and short</span><p>High weight, high temperature, high elevation and tailwind all raise the brake energy. Respect the minimum turnaround time before the next departure, and after a high-energy rejected take-off keep clear of the wheels — fusible plugs may release.</p></div>
""",
takeaways=["Brake energy grows with weight and the square of the speed.", "Fusible plugs deflate overheated tyres to prevent a burst.", "Respect the minimum turnaround time from the charts."],
check=dict(q="What is the purpose of the fusible plugs?", options=["To cool the brakes", "To deflate overheated tyres before they burst", "To measure brake wear", "To lock the wheels"], answer=1,
           explain="They melt at a set temperature and release the tyre pressure."),
),
# 11
dict(title="Performance in Abnormal Situations", minutes=8,
objectives=["Use the abnormal landing distance factors.", "Find the unfactored landing distance and apply the factors.",
            "Check the result against the LDA before the approach."],
body="""
<h2>Unfactored landing distance</h2>
<p>The AFM unfactored landing distance is the distance from 50 ft to a full stop in the normal configuration. It is the starting point for both dispatch (with the regulatory factors) and abnormal situations.</p>
""" + a("unfactored-ld-15", "Unfactored landing distance, flap 15°.") + a("unfactored-ld-35", "Unfactored landing distance, flap 35°.") + """
<h2>Abnormal configurations</h2>
<p>The unfactored landing distance in an abnormal configuration is the normal unfactored distance <strong>multiplied by the abnormal landing distance factor</strong> from the AFM tables (for example propeller, engine, flap, flight control, hydraulic or anti-skid failures).</p>
""" + a("abnormal-factors-1", "Landing distance factors for abnormal configurations (part 1).") + a("abnormal-factors-2", "Landing distance factors for abnormal configurations (part 2).") + a("abnormal-ld", "Unfactored landing distance in abnormal configurations.") + """
<h2>Decision</h2>
<ol>
  <li>Complete the QRH procedure and note the landing flap, VREF increment and the factor.</li>
  <li>Compute the abnormal landing distance for the actual weight, wind and runway condition.</li>
  <li>Compare with the LDA; if it does not fit with a reasonable margin, choose a longer runway.</li>
  <li>Brief the landing technique, braking and reverser plan.</li>
</ol>
<div class="callout warn"><span class="label">Do not rush</span><p>Abnormal landing distances can double the normal distance. Take the time to compute and cross-check.</p></div>
""",
takeaways=["Abnormal distance = normal unfactored distance × AFM abnormal factor.", "Always compare with the LDA before the approach.", "Brief the technique and the go-around."],
check=dict(q="How is the abnormal landing distance found?", options=["Normal factored distance + 10 %", "Normal unfactored distance × the AFM abnormal factor", "Take-off distance", "QRH guess"], answer=1,
           explain="The AFM abnormal landing distance factor multiplies the unfactored distance."),
),
]

QUESTIONS = [
Q(1, "Pressure altitude is read with which setting?", ["QNH", "QFE", "1013 hPa", "Field elevation"], 2, "Standard setting 1013 hPa."),
Q(1, "A high density altitude:", ["Improves performance", "Reduces performance: longer distances, lower climb rate", "Has no effect", "Only affects landing"], 1, "High density altitude = less performance."),
Q(1, "A headwind on take-off gives:", ["A longer distance", "A shorter distance and lower ground speed", "A higher ground speed", "No change"], 1, "Same airspeed, less ground speed."),
Q(1, "A runway is contaminated when more than what fraction is covered?", ["10 %", "25 %", "50 %", "100 %"], 1, "More than 25 %."),
Q(1, "A downslope on take-off:", ["Increases the take-off distance", "Reduces the take-off distance", "Reduces the ground speed", "Has no effect"], 1, "Gravity helps the acceleration."),
Q(2, "V2 is:", ["The decision speed", "The take-off safety speed with one engine inoperative", "The rotation speed", "The stall speed"], 1, "Safe one-engine climb speed."),
Q(2, "ASDA equals:", ["TORA + clearway", "TORA + stopway", "TODA + stopway", "LDA"], 1, "Runway plus stopway."),
Q(2, "On a wet runway, the take-off distance with an engine failure is measured to:", ["50 ft", "35 ft", "15 ft", "0 ft"], 2, "15 ft screen height."),
Q(2, "The all-engine take-off distance is factored by:", ["100 %", "115 %", "125 %", "167 %"], 1, "115 % of the all-engines distance to 35 ft."),
Q(3, "The net take-off flight path of a twin is the gross path reduced by:", ["0.5 %", "0.8 %", "1.1 %", "2.4 %"], 1, "0.8 %."),
Q(3, "The Type I climb is flown at about:", ["130 kt", "170 kt", "210 kt", "250 kt"], 2, "High speed climb."),
Q(3, "The driftdown speed is chosen for:", ["Maximum speed", "Minimum drag", "Maximum power", "Minimum time"], 1, "Best L/D — minimum drag."),
Q(4, "In which order are the take-off speeds found?", ["V2, V1, VR", "VR, then V1 from the V1/VR ratio, then V2", "V1 only", "VREF first"], 1, "The chart converts VR and V1/VR to V1."),
Q(4, "On a wet runway, V1 is reduced by about (company course, still air):", ["2 kt", "8 kt", "20 kt", "30 kt"], 1, "About 8 kt, corrected for wind per the AFM supplement."),
Q(4, "The WAT limit depends on:", ["Runway length", "Weight, altitude and temperature", "Wind only", "Fuel"], 1, "Weight–altitude–temperature."),
Q(5, "The minimum final segment gross gradient (twin) is:", ["0 %", "1.2 %", "2.4 %", "3.2 %"], 1, "CS 25.121(c)."),
Q(5, "The second segment gradient chart is for:", ["Both engines", "One engine inoperative, flap 5°", "Landing", "Clean"], 1, "OEI, take-off flap."),
Q(6, "Endurance is:", ["Fuel used over distance", "Fuel used over time", "Speed over distance", "Distance over time"], 1, "Endurance = time per fuel."),
Q(6, "Single-engine cruise uses:", ["Maximum take-off power", "Maximum continuous power", "Flight idle", "Long range cruise"], 1, "MCP on the remaining engine."),
Q(6, "Which schedule gives the best distance per fuel?", ["Maximum cruise", "Long range cruise", "Maximum endurance", "Type I climb"], 1, "LRC."),
Q(7, "For a turboprop, the dispatch landing distance must fit within:", ["60 % of LDA", "70 % of LDA", "85 % of LDA", "100 % of LDA"], 1, "CAT.POL.A.230(a)(2)."),
Q(7, "Which is a limit on the landing weight?", ["Cruise level", "Brake energy", "Climb type", "Descent type"], 1, "Brake energy is one of the four limits."),
Q(8, "The minimum approach climb gradient (OEI, twin) is:", ["1.2 %", "2.1 %", "2.4 %", "3.2 %"], 1, "CS 25.121(d)."),
Q(8, "The minimum balked landing gradient (all engines) is:", ["2.1 %", "2.4 %", "3.2 %", "5 %"], 2, "CS 25.119."),
Q(9, "Before entering icing conditions, take-off data assume:", ["Ice on all surfaces", "Ice protection ON, no ice accumulation", "Ice protection OFF", "No correction"], 1, "Case 1."),
Q(9, "Ice on the aeroplane:", ["Reduces stall speed", "Increases drag and stall speed", "Improves climb", "Has no effect"], 1, "Higher speeds, lower gradients, longer distances."),
Q(10, "After a high-energy RTO, the tyres may deflate because:", ["The brakes lock", "The fusible plugs melt", "The pressure gauge fails", "The anti-skid releases air"], 1, "Fusible plugs protect against bursts."),
Q(10, "The minimum turnaround time chart is entered with:", ["Fuel", "The brake energy absorbed", "Passenger count", "Altitude only"], 1, "Brake energy per brake."),
Q(11, "The abnormal landing distance equals:", ["Normal factored distance", "Unfactored distance × abnormal factor", "Take-off distance", "LDA × 0.7"], 1, "Per the AFM tables."),
Q(11, "If the abnormal landing distance exceeds the LDA:", ["Land anyway", "Choose a longer runway / divert", "Increase speed", "Use flap 0"], 1, "Find a runway where it fits."),
]

COURSE = dict(
    slug="q200-performance",
    title="Dash 8-Q200 Performance",
    header_title="Dash 8-Q200 Performance",
    tagline="Dash 8-Q200 performance through all phases of flight with the AFM charts and Operating Data Manual tables: definitions, take-off, climb, cruise, descent, landing, go-around, icing, brake energy and abnormal situations.",
    purpose="Enable Q200 flight crew to compute aircraft performance during all phases of flight using the AFM charts, Operating Data Manual tables and related material, in line with EASA CS-25 and Part-CAT.",
    audience="Dash 8-Q200 flight crew (type rating and recurrent).",
    objectives=["Explain the environmental factors and definitions", "Compute take-off speeds, WAT limit, gradients and field lengths",
                "Use the climb, cruise and descent tables", "Compute landing weight limits and go-around gradients",
                "Apply icing corrections", "Respect brake energy and turnaround time", "Compute abnormal landing distances"],
    icon="plane", cert_prefix="Q2P", quiz_count=15, pass_mark=80,
    group="refresher", season="Performance",
    finale=None,
    modules=[dict(title="Definitions", summary="Environmental factors, speeds, runway distances, segments, climb and descent types, driftdown", icon="search", lessons=range(1, 4)),
             dict(title="Take-off", summary="Take-off speeds, WAT limit, climb gradients and field lengths", icon="runway", lessons=range(4, 6)),
             dict(title="Climb, Cruise, Descent and Landing", summary="Climb and cruise tables, descent, landing and go-around", icon="plane", lessons=range(6, 9)),
             dict(title="Special Cases", summary="Icing, brake energy and turnaround time, abnormal situations", icon="snow", lessons=range(9, 12))],
    lessons=LESSONS, questions=QUESTIONS,
    references=REGS,
    images={1: ("gen", "Turboprop on a hot apron", "Hot and high = less performance."),
            2: ("gen", "Runway with stopway seen from the threshold", "TORA, TODA, ASDA."),
            3: ("gen", "Turboprop climbing away", "Segments and climb types."),
            4: ("gen", "Turboprop lined up for take-off", "VR, V1, V2 and the WAT limit."),
            5: ("gen", "Turboprop climbing over hills", "Gradients and field lengths."),
            6: ("gen", "Turboprop cruising above the clouds", "Range or endurance?"),
            7: ("gen", "Turboprop descending toward the airport", "Four limits on the landing weight."),
            8: ("gen", "Turboprop going around", "2.1 % OEI, 3.2 % all engines."),
            9: ("gen", "Turboprop in icing clouds", "Before, in and after icing."),
            10: ("gen", "Turboprop on a short runway", "Respect the turnaround time."),
            11: ("gen", "Turboprop on final approach", "Unfactored × abnormal factor.")},
)
