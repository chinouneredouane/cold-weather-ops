# Cold Weather Operations — lessons 1–10
# Each lesson: title, minutes, objectives, body (HTML), takeaways, check (knowledge check).

LIFT_CURVE_SVG = """
<figure class="diagram">
<svg viewBox="0 0 600 330" role="img" aria-labelledby="lc-t lc-d">
  <title id="lc-t">Lift coefficient versus angle of attack, clean and contaminated wing</title>
  <desc id="lc-d">The contaminated wing produces less lift at every angle of attack and stalls at a lower angle, before the stall warning activates.</desc>
  <g font-family="system-ui,Segoe UI,Arial,sans-serif" font-size="13" fill="#24342b">
    <line x1="60" y1="280" x2="570" y2="280" stroke="#5b6b62" stroke-width="1.5"/>
    <line x1="60" y1="280" x2="60" y2="30" stroke="#5b6b62" stroke-width="1.5"/>
    <text x="315" y="315" text-anchor="middle">Angle of attack →</text>
    <text x="22" y="155" text-anchor="middle" transform="rotate(-90 22 155)">Lift coefficient (CL) →</text>
    <line x1="385" y1="34" x2="385" y2="280" stroke="#c8102e" stroke-width="1.5" stroke-dasharray="5 5"/>
    <text x="392" y="252" fill="#c8102e" font-weight="600">Stall warning</text>
    <text x="392" y="268" fill="#c8102e">(scheduled for a clean wing)</text>
    <path d="M60 250 L360 78 Q410 45 435 52 Q470 62 505 108" fill="none" stroke="#1d7a3e" stroke-width="4" stroke-linecap="round"/>
    <path d="M60 256 L285 136 Q318 112 335 116 Q362 124 392 168" fill="none" stroke="#9a6200" stroke-width="4" stroke-dasharray="10 6" stroke-linecap="round"/>
    <circle cx="433" cy="51" r="5" fill="#1d7a3e"/>
    <text x="440" y="42" fill="#125a2b" font-weight="700">CLmax — clean wing</text>
    <circle cx="333" cy="115" r="5" fill="#9a6200"/>
    <text x="150" y="92" fill="#9a6200" font-weight="700">CLmax — contaminated</text>
    <line x1="300" y1="97" x2="328" y2="111" stroke="#9a6200" stroke-width="1.2"/>
    <line x1="338" y1="115" x2="460" y2="115" stroke="#9a6200" stroke-width="1" stroke-dasharray="3 3"/>
    <path d="M455 57 L455 111" stroke="#5b6b62" stroke-width="1.2" marker-end="url(#ah)" marker-start="url(#ah)"/>
    <text x="465" y="150">up to ~30 %</text><text x="465" y="166">less lift</text>
    <defs><marker id="ah" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#5b6b62"/></marker></defs>
  </g>
</svg>
<figcaption>Illustrative only. Roughness no thicker than coarse sandpaper lowers maximum lift and the stall angle of attack. The aircraft can stall <em>before</em> the stall warning activates.</figcaption>
</figure>
"""

STEP_SVG = """
<figure class="diagram">
<svg viewBox="0 0 640 230" role="img" aria-labelledby="st-t st-d">
  <title id="st-t">One-step and two-step de-icing/anti-icing timelines</title>
  <desc id="st-d">In a one-step procedure the holdover time starts at the beginning of the single application. In a two-step procedure it starts at the beginning of the second, anti-icing step, which must be applied within three minutes of the first.</desc>
  <g font-family="system-ui,Segoe UI,Arial,sans-serif" font-size="13" fill="#24342b">
    <text x="10" y="58" font-weight="700">One-step</text>
    <rect x="120" y="36" width="230" height="36" rx="8" fill="#c76a00"/>
    <text x="235" y="59" text-anchor="middle" fill="#fff" font-weight="600">Heated fluid: de-ice + anti-ice</text>
    <rect x="350" y="44" width="270" height="20" rx="4" fill="#e7f3eb" stroke="#1d7a3e"/>
    <text x="485" y="58" text-anchor="middle" fill="#125a2b">holdover time running</text>
    <line x1="120" y1="26" x2="120" y2="84" stroke="#c8102e" stroke-width="2"/>
    <text x="124" y="22" fill="#c8102e" font-weight="700">HOT starts</text>

    <text x="10" y="168" font-weight="700">Two-step</text>
    <rect x="120" y="146" width="150" height="36" rx="8" fill="#c76a00"/>
    <text x="195" y="169" text-anchor="middle" fill="#fff" font-weight="600">Step 1: de-ice</text>
    <rect x="300" y="146" width="150" height="36" rx="8" fill="#1d7a3e"/>
    <text x="375" y="169" text-anchor="middle" fill="#fff" font-weight="600">Step 2: anti-ice</text>
    <rect x="450" y="154" width="170" height="20" rx="4" fill="#e7f3eb" stroke="#1d7a3e"/>
    <text x="535" y="168" text-anchor="middle" fill="#125a2b">holdover time running</text>
    <path d="M272 200 L298 200" stroke="#5b6b62" marker-end="url(#ah2)" marker-start="url(#ah2)"/>
    <text x="285" y="218" text-anchor="middle">≤ 3 min</text>
    <line x1="300" y1="136" x2="300" y2="194" stroke="#c8102e" stroke-width="2"/>
    <text x="304" y="132" fill="#c8102e" font-weight="700">HOT starts</text>
    <defs><marker id="ah2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#5b6b62"/></marker></defs>
  </g>
</svg>
<figcaption>The holdover time always starts at the <strong>beginning of the final application</strong>, not at the end.</figcaption>
</figure>
"""

LESSONS_A = [
# ---------------------------------------------------------------- 1
dict(
title="Course Orientation and Objectives",
minutes=5,
objectives=[
  "Describe the purpose, scope and structure of this course.",
  "Explain how progress, narration, knowledge checks and the final quiz work.",
  "Recognise the relationship between this course and the aircraft and company manuals.",
],
body="""
<h2>Purpose</h2>
<p>This course gives Domestic Airlines crews a practical understanding of aircraft operations in cold weather. It covers aircraft contamination, ground de-icing and anti-icing, holdover times, contaminated runways, cold-soaked systems, cold temperature altimetry and the human factors that drive winter accidents.</p>
<p>Winter conditions rarely look dramatic. Most cold weather accidents began with something small: a thin layer of frost, a holdover time quietly expiring in the queue, a runway report that was already out of date. The aim of this course is to help you recognise those small things early and to act on them with confidence.</p>

<h2>Who this course is for</h2>
<ul>
  <li><strong>Flight crew</strong> — the primary audience. The pilot-in-command is responsible for making sure the aircraft is free of contamination before take-off.</li>
  <li><strong>Cabin crew, flight dispatchers and ground operations staff</strong> — the course is also useful for everyone who supports a winter departure.</li>
</ul>

<h2>Course structure</h2>
<div class="table-wrap"><table>
  <tr><th>Module</th><th>Lessons</th><th>Focus</th></tr>
  <tr><td>1. Foundations</td><td>1–5</td><td>Weather, contaminants, icing and the Clean Aircraft Concept</td></tr>
  <tr><td>2. De-icing and Anti-icing</td><td>6–11</td><td>Methods, fluids, holdover times, preparation and communication</td></tr>
  <tr><td>3. Inspections</td><td>12–13</td><td>Clear ice, post-treatment checks and the pre-take-off checks</td></tr>
  <tr><td>4. Runways and Performance</td><td>14–18</td><td>Contaminated runway performance, GRF reporting, take-off, landing and taxi</td></tr>
  <tr><td>5. Aircraft Systems in the Cold</td><td>19–23</td><td>Cold soak, engines, systems, fuel, flight controls and in-flight icing</td></tr>
  <tr><td>6. Operations and Human Factors</td><td>24–30</td><td>Altimetry, dispatch, cabin, CRM, emergencies, regulation and accident lessons</td></tr>
</table></div>

<h2>How to use this course</h2>
<ul>
  <li><strong>Lessons</strong> take 5–10 minutes each. A lesson is marked complete when you reach its end or press <em>Next</em>.</li>
  <li><strong>Narration</strong> — press <em>Listen</em> on any lesson to hear it read aloud.</li>
  <li><strong>Knowledge checks</strong> at the end of each lesson are for practice only and are not scored.</li>
  <li><strong>Final quiz</strong> — 20 questions drawn at random from a bank of 50. The pass mark is 80 %. You may retake it as many times as you need.</li>
  <li><strong>Progress</strong> is saved in this browser on this device. Using another device or clearing browser data resets it.</li>
</ul>

<div class="callout warn"><span class="label">Important</span>
<p>This course is general training material based on international guidance (ICAO, EASA, FAA, Transport Canada and SAE). It does <strong>not</strong> replace the Aircraft Flight Manual (AFM), FCOM, QRH, MEL or the Domestic Airlines Operations Manual. Where they differ, the approved aircraft and company documents always take precedence.</p>
</div>

<h2>Course objectives</h2>
<p>By the end of the course you will be able to:</p>
<ul>
  <li>identify frost, ice, snow and slush hazards and explain their effect on aircraft performance;</li>
  <li>apply the Clean Aircraft Concept and the company ground de-icing/anti-icing programme;</li>
  <li>select and use holdover time guidelines correctly, and know when a pre-take-off contamination check or re-treatment is required;</li>
  <li>interpret runway condition reports (RWYCC) and assess take-off and landing performance on contaminated runways;</li>
  <li>operate aircraft systems safely after cold soak and in icing conditions;</li>
  <li>apply cold temperature altimeter corrections;</li>
  <li>use CRM and threat and error management to resist time pressure in winter operations.</li>
</ul>
""",
takeaways=[
  "The pilot-in-command is responsible for making sure the aircraft is free of contamination before take-off.",
  "The AFM, FCOM and Operations Manual always take precedence over this course.",
  "Final quiz: 20 random questions, 80 % to pass, unlimited attempts.",
],
check=dict(
  q="If this course and the Aircraft Flight Manual give different guidance, which do you follow?",
  options=["This course, because it is more recent", "The Aircraft Flight Manual and company procedures", "Whichever is more conservative, decided by the first officer", "The de-icing provider's instructions"],
  answer=1,
  explain="Approved aircraft and company documents (AFM, FCOM, Operations Manual) always take precedence over general training material.",
),
),

# ---------------------------------------------------------------- 2
dict(
title="Cold Weather Meteorology",
minutes=9,
objectives=[
  "Explain supercooled water and why it is the key ingredient of icing.",
  "Describe how freezing rain, freezing drizzle, ice pellets and the different snow types form.",
  "Decode the winter weather groups used in METAR and TAF reports.",
],
body="""
<h2>Supercooled water</h2>
<p>Liquid water does not automatically freeze at 0 °C. Small, pure droplets can remain liquid well below freezing — in theory down to about −40 °C. Such droplets are called <strong>supercooled</strong>. They are unstable: when one strikes a surface, such as a wing, a propeller or an engine inlet, it freezes partly or completely on impact.</p>
<p>Supercooled water is found in cloud, fog, drizzle and rain at sub-zero temperatures. It is the source of almost all airframe icing, both in flight and on the ground.</p>

<h2>Precipitation types that matter</h2>
<div class="table-wrap"><table>
  <tr><th>Type</th><th>METAR</th><th>How it forms</th><th>Why it matters</th></tr>
  <tr><td>Freezing rain</td><td><code>FZRA</code></td><td>Snow melts in a warm layer aloft (a temperature inversion) and falls as rain into a sub-zero layer near the surface, becoming supercooled.</td><td>Forms clear ice rapidly. Holdover times are very short or not available. Heavy and moderate freezing rain normally prohibit take-off.</td></tr>
  <tr><td>Freezing drizzle</td><td><code>FZDZ</code></td><td>Small supercooled drops, often from shallow stratus. It can form without a warm layer aloft.</td><td>A source of supercooled large droplets (SLD) in flight; it builds ice on the ground steadily.</td></tr>
  <tr><td>Freezing fog</td><td><code>FZFG</code></td><td>Fog made of supercooled droplets.</td><td>Builds rime on parked and taxiing aircraft and engine fan blades. Engine run-ups may be required.</td></tr>
  <tr><td>Snow (dry or wet)</td><td><code>SN</code></td><td>Ice crystals that grow in cloud. Wet snow falls when the temperature is near 0 °C.</td><td>Wet snow has a high water content and dilutes anti-icing fluid quickly, so holdover times are much shorter.</td></tr>
  <tr><td>Snow grains</td><td><code>SG</code></td><td>Very small, opaque grains of ice, usually from stratus.</td><td>Treated like snow when holdover time guidelines are used.</td></tr>
  <tr><td>Ice pellets</td><td><code>PL</code></td><td>Raindrops that refreeze while falling through a cold layer.</td><td>Fluid failure is hard to see, so special <em>allowance times</em> are used instead of holdover times.</td></tr>
  <tr><td>Hail / small hail</td><td><code>GR</code> / <code>GS</code></td><td>Ice formed in convective cloud.</td><td>No holdover time guidelines for hail; small hail has limited allowance times.</td></tr>
  <tr><td>Blowing snow</td><td><code>BLSN</code></td><td>Snow lifted from the ground by wind.</td><td>Re-contaminates treated surfaces and reduces visibility. Snow intensity is assessed from the falling snow only.</td></tr>
</table></div>
<p>The prefixes <code>-</code>, no sign and <code>+</code> indicate light, moderate and heavy intensity. Because intensity strongly affects holdover times, check it every time you read a report.</p>

<h2>Frost</h2>
<p>Frost forms when a surface cools to below the frost point of the surrounding air, typically on clear, calm nights through radiative cooling. It can also form on a wing that has been cold-soaked by very cold fuel, even when the air temperature is <strong>above</strong> 0 °C. This is <em>cold-soaked fuel frost</em> (CSFF). Frost that is still forming is called <strong>active frost</strong>, and it affects holdover times.</p>

<h2>Temperature inversions</h2>
<p>In winter, cold, dense air often collects in valleys and over high plateaus, with warmer air above. Inversions trap fog and low cloud for days and create the warm layer aloft that produces freezing rain. On the northern high plateaus and mountain airports of our network, an inversion can mean freezing fog at the field while the air a few thousand feet above is several degrees warmer.</p>

<h2>Reading the reports</h2>
<ul>
  <li><strong>METAR</strong>: check the weather group (e.g. <code>-FZDZ BR</code>), the temperature/dew point spread (a small spread means fog or frost is likely), and the runway state or runway condition information.</li>
  <li><strong>TAF</strong>: look for <code>TEMPO</code>, <code>BECMG</code> and <code>PROB</code> groups that bring freezing precipitation or snow within your departure or arrival window.</li>
  <li><strong>Trends</strong>: a falling temperature with a small dew point spread at dusk is the classic frost and freezing fog set-up.</li>
  <li><strong>Pilot reports, radar and satellite</strong> confirm what the reports suggest. A front or a terrain effect can change the precipitation type within minutes.</li>
</ul>
<div class="callout"><span class="label">Good practice</span><p>Brief the expected winter threats before departure: precipitation type and intensity, temperature trend, runway condition and de-icing plan. Update the brief whenever the weather changes.</p></div>
""",
takeaways=[
  "Supercooled droplets freeze on impact; they cause almost all airframe icing.",
  "Freezing rain needs a warm layer aloft; freezing drizzle and freezing fog do not.",
  "Precipitation type and intensity drive holdover times — check them every time.",
  "Cold-soaked fuel can create frost on wings even above 0 °C.",
],
check=dict(
  q="A METAR reports +SN. What does the “+” mean for your de-icing planning?",
  options=["Snow is ending soon", "Heavy snow — holdover times will be short or may not exist", "Snow mixed with rain", "Snow at the aerodrome but not on the runway"],
  answer=1,
  explain="“+” indicates heavy intensity. Heavy snow sharply reduces holdover times; for some fluids and temperatures no holdover time is published.",
),
),

# ---------------------------------------------------------------- 3
dict(
title="Frost, Ice and Snow — Types and Hazards",
minutes=8,
objectives=[
  "Identify the main forms of aircraft surface contamination.",
  "Describe the specific hazard of each contaminant.",
  "Recognise the conditions that produce clear ice on a cold-soaked wing.",
],
body="""
<h2>What counts as contamination</h2>
<p>Any frost, ice, snow or slush that adheres to or sits on an aircraft surface is contamination. Even a thin, smooth-looking layer changes the shape and roughness of the surface. The main types are listed below.</p>
<div class="table-wrap"><table>
  <tr><th>Contaminant</th><th>Description</th><th>Specific hazard</th></tr>
  <tr><td>Frost (hoar frost)</td><td>Thin, white crystalline deposit formed by direct deposition of water vapour.</td><td>Surface roughness. Even thin frost can significantly reduce lift and raise the stall speed.</td></tr>
  <tr><td>Cold-soaked fuel frost (CSFF)</td><td>Frost or ice on wing surfaces above or below fuel tanks containing very cold fuel.</td><td>Can form at positive air temperatures and on a clear day; it often appears on the lower wing surface first.</td></tr>
  <tr><td>Clear (glaze) ice</td><td>Transparent, smooth, hard ice from freezing rain or drizzle, or from rain on a cold-soaked wing.</td><td>Very difficult to see; may look like a wet wing. Can break off and be ingested by rear-mounted engines.</td></tr>
  <tr><td>Rime ice</td><td>Opaque, white, rough ice from small supercooled droplets (freezing fog).</td><td>Builds on leading edges, probes, fan blades and propellers.</td></tr>
  <tr><td>Dry snow</td><td>Fine snow that does not stick when the surface is cold. It can be blown off.</td><td>Sticks to a warm or wet surface and can melt and refreeze. Never assume it will blow off on take-off.</td></tr>
  <tr><td>Wet snow</td><td>Snow with high liquid water content, near 0 °C.</td><td>Adheres readily, adds weight, and dilutes anti-icing fluid very quickly.</td></tr>
  <tr><td>Slush</td><td>Water-saturated snow that splashes.</td><td>Thrown onto flaps, gear and engines during taxi; can refreeze in flight. On runways it causes drag and reduces braking.</td></tr>
</table></div>

<h2>Clear ice on a cold-soaked wing</h2>
<p>After a long flight at altitude, the fuel in the wing tanks can remain far below 0 °C for hours. If the aircraft is then exposed to rain, drizzle, fog or high humidity on the ground, the water freezes on the cold wing skin and forms <strong>clear ice</strong>. This can happen at outside air temperatures of +5 °C or more.</p>
<div class="callout caution"><span class="label">Watch for</span>
<p>The conditions are cold fuel (large fuel quantity left in the tanks after a long sector, or cold fuel uploaded), precipitation or high humidity, and air temperature near or above freezing. Clear ice cannot be reliably detected by eye — a <strong>tactile check</strong> by hand (or with an approved detection system) is required. See Lesson 12.</p>
</div>

<h2>Acceptable deposits</h2>
<p>Some AFMs permit specific, limited deposits. Typical examples are a thin layer of hoar frost on the upper fuselage, or CSFF on the lower wing surface in a defined area. These are <strong>exceptions written into the AFM</strong> for a particular type, with exact limits. If your AFM does not explicitly allow a deposit, it must be removed.</p>
<p>"Thin hoar frost" usually means a uniform white deposit thin enough that surface features — paint lines, markings and lettering — can still be seen through it.</p>
""",
takeaways=[
  "All frost, ice, snow and slush on critical surfaces is contamination.",
  "Clear ice looks like a wet wing; it must be checked by touch.",
  "Cold-soaked fuel can produce frost or clear ice well above 0 °C.",
  "Only deposits explicitly permitted by the AFM, within its limits, are acceptable.",
],
check=dict(
  q="An aircraft arrives after a long sector with plenty of fuel remaining. It is +4 °C with light drizzle. What is the main concern?",
  options=["Fuel freezing in the tanks", "Clear ice forming on the cold-soaked wing", "Brake overheating", "No concern — the temperature is above freezing"],
  answer=1,
  explain="Cold-soaked fuel keeps the wing skin below 0 °C; drizzle freezes on it as clear ice, which is hard to see and must be checked by touch.",
),
),

# ---------------------------------------------------------------- 4
dict(
title="Aircraft Icing — On the Ground and in Flight",
minutes=8,
objectives=[
  "Distinguish ground icing from in-flight icing.",
  "State the standard definition of icing conditions used for engine and wing anti-ice.",
  "Describe the main types and intensities of in-flight icing.",
],
body="""
<h2>Ground icing</h2>
<p>On the ground the aircraft is exposed to precipitation, frost, freezing fog and slush from taxiways for as long as it is parked or taxiing. Ground icing is managed with <strong>de-icing and anti-icing fluids</strong> and inspections. The aircraft's own ice protection systems are <strong>not designed</strong> to clean wings on the ground.</p>
<p>Main sources:</p>
<ul>
  <li>Frost and freezing fog on parked aircraft;</li>
  <li>Falling snow, freezing rain, drizzle and ice pellets;</li>
  <li>Cold-soaked fuel frost and clear ice;</li>
  <li>Slush and spray from taxiways and runways;</li>
  <li>Blowing snow and snow blown by other aircraft's jet blast.</li>
</ul>

<h2>Icing conditions — the standard definition</h2>
<div class="callout info"><span class="label">Definition (typical AFM wording)</span>
<p>Icing conditions exist when the outside air temperature (on the ground and for take-off) or total air temperature (in flight) is <strong>10 °C or below</strong>, and visible moisture in any form is present — cloud, fog with visibility of 1 600 m (1 statute mile) or less, rain, snow, sleet or ice crystals.</p>
<p>On the ground, icing conditions also exist when the OAT is 10 °C or below and there is snow, ice, standing water or slush on ramps, taxiways or runways that may be ingested by the engines or freeze on engines, nacelles or engine sensor probes.</p>
</div>
<p>This definition tells you when to use <strong>engine anti-ice</strong> (and, in flight, wing anti-ice according to the AFM). Always use the exact wording and limits in your own AFM/FCOM.</p>

<h2>In-flight icing</h2>
<div class="table-wrap"><table>
  <tr><th>Type</th><th>Conditions</th><th>Appearance</th></tr>
  <tr><td>Rime</td><td>Small droplets, colder temperatures, stratiform cloud</td><td>Opaque, white, rough; forms on leading edges</td></tr>
  <tr><td>Clear (glaze)</td><td>Large droplets, temperatures near 0 °C to about −10 °C, cumuliform cloud or freezing rain</td><td>Transparent, dense; can run back and form horns or ridges</td></tr>
  <tr><td>Mixed</td><td>Combination of the above</td><td>Rough and partly clear</td></tr>
  <tr><td>Supercooled large droplets (SLD)</td><td>Freezing drizzle and freezing rain</td><td>Ice forms <strong>behind</strong> the protected areas, where ice protection systems cannot remove it</td></tr>
</table></div>
<p>Pilots report icing intensity as <strong>trace, light, moderate or severe</strong>. Severe icing is a rate at which the ice protection systems cannot reduce or control the hazard; immediate exit from the conditions is required.</p>

<h2>Why the distinction matters</h2>
<p>Ground contamination affects the whole upper surface of the wing and tail, which is where lift is generated. In-flight ice protection systems only protect leading edges, engine inlets, probes and windows. A wing that leaves the ground contaminated cannot be cleaned by switching on anti-ice.</p>
""",
takeaways=[
  "Icing conditions: OAT/TAT 10 °C or below with visible moisture, or contaminated surfaces on the ground.",
  "Ground icing is removed with fluids — not with the aircraft's ice protection systems.",
  "SLD forms ice behind protected areas; exit the conditions.",
],
check=dict(
  q="On the ground the OAT is +8 °C and there is slush on the taxiways but no precipitation. Are icing conditions present?",
  options=["No — there is no visible moisture in the air", "Yes — slush that may be ingested at OAT 10 °C or below counts as icing conditions", "Only if the temperature falls below 0 °C", "Only at night"],
  answer=1,
  explain="On the ground, snow, ice, standing water or slush on surfaces that may be ingested, with OAT 10 °C or below, meets the typical icing conditions definition.",
),
),

# ---------------------------------------------------------------- 5
dict(
title="The Clean Aircraft Concept",
minutes=9,
objectives=[
  "State the Clean Aircraft Concept and its regulatory basis.",
  "List the critical surfaces that must be free of contamination.",
  "Explain the aerodynamic effects of contamination on lift, drag, stall and control.",
],
body="""
<h2>The rule</h2>
<div class="callout warn"><span class="label">Clean Aircraft Concept</span>
<p>No one may take off in an aircraft with frost, ice, snow or slush adhering to the wings, control surfaces, propellers, engine inlets or other critical surfaces, except as specifically permitted by the AFM.</p>
</div>
<p>This principle appears in ICAO Annex 6, EASA Air Operations (CAT.OP.MPA.250), FAA 14 CFR 121.629 and the Domestic Airlines Operations Manual. There is no "small amount is acceptable" rule. The commander has the final responsibility for making sure the aircraft is clean.</p>

<h2>Critical surfaces</h2>
<ul>
  <li>Wings: upper and lower surfaces, leading-edge devices (slats), flaps and spoilers;</li>
  <li>Horizontal and vertical stabilisers, elevators and rudder;</li>
  <li>Ailerons and all other control surfaces, including their gaps and hinges;</li>
  <li>Propellers, engine inlets and fan blades;</li>
  <li>Upper fuselage on aircraft with rear-mounted engines (ice shed into the engines);</li>
  <li>Air data probes and static ports, angle-of-attack vanes and ice detectors;</li>
  <li>Landing gear, gear doors and fuel tank vents.</li>
</ul>

<h2>What contamination does</h2>
<p>Research and accident investigations show that frost, ice or snow with roughness similar to <strong>medium or coarse sandpaper</strong> on the wing upper surface can:</p>
<ul>
  <li>reduce maximum lift by up to about <strong>30 %</strong>;</li>
  <li>increase drag by up to about <strong>40 %</strong>;</li>
  <li>reduce the stall angle of attack, so the wing stalls at a <strong>lower angle</strong> and a <strong>higher speed</strong>;</li>
  <li>cause stall <strong>without warning</strong>, because stall warning systems are scheduled for a clean wing;</li>
  <li>cause asymmetric lift and roll-off at or just after rotation;</li>
  <li>restrict or jam control surfaces, and increase weight;</li>
  <li>break off and damage engines, especially rear-mounted engines.</li>
</ul>
""" + LIFT_CURVE_SVG + """
<h2>Why take-off is the critical moment</h2>
<p>At rotation the aircraft is heavy, slow and pitching to a high angle of attack, close to the ground. This is exactly where contamination removes the safety margin. A contaminated aircraft may rotate normally and then fail to climb, roll uncommanded, or stall in ground effect before the stall warning activates.</p>
<div class="callout caution"><span class="label">Remember</span><p>Do not assume contamination will blow off during the take-off roll. Snow and frost that look loose may be frozen to the surface underneath.</p></div>
""",
takeaways=[
  "No frost, ice, snow or slush on critical surfaces at take-off — unless the AFM explicitly allows it.",
  "Sandpaper-like roughness: up to ~30 % less lift and ~40 % more drag.",
  "A contaminated wing can stall before the stall warning activates.",
  "The commander has the final responsibility for a clean aircraft.",
],
check=dict(
  q="Why might a contaminated wing stall without any stall warning?",
  options=["The stall warning system is inhibited on the ground", "Contamination lowers the stall angle of attack below the angle at which the warning is set for a clean wing", "Anti-icing fluid blocks the angle-of-attack vanes", "Stall warning only works with flaps retracted"],
  answer=1,
  explain="Stall warning is scheduled for a clean wing. Contamination lowers the critical angle of attack, so the wing can stall before the warning angle is reached.",
),
),

# ---------------------------------------------------------------- 6
dict(
title="De-icing and Anti-icing Principles",
minutes=8,
objectives=[
  "Distinguish de-icing from anti-icing.",
  "Describe one-step and two-step procedures and when holdover time starts.",
  "Identify the main safety considerations for treatment.",
],
body="""
<h2>Two different jobs</h2>
<ul>
  <li><strong>De-icing</strong> removes frost, ice, snow or slush from the aircraft so that surfaces are clean. It is normally done with heated fluid (often Type I, or diluted Type II/IV), at a minimum of 60 °C at the nozzle. Hot water may be used at some temperatures if the procedure allows it. Some facilities use forced air or infrared heating.</li>
  <li><strong>Anti-icing</strong> protects clean surfaces against new accumulation for a limited period — the <strong>holdover time</strong>. It is normally done with thickened fluid (Type II, III or IV), applied unheated or heated, onto a surface that is already clean.</li>
</ul>
<p>When no precipitation is falling and no frost is forming, de-icing alone may be enough. When precipitation is falling, or is expected before take-off, anti-icing is required.</p>

<h2>One-step and two-step procedures</h2>
<p><strong>One-step:</strong> a single application of heated, freezing-point-depressant (FPD) fluid cleans the aircraft and leaves a protective film. It is used when the expected holdover time from that fluid is enough.</p>
<p><strong>Two-step:</strong> the first step removes the contamination; the second step applies an anti-icing fluid for longer protection. The second step must be applied <strong>before the first-step fluid freezes</strong> — typically within <strong>3 minutes</strong> — and treatment is done area by area if necessary.</p>
""" + STEP_SVG + """
<h2>Safety principles</h2>
<ul>
  <li>The aircraft must be configured as the AFM and de-icing procedures require before spraying starts (Lesson 9).</li>
  <li>No aircraft movement, engine power change or configuration change during treatment unless the de-icing crew is told and agrees.</li>
  <li>Treatment must be symmetrical: if one wing is treated, the other wing must receive the same treatment.</li>
  <li>Fluid makes the ramp extremely slippery for people and vehicles.</li>
  <li>Glycol fumes in the cabin or flight deck must be prevented by switching off bleed air as required; report any smell or smoke.</li>
  <li>A <strong>post de-icing/anti-icing check</strong> is mandatory after treatment (Lesson 12).</li>
</ul>

<h2>Responsibilities</h2>
<p>The de-icing service provider is responsible for the quality of the treatment and the post-treatment check. The commander remains responsible for accepting the aircraft as clean and for deciding whether it remains clean until take-off.</p>
""",
takeaways=[
  "De-icing removes contamination; anti-icing prevents new accumulation for a limited time.",
  "Two-step: second step within about 3 minutes, before the first-step fluid freezes.",
  "Holdover time starts at the beginning of the final application.",
  "Treatment must be symmetrical, and a post-treatment check is mandatory.",
],
check=dict(
  q="In a two-step procedure, when does the holdover time start?",
  options=["At the start of step one", "At the end of step one", "At the beginning of step two (the final anti-icing application)", "When the aircraft starts to taxi"],
  answer=2,
  explain="Holdover time always starts at the beginning of the final (anti-icing) application.",
),
),

# ---------------------------------------------------------------- 7
dict(
title="De-icing and Anti-icing Fluids: Types I, II, III and IV",
minutes=9,
objectives=[
  "Compare the four SAE fluid types by composition, colour, use and holdover time.",
  "Explain fluid concentration and the Lowest Operational Use Temperature (LOUT).",
  "Recognise problems caused by thickened fluid residues.",
],
body="""
<h2>The four fluid types</h2>
<p>Aircraft de-icing/anti-icing fluids are mainly glycol (propylene or ethylene) and water. They are qualified to SAE specifications: <strong>AMS1424</strong> for Type I and <strong>AMS1428</strong> for Types II, III and IV.</p>
<div class="table-wrap"><table>
  <tr><th>Type</th><th>Thickened?</th><th>Typical colour</th><th>Main use</th><th>Relative holdover time</th></tr>
  <tr><td><strong>I</strong></td><td>No — low viscosity, flows off quickly</td><td>Orange</td><td>De-icing (heated); short-term protection</td><td>Short</td></tr>
  <tr><td><strong>II</strong></td><td>Yes (pseudoplastic)</td><td>Colourless to pale yellow</td><td>Anti-icing for aircraft with rotation speeds above about 100 kt</td><td>Medium to long</td></tr>
  <tr><td><strong>III</strong></td><td>Yes</td><td>Bright yellow</td><td>Anti-icing for aircraft with lower rotation speeds (about 60 kt and above); some are approved heated for de-icing</td><td>Between I and II</td></tr>
  <tr><td><strong>IV</strong></td><td>Yes</td><td>Green</td><td>Anti-icing for aircraft with rotation speeds above about 100 kt</td><td>Longest</td></tr>
</table></div>
<p>Thickened fluids stay on the wing while the aircraft is stationary, then thin and <strong>shear off</strong> under the airflow of the take-off roll, so that the wing is clean at rotation. This is why a thickened fluid is only approved for aircraft whose take-off speed is high enough for it to flow off, as tested in the aerodynamic acceptance test. Use only fluids approved for your aircraft type.</p>

<h2>Concentration</h2>
<p>Fluids are applied neat or mixed with water. The mix is written as <em>fluid/water</em>:</p>
<ul>
  <li><strong>100/0</strong> — neat fluid, longest protection;</li>
  <li><strong>75/25</strong> — three parts fluid, one part water;</li>
  <li><strong>50/50</strong> — half fluid, half water, shortest protection, warmer temperatures only.</li>
</ul>
<p>Type I is always diluted for use, according to the temperature.</p>

<h2>Lowest Operational Use Temperature (LOUT)</h2>
<p>Each fluid and mix has a LOUT. It is the <strong>higher</strong> of:</p>
<ul>
  <li>the temperature at which the fluid passes the aerodynamic acceptance test for the aircraft category, and</li>
  <li>the fluid's freezing point plus a buffer — <strong>10 °C for Type I</strong> and <strong>7 °C for Types II, III and IV</strong>.</li>
</ul>
<p>A fluid must not be used at an OAT (or aircraft skin temperature, if lower) below its LOUT.</p>

<h2>Fluid residues</h2>
<p>Repeated application of thickened fluids — particularly with one-step treatments using Type II or IV — can leave <strong>dried residue</strong> in aerodynamically quiet areas: control surface gaps, hinges, balance bays and trailing edges. The residue can rehydrate in rain or humidity, swell into a gel and <strong>freeze at altitude</strong>, restricting flight controls. Report any stiff or unusual control feel to maintenance (Lesson 23).</p>

<h2>Handling cautions</h2>
<ul>
  <li>Do not spray thickened fluid onto cockpit windows — it smears and reduces visibility.</li>
  <li>Fluids are slippery and environmentally controlled; follow ramp and environmental rules.</li>
  <li>Fluid brands within a type have different holdover times. Use the brand-specific table when the fluid name is known.</li>
</ul>
""",
takeaways=[
  "Type I: unthickened, orange, de-icing, short protection. Types II and IV: thickened, longer protection, for faster aircraft. Type III: for lower rotation speeds.",
  "Concentration is written fluid/water — 100/0 gives the longest protection.",
  "LOUT: freezing point + 10 °C (Type I) or + 7 °C (II/III/IV), or the aerodynamic limit, whichever is higher.",
  "Thickened fluid residues can freeze in control surface gaps.",
],
check=dict(
  q="Which fluid normally provides the longest holdover time?",
  options=["Type I", "Type II 50/50", "Type IV 100/0", "Hot water"],
  answer=2,
  explain="Neat (100/0) Type IV fluid normally provides the longest protection.",
),
),

# ---------------------------------------------------------------- 8
dict(
title="Holdover Times and Allowance Times",
minutes=10,
objectives=[
  "Define holdover time and explain its limits.",
  "Use holdover time guidelines correctly, step by step.",
  "Explain allowance times for ice pellets and small hail, and the factors that shorten protection.",
],
body="""
<h2>Definition</h2>
<p><strong>Holdover time (HOT)</strong> is the <em>estimated</em> time for which an anti-icing fluid will prevent frost or ice from forming and snow from accumulating on the treated surfaces of an aircraft. It starts at the <strong>beginning of the final application</strong> of fluid and ends when the fluid is expected to lose its effectiveness (fluid failure).</p>
<p>HOT guidelines are published each winter season by the FAA and Transport Canada and are used worldwide. The Domestic Airlines Operations Manual states which tables crews must use. Tables change every year, so always use the current season's tables.</p>

<div class="callout warn"><span class="label">Holdover time is a guideline, not a guarantee</span>
<p>Tables are based on tests in controlled conditions. Heavy precipitation, high moisture content, strong wind, jet blast, and an aircraft skin colder than the air all shorten the real protection time. If the surfaces show signs of contamination, the aircraft is not clean, however much holdover time remains.</p>
</div>

<h2>Using the tables — step by step</h2>
<ol class="steps">
  <li><strong>Identify the fluid</strong> from the anti-icing code: type, brand if known, and concentration (e.g. Type IV, 100/0).</li>
  <li><strong>Select the correct table</strong> — brand-specific if the fluid is known, otherwise the generic table for that type.</li>
  <li><strong>Find the OAT row.</strong> Use the outside air temperature, and check it is not below the fluid's LOUT.</li>
  <li><strong>Find the precipitation column</strong> — frost, freezing fog, snow/snow grains, freezing drizzle, light freezing rain, rain on a cold-soaked wing. Assess snow intensity from the <em>snowfall intensity as a function of visibility</em> table, not just from the METAR.</li>
  <li><strong>Read the time range.</strong> The <em>shorter</em> value applies to the heavier end of that intensity category, the <em>longer</em> value to the lighter end. Use the shorter time when conditions are at the heavier end or uncertain.</li>
  <li><strong>Note the start time</strong> from the anti-icing code and calculate when the HOT ends. Write it down and brief it.</li>
  <li><strong>Keep reassessing.</strong> If the precipitation type or intensity changes, recalculate. If no HOT exists for the new conditions, the aircraft must return for treatment.</li>
</ol>

<h2>When holdover time is exceeded</h2>
<p>If the HOT has run out before take-off, take-off is only permitted if a <strong>pre-take-off contamination check</strong> shows the critical surfaces are clean, carried out within 5 minutes before beginning the take-off (Lesson 13). Otherwise the aircraft must be re-treated.</p>

<h2>Allowance times</h2>
<p>In <strong>ice pellets</strong> and <strong>small hail</strong>, and mixes of these with other precipitation, fluid failure is difficult to see. Instead of holdover times, the tables give <strong>allowance times</strong> for specific Type III and Type IV fluids. Allowance times:</p>
<ul>
  <li>start at the beginning of the final application, like a HOT;</li>
  <li><strong>cannot be extended</strong> by a pre-take-off contamination check — when the allowance time is exceeded, the aircraft must be re-treated;</li>
  <li>may carry extra restrictions, such as maximum rotation speed or limits on flap configuration.</li>
</ul>

<h2>Conditions with no holdover time</h2>
<p>No HOT guidelines exist for <strong>moderate or heavy freezing rain</strong>, <strong>hail</strong>, or <strong>heavy ice pellets</strong>. Take-off in these conditions is generally not authorised. Check the Operations Manual for heavy snow, which has guidelines for some fluids only.</p>
""",
takeaways=[
  "HOT starts at the beginning of the final application and is only an estimate.",
  "Use the current season's tables, the correct fluid and concentration, OAT and precipitation type/intensity.",
  "HOT exceeded → pre-take-off contamination check within 5 minutes of take-off, or re-treat.",
  "Allowance times (ice pellets, small hail) cannot be extended — re-treat when they expire.",
],
check=dict(
  q="An allowance time for ice pellets has expired while you hold for take-off. What is the correct action?",
  options=["Carry out a pre-take-off contamination check and depart if clean", "Depart immediately because ice pellets bounce off", "Return for re-treatment", "Switch on wing anti-ice and depart"],
  answer=2,
  explain="Allowance times cannot be extended by a pre-take-off contamination check. When the allowance time expires, the aircraft must be re-treated.",
),
),

# ---------------------------------------------------------------- 9
dict(
title="Preparing the Aircraft and Protecting Sensitive Areas",
minutes=8,
objectives=[
  "Configure the aircraft for de-icing according to the AFM/FCOM.",
  "Identify areas that must not be sprayed directly.",
  "Describe good application practice from the crew's point of view.",
],
body="""
<h2>Typical aircraft configuration for treatment</h2>
<p>Each aircraft type has a de-icing configuration in the FCOM or the company manuals. Typical items are:</p>
<ul>
  <li><strong>Parking brake set</strong> (or brakes held as the pad procedure requires) and the aircraft stationary;</li>
  <li><strong>Engines</strong> shut down or at idle, as the AFM and the facility procedure require; <strong>APU</strong> running if required;</li>
  <li><strong>Air conditioning packs and APU bleed off</strong> (or as specified) to prevent fluid fumes entering the cabin and flight deck;</li>
  <li><strong>Flaps and slats</strong> retracted, unless the AFM requires another setting;</li>
  <li><strong>Flight controls neutral</strong>, and stabiliser trim as specified;</li>
  <li><strong>Doors and windows closed</strong>;</li>
  <li>Probe/window heat and other systems as the FCOM specifies.</li>
</ul>
<p>Confirm the configuration to the de-icing crew before spraying begins (Lesson 10).</p>

<h2>Areas that must not be sprayed directly</h2>
<div class="table-wrap"><table>
  <tr><th>Area</th><th>Why</th></tr>
  <tr><td>Pitot probes, static ports, AoA vanes, TAT probes, ice detectors</td><td>Fluid residue causes erroneous air data and warnings</td></tr>
  <tr><td>Engine inlets, exhausts, thrust reversers; APU inlet and exhaust</td><td>Fluid ingestion causes fumes and smoke in the cabin, and possible engine damage</td></tr>
  <tr><td>Cockpit and cabin windows</td><td>Thickened fluid smears and reduces visibility</td></tr>
  <tr><td>Brakes and wheels</td><td>Fluid on hot brakes can catch fire or produce smoke</td></tr>
  <tr><td>Landing gear bays, electrical connectors and antennas</td><td>Contamination of components and connectors</td></tr>
  <tr><td>Control surface gaps and balance bays (high-pressure spray)</td><td>Forces contamination and fluid into gaps, where residue can collect and freeze</td></tr>
</table></div>

<h2>Good application practice</h2>
<p>De-icing crews follow their own procedures (SAE AS6285). As a crew member it helps to know what "good" looks like:</p>
<ul>
  <li>Spraying generally works from the highest point downward and from the leading edge rearward, so that contamination is pushed off the aircraft, not onto clean areas.</li>
  <li>Hot fluid is used close to the surface for de-icing, to transfer heat. Anti-icing fluid is applied as an even, complete layer.</li>
  <li>Both sides of the aircraft are treated in the same way.</li>
  <li>The vertical and horizontal stabilisers, which you cannot see from the flight deck, are treated and checked.</li>
  <li>Treatment of the fuselage depends on the AFM and conditions. On rear-engine aircraft the upper fuselage is a critical surface.</li>
</ul>
<div class="callout caution"><span class="label">During treatment</span><p>Do not change configuration, move control surfaces, change engine power or move the aircraft until the de-icing crew confirms that all personnel and equipment are clear.</p></div>
""",
takeaways=[
  "Configure the aircraft exactly as the FCOM specifies before spraying starts.",
  "Packs and APU bleed off (or as specified) prevent glycol fumes in the cabin.",
  "No direct spray on probes, engine and APU inlets, windows, brakes or control surface gaps.",
  "No movement or configuration change until the de-icing crew confirms all clear.",
],
check=dict(
  q="Why are the air conditioning packs and APU bleed normally switched off during de-icing?",
  options=["To save fuel", "To prevent glycol fumes entering the cabin and flight deck", "To keep the engines warm", "To reduce noise for the de-icing crew"],
  answer=1,
  explain="Fluid drawn into the APU or engine inlets would be carried into the air conditioning system and cause fumes or smoke in the cabin and flight deck.",
),
),

# ---------------------------------------------------------------- 10
dict(
title="Communication with the De-icing Crew and the Anti-icing Code",
minutes=8,
objectives=[
  "Use a structured communication sequence before, during and after treatment.",
  "Read and record the anti-icing code.",
  "Apply closed-loop communication under time pressure.",
],
body="""
<h2>Why communication matters</h2>
<p>The flight crew cannot see most of what happens during de-icing. The de-icing crew cannot see inside the flight deck. Several accidents and serious incidents happened because one side assumed what the other was doing — engines moved while people were near the aircraft, or an aircraft taxied with parts of it untreated. Communication must follow a standard sequence and use closed-loop read-back.</p>

<h2>Before treatment</h2>
<ul>
  <li>Establish contact on the agreed radio frequency or interphone.</li>
  <li>The crew confirms the aircraft is configured for de-icing and the brakes are set.</li>
  <li>Agree the treatment: de-icing only, one-step or two-step, fluid type and concentration, and the areas to treat.</li>
  <li>Make a PA to the passengers (and inform cabin crew) that de-icing is about to begin; they will hear noise and may smell fluid.</li>
</ul>

<h2>After treatment — the anti-icing code</h2>
<p>When treatment and the post-treatment check are complete, the de-icing crew passes the <strong>anti-icing code</strong>. The SAE AS6285 format contains:</p>
<ol>
  <li>Fluid type (I, II, III or IV);</li>
  <li>Concentration, as fluid/water percentage (not needed for Type I);</li>
  <li>Local time at the <strong>beginning</strong> of the final application;</li>
  <li>Date (written record);</li>
  <li>The statement “post de-icing/anti-icing check completed”.</li>
</ol>
<p>Where a brand name is known, it may also be given so you can use brand-specific tables.</p>

<div class="dialog" data-skip-narration>
  <p><b>De-icing crew:</b> “Domestic 247, treatment complete. Anti-icing code: Type four, one hundred percent, start time one four three five, post de-icing anti-icing check completed.”</p>
  <p><b>Flight crew:</b> “Type four, one hundred, one four three five, check completed — Domestic 247.”</p>
  <p><b>De-icing crew:</b> “All personnel and equipment clear. Contact ground on one two one decimal niner.”</p>
  <p><b>Flight crew:</b> “Clear, ground one two one decimal niner, Domestic 247.”</p>
</div>
<p class="muted">Example only — use the phraseology in the Operations Manual and the local de-icing procedures.</p>

<h2>Using the code</h2>
<ul>
  <li>Read the code back in full. Write it on the flight log or enter it as the company procedure requires.</li>
  <li>Calculate the HOT using the fluid, concentration and current conditions, and brief the end time.</li>
  <li>Do not move the aircraft, start engines or change configuration until the "all clear" call.</li>
</ul>

<div class="callout"><span class="label">Under time pressure</span><p>De-icing usually happens at the busiest moment of a winter departure. Slow down: use standard phrases, read back every number, and ask again if anything is unclear. Thirty seconds of clarification is cheaper than a return to the pad — or an accident.</p></div>
""",
takeaways=[
  "Confirm configuration, brakes set and the treatment plan before spraying starts.",
  "Anti-icing code: fluid type, concentration, start time of final step, date, check completed.",
  "Read back the code and calculate HOT from the start time of the final application.",
  "Do not move until the de-icing crew calls “all personnel and equipment clear”.",
],
check=dict(
  q="Which time in the anti-icing code do you use to calculate holdover time?",
  options=["The time the de-icing truck arrived", "The time treatment finished", "The local time at the beginning of the final application", "The time you received the code"],
  answer=2,
  explain="The anti-icing code gives the local start time of the final application, which is when holdover time begins.",
),
),
]
