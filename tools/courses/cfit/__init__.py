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


def architecture_diagram():
    ins = ["Radio altimeter", "Air data: altitude, speed, vertical speed", "Inertial / AHRS: attitude, track", "GNSS position",
           "ILS glideslope deviation", "Gear and flap position", "Terrain, obstacle and runway database"]
    rows = "".join(f'<rect x="20" y="{30+i*40}" width="250" height="30" rx="6" fill="#eef3f0" stroke="{LINE}"/>'
                   f'<text x="32" y="{50+i*40}">{t}</text><path d="M270 {45+i*40} L330 165" stroke="{MUTED}" stroke-width="1.5" fill="none"/>' for i, t in enumerate(ins))
    outs = [("Aural alerts", "“PULL UP”, “TERRAIN” …"), ("Caution / warning lights", "amber / red"), ("Terrain display", "on ND / MFD")]
    orows = "".join(f'<path d="M470 165 L505 {70+i*90}" stroke="{MUTED}" stroke-width="1.5" fill="none"/><rect x="505" y="{50+i*90}" width="185" height="44" rx="6" fill="#fff" stroke="{GREEN}"/>'
                    f'<text x="515" y="{68+i*90}" font-weight="700">{a}</text><text x="515" y="{86+i*90}" fill="{MUTED}">{b}</text>' for i, (a, b) in enumerate(outs))
    svg = rows + f'<rect x="330" y="120" width="140" height="90" rx="10" fill="{GREEN}"/><text x="400" y="160" text-anchor="middle" fill="#fff" font-weight="700" font-size="15">EGPWS</text><text x="400" y="180" text-anchor="middle" fill="#fff">computer</text>' + orows
    return f"""<figure class="diagram"><svg viewBox="0 0 700 320" role="img" aria-label="EGPWS inputs and outputs"><title>EGPWS architecture</title>
<desc>Inputs from the radio altimeter, air data, inertial reference, GNSS, glideslope, configuration and the terrain database feed the EGPWS computer, which drives aural alerts, lights and the terrain display.</desc>
<g {FONT} font-size="12.5" fill="{INK}">{svg}</g></svg>
<figcaption>What the EGPWS uses and what it gives the crew. A wrong input (for example a faulty radio altimeter or a poor GNSS position) degrades the alerts — this is why some failures have MEL and QRH procedures.</figcaption></figure>"""


def display_diagram():
    bands = [("#c62828", "Solid red: terrain WARNING area", 1), ("#d32f2f", "Red dots (high density): more than 2,000 ft above you", 1),
             ("#f9a825", "Solid yellow: terrain CAUTION area", 1), ("#fbc02d", "Yellow dots (high density): 1,000–2,000 ft above you", 1),
             ("#fdd835", "Yellow dots (low density): 500 ft below* to 1,000 ft above", 1), ("#4caf50", "Green dots (medium density): 500–1,000 ft below you", 1),
             ("#66bb6a", "Green dots (low density): 1,000–2,000 ft below you", 1), ("#000", "Black: more than 2,000 ft below you", 1), ("#e040fb", "Magenta dots (high density): no terrain data", 1)]
    def sw(i, c, t, o):
        y = 24 + i * 31
        if "dots" in t:
            dens = 4 if "high" in t else 7
            dots = "".join(f'<circle cx="{303 + dx}" cy="{y + 3 + dy}" r="1.6" fill="{c}"/>' for dx in range(0, 24, dens) for dy in range(0, 20, dens))
            box = f'<rect x="300" y="{y}" width="26" height="22" rx="3" fill="#0b0f14"/>' + f'<g opacity="{o}">{dots}</g>'
        else:
            box = f'<rect x="300" y="{y}" width="26" height="22" rx="3" fill="{c}" opacity="{o}" stroke="#999" stroke-width=".5"/>'
        return box + f'<text x="336" y="{y + 16}">{t}</text>'
    rows = "".join(sw(i, c, t, o) for i, (c, t, o) in enumerate(bands))
    nd = (f'<rect x="20" y="20" width="250" height="280" rx="12" fill="#0b0f14"/><path d="M40 270 A110 110 0 0 1 250 270" stroke="#fff" stroke-width="1.5" fill="none" opacity=".7"/>'
          f'<g opacity=".95"><circle cx="90" cy="150" r="26" fill="#2e7d32" opacity=".6"/><circle cx="200" cy="120" r="32" fill="#fbc02d" opacity=".7"/>'
          f'<circle cx="210" cy="110" r="14" fill="#d32f2f"/><circle cx="120" cy="90" r="20" fill="#66bb6a" opacity=".5"/><rect x="170" y="190" width="40" height="22" fill="#f9a825"/></g>'
          f'<path d="M145 285 l-10 -22 h20z" fill="#fff"/><text x="145" y="40" text-anchor="middle" fill="#fff" font-size="11">TERR</text>')
    svg = nd + rows
    return f"""<figure class="diagram"><svg viewBox="0 0 700 320" role="img" aria-label="Terrain display colours"><title>EGPWS terrain display colours</title>
<desc>The terrain display uses red, yellow, green, black and magenta, with dot density showing terrain height relative to the aircraft. Solid yellow and solid red show caution and warning areas.</desc>
<g {FONT} font-size="12" fill="{INK}">{rows}</g><g {FONT}>{nd}</g></svg>
<figcaption>* 250 ft below with the gear down. Typical EGPWS terrain colours: the colour depends on terrain height <strong>relative to the aircraft</strong>, not on absolute elevation. Some installations add a “peaks” mode or cyan for water — check your FCOM / AOM.</figcaption></figure>"""


def modes_diagram():
    def panel(x, y, title, alert, path, terrain, extra=""):
        return (f'<g transform="translate({x},{y})"><rect width="215" height="135" rx="8" fill="#f6f8f7" stroke="{LINE}"/>'
                f'<text x="10" y="20" font-weight="700">{title}</text><text x="10" y="38" fill="{RED}" font-weight="700">{alert}</text>'
                f'<path d="{terrain}" fill="#7a9a83"/>{extra}<path d="{path}" stroke="{BLUE}" stroke-width="3" fill="none" marker-end="url(#ah)"/></g>')
    flat = "M0 135 L0 118 L215 118 L215 135z"
    svg = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#1f5fa8"/></marker></defs>'
           + panel(10, 10, "Mode 1 — descent rate", "SINK RATE · PULL UP", "M20 50 L150 108", flat)
           + panel(242, 10, "Mode 2 — terrain closure", "TERRAIN TERRAIN · PULL UP", "M15 70 L190 72", "M0 135 L0 118 L110 118 L170 70 L215 80 L215 135z")
           + panel(474, 10, "Mode 3 — loss after take-off", "DON'T SINK", "M15 110 L90 60 L180 80", flat)
           + panel(10, 165, "Mode 4 — too low, not configured", "TOO LOW GEAR / FLAPS", "M15 70 L190 100", flat)
           + panel(242, 165, "Mode 5 — below glideslope", "GLIDESLOPE", "M15 55 L190 108", flat, '<path d="M15 45 L200 100" stroke="#2e7d32" stroke-width="2" stroke-dasharray="6 4" fill="none"/><text x="120" y="64" fill="#2e7d32" font-size="11">glideslope</text>')
           + panel(474, 165, "Mode 6 callouts · Mode 7", "BANK ANGLE · WINDSHEAR", "M20 60 L120 85 L195 75", flat))
    return f"""<figure class="diagram"><svg viewBox="0 0 700 320" role="img" aria-label="EGPWS basic modes"><title>EGPWS basic modes 1 to 7</title>
<desc>Six panels show the situations that trigger each basic mode: excessive descent rate, excessive terrain closure, altitude loss after take-off, too low when not configured, below glideslope, and callouts, bank angle and windshear.</desc>
<g {FONT} font-size="12" fill="{INK}">{svg}</g></svg>
<figcaption>The basic modes use the radio altimeter and aircraft data — they work even without the terrain database, but they cannot see a steep slope ahead. The enhanced look-ahead function covers that (Lesson 7).</figcaption></figure>"""


ESCAPE = """
<div class="table-wrap"><table>
<tr><th>Fleet</th><th>Pilot flying</th><th>Pilot monitoring</th></tr>
<tr><td><strong>Dash 8-Q400</strong><br><span class="muted">Company SOP, EGPWS Recovery (Rev 02)</span></td>
<td>Calls <strong>“CHECK POWER”</strong>. Selects <strong>GA</strong> and disconnects the autopilot. Advances the power levers <strong>to the detent</strong>, rolls wings level and pitches aggressively to initiate the climb, respecting the stick shaker. Targets <strong>V<sub>GA</sub></strong>.<br>Once clear of terrain: establishes level flight and reconfigures the aircraft.</td>
<td>Confirms <strong>NTOP</strong> on the engine display and calls <strong>“POWER SET”</strong>. Monitors radio altimeter and vertical speed and informs the PF of performance and terrain clearance.<br>Once clear: advises ATC — “(call sign) EGPWS recovery, new altitude / flight level …”.</td></tr>
<tr><td><strong>Dash 8-Q200</strong><br><span class="muted">Company SOP, Table 25 EGPWS recovery</span></td>
<td>Calls <strong>“CHECK POWER”</strong>. Selects <strong>GA</strong> and disconnects the AP. Advances the power levers to <strong>MTOP</strong>, rolls wings level and pitches aggressively to initiate the climb, responding to the stick shaker. Targets <strong>V<sub>GA</sub></strong>.<br>Once clear: establishes level flight and configures the aircraft.</td>
<td>Confirms <strong>MTOP</strong> and calls <strong>“POWER SET”</strong>. Monitors radio altimeter and vertical speed and informs the PF of performance and terrain clearance.<br>Once clear: advises ATC of the EGPWS recovery and new altitude or flight level.</td></tr>
<tr><td><strong>Boeing 737-800</strong><br><span class="muted">Boeing QRH / FCTM — check against your current QRH</span></td>
<td><strong>Terrain Avoidance</strong> (QRH Non-Normal Manoeuvres, memory item): disconnect the <strong>autopilot</strong> and <strong>autothrottle</strong>; aggressively apply <strong>maximum thrust</strong>; simultaneously roll <strong>wings level</strong> and rotate to an initial pitch attitude of <strong>20°</strong>; <strong>retract the speedbrakes</strong>; if terrain remains a threat, continue rotation up to the pitch limit indicator or stick shaker; <strong>do not change gear or flap configuration</strong> until terrain separation is assured. When clear: slowly decrease pitch and accelerate.</td>
<td>Assures <strong>maximum thrust</strong>; verifies all required actions are completed and calls out any omissions; calls out the <strong>radio altitude trend</strong> (increasing or decreasing). When clear: advises ATC.</td></tr>
</table></div>"""

LESSONS = [
dict(title="CFIT: Definition, Defences and Contributing Factors", minutes=8,
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

dict(title="Altimeters, Safe Altitudes and Charts", minutes=10,
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
<div class="callout info"><span class="label">Rule of thumb</span><p>The error is about <strong>4 % of the height above the altimeter-setting source for every 10 °C below ISA</strong>. Example: aerodrome temperature −20 °C at sea level is 35 °C below ISA, so at 3,000 ft above the aerodrome the aircraft can be about 3,000 × 4 % × 3.5 ≈ <strong>420 ft lower</strong> than indicated. Use the PANS-OPS / company correction table for the actual values.</p></div>
""",
takeaways=["Know the units; read back and cross-check every altimeter setting.", "Cross-check radio and barometric altimeters.", "Use up-to-date charts; stay at or above MSA unless on a published procedure, under radar control or visual.", "In cold air you are lower than indicated — apply corrections."],
check=dict(q="When may you descend below the MSA?", options=["Whenever ATC is in contact", "When established on a published procedure, under radar control with clearance, or visual with terrain", "When the radio altimeter shows more than 1,000 ft", "When the GPS is serviceable"], answer=1,
           explain="Descent below MSA is only safe on a published procedure, under radar control with clearance, or when visual with the terrain."),
),

dict(title="ATC, Complacency and Crew Alertness", minutes=8,
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

dict(title="SOPs, Stabilised Approaches and CDFA", minutes=9,
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

dict(title="EGPWS / TAWS: The System and the Terrain Display", minutes=10,
objectives=["Explain why TAWS is required and what the EGPWS adds to the classic GPWS.", "List the EGPWS inputs and the effect of a wrong input.", "Read the terrain display and use the inhibit switches correctly."],
body="""
<h2>Why TAWS</h2>
<p>ICAO Annex 6 and EASA <strong>CAT.IDE.A.150</strong> require a terrain awareness warning system (TAWS) on commercial aeroplanes. The first generation, the <strong>GPWS</strong>, looked only <em>down</em> with the radio altimeter: it could not warn of a steep slope ahead in time. The <strong>Enhanced GPWS (EGPWS)</strong> adds a worldwide <strong>terrain, obstacle and runway database</strong> and the aircraft position, so it can look <strong>ahead</strong> of the aircraft. Since EGPWS became mandatory, CFIT accidents with a working, correctly used system have become very rare.</p>
""" + architecture_diagram() + """
<h2>Position and altitude</h2>
<ul>
  <li>The look-ahead function depends on an accurate <strong>position</strong> (GNSS, or FMS position) and a valid, current <strong>database</strong>.</li>
  <li>Many installations compute a <strong>geometric altitude</strong> from GNSS, barometric and radio altitude. It reduces errors from a wrong altimeter setting or very cold temperatures.</li>
  <li>A position error, an out-of-date database or an aerodrome not in the database can cause <strong>nuisance alerts</strong> — or <strong>missed alerts</strong>. Report every nuisance alert so that the database can be checked.</li>
</ul>

<h2>The terrain display</h2>
""" + display_diagram() + """
<ul>
  <li>Select the terrain display in the climb and descent, especially near high terrain — it gives the picture <strong>before</strong> any alert.</li>
  <li>When a look-ahead caution or warning is triggered, the display usually pops up automatically and the threatening terrain is shown in <strong>solid yellow</strong> (caution) or <strong>solid red</strong> (warning).</li>
  <li>The terrain display is <strong>not for navigation</strong>: never use it to manoeuvre around terrain in IMC.</li>
</ul>

<h2>Inhibits, failures and the MEL</h2>
<ul>
  <li>Typical controls: a <strong>flap override / flap inhibit</strong> (landing with less than landing flaps, per the QRH), a <strong>gear override</strong>, a <strong>terrain inhibit</strong> (look-ahead off, for example when position is unreliable — only when the QRH or the company procedure says so) and a <strong>glideslope cancel</strong>.</li>
  <li>Never inhibit a function to silence an alert you do not understand.</li>
  <li>An EGPWS failure or a terrain function failure is shown on the flight deck; dispatch is only possible within the <strong>MEL</strong> limits, and the crew must brief the lost protection.</li>
</ul>
<p class="muted">Switch names and locations differ between the B737-800, Q400 and Q200 — check the FCOM / AOM of your fleet.</p>
""",
takeaways=["TAWS is mandatory; EGPWS adds a terrain database and look-ahead to the classic GPWS.", "Wrong position, database or radio altimeter input = wrong or missed alerts.", "Terrain colours show height relative to the aircraft; solid yellow = caution, solid red = warning.", "Inhibit switches only as the QRH or company procedure says; EGPWS failures per MEL."],
check=dict(q="On the terrain display, what does high-density red show?", options=["Terrain below the aircraft", "Terrain more than 2,000 ft above the aircraft", "Water", "Terrain with no database"], answer=1, explain="Red dots show terrain more than about 2,000 ft above the aircraft altitude; solid red marks a warning area."),
),

dict(title="EGPWS Basic Modes 1 to 7", minutes=12,
objectives=["Describe what each basic mode protects against.", "Recognise the aural alert of each mode.", "Know which alerts are cautions and which are warnings."],
body="""
<h2>The basic modes</h2>
<p>The basic modes compare the radio altitude, the barometric descent rate, the configuration and the glideslope with envelopes. They work without the terrain database — but they react to the terrain <strong>below</strong>, so their warning time is short.</p>
""" + modes_diagram() + """
<div class="table-wrap"><table>
<tr><th>Mode</th><th>Protects against</th><th>Caution</th><th>Warning</th><th>Active</th></tr>
<tr><td class="code">1</td><td>Excessive <strong>descent rate</strong> for the height above terrain</td><td>“SINK RATE”</td><td>“PULL UP”</td><td>All phases, close to the ground</td></tr>
<tr><td class="code">2</td><td>Excessive <strong>closure rate</strong> with rising terrain</td><td>“TERRAIN TERRAIN”</td><td>“PULL UP”</td><td>Mainly when not in landing configuration (2A); reduced envelope in landing configuration (2B)</td></tr>
<tr><td class="code">3</td><td><strong>Altitude loss</strong> after take-off or go-around</td><td>“DON'T SINK”</td><td>—</td><td>Climb after take-off or go-around</td></tr>
<tr><td class="code">4</td><td><strong>Unsafe terrain clearance</strong> when not in landing configuration</td><td>“TOO LOW GEAR”, “TOO LOW FLAPS”, “TOO LOW TERRAIN”</td><td>—</td><td>4A gear up, 4B flaps not in landing position, 4C after take-off</td></tr>
<tr><td class="code">5</td><td>Excessive deviation <strong>below the glideslope</strong></td><td>“GLIDESLOPE” (louder as the deviation grows)</td><td>—</td><td>ILS approach, at low height; can be cancelled</td></tr>
<tr><td class="code">6</td><td><strong>Advisory callouts</strong></td><td>Altitude callouts, “MINIMUMS”, “BANK ANGLE”</td><td>—</td><td>As configured for the fleet</td></tr>
<tr><td class="code">7</td><td><strong>Windshear</strong> (reactive), where installed</td><td>Windshear caution</td><td>“WINDSHEAR WINDSHEAR WINDSHEAR”</td><td>Take-off and approach, at low height</td></tr>
</table></div>
<p class="muted">Envelopes, heights and exact wording depend on the installation and the fleet. Predictive windshear (weather radar, B737-800) is a separate system — see the Windshear course.</p>

<h2>How to react</h2>
<ul>
  <li><strong>Mode 1 “SINK RATE”</strong> — reduce the descent rate now. If “PULL UP” follows, escape manoeuvre.</li>
  <li><strong>Mode 2 “TERRAIN TERRAIN”</strong> — you are closing with terrain: check position, altitude and the terrain display; climb if in doubt. “PULL UP”: escape manoeuvre.</li>
  <li><strong>Mode 3 “DON'T SINK”</strong> — stop the descent and re-establish the climb (often after a too early flap retraction or a thrust reduction).</li>
  <li><strong>Mode 4 “TOO LOW GEAR / FLAPS”</strong> — you are low and not configured: if this is not a planned non-normal landing, go around. “TOO LOW TERRAIN”: climb.</li>
  <li><strong>Mode 5 “GLIDESLOPE”</strong> — correct back to the glideslope; if not possible, go around.</li>
  <li><strong>Mode 7 “WINDSHEAR”</strong> — windshear escape manoeuvre (FCOM / AOM).</li>
</ul>
<div class="callout warn"><span class="label">Order of priority</span><p>When several alerts sound, the system gives priority to the most urgent — windshear and “PULL UP” first. The crew response follows the same order: a warning always means the escape manoeuvre (Lesson 8).</p></div>
""",
takeaways=["Mode 1 descent rate, 2 terrain closure, 3 loss after take-off, 4 too low not configured, 5 below glideslope, 6 callouts, 7 windshear.", "Basic modes look down; their warning time is short.", "Cautions: correct now. Warnings (“PULL UP”, “WINDSHEAR”): escape manoeuvre."],
check=dict(q="After take-off, the crew retracts the flaps too early and the aircraft starts to sink. Which alert is expected?", options=["“SINK RATE” (mode 1)", "“DON'T SINK” (mode 3)", "“GLIDESLOPE” (mode 5)", "“TOO LOW GEAR” (mode 4)"], answer=1, explain="Mode 3 warns of altitude loss after take-off or go-around: “DON'T SINK”."),
),

dict(title="Enhanced Functions and Crew Response", minutes=9,
objectives=["Describe the EGPWS look-ahead and terrain clearance floor functions.", "Distinguish cautions from warnings.", "Apply the company response to EGPWS cautions and warnings."],
body="""
<h2>Enhanced functions</h2>
<ul>
  <li><strong>Terrain look-ahead</strong> — compares the predicted flight path with the terrain and obstacle database: “CAUTION TERRAIN” / “TERRAIN AHEAD” first, then “TERRAIN AHEAD, PULL UP” / “PULL UP”. Obstacle versions: “CAUTION OBSTACLE”, “OBSTACLE AHEAD, PULL UP”.</li>
  <li><strong>Terrain clearance floor</strong> — a protection floor around each runway in the database: if the aircraft descends below it short of the runway, “TOO LOW TERRAIN”. It catches a “landing short” in a flat area where the basic modes stay silent.</li>
  <li>Some installations add a <strong>runway field clearance floor</strong> and “peaks” display modes.</li>
</ul>

""" + lookahead_diagram() + """
<h2>Cautions and warnings</h2>
<ul>
  <li><strong>Caution</strong> (amber) — for example “SINK RATE”, “TERRAIN TERRAIN”, “DON'T SINK”, “TOO LOW FLAPS”, “TOO LOW GEAR”, “CAUTION TERRAIN”, “CAUTION OBSTACLE”, “BANK ANGLE”, “GLIDESLOPE”. <strong>Company SOP</strong>: the crew shall immediately assess the flight path or configuration with respect to the ground, and the PF shall take appropriate action to correct the situation. Q200 SOP: the PF verbalises the action to the PM with <strong>“CORRECTING”</strong>.</li>
  <li><strong>Warning</strong> (red) — for example “TOO LOW TERRAIN”, “TERRAIN PULL UP”, “OBSTACLE PULL UP” or “PULL UP” (“WHOOP WHOOP PULL UP”). <strong>Apply the escape manoeuvre immediately</strong> (Lesson 8).</li>
</ul>
<div class="callout warn"><span class="label">No delay</span><p>At night or in IMC, a warning must be followed <strong>without hesitation and without trying to confirm it visually</strong>. The Q200 SOP adds: “The flight crew must use a good judgment in this matter.” A warning should only ever be judged spurious in daylight VMC, with the terrain and obstacles clearly in sight and no doubt about the aircraft's position. Report every alert.</p></div>
""",
takeaways=["Look-ahead: CAUTION TERRAIN first, then TERRAIN AHEAD PULL UP; terrain clearance floor protects short of the runway.", "Caution: assess the flight path and correct (“CORRECTING”).", "Warning (“PULL UP”, “TERRAIN AHEAD PULL UP”): escape manoeuvre immediately.", "At night or in IMC, never wait to confirm a warning visually."],
check=dict(q="At night in IMC you hear “TERRAIN AHEAD, PULL UP”. What do you do?", options=["Check the chart first", "Apply the escape manoeuvre immediately", "Reduce speed and level off", "Ask ATC to confirm terrain clearance"], answer=1,
           explain="A warning at night or in IMC requires the escape manoeuvre immediately, without trying to confirm it."),
),

dict(title="The Escape Manoeuvre — by Fleet", minutes=10,
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
takeaways=["Q400: CHECK POWER → GA, AP off → power levers to detent → wings level, pitch aggressively (stick shaker) → NTOP, POWER SET → VGA.", "Q200: the same sequence with MTOP.", "B737-800: A/P and A/T off, maximum thrust, wings level, pitch 20° (then PLI / stick shaker), speedbrakes retracted, no configuration change — a QRH memory item.", "After the escape: level off, reconfigure, tell ATC “EGPWS recovery”."],
check=dict(q="During the Q400 EGPWS recovery, what does the PM confirm and call?", options=["“Gear up”", "NTOP on the engine display — “POWER SET”", "“Flaps zero”", "“Autopilot on”"], answer=1, explain="The PM confirms NTOP on the engine display and calls “POWER SET”."),
),

dict(title="Training Recommendations and Lessons from Accidents", minutes=10,
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
Q(6, "Which EGPWS mode protects against an unsafe terrain clearance when not in landing configuration?", ["Mode 1", "Mode 3", "Mode 4", "Mode 6"], 2, "Mode 4: TOO LOW GEAR / TOO LOW FLAPS / TOO LOW TERRAIN."),
Q(7, "What does the EGPWS enhanced look-ahead function use?", ["Only the radio altimeter", "A terrain database and the aircraft position", "ATC radar", "The weather radar"], 1, "It compares the predicted path with a terrain database."),
Q(7, "According to the company SOP, what does the crew do after an EGPWS caution such as “SINK RATE”?", ["Escape manoeuvre", "Immediately assess flight path and configuration; PF corrects (“CORRECTING”)", "Ignore it below 500 ft", "Switch off the EGPWS"], 1, "Cautions require immediate assessment and correction."),
Q(7, "At night in IMC, an EGPWS warning should be:", ["Confirmed visually first", "Followed immediately with the escape manoeuvre", "Reported only", "Ignored if the GPS is accurate"], 1, "Never delay the escape at night or in IMC."),
Q(8, "In the Q400 EGPWS recovery, what does the PF call first?", ["“GO AROUND”", "“CHECK POWER”", "“PULL UP”", "“ESCAPE”"], 1, "The PF calls “CHECK POWER”."),
Q(8, "To which power setting does the Q200 PF advance the power levers in the EGPWS recovery?", ["NTOP", "MTOP", "Flight idle", "MCP"], 1, "The Q200 SOP specifies MTOP."),
Q(8, "What speed does the PF target during the Dash 8 EGPWS recovery?", ["VREF", "VGA", "V2 + 20", "VMO"], 1, "The PF targets VGA."),
Q(8, "Why must the stick shaker be respected during the escape?", ["It disconnects the autopilot", "The best climb gradient is near, but not beyond, the stall warning", "It retracts the flaps", "It is required by ATC"], 1, "Pitch for maximum climb without stalling."),
Q(9, "Which accident involved a likely confusion between vertical speed and flight path angle modes?", ["Korean Air 801", "Air Inter 148", "American Airlines 965", "Air Florida 90"], 1, "Air Inter 148 (A320, 1992)."),
Q(2, "Rule of thumb: how large is the cold temperature altimeter error?", ["About 1 % per 10 °C below ISA", "About 4 % of height above the source per 10 °C below ISA", "About 10 % per 1 °C", "There is no error below ISA"], 1, "About 4 % of the height above the altimeter-setting source for every 10 °C below ISA."),
Q(5, "What does the EGPWS add to the classic GPWS?", ["A louder horn", "A terrain, obstacle and runway database with the aircraft position, to look ahead", "Automatic pull-up", "A second radio altimeter"], 1, "The database and position allow a look-ahead function."),
Q(5, "What is the effect of a large position error on the EGPWS?", ["None", "Nuisance or missed look-ahead alerts", "It stops the basic modes", "It switches off the radio altimeter"], 1, "The look-ahead depends on accurate position: errors give false or missed alerts."),
Q(5, "May the terrain display be used to navigate around terrain in IMC?", ["Yes", "No — it is for awareness only", "Only below MSA", "Only with ATC approval"], 1, "The terrain display is not a navigation display."),
Q(5, "On the terrain display, what does a solid yellow area mean?", ["Water", "A look-ahead caution area", "Terrain far below", "No data"], 1, "Solid yellow marks a caution area; solid red a warning area."),
Q(6, "Which mode gives “SINK RATE” then “PULL UP”?", ["Mode 1", "Mode 3", "Mode 5", "Mode 6"], 0, "Mode 1: excessive descent rate."),
Q(6, "Which mode gives “TERRAIN TERRAIN” when rising terrain closes in?", ["Mode 1", "Mode 2", "Mode 4", "Mode 7"], 1, "Mode 2: excessive terrain closure rate."),
Q(6, "“DON'T SINK” comes from which mode?", ["Mode 2", "Mode 3", "Mode 5", "Mode 6"], 1, "Mode 3: altitude loss after take-off or go-around."),
Q(6, "What is the response to a mode 5 “GLIDESLOPE” alert?", ["Escape manoeuvre", "Correct back to the glideslope, or go around if not possible", "Ignore it", "Increase speed"], 1, "Correct the deviation; go around if it cannot be corrected."),
Q(7, "What does the terrain clearance floor function protect against?", ["Overspeed", "Descending below a floor around the runway short of the runway", "Tail strike", "Engine failure"], 1, "It warns “TOO LOW TERRAIN” if the aircraft descends below the floor near the runway."),
Q(8, "In the B737-800 terrain avoidance manoeuvre, what initial pitch attitude is targeted?", ["10°", "15°", "20°", "25°"], 2, "Roll wings level and rotate to an initial 20° pitch, then up to the PLI or stick shaker if needed."),
Q(8, "During the B737-800 escape, what must be done with the speedbrakes?", ["Leave them extended", "Retract them", "Extend them fully", "Arm them"], 1, "Retract the speedbrakes — the AA965 lesson."),
Q(8, "During the escape, when may the gear or flap configuration be changed?", ["Immediately", "Only when terrain separation is assured", "At 1,000 ft RA", "Never"], 1, "Do not change configuration until terrain separation is assured."),
]

COURSE = dict(
    slug="cfit-egpws-refresher",
    title="CFIT and EGPWS Refresher",
    header_title="CFIT and EGPWS Refresher",
    tagline="Controlled flight into terrain: altimetry, safe altitudes, stabilised approaches and CDFA, the EGPWS system, terrain display and modes 1–7, and the escape manoeuvre for each fleet.",
    purpose="Refresh flight crew knowledge of CFIT prevention and EGPWS (TAWS) procedures, in line with ICAO Annex 6 and PANS-OPS, EASA CAT.IDE.A.150 and CAT.OP.MPA.115, and the company SOPs.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Define CFIT and its contributing factors", "Apply altimeter, safe altitude and chart procedures", "Challenge clearances and manage complacency",
                "Fly stabilised approaches and CDFA", "Explain the EGPWS system, terrain display and basic modes 1–7", "Respond correctly to EGPWS cautions and warnings", "Apply the escape manoeuvre for your fleet"],
    icon="search", cert_prefix="CFIT", quiz_count=15, pass_mark=80,
    group="refresher", season="Summer",
    finale=None,
    modules=[dict(title="CFIT Awareness and Prevention", summary="Definition, altimetry, safe altitudes, ATC, complacency, SOPs and CDFA", icon="search", lessons=range(1, 5)),
             dict(title="EGPWS / TAWS", summary="System, terrain display, basic modes 1–7, enhanced functions and crew response", icon="plane", lessons=range(5, 8)),
             dict(title="Escape Manoeuvre and Lessons Learned", summary="Escape manoeuvre for each fleet, training and accident case studies", icon="plane", lessons=range(8, 10))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner on approach towards mountains in poor visibility", "Most CFIT accidents happen on approach — often on non-precision approaches."),
            2: ("gen", "Flight deck with the attitude indicator and mountains ahead", "Know the altimeter setting, the safe altitude and the terrain around you."),
            3: ("gen", "Two pilots on the flight deck at dusk", "Challenge clearances that do not fit your terrain picture."),
            4: ("gen", "Airliner on a constant-angle approach to a runway", "CDFA: one constant angle to the runway."),
            5: ("gen", "Flight deck at dusk with mountains ahead", "The EGPWS looks ahead using a terrain database and the aircraft position."),
            6: ("gen", "Airliner descending towards rising terrain", "The basic modes watch the terrain below the aircraft."),
            7: ("gen", "Night flight deck with terrain ahead", "At night or in IMC, follow an EGPWS warning immediately."),
            8: ("gen", "Airliner climbing steeply away from high terrain", "The escape manoeuvre: maximum power, wings level, pitch for the best climb."),
            9: ("gen", "Airliner climbing over mountains at sunset", "Every CFIT lesson was learned the hard way.")},
)
