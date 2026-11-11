# Cold Weather Operations — lessons 11–20

RUNWAY_SVG = """
<figure class="diagram">
<svg viewBox="0 0 640 210" role="img" aria-labelledby="rw-t rw-d">
  <title id="rw-t">Runway divided into thirds with a runway condition code for each third</title>
  <desc id="rw-d">Runway 09 is divided into three thirds reported in the direction of the lower runway designator. Example codes 5, 5 and 2: the last third has slush 6 millimetres deep.</desc>
  <g font-family="system-ui,Segoe UI,Arial,sans-serif" font-size="13" fill="#24342b">
    <rect x="20" y="60" width="600" height="80" rx="4" fill="#3b4540"/>
    <rect x="220" y="60" width="2" height="80" fill="#fff" opacity=".7"/>
    <rect x="420" y="60" width="2" height="80" fill="#fff" opacity=".7"/>
    <g fill="#fff"><rect x="40" y="97" width="30" height="6"/><rect x="100" y="97" width="30" height="6"/><rect x="160" y="97" width="30" height="6"/><rect x="250" y="97" width="30" height="6"/><rect x="310" y="97" width="30" height="6"/><rect x="370" y="97" width="30" height="6"/><rect x="450" y="97" width="30" height="6"/><rect x="510" y="97" width="30" height="6"/><rect x="570" y="97" width="30" height="6"/></g>
    <rect x="422" y="60" width="198" height="80" fill="#9cc3d9" opacity=".55"/>
    <text x="30" y="52" font-weight="700">RWY 09 →</text>
    <text x="120" y="34" text-anchor="middle" font-weight="700">First third</text>
    <text x="320" y="34" text-anchor="middle" font-weight="700">Second third</text>
    <text x="520" y="34" text-anchor="middle" font-weight="700">Third third</text>
    <circle cx="120" cy="170" r="17" fill="#1d7a3e"/><text x="120" y="176" text-anchor="middle" fill="#fff" font-weight="800" font-size="17">5</text>
    <circle cx="320" cy="170" r="17" fill="#1d7a3e"/><text x="320" y="176" text-anchor="middle" fill="#fff" font-weight="800" font-size="17">5</text>
    <circle cx="520" cy="170" r="17" fill="#c76a00"/><text x="520" y="176" text-anchor="middle" fill="#fff" font-weight="800" font-size="17">2</text>
    <text x="150" y="175">WET</text><text x="350" y="175">WET</text><text x="550" y="175">SLUSH 6 mm</text>
  </g>
</svg>
<figcaption>Example report <code>5/5/2</code>: runway condition codes for each third, given in the direction of the lower runway designator.</figcaption>
</figure>
"""

LESSONS_B = [
# ---------------------------------------------------------------- 11
dict(
title="Gate and Remote De-icing Operations",
minutes=7,
objectives=[
  "Compare gate de-icing with remote (pad) de-icing.",
  "Describe a typical remote de-icing pad procedure.",
  "Manage the time between treatment and take-off.",
],
body="""
<h2>Two ways to de-ice</h2>
<div class="table-wrap"><table>
  <tr><th></th><th>At the gate / stand</th><th>Remote pad or central facility</th></tr>
  <tr><td>Engines</td><td>Normally shut down; APU running</td><td>Normally running at idle (per AFM and facility procedure)</td></tr>
  <tr><td>Distance to runway</td><td>Longer taxi — more holdover time used before take-off</td><td>Close to the departure runway — less holdover time used</td></tr>
  <tr><td>Communication</td><td>Ground crew via interphone or radio</td><td>Pad control / de-icing coordinator by radio, then the vehicle operator</td></tr>
  <tr><td>Main risks</td><td>HOT running out during pushback and taxi</td><td>Wrong position on the pad, engines near personnel, confusion between ATC, pad control and the de-icing crew</td></tr>
</table></div>

<h2>A typical remote pad procedure</h2>
<ol class="steps">
  <li>Before taxi, check the airport de-icing procedures (charts, NOTAMs, frequencies) and brief the sequence.</li>
  <li>ATC or the coordinator assigns a pad. Taxi in following the lead-in line and marshaller or stop-position signs, and stop on the stop line.</li>
  <li>Set the parking brake and configure the aircraft for de-icing. Report "configured" on the pad frequency.</li>
  <li>Agree the treatment and receive the start call. Hold position — no movement, power or configuration change.</li>
  <li>Receive the anti-icing code and the "all personnel and equipment clear" call.</li>
  <li>Only then reconfigure, complete the after de-icing checks, and contact ATC to leave the pad as instructed.</li>
</ol>

<h2>Managing the time to take-off</h2>
<ul>
  <li>Coordinate with ATC before treatment so that you are not de-iced and then held for a long time.</li>
  <li>Taxi at a safe speed with good separation. Avoid the jet blast of the aircraft ahead, which blows snow and slush onto treated surfaces and thins the fluid.</li>
  <li>Some AFMs recommend delaying flap extension until close to the runway when taxiing through slush or snow. Others require flaps to be set before anti-icing so that the surfaces are protected. Follow your FCOM.</li>
  <li>Continuously compare the remaining holdover time with the expected take-off time. If it will not be enough, decide early — a planned return for re-treatment is better than a rushed decision at the holding point.</li>
</ul>
""",
takeaways=[
  "Gate de-icing uses more holdover time; pad de-icing is closer to the runway but more complex.",
  "On the pad, stay stationary and configured until “all clear” is received.",
  "Keep clear of jet blast and compare remaining HOT with the expected take-off time.",
],
check=dict(
  q="During remote pad de-icing, when may you reconfigure the aircraft and prepare to taxi?",
  options=["As soon as spraying stops", "When the anti-icing code is received and the de-icing crew confirms all personnel and equipment are clear", "When ATC gives a taxi clearance", "When the last de-icing truck starts to move"],
  answer=1,
  explain="Reconfiguring or moving is only safe after the treatment is complete, the code is received and the de-icing crew confirms all personnel and equipment are clear.",
),
),

# ---------------------------------------------------------------- 12
dict(
title="Inspections: Walk-around, Clear Ice and the Post-treatment Check",
minutes=8,
objectives=[
  "Perform a winter-specific exterior inspection.",
  "Know when a tactile check for clear ice is required.",
  "Describe the purpose and scope of the post de-icing/anti-icing check.",
],
body="""
<h2>The winter walk-around</h2>
<p>A cold weather exterior inspection takes longer and needs more light. Use a strong torch or the floodlights at night. In addition to the normal items, check:</p>
<ul>
  <li><strong>Wings, tail and control surfaces</strong> — upper surfaces where they can be seen. Use steps or an elevated platform where required, because frost on the upper wing can be invisible from the ground.</li>
  <li><strong>Engine inlets and fan blades</strong> — free of ice; fan rotates freely (where permitted to check). Propellers clear.</li>
  <li><strong>Probes, static ports, AoA vanes, drains and vents</strong> — clear, covers removed.</li>
  <li><strong>Landing gear, wheel wells, brakes and tyres</strong> — no ice or packed snow; tyres not frozen to the ground.</li>
  <li><strong>Fuel tank vents</strong> and <strong>doors and seals</strong> — free of ice.</li>
  <li>All <strong>covers and plugs</strong> removed and stowed.</li>
</ul>

<h2>Clear ice — when a tactile check is required</h2>
<p>A <strong>tactile (hands-on) check</strong> of the wing upper surface, or the use of an approved remote ice detection system, is required when clear ice may be present. Typical conditions:</p>
<ul>
  <li>the aircraft has cold-soaked fuel (after a long or high-altitude flight, or after uploading cold fuel);</li>
  <li>there is or has been precipitation, fog, high humidity or frost;</li>
  <li>the OAT is near or even above freezing.</li>
</ul>
<p>Many aircraft types have a defined area for the tactile check. On aircraft with rear-mounted engines it is often mandatory before every departure in these conditions. Ice that sheds from the wing at rotation can be ingested by both engines (see the SAS 751 case in Lesson 30).</p>
<div class="callout caution"><span class="label">Note</span><p>A wet-looking wing in cold conditions is not proof of a clean wing. If in doubt, touch it — or have it de-iced.</p></div>

<h2>Post de-icing/anti-icing check</h2>
<p>After treatment, a qualified member of the de-icing provider must check all treated surfaces from points with a clear view. Where needed this includes the upper wing from an elevated position, the horizontal and vertical stabilisers, and the control surfaces. The aircraft must be clean, with an even layer of anti-icing fluid where anti-icing was applied.</p>
<p>Completion of this check is confirmed in the anti-icing code. Without it, the aircraft must not be dispatched. The commander may still ask for any area to be re-checked or re-treated.</p>

<h2>Commander's acceptance</h2>
<p>The commander must be satisfied that the aircraft is clean. Use the information available to you: the code, your own observation of the wings, reports from cabin crew, and the weather since treatment.</p>
""",
takeaways=[
  "Winter walk-around: upper surfaces, inlets, probes, gear, vents and covers.",
  "Cold-soaked fuel + moisture → clear ice risk → tactile check or approved detection.",
  "The post de-icing/anti-icing check is mandatory and confirmed in the anti-icing code.",
],
check=dict(
  q="Which situation most clearly calls for a tactile check of the wing?",
  options=["Dry, cold day with an empty fuel tank", "After a long sector with cold fuel remaining, with drizzle at +3 °C", "Hot day with heavy rain", "After the aircraft has been in a heated hangar"],
  answer=1,
  explain="Cold-soaked fuel together with drizzle near 0 °C is the classic clear ice condition. Clear ice is hard to see and must be checked by touch or an approved detection system.",
),
),

# ---------------------------------------------------------------- 13
dict(
title="The Pre-take-off Check and the Pre-take-off Contamination Check",
minutes=8,
objectives=[
  "Distinguish the pre-take-off check from the pre-take-off contamination check (PTCC).",
  "State when each is required, who performs it and how.",
  "Recognise the signs of anti-icing fluid failure.",
],
body="""
<h2>Two different checks</h2>
<div class="table-wrap"><table>
  <tr><th></th><th>Pre-take-off check</th><th>Pre-take-off contamination check (PTCC)</th></tr>
  <tr><td>When</td><td>Within the holdover time, as part of the before-take-off actions</td><td>When the holdover time has been <strong>exceeded</strong>, or when the crew is in doubt</td></tr>
  <tr><td>Timing</td><td>Before take-off, as conditions require</td><td>Within <strong>5 minutes</strong> before beginning the take-off</td></tr>
  <tr><td>Who / where</td><td>Flight crew, normally from inside the aircraft (wings or representative surfaces)</td><td>A qualified person, normally from <strong>outside</strong> the aircraft, or from inside only where an approved procedure allows it</td></tr>
  <tr><td>What</td><td>The wings or representative surfaces that can be seen</td><td>The critical surfaces needed to confirm the aircraft is clean</td></tr>
  <tr><td>If contamination is seen</td><td colspan="2">Do not take off. Return for treatment.</td></tr>
</table></div>
<p>A PTCC cannot be used to extend an <strong>allowance time</strong> (ice pellets, small hail) — see Lesson 8.</p>

<h2>Signs of fluid failure</h2>
<ul>
  <li>The surface loses its gloss and looks dull or matt;</li>
  <li>Snow builds up on the surface rather than being absorbed;</li>
  <li>Ice crystals or slush appear in the fluid;</li>
  <li>Frozen fluid or a "slushy" texture, often starting at the leading edge or wing tips;</li>
  <li>Accumulation on other surfaces, such as wiper blades or nose cone, while the HOT is still running (a useful early warning).</li>
</ul>
<p>Fluid failure normally starts on the <strong>leading edge and wing tips</strong>, where the fluid layer is thinnest, and on surfaces exposed to wind.</p>

<h2>Practical points</h2>
<ul>
  <li>Use wing inspection lights at night. Check both sides.</li>
  <li>Cabin crew may be asked to look at the wings, using the company procedure. They must know what they are looking for and how to report it.</li>
  <li>If conditions get worse — heavier snow, a change to freezing rain — the HOT you calculated is no longer valid. Recalculate or return.</li>
</ul>

<div class="callout warn"><span class="label">Decision point</span><p>Agree before taxi: “If the HOT expires before take-off and a PTCC is not available, we return for treatment.” A pre-briefed decision protects you from pressure at the holding point.</p></div>
""",
takeaways=[
  "Pre-take-off check: within HOT, flight crew, usually from inside.",
  "PTCC: HOT exceeded, within 5 minutes of take-off, normally from outside the aircraft.",
  "Dull surface, snow building up or ice crystals in the fluid mean fluid failure — return for treatment.",
  "Pre-brief the decision to return before you taxi.",
],
check=dict(
  q="The holdover time has expired while you queue for take-off. Snowfall continues. What is required to take off?",
  options=["Nothing, provided the wings look clean from the flight deck", "A pre-take-off contamination check within 5 minutes before take-off, normally from outside — otherwise re-treat", "Engine and wing anti-ice on", "A new anti-icing code by radio"],
  answer=1,
  explain="With HOT exceeded, take-off is only permitted after a PTCC, completed within 5 minutes before take-off, that confirms the critical surfaces are clean. Otherwise the aircraft must be re-treated.",
),
),

# ---------------------------------------------------------------- 14
dict(
title="Performance Effects of Cold Weather and Contamination",
minutes=8,
objectives=[
  "Explain how runway contaminants affect acceleration and stopping.",
  "Describe the performance penalties of anti-ice and contaminated runways.",
  "Recognise the operational restrictions on reduced thrust and V1.",
],
body="""
<h2>Two families of effects</h2>
<p><strong>Aircraft contamination</strong> (Lesson 5) reduces lift and increases drag and stall speed. <strong>Runway contamination</strong> affects acceleration, stopping and directional control. This lesson covers the runway.</p>

<h2>Acceleration</h2>
<p>Loose, wet contaminants — standing water, slush, wet snow and deep dry snow — slow the aircraft down through:</p>
<ul>
  <li><strong>displacement drag</strong>: tyres pushing the contaminant aside;</li>
  <li><strong>impingement drag</strong>: spray striking the airframe, gear and flaps.</li>
</ul>
<p>The deeper and denser the contaminant, the greater the drag. Drag peaks close to the aquaplaning speed. The result is a longer take-off distance and, after an engine failure, a longer accelerate-go distance.</p>

<h2>Stopping and control</h2>
<ul>
  <li>Braking friction is reduced on every contaminant. On ice it can be a fraction of a dry runway.</li>
  <li>Aquaplaning reduces wheel braking and steering almost to zero (Lesson 16).</li>
  <li>Crosswind limits are reduced, depending on the runway condition code.</li>
  <li>The <strong>accelerate-stop distance</strong> grows. To compensate, performance calculations usually produce a <strong>lower V1</strong> and may reduce the maximum take-off mass.</li>
</ul>

<h2>Operational rules</h2>
<div class="callout warn"><span class="label">Typical restrictions — check your AFM</span>
<ul>
  <li><strong>Reduced (assumed temperature / FLEX) thrust is not permitted on contaminated runways.</strong> A fixed derate may be permitted when contaminated runway data exists for it.</li>
  <li>Use the contaminated runway performance data for the reported contaminant type and depth.</li>
  <li>Maximum contaminant depth for take-off is limited by the AFM — typically around 12.7 mm (½ in) of standing water, slush or wet snow, with higher limits for dry snow.</li>
</ul>
</div>

<h2>Anti-ice and cold temperatures</h2>
<ul>
  <li>Engine and wing anti-ice take bleed air, which reduces available thrust and climb performance. Performance tables include corrections when anti-ice is on.</li>
  <li>Cold, dense air normally <em>improves</em> engine and aircraft performance, but very low temperatures may bring limits on engine thrust, oil temperature or fluid use.</li>
  <li>Some types use higher approach or manoeuvring speeds when ice has accumulated on unprotected surfaces. Follow the FCOM's “ice accretion” speeds and performance corrections.</li>
</ul>
""",
takeaways=[
  "Wet contaminants add drag and lengthen take-off; all contaminants reduce braking.",
  "Contaminated runways usually mean a lower V1 and possibly a lower maximum take-off mass.",
  "No assumed-temperature (FLEX) reduced thrust on contaminated runways.",
  "Anti-ice reduces thrust — apply the performance corrections.",
],
check=dict(
  q="What is the usual rule on assumed temperature (FLEX) reduced thrust when the runway is contaminated?",
  options=["It is always required to protect the engines", "It is not permitted", "It is permitted if V1 is reduced by 10 kt", "It is permitted at night only"],
  answer=1,
  explain="Assumed temperature reduced thrust is not permitted on contaminated runways. A fixed derate may be allowed if the AFM provides contaminated runway data for it.",
),
),

# ---------------------------------------------------------------- 15
dict(
title="Runway Condition Reporting: GRF, RCAM and RWYCC",
minutes=10,
objectives=[
  "Explain the ICAO Global Reporting Format (GRF) and the Runway Condition Report (RCR).",
  "Interpret runway condition codes (RWYCC) using the RCAM.",
  "Make and use pilot braking action reports correctly.",
],
body="""
<h2>The Global Reporting Format</h2>
<p>Since November 2021, ICAO's <strong>Global Reporting Format (GRF)</strong> has been the standard method for assessing and reporting runway surface conditions. Its purpose is to give pilots a common language that links directly to aircraft performance data. The FAA uses an equivalent system called TALPA.</p>
<p>The aerodrome operator assesses the runway and issues a <strong>Runway Condition Report (RCR)</strong>, which reaches crews through ATIS, ATC and SNOWTAM.</p>

<h2>Reading a Runway Condition Report</h2>
<p>The aircraft performance part of the RCR is given for each <strong>third</strong> of the runway, in the direction of the <strong>lower</strong> runway designator:</p>
<p><code>XXXX 01170830 09 5/5/2 100/100/50 NR/NR/06 WET/WET/SLUSH</code></p>
<div class="table-wrap"><table>
  <tr><th>Element</th><th>Example</th><th>Meaning</th></tr>
  <tr><td>Aerodrome / date-time</td><td><code>XXXX 01170830</code></td><td>Location and time of assessment (month, day, hour, minute UTC)</td></tr>
  <tr><td>Runway</td><td><code>09</code></td><td>Lower runway designator</td></tr>
  <tr><td>RWYCC per third</td><td><code>5/5/2</code></td><td>Runway condition code for each third</td></tr>
  <tr><td>Coverage per third</td><td><code>100/100/50</code></td><td>Percentage of each third covered (reported as 25, 50, 75 or 100)</td></tr>
  <tr><td>Depth per third</td><td><code>NR/NR/06</code></td><td>Depth in mm of loose contaminant (water, slush, dry or wet snow); NR = not reported</td></tr>
  <tr><td>Contaminant per third</td><td><code>WET/WET/SLUSH</code></td><td>Type of surface condition</td></tr>
</table></div>
""" + RUNWAY_SVG + """
<h2>The Runway Condition Assessment Matrix (RCAM)</h2>
<div class="table-wrap"><table>
  <tr><th>RWYCC</th><th>Runway surface description</th><th>Pilot braking action</th></tr>
  <tr><td class="code">6</td><td>DRY</td><td>—</td></tr>
  <tr><td class="code">5</td><td>FROST; WET (including damp, and 3 mm of water or less); SLUSH, DRY SNOW or WET SNOW 3 mm or less</td><td>Good</td></tr>
  <tr><td class="code">4</td><td>COMPACTED SNOW at OAT −15 °C and below</td><td>Good to medium</td></tr>
  <tr><td class="code">3</td><td>WET (“slippery wet” runway); DRY SNOW or WET SNOW (any depth) ON TOP OF COMPACTED SNOW; DRY SNOW or WET SNOW more than 3 mm; COMPACTED SNOW at OAT above −15 °C</td><td>Medium</td></tr>
  <tr><td class="code">2</td><td>STANDING WATER more than 3 mm; SLUSH more than 3 mm</td><td>Medium to poor</td></tr>
  <tr><td class="code">1</td><td>ICE</td><td>Poor</td></tr>
  <tr><td class="code">0</td><td>WET ICE; WATER ON TOP OF COMPACTED SNOW; DRY SNOW or WET SNOW ON TOP OF ICE</td><td>Less than poor</td></tr>
</table></div>
<p>The aerodrome may upgrade or downgrade a code using measurements, observations and pilot reports. A runway with RWYCC 0 is not used for take-off or landing.</p>

<h2>Pilot braking action reports</h2>
<p>Pilots report braking action using the same terms — <strong>good, good to medium, medium, medium to poor, poor, less than poor</strong> — for example: “Braking action medium to poor, runway 27, second half.”</p>
<ul>
  <li>Report whenever braking or directional control is worse than reported, or when asked.</li>
  <li>Your report is an important input to the aerodrome's assessment and to the crew behind you.</li>
  <li>Reports age quickly in active precipitation. Always check the time of the RCR and the trend.</li>
</ul>
""",
takeaways=[
  "RCR is reported per runway third, in the direction of the lower designator.",
  "RWYCC 6 = dry … 0 = less than poor. 2 = standing water or slush more than 3 mm; 1 = ice.",
  "Use the reported codes directly with the performance data.",
  "Report braking action that is worse than reported.",
],
check=dict(
  q="A runway third is covered with 6 mm of slush. What RWYCC would normally be reported?",
  options=["5", "3", "2", "0"],
  answer=2,
  explain="In the RCAM, standing water or slush deeper than 3 mm corresponds to RWYCC 2 (medium to poor).",
),
),

# ---------------------------------------------------------------- 16
dict(
title="Take-off on Contaminated Runways",
minutes=9,
objectives=[
  "Apply AFM contaminant depth and crosswind limits for take-off.",
  "Explain aquaplaning and estimate aquaplaning speed.",
  "Plan for a rejected take-off and directional control on a slippery runway.",
],
body="""
<h2>Before you start</h2>
<ul>
  <li>Obtain the latest RCR. Confirm that the contaminant type and depth are within the AFM limits for take-off.</li>
  <li>Calculate performance using the contaminated runway data and the reported RWYCC: no assumed-temperature reduced thrust, and possibly a lower V1 and mass.</li>
  <li>Apply the reduced crosswind limit for the runway condition (Operations Manual / FCOM table).</li>
  <li>Brief the rejected take-off: decision speed, directional control technique, and the effect of reverse thrust in a crosswind.</li>
</ul>

<h2>Aquaplaning</h2>
<p>When a tyre rides on a layer of water or slush, it loses contact with the runway. Braking and steering become almost useless. The approximate minimum speed at which <strong>dynamic aquaplaning</strong> starts is:</p>
<div class="callout info"><span class="label">Rule of thumb</span>
<p><strong>V<sub>P</sub> (kt) ≈ 9 × √(tyre pressure in psi)</strong> for a rotating tyre (take-off). For a tyre that is not yet rotating, as at touchdown, the speed is lower — about 7.7 × √(tyre pressure).</p>
<p>Example: tyre pressure 196 psi → √196 = 14 → about 126 kt for a rotating tyre, about 108 kt at touchdown.</p>
</div>
<p>Other forms include <strong>viscous aquaplaning</strong> (a thin film on a smooth or rubber-coated surface) and <strong>reverted rubber aquaplaning</strong> (a locked wheel overheating and producing steam).</p>

<h2>During the take-off roll</h2>
<ul>
  <li>Where the AFM requires it, carry out a static run-up to shed fan ice. On a slippery surface the brakes may not hold, so use the technique in the FCOM.</li>
  <li>Apply thrust symmetrically. Keep straight with the rudder, using small nosewheel steering inputs at low speed only.</li>
  <li>Expect slower acceleration in slush or wet snow, and spray striking the airframe.</li>
</ul>

<h2>Rejected take-off on a slippery runway</h2>
<ul>
  <li>Stopping distances are much longer. Up to V1, reject for the reasons in your SOPs. Above V1, continue.</li>
  <li>Use maximum braking (or the RTO autobrake) and maximum reverse thrust as the procedure states.</li>
  <li><strong>Reverse thrust in a crosswind</strong> pushes the aircraft downwind and makes it weathervane. If the aircraft starts to drift off the centreline, the typical technique is: reduce reverse thrust towards idle, release the brakes momentarily, regain the centreline with rudder and steering, then reapply braking and reverse. Follow your FCOM.</li>
</ul>

<h2>After take-off</h2>
<p>Slush and snow thrown onto the landing gear, flaps and wheel wells can freeze at altitude. Some AFMs recommend specific actions after a take-off from a slush-covered runway, such as delayed retraction or cycling the gear. Apply them only when your FCOM states them.</p>
""",
takeaways=[
  "Check contaminant type and depth against AFM limits; use contaminated runway performance.",
  "Aquaplaning speed ≈ 9 × √(tyre pressure) for a rotating tyre, lower at touchdown.",
  "In a crosswind RTO, reverse thrust can push you downwind — know the recovery technique.",
],
check=dict(
  q="Tyre pressure is 144 psi. Approximately at what speed could dynamic aquaplaning begin during the take-off roll?",
  options=["About 72 kt", "About 108 kt", "About 144 kt", "About 160 kt"],
  answer=1,
  explain="9 × √144 = 9 × 12 = 108 kt for a rotating tyre.",
),
),

# ---------------------------------------------------------------- 17
dict(
title="Landing on Contaminated Runways",
minutes=9,
objectives=[
  "Perform a landing distance assessment at the time of arrival.",
  "Apply landing techniques for slippery runways.",
  "Recognise when to go around or divert.",
],
body="""
<h2>Landing distance assessment at the time of arrival</h2>
<p>Runway conditions at the time of arrival may be very different from those used at dispatch. Before the approach — normally before top of descent and again if conditions change — calculate the <strong>landing distance at time of arrival</strong> using:</p>
<ul>
  <li>the latest RCR (RWYCC per third, contaminant and depth);</li>
  <li>expected landing mass, wind, temperature, altitude, slope, configuration and approach speed additives;</li>
  <li>the planned autobrake setting and use of reverse thrust, as the performance data allows.</li>
</ul>
<p>Add the safety margin required by the Operations Manual. Industry guidance recommends at least <strong>15 %</strong> on the actual (unfactored) landing distance. If the result does not fit within the available landing distance, do not start the approach — hold, choose another runway, or divert.</p>

<h2>Technique</h2>
<ol class="steps">
  <li><strong>Stabilised approach</strong> on speed, on profile, with the correct additives. Go around if the approach is not stabilised.</li>
  <li><strong>Touch down firmly in the touchdown zone.</strong> Do not float — every second of float uses runway you need for stopping. A firm touchdown helps the wheels spin up and break through the water film.</li>
  <li><strong>Lower the nosewheel promptly</strong> for steering and to put weight on the wheels.</li>
  <li><strong>Ground spoilers</strong> deployed, verified and called.</li>
  <li><strong>Reverse thrust early</strong>: maximum reverse as soon as possible after touchdown, as the SOP states. Reversers are most effective at high speed.</li>
  <li><strong>Braking</strong>: autobrake as planned, or steady manual braking with the anti-skid working. Do not pump the brakes.</li>
  <li><strong>Directional control</strong> with rudder. Use nosewheel steering at low speed, with small inputs. In a crosswind with reverse thrust, apply the same recovery technique as for the rejected take-off.</li>
</ol>

<h2>When to go around or divert</h2>
<ul>
  <li>The approach is not stabilised, or the touchdown point will be beyond the touchdown zone.</li>
  <li>The runway report changes during the approach to a code or contaminant for which the landing distance is not enough.</li>
  <li>Braking action reports from preceding aircraft are worse than planned.</li>
  <li>Once reverse thrust is selected, you are committed to stop. The decision to go around must be made before that.</li>
</ul>

<h2>After landing</h2>
<p>Taxi slowly. Report braking action if it was worse than reported. On stand, consider the risk of brakes freezing after taxiing through slush. Use chocks and follow the SOP on releasing the parking brake (Lesson 19).</p>
""",
takeaways=[
  "Recalculate landing distance at the time of arrival, with at least the required margin (typically 15 %).",
  "Firm touchdown in the zone, no float, spoilers, early maximum reverse, steady braking.",
  "Go around before selecting reverse thrust if the landing is in doubt.",
],
check=dict(
  q="Why is a firm touchdown preferred on a runway covered with water or slush?",
  options=["To reduce the stress on the landing gear", "To help the wheels spin up, break through the water film and avoid floating", "To allow a longer flare", "To keep the reverse thrust in idle"],
  answer=1,
  explain="A firm touchdown in the touchdown zone avoids wasting runway, helps the wheels penetrate the water film and spin up, and reduces the risk of aquaplaning.",
),
),

# ---------------------------------------------------------------- 18
dict(
title="Taxi Operations on Slippery Surfaces",
minutes=7,
objectives=[
  "Taxi safely on contaminated aprons and taxiways.",
  "Avoid contaminating treated aircraft and other aircraft.",
  "Recognise the specific hazards of snowbanks and hidden markings.",
],
body="""
<h2>Speed, spacing and thrust</h2>
<ul>
  <li>Taxi slowly, at walking pace on ice or poor surfaces. Plan turns early and make them at low speed.</li>
  <li>Increase the spacing behind the aircraft ahead. You need more distance to stop, and you avoid its jet blast, which blows snow, slush and ice onto your treated surfaces.</li>
  <li>Use the minimum breakaway thrust. High thrust on ice can make the aircraft slide or yaw.</li>
  <li>Make small, smooth nosewheel steering inputs. A nosewheel that skids sideways does not steer.</li>
  <li>If the aircraft starts to slide, reduce thrust to idle and apply braking and steering gently.</li>
</ul>

<h2>Snow and the airport environment</h2>
<ul>
  <li><strong>Snowbanks</strong> along taxiway edges can strike wing tips, engine nacelles and propellers. Check the NOTAM/SNOWTAM for cleared widths.</li>
  <li><strong>Markings and lights may be covered</strong>. Use the airport chart, request progressive taxi instructions if unsure, and confirm the holding position.</li>
  <li><strong>Ramp areas</strong> near de-icing pads are extremely slippery because of glycol.</li>
  <li>Be aware of snow clearing vehicles and their crews, especially in low visibility.</li>
</ul>

<h2>Protecting the treated aircraft</h2>
<ul>
  <li>Taxi with the flaps up through slush or snow if your FCOM allows it. Set them before the runway, and complete the checklist before take-off.</li>
  <li>Do not taxi close behind other aircraft or through deep slush if it can be avoided.</li>
  <li>Monitor the precipitation and the remaining HOT while you taxi.</li>
</ul>

<h2>Single-engine taxi in winter</h2>
<p>Single-engine taxi may be restricted in winter. Engines may need a minimum warm-up before take-off thrust, asymmetric thrust is harder to control on slippery surfaces, and starting the second engine near the runway increases workload just when the HOT is running. Follow the Operations Manual.</p>
""",
takeaways=[
  "Slow taxi, larger spacing, minimum thrust, small steering inputs.",
  "Snowbanks and covered markings are hidden threats — use charts and NOTAMs.",
  "Keep clear of jet blast and deep slush to protect your treated surfaces.",
],
check=dict(
  q="Why should you increase spacing behind other aircraft while taxiing after de-icing?",
  options=["To save fuel", "To stop safely on slippery surfaces and avoid jet blast blowing contamination onto your aircraft", "Because ATC requires double separation in winter", "To keep the engines warm"],
  answer=1,
  explain="Extra spacing gives you room to stop on a slippery surface and keeps you out of jet blast, which can blow snow and slush onto treated surfaces and thin the fluid.",
),
),

# ---------------------------------------------------------------- 19
dict(
title="Cold Soak, Overnight Parking and Pre-flight Preparation",
minutes=8,
objectives=[
  "Protect an aircraft parked overnight in cold conditions.",
  "Prepare a cold-soaked aircraft for flight.",
  "Identify the effects of cold on tyres, brakes, water systems and batteries.",
],
body="""
<h2>Cold soak</h2>
<p>An aircraft is <strong>cold-soaked</strong> when its structure, fluids and equipment have cooled to the ambient temperature — usually after several hours parked outside in the cold, or after a long flight at high altitude. Cold soak affects nearly every system: fluids become thicker, seals harden, batteries lose capacity, and water freezes.</p>

<h2>Overnight parking (as the company procedure and AFM specify)</h2>
<ul>
  <li><strong>Covers and plugs</strong> fitted on engines, probes and inlets where available. Record them so they are removed before flight.</li>
  <li><strong>Potable water and waste systems</strong> drained if the aircraft will be unheated, to prevent pipes, tanks and valves from freezing.</li>
  <li><strong>Parking brake</strong>: after taxiing through slush or snow, wet brakes can freeze. The common practice is to chock the wheels and release the parking brake when permitted.</li>
  <li><strong>Batteries</strong>: in extreme cold, some types require removal or a heated location.</li>
  <li><strong>Fuel</strong>: drain water from the tank sumps as maintenance requires.</li>
  <li><strong>Doors closed</strong> to keep snow out and reduce cabin cooling.</li>
  <li>Where possible, park the aircraft nose into the wind or in a hangar when heavy snow or freezing precipitation is forecast.</li>
</ul>

<h2>Preparing a cold-soaked aircraft</h2>
<ul>
  <li>Plan for extra time. Cabin heating, de-icing and systems warm-up all take longer.</li>
  <li>Check that all covers and plugs are removed and that no snow or ice remains in inlets, wheel wells, vents and drains.</li>
  <li>Check tyre pressures. Pressure falls by about <strong>1 % for every 3 °C</strong> drop in temperature, so a tyre set in a warm hangar will be under-inflated outside.</li>
  <li>Hydraulic, oil and strut indications may read differently when cold. Follow the servicing procedures for cold temperatures.</li>
  <li>Oxygen bottle pressure is lower in the cold. Use the temperature-corrected minimum pressure chart.</li>
  <li>Switch on window heat early, at the low setting if your type has one, to avoid thermal shock to cold windshields.</li>
  <li>Warm the cabin before boarding when possible, using the APU or ground air conditioning.</li>
</ul>
""",
takeaways=[
  "Cold soak affects fluids, seals, batteries, water systems and tyres.",
  "Drain water systems, fit covers, and chock with the parking brake released after slush taxi (as the SOP states).",
  "Tyre pressure drops about 1 % per 3 °C — check it outside.",
  "Plan extra time for the preparation of a cold-soaked aircraft.",
],
check=dict(
  q="A tyre was set to the correct pressure at +15 °C in a hangar. The aircraft is now outside at −15 °C. What do you expect?",
  options=["Pressure about 10 % lower", "No change in pressure", "Pressure about 10 % higher", "Pressure about 30 % lower"],
  answer=0,
  explain="A 30 °C drop at about 1 % per 3 °C gives roughly a 10 % reduction in tyre pressure.",
),
),

# ---------------------------------------------------------------- 20
dict(
title="Engines and APU in Cold Weather",
minutes=8,
objectives=[
  "Apply cold-start considerations for engines and APU.",
  "Use engine anti-ice correctly on the ground.",
  "Explain engine run-up procedures for ice shedding in freezing fog and precipitation.",
],
body="""
<h2>Cold starts</h2>
<ul>
  <li><strong>Oil</strong> is more viscous. Expect higher oil pressure and slower rotation at first. Some engines need a minimum oil temperature before take-off thrust can be used.</li>
  <li><strong>Start times are longer.</strong> Monitor N2/N1, EGT and oil pressure closely. Know the starter duty cycle limits, and the hung start and no-light-off procedures.</li>
  <li><strong>Warm-up</strong>: the AFM gives a minimum warm-up time after a cold soak before high thrust. Plan it into the taxi.</li>
  <li><strong>Batteries</strong> have less capacity in the cold. Use ground power or the APU for engine starts where possible.</li>
  <li><strong>APU</strong>: check that the inlet and exhaust are free of snow and ice. The APU may need more time to start and stabilise.</li>
</ul>

<h2>Engine anti-ice on the ground</h2>
<p>Switch engine anti-ice on <strong>whenever icing conditions exist</strong> on the ground or are expected for take-off — OAT 10 °C or below with visible moisture, or with snow, ice, slush or standing water on the surfaces (Lesson 4). Follow the AFM for the timing, such as immediately after engine start, and before entering icing conditions in flight.</p>
<div class="callout caution"><span class="label">Do not forget</span><p>Engine inlet and probe ice can give <strong>false thrust indications</strong> (see the Air Florida 90 case in Lesson 30). Operate engine anti-ice as the AFM requires, and cross-check thrust with all engine parameters.</p></div>

<h2>Engine run-ups for ice shedding</h2>
<p>When taxiing or holding for a long time in freezing fog, freezing precipitation or heavy snow, ice can build up on the fan blades and spinner. Many AFMs require <strong>periodic run-ups</strong> to a specified thrust for a specified time to shed this ice, and a run-up before take-off. Follow the exact values and intervals in your FCOM, and keep clear of other aircraft, vehicles and people behind you.</p>

<h2>Turboprops and propellers</h2>
<ul>
  <li>Propellers must be free of ice and snow before engine start.</li>
  <li>Propeller de-ice and engine intake anti-ice/de-ice are used as the AFM specifies.</li>
  <li>Propeller blast can blow snow and slush onto other aircraft and onto your own tail.</li>
</ul>
""",
takeaways=[
  "Cold oil: higher pressure, longer starts, minimum warm-up before take-off thrust.",
  "Engine anti-ice on whenever icing conditions exist on the ground — per AFM.",
  "Periodic run-ups shed fan ice in freezing fog and precipitation.",
  "Iced probes can give false thrust indications — cross-check engine parameters.",
],
check=dict(
  q="You are holding for 25 minutes in freezing fog. What engine-related action does the AFM typically require?",
  options=["Shut down one engine", "Periodic engine run-ups to shed fan ice, as specified", "Switch engine anti-ice off to increase thrust", "Nothing until take-off"],
  answer=1,
  explain="In freezing fog, ice can build up on fan blades. Many AFMs require periodic run-ups to a specified thrust for a specified time to shed it.",
),
),
]
