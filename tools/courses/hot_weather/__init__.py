"""Hot Weather Operations (summer season), all fleets — 11 lessons following the company syllabus:
1 High temperature meteorology · 2 Density altitude and performance · 3 High temperature take-off planning ·
4 Brake energy management · 5 Engine limitations and hot starts · 6 Climb gradient and obstacle assessment ·
7 MEL/CDL in hot weather · 8 CRM in performance-limited operations · 9 Situation awareness ·
10 Human performance in high temperature · 11 Flight safety trends — summer season.

Sources: company summer recurrent programme; ICAO Annex 6; EASA CS-25 (take-off path, climb gradients) and Part-CAT
(CAT.POL.A); FAA Aviation Weather Handbook FAA-H-8083-28B and Pilot's Handbook of Aeronautical Knowledge
FAA-H-8083-25C (public-domain figures). Type values always come from the AFM / FCOM / AOM / QRH and the MEL."""
from courses.upset_recovery.diagrams import FONT, INK, MUTED, LINE, GREEN, GREEN_D, RED, AMBER, BLUE

_WX = "FAA Aviation Weather Handbook FAA-H-8083-28B"
_PHAK = "FAA Pilot's Handbook of Aeronautical Knowledge FAA-H-8083-25C"


def faa(img, caption, src):
    return (f'<figure class="lesson-figure"><img src="../media/images/{img}.jpg" alt="{caption}" loading="lazy">'
            f'<figcaption>{caption} <span class="muted">Source: {src} (public domain).</span></figcaption></figure>')


def svgfig(svg, title, caption, vb="0 0 700 320"):
    return (f'<figure class="diagram"><svg viewBox="{vb}" role="img" aria-label="{title}"><title>{title}</title>'
            f'<defs><marker id="hwa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10z" fill="{MUTED}"/></marker></defs>'
            f'<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg><figcaption>{caption}</figcaption></figure>')


def brake_energy_diagram():
    pts = " ".join(f"{60 + v * 5.6:.0f},{280 - (v / 100) ** 2 * 200:.0f}" for v in range(0, 101, 5))
    svg = (f'<line x1="60" y1="280" x2="640" y2="280" stroke="{INK}"/><line x1="60" y1="280" x2="60" y2="40" stroke="{INK}"/>'
           f'<polyline points="{pts}" fill="none" stroke="{RED}" stroke-width="3"/>'
           f'<text x="66" y="40" font-weight="700">Energy the brakes must absorb</text><text x="560" y="300">Speed at brake application</text>'
           f'<line x1="60" y1="96" x2="640" y2="96" stroke="{AMBER}" stroke-dasharray="6 5"/><text x="70" y="90" fill="{AMBER}" font-weight="700">Maximum brake energy limit</text>'
           f'<line x1="563" y1="96" x2="563" y2="280" stroke="{AMBER}" stroke-dasharray="4 4"/><text x="530" y="270" fill="{AMBER}">V<tspan font-size="10">MBE</tspan></text>'
           f'<text x="250" y="205" fill="{MUTED}">Energy grows with the SQUARE of speed:</text><text x="250" y="224" fill="{MUTED}">+10 % speed ≈ +21 % energy.</text>'
           f'<text x="250" y="243" fill="{MUTED}">Heat, altitude and tailwind raise the ground speed.</text>')
    return svgfig(svg, "Brake energy versus speed", "Brake energy rises with the square of the ground speed. On a hot, high runway the same V1 means a higher ground speed — check the brake energy (VMBE) limit and the brake cooling schedule.")


def flat_rating_diagram():
    svg = (f'<line x1="70" y1="270" x2="640" y2="270" stroke="{INK}"/><line x1="70" y1="270" x2="70" y2="40" stroke="{INK}"/>'
           f'<path d="M70 90 L380 90 L620 210" fill="none" stroke="{GREEN}" stroke-width="3.5"/><text x="80" y="80" fill="{GREEN_D}" font-weight="700">Available take-off thrust / power</text>'
           f'<path d="M70 230 L380 120 L620 120" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 5"/><text x="400" y="112" fill="{RED}" font-weight="700">EGT / ITT at take-off thrust → limit</text>'
           f'<line x1="380" y1="40" x2="380" y2="270" stroke="{AMBER}" stroke-dasharray="5 5"/><text x="300" y="292" fill="{AMBER}" font-weight="700">Flat-rating temperature</text>'
           f'<text x="560" y="292">OAT →</text><text x="90" y="250" fill="{MUTED}">Below it: full rated thrust, EGT margin shrinks as OAT rises</text>'
           f'<text x="400" y="240" fill="{MUTED}">Above it: thrust reduced to protect the engine</text>')
    return svgfig(svg, "Flat rating", "Typical flat-rating behaviour (illustrative): thrust is constant up to the flat-rating temperature while the EGT/ITT margin shrinks; above it, available thrust falls. Values per engine type: AFM/FCOM/AOM.")


def obstacle_diagram():
    svg = (f'<line x1="40" y1="280" x2="660" y2="280" stroke="#7a4c26" stroke-width="5"/><rect x="40" y="272" width="170" height="8" fill="#3b4540"/>'
           f'<path d="M210 280 L330 245 L660 120" fill="none" stroke="{GREEN}" stroke-width="3.5"/><text x="470" y="148" fill="{GREEN_D}" font-weight="700" transform="rotate(-21 470 148)">Gross flight path (one engine out)</text>'
           f'<path d="M210 280 L330 255 L660 160" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="9 5"/><text x="470" y="205" fill="{BLUE}" font-weight="700" transform="rotate(-17 470 205)">Net flight path (gross − 0.8 %)</text>'
           f'<path d="M540 280 L556 222 L572 280z" fill="#5d6b63"/><line x1="556" y1="222" x2="556" y2="190" stroke="{RED}" marker-end="url(#hwa)" marker-start="url(#hwa)"/>'
           f'<text x="566" y="214" fill="{RED}" font-weight="700">≥ 35 ft</text><text x="508" y="300">obstacle</text>'
           f'<text x="50" y="40" font-weight="700">Two-engine aeroplane, one engine inoperative</text>'
           f'<text x="50" y="60" fill="{MUTED}">2nd segment gross gradient ≥ 2.4 % (CS 25.121); net path clears obstacles by ≥ 35 ft (CAT.POL.A.210)</text>')
    return svgfig(svg, "Net take-off flight path", "Obstacle clearance uses the NET flight path (for twins, the gross gradient reduced by 0.8 %). High temperature lowers the gradient: the obstacle limit can restrict the take-off mass even on a long runway.")


FLEET = """<div class="table-wrap"><table>
<tr><th>Topic</th><th>Boeing 737-800</th><th>Dash 8-Q400 / Q200</th></tr>
<tr><td>Hot weather procedures</td><td>FCOM Supplementary Procedures — Adverse Weather, hot weather operation</td><td>AFM / AOM hot weather and high-temperature limitations</td></tr>
<tr><td>Engine and APU start limits</td><td>FCOM limitations (EGT); APU start on battery</td><td>AFM engine start and ITT limits; APU or ground power as installed</td></tr>
<tr><td>Bleeds-off take-off</td><td>Bleeds-off take-off procedure and performance credit (FCOM / QRH performance)</td><td>Bleed and pack settings for take-off per AFM performance charts</td></tr>
<tr><td>Performance</td><td>Company performance software, QRH performance tables, Jetplan</td><td>AFM performance charts or company software, Jetplan</td></tr>
</table></div>"""

LESSONS = [
# 1
dict(title="High Temperature Meteorology", minutes=9,
objectives=["Describe how heat builds up during the day and in heat waves.", "Explain how heating produces convection, thunderstorms, dust devils and dust storms.", "Recognise the summer weather threats in the reports and forecasts."],
body="""
<h2>Heating and the daily cycle</h2>
<p>Over land, the temperature peaks in the <strong>afternoon</strong>, well after noon, because the ground keeps absorbing more solar radiation than it loses. The hottest — and least dense — air, and the strongest convection, come in the afternoon and early evening.</p>
""" + faa("faa-diurnal-temperature", "The daily temperature cycle over land: maximum temperature in the afternoon, minimum around sunrise.", f"{_WX}, Figure 7-8") + """
<h2>Heat waves</h2>
<ul>
  <li>A <strong>heat wave</strong> is a period of several days with temperatures well above normal, often under a stationary high-pressure system.</li>
  <li>Night temperatures stay high, so even early departures can be performance-limited. Plan for the <strong>actual</strong> temperature, not the seasonal average.</li>
  <li>Watch the TAF for <code>TX</code> (maximum temperature) groups and check the take-off and landing time against the forecast peak.</li>
</ul>
<h2>Convection and thunderstorms</h2>
<p>Strong surface heating creates rising thermals. With enough moisture and instability they grow into towering cumulus and <strong>cumulonimbus</strong> — with turbulence, windshear, microbursts, hail, lightning and sudden wind changes.</p>
""" + faa("faa-thunderstorm-lifecycle", "The thunderstorm life cycle: towering cumulus, mature stage with up- and downdrafts, dissipating stage with downdrafts.", f"{_WX}, Figure 22-2") + """
<h2>Dust devils and dust storms</h2>
<p>Over dry, hot ground, intense heating creates <strong>dust devils</strong> — small, strong whirlwinds that can affect aircraft on take-off and landing. Thunderstorm outflow can raise a wall of dust and sand — a <strong>haboob</strong> — that reduces visibility to near zero within minutes.</p>
""" + faa("faa-dust-devil", "Dust devils: a life cycle — the hot ground heats the air, which rises and starts to rotate.", f"{_WX}, Figure 16-13") + faa("faa-haboob", "A haboob: a dust storm raised by thunderstorm outflow, approaching an airfield.", f"{_WX}, Figure 18-11") + """
<h2>Summer threats in the reports</h2>
<ul>
  <li><code>DU</code> dust, <code>SA</code> sand, <code>DRSA</code> low drifting sand, <code>BLSA</code> blowing sand, <code>SS</code> / <code>DS</code> sandstorm / duststorm, <code>PO</code> dust devils.</li>
  <li><code>TS</code>, <code>CB</code>, <code>TCU</code>, gusts (<code>G</code>), and convective SIGMETs.</li>
  <li>Regional threats for our network: hot, high southern aerodromes, sand and dust in the south, and convective weather in the north in summer.</li>
</ul>
""",
takeaways=["The hottest, least dense air is in the afternoon; heat waves keep nights hot too.", "Heating drives convection: CB, windshear and microbursts.", "Dust devils and haboobs can cut visibility in minutes.", "Know the codes: DU, SA, DRSA, BLSA, SS/DS, PO, TS."],
check=dict(q="When is the air temperature over land usually highest?", options=["At noon", "In the afternoon", "At sunrise", "At midnight"], answer=1, explain="The ground keeps gaining heat until the afternoon; the maximum temperature comes after noon."),
),
# 2
dict(title="Density Altitude and Aircraft Performance", minutes=9,
objectives=["Define density altitude.", "Explain how high temperature and elevation reduce thrust, lift and climb.", "Relate indicated, true and ground speed on a hot, high runway."],
body="""
<h2>Warm air is less dense</h2>
<p>At the same pressure, warm air holds fewer molecules in the same volume than cold air. <strong>Density altitude</strong> is the altitude in the standard atmosphere at which the density equals the actual density: a hot day makes the aircraft perform as if it were much higher.</p>
""" + faa("faa-temperature-density", "Effect of temperature on density: at equal mass and pressure, a warm air parcel takes more volume — fewer molecules per volume.", f"{_WX}, Figure 8-10") + """
<h2>What high density altitude does</h2>
<ul>
  <li><strong>Less thrust or power</strong> — jets and turboprops alike (see Lesson 5: flat rating).</li>
  <li><strong>Less lift</strong> at a given true airspeed — the same indicated airspeed means a <strong>higher true airspeed and ground speed</strong>.</li>
  <li><strong>Longer</strong> take-off and landing distances and <strong>lower</strong> climb gradients.</li>
</ul>
""" + faa("faa-density-altitude-effects", "High density altitude: the same aircraft needs a longer take-off roll and climbs more slowly.", f"{_WX}, Figure 8-15") + """
<h2>Altitude and temperature together</h2>
<p>Aerodrome elevation adds to the effect of temperature. A high-elevation aerodrome on a hot afternoon is the most demanding case: the take-off distance can be far longer than at sea level.</p>
""" + faa("faa-takeoff-altitude", "Take-off distance increases with altitude: the same aeroplane needs a much longer ground roll at 8,000 ft pressure altitude.", f"{_PHAK}, Figure 12-9") + """
<div class="callout info"><span class="label">Remember</span><p>Indicated airspeed tells the wing what it needs; true airspeed and ground speed tell the runway, the tyres and the brakes what they will get. On a hot, high runway the ground speed is higher at the same V speeds.</p></div>
""",
takeaways=["Density altitude = the standard-atmosphere altitude with the actual density.", "Hot and high: less thrust and lift, longer distances, lower climb gradient.", "Same IAS → higher TAS and ground speed: more runway, tyre speed and brake energy."],
check=dict(q="What happens to the take-off distance on a hot day at a high aerodrome?", options=["It decreases", "It increases significantly", "It stays the same", "It depends only on the wind"], answer=1, explain="Lower density reduces thrust and lift and raises the ground speed: distances increase."),
),
# 3
dict(title="High Temperature Take-off Planning", minutes=9,
objectives=["Identify the limits that determine the maximum take-off mass on a hot day.", "Select thrust and configuration correctly with approved performance data.", "Cross-check the performance calculation as a crew."],
body="""
<h2>The take-off mass limits</h2>
<p>The maximum take-off mass is the <strong>lowest</strong> of several limits. On hot days, the limits based on climb and energy usually become the limiting ones:</p>
<div class="table-wrap"><table>
<tr><th>Limit</th><th>Why heat makes it critical</th></tr>
<tr><td>Field length (runway)</td><td>Longer acceleration and stopping distances</td></tr>
<tr><td>Climb (WAT — weight, altitude, temperature)</td><td>Lower one-engine-out climb gradient</td></tr>
<tr><td>Obstacle</td><td>Lower net flight path (Lesson 6)</td></tr>
<tr><td>Tyre speed</td><td>Higher ground speed at lift-off</td></tr>
<tr><td>Brake energy (VMBE)</td><td>More energy to absorb in a rejected take-off (Lesson 4)</td></tr>
<tr><td>Structural / MEL / maximum temperature</td><td>AFM maximum take-off temperature; MEL penalties (Lesson 7)</td></tr>
</table></div>
<h2>Thrust and configuration</h2>
<ul>
  <li>Use <strong>approved</strong> data: company performance software, QRH or AFM tables, Jetplan — with the <strong>actual</strong> OAT, QNH, wind, runway condition and NOTAM distances.</li>
  <li><strong>Reduced (assumed temperature / derated) thrust</strong> is allowed only within the AFM and company limits; on a hot, limiting day full thrust may be required.</li>
  <li>A higher take-off flap setting may shorten the runway required but reduces the climb gradient — the performance tool selects the optimum.</li>
  <li><strong>Bleeds-off / packs-off</strong> take-off can give a performance credit where the procedure is approved for your type.</li>
  <li>Re-calculate if the temperature rises, the runway or intersection changes, or the mass changes after the load sheet.</li>
</ul>
<h2>Crew cross-check</h2>
<p>One pilot calculates, the other checks independently: runway, intersection, temperature, QNH, wind, mass, flap, thrust and V speeds. Wrong temperature, mass or flap entries are recurring causes of tail strikes and degraded take-offs.</p>
<div class="callout"><span class="label">Fleet</span>""" + FLEET + """</div>
""",
takeaways=["MTOM = the lowest of field, climb, obstacle, tyre speed, brake energy and other limits.", "Approved data, actual conditions; full thrust when limiting.", "Independent cross-check of every performance entry."],
check=dict(q="On a hot day at an elevated aerodrome, which limits most often restrict the take-off mass?", options=["Maximum zero fuel mass", "Climb (WAT) and obstacle limits", "Cabin altitude", "Fuel tank capacity"], answer=1, explain="Reduced climb gradient makes the climb and obstacle limits critical."),
),
# 4
dict(title="Brake Energy Management", minutes=8,
objectives=["Explain why brake energy is critical in hot weather.", "Apply the brake energy limit and the brake cooling schedule.", "Manage the rejected take-off and the turnaround with hot brakes."],
body="""
<h2>Energy grows with the square of speed</h2>
<p>In a rejected take-off the brakes turn the aircraft's kinetic energy into heat. Because energy grows with the <strong>square</strong> of the ground speed, the higher ground speeds of a hot, high runway — and any tailwind or downhill slope — increase brake energy sharply.</p>
""" + brake_energy_diagram() + """
<h2>The limits</h2>
<ul>
  <li><strong>Maximum brake energy speed (VMBE)</strong>: V1 must not exceed it. The performance tool checks it; it can limit the take-off mass.</li>
  <li><strong>Brake cooling schedule</strong>: after a landing or a rejected take-off, the AFM/FCOM gives the cooling time before the next take-off. In hot air, brakes cool more slowly.</li>
  <li><strong>Fuse plugs</strong> in the wheels melt to deflate a tyre before it bursts after very high brake energy. Keep away from the wheels after a high-energy stop.</li>
</ul>
<h2>Rejected take-off</h2>
<ul>
  <li>Brief the reject criteria: at high speed, reject only for the events in your SOP (engine failure, fire, or the aircraft unsafe or unable to fly).</li>
  <li>Use maximum braking (autobrake RTO where fitted) and reverse; stop on the runway centreline.</li>
  <li>After a high-energy RTO: tell ATC, consider fire services, follow the brake cooling schedule and do not taxi back for an immediate take-off.</li>
</ul>
<h2>On the turnaround</h2>
<ul>
  <li>Avoid riding the brakes during taxi: low, steady taxi speed and short firm brake applications.</li>
  <li>Check the brake temperature indication where fitted before the next take-off.</li>
</ul>
""",
takeaways=["Brake energy ∝ speed²: heat and altitude raise it sharply.", "V1 ≤ VMBE; respect the brake cooling schedule.", "After a high-energy RTO: ATC, fire services, cooling time; keep clear of the wheels."],
check=dict(q="If the ground speed at brake application is 10 % higher, the brake energy is about:", options=["10 % higher", "21 % higher", "5 % higher", "the same"], answer=1, explain="Energy is proportional to speed squared: 1.1² ≈ 1.21."),
),
# 5
dict(title="Engine Limitations and Hot Starts", minutes=8,
objectives=["Explain flat rating and the EGT/ITT margin in hot weather.", "Recognise and prevent hot and hung starts.", "Apply engine and APU limitations on the ground in high temperatures."],
body="""
<h2>Flat rating and EGT margin</h2>
<p>Engines are <strong>flat-rated</strong>: they give their rated thrust up to a certain outside temperature. As the OAT rises, the engine runs hotter to make that thrust, and the <strong>EGT / ITT margin</strong> shrinks. Above the flat-rating temperature, available thrust falls.</p>
""" + flat_rating_diagram() + """
<h2>Hot and hung starts</h2>
<ul>
  <li><strong>Hot start</strong>: EGT/ITT rising fast towards or beyond the start limit. <strong>Hung start</strong>: the engine stabilises below idle and does not accelerate.</li>
  <li>Hot air, a tailwind into the exhaust, low battery or air-start pressure, or a slow starter make them more likely.</li>
  <li>Prevention: correct start sequence, adequate start air or electrical power, monitor the parameters and be ready to abort exactly as the QRH / AOM states.</li>
</ul>
<h2>On the ground in the heat</h2>
<ul>
  <li>Keep ground running time and high thrust to a minimum; position into wind where possible.</li>
  <li>APU limits (EGT, load) are also closer — use ground power and conditioned air where available.</li>
  <li>Watch avionics and equipment cooling cautions on long ground times.</li>
</ul>
""",
takeaways=["Flat rating: thrust constant up to a temperature, EGT margin shrinking; above it thrust falls.", "Hot and hung starts: know the signs and the abort procedure.", "Minimise ground running; use ground power and conditioned air."],
check=dict(q="What happens to the EGT/ITT margin as the outside air temperature rises?", options=["It increases", "It decreases", "It stays the same", "It only changes in cruise"], answer=1, explain="The engine runs hotter to produce rated thrust in hot air: the margin shrinks."),
),
# 6
dict(title="Climb Gradient and Obstacle Assessment", minutes=9,
objectives=["Describe the one-engine-out take-off flight path and its segments.", "Explain gross and net flight paths and obstacle clearance.", "Assess performance-limited departures and the engine-out procedure."],
body="""
<h2>The one-engine-out take-off flight path</h2>
<ul>
  <li>The certified take-off path assumes an engine failure at V1 and continues to at least 1,500 ft above the runway.</li>
  <li>The <strong>second segment</strong> (gear up, take-off flaps, V2) is usually the most demanding: for a twin, the gross gradient must be at least <strong>2.4 %</strong> (CS 25.121).</li>
  <li>High temperature reduces the gradient — so the climb limit and the obstacle limit can restrict the mass.</li>
</ul>
""" + obstacle_diagram() + """
<h2>Obstacle clearance</h2>
<ul>
  <li>The <strong>net</strong> flight path is the gross path reduced by <strong>0.8 %</strong> for twins (CS 25.115). It must clear every obstacle in the departure funnel by at least <strong>35 ft</strong> (CAT.POL.A.210).</li>
  <li>The performance software uses the aerodrome obstacle data. A <strong>NOTAM</strong> about a new obstacle (crane) or a reduced runway changes the result.</li>
</ul>
<h2>Performance-limited departures</h2>
<ul>
  <li>Brief the <strong>engine-out procedure</strong> (EOSID) if the company publishes one — it may differ from the standard departure.</li>
  <li>Brief acceleration altitude, turn points and the return or take-off alternate plan.</li>
  <li>In hot weather the all-engines climb is also lower — check SID climb gradients and noise procedures against the expected performance.</li>
</ul>
""",
takeaways=["Second segment is the critical one: twin gross gradient ≥ 2.4 %.", "Net path = gross − 0.8 % (twin); clears obstacles by ≥ 35 ft.", "Brief the EOSID; check obstacle NOTAMs and SID gradients."],
check=dict(q="How much must the net take-off flight path clear obstacles by?", options=["0 ft", "35 ft", "500 ft", "1,000 ft"], answer=1, explain="CAT.POL.A.210: at least 35 ft vertically."),
),
# 7
dict(title="MEL and CDL in Hot Weather", minutes=7,
objectives=["Identify MEL and CDL items that reduce performance margins.", "Apply penalties and operational procedures correctly in high temperatures.", "Decide whether to dispatch when margins are already small."],
body="""
<h2>Items that cost performance</h2>
<ul>
  <li><strong>Performance penalties</strong>: some MEL items (for example anti-skid, a bleed or pack item, a thrust reverser, a spoiler) carry mass or V-speed penalties or require a longer runway.</li>
  <li><strong>CDL items</strong> (missing panels or seals) add drag: a climb-gradient penalty that matters most on a hot day.</li>
  <li><strong>Cooling items</strong>: a pack, avionics cooling or APU item can make a hot ground time very difficult.</li>
</ul>
<h2>Apply the procedure in full</h2>
<ul>
  <li>Read every item in full, including the <strong>(M) maintenance</strong> and <strong>(O) operational</strong> procedures, placards and conditions.</li>
  <li>Combine penalties: two "small" penalties together on a hot, high runway can make the take-off impossible at the planned mass.</li>
  <li>Hot fuel is less dense: convert uplift with the actual density, and respect MEL fuel minimums.</li>
</ul>
<div class="callout info"><span class="label">Example from the company LOFT — B737-800, MEL 28-01-03-01</span>
<p>A main tank aft fuel boost pump may be inoperative provided that both main tank forward pumps operate normally; at the start of take-off the associated tank holds not less than 7,500 lb (3,402 kg); a minimum of 2,500 lb (1,134 kg) is maintained in that tank; and the pump is deactivated. Always use the current MEL — this example is for training only.</p></div>
<h2>The dispatch decision</h2>
<p>If the margins are already small, consider: a cooler departure time, an offload of payload or fuel (with a fuel stop if needed), another runway, or not dispatching. The commander has the final word.</p>
""",
takeaways=["MEL/CDL items can add mass, speed or drag penalties — critical in heat.", "Read (M) and (O) procedures in full; combine all penalties.", "Small margins: cooler time, offload, other runway — or do not dispatch."],
check=dict(q="Why are CDL items more critical on a hot day?", options=["They make the cabin hotter", "Their drag penalty reduces an already lower climb gradient", "They increase fuel density", "They are not relevant"], answer=1, explain="CDL drag reduces climb gradient, which is already reduced by temperature."),
),
# 8
dict(title="CRM in Performance-Limited Operations", minutes=7,
objectives=["Apply CRM skills when performance margins are small.", "Use briefings and callouts to share the performance picture.", "Resist commercial and time pressure."],
body="""
<h2>Shared mental model</h2>
<ul>
  <li>Both pilots must know <strong>what limits the take-off today</strong> (field, climb, obstacle, brake energy) and by how much.</li>
  <li>Brief the critical items: V1 and reject criteria, engine-out procedure, acceleration altitude, return plan.</li>
</ul>
<h2>Communication and assertiveness</h2>
<ul>
  <li>Any change — temperature, intersection, wind, mass — is announced and re-checked, not absorbed silently.</li>
  <li>The PM monitors the performance-related callouts and speaks up if something does not fit (speed, runway remaining, rotation).</li>
  <li>Use the company escalation: question → state the concern → propose an action → refuse if unsafe.</li>
</ul>
<h2>Pressure and decision-making</h2>
<ul>
  <li>Performance-limited days create pressure to "make it work": offloading cargo, delaying, or changing runway costs time.</li>
  <li>Use a structured decision model (for example: facts — options — risks — decision — review) and involve the dispatcher and the cabin crew.</li>
  <li>A delayed, legal, safe departure is always the right outcome.</li>
</ul>
""",
takeaways=["Both pilots know today's limiting factor and margin.", "Announce and re-check every change; speak up.", "Use a decision model; resist commercial pressure."],
check=dict(q="The temperature rises by 4 °C during the boarding of a performance-limited flight. What should the crew do?", options=["Nothing, it is small", "Announce it and recalculate the performance", "Take off faster", "Ask ATC"], answer=1, explain="Any change to the inputs must be announced and the performance recalculated."),
),
# 9
dict(title="Situation Awareness in Hot Weather Operations", minutes=7,
objectives=["Maintain awareness of the environment, runway and performance margins.", "Recognise the cues that the margins are being eroded.", "Plan ahead for diversion, go-around and convective weather."],
body="""
<h2>The three levels</h2>
<ol class="steps">
  <li><strong>Perceive</strong>: actual OAT and wind, ATIS changes, NOTAMs, runway condition (sand, rubber, heat), cells on the radar.</li>
  <li><strong>Understand</strong>: what these mean for today's take-off and landing margins.</li>
  <li><strong>Project</strong>: what happens if the temperature rises further, a cell drifts onto the departure path, or the destination closes with dust.</li>
</ol>
<h2>Cues that margins are eroding</h2>
<ul>
  <li>Slow acceleration on the take-off roll; slow climb after lift-off.</li>
  <li>Rising temperature or a wind shift to a tailwind before departure.</li>
  <li>Long float in the flare; higher ground speed than expected on approach.</li>
  <li>Visibility trending down in dust; gust spreads increasing.</li>
</ul>
<h2>Plan ahead</h2>
<ul>
  <li>Go-around: in hot, high conditions the climb is lower — brief the missed approach and its gradient.</li>
  <li>Alternates: check that the alternate is not affected by the same dust or convective system.</li>
  <li>Fuel: extra fuel for weather deviations and holding when convection is forecast.</li>
</ul>
""",
takeaways=["Perceive — understand — project.", "Slow acceleration, tailwind shift, long float and falling visibility are warning cues.", "Brief the go-around; choose an alternate outside the same weather."],
check=dict(q="Which is a cue that take-off margins are being eroded?", options=["A headwind increase", "Slower than expected acceleration on the take-off roll", "A lower temperature", "A longer runway"], answer=1, explain="Slow acceleration indicates less margin than planned."),
),
# 10
dict(title="Human Performance Limitations in High Temperature", minutes=7,
objectives=["Describe the effects of heat stress and dehydration on the body.", "Explain their effect on attention, memory and decision-making.", "Apply countermeasures for crews on hot days."],
body="""
<h2>Heat stress and dehydration</h2>
<ul>
  <li>In hot flight decks and on hot aprons, the body loses water through sweat. Thirst comes <strong>late</strong>: by the time you feel thirsty you are already dehydrated.</li>
  <li>Even mild dehydration (about 2 % of body weight) is associated with reduced concentration, slower reactions and more errors.</li>
  <li>Signs: headache, fatigue, dizziness, irritability, dark urine; more serious: cramps, nausea, confusion (heat exhaustion, heat stroke).</li>
</ul>
<h2>Effects on performance</h2>
<ul>
  <li><strong>Attention narrows</strong>; monitoring and cross-checks suffer.</li>
  <li><strong>Working memory</strong> is reduced: more slips in data entry (performance, FMS, load sheet).</li>
  <li><strong>Decision-making</strong> becomes slower and more prone to bias; fatigue builds faster on long, hot duty days.</li>
</ul>
<h2>Countermeasures</h2>
<ul>
  <li>Drink water regularly before and during the duty, even without thirst; limit caffeine and avoid heavy meals before flight.</li>
  <li>Cool the flight deck early (ground air, APU, packs); use sun visors; dress for the heat on the walk-around.</li>
  <li>Use checklists and cross-checks deliberately; tell the other pilot if you feel unwell.</li>
  <li>Fatigue: report it through the company system (OM A FTL chapter).</li>
</ul>
""",
takeaways=["Thirst comes late; ~2 % dehydration already degrades performance.", "Heat narrows attention, reduces memory and slows decisions.", "Drink regularly, cool the flight deck, cross-check deliberately, report fatigue."],
check=dict(q="When should crews drink water on a hot duty day?", options=["Only when thirsty", "Regularly, before and during the duty", "Only after landing", "Never in flight"], answer=1, explain="Thirst comes late; drink regularly."),
),
# 11
dict(title="Flight Safety Trends — Summer Season", minutes=8,
objectives=["Review the flight safety events typical of the summer season.", "Apply the prevention for each event.", "Report events through the safety reporting system."],
body="""
<h2>Summer focus items</h2>
<div class="table-wrap"><table>
<tr><th>Event</th><th>Why it matters</th><th>Prevention</th></tr>
<tr><td><strong>Runway excursion</strong></td><td>High ground speed, long float, tailwind, sand on the runway</td><td>Stabilised approach to the aiming point; go around if a long landing develops</td></tr>
<tr><td><strong>High taxi speed</strong></td><td>Hot brakes, reduced margins, passenger injury</td><td>Company taxi speeds; short firm braking, never riding the brakes</td></tr>
<tr><td><strong>Wrong flap, ZFW, fuel or temperature entries</strong></td><td>Wrong speeds and trim: tail strike, degraded take-off</td><td>Independent cross-check by both pilots</td></tr>
<tr><td><strong>Hard and bounced landings</strong></td><td>Structural damage, injuries</td><td>Correct flare; bounced-landing technique; go around if in doubt; report</td></tr>
<tr><td><strong>Turbulence and windshear near convective weather</strong></td><td>Injuries, loss of control</td><td>Wide avoidance; seat belts on; windshear escape when required</td></tr>
<tr><td><strong>Use of reverse and APU</strong></td><td>Company reminder note</td><td>Apply the reminder note exactly as published</td></tr>
</table></div>
<h2>Reporting</h2>
<ul>
  <li>Report events and near-misses through the safety reporting system, under a just culture.</li>
  <li>Read the latest company safety notes and discuss them with the TRI/TRE before the summer simulator session (mandatory exercises: upset recovery, windshear, TCAS, EGPWS, pilot incapacitation).</li>
</ul>
""",
takeaways=["Runway excursions: stabilised approach, go around from a long landing.", "Moderate taxi speeds; cross-check flap, ZFW, fuel and temperature entries.", "Avoid convective weather widely; report every event."],
check=dict(q="What is the safest action when a long landing develops after a floated flare?", options=["Push the nose down", "Go around", "Use only reverse thrust", "Extend more flap"], answer=1, explain="If a long landing develops, go around."),
),
]


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


QUESTIONS = [
Q(1, "Over land, the maximum temperature of the day usually occurs:", ["Around sunrise", "At noon exactly", "In the afternoon", "At midnight"], 2, "The ground keeps heating until the afternoon."),
Q(1, "What is a haboob?", ["A sea breeze", "A dust storm raised by thunderstorm outflow", "A type of fog", "A cold front"], 1, "A haboob is a wall of dust driven by convective outflow."),
Q(1, "What does PO mean in a METAR?", ["Pollen", "Dust devils", "Rain showers", "Smoke"], 1, "PO = dust/sand whirls (dust devils)."),
Q(1, "What does DRSA in a METAR mean?", ["Dry runway", "Low drifting sand", "Drizzle", "Dust storm"], 1, "DRSA = low drifting sand."),
Q(2, "Density altitude is:", ["The height above the runway", "The standard-atmosphere altitude with the same air density as now", "The cabin altitude", "The pressure altitude minus elevation"], 1, "It expresses the actual density as an equivalent altitude."),
Q(2, "At high density altitude, the same IAS gives:", ["A lower ground speed", "A higher true airspeed and ground speed", "The same TAS", "More lift"], 1, "Lower density: higher TAS for the same IAS."),
Q(2, "Hot and high conditions:", ["Increase thrust", "Reduce thrust, lift and climb gradient", "Shorten distances", "Have no effect on jets"], 1, "All performance reduces."),
Q(3, "The maximum take-off mass is:", ["The highest of the limits", "The lowest of the applicable limits", "Always the structural limit", "Chosen by ATC"], 1, "The most restrictive limit decides."),
Q(3, "Which data must be used for take-off performance?", ["Rules of thumb", "Approved data with actual conditions", "Last flight's figures", "ATC estimates"], 1, "Approved data with actual OAT, QNH, wind and runway condition."),
Q(3, "What must be done if the temperature rises after the calculation?", ["Nothing", "Recalculate the performance", "Increase V1 by 5 kt", "Use flaps 40"], 1, "Any change in inputs requires a recalculation."),
Q(3, "Wrong ZFW or temperature entries can cause:", ["Better performance", "Wrong speeds and trim — tail strike or degraded take-off", "Nothing", "A fuel leak"], 1, "Cross-check every entry."),
Q(4, "Brake energy is proportional to:", ["Speed", "Speed squared", "Temperature", "Altitude only"], 1, "Kinetic energy = ½ m V²."),
Q(4, "V1 must not exceed:", ["VR", "VMBE (maximum brake energy speed)", "VREF", "VMO"], 1, "V1 ≤ VMBE."),
Q(4, "After a high-energy rejected take-off you should:", ["Taxi back and take off at once", "Inform ATC, consider fire services, follow the brake cooling schedule", "Set the parking brake hard", "Walk to the wheels to check them"], 1, "Hot brakes: cooling time, keep clear of the wheels."),
Q(4, "What do wheel fuse plugs do?", ["Increase brake power", "Melt to deflate the tyre before it bursts", "Cool the brakes", "Measure tyre pressure"], 1, "They release pressure after very high brake temperature."),
Q(5, "A flat-rated engine:", ["Gives more thrust when hot", "Gives rated thrust up to a temperature, with a shrinking EGT margin", "Has no EGT limit", "Is only on turboprops"], 1, "Thrust constant up to the flat-rating temperature."),
Q(5, "A hung start is:", ["A start that exceeds the EGT limit", "A start that stabilises below idle and does not accelerate", "A normal start", "A start on battery"], 1, "It hangs below idle."),
Q(5, "On a hot apron you should:", ["Keep the APU at maximum load all day", "Minimise ground running; use ground power and conditioned air", "Run engines at high thrust to cool them", "Ignore cooling cautions"], 1, "Protect engines, APU and avionics."),
Q(6, "Minimum second-segment gross gradient for a two-engine aeroplane:", ["1.2 %", "2.4 %", "3.3 %", "5 %"], 1, "CS 25.121: 2.4 % for twins."),
Q(6, "For a twin, the net flight path is the gross path reduced by:", ["0.5 %", "0.8 %", "1.0 %", "2.4 %"], 1, "CS 25.115: 0.8 % for two-engine aeroplanes."),
Q(6, "A NOTAM reports a new crane in the departure path. What changes?", ["Nothing", "The obstacle analysis — the limiting mass may decrease", "Only the fuel", "Only the SID name"], 1, "New obstacles change the obstacle limit."),
Q(6, "What is an EOSID?", ["An engine-out standard instrument departure / procedure", "A noise procedure", "An approach", "An ATC clearance"], 0, "The engine-out procedure, which may differ from the SID."),
Q(7, "Why are CDL items more critical in heat?", ["They cool the cabin", "Their drag penalty reduces an already lower climb gradient", "They change fuel density", "They do not matter"], 1, "Drag penalties add up with temperature."),
Q(7, "When applying an MEL item you must:", ["Read only the title", "Read and apply it in full, including (M) and (O) procedures", "Ignore placards", "Ask the passengers"], 1, "Apply every condition."),
Q(7, "Margins are very small on a hot afternoon. Options include:", ["Take off anyway", "A cooler departure time, offload, another runway — or not dispatching", "Ignore the limits", "Use a rolling take-off only"], 1, "The commander decides with all options."),
Q(8, "In a performance-limited operation, both pilots should know:", ["Only the flight number", "Today's limiting factor and the margin", "Only the fuel", "The passenger count"], 1, "Shared mental model."),
Q(8, "The temperature rises during boarding. The PM should:", ["Stay silent", "Announce it so the performance is recalculated", "Increase thrust", "Call the cabin"], 1, "Announce and re-check changes."),
Q(9, "Which is a cue that margins are eroding?", ["A cooler temperature", "Slow acceleration on the take-off roll", "A headwind increase", "A longer runway"], 1, "Slow acceleration = less margin."),
Q(9, "When choosing an alternate on a summer day, check that it is:", ["The nearest only", "Not affected by the same dust or convective system", "Always the departure aerodrome", "Unlit"], 1, "Avoid the same weather system."),
Q(10, "Mild dehydration of about 2 % of body weight:", ["Has no effect", "Can reduce concentration and slow reactions", "Improves alertness", "Only affects passengers"], 1, "Performance degrades early."),
Q(10, "Which is a sign of dehydration?", ["Clear urine", "Headache, fatigue, dizziness", "Better memory", "Cold hands only"], 1, "Headache, fatigue, dizziness, dark urine."),
Q(11, "The best prevention of a runway excursion after a long float is:", ["Push the nose down", "Go around", "Maximum reverse only", "Extend flaps"], 1, "Go around when a long landing develops."),
Q(11, "Which exercises are mandatory in the summer simulator session?", ["Only stalls", "Upset recovery, windshear, TCAS, EGPWS and pilot incapacitation", "Only circling", "Only engine fire"], 1, "These are mandatory."),
]

COURSE = dict(
    slug="hot-weather-operations",
    title="Hot Weather Operations",
    header_title="Hot Weather Operations",
    tagline="Summer and hot weather operations for all fleets: meteorology, density altitude and performance, take-off planning, brake energy, engines, obstacles, MEL, CRM, situation awareness, human performance and safety trends.",
    purpose="Prepare all flight crews (B737-800, Q400 and Q200) to operate safely and efficiently in high temperatures, following the company hot weather syllabus, ICAO Annex 6 and EASA CS-25 / Part-CAT performance principles.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Recognise high temperature weather threats", "Explain density altitude and its effect on performance", "Plan high temperature take-offs with approved data",
                "Manage brake energy and rejected take-offs", "Respect engine limitations and prevent hot starts", "Assess climb gradient and obstacle clearance",
                "Apply MEL/CDL penalties in hot weather", "Use CRM and situation awareness when margins are small", "Manage heat stress and dehydration", "Prevent the summer flight safety events"],
    icon="sun", cert_prefix="HWO", quiz_count=15, pass_mark=80,
    group="refresher", season="Summer",
    finale=None,
    modules=[dict(title="Weather and Performance", summary="Meteorology, density altitude and high temperature take-off planning", icon="sun", lessons=range(1, 4)),
             dict(title="Aircraft Limitations", summary="Brake energy, engines, climb gradient and obstacles, MEL/CDL", icon="gear", lessons=range(4, 8)),
             dict(title="Human Factors and Safety", summary="CRM, situation awareness, human performance and summer safety trends", icon="people", lessons=range(8, 12))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Thunderstorm building over a hot plain", "Heating drives convection, dust devils and dust storms."),
            2: ("gen", "Airliner taking off over a desert aerodrome in the heat", "Hot and high: less density, less thrust, longer distances."),
            3: ("gen", "Airliner lined up on a hot runway with heat haze", "The lowest limit decides the take-off mass."),
            4: ("gen", "Airliner on a hot apron with heat haze", "Brake energy grows with the square of speed."),
            5: ("gen", "Airliner cruising over the desert", "Flat rating: the EGT margin shrinks as the temperature rises."),
            6: ("gen", "Airliner climbing away over mountains", "The net flight path must clear every obstacle."),
            7: ("gen", "Two pilots on the flight deck at dusk", "Combine every MEL and CDL penalty."),
            8: ("gen", "Two pilots on the flight deck", "Both pilots know today's limiting factor."),
            9: ("gen", "Dust storm approaching an aerodrome", "Perceive, understand, project."),
            10: ("gen", "Flight deck in bright sun", "Thirst comes late: drink regularly."),
            11: ("gen", "Airliner landing on a sunny runway", "Stabilised approach — go around from a long landing.")},
)
