# Cold Weather Operations — lessons 21–30

LESSONS_C = [
# ---------------------------------------------------------------- 21
dict(
title="Aircraft Systems in Cold Conditions",
minutes=8,
objectives=[
  "Describe the effects of low temperatures on hydraulic, pneumatic, electrical and landing gear systems.",
  "Recognise cold-related problems with doors, slides, windows and water systems.",
  "Apply warm-up and checking procedures before flight.",
],
body="""
<h2>Hydraulics</h2>
<ul>
  <li>Hydraulic fluid becomes more viscous, so actuators move more slowly and pumps work harder.</li>
  <li>Cold seals contract and harden. Small leaks may appear after a cold soak and may stop after warm-up. Report them to maintenance.</li>
  <li>Reservoir levels and accumulator pre-charge pressures read lower in the cold. Use the temperature-corrected values.</li>
  <li>Operate the systems as the FCOM requires to warm the fluid before flight-control checks.</li>
</ul>

<h2>Pneumatics and air conditioning</h2>
<ul>
  <li>Water in ducts, water separators and drains can freeze. Check for unusual pack behaviour or fault messages.</li>
  <li>Bleed air demand from anti-ice systems reduces the bleed available for air conditioning and engine thrust.</li>
</ul>

<h2>Electrical and avionics</h2>
<ul>
  <li>Battery capacity is significantly lower in the cold. Check the voltage before an APU start on battery power.</li>
  <li>Displays and some avionics may need time to warm up. Follow the FCOM for warm-up before alignment.</li>
</ul>

<h2>Landing gear and brakes</h2>
<ul>
  <li>Shock struts can appear low after cold soak, because the gas and fluid contract. Check the servicing charts.</li>
  <li>Brakes can freeze after taxiing through slush or after washing. Check that the wheels turn at the start of taxi, and use gentle braking to dry and warm them.</li>
  <li>Ice and packed snow in wheel wells and on gear doors and switches can prevent retraction or extension, or cause false indications.</li>
</ul>

<h2>Doors, slides and windows</h2>
<ul>
  <li>Door seals can freeze to the frame. Do not force a frozen door. Follow the procedure, and ask for warm air or de-icing if needed.</li>
  <li>Slide bottle pressure is lower in the cold, and slides inflate more slowly. Check the temperature-corrected pressure gauges during the walk-around.</li>
  <li>Windshields: switch on window heat early to avoid thermal stress. Do not use hot fluid or hot water on cold windshields.</li>
</ul>

<h2>Water and waste</h2>
<p>Potable water lines, drains, waste tanks and valves freeze quickly in an unheated aircraft. If the aircraft was not drained overnight, check with maintenance before using the systems, and report any frozen lines. Lavatory and galley drains that freeze can lead to flooding or, in flight, ice that can break off and strike the airframe or engines.</p>
""",
takeaways=[
  "Cold hydraulic fluid slows actuators; seal leaks may appear after cold soak.",
  "Batteries, slide bottles and oxygen bottles show lower values in the cold — use corrected charts.",
  "Frozen brakes and iced wheel wells are common after slush taxi.",
  "Never force a frozen door; switch on window heat early.",
],
check=dict(
  q="During the walk-around at −20 °C, an escape slide bottle gauge reads lower than usual. What should you do?",
  options=["Ground the aircraft immediately", "Compare it with the temperature-corrected pressure chart", "Ignore it, because slides always work", "Ask the cabin crew to warm the slide"],
  answer=1,
  explain="Gas bottle pressures drop with temperature. The reading must be compared with the temperature-corrected minimum value before any decision.",
),
),

# ---------------------------------------------------------------- 22
dict(
title="Fuel Management at Low Temperatures",
minutes=8,
objectives=[
  "State the freezing points of common jet fuels and the operational fuel temperature limit.",
  "Manage low fuel temperature in flight.",
  "Plan winter fuel for de-icing, taxi and holding.",
],
body="""
<h2>Fuel freezing points</h2>
<div class="table-wrap"><table>
  <tr><th>Fuel</th><th>Maximum freezing point (specification)</th></tr>
  <tr><td>Jet A-1</td><td>−47 °C</td></tr>
  <tr><td>Jet A</td><td>−40 °C</td></tr>
</table></div>
<p>Fuel does not freeze solid at once. As it cools, wax crystals form, which can block filters and reduce flow. The AFM limit is usually the fuel freezing point plus a margin — commonly <strong>3 °C above the freezing point</strong> — or a fixed minimum fuel temperature, whichever is higher. If the actual freezing point of the uplifted fuel is known from the fuel documentation, the AFM may allow its use.</p>
<p>When fuel from different sources is mixed (for example, Jet A uplifted on top of Jet A-1), the most restrictive freezing point applies unless the actual value of the mix is known.</p>

<h2>Low fuel temperature in flight</h2>
<p>On long sectors at high altitude through very cold air, fuel temperature falls slowly towards the total air temperature (TAT). If the fuel temperature approaches the limit:</p>
<ul>
  <li><strong>Increase speed</strong> — a higher Mach number raises TAT through ram-air heating. Roughly +0.01 Mach gives about +0.5 to +0.7 °C TAT;</li>
  <li><strong>Descend</strong> into warmer air, if it is available;</li>
  <li><strong>Change route</strong> away from the coldest air mass.</li>
</ul>
<p>Every option costs fuel, so act early. Fuel temperature changes slowly, and a corrective action can take a long time to show an effect.</p>

<h2>Water and ice in fuel</h2>
<p>Fuel always contains some dissolved water. At low temperatures it comes out as droplets and ice crystals. Fuel heaters and fuel/oil heat exchangers deal with normal amounts. Unusual accumulations of ice in the fuel system have caused engine power problems. A well-known case is the 2008 Boeing 777 accident at London Heathrow (BA38), where ice released from the fuel system restricted the fuel flow during the final approach. Regular water draining by maintenance is an important defence.</p>

<h2>Winter fuel planning</h2>
<ul>
  <li>Add fuel for the expected <strong>de-icing delay</strong>, longer taxi times, APU use, and the possibility of returning for a second treatment.</li>
  <li>Add fuel for <strong>holding</strong> at a destination with snow clearance or reduced runway capacity, and for a more distant alternate if nearby airports have the same weather.</li>
  <li>Remember the cold-soak effect: tankering large quantities of very cold fuel can lead to frost or clear ice on the wings at the next station (Lesson 3).</li>
</ul>
""",
takeaways=[
  "Jet A-1 freezes at −47 °C, Jet A at −40 °C; the limit is typically the freezing point + 3 °C.",
  "Low fuel temperature in flight: increase Mach, descend or reroute — act early.",
  "Plan extra fuel for de-icing, taxi, holding and distant alternates.",
],
check=dict(
  q="Fuel temperature is approaching the limit in cruise. Which action raises the fuel temperature?",
  options=["Reducing speed", "Climbing higher", "Increasing Mach number or descending into warmer air", "Switching off the fuel pumps"],
  answer=2,
  explain="Increasing Mach number raises TAT through ram-air heating, and descending normally brings warmer air. Both slowly warm the fuel.",
),
),

# ---------------------------------------------------------------- 23
dict(
title="Flight Controls, Fluid Residues and In-flight Icing",
minutes=9,
objectives=[
  "Perform an effective flight-control check after de-icing.",
  "Recognise the hazard of thickened fluid residues.",
  "Operate ice protection systems and respond to SLD and tailplane icing.",
],
body="""
<h2>Flight-control check</h2>
<ul>
  <li>After de-icing and before take-off, check that the flight controls move <strong>full and free</strong> in the correct sense, as the checklist requires.</li>
  <li>Check smoothly and slowly. Any stiffness, restriction or unusual noise is a reason to stop and investigate. Do not take off with doubtful controls.</li>
  <li>Ice or snow in control surface gaps and hinges can restrict movement even when the surfaces themselves look clean.</li>
</ul>

<h2>Thickened fluid residues</h2>
<p>Type II and IV fluids can dry out and leave a residue in the aerodynamically quiet areas of the aircraft. This is more likely when they are used for one-step treatments without a hot Type I de-icing step. When rehydrated by rain or humidity, the residue swells into a gel that can <strong>freeze in flight</strong>.</p>
<div class="callout warn"><span class="label">Reported symptoms</span>
<p>Restricted or stiff elevator, aileron or trim movement, often at high altitude, sometimes with vibration. Report any unusual control feel in the technical log. Maintenance carries out residue inspections and cleaning at the intervals in the maintenance programme.</p>
</div>

<h2>Ice protection systems</h2>
<ul>
  <li><strong>Thermal (bleed air or electrical) anti-ice</strong> on wing leading edges, engine inlets, probes and windows: switch on before or when entering icing conditions, as the AFM requires.</li>
  <li><strong>Pneumatic de-icing boots</strong> on many turboprops: current guidance for most modern aircraft is to activate them at the first sign of ice and keep them operating. Follow your AFM.</li>
  <li>Ice detectors give a warning, but primary or advisory status depends on the type. Know which yours is.</li>
  <li>Use the minimum speeds for icing and the autopilot limitations in icing conditions from the AFM. The autopilot can hide changes in handling until it disconnects.</li>
</ul>

<h2>Severe icing and SLD</h2>
<p>Signs of severe icing or supercooled large droplets include:</p>
<ul>
  <li>ice behind the protected areas, such as on the upper or lower wing surface aft of the boots;</li>
  <li>ice on the side windows, or water splashing and streaming on the windshield at sub-zero temperatures;</li>
  <li>unusual or uncommanded roll, or unexpected aileron or trim forces;</li>
  <li>a rapid loss of speed or climb performance.</li>
</ul>
<p><strong>Action:</strong> tell ATC and <strong>leave the icing conditions immediately</strong> — change altitude or heading, or move to colder or warmer air. Disconnect the autopilot carefully if the AFM requires it, holding the controls firmly, and avoid abrupt manoeuvres.</p>

<h2>Tailplane icing</h2>
<p>The tail is thinner than the wing and collects ice more efficiently. A tailplane stall is most likely when the flaps are extended during the approach. Symptoms are light or buffeting elevator forces, difficulty in trimming, or a sudden nose-down pitch. Recovery differs from a wing stall, and the procedure is type-specific — typically return the flaps to the previous setting and pull back on the controls. Follow the AFM/QRH.</p>
""",
takeaways=[
  "Full and free control check after de-icing — never take off with doubtful controls.",
  "Thickened fluid residues can freeze in flight and restrict controls; report unusual feel.",
  "Severe icing or SLD: inform ATC and leave the conditions immediately.",
  "Tailplane stall is most likely with flap extension; recovery is type-specific.",
],
check=dict(
  q="In flight, you notice ice forming on the side windows and aft of the wing de-icing boots. What should you do?",
  options=["Continue and cycle the boots more often", "Treat it as possible severe icing/SLD — inform ATC and leave the conditions immediately", "Extend flaps to increase lift", "Engage the autopilot to reduce workload"],
  answer=1,
  explain="Ice on side windows and behind protected areas are signs of severe icing or SLD. Inform ATC and leave the icing conditions without delay.",
),
),

# ---------------------------------------------------------------- 24
dict(
title="Cold Temperature Altimetry and En-route Considerations",
minutes=9,
objectives=[
  "Explain why a barometric altimeter over-reads in cold air.",
  "Apply cold temperature corrections to minimum altitudes.",
  "Recognise the limits of baro-VNAV approaches at low temperature.",
],
body="""
<h2>Why cold air is dangerous for terrain clearance</h2>
<p>A barometric altimeter is calibrated for the ICAO Standard Atmosphere (ISA). In air colder than ISA, the pressure levels are closer together. The altimeter then shows a higher altitude than the true altitude. <strong>The aircraft is lower than indicated</strong> — “from high to low, look out below”.</p>
<p>The error is zero at the altimeter setting source (the aerodrome) and grows with height above it. It is greatest in very cold air and over high terrain.</p>

<h2>Rule of thumb</h2>
<div class="callout info"><span class="label">Approximation</span>
<p>Correction ≈ <strong>4 % of the height above the aerodrome for every 10 °C below ISA</strong> (ISA deviation measured at the aerodrome).</p>
<p>Example: aerodrome elevation 2 300 ft, temperature −20 °C. ISA at 2 300 ft ≈ 15 − 4.6 ≈ +10 °C, so ISA −30 °C. Initial approach fix at 5 300 ft, which is 3 000 ft above the aerodrome. Correction ≈ 3 × 4 % × 3 000 = 360 ft. Fly 5 660 ft, or round it up as the company procedure requires.</p>
</div>
<p>For accurate values, use the ICAO PANS-OPS cold temperature correction table or the company table. They apply to the published altitudes on the approach: minimum sector, initial, intermediate and final approach fix altitudes, step-down fixes, missed approach altitudes and the DA/MDA.</p>

<h2>Applying corrections</h2>
<ul>
  <li>The pilot is responsible for applying cold temperature corrections to minimum altitudes, unless the Operations Manual states otherwise.</li>
  <li><strong>Tell ATC</strong> when you apply corrections to an assigned or published altitude, because it affects separation.</li>
  <li>Do not correct altitudes assigned by radar controllers without coordination. Ask whether the assigned altitude is temperature-corrected if you are near terrain.</li>
  <li>The correction applies to the <strong>altimeter</strong> altitudes, not to radio altimeter heights (e.g. a CAT II/III decision height).</li>
</ul>

<h2>Baro-VNAV approaches</h2>
<p>A baro-VNAV glide path is affected by the same error: in cold air the actual path is <strong>lower and shallower</strong> than published. RNP approach charts with LNAV/VNAV minima state a <strong>minimum temperature</strong> below which baro-VNAV must not be used. Some FMS can apply temperature compensation. Use it only as your FCOM and Operations Manual permit.</p>

<h2>En-route winter considerations</h2>
<ul>
  <li>Very cold upper air masses: watch the fuel temperature (Lesson 22).</li>
  <li>Minimum en-route altitudes over high terrain need cold temperature awareness, especially at night with weak pressure gradients.</li>
  <li>Alternates may be affected by the same snow, icing or freezing rain as the destination. Check runway condition forecasts and de-icing availability.</li>
</ul>
""",
takeaways=[
  "In cold air the aircraft is lower than the altimeter shows.",
  "Correction ≈ 4 % per 10 °C below ISA per height above the aerodrome — use the official table.",
  "Correct minimum and approach altitudes and inform ATC; respect baro-VNAV temperature limits.",
],
check=dict(
  q="Aerodrome ISA deviation is −20 °C. A fix is 2 000 ft above the aerodrome. Using the rule of thumb, what is the approximate correction?",
  options=["About 40 ft", "About 160 ft", "About 400 ft", "About 800 ft"],
  answer=1,
  explain="2 × 4 % = 8 %; 8 % of 2 000 ft = 160 ft. Add it to the published altitude.",
),
),

# ---------------------------------------------------------------- 25
dict(
title="Dispatch, MEL/CDL and Winter Flight Planning",
minutes=8,
objectives=[
  "Recognise MEL and CDL items that restrict winter or icing operations.",
  "Plan alternates and fuel for winter conditions.",
  "Use NOTAM and SNOWTAM information in flight planning.",
],
body="""
<h2>MEL items with winter impact</h2>
<p>Many MEL items allow dispatch with a condition such as <em>“provided the aircraft is not operated in known or forecast icing conditions”</em>. In winter, those conditions often make the dispatch impossible. Typical items to check:</p>
<ul>
  <li>Wing or engine anti-ice valves and controllers;</li>
  <li>Probe and window heat;</li>
  <li>Ice detection system;</li>
  <li>Pneumatic boots and propeller de-ice (turboprops);</li>
  <li>APU — needed for heating, engine starts and, at some stations, for de-icing with the engines shut down;</li>
  <li>Thrust reversers and anti-skid, which affect landing and RTO performance on contaminated runways;</li>
  <li>Windshield wipers and rain repellent.</li>
</ul>
<p>CDL items (missing panels, seals or fairings) can change the performance and may also allow contamination into structures. Read the full MEL/CDL conditions, including operational (O) and maintenance (M) procedures.</p>

<h2>Weather and aerodrome information</h2>
<ul>
  <li><strong>SNOWTAM</strong> and <strong>RCR</strong>: runway conditions, cleared widths, snowbanks and the time of observation.</li>
  <li><strong>NOTAM</strong>: runway and taxiway closures for snow clearing, de-icing facility status, and lighting changes.</li>
  <li><strong>TAF and forecasts</strong>: precipitation type and timing at departure, destination and alternates.</li>
</ul>

<h2>Alternate selection</h2>
<ul>
  <li>Choose alternates that are not affected by the same weather system, where possible.</li>
  <li>Check runway length against the expected runway condition, and check that de-icing and snow clearing are available.</li>
  <li>Consider the opening hours and handling capability of the alternate in winter, and overnight parking if a return is not possible.</li>
</ul>

<h2>Winter fuel</h2>
<p>Add fuel for de-icing delays, extended taxi, a second treatment, holding, and a more distant alternate (see Lesson 22). The commander's extra fuel decision should be based on the specific threats briefed, not on habit.</p>

<h2>Stations without de-icing</h2>
<p>If an aircraft must overnight at a station without de-icing equipment, consider a hangar, covers, departure time and an alternative plan. The Dryden accident (Lesson 30) shows the danger of a station without the means to de-ice the aircraft properly.</p>
""",
takeaways=[
  "Check every MEL item for icing restrictions — winter conditions often prevent dispatch.",
  "Use SNOWTAM, RCR, NOTAM and TAF for departure, destination and alternates.",
  "Choose alternates outside the same weather system, with de-icing available.",
],
check=dict(
  q="An MEL item allows dispatch “provided the aircraft is not operated in known or forecast icing conditions”. The TAF forecasts −SN at departure. Can you dispatch?",
  options=["Yes, provided you avoid clouds", "No — forecast icing conditions exist at departure", "Yes, if the item is placarded", "Yes, at night only"],
  answer=1,
  explain="Snow with a temperature of 10 °C or below is a forecast icing condition, so the MEL condition cannot be met.",
),
),

# ---------------------------------------------------------------- 26
dict(
title="Cabin and Passenger Safety in Cold Conditions",
minutes=7,
objectives=[
  "Identify cabin and passenger hazards in winter operations.",
  "Describe the role of cabin crew in reporting contamination.",
  "Plan for an evacuation in cold conditions.",
],
body="""
<h2>Boarding and disembarking</h2>
<ul>
  <li>Steps, jet bridges and ramps can be icy. Make sure they are treated and lit, and have handrails. Remind passengers to hold on.</li>
  <li>Keep doors closed when not in use to preserve cabin heat and keep snow out.</li>
  <li>Glycol on the ramp is very slippery. Passengers walking on the apron must be kept away from de-icing areas.</li>
</ul>

<h2>During de-icing</h2>
<ul>
  <li>Inform the passengers before de-icing starts. They will hear noise, see fluid on the windows, and may smell glycol.</li>
  <li>Cabin crew must report <strong>smoke, unusual smells or fumes</strong> to the flight deck at once.</li>
  <li>Passengers should stay seated with seat belts fastened, because the aircraft may move soon after treatment.</li>
</ul>

<h2>Cabin crew as observers</h2>
<p>Cabin crew can often see the wings better than the pilots. A clear company procedure is needed so that cabin crew know:</p>
<ul>
  <li><strong>what to look for</strong> — snow building up, a dull surface, ice on leading edges;</li>
  <li><strong>how to report it</strong> — immediately, directly to the commander, even during busy phases;</li>
  <li>that their report will be welcomed and acted on.</li>
</ul>
<p>The Dryden inquiry (Lesson 30) found that cabin crew and passengers had seen snow on the wings, but this information did not reach the flight deck.</p>

<h2>Evacuation in cold conditions</h2>
<ul>
  <li>Slides inflate more slowly and may be less stable in strong wind and on icy surfaces.</li>
  <li>Overwing exits and wing surfaces may be covered with ice, snow or fluid — extremely slippery.</li>
  <li>Passengers will be outside, often without coats. Move them away from the aircraft, keep groups together and get them to shelter as soon as possible. Watch for hypothermia, especially in children and elderly passengers.</li>
  <li>Communicate with the airport emergency services about warm shelter and transport.</li>
</ul>
""",
takeaways=[
  "Treat and light steps and ramps; keep passengers away from de-icing areas.",
  "Cabin crew report fumes and any contamination they see — immediately.",
  "Cold evacuation: slower slides, icy wings, and hypothermia risk after evacuation.",
],
check=dict(
  q="A cabin crew member sees snow building up on the wing while the aircraft is holding for take-off. What should they do?",
  options=["Wait until after take-off to mention it", "Report it immediately and directly to the commander", "Tell the passengers to stay calm", "Write it in the cabin log"],
  answer=1,
  explain="Possible wing contamination before take-off is safety-critical information. It must be reported immediately and directly to the commander.",
),
),

# ---------------------------------------------------------------- 27
dict(
title="CRM and Threat and Error Management in Winter Operations",
minutes=8,
objectives=[
  "Identify typical winter threats and errors.",
  "Apply TEM countermeasures, including briefings and pre-agreed decision points.",
  "Recognise and resist plan continuation bias and commercial pressure.",
],
body="""
<h2>Typical winter threats</h2>
<ul>
  <li>Changing precipitation type and intensity; darkness and low visibility;</li>
  <li>Time pressure: slot times, passenger connections, crew duty limits, de-icing queues;</li>
  <li>Complex communication between ATC, pad control, the de-icing crew and the cabin;</li>
  <li>Unfamiliar procedures at airports that rarely have winter weather;</li>
  <li>Fatigue after early starts and long delays;</li>
  <li>Equipment issues: unserviceable APU, limited de-icing equipment.</li>
</ul>

<h2>Typical errors</h2>
<ul>
  <li>Using the wrong HOT table, fluid, concentration or start time;</li>
  <li>Not updating the HOT when conditions change;</li>
  <li>Skipping or rushing the winter-specific checklist items: anti-ice, run-ups, flaps after slush taxi, flight-control check;</li>
  <li>Using reduced thrust or wrong performance data on a contaminated runway;</li>
  <li>Assuming the de-icing crew treated an area — or assuming the flight crew is ready.</li>
</ul>

<h2>Countermeasures</h2>
<ol class="steps">
  <li><strong>Winter briefing.</strong> Weather, runway conditions, de-icing plan, HOT strategy, performance, anti-ice, taxi route and hazards.</li>
  <li><strong>Pre-agreed decision points.</strong> “If HOT expires before take-off, we return.” “If RWYCC falls below 3, we wait or divert.” Decisions made calmly before the pressure arrives are better than decisions made under it.</li>
  <li><strong>Monitoring and cross-checking.</strong> Both pilots calculate the HOT independently; the pilot monitoring tracks time and conditions.</li>
  <li><strong>Speaking up.</strong> Any crew member who sees a threat must say so clearly. Use the company's assertiveness model — for example: get attention, state the concern, propose an action, get agreement.</li>
  <li><strong>Workload management.</strong> Do the de-icing and HOT tasks at a planned moment, not during the taxi or take-off briefings.</li>
</ol>

<h2>Plan continuation bias</h2>
<p>The closer we get to completing a plan, the harder it is to change it — even when the information shows we should. In winter this appears as “just one more aircraft ahead of us, the HOT will be fine”, or “the runway was fine for the last aircraft”. Recognise it, name it, and go back to your pre-agreed decision points.</p>

<div class="callout"><span class="label">Organisational support</span><p>Domestic Airlines supports any crew decision to delay, return for de-icing or divert for safety reasons. No commercial consideration justifies taking off with a contaminated aircraft.</p></div>
""",
takeaways=[
  "Brief winter threats and agree decision points before the pressure starts.",
  "Both pilots calculate HOT; the pilot monitoring tracks time and conditions.",
  "Recognise plan continuation bias — go back to your decision points.",
],
check=dict(
  q="Which countermeasure best protects a crew from time pressure at the holding point?",
  options=["Taxiing faster", "A pre-agreed decision point, briefed before taxi, for when HOT expires", "Skipping the HOT calculation to save time", "Asking ATC for a shorter route"],
  answer=1,
  explain="Decision points agreed calmly before taxi remove the need to decide under pressure and help resist plan continuation bias.",
),
),

# ---------------------------------------------------------------- 28
dict(
title="Abnormal and Emergency Situations in Cold Weather",
minutes=9,
objectives=[
  "Recognise ice-related abnormal situations on the ground, at take-off and in flight.",
  "Apply the general principles for handling them.",
  "Prepare for a rejected take-off, a go-around and an evacuation in winter conditions.",
],
body="""
<h2>Engine ice ingestion and icing</h2>
<ul>
  <li><strong>Symptoms</strong>: high vibration, surges or stalls (bangs, EGT rise, fluctuating N1/N2), flameout.</li>
  <li><strong>Causes</strong>: ice shed from the wings or fuselage (especially with rear-mounted engines), fan ice build-up in freezing fog, inlet icing without anti-ice, ice crystal icing at high altitude.</li>
  <li><strong>Actions</strong>: fly the aircraft first. Then follow the QRH engine surge/stall, vibration or relight procedures, and use engine anti-ice as required. With a multiple-engine event, reduce thrust only as the QRH directs.</li>
</ul>

<h2>Stall and roll-off after take-off with a contaminated wing</h2>
<p>An aircraft with contaminated wings can roll or stall right after lift-off, possibly <strong>before the stall warning</strong>. Signs are an uncommanded roll, buffet, a failure to climb at the normal pitch attitude, or stick-shaker activation at a speed above normal. Apply the stall recovery as trained: reduce the angle of attack, level the wings and use thrust as required. In ground effect, keep the pitch attitude only as high as needed to stay airborne, accelerate, and climb gradually. Prevention — a clean aircraft — is the only reliable defence.</p>

<h2>Frozen or restricted flight controls</h2>
<p>If a control is restricted before take-off, do not take off. If a restriction appears in flight, use the QRH procedure for jammed controls. Avoid large forces that could cause a sudden release, and consider descending into warmer air to melt ice or frozen residue.</p>

<h2>Landing gear and brakes</h2>
<ul>
  <li>Gear that does not retract or does not indicate correctly after a slush take-off: follow the QRH. Do not cycle the gear unless the procedure allows it.</li>
  <li>Frozen brakes at the start of taxi: stop, and ask for maintenance. Do not use high thrust to break them free.</li>
  <li>Anti-skid or brake failures on contaminated runways greatly increase the landing distance. Recalculate with the failure, and divert if necessary.</li>
</ul>

<h2>Rejected take-off and go-around</h2>
<ul>
  <li>Brief the RTO for the contaminated runway — lower V1, directional control in a crosswind with reverse thrust.</li>
  <li>For a go-around after ice accretion, use the AFM speeds and configurations, and expect reduced climb performance.</li>
</ul>

<h2>Evacuation in winter</h2>
<p>Assess whether an evacuation is really needed, or whether a precautionary disembarkation is safer. If an evacuation is needed, consider the wind direction, slippery surfaces and the slide stability. Arrange shelter and transport with the emergency services as soon as possible (Lesson 26).</p>
""",
takeaways=[
  "Ice ingestion: vibration, surge, EGT rise — fly the aircraft, then follow the QRH.",
  "A contaminated wing can stall before the warning — prevention is the only real defence.",
  "Never take off with restricted controls; never use high thrust on frozen brakes.",
],
check=dict(
  q="Immediately after lift-off, the aircraft rolls unexpectedly and buffets at a normal speed after de-icing in snow. What is the most likely cause?",
  options=["A thrust reverser problem", "Wing contamination reducing lift and causing an early stall", "Too much fuel in the centre tank", "Engine anti-ice left on"],
  answer=1,
  explain="Uncommanded roll and buffet just after lift-off, in conditions where contamination is possible, strongly suggest a contaminated wing stalling early and asymmetrically.",
),
),

# ---------------------------------------------------------------- 29
dict(
title="Regulations, Standards and Safety Management",
minutes=8,
objectives=[
  "Identify the main international regulations and standards for cold weather operations.",
  "Describe the elements of a ground de-icing/anti-icing programme.",
  "Use the safety management system to report winter hazards.",
],
body="""
<h2>International framework</h2>
<div class="table-wrap"><table>
  <tr><th>Source</th><th>Content</th></tr>
  <tr><td>ICAO Annex 6, Part I</td><td>Operator responsibilities, including the requirement that an aircraft is not to take off unless it has been inspected for icing and, if necessary, de-iced and anti-iced.</td></tr>
  <tr><td>ICAO Doc 9640</td><td>Manual of Aircraft Ground De-icing/Anti-icing Operations.</td></tr>
  <tr><td>ICAO Annex 14 and PANS-Aerodromes (Doc 9981)</td><td>Global Reporting Format for runway surface conditions.</td></tr>
  <tr><td>ICAO Doc 10064</td><td>Aeroplane Performance Manual, including contaminated runway performance.</td></tr>
  <tr><td>EASA Air Operations</td><td>CAT.OP.MPA.250 (ice and other contaminants — ground procedures) and CAT.OP.MPA.255 (in-flight procedures).</td></tr>
  <tr><td>FAA</td><td>14 CFR 121.629 (Clean Aircraft Concept and de-icing programme) and AC 120-60 (ground de-icing/anti-icing programme).</td></tr>
  <tr><td>Transport Canada / FAA</td><td>Holdover time guidelines, published every winter season.</td></tr>
  <tr><td>SAE International</td><td>AS6285 (de-icing/anti-icing processes), AS6286 (training and qualification), AMS1424 and AMS1428 (fluid specifications).</td></tr>
</table></div>
<p>National regulations from the civil aviation authority, the aircraft AFM, and the Domestic Airlines Operations Manual implement these standards for our operation. They are the documents you must follow.</p>

<h2>The ground de-icing/anti-icing programme</h2>
<p>Operators must have an approved programme that typically includes:</p>
<ul>
  <li>responsibilities of the operator, the commander and the service providers;</li>
  <li>the procedures for inspection, treatment, communication and the anti-icing code;</li>
  <li>the holdover time guidelines to be used, and how to use them;</li>
  <li>initial and recurrent training for flight crew, cabin crew, dispatchers and ground staff;</li>
  <li>quality control of fluids, equipment and service providers;</li>
  <li>the pre-take-off check and pre-take-off contamination check procedures.</li>
</ul>

<h2>Safety management and reporting</h2>
<p>Winter operations produce many precursors to accidents. Report them through the company safety reporting system:</p>
<ul>
  <li>contamination found after de-icing, or a take-off with suspected contamination;</li>
  <li>communication errors with de-icing crews or ATC;</li>
  <li>fluid smells or smoke in the cabin;</li>
  <li>braking action worse than reported, and runway excursions or near-excursions;</li>
  <li>control stiffness or restriction, and residue findings;</li>
  <li>holdover times exceeded, or pressure to depart.</li>
</ul>
<p>Domestic Airlines operates a <strong>just culture</strong>: honest reports of errors and hazards are used to learn and to improve the system, not to blame individuals.</p>
""",
takeaways=[
  "ICAO, EASA, FAA, Transport Canada and SAE set the international framework; national rules, the AFM and the Operations Manual apply it.",
  "Operators need an approved ground de-icing/anti-icing programme with training and quality control.",
  "Report winter hazards and errors — just culture protects honest reporting.",
],
check=dict(
  q="Which organisation publishes the holdover time guidelines used worldwide each winter?",
  options=["IATA and ICAO", "The FAA and Transport Canada", "Each airport authority", "The aircraft manufacturer only"],
  answer=1,
  explain="Holdover time guidelines are published each season by the FAA and Transport Canada and are adopted by operators worldwide.",
),
),

# ---------------------------------------------------------------- 30
dict(
title="Lessons from Accidents and Course Review",
minutes=10,
objectives=[
  "Describe key cold weather accidents and their causal factors.",
  "Link each accident to the defences covered in this course.",
  "Review the essential principles before the final quiz.",
],
body="""
<h2>Accident case studies</h2>
<div class="table-wrap"><table>
  <tr><th>Accident</th><th>What happened</th><th>Lesson for us</th></tr>
  <tr><td><strong>Air Florida 90</strong><br>B737-200, Washington DC, January 1982</td><td>The engine anti-ice was off; iced engine pressure probes gave false high thrust indications, so the actual thrust was too low. Snow and ice were on the wings after a long wait following de-icing. The crew continued the take-off despite abnormal indications. The aircraft struck a bridge and fell into the Potomac River; 78 people died.</td><td>Use engine anti-ice when required. Cross-check thrust with all parameters. Respect the holdover time. Act on abnormal take-off indications.</td></tr>
  <tr><td><strong>Air Ontario 1363</strong><br>Fokker F28, Dryden, Canada, March 1989</td><td>The aircraft took off in snow without de-icing. The APU was unserviceable, there was no ground start, and the engines could not be shut down. Snow was seen on the wings by cabin crew and passengers, but this was not reported to the flight deck. 24 people died. The inquiry highlighted organisational pressures and the Clean Aircraft Concept.</td><td>Never take off contaminated. Check MEL implications in winter. Cabin crew must report contamination. Organisational support for safe decisions.</td></tr>
  <tr><td><strong>SAS 751</strong><br>MD-81, Gottröra, Sweden, December 1991</td><td>Clear ice formed overnight on the wings from cold-soaked fuel and was not removed. It broke off at take-off and was ingested by both rear-mounted engines, which surged and failed. The crew made a forced landing in a field. Everyone survived.</td><td>Clear ice is hard to see — use the tactile check. Rear-mounted engines are at particular risk.</td></tr>
  <tr><td><strong>USAir 405</strong><br>Fokker F28, New York LaGuardia, March 1992</td><td>The aircraft was de-iced, then waited about 35 minutes in snow before take-off. Ice built up on the wings; the aircraft stalled just after lift-off and crashed into the water. 27 people died.</td><td>Holdover time is limited and is an estimate. Inspect before take-off. Return for re-treatment when in doubt.</td></tr>
  <tr><td><strong>American Eagle 4184</strong><br>ATR 72, Roselawn, USA, October 1994</td><td>While holding in freezing drizzle (SLD), a ridge of ice formed behind the de-icing boots. It disturbed the airflow over the ailerons, causing a sudden roll upset. 68 people died.</td><td>Recognise SLD and leave icing conditions immediately. Know the autopilot limitations in icing.</td></tr>
  <tr><td><strong>Southwest 1248</strong><br>B737-700, Chicago Midway, December 2005</td><td>The aircraft landed in snow on a contaminated runway with a tailwind. Reverse thrust was deployed late, and the landing distance assessment relied on optimistic assumptions. The aircraft overran into a road; a child in a car died.</td><td>Calculate landing distance at the time of arrival with an adequate margin. Deploy reverse thrust promptly.</td></tr>
</table></div>

<h2>The essential principles</h2>
<ol class="steps">
  <li><strong>Clean aircraft.</strong> No frost, ice, snow or slush on critical surfaces at take-off, unless the AFM explicitly permits it.</li>
  <li><strong>Holdover time is an estimate.</strong> It starts at the beginning of the final application. Reassess when conditions change. If it is exceeded: a PTCC within 5 minutes of take-off, or re-treat. Allowance times cannot be extended.</li>
  <li><strong>Check, do not assume.</strong> Use tactile checks for clear ice, the post-treatment check, the pre-take-off checks, and the full and free control check.</li>
  <li><strong>Communicate in closed loop</strong> with the de-icing crew, ATC and the cabin. Read back the anti-icing code.</li>
  <li><strong>Use the right performance data.</strong> RWYCC, contaminated runway data, no reduced thrust, and the landing distance at time of arrival with a margin.</li>
  <li><strong>Protect the systems.</strong> Anti-ice when icing conditions exist, run-ups in freezing fog, cold-soak precautions, fuel temperature limits.</li>
  <li><strong>Correct for cold.</strong> Apply altimeter corrections to minimum altitudes and respect baro-VNAV temperature limits.</li>
  <li><strong>Decide early.</strong> Brief winter threats, agree decision points, and resist pressure. Returning for de-icing is always the right choice when in doubt.</li>
</ol>

<h2>Next steps</h2>
<p>You have now completed all the lessons. Take the <strong>final quiz</strong>: 20 questions drawn at random, with a pass mark of 80 %. After passing, you can print your certificate and watch the closing video.</p>
""",
takeaways=[
  "Most winter accidents combined contamination with time pressure and missed warnings.",
  "Every defence in this course exists because of a real accident.",
  "When in doubt: inspect, re-treat, recalculate — or do not go.",
],
check=dict(
  q="Which accident is most closely associated with clear ice from cold-soaked fuel being ingested by rear-mounted engines?",
  options=["Air Florida 90", "SAS 751", "Southwest 1248", "American Eagle 4184"],
  answer=1,
  explain="SAS 751 (MD-81, 1991): clear ice on the wings from cold-soaked fuel broke off at take-off and was ingested by both rear-mounted engines.",
),
),
]
