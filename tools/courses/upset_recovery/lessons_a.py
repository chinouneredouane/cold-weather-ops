# Upset Prevention and Recovery — lessons 1–8
from .diagrams import upset_envelope, angles, lift_curve, load_factor, coffin_corner, stability

LESSONS_A = [
# ---------------------------------------------------------------- 1
dict(
title="Course Orientation and the UPRT Framework",
minutes=7,
objectives=[
  "Describe the purpose, structure and assessment of this course.",
  "Identify the ICAO provisions and guidance that define upset prevention and recovery training (UPRT).",
  "Explain the three components of UPRT: academic, simulator (FSTD) and on-aeroplane training.",
],
body="""
<h2>Why this course exists</h2>
<p>Loss of control in flight (LOC-I) has been the largest single cause of fatalities in commercial air transport for many years. LOC-I accidents are rare, but most of them are not survivable. Investigations repeatedly found that crews met an unusual situation they had never practised, and they either did not recognise it in time or did not apply an effective recovery.</p>
<p>The aim of UPRT is first to <strong>prevent</strong> upsets — through knowledge, awareness and good flight path management — and then to make sure that pilots can <strong>recognise and recover</strong> from one if it happens. Prevention always comes first.</p>

<h2>The international framework</h2>
<div class="table-wrap"><table>
  <tr><th>Document</th><th>Content</th></tr>
  <tr><td>ICAO Annex 1 — Personnel Licensing</td><td>UPRT requirements in pilot licence training, including the multi-crew pilot licence (MPL)</td></tr>
  <tr><td>ICAO Annex 6, Part I — Operation of Aircraft</td><td>UPRT within operators' flight crew training programmes</td></tr>
  <tr><td>PANS-TRG (ICAO Doc 9868)</td><td>Procedures for training, including UPRT in licence and type rating training</td></tr>
  <tr><td>ICAO Doc 10011 — Manual on Aeroplane Upset Prevention and Recovery Training</td><td>The guidance on which this course is based: definitions, academic training elements, FSTD and on-aeroplane training</td></tr>
  <tr><td>Airplane Upset Prevention and Recovery Training Aid (AUPRTA), Revision 3</td><td>Industry guidance by the major manufacturers with ICAO, including recovery techniques</td></tr>
</table></div>
<p>National authorities, such as EASA and the FAA, have turned these provisions into licensing and operator requirements. The Domestic Airlines Operations Manual and the aircraft manufacturer's procedures (FCOM, QRH, FCTM) apply them to our fleet.</p>

<h2>The three components of UPRT</h2>
<ul>
  <li><strong>Academic training</strong> — the knowledge behind prevention and recovery: aerodynamics, causes of upsets, human factors and recovery principles. <em>This course covers the academic component.</em></li>
  <li><strong>FSTD (simulator) training</strong> — practice of prevention and recovery in the aircraft type, within the validated training envelope of the simulator.</li>
  <li><strong>On-aeroplane training</strong> — training in a suitable aeroplane, usually during licence training, which gives the real physiological sensations of g and unusual attitudes.</li>
</ul>

<h2>How to use this course</h2>
<ul>
  <li>24 lessons in 7 modules, about 3 hours in total. A lesson is marked complete when you reach its end or press <em>Next</em>.</li>
  <li>Each lesson has narration, a picture, diagrams, key takeaways and a practice knowledge check.</li>
  <li>The final quiz draws 20 questions from the question bank. The pass mark is 80 %.</li>
  <li>Your progress is saved in this browser on this device.</li>
</ul>

<div class="callout warn"><span class="label">Important</span>
<p>Recovery techniques in this course are generic principles from ICAO and industry guidance. <strong>Always use the procedures of the aircraft manufacturer</strong> (FCOM, QRH and FCTM) for your type. Where they differ from this course, the manufacturer's procedures take precedence.</p>
</div>
""",
takeaways=[
  "LOC-I is the leading cause of fatalities in commercial air transport; prevention comes first.",
  "ICAO Doc 10011 defines UPRT; Annex 1, Annex 6 and PANS-TRG require it.",
  "UPRT has three parts: academic, FSTD and on-aeroplane. This course is the academic part.",
  "Manufacturer procedures always take precedence over generic recovery techniques.",
],
check=dict(
  q="Which ICAO document is the main guidance manual for upset prevention and recovery training?",
  options=["Doc 9640", "Doc 10011", "Doc 4444", "Doc 9981"],
  answer=1,
  explain="ICAO Doc 10011 is the Manual on Aeroplane Upset Prevention and Recovery Training.",
),
),

# ---------------------------------------------------------------- 2
dict(
title="Upsets and Loss of Control: Definitions",
minutes=7,
objectives=[
  "State the definition of an aeroplane upset.",
  "Distinguish a developing upset from a fully developed upset and from loss of control in flight.",
  "Explain why early recognition is the most effective defence.",
],
body="""
<h2>What is an upset?</h2>
<p>An <strong>upset</strong> is an undesired aircraft state characterised by unintentional divergences from the parameters normally experienced during line operations or training. In practice, an aeroplane is generally considered to be in an upset when it unintentionally exceeds one or more of these values:</p>
<ul>
  <li><strong>pitch attitude more than 25° nose-up;</strong></li>
  <li><strong>pitch attitude more than 10° nose-down;</strong></li>
  <li><strong>bank angle more than 45°;</strong></li>
  <li>or, within these values, an <strong>airspeed inappropriate for the conditions</strong>.</li>
</ul>
""" + upset_envelope() + """
<h2>Developing and developed upsets</h2>
<p>An upset does not appear from nowhere. It nearly always begins as a <strong>developing upset</strong> — a deviation that is growing: speed decaying on approach, bank slowly increasing after an autopilot disconnect, pitch rising in turbulence. At this stage a small, early correction is usually enough.</p>
<p>If the deviation is not detected or corrected, it becomes a <strong>developed upset</strong>, where large control inputs and a structured recovery are needed. If recovery is not achieved, the result is <strong>loss of control in flight (LOC-I)</strong>: the aircraft departs from controlled flight, often with a stall, and may not be recoverable in the altitude available.</p>
<div class="callout"><span class="label">The key idea</span><p>The earlier a deviation is recognised, the smaller the correction and the larger the safety margin. Prevention and early recognition are far more effective than any recovery technique.</p></div>

<h2>Stall and upset</h2>
<p>A stall can be both a <strong>cause</strong> and a <strong>result</strong> of an upset. A stalled aeroplane may roll or pitch uncontrollably; an aeroplane in a nose-high upset may stall. In every case, <strong>stall recovery takes priority</strong> — you cannot recover the attitude while the wing is stalled (Lesson 19).</p>

<h2>Why upsets are dangerous</h2>
<ul>
  <li>They are rare, so most pilots have little or no real experience of them.</li>
  <li>They often arrive with <strong>startle and surprise</strong>, which slow down recognition and decision-making (Lesson 14).</li>
  <li>They may happen at night, in cloud or with failed instruments, where visual references are missing.</li>
  <li>The wrong instinctive reaction — such as pulling back when the aeroplane is stalled — can make them worse.</li>
</ul>
""",
takeaways=[
  "Upset: unintentional pitch above 25° nose-up or 10° nose-down, bank above 45°, or inappropriate speed.",
  "Developing upsets need small, early corrections; developed upsets need a structured recovery.",
  "Stall recovery always takes priority over attitude recovery.",
],
check=dict(
  q="Which of these situations meets the definition of an upset?",
  options=["A 30° bank turn in a holding pattern", "Unintentional bank of 55° after an autopilot disconnect", "A 15° nose-up pitch during a normal take-off", "A 3° glide path on approach"],
  answer=1,
  explain="An unintentional bank angle greater than 45° is an upset. The other situations are normal, intended manoeuvres.",
),
),

# ---------------------------------------------------------------- 3
dict(
title="Causes and Contributing Factors of Upsets",
minutes=8,
objectives=[
  "Describe the three main families of upset causes: environmental, systems-induced and pilot-induced.",
  "Recognise how several factors usually combine in an upset.",
  "Relate each family of causes to prevention strategies.",
],
body="""
<h2>Three families of causes</h2>
<div class="table-wrap"><table>
  <tr><th>Family</th><th>Examples</th></tr>
  <tr><td><strong>Environmentally induced</strong></td><td>Turbulence and clear-air turbulence; mountain waves; windshear and microbursts; wake turbulence; thunderstorms; airframe icing; temperature changes at high altitude</td></tr>
  <tr><td><strong>Systems-induced</strong></td><td>Autopilot or autothrust behaviour and disconnects; flight control malfunctions or degraded control laws; erroneous air data (unreliable airspeed); instrument failures; asymmetric thrust or engine failure</td></tr>
  <tr><td><strong>Pilot-induced</strong></td><td>Inattention and poor monitoring; distraction; inappropriate control inputs; mode confusion; poor energy management; spatial disorientation; startle; fatigue; inadequate manual flying skill</td></tr>
</table></div>

<h2>Upsets are rarely caused by one factor</h2>
<p>Accident investigations show a typical pattern: an <strong>initial trigger</strong> — often environmental or technical — followed by <strong>human responses</strong> that do not contain it, or that make it worse. For example:</p>
<ul>
  <li>Ice crystals block the pitot probes (environmental) → the autopilot disconnects and air data is unreliable (systems) → the pilot makes sustained nose-up inputs under stress (pilot-induced) → the aircraft stalls.</li>
  <li>A faulty sensor causes the autothrust to reduce thrust (systems) → the crew does not notice the speed decay (monitoring) → the stall warning surprises them at low altitude (startle).</li>
</ul>

<h2>Prevention strategies for each family</h2>
<ul>
  <li><strong>Environmental:</strong> knowledge of the threats, weather avoidance, respecting wake separation, briefing and planning, and using the right speeds and altitudes with adequate margins (Lesson 12).</li>
  <li><strong>Systems:</strong> understanding the automation and its modes, monitoring the flight mode annunciations, knowing the memory items for unreliable airspeed and flight control malfunctions (Lessons 13 and 18).</li>
  <li><strong>Pilot:</strong> disciplined monitoring, manual handling practice, energy awareness, managing startle, fatigue awareness and CRM (Lessons 14–16).</li>
</ul>
<div class="callout"><span class="label">Threat and error management</span><p>Treat every cause as a <strong>threat</strong> to be anticipated and briefed. Most upset-related accidents could have been stopped at the threat or error stage — long before an upset recovery was needed.</p></div>
""",
takeaways=[
  "Causes are environmental, systems-induced or pilot-induced — usually in combination.",
  "A technical or weather trigger often becomes an upset through human responses.",
  "Each family of causes has its own prevention strategy.",
],
check=dict(
  q="Which is an example of a systems-induced upset cause?",
  options=["Wake turbulence from a preceding aircraft", "Unreliable airspeed after a pitot probe blockage", "A microburst on approach", "Fatigue during a night flight"],
  answer=1,
  explain="Erroneous air data from a blocked pitot probe is a systems-induced factor, even if the blockage itself was caused by weather.",
),
),

# ---------------------------------------------------------------- 4
dict(
title="Lift, Angle of Attack and Flight Path",
minutes=9,
objectives=[
  "Explain the relationship between lift, airspeed, air density and angle of attack.",
  "Distinguish pitch attitude, flight path angle and angle of attack.",
  "Explain why angle of attack, not attitude or speed, determines the stall.",
],
body="""
<h2>The lift equation</h2>
<p>Lift depends on four things: <strong>air density</strong>, <strong>true airspeed (squared)</strong>, <strong>wing area</strong> and the <strong>lift coefficient</strong>, which mainly depends on the angle of attack and the wing configuration (flaps and slats).</p>
<p><code>Lift = ½ × ρ × V² × S × CL</code></p>
<p>At a given weight, the aircraft needs a certain amount of lift. If the speed decreases, the angle of attack must increase to keep the same lift — until the wing reaches its <strong>critical angle of attack</strong>. Speed and angle of attack are linked, but they are not the same thing.</p>

<h2>Three different angles</h2>
""" + angles() + """
<ul>
  <li><strong>Pitch attitude (θ)</strong> — the angle between the aircraft's longitudinal axis and the horizon. It is what the attitude indicator shows.</li>
  <li><strong>Flight path angle (γ)</strong> — the angle between the aircraft's path through the air and the horizon. A flight path vector, where fitted, shows it.</li>
  <li><strong>Angle of attack (α)</strong> — the angle between the wing chord and the relative airflow. It decides how much lift the wing produces, and whether it stalls.</li>
</ul>
<p>In normal flight the three are close together and easy to confuse. In an upset they can be very different. An aircraft in a stalled descent can have a nose-up pitch attitude, a steeply descending flight path, and an angle of attack far above the critical value.</p>

<h2>The lift curve</h2>
""" + lift_curve() + """
<p>As the angle of attack increases, lift increases almost linearly — until the airflow can no longer follow the upper surface of the wing. Beyond the critical angle of attack, the flow separates, lift falls and drag rises sharply. This is the <strong>stall</strong>.</p>
<div class="callout warn"><span class="label">Key principle</span><p>A wing can stall at <strong>any airspeed, any attitude and any power setting</strong>. The only way to unstall it is to <strong>reduce the angle of attack</strong>.</p></div>

<h2>Angle of attack information on the flight deck</h2>
<ul>
  <li>Stall warning (stick shaker, aural warning) and, on some types, a stick pusher are triggered by angle of attack sensors.</li>
  <li>Low-speed bands, pitch limit indicators and angle of attack indicators (where fitted) help you see how close you are to the critical angle.</li>
  <li>Know which of these your aircraft has, and how they behave if air data is unreliable.</li>
</ul>
""",
takeaways=[
  "Lift depends on density, speed², wing area and lift coefficient (angle of attack and configuration).",
  "Pitch attitude = flight path angle + angle of attack — they can be very different in an upset.",
  "The wing stalls at its critical angle of attack — at any speed, attitude or power.",
  "The only cure for a stall is to reduce the angle of attack.",
],
check=dict(
  q="An aircraft is 10° nose-up but descending steeply. What does this tell you about its angle of attack?",
  options=["It must be close to zero", "It is very high — possibly beyond the critical angle", "It is negative", "It cannot be determined from attitude and flight path"],
  answer=1,
  explain="Angle of attack = pitch attitude − flight path angle. With the nose up and the path steeply down, the angle of attack is very high.",
),
),

# ---------------------------------------------------------------- 5
dict(
title="The Stall",
minutes=9,
objectives=[
  "Describe the aerodynamic characteristics of an approach to stall and a full stall.",
  "Identify stall warning systems and natural stall cues.",
  "Explain the factors that change stall speed and stall behaviour.",
],
body="""
<h2>Approach to stall and full stall</h2>
<ul>
  <li><strong>Approach to stall (impending stall)</strong> — the angle of attack is approaching the critical value. Indications: stall warning (stick shaker, aural warning), low-speed indications, and possibly the onset of buffet.</li>
  <li><strong>Full stall</strong> — the critical angle of attack has been exceeded. Indications may include buffet (sometimes heavy), an uncommanded nose-down pitch or roll, inability to arrest a descent, loss of pitch authority, and stick pusher activation on aircraft that have one.</li>
</ul>
<p>Both require the same immediate action: <strong>reduce the angle of attack</strong>.</p>

<h2>Stall warning and protection systems</h2>
<ul>
  <li><strong>Stall warning</strong> (stick shaker, aural alert) activates with a margin before the stall — on transport aeroplanes, at a speed and angle of attack set by certification requirements.</li>
  <li><strong>Stick pusher</strong> (some types) pushes the control column forward to prevent the aircraft from reaching an aerodynamic stall. Do not fight it.</li>
  <li><strong>Envelope protection</strong> (fly-by-wire types in normal law) limits angle of attack — but protections can be lost when the control law degrades, for example with unreliable air data.</li>
  <li>Stall warning is scheduled for a <strong>clean wing</strong>. With ice or contamination, the stall may occur <strong>before</strong> the warning.</li>
</ul>

<h2>What changes the stall speed</h2>
<div class="table-wrap"><table>
  <tr><th>Factor</th><th>Effect on stall speed</th></tr>
  <tr><td>Higher weight</td><td>Increases (stall speed is proportional to √weight)</td></tr>
  <tr><td>Higher load factor (turns, pull-ups)</td><td>Increases with √n — about 41 % higher at 2 g (Lesson 6)</td></tr>
  <tr><td>Flaps and slats extended</td><td>Decreases (higher CLmax)</td></tr>
  <tr><td>Ice or contamination</td><td>Increases, and the critical angle of attack decreases</td></tr>
  <tr><td>Forward centre of gravity</td><td>Increases slightly (more tail down-force needed)</td></tr>
  <tr><td>Higher altitude</td><td>Indicated stall speed changes little at low altitude, but Mach effects raise it at high altitude (Lesson 7)</td></tr>
</table></div>

<h2>Stall behaviour</h2>
<ul>
  <li>Swept wings tend to stall at the tips first, which can cause roll-off and a nose-up pitching tendency. Design features (washout, vortex generators, fences) reduce this.</li>
  <li>Aircraft with T-tails may be susceptible to a <strong>deep stall</strong>, which is why they are often fitted with stick pushers.</li>
  <li>Power effects: on aircraft with underwing engines, high thrust gives a nose-up pitching moment (Lesson 10) which can work against stall recovery.</li>
  <li>Simulators may not reproduce full-stall behaviour accurately outside their validated envelope (Lesson 24).</li>
</ul>
<div class="callout caution"><span class="label">Remember</span><p>Pulling back to "hold altitude" when the stall warning activates increases the angle of attack — the opposite of what is needed. Altitude loss is secondary; <strong>reducing the angle of attack is the priority</strong>.</p></div>
""",
takeaways=[
  "Approach to stall and full stall both require an immediate reduction in angle of attack.",
  "Stall warning is scheduled for a clean wing — ice can cause a stall without warning.",
  "Weight, load factor, configuration and contamination change the stall speed.",
  "Do not fight a stick pusher.",
],
check=dict(
  q="The stick shaker activates during a level-off. What is the first priority?",
  options=["Maintain altitude with back pressure", "Reduce the angle of attack", "Increase bank to turn away", "Extend the speedbrakes"],
  answer=1,
  explain="The stall warning indicates a high angle of attack. Reducing the angle of attack is the first priority, even at the cost of altitude.",
),
),

# ---------------------------------------------------------------- 6
dict(
title="Load Factor and g-Awareness",
minutes=8,
objectives=[
  "Calculate load factor in a level turn and its effect on stall speed.",
  "State the structural limit load factors of transport aeroplanes and the meaning of manoeuvring speed.",
  "Apply g-awareness during upset recovery.",
],
body="""
<h2>Load factor</h2>
<p><strong>Load factor (n)</strong> is the ratio of lift to weight, felt as "g". In straight and level flight n = 1. In a level turn the wing must produce extra lift to hold altitude:</p>
<p><code>n = 1 / cos(bank angle)</code> — 30° gives 1.15 g, 45° gives 1.41 g, 60° gives 2 g.</p>
""" + load_factor() + """
<h2>Load factor and stall speed</h2>
<p>Stall speed increases with the square root of the load factor: <code>V<sub>S(n)</sub> = V<sub>S</sub> × √n</code>. At 60° of bank (2 g) the stall speed is about 41 % higher. This is why steep turns at low speed are dangerous, and why <strong>unloading</strong> — relaxing back pressure to reduce g — is a powerful way to lower the stall speed and the angle of attack during recovery.</p>

<h2>Structural limits</h2>
<ul>
  <li>Transport aeroplanes are typically designed for limit manoeuvring load factors of <strong>+2.5 g to −1.0 g</strong> with flaps retracted, and <strong>+2.0 g to 0 g</strong> with flaps extended. Check your AFM.</li>
  <li>Exceeding these limits may cause permanent structural deformation; the ultimate load (1.5 × limit) is where failure may occur.</li>
  <li>Rolling and pulling at the same time (a "rolling pull") produces asymmetric loads, which have lower limits.</li>
</ul>

<h2>Manoeuvring speed (V<sub>A</sub>)</h2>
<p>Below V<sub>A</sub>, a single full deflection of one flight control <strong>in one axis</strong> should not exceed structural limits. V<sub>A</sub> does <strong>not</strong> protect against:</p>
<ul>
  <li>full deflections in more than one axis at the same time;</li>
  <li>rapid <strong>alternating</strong> or reversing inputs, especially of the rudder (Lesson 8 — American Airlines 587).</li>
</ul>

<h2>g-awareness in recovery</h2>
<ul>
  <li>In a <strong>nose-high</strong> recovery, reduced or even slightly negative g (unloading) is often needed. It may feel uncomfortable; loose objects and unrestrained people can be thrown about.</li>
  <li>In a <strong>nose-low</strong> recovery, roll wings level <strong>before</strong> pulling, then pull smoothly — avoiding both the stall warning and excessive g.</li>
  <li>The sensation of g is not a reliable indicator of attitude; use the instruments.</li>
</ul>
""",
takeaways=[
  "Level turn: n = 1/cos(bank); 60° of bank = 2 g.",
  "Stall speed rises with √n: +41 % at 2 g. Unloading lowers stall speed and angle of attack.",
  "Typical limits flaps up: +2.5 g / −1.0 g. Avoid rolling pulls.",
  "VA does not protect against multiple-axis or alternating full inputs.",
],
check=dict(
  q="An aircraft with a 1 g stall speed of 120 kt is in a level 60° bank turn. What is its approximate stall speed?",
  options=["120 kt", "about 140 kt", "about 170 kt", "240 kt"],
  answer=2,
  explain="60° of bank gives 2 g; √2 ≈ 1.41; 120 × 1.41 ≈ 170 kt.",
),
),

# ---------------------------------------------------------------- 7
dict(
title="High-Altitude Aerodynamics",
minutes=9,
objectives=[
  "Explain the effects of Mach number and low air density on aircraft handling at high altitude.",
  "Describe buffet boundaries, buffet margins and the coffin corner.",
  "Recognise why recovery at high altitude needs a different approach from recovery at low altitude.",
],
body="""
<h2>Thin air and Mach effects</h2>
<p>At high altitude the air is thin. To produce the required lift, the aircraft flies at a high true airspeed and a relatively high angle of attack. At the same time, the speed of sound is lower in colder air, so the aircraft operates close to its <strong>critical Mach number</strong>. Two important consequences follow:</p>
<ul>
  <li>The critical angle of attack <strong>decreases</strong> as Mach number increases. The aircraft can stall at a lower angle of attack — and a higher indicated speed — than at low altitude.</li>
  <li>Engines produce much less excess thrust. There is little energy available to accelerate or climb.</li>
</ul>

<h2>Buffet boundaries and the coffin corner</h2>
""" + coffin_corner() + """
<ul>
  <li><strong>Low-speed buffet</strong> is the onset of airflow separation as the stall approaches.</li>
  <li><strong>High-speed (Mach) buffet</strong> is caused by shock waves and flow separation as the aircraft approaches its maximum Mach.</li>
  <li>As altitude and weight increase, the two boundaries come closer together. The point where they meet is often called the <strong>coffin corner</strong>.</li>
</ul>
<p>Operators commonly plan cruise levels with a margin to buffet of at least <strong>1.3 g</strong> — enough to absorb turbulence or a bank of about 40° without reaching buffet. The FMS "maximum altitude" usually includes such a margin. Flying above the optimum altitude reduces it.</p>

<h2>Handling at high altitude</h2>
<ul>
  <li><strong>Aerodynamic damping is lower</strong>: the aircraft responds more slowly and oscillations take longer to settle.</li>
  <li><strong>Small pitch changes produce large vertical speeds</strong> because of the high true airspeed.</li>
  <li><strong>Control inputs should be smooth and small.</strong> Large, rapid inputs can quickly exceed the buffet margin.</li>
  <li>Watch for temperature increases and wind shifts that suddenly reduce the Mach or speed margin.</li>
</ul>

<h2>Recovery at high altitude</h2>
<div class="callout warn"><span class="label">Key principle</span>
<p>At high altitude, an aircraft at or near the stall <strong>cannot be "powered out" of it</strong>. The excess thrust is too small. The angle of attack must be reduced, and the aircraft must be allowed to <strong>lose altitude</strong> to regain speed and margin. Trading altitude for speed is the correct action.</p>
</div>
<p>Accept a significant altitude loss. Return to the cleared level only after the aircraft is under control and the speed is appropriate. Inform ATC as soon as possible.</p>
""",
takeaways=[
  "The critical angle of attack decreases as Mach increases — high-altitude stalls occur at lower angles.",
  "Buffet boundaries converge with altitude and weight; keep at least the planned buffet margin.",
  "Damping is low and vertical speed changes are large — use small, smooth inputs.",
  "At high altitude, recover by reducing angle of attack and trading altitude for speed.",
],
check=dict(
  q="At FL390 the aircraft approaches a stall. What is the most effective recovery action?",
  options=["Apply maximum thrust and hold altitude", "Reduce the angle of attack and accept an altitude loss to regain speed", "Increase pitch to climb above the turbulence", "Extend flaps to lower the stall speed"],
  answer=1,
  explain="Excess thrust at high altitude is small. The angle of attack must be reduced, and altitude traded for speed.",
),
),

# ---------------------------------------------------------------- 8
dict(
title="Stability, Control and Rudder Use",
minutes=9,
objectives=[
  "Describe static and dynamic stability in pitch, roll and yaw.",
  "Explain the role of trim and the dangers of an out-of-trim condition.",
  "Apply correct rudder use and avoid hazardous rudder inputs.",
],
body="""
<h2>Static and dynamic stability</h2>
""" + stability() + """
<ul>
  <li><strong>Static stability</strong> is the initial tendency after a disturbance. <strong>Dynamic stability</strong> is what happens over time — whether the oscillations die out, continue or grow.</li>
  <li><strong>Longitudinal (pitch) stability</strong> depends mainly on the centre of gravity position relative to the neutral point. Aft CG reduces it (Lesson 11).</li>
  <li><strong>Lateral (roll) stability</strong> comes from wing dihedral and sweep. Swept wings produce a strong roll from sideslip (dihedral effect).</li>
  <li><strong>Directional (yaw) stability</strong> comes from the vertical stabiliser. The interaction of yaw and roll produces <strong>Dutch roll</strong>, which yaw dampers suppress.</li>
</ul>

<h2>Control surface fundamentals</h2>
<ul>
  <li>Control effectiveness depends on dynamic pressure: at low speed, larger deflections are needed; at high speed, small inputs have large effects.</li>
  <li>Spoilers assist roll on many jets. At high angles of attack, aileron effectiveness may be reduced and adverse yaw increased.</li>
  <li>The horizontal stabiliser (trim) is much more powerful than the elevator. If the stabiliser is trimmed fully nose-up, the elevator alone may not be able to lower the nose.</li>
</ul>

<h2>Trim</h2>
<p>The autopilot trims continuously. When it disconnects, the aircraft can be out of trim — for example after the autopilot has been holding a roll against an asymmetry, or trimming nose-up while speed decayed. Be ready for this whenever the autopilot disconnects. In a recovery, use <strong>pitch trim</strong> carefully to help achieve the required pitch, and do not leave the aircraft trimmed for an unsafe condition.</p>

<h2>Rudder use</h2>
<div class="callout warn"><span class="label">Warning</span>
<p>Rapid, <strong>alternating</strong> (cyclic) rudder inputs can generate loads beyond the design limits of the vertical stabiliser — even below V<sub>A</sub>. In November 2001, American Airlines Flight 587, an Airbus A300-600, encountered wake turbulence after take-off from New York. The first officer made repeated full rudder inputs from side to side. The vertical stabiliser separated and the aircraft crashed, killing 265 people.</p>
</div>
<ul>
  <li>On swept-wing transport aeroplanes, the rudder is mainly used for <strong>asymmetric thrust</strong>, crosswind take-offs and landings, and specific procedures.</li>
  <li>It is <strong>not</strong> normally used to roll the aircraft in upset recovery. Roll with aileron and spoiler. Use rudder only as the manufacturer's procedure states — for example when aileron and spoiler authority is not enough.</li>
  <li>Large rudder inputs at high speed produce sideslip and strong roll moments.</li>
</ul>
""",
takeaways=[
  "Static stability is the first tendency; dynamic stability is the behaviour over time.",
  "The stabiliser is more powerful than the elevator — mis-trim can limit recovery.",
  "Expect an out-of-trim condition when the autopilot disconnects.",
  "Never make rapid alternating rudder inputs; roll with aileron and spoiler.",
],
check=dict(
  q="What was the key lesson of the American Airlines 587 accident?",
  options=["Use full rudder to recover from wake turbulence", "Alternating rudder inputs can overload the vertical stabiliser even below VA", "Autopilot should be engaged in wake turbulence", "Spoilers are ineffective at high speed"],
  answer=1,
  explain="Repeated full rudder reversals generated loads that exceeded the vertical stabiliser's limits, even though the aircraft was below manoeuvring speed.",
),
),
]
