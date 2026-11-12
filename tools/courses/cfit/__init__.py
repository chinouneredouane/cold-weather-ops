"""CFIT / EGPWS refresher (summer season), all fleets. Based on the company CFIT presentations (Q400 and Q200,
TRI R. Djemli) and the company SOP EGPWS recovery tables, completed with ICAO Annex 6 / PANS-OPS (Doc 8168),
EASA CAT.IDE.A.150 and CAT.OP.MPA.115 (CDFA), and the Flight Safety Foundation ALAR / CFIT toolkit."""
from courses.upset_recovery.diagrams import FONT, INK, MUTED, LINE, GREEN, GREEN_D, RED, AMBER, BLUE


def cdfa_diagram():
    svg = f"""
<line x1="40" y1="280" x2="660" y2="280" stroke="#7a4c26" stroke-width="6"/>
<rect x="560" y="272" width="100" height="8" fill="#3b4540"/><text x="610" y="300" text-anchor="middle" fill="{MUTED}">runway</text>
<path d="M60 70 L580 272" stroke="{GREEN}" stroke-width="4"/>
<path d="M60 70 L160 70 L180 130 L300 130 L320 200 L470 200 L480 225" stroke="{RED}" stroke-width="3.5" stroke-dasharray="9 6" fill="none"/>
<line x1="40" y1="225" x2="660" y2="225" stroke="{AMBER}" stroke-dasharray="4 4"/><text x="46" y="218" fill="{AMBER}" font-weight="700">MDA</text>
<path d="M240 248 l20 -32 l20 32z M380 252 l14 -24 l14 24z" fill="#3e5a4a"/>
<text x="250" y="60" fill="{GREEN_D}" font-weight="700">CDFA: one constant descent angle, like an ILS glide path</text>
<text x="330" y="160" fill="{RED}" font-weight="700">“dive and drive”: step down early,</text>
<text x="330" y="178" fill="{RED}">then fly level close to the terrain</text>"""
    return f"""<figure class="diagram"><svg viewBox="0 0 700 320" role="img" aria-label="CDFA versus dive and drive"><title>CDFA versus step-down descent</title>
<desc>A continuous descent final approach follows a constant angle to the runway; a dive-and-drive profile descends early and flies level close to terrain.</desc>
<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg>
<figcaption>Continuous descent final approach (CDFA, also called CANPA) keeps the aircraft stabilised on a constant path. EASA requires CDFA for non-precision approaches unless otherwise approved (CAT.OP.MPA.115).</figcaption></figure>"""


def lookahead_diagram():
    svg = f"""
<path d="M40 300 L200 300 L260 240 L330 250 L420 140 L500 170 L560 110 L660 300z" fill="#5d7b67"/>
<path d="M100 150 l40 -4 l10 -10 l6 2 l-4 10 l30 -2 l4 4 l-30 4 l-4 12 l-6 0 l-2 -10 l-40 4z" fill="{INK}"/>
<path d="M190 150 L420 120 L420 200 Z" fill="{AMBER}" opacity=".25"/>
<path d="M190 150 L320 135 L320 180 Z" fill="{RED}" opacity=".35"/>
<text x="330" y="105" fill="{AMBER}" font-weight="700">CAUTION area: “TERRAIN AHEAD” / “CAUTION TERRAIN”</text>
<text x="200" y="215" fill="{RED}" font-weight="700">WARNING area: “TERRAIN AHEAD, PULL UP” / “PULL UP”</text>
<text x="40" y="40" font-weight="700" font-size="14">Enhanced function: look-ahead against the terrain database</text>
<text x="40" y="60" fill="{MUTED}">The caution comes first (typically up to about a minute ahead), the warning later (typically about 30 seconds ahead).</text>"""
    return f"""<figure class="diagram"><svg viewBox="0 0 700 320" role="img" aria-label="EGPWS look-ahead"><title>EGPWS terrain look-ahead</title>
<desc>The look-ahead function compares the predicted flight path with the terrain database and gives a caution then a warning.</desc>
<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg>
<figcaption>The look-ahead function depends on accurate aircraft position and an up-to-date terrain database. Exact timings depend on the installation.</figcaption></figure>"""


ESCAPE = """
<div class="table-wrap"><table>
<tr><th>Fleet</th><th>Pilot flying</th><th>Pilot monitoring</th></tr>
<tr><td><strong>Dash 8-Q400</strong><br><span class="muted">Company SOP, EGPWS Recovery (Rev 02)</span></td>
<td>Calls <strong>“CHECK POWER”</strong>. Selects <strong>GA</strong> and disconnects the autopilot. Advances the power levers <strong>to the detent</strong>, rolls wings level and pitches aggressively to initiate the climb, respecting the stick shaker. Targets <strong>V<sub>GA</sub></strong>.<br>Once clear of terrain: establishes level flight and reconfigures the aircraft.</td>
<td>Confirms <strong>NTOP</strong> on the engine display and calls <strong>“POWER SET”</strong>. Monitors radio altimeter and vertical speed and informs the PF of performance and terrain clearance.<br>Once clear: advises ATC — “(call sign) EGPWS recovery, new altitude / flight level …”.</td></tr>
<tr><td><strong>Dash 8-Q200</strong><br><span class="muted">Company SOP, Table 25 EGPWS recovery</span></td>
<td>Calls <strong>“CHECK POWER”</strong>. Selects <strong>GA</strong> and disconnects the AP. Advances the power levers to <strong>MTOP</strong>, rolls wings level and pitches aggressively to initiate the climb, responding to the stick shaker. Targets <strong>V<sub>GA</sub></strong>.<br>Once clear: establishes level flight and configures the aircraft.</td>
<td>Confirms <strong>MTOP</strong> and calls <strong>“POWER SET”</strong>. Monitors radio altimeter and vertical speed and informs the PF of performance and terrain clearance.<br>Once clear: advises ATC of the EGPWS recovery and new altitude or flight level.</td></tr>
<tr><td><strong>Boeing 737-800</strong></td>
<td colspan="2">Apply the <strong>Terrain Avoidance</strong> manoeuvre in the <strong>QRH (Non-Normal Manoeuvres)</strong> and the FCTM exactly as published. <em>Memory item — review it in your QRH before this course.</em></td></tr>
</table></div>"""

LESSONS = [
dict(title="CFIT: Definition, Defences and Contributing Factors", minutes=6,
objectives=["Define controlled flight into terrain (CFIT).", "Identify where and why CFIT accidents happen.", "List the main defences and contributing factors."],
body="""
<h2>Definition</h2>
<p><strong>Controlled flight into terrain (CFIT)</strong> occurs when an airworthy aircraft, under the complete control of the crew, is inadvertently flown into terrain, water or an obstacle. The crew is generally unaware of the danger until it is too late.</p>
<ul>
  <li>Most CFIT accidents happen during <strong>approach and landing</strong>, often on <strong>non-precision approaches</strong>.</li>
  <li>Many are caused by a loss of situational awareness, particularly in the <strong>vertical plane</strong>. Many crash sites lie on the extended centreline of an approach.</li>
  <li>Unfamiliarity with the approach, or misreading the approach chart, are common factors — especially where the approach has several step-down altitudes between the initial and final approach fixes.</li>
</ul>
<p>The result is almost always a hull loss with fatalities. Since terrain awareness warning systems (TAWS) became mandatory, CFIT accidents have become much rarer — but they still happen, mostly where the warning was absent, ignored or acted on too late.</p>

<h2>Defences</h2>
<ul>
  <li>Standard operating procedures, including briefings and callouts;</li>
  <li>terrain awareness warning systems (EGPWS / TAWS);</li>
  <li>situational awareness relative to terrain;</li>
  <li>flying the <strong>published IFR procedure</strong> — never improvising in IMC;</li>
  <li>appropriate use of the autoflight system;</li>
  <li>training — including the type-specific escape manoeuvre.</li>
</ul>

<h2>Contributing factors</h2>
<ul>
  <li><strong>Weather</strong>: rain, turbulence and icing increase workload; poor visibility and darkness contribute to disorientation.</li>
  <li><strong>Communication</strong>: non-standard phraseology, misunderstood clearances, altimeter setting errors.</li>
  <li><strong>Human factors</strong>: fatigue, complacency on familiar routes, distraction and high workload in the approach.</li>
  <li><strong>Automation</strong>: wrong mode, wrong target, or the crew not noticing an unintended descent.</li>
</ul>
""",
takeaways=["CFIT: an airworthy aircraft, under control, flown into terrain without the crew realising.", "Most occur in approach and landing, often non-precision approaches.", "Defences: SOPs, EGPWS, terrain awareness, published procedures, automation, training."],
check=dict(q="In which phase of flight do most CFIT accidents occur?", options=["Take-off", "Cruise", "Approach and landing", "Taxi"], answer=2, explain="Most CFIT accidents occur during approach and landing, often on non-precision approaches."),
),

dict(title="Altimeters, Safe Altitudes and Charts", minutes=7,
objectives=["Apply correct altimeter setting procedures.", "Use minimum safe altitudes and chart information.", "Recognise when temperature corrections are needed."],
body="""
<h2>Altimeters</h2>
<ul>
  <li>Know the <strong>units</strong> used in the area: hectopascals or inches of mercury, feet or metres. Be ready to convert feet and metres.</li>
  <li>Be vigilant during radio transmissions: read back the altimeter setting in full, and verify if in doubt — QNH 1013 and 29.92 can be confused.</li>
  <li>Apply the correct setting for the <strong>phase of flight</strong> (transition altitude and level), with a cross-check and read-back procedure on the flight deck.</li>
  <li><strong>Cross-check the radio altimeter with the barometric altimeter</strong>, especially in the approach.</li>
  <li>Fly higher than the minimum altitudes during atmospheric anomalies — strong winds over terrain, very low temperatures.</li>
  <li>Some EGPWS installations use <strong>geometric altitude</strong> (from GPS), which reduces errors from wrong altimeter settings or non-standard temperatures.</li>
</ul>

<h2>Safe altitudes</h2>
<ul>
  <li>Make sure the right charts are on board and <strong>up to date</strong>. Use colour terrain contours when available.</li>
  <li>Study the minimum safe altitude information — MSA, MORA / grid MORA, minimum sector altitudes and minimum vectoring altitudes.</li>
  <li>Know and fly at or above the safe altitude for your area of operation.</li>
  <li><strong>Descend below the MSA only</strong> when established on a published instrument procedure, under radar control with an appropriate clearance, or when visual with the terrain.</li>
  <li>Know the height of the highest terrain or obstacle in the area and your position relative to it.</li>
</ul>

<h2>Cold temperatures</h2>
<p>In air colder than ISA, the aircraft is <strong>lower than the altimeter shows</strong>. Apply cold temperature corrections to minimum altitudes according to PANS-OPS and the company procedure — see Lesson 24 of the Cold Weather Operations course.</p>
""",
takeaways=["Know the units; read back and cross-check every altimeter setting.", "Cross-check radio and barometric altimeters.", "Use up-to-date charts; stay at or above MSA unless on a published procedure, under radar control or visual.", "In cold air you are lower than indicated — apply corrections."],
check=dict(q="When may you descend below the MSA?", options=["Whenever ATC is in contact", "When established on a published procedure, under radar control with clearance, or visual with terrain", "When the radio altimeter shows more than 1,000 ft", "When the GPS is serviceable"], answer=1,
           explain="Descent below MSA is only safe on a published procedure, under radar control with clearance, or when visual with the terrain."),
),

dict(title="ATC, Complacency and Crew Alertness", minutes=6,
objectives=["Challenge clearances that conflict with terrain awareness.", "Recognise complacency on familiar routes.", "Use briefings and callouts to keep terrain awareness."],
body="""
<h2>Working with ATC</h2>
<ul>
  <li><strong>You are responsible for terrain clearance</strong> — including when accepting an altitude clearance.</li>
  <li><strong>Challenge or refuse</strong> ATC instructions that are not clearly understood, are questionable, or conflict with your own assessment of the aircraft's position relative to terrain.</li>
  <li>Use standard phraseology and good radio discipline. Read back every clearance so that everyone agrees on its content.</li>
  <li>Do not accept unreasonable clearances, such as a descent that does not fit the terrain or the approach.</li>
  <li>Use the autopilot mode that makes compliance with the ATC instruction easiest and most visible.</li>
</ul>

<h2>Complacency</h2>
<ul>
  <li>Familiarity can lead to complacency. <strong>Do not assume this flight will be like the last one.</strong></li>
  <li>Keep a professional attitude, even at an aerodrome you know well.</li>
  <li>Brief the operational differences: NOTAMs, inoperative aids, a different runway, the weather.</li>
</ul>

<h2>Briefings and callouts</h2>
<ul>
  <li>Terrain awareness is a primary reason for briefings and callouts. Both pilots must share a common understanding of what to expect.</li>
  <li>Brief the MSA, the highest terrain, the approach and missed approach, and the escape route.</li>
  <li>Call out FMA and FMS changes, deviations from the path, and undesirable energy states.</li>
</ul>
<div class="callout warn"><span class="label">Warning</span><p>During an approach in IMC, fly the <strong>published IFR approach procedure only</strong>. Do not improvise.</p></div>
""",
takeaways=["The crew is responsible for terrain clearance — challenge doubtful clearances.", "Familiarity breeds complacency; brief the differences every time.", "Brief MSA, terrain and escape route; call out FMA changes and deviations."],
check=dict(q="ATC clears you to descend to an altitude below the MSA, but you are not yet established on the approach and are unsure of your position. What do you do?", options=["Descend as cleared", "Question the clearance and do not descend until your position and terrain clearance are confirmed", "Descend at a low rate", "Ask the cabin crew to look outside"], answer=1,
           explain="The crew is responsible for terrain clearance. Challenge any clearance that conflicts with your terrain awareness."),
),

dict(title="SOPs, Stabilised Approaches and CDFA", minutes=7,
objectives=["Apply stabilised approach criteria and the go-around policy.", "Fly non-precision approaches with the CDFA technique.", "Use the autoflight system to reduce CFIT risk."],
body="""
<h2>Standard operating procedures</h2>
<ul>
  <li>Do not invent your own procedures. Follow the company SOPs.</li>
  <li>Before the approach, know which approach and runway aids are available (NOTAMs, ATIS, pilot reports) and use all of them.</li>
  <li>Understand the approach, missed approach and departure procedures, and comply with them.</li>
</ul>

<h2>Stabilised approach</h2>
<p>Fly stabilised approaches. If the aircraft is not stabilised by <strong>1,000 ft above aerodrome elevation in IMC</strong> or <strong>500 ft in VMC</strong> (or the gates in your Operations Manual), <strong>go around</strong>. Domestic Airlines applies a no-fault go-around policy.</p>

<h2>Continuous descent final approach (CDFA)</h2>
""" + cdfa_diagram() + """
<ul>
  <li>EASA requires non-precision approaches to be flown with the <strong>CDFA</strong> technique unless otherwise approved (CAT.OP.MPA.115). The company presentations also call it <strong>CANPA</strong> (constant angle non-precision approach).</li>
  <li>The aircraft descends on a constant angle — typically about 3° — from the final approach fix to the runway, without levelling off at the MDA.</li>
  <li>At the decision point (DA/H or MDA/H with the add-on defined by the company), if the required visual references are not in sight, go around.</li>
  <li>Where available and trained, use the autoflight system — for example LNAV/VNAV or FPA modes — to fly the constant angle.</li>
</ul>

<h2>Automation</h2>
<ul>
  <li>Use automation appropriately to reduce workload and to fly stabilised approaches.</li>
  <li>Understand the autopilot modes. Monitor the FMA, and intervene manually if the aircraft does not do what is intended.</li>
  <li>Avoid excessive descent rates and low or high speeds at low altitude.</li>
</ul>
""",
takeaways=["Not stabilised by 1,000 ft IMC / 500 ft VMC (or company gates): go around.", "Non-precision approaches: CDFA (CANPA) — constant angle, no levelling at MDA.", "Know the autopilot modes; monitor the FMA; intervene if needed."],
check=dict(q="What is the main CFIT benefit of the CDFA technique?", options=["It saves fuel", "It avoids early step-downs and level flight close to terrain, keeping the approach stabilised", "It allows descent below the MDA", "It removes the need for a missed approach"], answer=1,
           explain="CDFA flies a constant angle like an ILS, avoiding the dive-and-drive profile that brings the aircraft low and level near terrain."),
),

dict(title="EGPWS / TAWS: Alerts and Crew Response", minutes=8,
objectives=["Describe the EGPWS basic modes and enhanced functions.", "Distinguish cautions from warnings.", "Apply the company response to EGPWS cautions."],
body="""
<h2>The system</h2>
<p>A terrain awareness warning system (TAWS) is required for commercial aeroplanes (ICAO Annex 6; EASA CAT.IDE.A.150). Our fleets use the <strong>Enhanced GPWS (EGPWS)</strong>, which combines the classic ground proximity modes with a <strong>terrain database</strong> and the aircraft position.</p>
<div class="table-wrap"><table>
<tr><th>Mode</th><th>Protects against</th><th>Typical alerts</th></tr>
<tr><td>1</td><td>Excessive descent rate</td><td>“SINK RATE”, “PULL UP”</td></tr>
<tr><td>2</td><td>Excessive terrain closure rate</td><td>“TERRAIN TERRAIN”, “PULL UP”</td></tr>
<tr><td>3</td><td>Altitude loss after take-off or go-around</td><td>“DON'T SINK”</td></tr>
<tr><td>4</td><td>Unsafe terrain clearance when not in landing configuration</td><td>“TOO LOW GEAR”, “TOO LOW FLAPS”, “TOO LOW TERRAIN”</td></tr>
<tr><td>5</td><td>Excessive deviation below the glideslope</td><td>“GLIDESLOPE”</td></tr>
<tr><td>6</td><td>Advisory callouts</td><td>Altitude callouts, “BANK ANGLE”</td></tr>
<tr><td>Enhanced</td><td>Terrain and obstacles ahead (look-ahead); terrain clearance floor near runways</td><td>“CAUTION TERRAIN”, “CAUTION OBSTACLE”, “TERRAIN AHEAD”, “TERRAIN AHEAD PULL UP”, “OBSTACLE PULL UP”, “TOO LOW TERRAIN”</td></tr>
</table></div>
<p class="muted">Alert wording varies with the installation — check the aircraft manuals.</p>
""" + lookahead_diagram() + """
<h2>Cautions and warnings</h2>
<ul>
  <li><strong>Caution</strong> (amber) — for example “SINK RATE”, “TERRAIN TERRAIN”, “DON'T SINK”, “TOO LOW FLAPS”, “TOO LOW GEAR”, “CAUTION TERRAIN”, “CAUTION OBSTACLE”, “BANK ANGLE”, “GLIDESLOPE”. <strong>Company SOP</strong>: the crew shall immediately assess the flight path or configuration with respect to the ground, and the PF shall take appropriate action to correct the situation. Q200 SOP: the PF verbalises the action to the PM with <strong>“CORRECTING”</strong>.</li>
  <li><strong>Warning</strong> (red) — for example “TOO LOW TERRAIN”, “TERRAIN PULL UP”, “OBSTACLE PULL UP” or “PULL UP” (“WHOOP WHOOP PULL UP”). <strong>Apply the escape manoeuvre immediately</strong> (Lesson 6).</li>
</ul>
<div class="callout warn"><span class="label">No delay</span><p>At night or in IMC, a warning must be followed <strong>without hesitation and without trying to confirm it visually</strong>. The Q200 SOP adds: “The flight crew must use a good judgment in this matter.” A warning should only ever be judged spurious in daylight VMC, with the terrain and obstacles clearly in sight and no doubt about the aircraft's position. Report every alert.</p></div>
""",
takeaways=["EGPWS = basic modes 1–6 plus terrain database look-ahead.", "Caution: assess the flight path and correct (“CORRECTING”).", "Warning (“PULL UP”, “TERRAIN AHEAD PULL UP”): escape manoeuvre immediately.", "At night or in IMC, never wait to confirm a warning visually."],
check=dict(q="At night in IMC you hear “TERRAIN AHEAD, PULL UP”. What do you do?", options=["Check the chart first", "Apply the escape manoeuvre immediately", "Reduce speed and level off", "Ask ATC to confirm terrain clearance"], answer=1,
           explain="A warning at night or in IMC requires the escape manoeuvre immediately, without trying to confirm it."),
),

dict(title="The Escape Manoeuvre — by Fleet", minutes=6,
objectives=["Apply the company EGPWS recovery procedure for your fleet.", "Explain the reasons for each step.", "Complete the recovery and inform ATC."],
body="""
<h2>Company procedures</h2>
""" + ESCAPE + """
<h2>Why each step matters</h2>
<ul>
  <li><strong>Maximum available power immediately</strong> — the climb gradient depends on excess thrust. Turboprops respond quickly; jets need several seconds to spool up.</li>
  <li><strong>Autopilot off, wings level</strong> — the lift vector must point up; a bank reduces the climb.</li>
  <li><strong>Pitch aggressively, respecting the stick shaker</strong> — the best climb gradient is obtained close to the stall warning. Do not exceed it.</li>
  <li><strong>Do not change the configuration</strong> during the escape unless your procedure says so. Retracting flaps or gear too early can reduce the climb capability.</li>
  <li><strong>The PM monitors</strong> radio altimeter and vertical speed and calls the trend — the PF concentrates on flying.</li>
  <li><strong>Continue</strong> until the warning stops and terrain clearance is assured, then level off, reconfigure and inform ATC.</li>
</ul>
<div class="callout"><span class="label">Practise it</span><p>The escape manoeuvre is a last resort. It is practised in the simulator during recurrent training — so that, if needed, it happens instinctively.</p></div>
""",
takeaways=["Q400: CHECK POWER → GA, AP off → power levers to detent → wings level, pitch aggressively (stick shaker) → NTOP, POWER SET → VGA.", "Q200: the same sequence with MTOP.", "B737-800: QRH Terrain Avoidance manoeuvre — a memory item.", "After the escape: level off, reconfigure, tell ATC “EGPWS recovery”."],
check=dict(q="During the Q400 EGPWS recovery, what does the PM confirm and call?", options=["“Gear up”", "NTOP on the engine display — “POWER SET”", "“Flaps zero”", "“Autopilot on”"], answer=1, explain="The PM confirms NTOP on the engine display and calls “POWER SET”."),
),

dict(title="Training Recommendations and Lessons from Accidents", minutes=7,
objectives=["Describe the CFIT ground and simulator training content.", "Learn from well-known CFIT accidents.", "Summarise the key CFIT prevention principles."],
body="""
<h2>Training</h2>
<p>The <strong>ground training</strong> builds the awareness to recognise and avoid CFIT situations. The <strong>simulator training</strong> applies that knowledge and develops proficiency in the escape manoeuvre. This training is given at initial and type training and repeated in recurrent training (at least every two years for the full programme).</p>
<p>Topics to review regularly:</p>
<ul>
  <li>avoiding excessive descent rates, and low or high speeds at low level;</li>
  <li>autopilot modes, FMA and FMS callouts, and manual intervention;</li>
  <li>barometric and radio altimetry; stabilised approach criteria; descent below MSA;</li>
  <li>the missed approach — especially when it appears likely — and go-around awareness;</li>
  <li>approach charts and en-route charts (including grid MORA);</li>
  <li>CRM and threat and error management briefings that highlight terrain.</li>
</ul>
<p>The simulator session should include LOFT into airports with high terrain, non-precision approaches with CDFA, circling and visual approaches, go-arounds (especially from circling), type-specific terrain escape manoeuvres, and emergency descents over mountainous terrain using escape routes.</p>

<h2>Lessons from accidents</h2>
<div class="table-wrap"><table>
<tr><th>Accident</th><th>What happened</th><th>Lesson</th></tr>
<tr><td><strong>Air Inter 148</strong><br>Airbus A320, Mont Sainte-Odile, France, January 1992</td><td>During a night approach in mountainous terrain the aircraft descended far more steeply than intended; a confusion between vertical speed and flight path angle modes was considered a likely factor. No GPWS was fitted. 87 people died.</td><td>Monitor the FMA and the vertical profile; cross-check altitude against distance.</td></tr>
<tr><td><strong>American Airlines 965</strong><br>Boeing 757, near Cali, Colombia, December 1995</td><td>During a rushed approach the crew entered a wrong navigation point in the FMS; the aircraft turned towards high terrain while descending. The GPWS escape was flown, but the speedbrakes were still extended. 159 people died.</td><td>Do not accept a rushed approach; verify FMS entries; in the escape, maximum performance — speedbrakes retracted.</td></tr>
<tr><td><strong>Korean Air 801</strong><br>Boeing 747, Guam, August 1997</td><td>At night, in rain, the crew flew a non-precision approach while the glideslope was out of service, and descended below the minimum altitude before reaching the step-down fix. 228 people died.</td><td>Brief inoperative aids; respect step-down altitudes and MDA; use CDFA.</td></tr>
</table></div>

<h2>Conclusion</h2>
<ul>
  <li>Adhere to the company SOPs at all times — and understand why.</li>
  <li>Know your horizontal and vertical terrain clearance in every phase of flight.</li>
  <li>Respond immediately to EGPWS warnings.</li>
</ul>
""",
takeaways=["Ground training builds awareness; simulator training builds the escape manoeuvre.", "Air Inter 148, AA965 and KAL801: mode awareness, FMS checks, step-down discipline.", "SOPs, terrain awareness and immediate response to warnings prevent CFIT."],
check=dict(q="What extra lesson does the American Airlines 965 accident teach about the escape manoeuvre?", options=["Keep the autopilot engaged", "Make sure the speedbrakes are retracted for maximum climb performance", "Extend the flaps", "Climb only to the MSA"], answer=1,
           explain="During the AA965 escape the speedbrakes remained extended, reducing climb performance."),
),
]


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


QUESTIONS = [
Q(1, "Which statement defines CFIT?", ["An aircraft out of control strikes the ground", "An airworthy aircraft under crew control is inadvertently flown into terrain, water or an obstacle", "A runway excursion on landing", "A collision with another aircraft"], 1, "CFIT involves an airworthy aircraft under control, unaware of the terrain."),
Q(1, "Most CFIT accidents occur:", ["In cruise", "During approach and landing", "During taxi", "During take-off"], 1, "Approach and landing, often non-precision approaches."),
Q(1, "Loss of situational awareness in CFIT is most often in which plane?", ["Lateral", "Vertical", "Longitudinal", "Temporal"], 1, "CFIT accidents often involve loss of vertical situational awareness."),
Q(2, "Why must you read back the altimeter setting in full?", ["It is polite", "To avoid confusions such as 1013 hPa and 29.92 inHg, or wrong digits", "To save time", "To test the radio"], 1, "Full read-back catches unit and digit errors."),
Q(2, "In air much colder than ISA, the aircraft is:", ["Higher than indicated", "Lower than indicated", "At the indicated altitude", "Unaffected"], 1, "In cold air true altitude is lower than indicated."),
Q(2, "What does grid MORA provide?", ["Minimum off-route altitude with terrain clearance within a grid area", "Maximum operating altitude", "Missed approach altitude", "Minimum radar altitude only"], 0, "Grid MORA gives terrain clearance within each grid square."),
Q(3, "Who is responsible for terrain clearance when you accept an ATC altitude clearance?", ["ATC only", "The flight crew", "The dispatcher", "The aerodrome operator"], 1, "The crew remains responsible for terrain clearance."),
Q(3, "How can complacency at a familiar aerodrome be countered?", ["Skip the briefing", "Brief the operational differences and follow SOPs every time", "Fly faster", "Use visual approaches only"], 1, "Brief differences and adhere to SOPs."),
Q(4, "If not stabilised by 1,000 ft above aerodrome elevation in IMC, you must:", ["Continue and correct", "Go around", "Request a visual approach", "Extend speedbrakes"], 1, "Unstabilised at the gate: go around."),
Q(4, "What does CDFA stand for?", ["Constant direction final approach", "Continuous descent final approach", "Controlled descent flight altitude", "Corrected decision final altitude"], 1, "Continuous descent final approach — also called CANPA."),
Q(4, "Which EASA rule requires CDFA for non-precision approaches?", ["CAT.OP.MPA.115", "SPA.RVSM.100", "ORO.FTL.210", "CAT.IDE.A.150"], 0, "CAT.OP.MPA.115 covers the approach flight technique (CDFA)."),
Q(5, "Which EGPWS mode protects against an unsafe terrain clearance when not in landing configuration?", ["Mode 1", "Mode 3", "Mode 4", "Mode 6"], 2, "Mode 4: TOO LOW GEAR / TOO LOW FLAPS / TOO LOW TERRAIN."),
Q(5, "What does the EGPWS enhanced look-ahead function use?", ["Only the radio altimeter", "A terrain database and the aircraft position", "ATC radar", "The weather radar"], 1, "It compares the predicted path with a terrain database."),
Q(5, "According to the company SOP, what does the crew do after an EGPWS caution such as “SINK RATE”?", ["Escape manoeuvre", "Immediately assess flight path and configuration; PF corrects (“CORRECTING”)", "Ignore it below 500 ft", "Switch off the EGPWS"], 1, "Cautions require immediate assessment and correction."),
Q(5, "At night in IMC, an EGPWS warning should be:", ["Confirmed visually first", "Followed immediately with the escape manoeuvre", "Reported only", "Ignored if the GPS is accurate"], 1, "Never delay the escape at night or in IMC."),
Q(6, "In the Q400 EGPWS recovery, what does the PF call first?", ["“GO AROUND”", "“CHECK POWER”", "“PULL UP”", "“ESCAPE”"], 1, "The PF calls “CHECK POWER”."),
Q(6, "To which power setting does the Q200 PF advance the power levers in the EGPWS recovery?", ["NTOP", "MTOP", "Flight idle", "MCP"], 1, "The Q200 SOP specifies MTOP."),
Q(6, "What speed does the PF target during the Dash 8 EGPWS recovery?", ["VREF", "VGA", "V2 + 20", "VMO"], 1, "The PF targets VGA."),
Q(6, "Why must the stick shaker be respected during the escape?", ["It disconnects the autopilot", "The best climb gradient is near, but not beyond, the stall warning", "It retracts the flaps", "It is required by ATC"], 1, "Pitch for maximum climb without stalling."),
Q(7, "Which accident involved a likely confusion between vertical speed and flight path angle modes?", ["Korean Air 801", "Air Inter 148", "American Airlines 965", "Air Florida 90"], 1, "Air Inter 148 (A320, 1992)."),
]

COURSE = dict(
    slug="cfit-egpws-refresher",
    title="CFIT and EGPWS Refresher",
    header_title="CFIT and EGPWS Refresher",
    tagline="Controlled flight into terrain: altimetry, safe altitudes, stabilised approaches and CDFA, EGPWS alerts and the escape manoeuvre for each fleet.",
    purpose="Refresh flight crew knowledge of CFIT prevention and EGPWS (TAWS) procedures, in line with ICAO Annex 6 and PANS-OPS, EASA CAT.IDE.A.150 and CAT.OP.MPA.115, and the company SOPs.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Define CFIT and its contributing factors", "Apply altimeter, safe altitude and chart procedures", "Challenge clearances and manage complacency",
                "Fly stabilised approaches and CDFA", "Respond correctly to EGPWS cautions and warnings", "Apply the escape manoeuvre for your fleet"],
    icon="search", cert_prefix="CFIT", quiz_count=10, pass_mark=80,
    group="refresher", season="Summer",
    finale=None,
    modules=[dict(title="CFIT Awareness and Prevention", summary="Definition, altimetry, safe altitudes, ATC, complacency, SOPs and CDFA", icon="search", lessons=range(1, 5)),
             dict(title="EGPWS and the Escape Manoeuvre", summary="Alerts, crew response, fleet escape procedures, training and accidents", icon="plane", lessons=range(5, 8))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner on approach towards mountains in poor visibility", "Most CFIT accidents happen on approach — often on non-precision approaches."),
            2: ("gen", "Flight deck with the attitude indicator and mountains ahead", "Know the altimeter setting, the safe altitude and the terrain around you."),
            3: ("gen", "Two pilots on the flight deck at dusk", "Challenge clearances that do not fit your terrain picture."),
            4: ("gen", "Airliner on a constant-angle approach to a runway", "CDFA: one constant angle to the runway."),
            5: ("gen", "Night flight deck with terrain ahead", "At night or in IMC, follow an EGPWS warning immediately."),
            6: ("gen", "Airliner climbing steeply away from high terrain", "The escape manoeuvre: maximum power, wings level, pitch to the stick shaker."),
            7: ("gen", "Airliner climbing over mountains at sunset", "Every CFIT lesson was learned the hard way.")},
)
