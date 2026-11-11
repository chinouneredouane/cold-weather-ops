# Upset Prevention and Recovery — lessons 17–24
from .diagrams import attitudes, recovery_priority, adi, fig

LESSONS_C = [
# ---------------------------------------------------------------- 17
dict(
title="Recognising a Developing Upset",
minutes=8,
objectives=[
  "Identify the flight-deck cues of a developing upset.",
  "Read an attitude indicator quickly and correctly in an unusual attitude.",
  "Confirm the situation by cross-checking instruments.",
],
body="""
<h2>Cues of a developing upset</h2>
<ul>
  <li><strong>Speed:</strong> trend vector towards the low-speed band or the overspeed limit; speed not stabilising after a thrust change.</li>
  <li><strong>Attitude:</strong> pitch or bank increasing without an intended input; pitch limit indicator approaching the aircraft symbol.</li>
  <li><strong>Energy:</strong> thrust at idle when it should be climbing; pitch high and speed decaying.</li>
  <li><strong>Automation:</strong> unexpected mode changes, autopilot or autothrust disconnect, flight control law changes.</li>
  <li><strong>Physical:</strong> buffet, unusual noise, unexpected control forces, g changes.</li>
  <li><strong>Warnings:</strong> stall warning, overspeed, bank angle aural alert, windshear alert.</li>
</ul>

<h2>Reading the attitude indicator</h2>
""" + attitudes() + """
<ul>
  <li><strong>Look at the attitude indicator first.</strong> Determine pitch (sky or ground? which pitch line?) and bank (where is the sky pointer?).</li>
  <li>The <strong>sky pointer</strong> (or bank pointer) always points towards the sky. In a nose-low, high-bank upset, <strong>roll towards the sky pointer</strong> to bring the wings level.</li>
  <li>At extreme attitudes, the display may show mostly sky or mostly ground, and chevrons may point the way back to the horizon. Know your PFD.</li>
</ul>

<h2>Confirm before you act</h2>
<ul>
  <li>Cross-check both primary attitude indicators and the <strong>standby</strong> instrument. A single failed indicator can create a false upset.</li>
  <li>Confirm the trend with airspeed, altitude and vertical speed. A nose-high attitude with decaying speed and a climbing altimeter is very different from a nose-high attitude with a rapid descent (possible stall).</li>
  <li>Say what you see: “Nose high, wings level, speed decreasing.” This helps both pilots build the same picture.</li>
</ul>
<div class="callout"><span class="label">Act early</span><p>If you recognise a developing upset, correct it immediately with small, smooth inputs. A small correction now prevents a large recovery later.</p></div>
""",
takeaways=[
  "Developing upsets show up as speed, attitude, energy, automation, physical and warning cues.",
  "Read the attitude indicator first; the sky pointer always points to the sky.",
  "Confirm with the other attitude indicator, the standby instrument and the speed, altitude and vertical speed trends.",
],
check=dict(
  q="In a nose-low, high-bank upset, which way should you roll to bring the wings level?",
  options=["Away from the sky pointer", "Towards the sky pointer — the shortest direction to wings level", "Always to the left", "It does not matter"],
  answer=1,
  explain="The sky pointer points towards the sky. Rolling towards it brings the lift vector up and the wings level by the shortest way.",
),
),

# ---------------------------------------------------------------- 18
dict(
title="Unreliable Airspeed and Instrument Failures",
minutes=8,
objectives=[
  "Recognise the symptoms of unreliable airspeed.",
  "Apply the generic memory actions: pitch and thrust.",
  "Describe how to troubleshoot and stabilise after unreliable air data.",
],
body="""
<h2>Causes</h2>
<ul>
  <li>Pitot probes blocked by ice crystals, heavy rain, volcanic ash, insects or covers left in place.</li>
  <li>Static ports blocked — for example by tape or residue after maintenance or washing.</li>
  <li>Failed probe heaters, damaged probes, or faulty air data computers.</li>
</ul>

<h2>Symptoms</h2>
<ul>
  <li>Disagreement between the captain's, first officer's and standby airspeed or altitude.</li>
  <li>Speed that does not match the pitch and thrust (for example, speed rising in a climb at constant thrust).</li>
  <li>Simultaneous, contradictory warnings: overspeed and stall warning together, or "rudder ratio", "Mach trim" and altitude alerts.</li>
  <li>Autopilot and autothrust disconnect, flight control law degradation on fly-by-wire types.</li>
</ul>

<h2>Memory actions</h2>
<p>Most manufacturers' unreliable airspeed procedures begin with memory items along these lines:</p>
<ol class="steps">
  <li><strong>Autopilot and autothrust — disconnect</strong> (they may be using the faulty data).</li>
  <li><strong>Flight directors — off</strong> where the procedure requires it.</li>
  <li><strong>Pitch and thrust — set</strong> to the memory values for the flight phase (for example, a climb attitude and climb thrust after take-off; a level-flight attitude at cruise).</li>
</ol>
<p>Use the <strong>exact values and procedure</strong> from your QRH. Do not chase the airspeed indication.</p>

<h2>Stabilise, then troubleshoot</h2>
<ul>
  <li>When safe — above minimum safe altitude, wings level, stable pitch and thrust — use the QRH tables to set pitch and thrust for the phase of flight and weight.</li>
  <li>Use other information: GPS ground speed, angle of attack indication where fitted, the flight path vector, and ATC for ground speed and altitude (in an emergency).</li>
  <li>Identify a reliable source if possible. If none, continue with pitch and power tables.</li>
</ul>
<div class="callout warn"><span class="label">Key lesson</span><p>In several accidents, a short air data problem became a fatal stall because the crew reacted to the false indications with large, sustained pitch inputs. <strong>Pitch and power first</strong>, avoid large inputs, and respect the stall warning.</p></div>
""",
takeaways=[
  "Unreliable airspeed: disagreements, impossible combinations, contradictory warnings.",
  "Memory items: autopilot and autothrust off, flight directors off as required, set memory pitch and thrust.",
  "Stabilise first, then troubleshoot with QRH tables and other data.",
],
check=dict(
  q="Shortly after take-off, the airspeed indications disagree and both overspeed and stall warnings occur. What is the first action?",
  options=["Follow the flight director", "Apply the unreliable airspeed memory items: autopilot and autothrust off, set memory pitch and thrust", "Pull up to reduce the overspeed", "Reduce thrust to idle"],
  answer=1,
  explain="Contradictory warnings indicate unreliable air data. Disconnect the automation and fly the memory pitch and thrust.",
),
),

# ---------------------------------------------------------------- 19
dict(
title="Upset Recovery Principles",
minutes=8,
objectives=[
  "State the general principles of upset recovery.",
  "Explain why stall recovery takes priority.",
  "Describe the correct use of automation, thrust, rudder and g during recovery.",
],
body="""
<h2>The recovery sequence</h2>
""" + recovery_priority() + """
<ol class="steps">
  <li><strong>Recognise and confirm</strong> the situation — attitude first, cross-checked (Lesson 17).</li>
  <li><strong>Disconnect the autopilot and autothrust</strong> — they may be causing or worsening the upset, and their behaviour is unpredictable at extreme attitudes.</li>
  <li><strong>If stalled, recover from the stall first</strong> — reduce angle of attack (Lesson 20). Attitude cannot be recovered while the wing is stalled.</li>
  <li><strong>Recover the attitude</strong> using the nose-high or nose-low technique (Lessons 21 and 22).</li>
  <li><strong>Return to a safe flight path</strong> — level flight or a climb, appropriate speed, trimmed.</li>
</ol>

<h2>General principles</h2>
<ul>
  <li><strong>Use the manufacturer's procedures.</strong> The generic principles here explain <em>why</em>; the FCOM and QRH tell you <em>how</em> for your type.</li>
  <li><strong>Pitch is controlled with elevator and stabiliser trim.</strong> Use trim carefully to assist a large pitch input, not as the primary control.</li>
  <li><strong>Roll with aileron and spoiler.</strong> Full deflection may be needed. Rudder is normally not required and must never be used in rapid alternating inputs.</li>
  <li><strong>Thrust is used as required</strong> — remember pitch-power coupling: reducing thrust can help lower the nose, adding thrust helps a nose-low recovery only after the wings are level and the speed allows it.</li>
  <li><strong>Respect g limits.</strong> Unload in a nose-high recovery; avoid a rolling pull and excessive g in a nose-low recovery.</li>
  <li><strong>Do not change configuration</strong> (flaps, gear) unless the procedure requires it. Speedbrakes may be used in high-speed nose-low situations.</li>
  <li><strong>Communicate</strong> — announce the upset and the recovery; the pilot monitoring calls out attitude, speed and altitude.</li>
</ul>

<h2>Common errors</h2>
<ul>
  <li>Pulling back in a stall or a nose-low, high-bank attitude.</li>
  <li>Applying full thrust in a nose-high, low-speed upset on an aircraft with underwing engines.</li>
  <li>Over-controlling — large inputs in both directions, especially at high altitude.</li>
  <li>Using rudder to roll, or making alternating rudder inputs.</li>
  <li>Failing to disconnect the automation, or re-engaging it too early.</li>
</ul>
""",
takeaways=[
  "Recognise and confirm → automation off → stall recovery first → attitude recovery → safe flight path.",
  "Elevator and trim for pitch; aileron and spoiler for roll; rudder normally not needed.",
  "Use thrust as required, with pitch-power coupling in mind.",
  "Communicate throughout; follow the manufacturer's procedures.",
],
check=dict(
  q="An aircraft is nose-high, rolling, with the stall warning active. What is the priority?",
  options=["Roll the wings level first", "Recover from the stall — reduce the angle of attack", "Apply full thrust", "Extend the flaps"],
  answer=1,
  explain="Stall recovery always takes priority. Attitude cannot be recovered while the wing is stalled.",
),
),

# ---------------------------------------------------------------- 20
dict(
title="Stall Recovery",
minutes=8,
objectives=[
  "Apply the industry stall recovery template.",
  "Explain each step and the reasons behind it.",
  "Recognise the conditions that make stall recovery difficult.",
],
body="""
<h2>The stall recovery template</h2>
<p>Following accidents in which crews tried to "power out" of stalls while holding altitude, manufacturers and authorities adopted a common stall recovery template. A typical version is shown below. <strong>Use your manufacturer's procedure.</strong></p>
<div class="table-wrap"><table>
  <tr><th>Step</th><th>Action</th><th>Why</th></tr>
  <tr><td>1</td><td><strong>Autopilot and autothrust — disconnect</strong></td><td>The automation may be holding the nose up or reducing thrust; it will not recover a stall.</td></tr>
  <tr><td>2a</td><td><strong>Nose-down pitch control — apply until the stall warning stops</strong> and the aircraft is no longer stalled</td><td>Reducing the angle of attack is the only way to unstall the wing.</td></tr>
  <tr><td>2b</td><td><strong>Nose-down pitch trim — as needed</strong></td><td>If the aircraft was trimmed nose-up, the elevator alone may not be enough.</td></tr>
  <tr><td>3</td><td><strong>Bank — wings level</strong></td><td>Levelling the wings directs the lift vector upwards and reduces the load factor.</td></tr>
  <tr><td>4</td><td><strong>Thrust — as needed</strong></td><td>Add thrust once the angle of attack is reduced; be aware of the nose-up pitching moment of underwing engines. At low speed with high thrust, reducing thrust may be needed to lower the nose.</td></tr>
  <tr><td>5</td><td><strong>Speedbrakes / spoilers — retract</strong></td><td>They increase drag and the stall speed.</td></tr>
  <tr><td>6</td><td><strong>Return to the desired flight path</strong></td><td>Recover smoothly, avoiding a secondary stall warning or excessive g.</td></tr>
</table></div>

<h2>Important points</h2>
<ul>
  <li><strong>Reducing angle of attack comes before everything else — including altitude.</strong> Accept the altitude loss.</li>
  <li><strong>The stall warning is a stall.</strong> Treat any stall warning (except a confirmed false warning on take-off, if your procedure allows) as requiring the recovery template.</li>
  <li>A nose-down input may need to be <strong>large and sustained</strong>. A pitch attitude below the horizon may be required.</li>
  <li>Avoid a <strong>secondary stall</strong>: do not pull up too quickly after the warning stops.</li>
  <li>If the stick pusher activates, <strong>do not oppose it</strong>.</li>
  <li>Near the ground, the same template applies; only the urgency changes.</li>
</ul>

<h2>When stall recovery becomes difficult</h2>
<ul>
  <li>High altitude — little excess thrust, large altitude loss needed (Lesson 7).</li>
  <li>Nose-up trim — the stabiliser may need to be trimmed nose-down.</li>
  <li>High thrust with underwing engines — the nose-up moment opposes the recovery.</li>
  <li>Startle and unreliable instruments — the crew may not recognise that the aircraft is stalled.</li>
</ul>
""",
takeaways=[
  "Template: automation off → nose down (and trim) until unstalled → wings level → thrust as needed → speedbrakes retracted → return to flight path.",
  "Angle of attack first — altitude is secondary.",
  "Avoid a secondary stall; never oppose the stick pusher.",
],
check=dict(
  q="During stall recovery, the nose-down elevator input does not reduce the angle of attack enough. What else may be needed?",
  options=["Nose-up trim", "Nose-down pitch trim, and reducing thrust if high thrust is causing a nose-up moment", "Full rudder", "Extending the speedbrakes"],
  answer=1,
  explain="If the aircraft is trimmed nose-up or high underwing thrust is pitching it up, nose-down trim and a thrust reduction may be needed to reduce the angle of attack.",
),
),

# ---------------------------------------------------------------- 21
dict(
title="Nose-High Upset Recovery",
minutes=8,
objectives=[
  "Apply the generic nose-high recovery technique.",
  "Explain the use of bank and thrust to lower the nose.",
  "Complete the recovery without over-correcting into a nose-low upset.",
],
body="""
<h2>The situation</h2>
<p>The pitch attitude is unintentionally high — for example more than 25° nose-up — and the airspeed is decreasing, or is already low. The aircraft is heading towards a stall. The goal is to <strong>lower the nose</strong> and regain speed before the angle of attack reaches the critical value.</p>
""" + fig(adi(35, 0, cx=150, cy=140, r=105, uid="nh2", label="Nose-high: about 35° up, wings level"),
          "Nose-high upset. The speed is decaying; recognise it early.", "Attitude indicator showing nose-high", "35 degrees nose-up, wings level.", "0 0 300 290", maxw=340) + """
<h2>Generic technique (based on industry guidance)</h2>
<ol class="steps">
  <li><strong>Recognise and confirm</strong> the situation. Announce “Nose high”.</li>
  <li><strong>Autopilot and autothrust — disconnect.</strong></li>
  <li><strong>Apply as much as full nose-down elevator.</strong> Accept reduced g — the feeling of being light in your seat. Use nose-down stabiliser trim if needed.</li>
  <li><strong>If more is needed to lower the nose:</strong>
    <ul>
      <li><strong>Reduce thrust</strong> (aircraft with underwing engines) to reduce the nose-up moment;</li>
      <li><strong>Roll</strong> to a bank angle that helps the nose drop — the lift vector moves away from the vertical, and the nose falls towards the horizon. Do not normally exceed about 60° of bank.</li>
    </ul>
  </li>
  <li><strong>Complete the recovery:</strong> as the nose approaches the horizon, roll wings level, check the airspeed, adjust thrust and establish the required pitch attitude.</li>
</ol>
<p class="muted">Always follow the manufacturer's procedure for your type.</p>

<h2>Points to remember</h2>
<ul>
  <li>If the aircraft is <strong>stalled</strong>, apply the stall recovery first (Lesson 20).</li>
  <li>Unloading reduces the angle of attack and the stall speed. A low-g sensation is expected and acceptable.</li>
  <li>Do not over-correct. A nose-high upset recovered too aggressively can become a nose-low, high-speed upset.</li>
  <li>Unsecured objects and passengers or crew without seat belts may be thrown upwards during unloading.</li>
</ul>
""",
takeaways=[
  "Nose-high: automation off, nose-down elevator (as much as full), trim as needed.",
  "If needed: reduce thrust (underwing engines) and/or roll to bank to help the nose drop — normally not more than about 60°.",
  "Approaching the horizon: wings level, check speed, set thrust and pitch.",
],
check=dict(
  q="In a nose-high upset, full nose-down elevator is not lowering the nose quickly enough. Which additional techniques can help?",
  options=["Add thrust and pull up", "Reduce thrust and/or roll to a moderate bank angle", "Extend the flaps", "Apply alternating rudder"],
  answer=1,
  explain="Reducing thrust removes the nose-up moment of underwing engines, and banking lets the nose fall towards the horizon.",
),
),

# ---------------------------------------------------------------- 22
dict(
title="Nose-Low and High-Bank Upset Recovery",
minutes=8,
objectives=[
  "Apply the generic nose-low recovery technique.",
  "Explain why the wings must be levelled before pulling.",
  "Manage speed and g in a high-speed, nose-low recovery.",
],
body="""
<h2>The situation</h2>
<p>The pitch is unintentionally low — for example more than 10° nose-down — often combined with a high bank angle. The speed is usually increasing. The danger is <strong>overspeed</strong>, <strong>structural overload</strong> and ground contact — and, if the aircraft is stalled, a continued uncontrolled descent.</p>
""" + fig(adi(-20, 75, cx=150, cy=140, r=105, uid="nl2", label="Nose-low: 20° down, 75° right bank"),
          "Nose-low, high-bank upset: roll towards the sky pointer before pulling.", "Attitude indicator showing nose-low, high bank", "20 degrees nose-down with 75 degrees of right bank.", "0 0 300 290", maxw=340) + """
<h2>Generic technique (based on industry guidance)</h2>
<ol class="steps">
  <li><strong>Recognise and confirm</strong> the situation. Announce “Nose low”, with the direction of bank.</li>
  <li><strong>Autopilot and autothrust — disconnect.</strong></li>
  <li><strong>Recover from the stall, if stalled</strong> — even with the nose low, the wing may be stalled (high descent rate, stall warning, buffet). Reduce the angle of attack first.</li>
  <li><strong>Roll in the shortest direction to wings level.</strong> Full aileron and spoiler may be needed. It may be necessary to <strong>unload</strong> (reduce back pressure) to improve roll response.</li>
  <li><strong>Recover to level flight:</strong> apply nose-up elevator smoothly, use stabiliser trim if necessary, and adjust thrust and drag as required — reduce thrust and extend the speedbrakes if the speed is high.</li>
</ol>
<p class="muted">Always follow the manufacturer's procedure for your type.</p>

<h2>Why roll before pull</h2>
<ul>
  <li>With high bank, pulling back mainly <strong>tightens the turn</strong> and increases the descent — it does not raise the nose. This is how a graveyard spiral develops.</li>
  <li>A <strong>rolling pull</strong> — rolling and pulling at the same time — produces asymmetric structural loads with lower limits.</li>
  <li>Once the wings are near level, the lift vector points up, and the pull raises the nose efficiently.</li>
</ul>

<h2>Bank beyond 90°</h2>
<p>If the aircraft is beyond 90° of bank, the shortest way to wings level may require continuing the roll through the inverted position — follow the sky pointer. Unload while rolling. Pulling while inverted only steepens the dive.</p>

<h2>Managing speed and g</h2>
<ul>
  <li>Reduce thrust and use speedbrakes as needed to control the speed.</li>
  <li>Pull smoothly to recover — firmly enough to stop the descent, but without exceeding the g limit or triggering the stall warning. Your FCTM gives type-specific guidance.</li>
  <li>Avoid a secondary nose-high upset: as the nose passes the horizon, establish level flight and a suitable speed.</li>
</ul>
""",
takeaways=[
  "Nose-low: automation off → stall recovery if stalled → roll wings level (shortest direction) → then pull.",
  "Never pull with high bank — it tightens the spiral and risks a rolling pull.",
  "Control speed with thrust and speedbrakes; pull smoothly within g limits.",
],
check=dict(
  q="In a nose-low upset with 80° of bank and increasing speed, what should you do before pulling back?",
  options=["Add thrust", "Roll wings level in the shortest direction (unloading if needed)", "Extend the flaps", "Apply full rudder"],
  answer=1,
  explain="With high bank, pulling only tightens the turn. Roll wings level first, then pull smoothly to recover.",
),
),

# ---------------------------------------------------------------- 23
dict(
title="Lessons from Accidents",
minutes=10,
objectives=[
  "Describe key loss of control accidents and their causal factors.",
  "Link each accident to the prevention and recovery principles of this course.",
  "Recognise the common threads in LOC-I accidents.",
],
body="""
<h2>Case studies</h2>
<div class="table-wrap"><table>
  <tr><th>Accident</th><th>What happened</th><th>Lesson for us</th></tr>
  <tr><td><strong>American Airlines 587</strong><br>Airbus A300-600, New York, November 2001</td><td>After encountering wake turbulence on climb-out, the first officer made repeated full rudder inputs in alternating directions. The loads exceeded the vertical stabiliser's design limits and it separated. 265 people died.</td><td>Never use alternating rudder inputs. Respect wake separation. V<sub>A</sub> does not protect against cyclic inputs.</td></tr>
  <tr><td><strong>Colgan Air 3407</strong><br>Bombardier Q400, Buffalo, February 2009</td><td>During the approach the speed decayed until the stick shaker activated. The captain responded with nose-up inputs; the stick pusher activated and was overridden. The aircraft stalled and crashed into a house. 50 people died.</td><td>Monitor speed. Respond to the stall warning by reducing angle of attack. Never fight the stick pusher.</td></tr>
  <tr><td><strong>Turkish Airlines 1951</strong><br>Boeing 737-800, Amsterdam, February 2009</td><td>A faulty radio altimeter caused the autothrottle to reduce thrust to idle during the approach. The crew did not notice the speed decay in time. The aircraft stalled at low altitude and crashed short of the runway. 9 people died.</td><td>Monitor the automation and the FMA. Watch the speed. Apply the stall recovery promptly.</td></tr>
  <tr><td><strong>Air France 447</strong><br>Airbus A330-200, South Atlantic, June 2009</td><td>In cruise, ice crystals blocked the pitot probes; airspeed became unreliable, the autopilot disconnected and the flight control law degraded. The pilot flying made sustained nose-up inputs; the aircraft climbed, stalled, and descended in a stall until it hit the ocean. 228 people died.</td><td>Unreliable airspeed: pitch and power, small inputs. At high altitude, recover by reducing angle of attack. Recognise a stall even in degraded modes.</td></tr>
  <tr><td><strong>Gulf Air 072</strong><br>Airbus A320, Bahrain, August 2000</td><td>During a go-around at night over the sea, the aircraft was pitched nose-down and descended into the water. Spatial disorientation (somatogravic illusion) was found to be a likely factor. 143 people died.</td><td>Go-arounds at night: follow the attitude indicator. Use standard callouts and intervene.</td></tr>
  <tr><td><strong>Indonesia AirAsia 8501</strong><br>Airbus A320, Java Sea, December 2014</td><td>Repeated faults in the rudder travel limiter led the crew to reset a flight control computer in flight. The autopilot disengaged, the control law degraded, and the aircraft rolled. The subsequent inputs led to a stall that was not recovered. 162 people died.</td><td>Do not perform non-procedural resets. Fly the aircraft first after an autopilot disconnect. Recognise and recover from the stall.</td></tr>
</table></div>

<h2>The common threads</h2>
<ol class="steps">
  <li><strong>A trigger</strong> — weather, a technical fault, or a distraction.</li>
  <li><strong>Monitoring failures</strong> — speed, automation modes or attitude were not watched closely enough.</li>
  <li><strong>Startle and surprise</strong> — the situation did not match the crew's expectations.</li>
  <li><strong>Inappropriate reaction</strong> — pulling back, chasing false indications, or using the wrong control.</li>
  <li><strong>No recovery</strong> — the stall was not recognised, or the recovery was incomplete.</li>
</ol>
<p>Each of these steps could have been interrupted by the principles in this course: monitoring, callouts, pitch and power, angle of attack awareness and the recovery templates.</p>
""",
takeaways=[
  "LOC-I accidents follow a pattern: trigger → monitoring failure → startle → wrong reaction → no recovery.",
  "Every link can be broken by monitoring, callouts, pitch and power, and correct recovery technique.",
  "Reduce angle of attack in any stall — at any altitude, with any automation state.",
],
check=dict(
  q="Which accident showed that rapid, alternating rudder inputs can cause structural failure?",
  options=["Air France 447", "American Airlines 587", "Colgan Air 3407", "Turkish Airlines 1951"],
  answer=1,
  explain="American Airlines 587: alternating full rudder inputs after a wake encounter overloaded the vertical stabiliser.",
),
),

# ---------------------------------------------------------------- 24
dict(
title="Course Review and Simulator Training",
minutes=8,
objectives=[
  "Review the essential principles of upset prevention and recovery.",
  "Explain the limitations of flight simulators in UPRT.",
  "Prepare for the practical (FSTD) component of UPRT.",
],
body="""
<h2>The essential principles</h2>
<ol class="steps">
  <li><strong>Prevention first.</strong> Flight path management, monitoring and energy awareness stop most upsets before they start.</li>
  <li><strong>Know the aerodynamics.</strong> The wing stalls at its critical angle of attack — at any speed, attitude or power.</li>
  <li><strong>Respect the margins</strong> — speed, buffet and g. Most upsets begin with an eroded margin.</li>
  <li><strong>Understand the automation</strong> — and expect it to hand you a problem when it disconnects.</li>
  <li><strong>Manage startle</strong> — small inputs, attitude first, then act on a plan.</li>
  <li><strong>Communicate</strong> — callouts, clear transfer of control, no dual inputs.</li>
  <li><strong>Stall recovery first</strong> — reduce the angle of attack, accept the altitude loss.</li>
  <li><strong>Recover with the right technique</strong> — nose-high: unload, reduce thrust, bank if needed; nose-low: roll wings level, then pull.</li>
</ol>

<h2>Simulator (FSTD) training</h2>
<p>The FSTD component of UPRT lets you practise recognition and recovery in your aircraft type. Doc 10011 emphasises that simulator training must stay within the <strong>validated training envelope</strong> of the device:</p>
<ul>
  <li>Simulators are based on flight test data. Beyond the stall, at extreme attitudes or sideslip, the data may be extrapolated — the simulator may not behave like the real aircraft.</li>
  <li>A simulator cannot reproduce sustained g forces or the full physiological effects of an upset — this is why on-aeroplane training exists in licence training.</li>
  <li>Training outside the valid envelope risks <strong>negative training</strong>: learning a technique that would not work, or would be dangerous, in the real aircraft.</li>
  <li>Instructors must be trained to use the FSTD correctly, to recognise when it is outside its valid envelope, and to debrief using the instructor station tools.</li>
</ul>

<h2>Your next steps</h2>
<ul>
  <li>Complete the final quiz (20 questions, pass mark 80 %).</li>
  <li>Review your type's FCOM and QRH procedures for stall recovery, unreliable airspeed, windshear and upset recovery.</li>
  <li>Bring your questions to the next simulator session and practise prevention as well as recovery.</li>
</ul>
""",
takeaways=[
  "Prevention first; stall recovery first; the right technique for nose-high and nose-low.",
  "FSTD training must stay within the simulator's validated envelope to avoid negative training.",
  "Simulators cannot reproduce sustained g; on-aeroplane training fills that gap in licence training.",
],
check=dict(
  q="Why must UPRT in a simulator stay within its validated training envelope?",
  options=["To save simulator time", "Outside it, the simulator may not represent the aircraft accurately, which risks negative training", "Because the instructor station does not work outside it", "Because regulations forbid stall training"],
  answer=1,
  explain="Beyond the validated envelope, simulator behaviour may be extrapolated and inaccurate, so pilots could learn techniques that would not work in the real aircraft.",
),
),
]
