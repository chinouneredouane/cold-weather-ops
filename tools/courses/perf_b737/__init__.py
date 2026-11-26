"""Boeing 737-800 NG Performance — 10 lessons following the standard EASA performance syllabus
(ATPL 032 / type-rating performance) and the chapters of the company B737-800 NG performance course:
take-off (speeds, limiting weights, field length, runway condition, climb, obstacles, tyre speed, brake energy, flaps,
reduced and derated thrust), en-route (cost index, climb, cruise altitude and speed, driftdown) and landing
(speeds, dispatch and in-flight landing distance).

Sources: company B737-800 NG performance course (diagrams); EASA CS-25, Part-CAT CAT.POL.A, AMC 25-13; ICAO Annex 6 and 14;
Boeing FCOM/FCTM/FPPM principles. Operational values always come from the company performance tool (OPT/EFB), FCOM PI and QRH."""
from courses.perf_common import fig, Q, REGS

_S = "Domestic Airlines B737-800 NG performance course"


def f(img, caption):
    return fig("b738-" + img, caption, _S)


LESSONS = [
# 1
dict(title="Performance Framework and Take-off Speeds", minutes=10,
objectives=["Name the speeds demonstrated during certification.", "Define the operational take-off speeds V1, VR, VLOF and V2.",
            "Explain how weight, density, flaps, slope and wind move V1, VR and V2."],
body="""
<h2>Why performance is regulated</h2>
<p>Performance rules make sure that an engine failure at the most critical moment of a flight never leaves the crew without a safe option. Certification (EASA CS-25) demonstrates what the aeroplane can do; the operating rules (Part-CAT, CAT.POL.A) say how much margin the airline must keep on every flight. For the B737-800 the results are delivered through the company performance tool, the FCOM Performance Inflight (PI) chapter and the QRH.</p>
<h2>Demonstrated speeds</h2>
<ul>
  <li><strong>VS / VSR</strong> — stall speed. Certification uses the reference stall speed VSR, a calibrated airspeed not lower than the 1-g stall speed (CS 25.103).</li>
  <li><strong>VMU</strong> — minimum unstick speed: the lowest speed at which the aeroplane can safely lift off and continue the take-off, at the maximum attainable angle of attack on the ground (CS 25.107).</li>
  <li><strong>VMCG</strong> — minimum control speed on the ground: after a sudden failure of the critical engine, the crew keeps the lateral deviation within 30 ft of the centreline with <strong>rudder only</strong> — no nosewheel steering. Determined at maximum take-off thrust, aft CG, trimmed for take-off (CS 25.149).</li>
  <li><strong>VMCA</strong> — minimum control speed in the air: straight flight with not more than 5° of bank and a heading change of 20° at most during the recovery.</li>
  <li><strong>VTIRE</strong> — maximum certified tyre speed: 225 mph (195 kt ground speed) for the B737.</li>
</ul>
<div class="callout caution"><span class="label">Note</span><p>Crosswind and slippery runways are <strong>not</strong> taken into account when VMCG and VMCA are determined.</p></div>
""" + f("speeds-overview", "Overview of the take-off speeds: demonstrated, operational, related and certified speeds in their order along the take-off.") + """
<h2>Operational speeds</h2>
<ul>
  <li><strong>VEF</strong> — the speed at which the critical engine is assumed to fail; not less than VMCG.</li>
  <li><strong>V1</strong> — the maximum speed at which the first action to stop must be taken, and the minimum speed from which the take-off can be continued after a failure at VEF. One second of recognition is allowed between VEF and V1. A single V1 is used for both cases (CAT.POL.A.205). V1 ≥ VMCG and V1 ≤ VR and VMBE.</li>
  <li><strong>VR</strong> — rotation speed, chosen so that a normal rotation (about 3° per second) gives V2 at 35 ft after an engine failure at VEF. VR ≥ V1 and VR ≥ 1.05 VMCA.</li>
  <li><strong>VLOF</strong> — lift-off speed (≥ 1.1 VMU all engines, ≥ 1.05 VMU one engine inoperative).</li>
  <li><strong>V2</strong> — take-off safety speed at the screen height: V2 ≥ 1.13 VSR and ≥ 1.1 VMCA.</li>
</ul>
<h2>What moves the speeds</h2>
<table><thead><tr><th>Factor</th><th>V1</th><th>VR</th><th>V2</th></tr></thead><tbody>
<tr><td>Higher weight</td><td>Higher (limited by the ability to stop)</td><td>Higher</td><td>Higher</td></tr>
<tr><td>Lower density (hot, high)</td><td>Higher</td><td>Higher</td><td>Lower to keep TODR within TODA; pressure altitude matters more than OAT</td></tr>
<tr><td>More flap</td><td>Lower</td><td>Lower</td><td>Lower</td></tr>
<tr><td>Downslope / tailwind</td><td>Lower (stopping is harder)</td><td>No effect</td><td>No effect</td></tr>
<tr><td>Upslope / headwind</td><td>Higher allowed</td><td>No effect</td><td>No effect</td></tr>
</tbody></table>
<div class="callout info"><span class="label">Boeing practice</span><p>In windshear or gusty crosswind conditions VR (and V2) may be increased, up to the VR for the performance-limited weight and by 20 kt at most, to improve the climb capability.</p></div>
""",
takeaways=["Certification demonstrates VSR, VMU, VMCG, VMCA and VTIRE.", "VMCG ≤ VEF < V1 ≤ VR; V2 ≥ 1.13 VSR and ≥ 1.1 VMCA.",
           "Heavier → all speeds higher; downslope and tailwind lower V1."],
check=dict(q="How is VMCG demonstrated?", options=["With nosewheel steering and brakes", "With rudder only, keeping within 30 ft of the centreline", "On a wet runway with crosswind", "With both engines at idle"], answer=1,
           explain="VMCG uses aerodynamic controls only — no nosewheel steering — and the lateral deviation must stay within 30 ft."),
),
# 2
dict(title="Maximum Take-off Weight and Field Length", minutes=10,
objectives=["List the limits that make up the performance-limited take-off weight.", "Define TORA, TODA, ASDA, stopway and clearway.",
            "Explain the accelerate-stop and take-off distance requirements and the line-up correction."],
body="""
<h2>The most limiting weight wins</h2>
<p>The <strong>performance-limited take-off weight (PLTOW)</strong> is the lowest of the field length, climb, obstacle, tyre speed and brake energy limit weights, further reduced by MEL items. The <strong>maximum allowable take-off weight</strong> is the lowest of the PLTOW, the maximum certified structural take-off weight and the maximum allowable landing weight plus trip fuel.</p>
""" + f("max-allowable-tow", "Building the maximum allowable take-off weight: the lowest of all limit weights.") + """
<h2>Declared distances</h2>
<ul>
  <li><strong>TORA</strong> — runway length declared available and suitable for the ground run.</li>
  <li><strong>ASDA</strong> — TORA plus stopway (if declared). <strong>Stopway</strong>: at least as wide as the runway, able to support the aeroplane during a rejected take-off.</li>
  <li><strong>TODA</strong> — TORA plus clearway. <strong>Clearway</strong>: under airport control, at least 500 ft wide, no object above a 1.25 % plane, not longer than half the TORA.</li>
</ul>
""" + f("clearway-stopway", "Stopway = ASDA − TORA; clearway = TODA − TORA.") + f("clearway-stopway-table", "Clearway and stopway compared. The runway end safety area (RESA) is neither and is never used in performance calculations.") + """
<h2>Accelerate-stop distance</h2>
<p>The accelerate-stop distance is the distance to accelerate with all engines to V1 (including one second between VEF and V1), to keep V1 for two seconds while the stopping configuration is set, and to decelerate to a full stop. On a <strong>dry</strong> runway no credit is taken for reverse thrust; on a wet or contaminated runway one reverser may be credited. Brakes are assumed fully worn (CS 25.101).</p>
""" + f("asd", "Accelerate-stop distance for a given take-off weight: acceleration, transition and deceleration.") + """
<h2>Take-off distance and run</h2>
<p>CAT.POL.A.205 requires: accelerate-stop distance ≤ ASDA, take-off distance ≤ TODA, take-off run ≤ TORA. The take-off distance is the longer of the distance to 35 ft with an engine failure at VEF, and 115 % of the all-engine distance to 35 ft. The <strong>field length limit weight</strong> is the lower of the ASD-limited and TOD-limited weights.</p>
<h2>Line-up correction</h2>
<p>Lining up uses runway. Whenever the aeroplane cannot start at the threshold, the available distances are reduced (CAT.POL.A.205): ASDA by the threshold-to-nose-gear distance, TODA by the threshold-to-main-gear distance, taking the minimum edge safety distance into account.</p>
""" + f("lineup-correction", "Line-up corrections: (A) for TODA, measured to the main gear; (B) for ASDA, measured to the nose gear.") + f("lineup", "Line-up assumptions for 90° and 180° turns. Following the yellow exit line from a high-speed intersection loses more runway than the data assume.") + """
<div class="callout caution"><span class="label">Intersection take-off</span><p>Use the data computed for the actual intersection. Company take-off data normally already include the standard line-up corrections.</p></div>
""",
takeaways=["Max allowable TOW = lowest of PLTOW, structural TOW, and max landing weight + trip fuel.", "ASD ≤ ASDA, TOD ≤ TODA, TOR ≤ TORA.",
           "No reverse thrust credit on a dry runway; brakes assumed fully worn.", "Correct ASDA to the nose gear and TODA to the main gear for line-up."],
check=dict(q="Which distance may include a stopway?", options=["TORA", "TODA", "ASDA", "LDA"], answer=2, explain="ASDA = TORA + stopway; clearway is added to TODA."),
),
# 3
dict(title="Balanced Take-off and Runway Surface Condition", minutes=10,
objectives=["Explain the balanced V1 and the balanced field length.", "Compare dry, wet and contaminated runway take-off rules.",
            "Explain the V1(MCG) limit weight and why clearway is restricted on wet and contaminated runways."],
body="""
<h2>Balanced V1</h2>
<p>For a fixed runway, a heavy take-off needs a <strong>low V1</strong> to be able to stop within the ASDA, but a <strong>high V1</strong> to reach V2 at 35 ft within the TODA after an engine failure. The highest weight is obtained where the two requirements meet: the <strong>balanced V1</strong> and the balanced take-off weight.</p>
""" + f("balanced-graph1", "Graph 1 — take-off weight versus V1 for a fixed runway: the ASDA line (red) and the TODA line (green) cross at the balanced V1.") + """
<h2>Balanced field length</h2>
<p>For a fixed weight, a low V1 shortens the accelerate-stop distance but lengthens the take-off distance, and the reverse for a high V1. The shortest required runway is where ASDR equals TODR: the <strong>balanced field length</strong>. With a stopway or clearway the optimum V1 moves and the take-off is "unbalanced".</p>
""" + f("balanced-graph2", "Graph 2 — required field length versus V1 for a fixed weight: ASDR = TODR gives the balanced field length.") + """
<h2>Dry and wet runways</h2>
<p>A <strong>damp</strong> runway (not shiny) may be treated as dry, except grass (CAT.POL.A.105); industry (TALPA) and ICAO guidance recommend treating it as wet. A <strong>wet</strong> runway has a reflective surface without significant standing water. Acceleration is unchanged but stopping is worse, so:</p>
<ul>
  <li>V1 is re-balanced to a lower value and the field length limit weight decreases;</li>
  <li>one reverser may be credited in the accelerate-stop distance;</li>
  <li>the screen height is reduced from 35 ft to <strong>15 ft</strong>, therefore clearway cannot be used;</li>
  <li>the weight may never exceed the dry-runway weight in the same conditions (CAT.POL.A.205(b)(5)) — the "dry check".</li>
</ul>
""" + f("wet-screen-height", "Wet runway take-off: lower V1 and weight, 15 ft screen height — the same TODR and ASDR as on a dry runway.") + """
<h2>Contaminated runways</h2>
<p>A runway is contaminated when more than 25 % of the surface in use is covered by standing water or slush deeper than 3 mm, loose snow (ICAO: deeper than 20 mm), compacted snow or ice. <strong>Fluid</strong> contaminants add displacement and spray drag and can cause aquaplaning; <strong>hard</strong> contaminants reduce friction without adding drag.</p>
""" + f("fluid-contaminant", "Fluid contaminant: spray and displacement drag increase with depth.") + f("hard-contaminant", "Hard contaminant: reduced tyre-to-ground friction; depth is not relevant.") + """
<p>The rules credit reverse thrust and a 15 ft screen height, but <strong>assumed-temperature reduced thrust is not allowed</strong>. GM1 CAT.POL.A.400: such operations should be rare — the first option is to wait for the runway to be cleared.</p>
<h2>V1(MCG) limit weight</h2>
<p>On a slippery runway V1 may need to be reduced so much that it falls below VMCG. V1 is then set equal to VMCG, which needs more stopping distance; the weight for which the aeroplane can accelerate to VMCG and just stop within the ASDA is the <strong>V1(MCG) limit weight</strong>. A derate (not an assumed temperature) lowers VMCG and can raise this limit.</p>
<h2>Clearway on contaminated runways</h2>
<p>The contaminated-runway adjustments give the same distance to 15 ft as the dry weight needs to 35 ft. If the dry weight already used clearway, the height at the runway end after an engine failure could be <strong>close to zero</strong>.</p>
""" + f("contaminated-clearway", "With clearway credited, the runway end crossing height on a contaminated runway can fall to 0–15 ft.") + f("contaminated-climb", "Once airborne, the lower (field-limited) weight on a contaminated runway gives a better climb gradient and more obstacle clearance."),
takeaways=["Balanced V1: ASD-limited and TOD-limited weights equal — the maximum field-limited weight.", "Wet: lower V1, one reverser credit, 15 ft screen height, no clearway, never heavier than dry.",
           "Contaminated: no assumed-temperature reduced thrust; check the V1(MCG) limit weight.", "Waiting for the runway to be cleared is always the first option."],
check=dict(q="What screen height is used at the end of the take-off distance on a wet runway?", options=["50 ft", "35 ft", "15 ft", "0 ft"], answer=2,
           explain="The wet-runway rules reduce the screen height to 15 ft — and so clearway cannot be used."),
),
# 4
dict(title="Take-off Climb Requirements and Improved Climb", minutes=9,
objectives=["Describe the four take-off flight path segments and their minimum gradients.", "Define the climb limit weight and the climb gradient.",
            "Explain improved climb, its advantages and its restrictions."],
body="""
<h2>The take-off flight path</h2>
<p>The take-off path runs from brake release to 1,500 ft above the runway (or the end of the transition to the en-route configuration, if higher). The <strong>take-off flight path</strong> starts at 35 ft at the end of the take-off distance and is computed with the critical engine inoperative from VEF, in still air, without ground effect (CS 25.111, 25.115). Boeing uses the minimum clean manoeuvring speed (VREF40 + 70 kt) as the final take-off speed.</p>
""" + f("takeoff-segments", "The four take-off flight path segments for a twin: gear retraction (gradient > 0), second segment at V2 (≥ 2.4 %), level acceleration (third segment) and final segment (≥ 1.2 %) at maximum continuous thrust.") + """
<table><thead><tr><th>Segment</th><th>Configuration</th><th>Minimum gross gradient (twin)</th></tr></thead><tbody>
<tr><td>First</td><td>Take-off flaps, gear retracting, V2, take-off thrust</td><td>Positive</td></tr>
<tr><td>Second</td><td>Gear up, take-off flaps, V2, take-off thrust</td><td>2.4 %</td></tr>
<tr><td>Third</td><td>Level acceleration (min 400 ft) and flap retraction</td><td>—</td></tr>
<tr><td>Final</td><td>Clean, maximum continuous thrust, final take-off speed</td><td>1.2 %</td></tr>
</tbody></table>
<p>The take-off thrust time limit (10 minutes with an engine out) ends the third segment. If any gradient cannot be achieved, the weight is reduced to the <strong>climb limit weight</strong>. More flap means more drag and a lower climb limit weight.</p>
""" + f("climb-gradient", "Climb gradient = altitude gain / horizontal distance. Rule of thumb: vertical speed (ft/min) divided by ground speed (kt) gives the gradient in percent.") + """
<h2>Improved climb</h2>
<p>When the runway is longer than the field limit requires, the excess runway can be traded for <strong>higher V1, VR and V2</strong>. The aeroplane then climbs at a speed closer to its best climb speed, so the climb limit weight (and often the obstacle limit weight) increases. Speeds can be raised until the field length or tyre speed limit becomes limiting, and V1 must stay below VMBE.</p>
""" + f("improved-climb", "Improved climb: a higher V2 gives either the same gradient at a higher weight (B) or a higher gradient at the same weight (C).") + f("improved-climb-tow", "The maximum improved-climb weight lies where the rising climb limit meets the falling field and tyre speed limit.") + """
<h2>Benefits and restrictions</h2>
<ul>
  <li><strong>Benefits</strong>: higher weight or higher assumed temperature when climb- or obstacle-limited; more tail clearance; distant obstacles become less limiting; the end of the third segment is reached higher.</li>
  <li><strong>Restrictions</strong>: smaller rejected take-off margin; close-in obstacles can become more limiting; more tyre wear; closer to VTIRE and VMBE — a slow rotation can exceed the tyre speed. Not with anti-skid inoperative. Speeds come from the performance tool or FPPM, not from the FMC.</li>
</ul>
""" + f("improved-climb-obstacles", "Improved climb increases the clearance over distant obstacles but reduces it over close-in obstacles."),
takeaways=["Twin minimum gross gradients: 1st > 0, 2nd 2.4 %, final 1.2 %.", "The climb limit weight is computed one engine out, in still air.",
           "Improved climb trades excess runway for higher speeds and a better gradient.", "Improved climb increases tyre speed and brake energy exposure."],
check=dict(q="What is the minimum second-segment gross climb gradient for a twin-engine aeroplane?", options=["1.2 %", "1.7 %", "2.4 %", "3.2 %"], answer=2,
           explain="CS 25.121(b): 2.4 % for two-engine aeroplanes, gear up, take-off flaps, V2."),
),
# 5
dict(title="Obstacles, Tyre Speed, Brake Energy and Flap Selection", minutes=10,
objectives=["Apply the net take-off flight path and obstacle clearance rules.", "Explain the engine failure procedure (SID deviation and restriction points).",
            "Explain the tyre speed and brake energy limits and how the take-off flap setting changes each limit."],
body="""
<h2>Obstacle accountability area</h2>
<p>Every obstacle inside the obstacle accountability area (departure sector) must be cleared with one engine inoperative until the aeroplane reaches 1,500 ft net height. CAT.POL.A.210 sets the lateral limits: a semi-width of 90 m + 0.125 D (60 m + half the wingspan for small wingspans), up to 300 m with sufficient navigation accuracy or 600 m otherwise for track changes up to 15°, and wider (600 m / 900 m) for larger track changes.</p>
""" + f("oaa", "Obstacle accountability area for track changes up to 15°.") + """
<h2>Net flight path</h2>
<p>The <strong>gross</strong> flight path is what an average aeroplane achieves with one engine out. The <strong>net</strong> flight path is the gross gradient reduced by <strong>0.8 %</strong> for a twin, to cover pilot technique and fleet variation. The net path must clear every obstacle by at least <strong>35 ft</strong>, or <strong>50 ft</strong> when the bank angle exceeds 15°. The most penalising obstacle gives the <strong>obstacle limit weight</strong>.</p>
""" + f("net-flight-path", "Vertical obstacle clearance: the net take-off flight path clears obstacles by at least 35 ft.") + f("reduced-screen-height", "Wet or contaminated runway: the gross path starts at 15 ft, so a close-in obstacle may be cleared by between 15 and 35 ft (AMC1 CAT.POL.A.210).") + """
<h2>Engine failure procedures</h2>
<p>Where obstacles would make the straight-out limit too restrictive, the company publishes an <strong>engine failure procedure</strong> (emergency turn). PANS-OPS makes this the operator's responsibility. Two points may be defined on a SID: the <strong>SID deviation point</strong>, where the engine-out route leaves the SID, and the <strong>SID restriction point</strong>, after which the SID itself can be followed safely with one engine inoperative.</p>
<div class="callout warn"><span class="label">Remember</span><p>A SID climb gradient (standard 3.3 %) is an all-engines gradient: meeting it does not prove one-engine-inoperative obstacle clearance.</p></div>
""" + f("thrust-drag", "Excess thrust with both engines is about four times the one-engine excess thrust: the height gained before a failure matters.") + """
<h2>Tyre speed and brake energy</h2>
<ul>
  <li>The <strong>tyre speed limit weight</strong> is the weight whose lift-off ground speed equals the certified tyre speed (B737: 225 mph / 195 kt). It can limit at hot and high airports or with improved climb. More flap or less weight lowers VLOF. Rotate at the normal rate — a slow rotation raises the actual lift-off speed.</li>
  <li><strong>VMBE</strong> is the highest V1 from which the brakes can absorb the energy of a stop. It is demonstrated with 90 % worn brakes, no reverse thrust and residual heat equal to 3 taxi miles and 3 stops; a safe evacuation must remain possible for 5 minutes after the stop. If V1 exceeds VMBE, reduce the weight or unbalance V1.</li>
</ul>
<h2>Choosing the take-off flap</h2>
<p>More flap creates more lift and more drag: shorter take-off distance and higher field limit weight, more tail clearance — but a lower climb limit and obstacle limit weight. <strong>Field-limited: choose more flap. Climb- or obstacle-limited: choose less flap.</strong> The performance tool normally optimises the flap setting.</p>
""",
takeaways=["Net path = gross − 0.8 % (twin); clearance ≥ 35 ft, ≥ 50 ft if bank > 15°.", "Meeting a SID gradient does not guarantee engine-out obstacle clearance.",
           "Tyre speed limits VLOF; VMBE limits V1.", "Field-limited → more flap; climb- or obstacle-limited → less flap."],
check=dict(q="The take-off is obstacle-limited. Which flap change usually helps?", options=["More flap", "Less flap", "Flap has no effect", "Flaps up"], answer=1,
           explain="Less flap reduces drag and improves the climb gradient — provided the field length allows it."),
),
# 6
dict(title="Reduced and Derated Take-off Thrust", minutes=10,
objectives=["Explain flat rating and EGT margin on the CFM56-7B.", "Compare derated thrust and the assumed temperature method.",
            "List the restrictions on reduced thrust and its effect on the take-off speeds."],
body="""
<h2>Flat-rated engine</h2>
<p>The CFM56-7B gives constant take-off thrust up to the <strong>flat-rating temperature</strong> (FRT, corner point; about ISA + 15 °C). Below it the engine is pressure-limited and N1 and EGT rise with OAT; above it the engine is temperature-limited: EGT stays at the limit and thrust falls.</p>
""" + f("flat-rating", "CFM56 flat rating: constant TO/GA thrust up to the flat-rated temperature; above it thrust decreases while EGT is held. EGT margin = red line − EGT at full thrust above the FRT.") + """
<h2>EGT margin and engine life</h2>
<p>Engine deterioration lowers the EGT margin; when the OAT limit falls below the FRT, a full-thrust take-off can exceed the red line. Engines cause about two thirds of aircraft performance deterioration. CFM figures: a 10 °C loss of EGT margin is about 3,000 cycles and costs about 0.7 % fuel; 1 % N1 ≈ 10 °C EGT; 1 °C of assumed temperature ≈ 3.5 °C EGT. Pilot tools: <strong>reduce take-off thrust whenever possible</strong>, and allow at least 3 minutes of cooling at or near idle after landing (taxi included).</p>
<h2>Derated thrust (fixed)</h2>
<p>A derate is a lower certified rating with its own AFM data — as if the aircraft had smaller engines. The derated value is a <strong>limit</strong>: VMCG and VMCA are computed at the derated thrust, so they are lower. Advantages: higher V1(MCG) limit weight, allowed on contaminated runways and with anti-skid inoperative, better trimmed, may improve loadability. Danger: advancing the levers beyond the derate after an engine failure at low speed can cause loss of directional control.</p>
<h2>Assumed temperature method (ATM)</h2>
<p>The crew enters a temperature higher than the OAT; the engine produces the thrust for that temperature. The thrust setting is <strong>not a limit</strong>: full thrust for the actual OAT may be selected at any time (AMC 25-13), because VMCG and VMCA are based on full thrust at the actual OAT. The maximum reduction is <strong>25 %</strong> of the rated thrust; the assumed temperature cannot be below the FRT; and it is limited by the actual weight reaching the performance-limited weight.</p>
""" + f("assumed-temp-thrust", "Assumed temperature: reduced thrust between the actual OAT and the maximum assumed temperature; at most 25 % below the available thrust.") + """
<h2>Built-in margins of ATM</h2>
<p>At the actual (lower) temperature the air is denser: the <strong>true airspeed is lower</strong> for the same IAS and the <strong>thrust is higher</strong> than computed. The aeroplane therefore uses less runway and climbs better than assumed. These margins exist only when the assumed temperature is above the FRT and above the OAT, they do not exist with a derate, and they must never be used for weight planning.</p>
""" + f("atm-margins", "ATM is conservative: the actual performance is always better than the assumed performance.") + """
<h2>Restrictions and effects</h2>
<ul>
  <li>No ATM on contaminated runways; on wet runways only with suitable data; not when items increase workload (inoperative engine instruments, reversers or anti-skid, engine intermix, non-standard procedures) — AMC 25-13.</li>
  <li><strong>Double derate</strong>: ATM applied to a derate, at most 25 % below the derated thrust.</li>
  <li>Reduced thrust needs a <strong>higher V1</strong> (re-balancing) and a <strong>lower V2</strong>; the trim is set for full thrust, so expect a nose-up trim after take-off.</li>
  <li>The application of reduced thrust is always at the commander's discretion; company restrictions apply.</li>
</ul>
<div class="callout info"><span class="label">Optimised take-off</span><p>The performance tool combines flap settings and improved climb to find the highest assumed temperature — this does not reduce the margins: a higher assumed temperature gives more TAS and thrust margin.</p></div>
""",
takeaways=["CFM56 flat rated to about ISA + 15 °C; reduce thrust whenever possible to protect EGT margin.", "Derate = a new limit (lower VMC); ATM = not a limit, full thrust always available.",
           "ATM: maximum 25 % reduction, not below the FRT, never on contaminated runways.", "ATM margins come from lower TAS and higher actual thrust — never plan with them."],
check=dict(q="With the assumed temperature method, may the crew advance the thrust levers to full thrust after an engine failure?", options=["No — the reduced thrust is a limit", "Yes — reduced thrust is not a limit", "Only above V2", "Only with a derate"], answer=1,
           explain="AMC 25-13: with reduced (ATM) thrust, full take-off thrust may be selected at any time; VMCG/VMCA were computed with full thrust."),
),
# 7
dict(title="En-route Climb and Cruise", minutes=9,
objectives=["Explain the cost index and its effect on speeds.", "Describe the climb profile and the crossover altitude.",
            "Choose a cruise altitude and speed: optimum and maximum altitude, step climb, MRC, LRC and ECON."],
body="""
<h2>Cost index</h2>
<p><strong>Cost index (CI) = time-related costs / fuel costs.</strong> A low CI flies slower and burns less fuel; a high CI flies faster to save time-related costs. CI 0 gives the maximum range cruise speed.</p>
<h2>Climb</h2>
<p>The economy climb speed increases with weight and cost index. Climbing at constant IAS, the TAS increases; at constant Mach, it decreases. The change from IAS to Mach happens at the <strong>crossover altitude</strong> (around FL290 for 300 kt / M0.78).</p>
""" + f("ias-mach", "IAS and Mach versus altitude: climb profile 250 kt – 300 kt – M0.78, crossover altitude and tropopause.") + """
<h2>Optimum and maximum altitude</h2>
<ul>
  <li>The <strong>optimum altitude</strong> gives the best fuel mileage (or, at ECON speed, the lowest cost). It rises as weight decreases. Stay within about ±2,000 ft (±1,000 ft in RVSM airspace): 2,000 ft below optimum costs about 1 % fuel, 2,000 ft above about 2 %.</li>
  <li>The <strong>maximum altitude</strong> is the lowest of the certified ceiling, the thrust-limited altitude (residual climb 100 ft/min in cruise, 300 ft/min in climb) and the manoeuvre-margin altitude (buffet margin 1.3 g ≈ 40° bank; optimum altitude gives about 1.5 g).</li>
</ul>
""" + f("step-climb", "Step climbs keep the aeroplane close to the optimum altitude as fuel burns.") + f("cg-travel", "737NG CG travel with fuel burn. Enter a realistic cruise CG in the FMC: the default forward CG gives a conservative maximum altitude.") + """
<div class="callout caution"><span class="label">Near the maximum altitude</span><p>Only LNAV protects the bank angle against the thrust limit. Otherwise fly at least 10 kt above the lower amber band and keep the bank below 10°. The FMC maximum altitude does not account for stick-shaker speeds.</p></div>
<h2>Cruise speed</h2>
<ul>
  <li><strong>MRC</strong> — maximum range cruise: the best fuel mileage for the weight (CI 0); poor speed stability.</li>
  <li><strong>LRC</strong> — long range cruise: about 1 % less mileage but 3–5 % faster, with better speed stability.</li>
  <li><strong>ECON</strong> — speed for the minimum total cost, from MRC at CI 0 up to the cruise thrust limit. Tailwind lowers it, headwind raises it. Typical airline CI values give a speed between MRC and LRC.</li>
</ul>
""" + f("mrc-lrc", "Fuel mileage versus cruise speed: MRC and LRC decrease as the weight decreases.") + f("econ-speed", "ECON speed: the minimum of fuel plus time-related costs."),
takeaways=["CI = time costs / fuel costs; CI 0 = MRC.", "Optimum altitude rises as weight decreases; step climb to stay within ±2,000 ft (RVSM ±1,000 ft).",
           "Maximum altitude: certified, thrust-limited or buffet-limited (1.3 g), whichever is lowest.", "LRC ≈ 1 % less mileage than MRC but 3–5 % faster."],
check=dict(q="What does a cost index of zero give?", options=["Maximum speed", "Maximum range cruise (minimum fuel)", "Long range cruise", "Holding speed"], answer=1,
           explain="With no time-related cost, the FMC minimises fuel: MRC."),
),
# 8
dict(title="Driftdown and En-route Obstacle Clearance", minutes=8,
objectives=["Describe the driftdown procedure and the driftdown ceiling.", "Apply the net driftdown flight path clearance rules (CAT.POL.A.215).",
            "Explain the lateral corridor and the route study."],
body="""
<h2>Why the aeroplane drifts down</h2>
<p>After an engine failure in cruise the thrust required exceeds the maximum continuous thrust of the remaining engine. The aeroplane must descend to a lower altitude where denser air gives enough thrust to balance the drag.</p>
<h2>The driftdown procedure</h2>
<ol>
  <li>Set <strong>maximum continuous thrust</strong> on the remaining engine.</li>
  <li>Decelerate to the <strong>optimum driftdown speed</strong> (best lift-to-drag ratio) while maintaining altitude.</li>
  <li>Descend at this speed to the <strong>driftdown ceiling</strong> (level-off altitude).</li>
</ol>
<p>A higher speed gives a steeper descent and a lower level-off altitude. After the driftdown, LRC gives the best range.</p>
""" + f("driftdown-speed", "A higher driftdown speed gives a lower level-off altitude.") + """
<h2>Vertical clearance</h2>
<p>The <strong>net driftdown flight path</strong> (gross gradient reduced by 1.1 % for a twin) must clear all obstacles by <strong>2,000 ft</strong> during the descent and by <strong>1,000 ft</strong> after level-off, within 5 NM either side of the track, and allow level flight at 1,500 ft above the aerodrome of intended landing (CAT.POL.A.215). Anti-ice drag and the most unfavourable CG are included when applicable.</p>
""" + f("driftdown-requirements", "Driftdown requirements: gross and net driftdown paths, 2,000 ft and 1,000 ft obstacle clearances, 1,500 ft over the diversion airport.") + """
<h2>Lateral clearance and route study</h2>
<p>EASA requires 5 NM either side of the intended track (more than the ICAO 5 statute miles), increased to 10 NM when the navigation accuracy is not met. For mountainous routes, a route study defines escape procedures and decision points from the most critical point of failure. If the requirements cannot be met, the weight is restricted or another route is chosen.</p>
""" + f("driftdown-route", "Driftdown route analysis: escape paths and decision points over high terrain."),
takeaways=["Driftdown: MCT, decelerate to the best L/D speed, descend to the driftdown ceiling.", "Net path = gross − 1.1 % (twin); 2,000 ft clearance in descent, 1,000 ft after level-off.",
           "Corridor 5 NM each side (10 NM without the navigation accuracy).", "Mountain routes need a route study with escape procedures."],
check=dict(q="During driftdown, by how much must the net flight path clear the terrain?", options=["500 ft", "1,000 ft", "2,000 ft", "35 ft"], answer=2,
           explain="CAT.POL.A.215: 2,000 ft during the descent, 1,000 ft for level flight."),
),
# 9
dict(title="Landing Speeds and Dispatch Landing Requirements", minutes=10,
objectives=["Define LDA and explain the displaced threshold.", "Define VREF and the final approach speed (FAS).",
            "Apply the dispatch landing field length rules for dry, wet and contaminated runways."],
body="""
<h2>Landing distance available</h2>
<p>The LDA is the runway length declared suitable for the landing ground run. Stopway cannot be used. An obstacle in the approach funnel creates a <strong>displaced threshold</strong>: the LDA starts at the displaced threshold, while the paved area before it remains usable for taxi, take-off and the landing roll-out of the opposite direction.</p>
""" + f("displaced-threshold", "Displaced threshold due to an obstacle in the approach path.") + """
<h2>Landing speeds</h2>
<p><strong>VREF</strong> is at least 1.23 VSR0 in the landing configuration and not less than VMCL. The <strong>final approach speed</strong> (FAS) is VREF plus a correction: half the steady headwind component plus the full gust increment, at least 5 kt and at most 20 kt, and at least 5 kt below the flap placard speed. The gust increment is kept to touchdown; touchdown is normally between VREF and VREF − 5 kt.</p>
""" + f("landing-speeds", "Landing speeds: FAS down to 50 ft at the threshold, touchdown between VREF and VREF − 5 kt.") + """
<h2>Maximum allowable landing weight</h2>
<p>For dispatch, the landing weight at destination and alternates is the lowest of the <strong>landing field limit weight</strong>, the <strong>landing climb limit weight</strong> (approach and landing climb gradients), the maximum structural landing weight and, where relevant, the quick-turnaround brake cooling limit. Not more than 50 % of the headwind and not less than 150 % of the tailwind are used, and slopes beyond ±2 % are accounted for (the B737NG is limited to ±2 %).</p>
<h2>Certified landing distance</h2>
<p>The flight-test landing distance (from 50 ft, aggressive technique, maximum manual braking, no reverse) is multiplied by <strong>1.67</strong> for a dry runway — the aeroplane must stop within <strong>60 % of the LDA</strong> (CAT.POL.A.230). On a wet runway the requirement is 115 % of the dry distance (CAT.POL.A.235): <strong>52 % of the LDA</strong>. On a contaminated runway it is the longer of the wet distance and 115 % of the approved contaminated landing distance.</p>
""" + f("certified-landing-distance", "Certified landing distances: flight-test distance + 67 % (dry), + 15 % more (wet).") + f("lflw-margins", "Planning margins on the LDA: 40 % dry and 48 % wet.") + """
<h2>Which runway?</h2>
<p>The dispatch check is made for the most favourable runway in still air <strong>and</strong> for the runway most likely to be assigned with the expected wind (GM1 CAT.POL.A.230). If the weight only meets the first case, dispatch is possible with two suitable alternates; if it only fails the second, one suitable alternate is required — and in flight the actual landing weight must meet the limit for the actual wind.</p>
""",
takeaways=["VREF ≥ 1.23 VSR0; FAS = VREF + ½ steady headwind + full gust (5–20 kt).", "Dispatch dry: stop within 60 % of LDA (factor 1.67).",
           "Wet: 115 % of the dry distance (52 % of LDA).", "Check both the longest runway in still air and the expected runway with the expected wind."],
check=dict(q="For dispatch to a dry runway, a jet must be able to stop within what part of the LDA?", options=["50 %", "60 %", "70 %", "85 %"], answer=1,
           explain="CAT.POL.A.230: turbojet aeroplanes — 60 % of the LDA."),
),
# 10
dict(title="In-flight Landing Distance and Runway Condition Reports", minutes=9,
objectives=["Explain the in-flight landing performance assessment at the time of arrival.", "Use runway condition reports (GRF / RCAM) in the assessment.",
            "Recall the go-around climb gradients and the autoland correction."],
body="""
<h2>Dispatch is not the end</h2>
<p>The dispatch rules use planning assumptions. Before starting an approach, the commander must be satisfied that the weather, the runway condition and the aeroplane's performance allow a safe approach, landing or missed approach (CAT.OP.MPA.300). The assessment uses the actual landing weight and the actual conditions:</p>
<ul>
  <li>the <strong>landing distance required</strong> must not exceed the LDA;</li>
  <li>the <strong>go-around gradient</strong> must be achievable.</li>
</ul>
<h2>Factored in-flight landing distance</h2>
<p>The in-flight landing distance from the QRH / performance tool is an operational distance for the actual braking action, speed additives, reverser use and autobrake. A margin of <strong>15 %</strong> is applied when the runway is not dry — company data normally include it. QRH Normal Configuration Landing Distance tables for slippery runways are already factored by 15 %. Landing distance data are based on fully worn brakes (CS 25.101).</p>
<h2>Runway condition reports</h2>
<p>Under the Global Reporting Format (ICAO Annex 14 / PANS-Aerodromes, applicable since November 2021), the aerodrome reports a <strong>runway condition code</strong> (RWYCC 6 to 0) for each third of the runway, with the contaminant type, depth and coverage. The code links directly to a braking action and to the performance data:</p>
<table><thead><tr><th>RWYCC</th><th>Typical description</th><th>Braking action</th></tr></thead><tbody>
<tr><td>6</td><td>Dry</td><td>—</td></tr>
<tr><td>5</td><td>Wet (up to 3 mm), frost</td><td>Good</td></tr>
<tr><td>4</td><td>Compacted snow (OAT −15 °C or colder)</td><td>Good to medium</td></tr>
<tr><td>3</td><td>Slush, dry/wet snow over 3 mm, wet "slippery wet" runway</td><td>Medium</td></tr>
<tr><td>2</td><td>Standing water or slush over 3 mm</td><td>Medium to poor</td></tr>
<tr><td>1</td><td>Ice</td><td>Poor</td></tr>
<tr><td>0</td><td>Wet ice, water on compacted snow</td><td>Less than poor — no operations</td></tr>
</tbody></table>
<h2>Pilot reports of braking action</h2>
<p>The reported code is an assessment made at a given time. Conditions change quickly with precipitation, temperature and traffic.</p>
<div class="callout warn"><span class="label">Pilot reports</span><p>An air-report of braking action worse than the reported code is an important threat: downgrade the assessment and share the report. See the Cold Weather Operations course (GRF module) for full detail.</p></div>
<h2>Go-around and autoland</h2>
<ul>
  <li><strong>Approach climb</strong> (one engine inoperative, approach flaps, gear up): at least <strong>2.1 %</strong> for a twin (CS 25.121(d)).</li>
  <li><strong>Landing climb</strong> (all engines, landing configuration, gear down): at least <strong>3.2 %</strong> (CS 25.119).</li>
  <li>Autoland may need a longer landing distance (CS-AWO): reduce the LDA by the published autoland increment (AMC7 CAT.POL.A.320).</li>
  <li>If the dispatch relied on the actual wind at a single-runway destination, check that the actual landing weight does not exceed the limit for the actual wind.</li>
</ul>
<div class="callout info"><span class="label">Good practice</span><p>Brief the landing distance assessment with the approach briefing: runway, RWYCC, wind, autobrake, flap, reverser plan, and the go-around gradient if the missed approach is demanding.</p></div>
""",
takeaways=["Before every approach: actual landing distance ≤ LDA and go-around gradient achievable (CAT.OP.MPA.300).", "Apply 15 % to the in-flight landing distance when the runway is not dry.",
           "RWYCC 6–0 links runway condition to braking action and data; RWYCC 0 = no operations.", "Approach climb 2.1 % (OEI), landing climb 3.2 % (AEO)."],
check=dict(q="The runway condition code reported is 0. What does it mean?", options=["Dry runway", "Good braking", "Less than poor braking — no operations", "Medium braking"], answer=2,
           explain="RWYCC 0 (wet ice, water on compacted snow): braking less than poor — operations are not permitted."),
),
]

QUESTIONS = [
Q(1, "Which speed must not be less than VMCG?", ["VMU", "VEF and V1", "VREF", "VLOF only"], 1, "VEF ≥ VMCG, and V1 is at least VMCG."),
Q(1, "VMCA is demonstrated with a maximum bank angle of:", ["0°", "5°", "15°", "30°"], 1, "Straight flight with not more than 5° bank toward the live engine."),
Q(1, "How much recognition time is allowed between VEF and V1?", ["None", "One second", "Two seconds", "Three seconds"], 1, "One second between the failure and the pilot's first action."),
Q(1, "V2 must be at least:", ["1.05 VSR", "1.13 VSR and 1.1 VMCA", "1.23 VSR0", "VMCG + 10 kt"], 1, "V2 ≥ 1.13 VSR and ≥ 1.1 VMCA."),
Q(1, "A tailwind on take-off:", ["Increases V1", "Decreases V1 because stopping is harder", "Increases V2", "Has no effect on V1"], 1, "Tailwind hurts the stopping capability: V1 is lower."),
Q(2, "The clearway is added to:", ["TORA to give ASDA", "TORA to give TODA", "ASDA to give LDA", "LDA"], 1, "TODA = TORA + clearway."),
Q(2, "On a dry runway, the accelerate-stop distance credits:", ["Both reversers", "One reverser", "No reverse thrust", "Reverse thrust and autobrake"], 2, "No reverse thrust credit on a dry runway; speedbrakes are credited."),
Q(2, "The line-up correction for ASDA is measured to the:", ["Main gear", "Nose gear", "Tail", "Wing tip"], 1, "ASDA: threshold to nose gear; TODA: threshold to main gear."),
Q(2, "The maximum allowable take-off weight can be restricted by the maximum landing weight plus:", ["Taxi fuel", "Trip fuel", "Reserve fuel", "Contingency fuel"], 1, "The aeroplane must arrive at or below the maximum allowable landing weight."),
Q(2, "May the RESA be used as stopway?", ["Yes", "No", "Only on wet runways", "Only for take-off"], 1, "RESA is not stopway or clearway and is never used in performance calculations."),
Q(3, "On a fixed runway, the maximum field-limited weight is reached when:", ["V1 = VR", "The ASD-limited and TOD-limited weights are equal (balanced V1)", "V1 = VMCG", "TORA = LDA"], 1, "The two lines cross at the balanced V1."),
Q(3, "On a wet runway, clearway:", ["Is fully credited", "Cannot be used because the screen height is 15 ft", "Doubles", "Replaces the stopway"], 1, "With a 15 ft screen height, clearway is not used."),
Q(3, "Which is NOT allowed on a contaminated runway?", ["Derated thrust", "Assumed temperature reduced thrust", "Reverse thrust credit", "15 ft screen height"], 1, "ATM is prohibited on contaminated runways (AMC 25-13)."),
Q(3, "What is the V1(MCG) limit weight?", ["The weight at which V1 = VR", "The weight for which the aeroplane can accelerate to VMCG and just stop within the ASDA", "The tyre speed limit", "The brake energy limit"], 1, "When V1 would fall below VMCG, V1 = VMCG and the weight is limited."),
Q(3, "A runway is contaminated when more than what part of the surface is covered?", ["10 %", "25 %", "50 %", "75 %"], 1, "More than 25 % of the area in use."),
Q(4, "The final take-off segment minimum gross gradient for a twin is:", ["0 %", "1.2 %", "2.4 %", "3.2 %"], 1, "CS 25.121(c): 1.2 %."),
Q(4, "Climb requirements are computed with:", ["The actual wind", "Zero wind, one engine inoperative", "50 % headwind", "Both engines"], 1, "Still air, critical engine inoperative from VEF."),
Q(4, "Improved climb is only possible when:", ["The take-off is field-limited", "There is excess runway", "The runway is contaminated", "Anti-skid is inoperative"], 1, "It trades excess runway for higher speeds."),
Q(4, "A rule of thumb for the climb gradient in percent is:", ["IAS / altitude", "Vertical speed (ft/min) / ground speed (kt)", "N1 / OAT", "TAS / 60"], 1, "V/S in ft/min divided by GS in kt."),
Q(5, "The net take-off flight path for a twin is the gross path reduced by:", ["0.5 %", "0.8 %", "1.1 %", "1.6 %"], 1, "0.8 % for two-engine aeroplanes."),
Q(5, "With a bank angle above 15°, the net path must clear obstacles by:", ["35 ft", "50 ft", "100 ft", "1,000 ft"], 1, "CAT.POL.A.210: 50 ft when the bank exceeds 15°."),
Q(5, "If V1 exceeds VMBE:", ["Increase the weight", "Reduce the weight or V1", "Ignore it on a dry runway", "Use more reverse"], 1, "Reduce the weight or unbalance V1 below VMBE."),
Q(5, "The take-off is field-length limited. Which flap change usually helps?", ["Less flap", "More flap", "Flaps up", "No change"], 1, "More flap shortens the take-off distance."),
Q(5, "Meeting the SID all-engine climb gradient:", ["Guarantees engine-out obstacle clearance", "Does not prove engine-out obstacle clearance", "Replaces the performance check", "Is only for turboprops"], 1, "The engine failure procedure covers one-engine-inoperative obstacle clearance."),
Q(6, "Above the flat-rating temperature, the CFM56:", ["Keeps constant thrust", "Is temperature-limited: thrust decreases", "Increases EGT margin", "Increases N1"], 1, "Above the FRT the EGT is held and thrust falls."),
Q(6, "The maximum thrust reduction with the assumed temperature method is:", ["10 %", "25 %", "40 %", "50 %"], 1, "AMC 25-13: reduced thrust at least 75 % of the rated thrust."),
Q(6, "Why does a derate increase the V1(MCG) limit weight?", ["It increases V1", "VMCG is computed with the lower derated thrust", "It reduces the weight", "It removes the 1-second rule"], 1, "Lower maximum thrust → lower VMCG."),
Q(6, "Reduced thrust requires:", ["A lower V1 and a higher V2", "A higher V1 and a lower V2", "No speed change", "VR = V2"], 1, "Re-balancing gives a higher V1; less excess thrust gives a lower V2."),
Q(6, "An assumed temperature below the flat-rating temperature:", ["Reduces thrust a lot", "Gives no thrust reduction", "Is prohibited", "Increases thrust"], 1, "Thrust is constant below the FRT."),
Q(7, "A high cost index means:", ["Low speed, low fuel burn", "High speed, high fuel burn, shorter trip time", "MRC", "Holding speed"], 1, "Time-related costs dominate."),
Q(7, "Flying 2,000 ft above the optimum altitude costs about:", ["0 %", "1 %", "2 %", "5 %"], 2, "About 2 % (2,000 ft below: about 1 %)."),
Q(7, "The standard FMC buffet margin is:", ["1.0 g", "1.3 g", "1.5 g", "2.5 g"], 1, "1.3 g, about 40° bank to buffet onset."),
Q(7, "LRC compared with MRC is:", ["Slower", "About 1 % less mileage but 3–5 % faster", "Always more economical", "Only for driftdown"], 1, "LRC gives up 1 % mileage for speed and stability."),
Q(8, "The first action of the driftdown procedure is:", ["Descend immediately at high speed", "Set maximum continuous thrust on the remaining engine", "Extend flaps", "Climb"], 1, "MCT, then decelerate at altitude to the driftdown speed."),
Q(8, "The net driftdown path of a twin is the gross reduced by:", ["0.8 %", "1.1 %", "1.6 %", "2.4 %"], 1, "1.1 % for two-engine aeroplanes."),
Q(8, "The EASA lateral corridor for en-route obstacle clearance is:", ["2 NM", "5 NM each side (10 NM without the navigation accuracy)", "20 NM", "1 NM"], 1, "CAT.POL.A.215: 5 NM, or 10 NM."),
Q(9, "The final approach speed correction for wind is:", ["Full headwind", "Half the steady headwind plus the full gust, 5 to 20 kt", "Gust only", "Always 5 kt"], 1, "Boeing: ½ steady headwind + full gust, minimum 5, maximum 20 kt."),
Q(9, "For dispatch on a wet runway, the LDA must be at least:", ["100 % of the dry distance", "115 % of the dry required distance", "150 %", "60 %"], 1, "CAT.POL.A.235: 115 %."),
Q(9, "Which wind may be used for landing dispatch?", ["100 % of the headwind", "Not more than 50 % of the headwind and not less than 150 % of the tailwind", "Zero always", "Actual wind only"], 1, "CAT.POL.A.230(d)."),
Q(10, "Before commencing an approach, which rule requires the commander to be satisfied about landing performance?", ["CAT.POL.A.210", "CAT.OP.MPA.300", "CS 25.107", "ORO.FTL.205"], 1, "CAT.OP.MPA.300 — approach and landing conditions."),
Q(10, "The minimum approach climb gradient (OEI) for a twin is:", ["1.2 %", "2.1 %", "2.4 %", "3.2 %"], 1, "CS 25.121(d): 2.1 %."),
Q(10, "The margin normally added to the in-flight landing distance on a non-dry runway is:", ["0 %", "15 %", "40 %", "67 %"], 1, "15 % is recommended and included in company data."),
]

COURSE = dict(
    slug="b737-performance",
    title="Boeing 737-800 NG Performance",
    header_title="B737-800 NG Performance",
    tagline="Take-off, en-route and landing performance of the Boeing 737-800 NG: speeds, limiting weights, runway condition, climb and obstacles, reduced thrust, cruise, driftdown and landing distance.",
    purpose="Give B737-800 flight crew a complete understanding of aeroplane performance — the certification basis (CS-25), the operating rules (Part-CAT CAT.POL.A) and Boeing practice — so they can use the company performance tool, FCOM PI and QRH with full understanding.",
    audience="Boeing 737-800 NG flight crew (type rating and recurrent).",
    objectives=["Define the certification and operational take-off speeds", "Build the maximum allowable take-off weight", "Apply field length, runway condition, climb and obstacle rules",
                "Use reduced and derated thrust correctly", "Choose cruise altitude and speed", "Plan and fly a driftdown", "Apply the dispatch and in-flight landing rules"],
    icon="plane", cert_prefix="B738P", quiz_count=20, pass_mark=80,
    group="refresher", season="Performance",
    finale=None,
    modules=[dict(title="Take-off Performance", summary="Speeds, limiting weights, field length, runway condition, climb, obstacles, brakes, flaps and reduced thrust", icon="runway", lessons=range(1, 7)),
             dict(title="En-route Performance", summary="Cost index, climb, cruise altitude and speed, driftdown", icon="plane", lessons=range(7, 9)),
             dict(title="Landing Performance", summary="Landing speeds, dispatch and in-flight landing distance, runway condition reports", icon="runway", lessons=range(9, 11))],
    lessons=LESSONS, questions=QUESTIONS,
    references=REGS,
    images={1: ("gen", "Boeing 737 lined up for take-off", "Every speed has a meaning."),
            2: ("gen", "Runway seen from the threshold", "The lowest limit decides."),
            3: ("gen", "Wet runway at dusk", "Wet and contaminated runways change the rules."),
            4: ("gen", "Airliner climbing away after take-off", "One engine out, the gradient must still be there."),
            5: ("gen", "Airliner climbing over hills", "The net path must clear every obstacle."),
            6: ("gen", "Airliner taking off on a cool morning", "Reduce thrust whenever you can."),
            7: ("gen", "Airliner cruising above the clouds", "Cost index decides the speed."),
            8: ("gen", "Airliner over mountains", "Driftdown: stay as high as possible."),
            9: ("gen", "Airliner on final approach", "60 % of the LDA for dispatch."),
            10: ("gen", "Airliner landing on a wet runway", "Assess the landing distance before every approach.")},
)
