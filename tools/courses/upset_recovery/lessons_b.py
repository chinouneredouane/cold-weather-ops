# Upset Prevention and Recovery — lessons 9–16
from .diagrams import energy, pitch_power, cg_effects, windshear, wake, somatogravic

LESSONS_B = [
# ---------------------------------------------------------------- 9
dict(
title="Aeroplane Certification and the Flight Envelope",
minutes=7,
objectives=[
  "Describe what certification does — and does not — demonstrate about aircraft handling.",
  "Identify the main speed and load limits of the flight envelope.",
  "Explain why upset recovery may take the aircraft outside the conditions tested in certification.",
],
body="""
<h2>What certification demonstrates</h2>
<p>Transport aeroplanes are certified to standards such as CS-25 and FAR Part 25. Test pilots demonstrate that, within the <strong>normal flight envelope</strong>, the aeroplane has adequate stability, controllability, stall warning and stall characteristics, and the required structural strength.</p>
<p>Certification does <strong>not</strong> demonstrate:</p>
<ul>
  <li>recovery from every possible attitude — such as inverted flight or very high bank;</li>
  <li>behaviour far beyond the stall, at extreme sideslip, or combined with failures;</li>
  <li>how an average line pilot performs when startled at night.</li>
</ul>
<p>Upsets can therefore take the aircraft into conditions where its behaviour is <strong>less well known</strong> — and where simulator data may also be limited (Lesson 24).</p>

<h2>The flight envelope</h2>
<div class="table-wrap"><table>
  <tr><th>Limit</th><th>Meaning</th></tr>
  <tr><td>V<sub>MO</sub> / M<sub>MO</sub></td><td>Maximum operating speed / Mach number — not to be deliberately exceeded</td></tr>
  <tr><td>V<sub>D</sub> / M<sub>D</sub></td><td>Design dive speed — demonstrated in flight test, with structural margin; not for line use</td></tr>
  <tr><td>V<sub>A</sub></td><td>Design manoeuvring speed — full deflection of one control in one axis is acceptable below it (Lesson 6)</td></tr>
  <tr><td>V<sub>FE</sub>, V<sub>LE</sub>, V<sub>LO</sub></td><td>Flap and landing gear speed limits</td></tr>
  <tr><td>V<sub>S1g</sub> / V<sub>SR</sub></td><td>Reference stall speed — the basis for take-off and approach speeds</td></tr>
  <tr><td>Load factor limits</td><td>Typically +2.5 / −1.0 g clean, +2.0 / 0 g with flaps extended</td></tr>
</table></div>

<h2>Margins in normal operation</h2>
<ul>
  <li>Operating speeds include margins above the stall: for example, the final approach reference speed is typically about 1.23 × V<sub>SR</sub> in the landing configuration.</li>
  <li>Manoeuvring speeds for each flap setting, and the speed bands on the PFD, show the safe range for normal manoeuvres.</li>
  <li>The buffet margin at cruise (Lesson 7) protects against turbulence and bank.</li>
</ul>
<p>These margins are what prevention protects. Most developing upsets begin as an erosion of one of these margins — usually speed.</p>

<div class="callout"><span class="label">In a recovery</span><p>Exceeding a speed or load limit to save the aircraft is acceptable when there is no alternative — but avoid it if you can, and report any exceedance so that maintenance can inspect the aircraft.</p></div>
""",
takeaways=[
  "Certification demonstrates behaviour within the normal envelope, not every possible upset.",
  "Know VMO/MMO, VA, flap/gear limits, stall reference speed and g limits.",
  "Operating speeds include margins; most upsets start with an eroded margin.",
  "Report any limit exceedance after a recovery.",
],
check=dict(
  q="Which statement about certification is correct?",
  options=["Certification proves recovery from any attitude", "Certification demonstrates handling within the normal flight envelope, not every upset condition", "Certification tests are done with startled line pilots", "VD may be used in normal line operations"],
  answer=1,
  explain="Certification demonstrates stability, control and stall behaviour within the normal envelope. Extreme upset conditions may be outside what was tested.",
),
),

# ---------------------------------------------------------------- 10
dict(
title="Energy Management and Pitch-Power Coupling",
minutes=8,
objectives=[
  "Describe aircraft energy states and how pitch, thrust and drag change them.",
  "Explain the effect of underwing engines on pitch.",
  "Apply energy awareness to prevention and recovery.",
],
body="""
<h2>Energy states</h2>
""" + energy() + """
<p>An aircraft's total energy is the sum of its <strong>potential energy</strong> (altitude) and <strong>kinetic energy</strong> (airspeed). Pitch exchanges one for the other. Only <strong>thrust and drag</strong> change the total. Common unsafe energy states:</p>
<ul>
  <li><strong>Low energy</strong> — low speed and low altitude, for example after a speed decay on approach. Few options remain.</li>
  <li><strong>High energy</strong> — high speed in a descent, for example in a nose-low upset. The risk is overspeed and structural overload.</li>
  <li><strong>Mismatch</strong> — high pitch with decaying speed (the energy is going into the climb), or low thrust with a level attitude.</li>
</ul>

<h2>Thrust response</h2>
<ul>
  <li>Jet engines take several seconds to accelerate from idle. Thrust is not an instant cure for a low-energy state — anticipate.</li>
  <li>At high altitude, excess thrust is small (Lesson 7).</li>
  <li>On the "back side" of the drag curve, below minimum drag speed, slowing down <em>increases</em> drag and the thrust needed. Speed can decay quickly if not corrected.</li>
</ul>

<h2>Pitch-power coupling</h2>
""" + pitch_power() + """
<p>With engines mounted below the wing, the thrust line is below the centre of gravity. Increasing thrust produces a <strong>nose-up</strong> pitching moment; reducing thrust produces a nose-down moment. Expect it during a go-around, and in recoveries:</p>
<ul>
  <li>In a <strong>nose-high, low-speed</strong> situation, high thrust can make it harder to lower the nose. Reducing thrust may be necessary to regain pitch control.</li>
  <li>In a <strong>stall recovery</strong>, adding thrust too early can work against the nose-down input.</li>
  <li>A go-around with full thrust from a low speed produces a strong pitch-up; follow the pitch target and trim as required.</li>
</ul>

<h2>Speedbrakes and configuration</h2>
<p>Speedbrakes increase drag and, on many types, the stall speed. They are a tool for high-energy situations — such as a nose-low, high-speed upset — but should be retracted in a low-energy situation or stall recovery. Do not change the flap or gear configuration in a recovery unless the procedure requires it.</p>
""",
takeaways=[
  "Total energy = altitude + speed. Pitch exchanges them; thrust and drag change the total.",
  "Jet thrust takes time to build — anticipate low-energy situations.",
  "Underwing engines: more thrust = nose-up moment; less thrust = nose-down.",
  "Speedbrakes for high energy only; retract them in a stall recovery.",
],
check=dict(
  q="In a nose-high, low-speed situation on an aircraft with underwing engines, why may thrust need to be reduced?",
  options=["To save fuel", "Because high thrust creates a nose-up moment that resists lowering the nose", "To increase the stall speed", "To engage the autopilot"],
  answer=1,
  explain="The thrust line below the CG produces a nose-up moment. Reducing thrust helps the elevator lower the nose.",
),
),

# ---------------------------------------------------------------- 11
dict(
title="Weight and Balance Effects",
minutes=7,
objectives=[
  "Explain how weight affects stall speed, performance and buffet margin.",
  "Describe the effects of forward and aft centre of gravity on stability and control.",
  "Recognise how loading errors can contribute to an upset.",
],
body="""
<h2>Weight</h2>
<ul>
  <li>Stall speed increases with the square root of weight. A heavier aircraft must fly faster for the same margin.</li>
  <li>At high altitude, higher weight reduces the buffet margin and the maximum altitude (Lesson 7).</li>
  <li>Climb performance and acceleration are lower at high weight — less energy is available in a recovery.</li>
  <li>An incorrect weight entered in the FMS produces incorrect speeds, which can erode the stall margin from take-off onwards.</li>
</ul>

<h2>Centre of gravity</h2>
""" + cg_effects() + """
<div class="table-wrap"><table>
  <tr><th></th><th>Forward CG</th><th>Aft CG</th></tr>
  <tr><td>Longitudinal stability</td><td>Greater</td><td>Reduced</td></tr>
  <tr><td>Pitch control forces</td><td>Heavier</td><td>Lighter — easy to over-control</td></tr>
  <tr><td>Stall speed</td><td>Slightly higher</td><td>Slightly lower</td></tr>
  <tr><td>Elevator authority</td><td>More needed to rotate and flare</td><td>Less nose-down authority for stall recovery</td></tr>
  <tr><td>Fuel consumption</td><td>Slightly higher (more tail down-force)</td><td>Slightly lower</td></tr>
</table></div>

<h2>Loading errors</h2>
<ul>
  <li>Cargo or passengers loaded differently from the load sheet can move the CG outside the envelope.</li>
  <li>Unsecured cargo that shifts during rotation or in turbulence can cause a sudden, large pitch change.</li>
  <li>Incorrect trim settings for take-off — from a wrong CG — can cause an early or late rotation and a nose-high or tail-strike situation.</li>
</ul>
<div class="callout"><span class="label">Prevention</span><p>Check the load sheet and the FMS entries carefully, cross-check weight and CG with the fuel and passenger figures, and be alert to unusual control forces at rotation. If the aircraft does not feel right, say so.</p></div>
""",
takeaways=[
  "Higher weight: higher stall speed, lower buffet margin, less excess energy.",
  "Aft CG: less stable, lighter forces, less nose-down authority. Forward CG: heavier forces, higher stall speed.",
  "Loading and FMS weight errors erode margins before the flight begins.",
],
check=dict(
  q="What is a typical effect of an aft centre of gravity?",
  options=["Heavier pitch control forces", "Reduced longitudinal stability and lighter pitch forces", "Higher stall speed", "More nose-down elevator authority"],
  answer=1,
  explain="An aft CG reduces stability and makes pitch forces lighter, so the aircraft is easier to over-control.",
),
),

# ---------------------------------------------------------------- 12
dict(
title="Environmental Threats",
minutes=9,
objectives=[
  "Describe the upset hazards of turbulence, mountain waves, windshear, wake turbulence, thunderstorms and icing.",
  "Apply avoidance strategies for each.",
  "State the main actions for windshear and wake encounters.",
],
body="""
<h2>Turbulence and mountain waves</h2>
<ul>
  <li><strong>Severe turbulence</strong> and clear-air turbulence can cause large, rapid attitude and altitude changes. Use the recommended turbulence penetration speed, keep seat belts fastened, and avoid large control inputs. The autopilot may remain engaged unless the procedure says otherwise.</li>
  <li><strong>Mountain waves</strong> — strong winds across ridges create waves with powerful up- and downdrafts, sometimes marked by lenticular clouds. They can exceed the climb capability of the aircraft and cause speed excursions at high altitude.</li>
</ul>

<h2>Windshear and microbursts</h2>
""" + windshear() + """
<ul>
  <li><strong>Avoid</strong> — delay take-off or approach when windshear is reported or forecast, especially near convective weather.</li>
  <li><strong>Recognise</strong> — predictive and reactive windshear warnings; unexplained speed changes of 15 kt or more; large vertical speed or pitch deviations.</li>
  <li><strong>Recover</strong> — apply the manufacturer's windshear escape manoeuvre: typically maximum (go-around) thrust, wings level, pitch towards the target or flight director guidance, <strong>no configuration change</strong> until clear, and respect the stall warning.</li>
</ul>

<h2>Wake turbulence</h2>
""" + wake() + """
<ul>
  <li>Wake vortices from a heavier aircraft can cause a roll rate greater than the following aircraft's roll authority.</li>
  <li>Respect wake separation; stay at or above the preceding aircraft's flight path; be most careful in calm wind conditions, where vortices persist.</li>
  <li>If you encounter a wake: release excessive back pressure, roll wings level with aileron, and <strong>do not use aggressive or alternating rudder</strong> (Lesson 8).</li>
</ul>

<h2>Thunderstorms</h2>
<p>Thunderstorms combine severe turbulence, windshear, hail, icing and lightning. Avoid them by a wide margin — company guidance typically recommends at least 20 NM laterally from severe cells — and never fly under the anvil or between closely spaced cells.</p>

<h2>Icing</h2>
<ul>
  <li>Airframe ice reduces the critical angle of attack, so the stall can occur before stall warning.</li>
  <li><strong>Supercooled large droplets</strong> and severe icing create ice behind protected areas, and can cause roll upsets. Leave the conditions immediately.</li>
  <li><strong>Tailplane icing</strong> can cause a nose-down pitch upset with flap extension.</li>
  <li><strong>Ice crystals</strong> at high altitude can block pitot probes and cause unreliable airspeed (Lesson 18).</li>
</ul>
<p class="muted">Icing is covered in detail in the Cold Weather Operations course.</p>
""",
takeaways=[
  "Avoid known threats: windshear, thunderstorms, mountain waves and wake turbulence.",
  "Windshear escape: maximum thrust, wings level, follow pitch guidance, no configuration change.",
  "Wake encounter: unload, roll wings level with aileron, no alternating rudder.",
  "Ice can cause a stall before the warning; ice crystals can cause unreliable airspeed.",
],
check=dict(
  q="During an approach you receive a reactive windshear warning. What is a typical element of the escape manoeuvre?",
  options=["Retract the flaps to reduce drag", "Apply maximum thrust and follow pitch guidance, without changing configuration", "Lower the nose to gain speed", "Extend the speedbrakes"],
  answer=1,
  explain="The windshear escape manoeuvre applies maximum thrust, keeps the wings level, follows the pitch target, and leaves the configuration unchanged until clear of the windshear.",
),
),

# ---------------------------------------------------------------- 13
dict(
title="Automation, Flight Control Laws and System Failures",
minutes=8,
objectives=[
  "Describe how automation can mask or create a developing upset.",
  "Explain the effects of autopilot disconnect, mode confusion and degraded flight control laws.",
  "Apply automation management principles to upset prevention.",
],
body="""
<h2>Advantages and limits of automation</h2>
<p>Automation flies precisely and reduces workload, which helps prevent many upsets. But it can also:</p>
<ul>
  <li><strong>mask</strong> a developing problem — the autopilot holds the aircraft against an asymmetry, ice accretion or mis-trim until it reaches its limit and disconnects, handing the pilot an aircraft that is already out of trim;</li>
  <li><strong>create</strong> an upset — an unexpected mode, a faulty sensor driving the autothrust or a flight control system, or a disconnect at a critical moment;</li>
  <li>reduce the pilot's awareness of the aircraft's energy state and the manual flying skill needed to recover.</li>
</ul>

<h2>Mode awareness</h2>
<ul>
  <li>The <strong>flight mode annunciator (FMA)</strong> shows what the automation is actually doing. Read it, announce changes, and cross-check.</li>
  <li>Watch for modes where the autothrust is <strong>not</strong> controlling speed — such as idle-thrust descent modes, "hold" modes, or after the autothrust has disconnected.</li>
  <li>If the automation does not do what you expect, <strong>reduce the level of automation</strong> or fly manually — do not spend time reprogramming at low altitude.</li>
</ul>

<h2>Autopilot disconnect</h2>
<p>An unexpected disconnect, with its aural warning, is a classic trigger for startle. Be ready for an out-of-trim condition. The pilot flying takes control smoothly, announces it, and stabilises the attitude and speed before doing anything else.</p>

<h2>Fly-by-wire control laws</h2>
<ul>
  <li>In <strong>normal law</strong>, envelope protections typically limit bank, pitch, load factor, angle of attack and overspeed.</li>
  <li>Failures — such as unreliable air data or certain system faults — can cause the system to revert to an <strong>alternate or direct law</strong>, in which some or all protections are lost. Handling may also change.</li>
  <li>In a degraded law, the aircraft <strong>can be stalled</strong>. Stall warning and recovery become the pilot's responsibility.</li>
</ul>

<h2>Other system-induced threats</h2>
<ul>
  <li>Engine failure or asymmetric thrust at low speed — yaw and roll that the autopilot may initially hide.</li>
  <li>Flight control malfunctions — jammed or runaway trim, spoiler or rudder problems. Know the memory items.</li>
  <li>Instrument failures — compare the attitude indicators with each other and with the standby instrument.</li>
</ul>
<div class="callout"><span class="label">Principle</span><p>Use the level of automation that best suits the situation — and always be able to fly the aircraft manually.</p></div>
""",
takeaways=[
  "Automation can mask a developing upset until it disconnects — expect an out-of-trim aircraft.",
  "Read and announce the FMA; reduce automation if it does not do what you expect.",
  "In degraded fly-by-wire laws, protections may be lost and the aircraft can stall.",
],
check=dict(
  q="The autopilot disconnects unexpectedly in cruise. What should the pilot flying do first?",
  options=["Re-engage the autopilot immediately", "Take control smoothly, announce it, and stabilise attitude and speed", "Check the circuit breakers", "Call the cabin crew"],
  answer=1,
  explain="Fly the aircraft first: take control, announce it, and stabilise the attitude and speed, expecting a possible out-of-trim condition.",
),
),

# ---------------------------------------------------------------- 14
dict(
title="Startle, Surprise and Spatial Disorientation",
minutes=9,
objectives=[
  "Distinguish startle from surprise and describe their effects on performance.",
  "Describe the main vestibular and visual illusions that lead to upsets.",
  "Apply strategies to manage startle and disorientation.",
],
body="""
<h2>Startle and surprise</h2>
<ul>
  <li><strong>Startle</strong> is an automatic physical reflex to a sudden, intense event — a loud warning, a bang, a violent jolt. It lasts seconds and can cause an involuntary movement on the controls.</li>
  <li><strong>Surprise</strong> is a mental reaction to something unexpected: the situation does not match what you thought was happening. It can last much longer.</li>
</ul>
<p>Together they can cause stress, tunnel vision, freezing, an inappropriate instinctive reaction (such as pulling back), or a delay in recognising what is happening. Investigators have found these effects in many LOC-I accidents.</p>

<h2>Managing startle and surprise</h2>
<ul>
  <li><strong>Expect the unexpected</strong> — brief threats, think through "what if", and practise unusual situations in the simulator.</li>
  <li><strong>Control the first reaction</strong> — keep inputs small, avoid sudden large movements, and breathe.</li>
  <li><strong>Re-establish the picture</strong> — look at the attitude indicator first, then speed, altitude and vertical speed. Say what you see.</li>
  <li><strong>Act on a plan</strong> — apply the trained recovery or procedure once the situation is recognised.</li>
</ul>

<h2>Spatial disorientation</h2>
<p>Without visual references, the body's balance organs are easily misled. The most dangerous illusions in transport flying are:</p>
""" + somatogravic() + """
<ul>
  <li><strong>Somatogravic illusion</strong> — acceleration feels like a nose-up pitch; deceleration feels like nose-down. Strongest during go-arounds and night take-offs over dark terrain or water.</li>
  <li><strong>Somatogyral illusions</strong> — "the leans": a slow roll is not felt, and correcting it feels like a bank the other way. In the <strong>graveyard spiral</strong>, a sustained, unfelt bank becomes a descending spiral, and pulling back only tightens it.</li>
  <li><strong>Visual illusions</strong> — a sloping cloud deck taken as the horizon; lights on the ground confused with stars; the "black hole" approach over dark terrain.</li>
</ul>
<div class="callout warn"><span class="label">Countermeasure</span><p>When sensations and instruments disagree, <strong>believe the instruments</strong>. Cross-check both attitude indicators and the standby instrument. The pilot monitoring calls out any deviation in pitch, bank or vertical speed.</p></div>
""",
takeaways=[
  "Startle is a reflex lasting seconds; surprise is a mental mismatch that can last longer.",
  "Manage startle: small inputs, breathe, attitude first, then act on a plan.",
  "Somatogravic illusion: acceleration feels like pitching up — dangerous in night go-arounds.",
  "When senses and instruments disagree, believe the instruments.",
],
check=dict(
  q="During a night go-around with high thrust, the pilot feels the aircraft is pitching up steeply. What is the likely cause?",
  options=["A pitot blockage", "The somatogravic illusion caused by acceleration", "Tailplane icing", "Wake turbulence"],
  answer=1,
  explain="Strong forward acceleration creates a false sensation of nose-up pitch. The natural reaction — pushing forward — can fly the aircraft into the ground.",
),
),

# ---------------------------------------------------------------- 15
dict(
title="CRM, Monitoring and Intervention",
minutes=8,
objectives=[
  "Describe the role of the pilot monitoring in upset prevention.",
  "Use standard callouts and intervention techniques.",
  "Apply clear transfer of control during an upset.",
],
body="""
<h2>The pilot monitoring is the first line of defence</h2>
<p>Many developing upsets are first visible to the pilot who is <strong>not</strong> flying. Effective monitoring means actively checking the flight path, the automation modes and the energy state — not just looking at the instruments.</p>
<ul>
  <li>Monitor during periods of low workload as carefully as during high workload. Developing upsets often start in cruise.</li>
  <li>Watch for trends: speed decaying, bank slowly increasing, pitch rising, vertical speed growing.</li>
  <li>Plan monitoring during high-workload phases, such as approach and go-around, so that someone is always watching the flight path.</li>
</ul>

<h2>Callouts</h2>
<p>Use the standard callouts of your Operations Manual. Typical examples:</p>
<div class="table-wrap"><table>
  <tr><th>Deviation</th><th>Typical callout</th></tr>
  <tr><td>Speed below target or trend towards the low-speed band</td><td>“Speed”</td></tr>
  <tr><td>Excessive bank</td><td>“Bank angle”</td></tr>
  <tr><td>Excessive pitch</td><td>“Pitch”</td></tr>
  <tr><td>Excessive descent rate</td><td>“Sink rate”</td></tr>
  <tr><td>Upset recognised</td><td>“Nose high” / “Nose low”, with the bank direction</td></tr>
</table></div>
<p>The pilot flying acknowledges and corrects. If there is no response, the pilot monitoring repeats the callout, then states the action needed — and is ready to take control.</p>

<h2>Intervention and transfer of control</h2>
<ul>
  <li>If the pilot flying does not respond to callouts, or is clearly incapacitated or disoriented, the pilot monitoring <strong>takes control</strong>: “I have control.”</li>
  <li>Transfer of control must be <strong>clear and acknowledged</strong> — “You have control.” Never let two pilots make inputs at the same time; on side-stick aircraft, dual inputs are summed.</li>
  <li>The company supports any crew member who intervenes in good faith to protect the flight.</li>
</ul>

<h2>Communication in a recovery</h2>
<ul>
  <li>The pilot flying announces the upset and the recovery: “Nose low, rolling left, recovering.”</li>
  <li>The pilot monitoring calls attitude, speed and altitude, watches for g limits and the stall warning, and reads relevant checklists only once the aircraft is stable.</li>
  <li>Inform ATC as soon as possible after control is regained.</li>
</ul>
""",
takeaways=[
  "The pilot monitoring is often first to see a developing upset — monitor actively, especially trends.",
  "Use standard callouts: speed, bank angle, pitch, sink rate, nose high / nose low.",
  "Transfer control clearly: “I have control” — “You have control.” No dual inputs.",
],
check=dict(
  q="The pilot flying does not respond to two “Bank angle” callouts as bank increases through 50°. What should the pilot monitoring do?",
  options=["Wait for the autopilot to correct", "Take control clearly with “I have control” and recover", "Make an input on the controls without saying anything", "Inform ATC first"],
  answer=1,
  explain="If callouts are not answered, the pilot monitoring takes control with a clear, acknowledged transfer, then recovers the aircraft.",
),
),

# ---------------------------------------------------------------- 16
dict(
title="Flight Path Management and Manual Handling",
minutes=8,
objectives=[
  "Describe flight path management as the core of upset prevention.",
  "Apply the pitch-and-power method to manual flying.",
  "Maintain manual handling skills and know when to use them.",
],
body="""
<h2>Flight path management</h2>
<p>Flight path management is the planning, execution and monitoring of the aircraft's trajectory and energy — whether flown manually or with automation. It is the most important upset prevention tool. It includes:</p>
<ul>
  <li><strong>planning</strong> — briefing the expected path, speeds, configuration changes and threats;</li>
  <li><strong>executing</strong> — choosing the right level of automation and flying accurately;</li>
  <li><strong>monitoring</strong> — checking that the aircraft is doing what was planned, and recognising deviations early.</li>
</ul>

<h2>Pitch and power</h2>
<p>Manual flying is built on <strong>known pitch attitudes and thrust settings</strong> for each phase of flight. If you know that a given pitch and thrust produce level flight at a given speed and configuration, you can fly the aircraft safely even with unreliable instruments — and you will recognise immediately when something is wrong.</p>
<ul>
  <li>Set the attitude first, then the thrust, then trim. Wait for the aircraft to settle before making further changes.</li>
  <li>Use small, smooth inputs. Make a correction, hold it, and observe the result.</li>
  <li>Learn the typical values for your type from the FCTM and the unreliable airspeed tables.</li>
</ul>

<h2>The instrument scan</h2>
<p>The attitude indicator is the centre of the scan. Move from attitude to speed, attitude to altitude, attitude to heading, and back. A good scan detects a developing upset within seconds.</p>

<h2>Keeping manual skills current</h2>
<ul>
  <li>Hand-fly when conditions, workload and company policy allow — for example a departure or an approach in good weather.</li>
  <li>Practise manual flying with the flight director off in the simulator.</li>
  <li>Use automation as a tool — not as a substitute for understanding where the aircraft is and where it is going.</li>
</ul>
<div class="callout"><span class="label">Golden rules</span><p><strong>Fly the aircraft</strong> first. Then navigate, then communicate. Whatever happens, someone must always be flying and monitoring the flight path.</p></div>
""",
takeaways=[
  "Flight path management — plan, execute, monitor — is the core of prevention.",
  "Pitch + power = performance: know the values for your type.",
  "Attitude indicator at the centre of the scan; small, smooth inputs.",
  "Keep manual skills current within company policy.",
],
check=dict(
  q="What is the basis of the pitch-and-power method?",
  options=["Following the flight director at all times", "Known pitch attitudes and thrust settings produce predictable performance", "Using full thrust whenever speed decays", "Flying by vertical speed only"],
  answer=1,
  explain="For a given configuration and weight, a known pitch attitude and thrust setting produce predictable speed and vertical speed.",
),
),
]
