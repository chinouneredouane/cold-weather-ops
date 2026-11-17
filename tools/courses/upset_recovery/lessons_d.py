# Upset Prevention and Recovery — lessons 24–27: elements of the Domestic Airlines OM D 2.6.76 UPRT programme
# not covered in depth by lessons 1–23 (A10 propeller effects, E1/E3 engine effects, I system malfunctions,
# J specialised elements, K3 TEM / fatigue / workload). Fleet-specific values come from FCOM / AOM / QRH.

LESSONS_D = [
# ---------------------------------------------------------------- 24
dict(
title="Engine and Propeller Effects: Jet and Turboprop",
minutes=9,
objectives=[
  "Explain total energy as kinetic, potential and chemical (thrust) energy.",
  "Describe how thrust changes affect pitch on underwing-engine jets (B737-800).",
  "Describe propeller slipstream, torque and asymmetric effects on turboprops (Q400, Q200) and their role in upsets and recovery.",
],
body="""
<h2>Three forms of energy</h2>
<p>Lesson 10 described the exchange between <strong>kinetic energy</strong> (speed) and <strong>potential energy</strong> (altitude). The third form is <strong>chemical energy</strong>: the fuel, turned into thrust by the engines. Only thrust minus drag can <strong>add</strong> energy to the aircraft. How quickly and how much depends on the engine type, the altitude and the speed.</p>
<div class="table-wrap"><table>
  <tr><th></th><th>Turbofan (B737-800)</th><th>Turboprop (Q400, Q200)</th></tr>
  <tr><td>Response from low power</td><td>Slow: several seconds to spool up from idle</td><td>Fast: power and propeller respond quickly</td></tr>
  <tr><td>Effect on pitch</td><td>Underwing engines: thrust increase = <strong>nose-up</strong> moment; reduction = nose-down</td><td>Slipstream over wing and tail changes lift and pitch with power</td></tr>
  <tr><td>Effect on yaw and roll</td><td>Small with both engines; large asymmetry after engine failure</td><td>Torque, slipstream and asymmetric blade effect: yaw and roll with large power changes at low speed</td></tr>
  <tr><td>Thrust at high altitude</td><td>Much reduced — little excess thrust</td><td>Reduced; lower operating altitudes</td></tr>
</table></div>

<h2>Jets: the pitch-thrust couple</h2>
<ul>
  <li>The B737-800 engines are <strong>below the centre of gravity</strong>. Adding thrust pitches the nose up; reducing it pitches the nose down.</li>
  <li>At low speed with high thrust, the elevator may not be able to stop the nose-up moment. This is why, in a <strong>nose-high, low-speed upset</strong> or a stall, a <strong>thrust reduction</strong> may be needed to get the nose down (Lessons 20 and 21).</li>
  <li>From idle, the spool-up time means that thrust arrives late. Anticipate: energy that is not there cannot be created instantly.</li>
</ul>

<h2>Turboprops: propeller effects</h2>
<ul>
  <li><strong>Slipstream</strong> — the propellers blow air over the parts of the wing behind them and over the tail. With high power, that part of the wing produces more lift, so the <strong>power-on stall speed is lower</strong> than the power-off one. A sudden power reduction removes that extra lift.</li>
  <li><strong>Torque and asymmetric blade effect</strong> — large power changes at <strong>low speed and high angle of attack</strong> create yaw and roll tendencies that the pilot must correct with rudder and aileron.</li>
  <li><strong>Tail effects</strong> — on T-tail aircraft such as the Dash 8 family, slipstream and wing wake over the tail change with power and angle of attack. Stall characteristics are why some types are fitted with a <strong>stick pusher</strong> (check your AOM).</li>
  <li><strong>Engine failure</strong> — a windmilling, unfeathered propeller creates large drag and yaw. The autofeather and the engine failure procedure exist to remove it quickly.</li>
</ul>
<div class="callout warn"><span class="label">In a recovery</span><p>On a turboprop at low speed, apply power <strong>smoothly</strong> and be ready with rudder to keep the aircraft coordinated. An abrupt full-power application near the stall can produce a yaw and roll that turns a recoverable situation into an upset.</p></div>

<h2>Icing and contamination</h2>
<p>Ice on the wing or tail raises the stall speed and can cause a stall <strong>before</strong> the normal stall warning, with roll-off or pitch-down. Turboprops spend more time at the altitudes where icing is common. Respect the ice protection procedures and the icing speed and stall-warning settings of your AOM (see the Cold Weather Operations course).</p>
""",
takeaways=[
  "Energy: kinetic, potential and chemical — only thrust minus drag adds energy.",
  "B737-800: thrust up = nose up; in a nose-high low-speed upset, reducing thrust may be needed.",
  "Turboprops: slipstream lowers the power-on stall speed; large power changes at low speed cause yaw and roll.",
  "Ice can cause a stall before the normal warning.",
],
check=dict(
  q="On a turboprop at low speed, why should power be applied smoothly during a stall recovery?",
  options=["To save fuel", "Abrupt power at low speed and high angle of attack can cause a strong yaw and roll", "Turboprops respond slowly", "To avoid exceeding VMO"],
  answer=1,
  explain="Torque, slipstream and asymmetric blade effects at low speed can produce yaw and roll; apply power smoothly and coordinate with rudder.",
),
),

# ---------------------------------------------------------------- 25
dict(
title="System Malfunctions: Flight Controls, Power Loss and Stall Protection",
minutes=9,
objectives=[
  "Recognise flight control malfunctions that can lead to an upset.",
  "Manage a partial or total loss of power without losing control.",
  "Recognise failures of the stall-protection and ice-warning systems.",
],
body="""
<h2>Flight control malfunctions</h2>
<ul>
  <li><strong>Runaway trim</strong> — an uncommanded, continuous trim movement. On the B737-800 the stabiliser trim can overpower the elevator if not stopped: apply the <strong>QRH Runaway Stabilizer</strong> procedure (memory items) without delay.</li>
  <li><strong>Jammed or restricted controls</strong> — use the other controls (trim, the other pilot's control column where the type allows), reduce speed changes and follow the QRH.</li>
  <li><strong>Asymmetric flaps or spoilers</strong> — an unexpected roll during configuration change: stop the selection, control the roll, apply the QRH.</li>
  <li><strong>Autopilot or yaw damper malfunction</strong> — disconnect, fly manually, and check the FMA (Lesson 13).</li>
</ul>
<p>The common rule: <strong>fly the aircraft first</strong> — keep attitude and energy under control — then identify the failure and apply the checklist.</p>

<h2>Partial or total loss of power</h2>
<ul>
  <li><strong>Engine failure</strong> — yaw and roll towards the failed engine. Below V<sub>MCA</sub> directional control can be lost: keep the speed above it and use rudder to keep the aircraft straight.</li>
  <li>On turboprops, an <strong>unfeathered propeller</strong> adds large drag and yaw — check autofeather or feather manually per the AOM.</li>
  <li><strong>Partial power loss</strong> or an engine that does not respond can be harder to recognise than a clean failure. Cross-check engine parameters with the aircraft's response.</li>
  <li><strong>High-altitude engine events</strong> (Training Aid, Appendix 3-E): a <strong>multi-engine flameout</strong> needs prompt recognition and the recall items — establish the airspeed for a windmill restart and expect a large altitude loss. After a flameout, a <strong>core lock</strong> can stop the engine core from turning: follow the QRH speed and altitude guidance to restore rotation. A <strong>rollback</strong> is an uncommanded loss of thrust (moisture, icing, fuel control problems): check the thrust actually produced against the thrust selected.</li>
  <li><strong>Total loss of power</strong> — the aircraft becomes a glider: pitch for the best glide speed, keep energy, and do not let the speed decay while handling the restart.</li>
</ul>

<h2>Instrument and automation failures</h2>
<p>Unreliable airspeed and instrument failures are covered in Lesson 18; automation failures in Lesson 13. They are among the most common triggers of upsets because the crew loses the information it needs to control the aircraft.</p>

<h2>Stall-protection and ice-warning failures</h2>
<ul>
  <li>A <strong>false stall warning</strong> (for example from a damaged angle-of-attack vane) can lead the crew to the wrong action, or to ignore a later real warning. Cross-check attitude, speed and the other side before deciding — but never ignore a stick shaker without positive evidence that it is false.</li>
  <li>A <strong>failed stall warning</strong> removes a defence: monitor speed and angle of attack margins closely.</li>
  <li>In <strong>icing</strong> the stall can occur at a lower angle of attack. Some turboprops use an icing setting that advances the stall warning and increases the reference speeds — use it exactly as the AOM requires. An ice detection failure means the crew must judge icing visually and apply the procedures.</li>
  <li><strong>Fly-by-wire protections</strong> (not fitted to our fleets) can degrade after failures, removing the envelope protection pilots may rely on. Pilots moving to such types must learn their degraded laws.</li>
</ul>

<h2>Case studies</h2>
<div class="table-wrap"><table>
  <tr><th>Accident</th><th>What happened</th><th>Lesson</th></tr>
  <tr><td><strong>Colgan Air 3407</strong><br>Dash 8-Q400, Buffalo, USA, February 2009</td><td>During the approach the speed decayed; the stick shaker activated and the captain pulled back. The aircraft stalled and the stick pusher activated; the crew did not recover. 50 people died.</td><td>Monitor speed; respond to the stick shaker by <strong>reducing angle of attack</strong>, never by pulling.</td></tr>
  <tr><td><strong>American Eagle 4184</strong><br>ATR 72, Roselawn, USA, October 1994</td><td>Holding in freezing drizzle, ice formed behind the protected areas. When the flaps were retracted the aircraft rolled uncontrollably. 68 people died.</td><td>Severe icing can cause roll upsets without warning: leave the icing conditions.</td></tr>
</table></div>
""",
takeaways=[
  "Fly the aircraft first, then the checklist.",
  "B737-800 runaway stabilizer: QRH memory items without delay.",
  "Engine failure: keep above VMCA, rudder to keep straight; turboprops — feather the propeller.",
  "Stick shaker: reduce angle of attack — never pull (Colgan 3407).",
],
check=dict(
  q="What is the correct first response to a stick shaker on approach?",
  options=["Pull up to stop the descent", "Reduce the angle of attack (push / unload), then manage thrust and configuration", "Increase flap", "Engage the autopilot"],
  answer=1,
  explain="A stick shaker means a high angle of attack. The response is to reduce it — Colgan 3407 shows the danger of pulling.",
),
),

# ---------------------------------------------------------------- 26
dict(
title="Specialised Manoeuvres: Slow Flight, Steep Turns, Spiral Dive and Uncoordinated Stalls",
minutes=9,
objectives=[
  "Describe aircraft behaviour in slow flight and steep turns.",
  "Recognise a spiral dive and recover in the right order.",
  "Explain uncoordinated (yaw-aggravated) stalls, stick pusher activation, and how recovery changes with speed.",
],
body="""
<h2>Why these manoeuvres</h2>
<p>The OM D UPRT programme (element J) includes specialised manoeuvres trained in the simulator. This lesson gives the theory behind them, so that the simulator session builds on understanding.</p>

<h2>Slow flight</h2>
<ul>
  <li>At low speed the controls are <strong>less effective</strong> and need larger inputs; the aircraft is close to the critical angle of attack.</li>
  <li>Below the minimum drag speed the aircraft is on the <strong>back side of the power curve</strong>: a lower speed needs <strong>more</strong> thrust. Pitching up without power makes the speed decay further.</li>
</ul>

<h2>Steep turns</h2>
<ul>
  <li>In a level turn the load factor rises with bank: about 1.4 g at 45° and 2 g at 60°. The stall speed rises with the square root of the load factor (Lesson 6).</li>
  <li>Back pressure and thrust must increase to hold altitude. At high bank the aircraft tends to <strong>overbank</strong>; hold the bank with opposite aileron.</li>
</ul>

<h2>Spiral dive</h2>
<ul>
  <li>A nose-low, high-bank descent with <strong>increasing speed</strong> and load factor — often entered without the crew noticing (spatial disorientation, Lesson 14).</li>
  <li><strong>Pulling first</strong> only tightens the spiral and increases g. Recovery: reduce thrust, <strong>roll wings level first</strong>, then recover pitch smoothly within g limits; use speedbrakes if the speed is high.</li>
</ul>

<h2>Approach to stall and full stall</h2>
<ul>
  <li><strong>Approach to stall</strong> — first indication (stick shaker, buffet): reduce angle of attack immediately and recover the speed.</li>
  <li><strong>Full stall</strong> — buffet, nose drop, roll-off or loss of pitch authority: reduce angle of attack until the stall indications stop, then recover (Lesson 20).</li>
  <li><strong>Uncoordinated stall</strong> — with yaw (sideslip) at the stall, one wing stalls first and the aircraft rolls and yaws towards it (wing drop). Large aileron inputs can deepen the stall on the low wing. <strong>Reduce angle of attack first</strong>, keep the rudder neutral or use it only to stop further yaw, then roll wings level once unstalled.</li>
  <li><strong>Stick pusher</strong> (where fitted, for example on the Q400 — check your AOM): it pushes the nose down to reduce angle of attack. <strong>Do not fight it.</strong> Let it work, then complete the stall recovery.</li>
</ul>

<h2>Recovery depends on speed</h2>
<div class="table-wrap"><table>
  <tr><th>Upset</th><th>High speed</th><th>Low speed</th></tr>
  <tr><td><strong>Nose-high</strong></td><td>Plenty of energy: unload towards 1 g, let the nose come down, avoid excessive g; reduce thrust if the speed increases quickly.</td><td>Little energy, stall risk: unload (towards 0.5 g), reduce thrust if the nose will not come down (underwing engines), bank to help the nose drop (Lesson 21).</td></tr>
  <tr><td><strong>Nose-low</strong></td><td>Speed rising fast: reduce thrust, <strong>roll wings level first</strong>, speedbrakes as needed, then recover pitch within g limits (Lesson 22).</td><td>The aircraft may be stalled: <strong>stall recovery first</strong>, then roll wings level and recover with thrust.</td></tr>
</table></div>
<div class="callout"><span class="label">LOFT / LOS</span><p>The programme ends with line-oriented scenarios (LOFT / LOS), where upsets develop from realistic threats such as weather, automation or system failures — training recognition and crew coordination, not only the manoeuvre.</p></div>
""",
takeaways=[
  "Slow flight: weak controls, back side of the power curve.",
  "Spiral dive: thrust reduce, roll wings level first, then pull.",
  "Uncoordinated stall: reduce angle of attack first; avoid large aileron inputs while stalled.",
  "Stick pusher: never fight it. Recovery technique depends on speed as well as attitude.",
],
check=dict(
  q="In a spiral dive with increasing speed, what is the correct order?",
  options=["Pull hard, then roll level", "Reduce thrust and roll wings level first, then recover pitch smoothly", "Add thrust and pull", "Extend the flaps"],
  answer=1,
  explain="Pulling in a high bank tightens the spiral. Reduce thrust, roll wings level, then recover pitch within g limits.",
),
),

# ---------------------------------------------------------------- 27
dict(
title="Threat and Error Management, Workload and Fatigue",
minutes=8,
objectives=[
  "Apply the threat and error management (TEM) framework to upset prevention.",
  "Explain how human information processing, fixation and distraction lead to upsets.",
  "Manage workload and fatigue to keep monitoring effective.",
],
body="""
<h2>Human information processing</h2>
<ul>
  <li>Pilots perceive, interpret, decide and act with a <strong>limited attention</strong>. Under high workload or stress, attention narrows.</li>
  <li><strong>Expectation</strong> shapes perception: we tend to see what we expect, and to reject information that does not fit our mental model.</li>
  <li><strong>Fixation</strong> on one problem, <strong>distraction</strong> by another task, or simple <strong>inattention</strong> let a deviation grow unnoticed — the start of most upsets.</li>
  <li><strong>Instrument interpretation</strong> — read the attitude first: the horizon line and the bank pointer ("sky pointer") show which way is up. Confirm with the other instruments.</li>
</ul>

<h2>Threat and error management (TEM)</h2>
<div class="table-wrap"><table>
  <tr><th>Element</th><th>Definition</th><th>Upset examples</th></tr>
  <tr><td><strong>Threats</strong></td><td>Events outside the crew's control that increase complexity</td><td>Turbulence, icing, convective weather, system failures, late ATC changes</td></tr>
  <tr><td><strong>Errors</strong></td><td>Crew actions or inactions that deviate from intentions or expectations</td><td>Wrong mode selected, speed not monitored, wrong trim, missed callout</td></tr>
  <tr><td><strong>Undesired aircraft states</strong></td><td>Deviations of position, speed, attitude or configuration caused by threats or errors</td><td>Low speed, excessive bank, unstable approach — the step just before an upset</td></tr>
</table></div>
<p>Countermeasures: <strong>anticipate</strong> threats in the briefing, <strong>detect</strong> errors with active monitoring and cross-checks, and <strong>recover</strong> from an undesired state before it becomes an upset.</p>

<h2>Active monitoring and verification</h2>
<ul>
  <li>Monitoring is an active task: the PM checks the flight path and FMA, compares with expectations and <strong>speaks up</strong> (Lesson 15).</li>
  <li>Verify every change: mode, target, configuration. "What is it doing now? What will it do next?"</li>
</ul>

<h2>Workload management</h2>
<ul>
  <li>Plan high-workload phases in advance; brief the threats.</li>
  <li>Prioritise: <strong>aviate, navigate, communicate</strong>. Delegate tasks clearly between PF and PM.</li>
  <li>Choose the level of automation that reduces workload — and revert to manual flight when the automation does not do what is needed.</li>
</ul>

<h2>Fatigue</h2>
<ul>
  <li>Fatigue slows reactions, narrows attention and increases errors — including missed monitoring.</li>
  <li>Use the company fatigue management and reporting procedures (OM A FTL chapter). Tell the other pilot when you are tired, and use controlled rest only as the OM allows.</li>
</ul>

<h2>Crew resource management</h2>
<p>All these skills come together in CRM: a shared mental model, clear communication, assertiveness and leadership. Most upset accidents show a breakdown of at least one of them.</p>
""",
takeaways=[
  "Limited attention, expectation, fixation and distraction let deviations grow.",
  "TEM: threats → errors → undesired aircraft states → upset; anticipate, detect, recover.",
  "Active monitoring and verification of every mode and target change.",
  "Manage workload (aviate, navigate, communicate) and report fatigue.",
],
check=dict(
  q="In the TEM framework, what is a low speed caused by a missed thrust setting?",
  options=["A threat", "An undesired aircraft state", "A countermeasure", "A latent condition"],
  answer=1,
  explain="The error (missed thrust setting) creates an undesired aircraft state (low speed), which must be recovered before it becomes an upset.",
),
),
]
