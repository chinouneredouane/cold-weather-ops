"""Low Visibility Operations (LVO) — CAT II, LVTO and LV taxi, Boeing 737-800.

Built from the documents provided by the training department:
- All Weather Operation Procedures B737-800 (AWOP), Ed.01 Rev.00, 05/01/2017 — company procedures and minima;
- Low Visibility Operation Procedures Guide B737-800 (LVO_TAL), first edition 05/01/2017 — same company content;
- Low Visibility Procedures, Boeing 737NG Manual, Ed.01 (Nov 2021), two versions — used ONLY for general
  aerodrome, lighting and B737NG autoland / go-around system knowledge (its minima belong to another operator);
- ICAO NACC presentation "Flight Operations in Low Visibility Conditions" (2016) — visual references, human factors,
  photos and diagrams (credited ICAO / KLM in the presentation).
References in the company documents: DACM Instruction No 1148 (operating minima), ICAO Doc 9365, EASA AWO.
"""

IMG = "../media/images/"


def fig(name, caption, alt, maxw=None):
    lim = f"max-width:{maxw}px;margin:0 auto;" if maxw else ""
    return (f'<figure class="diagram"><img src="{IMG}{name}.jpg" alt="{alt}" loading="lazy" '
            f'style="{lim}width:100%;height:auto;display:block"><figcaption>{caption}</figcaption></figure>')


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


COMPANY = """<div class="table-wrap"><table>
<tr><th>Domestic Airlines — B737-800 LVO authorisation (company AWO procedures)</th><th></th></tr>
<tr><td>Approach</td><td><strong>CAT II only</strong> — DH <strong>100 ft</strong>, TDZ RVR <strong>350 m</strong>, MID RVR 175 m; <strong>autoland mandatory</strong></td></tr>
<tr><td>Low visibility take-off</td><td>Minimum RVR <strong>175 m</strong> — TDZ and MID RVR required</td></tr>
<tr><td>Pilot flying</td><td>The <strong>captain (left seat)</strong> is PF in all phases of LVO</td></tr>
<tr><td>Fleet</td><td>B737-800 only. Dash 8-Q400 and Q200: no LVO authorisation (CAT I operations)</td></tr>
</table></div>
<p class="muted">The company documents also state that the B737NG fleet is certified for CAT IIIA; the company authorisation is CAT II. Always check the current AOC operations specifications and the OM A.</p>"""

LESSONS = [
dict(title="LVO Concept, Categories and Requirements", minutes=8,
objectives=["Define all weather operations (AWO), LVO and LVP.", "State the ICAO approach categories and the company CAT II minima.", "List the four conditions required before any LVO."],
body="""
<h2>All weather operations</h2>
<p><strong>All weather operations (AWO)</strong> means operating an aircraft in low visibility conditions. It includes low visibility take-off (LVTO), lower than standard CAT I, other than standard CAT II, standard CAT II and CAT III. The aim is to keep traffic regular in low visibility <strong>with a level of safety equivalent to normal operations</strong>.</p>
<p><strong>Low visibility operations (LVO)</strong> consist of three phases:</p>
<ul><li>low visibility <strong>taxi</strong>;</li><li>low visibility <strong>take-off</strong> (LVTO);</li><li>low visibility <strong>approach and landing</strong>.</li></ul>
<p><strong>Low visibility procedures (LVP)</strong> are the procedures applied at an aerodrome to protect these operations: protection of the runway against incursion and of the accuracy and integrity of the ILS signals. LVP are established for departures with RVR below 550 m, for CAT II and III approaches, and when weather prevents full visual observation of the manoeuvring area.</p>
""" + fig("fig-lvp-relationship", "Relationship between meteorological conditions, aerodrome LVP phases and the pilot's operations (from the B737NG low visibility procedures manual).", "Chart relating RVR and cloud base, LVP phases and approach categories", 520) + """
<h2>Approach categories (ICAO)</h2>
<div class="table-wrap"><table>
<tr><th>Category</th><th>Decision height</th><th>RVR</th></tr>
<tr><td class="code">I</td><td>Not lower than 200 ft</td><td>Visibility ≥ 800 m or RVR ≥ 550 m</td></tr>
<tr><td class="code">II</td><td>Lower than 200 ft, not lower than 100 ft</td><td>RVR ≥ 300 m (ICAO)</td></tr>
<tr><td class="code">III</td><td>Lower than 100 ft, or no DH</td><td>RVR below 300 m, or no RVR limitation</td></tr>
</table></div>
<p>ICAO and EASA now group the former CAT IIIA, IIIB and IIIC as <strong>CAT III</strong>. When the DH and the RVR fall in different categories, the operation is conducted in the most demanding category. The company definition of CAT II also specifies the RVR at the measuring points: <strong>RVR A</strong> (threshold / touchdown zone), <strong>RVR B</strong> (mid-point) and <strong>RVR C</strong> (roll-out end).</p>

<h2>Company authorisation</h2>
""" + COMPANY + """
<h2>Four conditions before any LVO</h2>
<ol class="steps">
  <li><strong>Operator</strong> — authorised by the Authority (DACM) for the operation.</li>
  <li><strong>Crew</strong> — trained, checked and current for LVO. Both pilots must be qualified.</li>
  <li><strong>Aircraft</strong> — certified for the operation (CAT II autoland) with the required equipment serviceable.</li>
  <li><strong>Aerodrome</strong> — LVP declared <strong>in force</strong>, with the required ground equipment serviceable.</li>
</ol>
<div class="callout"><span class="label">Company notes</span><p>LVO in operation may be announced by ATIS, GND or TWR when RVR is below <strong>800 m</strong>; LVTO procedures must be in operation when RVR is below <strong>400 m</strong>. When LVO is in operation and the RVR is above CAT I minimums, <strong>non-qualified crews</strong> are not authorised to conduct low visibility taxi, take-off or approach.</p></div>
""",
takeaways=["LVO = LV taxi + LVTO + LV approach; LVP protect the runway and the ILS.", "CAT I: DH 200 ft, RVR 550 m; CAT II: DH 100–200 ft; CAT III: below 100 ft or no DH.", "Company B737-800: CAT II only — DH 100 ft, TDZ RVR 350 m, autoland mandatory; LVTO 175 m; captain PF.", "Operator, crew, aircraft and aerodrome must all be qualified."],
check=dict(q="Which four elements must all be qualified before any LVO?", options=["Aircraft, fuel, weather, ATC", "Operator approval, crew qualification, aircraft certification and aerodrome LVP in force", "Captain, first officer, dispatcher and cabin crew", "Only the aircraft and the runway"], answer=1,
           explain="The operator must be authorised, the crew qualified and current, the aircraft certified and serviceable, and the aerodrome must have LVP in force."),
),

dict(title="Seeing in Low Visibility: Visual References and Human Factors", minutes=7,
objectives=["Explain why the visual phase is so short in CAT II.", "Define RVR, slant visual range, visual segment and cockpit cut-off angle.", "State the visual reference required at DH."],
body="""
<h2>A short visual phase</h2>
<p>In low visibility the <strong>instrument phase</strong> of the approach becomes longer and the <strong>visual phase</strong> shorter. At a CAT II DH of 100 ft, the runway is <strong>less than 5 seconds away</strong>. In CAT III, pilots may see the runway lights only about 5 seconds before touchdown — there is no margin for error.</p>
<ul>
  <li>The average time for a pilot to switch from outside cues to the instruments and back is about <strong>2.5 seconds</strong> — during which a jet travels about 150 m.</li>
  <li>The fovea of the eye is only about 1.5° wide: the lighting patterns must emphasise the centreline.</li>
  <li>Visual workload is manageable when the situation unfolds as expected — but capacity breaks down with ambiguous or transitory cues. Standardisation of lighting and procedures is essential.</li>
</ul>

<h2>Definitions</h2>
<ul>
  <li><strong>RVR</strong> — the range over which the pilot on the runway centreline can see the runway surface markings or the lights delineating the runway or its centreline.</li>
  <li><strong>Slant visual range (SVR)</strong> — the distance between the pilot's eye and the farthest light the pilot can see.</li>
  <li><strong>Visual segment</strong> — the length of approach and runway lighting in view at any one moment.</li>
  <li><strong>Cockpit cut-off angle</strong> — the angle below which the ground is hidden by the nose: around 11°–15° depending on the aircraft. On the B737NG the ground is hidden for about <strong>12 m</strong> ahead of the pilot during taxi.</li>
</ul>
""" + fig("fig-visual-segment", "Variation of the visual segment with height in homogeneous fog: from 200 ft the approach lights are exposed for about 15 seconds; from 100 ft for only about 3 seconds (ICAO presentation).", "Diagram of the visual segment and obscured segment at different heights") + """
<p>From 200 ft to the point where the threshold lights disappear under the nose takes about 10–12 seconds; at 100 ft the exposure time is 3–5 seconds. A rough guide for the minimum acceptable visual segment is about <strong>150 m (5 lights)</strong> ahead of the aircraft.</p>

<h2>Required visual reference at DH (CAT II)</h2>
<div class="callout warn"><span class="label">Company rule</span>
<p>A CAT II approach may not be continued below DH unless a visual reference of <strong>at least a 3-light segment</strong> of the approach light centreline, the touchdown zone lights, the runway centreline lights or the runway edge lights — or a combination of these — is attained <strong>and can be maintained</strong>.</p></div>
""" + fig("fig-fog-sequence", "Approach and runway lighting seen on approach in different visibility conditions (ICAO presentation, source KLM).", "Four approach views of runway lighting") ,
takeaways=["At CAT II DH the runway is less than 5 seconds away.", "Visual segment, SVR and cockpit cut-off angle decide what the pilot can see.", "Below DH only with at least a 3-light segment, attained and maintained."],
check=dict(q="What visual reference is required to continue a CAT II approach below DH?", options=["The whole runway", "At least a 3-light segment of approach, TDZ, centreline or edge lights, attained and maintained", "Any single light", "The PAPI only"], answer=1, explain="At least a 3-light segment of the specified lights, attained and maintained."),
),

dict(title="The Aerodrome: Lighting, Signs and LVP", minutes=8,
objectives=["Recognise the runway and taxiway lighting used in LVO.", "Identify stop bars, CAT II/III holding positions and RETILs.", "Explain the ILS critical and sensitive areas."],
body="""
<h2>Approach and runway lighting</h2>
""" + fig("fig-cat1-lights", "CAT I approach and runway lighting (ICAO presentation).", "CAT I approach lighting at dusk", 640) + """
<ul>
  <li><strong>Runway edge lights</strong> — white; on ILS runways without centreline lights, the last 600 m (or last third) may be <strong>yellow</strong> (caution zone). Runway end lights are red.</li>
  <li><strong>Runway centreline lights</strong> — white; colour-coded <strong>alternating red and white from 900 m</strong> before the runway end, and <strong>all red for the last 300 m</strong>.</li>
  <li><strong>Touchdown zone lights</strong> — required on runways used in low visibility; from the threshold for 900 m or to the mid-point, whichever is less.</li>
  <li><strong>Taxiway centreline lights</strong> — green; blue edge lights on minor taxiways and aprons. Green lead-off lights may guide to an exit; lead-on lights are lit only with a clearance.</li>
</ul>

<h2>Stop bars and holding positions</h2>
""" + fig("fig-stopbar", "A lit red stop bar across a taxiway.", "Red stop bar lights across a taxiway", 360) + """
<div class="callout warn"><span class="label">Never</span><p><strong>Never cross a lighted red stop bar — even if cleared by ATC.</strong> Stop and ask.</p></div>
""" + fig("fig-holding-signs", "Runway-holding positions: CAT II/III holding positions (A2) are further from the runway than CAT I / visual ones (A1), to protect the ILS signal.", "Taxiway with A1 and A2 CAT II/III holding position signs", 420) + """
<ul>
  <li>CAT II/III runway-holding positions are set <strong>farther back</strong> from the runway than CAT I positions, to keep aircraft out of the ILS critical and sensitive areas.</li>
  <li>A <strong>surface movement guidance and control system (SMGCS)</strong> may switch taxiway centreline sections and stop bars to guide aircraft along their cleared route.</li>
</ul>

<h2>Rapid exit taxiway indicator lights</h2>
""" + fig("fig-retils", "RETILs: yellow lights in a 3-2-1 pattern, 100 m apart, the single light 100 m before the turn-off.", "Diagram of rapid exit taxiway indicator lights", 560) + """
<h2>ILS protection</h2>
<ul>
  <li><strong>ILS critical area</strong> — around the localiser and glide path antennas; vehicles and aircraft are excluded during ILS operations.</li>
  <li><strong>ILS sensitive area</strong> — beyond the critical area; movement is controlled to prevent interference.</li>
  <li><strong>Obstacle free zone (OFZ)</strong> — kept clear of all obstacles above the inner runway strip.</li>
</ul>
<p>With LVP in force, ATC increases spacing so that a landing aircraft is not disturbed by an aircraft in the sensitive area.</p>
""",
takeaways=["Centreline lights: red/white from 900 m to go, all red last 300 m.", "TDZ lights: required for LVO runways; edge lights may be yellow in the last 600 m.", "Never cross a lit red stop bar; CAT II/III holding positions are farther back.", "ILS critical and sensitive areas protect the signal — LVP increase spacing."],
check=dict(q="ATC clears you to cross a runway, but the stop bar in front of you is still lit red. What do you do?", options=["Cross — the clearance is valid", "Stop and ask ATC; never cross a lit red stop bar", "Cross slowly", "Flash the landing lights and cross"], answer=1, explain="A lit red stop bar must never be crossed, even with a clearance."),
),

dict(title="Planning and Low Visibility Taxi", minutes=7,
objectives=["Prepare a flight with low visibility at departure or destination.", "Select take-off and destination alternates.", "Apply the company low visibility taxi procedures."],
body="""
<h2>Pre-flight planning</h2>
<ul>
  <li><strong>Both pilots</strong> qualified and current for LVO.</li>
  <li><strong>NOTAMs</strong> reviewed — runway lighting, RVR equipment, ILS status.</li>
  <li><strong>LVP in force</strong> at the aerodrome (ATIS or RTF).</li>
  <li><strong>Technical log and MEL</strong> — defects that may affect LVO capability (see the required equipment list, Lesson 6).</li>
  <li><strong>Weather</strong> within company, crew and aerodrome minima.</li>
  <li><strong>Fuel</strong> — extra fuel for possible delays.</li>
  <li><strong>Alternates</strong> — take-off and destination alternates within minima.</li>
</ul>

<h2>Alternates</h2>
<ul>
  <li><strong>Take-off alternate</strong> — required when the weather at departure is below the landing minima, or a return is not possible. For a twin, within <strong>one hour</strong> at the one-engine-inoperative cruise speed (still air, actual take-off mass). The weather from one hour before to one hour after the ETA must be at or above the applicable minima (at least CAT I for one engine inoperative).</li>
  <li><strong>Destination alternate</strong> — the weather from one hour before to one hour after the ETA must be at or above the planning minima in the OM A.</li>
</ul>

<h2>Low visibility taxi (company procedure)</h2>
<ol class="steps">
  <li>Brief the <strong>taxi routing</strong>, runway crossings, <strong>stop bars</strong>, hot spots, sensitive areas and special local procedures — using the low visibility taxi chart if available.</li>
  <li>Complete <strong>checklists, set-ups, briefings and paperwork with the aircraft stopped</strong> — before taxi or at the CAT II holding point.</li>
  <li>Taxi at a <strong>maximum of 10 kt</strong>. The <strong>captain</strong> taxis.</li>
  <li><strong>Both pilots</strong> keep a maximum lookout and stay aware of other traffic; sterile flight deck.</li>
  <li>Make sure every ATC clearance is understood and acknowledged; ask in case of doubt.</li>
  <li>If unsure of your position: <strong>stop immediately</strong> and ask ATC — request a <strong>follow-me</strong> vehicle or progressive taxi.</li>
</ol>
<div class="callout warn"><span class="label">Remember</span><p>There is no minimum visibility for taxi, but the commander remains responsible for clearance from other aircraft, vehicles and obstacles. At many aerodromes ATC cannot see you. From the B737NG flight deck, the ground is hidden for about 12 m ahead.</p></div>
""",
takeaways=["Plan: both pilots qualified, NOTAMs, LVP in force, MEL, minima, fuel, alternates.", "Take-off alternate within 1 hour OEI when below landing minima at departure.", "LV taxi: brief, paperwork stopped, max 10 kt, captain taxis, stop if unsure, never cross a red stop bar."],
check=dict(q="What is the maximum taxi speed in low visibility according to the company procedure?", options=["5 kt", "10 kt", "20 kt", "30 kt"], answer=1, explain="Maximum 10 kt."),
),

dict(title="Low Visibility Take-off (LVTO)", minutes=6,
objectives=["Apply the company LVTO minima and RVR requirements.", "Use pilot assessment correctly.", "Prepare the take-off in low visibility."],
body="""
<h2>Company LVTO minima (B737-800)</h2>
<ul>
  <li>The company is approved for LVTO with a minimum <strong>RVR of 175 m</strong>.</li>
  <li><strong>TDZ and MID RVR are required.</strong></li>
  <li>When not reported, the TDZ RVR may be determined by <strong>pilot assessment</strong>.</li>
  <li>When the TDZ RVR is measured, pilot assessment is possible <strong>only when the reported RVR is above 150 m</strong>.</li>
  <li>LVTO procedures must be in operation when the RVR is below <strong>400 m</strong>; any take-off with RVR below 400 m is an LVTO.</li>
</ul>
<div class="callout info"><span class="label">General rules (OM A / EASA)</span>
<ul><li>The RVR / visibility conversion table is <strong>not</strong> used for take-off minima.</li>
<li>The required RVR must be achieved at <strong>all relevant reporting points</strong> — the lowest relevant value decides.</li>
<li>Take-off minima also depend on the runway lighting (edge and centreline lights) and the RVR equipment — check the aerodrome take-off minima on the chart (e.g. Jeppesen 10-9).</li></ul></div>

<h2>Before take-off</h2>
<ul>
  <li><strong>Captain only</strong> take-off in LVO.</li>
  <li>Check the take-off alternate.</li>
  <li>Tune the ILS for localiser reference where available, and verify the aircraft heading matches the runway heading.</li>
  <li>Line up on the centreline and set take-off thrust only when aligned — a rolling take-off during alignment is not recommended.</li>
  <li>Brief the rejected take-off: directional control on the centreline lights, and the RVR along the runway.</li>
</ul>
""",
takeaways=["Company LVTO: RVR 175 m minimum, TDZ and MID RVR required.", "Pilot assessment of TDZ RVR when not reported, or when the reported RVR is above 150 m.", "Captain only take-off; align before applying thrust; brief the reject."],
check=dict(q="What is the company minimum RVR for a low visibility take-off on the B737-800?", options=["125 m", "175 m", "300 m", "400 m"], answer=1, explain="The company LVTO minimum is RVR 175 m with TDZ and MID RVR required."),
),

dict(title="CAT II Approach and Autoland", minutes=10,
objectives=["Check the landing requirements and required airborne equipment.", "Set up and brief the CAT II approach.", "Fly the CAT II autoland with the company callouts."],
body="""
<h2>Landing requirements (company)</h2>
<div class="table-wrap"><table>
<tr><th>Item</th><th>CAT I</th><th>CAT II</th></tr>
<tr><td>Autopilot</td><td>1 A/P</td><td><strong>Autoland</strong></td></tr>
<tr><td>Minimum DH (use Jeppesen if higher)</td><td>200 ft</td><td><strong>100 ft</strong></td></tr>
<tr><td>TDZ RVR (use Jeppesen if higher)</td><td>550 m</td><td><strong>350 m</strong></td></tr>
<tr><td>MID RVR (independent of Jeppesen)</td><td>—</td><td><strong>175 m</strong></td></tr>
<tr><td>Roll-out RVR</td><td>—</td><td>Required if reported (may be replaced by MID RVR if not reported)</td></tr>
<tr><td>Ground equipment</td><td colspan="2">See the table of failed or downgraded ground equipment (OM A)</td></tr>
<tr><td>Braking action</td><td colspan="2">Medium or better (µ > 0.3)</td></tr>
<tr><td>Runway length</td><td colspan="2">Landing distance + 15 % (advisory data, braking good or medium)</td></tr>
<tr><td>Weather</td><td colspan="2">No heavy precipitation; maximum headwind 25 kt, crosswind 20 kt, tailwind 10 kt</td></tr>
</table></div>

<h2>Required airborne equipment (CAT II)</h2>
<p>All engines; flaps 30 or 40 (<strong>flaps 40 recommended</strong>); hydraulic systems A and B; auto speedbrakes; antiskid; both EFIS control panels; two generators on the buses; <strong>both A/Ps engaged in APP mode</strong>, with disengage switches, lights and aural warning; FD bars on both PFDs; both TO/GA switches; two ADIRUs in NAV mode; both ILS receivers with valid indications and one means to check glideslope validity (OM, DME or equivalent); both DEUs (no source transfer); standby horizon; displays, altitude and FMA on both PFDs; radio altimeter and DH on both PFDs; windshield wipers in precipitation. If any item is missing, check the full table and the MEL — the capability may be downgraded.</p>

<h2>Set-up</h2>
<ul>
  <li><strong>BARO</strong> minimums: for CAT II, set <strong>threshold elevation + 500 ft</strong> (for CAT I, set the DA).</li>
  <li><strong>RADIO</strong> minimums: set the CAT II DH (100 ft) and keep the selector on RADIO.</li>
  <li>Brief crew and aircraft status, weather, NOTAMs, fuel for destination and alternate, the approach, the go-around and the failure responses.</li>
  <li>Approach ban: do not continue beyond the outer marker or equivalent (or 1,000 ft above the aerodrome) unless the reported controlling RVR is at or above the minima.</li>
</ul>

<h2>B737NG autoland sequence</h2>
<ul>
  <li>Both VHF NAV receivers tuned to the ILS; APP mode armed; the second A/P engaged in CMD — it must be engaged by <strong>800 ft RA</strong>.</li>
  <li>Below <strong>1,500 ft RA</strong> after LOC and G/S capture: the second A/P couples, the ILS deviation monitor is tested, <strong>FLARE armed</strong> is annunciated and A/P go-around arms.</li>
  <li>At <strong>400 ft RA</strong> the stabiliser is trimmed further nose-up — if the A/Ps then disengage, forward control column force may be needed. If FLARE is not armed by about 350 ft RA, both A/Ps disengage; <strong>no FLARE armed at 500 ft: go around</strong>.</li>
  <li>About <strong>50 ft RA</strong>: FLARE engaged; at about <strong>27 ft</strong>: RETARD; the A/T disengages about 2 seconds after touchdown; the <strong>A/P is disengaged manually</strong> after touchdown and the roll-out is flown manually.</li>
</ul>

<h2>Company procedure and callouts</h2>
<div class="table-wrap"><table>
<tr><th>Phase</th><th>PF (captain)</th><th>PM</th></tr>
<tr><td>Cleared for approach</td><td>ILS NAV 1, APP mode</td><td>“CHECKED”</td></tr>
<tr><td>LOC alive / captured</td><td>“CHECKED”; ILS NAV 2, A/P B in CMD</td><td>“LOC ALIVE”; “CHECKED”</td></tr>
<tr><td>GS alive</td><td>“CHECKED”</td><td>“GS ALIVE”</td></tr>
<tr><td>OM or FAF</td><td>“CHECKED”</td><td>“OM / FIX … FT”</td></tr>
<tr><td>500 ft above threshold</td><td>“CHECKED”</td><td>“STABLE, 500, FLARE ARMED” — then FMA callouts</td></tr>
<tr><td>100 ft above minimum</td><td>“CHECKED”</td><td>“APPROACHING MINIMUM” (if no automatic callout)</td></tr>
<tr><td>Minimum</td><td>“CONTINUE” or “GO-AROUND”</td><td>“MINIMUMS”</td></tr>
<tr><td>50 ft</td><td>Disconnect A/P if no FLARE green, and land manually</td><td>“FLARE” or “NO FLARE”</td></tr>
<tr><td>27 ft</td><td></td><td>“RETARD”</td></tr>
<tr><td>Touchdown</td><td>Disconnect A/P; extend speedbrakes manually if not up; maximum reverse</td><td>“SPEEDBRAKES UP” or “NOT UP”; “REVERSERS NORMAL” or “NO REVERSE ENG 1/2”</td></tr>
<tr><td>Roll-out</td><td>Manual braking; disarm autobrakes</td><td>Monitor deceleration; “AUTOBRAKES DISARM”</td></tr>
</table></div>
<h3>Deviation callouts (PM)</h3>
<p>“SPEED” (IAS +10 / −5 kt) · “SINK RATE” (more than 1,000 ft/min) · “PITCH” (excessive pitch change) · “BANK” (more than 7°) · “LOCALIZER” (more than ¼ dot) · “GLIDESLOPE” (more than ½ dot). <strong>FMA callouts are mandatory during LVO.</strong></p>

<h2>Loss of visual reference</h2>
<ul>
  <li><strong>Before touchdown</strong>: if the required visual reference is lost below DH, <strong>go around immediately</strong> — even if the aircraft touches down during the go-around, continue it.</li>
  <li><strong>After touchdown</strong>: if the visual reference is lost, <strong>do not attempt a go-around</strong>.</li>
</ul>
""",
takeaways=["CAT II: DH 100 ft, TDZ RVR 350 m, MID 175 m, autoland, braking medium or better, winds 25/20/10.", "BARO = threshold + 500 ft; RADIO = DH 100 ft.", "Second A/P by 800 ft RA; FLARE armed by 500 ft or go around; FLARE 50 ft, RETARD 27 ft; disconnect A/P after touchdown.", "FMA callouts mandatory; go around if reference is lost before touchdown, never after."],
check=dict(q="During a CAT II autoland, FLARE is not armed at 500 ft. What do you do?", options=["Continue and land manually", "Go around", "Engage the second A/P", "Continue to DH and decide"], answer=1, explain="No FLARE armed at 500 ft: go around (there is no automatic go-around capability without FLARE armed)."),
),

dict(title="Failures, Contingencies and Go-around", minutes=8,
objectives=["Respond to AFDS failures above and below 800 ft RA.", "Handle engine failure, fire and incapacitation on a CAT II approach.", "Fly the CAT II go-around."],
body="""
<h2>General rule</h2>
<p>In case of failure of any system, instrument or AFDS element affecting CAT II, apply the QRH. <strong>All non-normal checklists must be completed by 1,000 ft above the aerodrome</strong>; otherwise go around and reassess the capability with the required equipment table.</p>

<h2>AFDS failures (company)</h2>
<div class="table-wrap"><table>
<tr><th>Failure</th><th>Above 800 ft RA</th><th>At or below 800 ft RA</th><th>During go-around</th></tr>
<tr><td>Flashing red A/P disengage light and horn</td><td>Re-engage A/P</td><td>Execute manual go-around (a)</td><td>Execute manual go-around</td></tr>
<tr><td>Steady red A/P disengage light (stabiliser out of trim)</td><td>Not applicable</td><td>Disengage A/P and execute manual go-around (a)</td><td>Not applicable</td></tr>
<tr><td>Flashing red A/T disengage light</td><td colspan="3">Continue with manual thrust</td></tr>
<tr><td>No FLARE armed annunciation</td><td>Engage second A/P</td><td>Disengage A/P and execute manual go-around (a)</td><td>Not applicable</td></tr>
<tr><td>Warning / caution lights</td><td colspan="2">Apply the QRH — NNCs completed by 1,000 ft AAL</td><td>Apply the QRH</td></tr>
<tr><td>ILS deviation alert</td><td colspan="2">Go-around (a)</td><td>Not applicable</td></tr>
</table></div>
<p class="muted">(a) If suitable visual reference is established, perform a manual landing.</p>

<h2>Engine failure, fire, incapacitation (company)</h2>
<ul>
  <li><strong>Engine failure</strong> during a CAT II approach: disconnect A/P and A/T and execute a <strong>manual go-around</strong>, or a manual landing if suitable visual reference is established.</li>
  <li><strong>Engine or APU fire</strong> during the final CAT II approach with no visual reference at minimums: <strong>autoland may be performed</strong> and the NNC done on the ground.</li>
  <li><strong>Pilot incapacitation</strong> during a CAT II approach with no visual reference at minimums: <strong>autoland may be performed</strong>; tell ATC to get medical assistance on landing, and advise if unable to vacate the runway.</li>
</ul>

<h2>Failed ground equipment</h2>
<ul>
  <li>Use the OM A table of failed or downgraded equipment before and during the flight. After passing 1,000 ft above the aerodrome, the commander may continue at his discretion if a ground failure is announced late.</li>
  <li>For CAT II, a <strong>combination</strong> of runway light deficiencies and RVR equipment deficiencies is not permitted. Failures other than ILS affect the RVR, not the DH.</li>
</ul>

<h2>Go-around (B737NG)</h2>
<ol class="steps">
  <li>PF pushes <strong>TO/GA</strong>: “GO-AROUND, CHECK GA THRUST” — A/T advances to reduced go-around thrust (1,000–2,000 ft/min climb); pitch TO/GA, about 15° nose-up initially; second push for full go-around thrust if needed.</li>
  <li>“FLAPS 15” — PM sets flaps and calls “GO-AROUND THRUST SET”.</li>
  <li>Positive rate: “GEAR UP”.</li>
  <li>Above <strong>400 ft RA</strong>, select the roll mode; below 400 ft the AFDS stays in go-around mode unless both A/Ps and FDs are disengaged.</li>
  <li>At acceleration height, retract flaps on schedule; then LVL CHG or VNAV, climb thrust, after take-off checklist.</li>
</ol>
<p>Note: the pitch mode cannot change from TO/GA until enough nose-down trim has been added for single A/P operation; if the stabiliser trim is not satisfactory, ALT ACQ is inhibited and the A/P disengage lights show steady red.</p>
""",
takeaways=["All NNCs by 1,000 ft AAL — otherwise go around.", "Below 800 ft RA, most A/P failures mean a manual go-around (or manual landing with visual reference).", "Engine failure: manual go-around; fire or incapacitation with no visual reference at minimums: autoland may be performed.", "Go-around: TO/GA, flaps 15, gear up; roll mode only above 400 ft RA."],
check=dict(q="At 600 ft RA on a CAT II approach, the A/P disengage light flashes red with the horn. What is the company response?", options=["Re-engage the A/P", "Execute a manual go-around (or land manually only with suitable visual reference)", "Continue to DH", "Disconnect the A/T only"], answer=1, explain="At or below 800 ft RA: execute a manual go-around, unless suitable visual reference allows a manual landing."),
),
]

QUESTIONS = [
Q(1, "LVO consists of:", ["Taxi, take-off and approach in low visibility", "Only CAT III landings", "Night flying", "Icing operations"], 0, "Low visibility taxi, take-off and approach."),
Q(1, "What is the company CAT II approach minimum for the B737-800?", ["DH 50 ft, RVR 175 m", "DH 100 ft, TDZ RVR 350 m", "DH 200 ft, RVR 550 m", "No DH"], 1, "CAT II: DH 100 ft, TDZ RVR 350 m (MID 175 m)."),
Q(1, "Who is the pilot flying in all phases of LVO?", ["The first officer", "The captain (left seat)", "Either pilot", "The more experienced pilot"], 1, "The left-seat pilot is PF in all LVO phases."),
Q(1, "According to ICAO, CAT I requires a DH not lower than:", ["100 ft", "150 ft", "200 ft", "250 ft"], 2, "CAT I: DH 200 ft."),
Q(1, "Which Domestic Airlines fleet is authorised for LVO?", ["Q200", "Q400", "B737-800", "All fleets"], 2, "Only the B737-800."),
Q(2, "At a CAT II DH of 100 ft, how far away is the runway in time?", ["About 30 seconds", "Less than 5 seconds", "About 1 minute", "About 15 seconds"], 1, "Less than 5 seconds."),
Q(2, "What is the visual segment?", ["The distance to the runway", "The length of approach/runway lighting in view at one moment", "The cockpit cut-off angle", "The RVR at mid-point"], 1, "Visual segment = lighting in view at an instant."),
Q(2, "Minimum visual reference to continue below DH in CAT II:", ["One light", "A 3-light segment of approach, TDZ, centreline or edge lights", "The threshold only", "The PAPI"], 1, "At least a 3-light segment, attained and maintained."),
Q(3, "Runway centreline lights in the last 300 m are:", ["White", "Alternating red and white", "All red", "Green"], 2, "All red for the last 300 m."),
Q(3, "A lit red stop bar may be crossed:", ["When cleared by ATC", "Never", "At night only", "If no traffic is visible"], 1, "Never cross a lit red stop bar."),
Q(3, "Why are CAT II/III holding positions farther from the runway?", ["To save fuel", "To protect the ILS critical and sensitive areas", "For noise", "To give the crew more time"], 1, "To keep aircraft clear of ILS protected areas."),
Q(4, "Maximum taxi speed in low visibility (company):", ["10 kt", "15 kt", "20 kt", "No limit"], 0, "10 kt."),
Q(4, "If unsure of your position during low visibility taxi, you should:", ["Continue slowly", "Stop immediately and ask ATC (follow-me / progressive taxi)", "Turn around", "Use the landing lights and continue"], 1, "Stop and ask."),
Q(4, "When should checklists and paperwork be completed in LVO?", ["During taxi", "With the aircraft stopped", "After take-off", "At the holding point while rolling"], 1, "With the aircraft stopped."),
Q(5, "Company LVTO minimum RVR:", ["125 m", "175 m", "300 m", "400 m"], 1, "175 m."),
Q(5, "When the TDZ RVR is measured, pilot assessment is possible only when the reported RVR is above:", ["75 m", "150 m", "300 m", "550 m"], 1, "Above 150 m."),
Q(5, "Can the RVR/visibility conversion table be used for take-off minima?", ["Yes", "No", "Only at night", "Only for CAT II"], 1, "No — not for take-off."),
Q(6, "What is set in the BARO minimums for a CAT II approach?", ["The DH", "Threshold elevation + 500 ft", "The MDA", "1,000 ft"], 1, "Threshold elevation + 500 ft."),
Q(6, "By what height must the second A/P be engaged for a dual-channel approach?", ["1,500 ft RA", "800 ft RA", "400 ft RA", "50 ft RA"], 1, "By 800 ft RA."),
Q(6, "Maximum crosswind for a company CAT II autoland:", ["10 kt", "15 kt", "20 kt", "25 kt"], 2, "20 kt (headwind 25, tailwind 10)."),
Q(6, "Visual reference is lost after touchdown. What do you do?", ["Go around", "Do not go around — continue the roll-out", "Apply TO/GA", "Stop on the runway immediately"], 1, "After touchdown a go-around must not be attempted."),
Q(7, "By what height must all non-normal checklists be completed?", ["500 ft AAL", "1,000 ft AAL", "DH", "1,500 ft RA"], 1, "1,000 ft above aerodrome level."),
Q(7, "Engine failure on a CAT II approach (no visual reference):", ["Continue autoland", "Disconnect A/P and A/T and execute a manual go-around", "Re-engage A/P", "Continue to DH"], 1, "Manual go-around (or manual landing with visual reference)."),
Q(7, "Pilot incapacitation on a CAT II approach, no visual reference at minimums:", ["Go around always", "Autoland may be performed; inform ATC for medical assistance", "Divert immediately", "Climb to MSA"], 1, "Autoland may be performed."),
]

COURSE = dict(
    slug="lvo-cat2", title="Low Visibility Operations (LVO) — CAT II", header_title="Low Visibility Operations",
    tagline="Low visibility taxi, take-off and CAT II autoland on the Boeing 737-800: concepts, visual references, aerodrome lighting, company minima, procedures, callouts and failures.",
    purpose="Train B737-800 crews in the company low visibility procedures (LV taxi, LVTO and CAT II autoland), based on the company All Weather Operation procedures, ICAO Doc 9365 and the ICAO low visibility presentation.",
    audience="Boeing 737-800 flight crew (captains and first officers). Q400 and Q200 crews may take it for awareness.",
    objectives=["Explain AWO, LVO, LVP and the approach categories", "Use visual references correctly at and below DH", "Recognise LVO aerodrome lighting, stop bars and protected areas",
                "Plan the flight and taxi in low visibility", "Apply the LVTO minima and procedures", "Fly the CAT II autoland with the company callouts", "Handle failures and the go-around"],
    icon="runway", cert_prefix="LVO", quiz_count=15, pass_mark=80, group="refresher", season="Additional", finale=None,
    modules=[dict(title="LVO Concepts", summary="Categories, requirements, visual references and the aerodrome", icon="search", lessons=range(1, 4)),
             dict(title="LVO Procedures (B737-800)", summary="Planning, LV taxi, LVTO, CAT II autoland, failures and go-around", icon="runway", lessons=range(4, 8))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("doc", "Approach to a runway at dusk in low light", "Low visibility operations: a level of safety equivalent to normal conditions."),
            2: ("doc", "Runway lights seen through low cloud and fog from the flight deck", "In low visibility the visual phase is very short (ICAO presentation)."),
            3: ("doc", "CAT II and III approach and runway lighting at night", "CAT II / III lighting: red side-row barrettes in the inner 300 m and touchdown zone lights (ICAO presentation)."),
            4: ("doc", "Approach lights in fog", "Plan the flight and the taxi before you move."),
            5: ("doc", "Runway and approach lights at night", "LVTO: RVR 175 m minimum, captain only."),
            6: ("doc", "Approach lighting seen from the air", "CAT II autoland: DH 100 ft, RVR 350 m."),
            7: ("doc", "Runway seen on approach in winter conditions", "Know the failure responses before the approach.")},
)
