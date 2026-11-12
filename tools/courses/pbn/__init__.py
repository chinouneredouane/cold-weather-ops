"""W3 — PBN Refresher (winter season), all fleets. Built on ICAO Doc 9613 (PBN Manual), Doc 8168 (PANS-OPS),
EASA Part-CAT and Part-SPA (SPA.PBN, specific approval for RNP AR APCH only) and AMC 20-27/28."""
from courses.upset_recovery.diagrams import FONT, INK, MUTED, GREEN, GREEN_D, RED, AMBER, BLUE


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


def containment():
    svg = f"""
<rect x="40" y="70" width="620" height="160" rx="8" fill="{AMBER}" opacity=".12"/>
<rect x="40" y="110" width="620" height="80" rx="8" fill="{GREEN}" opacity=".18"/>
<line x1="40" y1="150" x2="660" y2="150" stroke="{GREEN_D}" stroke-width="3"/>
<path d="M60 160 Q200 132 340 155 T660 146" stroke="{BLUE}" stroke-width="3" fill="none"/>
<path d="M100 140 l20 -4 l6 -6 l4 2 l-3 6 l16 -1 l2 3 l-16 2 l-2 7 l-4 0 l-1 -6 l-20 2z" fill="{INK}"/>
<text x="670" y="154" fill="{GREEN_D}" font-weight="700">desired path</text>
<text x="670" y="118" fill="{GREEN_D}">± RNP value (95 %)</text>
<text x="670" y="78" fill="{AMBER}">± 2 × RNP</text>
<text x="40" y="40" font-weight="700" font-size="14">RNP: the aircraft must stay within ± the RNP value at least 95 % of the flight time —</text>
<text x="40" y="58" fill="{MUTED}">and an RNP system must monitor its own performance and alert the crew when it cannot.</text>
<text x="40" y="260" fill="{BLUE}">actual flight path = path definition error + flight technical error + navigation system error</text>"""
    return f"""<figure class="diagram"><svg viewBox="0 0 820 280" role="img" aria-label="RNP containment"><title>RNP lateral performance</title>
<desc>The desired path with a band of plus or minus the RNP value, and an outer band of two times RNP.</desc>
<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg>
<figcaption>Total system error combines the path definition, flight technical and navigation system errors. On-board performance monitoring and alerting is what makes a specification “RNP”.</figcaption></figure>"""


LESSONS = [
dict(title="The PBN Concept", minutes=7,
objectives=["Explain the performance-based navigation (PBN) concept.", "Distinguish RNAV and RNP specifications.", "Identify the elements of a PBN operation."],
body="""
<h2>From sensors to performance</h2>
<p>Conventional navigation is based on flying to and from ground beacons (VOR, NDB). <strong>Performance-based navigation (PBN)</strong> (ICAO Doc 9613) defines instead the <strong>performance</strong> an aircraft's area navigation system must achieve — accuracy, integrity, continuity and functionality — for a given airspace or procedure.</p>
<p>A PBN operation has three elements:</p>
<ul>
  <li>the <strong>navigation specification</strong> — the aircraft, system and crew requirements;</li>
  <li>the <strong>navaid infrastructure</strong> — GNSS, DME/DME, VOR/DME;</li>
  <li>the <strong>navigation application</strong> — the routes and procedures designed for it.</li>
</ul>

<h2>RNAV and RNP</h2>
""" + containment() + """
<ul>
  <li>An <strong>RNAV</strong> specification has no requirement for on-board performance monitoring and alerting.</li>
  <li>An <strong>RNP</strong> specification <strong>requires on-board performance monitoring and alerting</strong> — the system tells the crew when it cannot meet the required performance (for example “UNABLE REQD NAV PERF – RNP” or a similar alert).</li>
  <li>The number (e.g. RNP 1) is the lateral accuracy in nautical miles that must be achieved at least 95 % of the flight time.</li>
</ul>

<h2>Navigation specifications</h2>
<div class="table-wrap"><table>
<tr><th>Phase</th><th>Typical specifications</th></tr>
<tr><td>Oceanic / remote</td><td>RNAV 10, RNP 4, RNP 2</td></tr>
<tr><td>En route continental</td><td>RNAV 5 (B-RNAV), RNAV 2, RNP 2, Advanced RNP</td></tr>
<tr><td>Terminal (SID / STAR)</td><td>RNAV 1, RNP 1, Advanced RNP</td></tr>
<tr><td>Approach</td><td>RNP APCH (LNAV, LNAV/VNAV, LP, LPV), RNP AR APCH</td></tr>
</table></div>
<p>The aircraft's <strong>AFM / AFM supplement</strong> states which specifications it is certified for, and the <strong>MEL</strong> gives the dispatch requirements. Check your fleet's capabilities in the OM B.</p>
""",
takeaways=["PBN = navigation specification + navaid infrastructure + navigation application.", "RNP requires on-board performance monitoring and alerting; RNAV does not.", "RNP 1 = ±1 NM at least 95 % of the time.", "Fleet capability: AFM, OM B and MEL."],
check=dict(q="What distinguishes an RNP specification from an RNAV specification?", options=["A smaller number", "On-board performance monitoring and alerting", "The use of VOR", "Autopilot coupling"], answer=1, explain="RNP requires on-board performance monitoring and alerting."),
),

dict(title="GNSS, Integrity and the Navigation Database", minutes=7,
objectives=["Explain GNSS integrity monitoring and its limits.", "Recognise GNSS interference threats.", "Check and use the navigation database correctly."],
body="""
<h2>GNSS and integrity</h2>
<ul>
  <li>Most PBN operations rely on <strong>GNSS</strong>. Integrity is provided by <strong>receiver autonomous integrity monitoring (RAIM)</strong> or equivalent aircraft-based augmentation, and by satellite-based augmentation (SBAS) where available.</li>
  <li>Check the <strong>GNSS NOTAMs</strong> and the predicted RAIM availability for the route and the time of the approach, as the company procedure requires.</li>
  <li>Know the backup: DME/DME or IRS updating, and conventional procedures and navaids.</li>
</ul>

<h2>GNSS interference</h2>
<p><strong>Jamming</strong> (signal blocked) and <strong>spoofing</strong> (false signal) are increasingly common in some regions. Effects include loss of GNSS position, position or time jumps, EGPWS terrain alerts, ADS-B and clock errors. Follow the company and manufacturer guidance: cross-check position with other sources, consider deselecting GNSS where the procedure allows, use conventional navaids, inform ATC and report.</p>

<h2>The navigation database</h2>
<ul>
  <li>Check the <strong>AIRAC cycle</strong> is current before flight.</li>
  <li>Procedures must be <strong>loaded from the database</strong> by name — never built manually from waypoints for an RNP approach.</li>
  <li>Cross-check the loaded procedure with the chart: waypoint sequence, tracks, distances, altitude and speed constraints, and the vertical path angle on the final approach.</li>
  <li>Do not modify the final approach segment of an RNP approach (except where your procedure allows specific changes).</li>
</ul>
""",
takeaways=["Check GNSS NOTAMs and RAIM / integrity availability.", "Jamming and spoofing: cross-check, use conventional navaids, inform ATC and report.", "Current AIRAC; load procedures by name; cross-check with the chart; do not modify the final approach."],
check=dict(q="How must an RNP approach be loaded in the FMS?", options=["Built from individual waypoints", "Loaded by name from the current navigation database and cross-checked with the chart", "Copied from the previous flight", "Entered as a direct-to"], answer=1, explain="RNP approaches must be loaded from the database and checked against the chart."),
),

dict(title="RNAV Departures, Arrivals and En-route Operations", minutes=6,
objectives=["Fly RNAV SIDs and STARs correctly.", "Apply flight technical error limits.", "Manage contingencies on RNAV routes."],
body="""
<h2>Before departure</h2>
<ul>
  <li>Check that the aircraft and crew are approved and the equipment required by the MEL is operational.</li>
  <li>Load and cross-check the SID: waypoints, fly-by and fly-over points, altitude and speed constraints.</li>
  <li>Brief the procedure and any changes that ATC may give (e.g. direct-to clearances).</li>
</ul>

<h2>Flying the procedure</h2>
<ul>
  <li>Use the lateral navigation mode (LNAV) and the flight director or autopilot, as the SOP requires, to keep the <strong>flight technical error</strong> small — typically within half the navigation accuracy (for RNAV 1 / RNP 1: within 0.5 NM).</li>
  <li>Monitor the cross-track deviation and the navigation performance indications.</li>
  <li>Respect the published altitude and speed constraints — they are part of the procedure.</li>
</ul>

<h2>Contingencies</h2>
<ul>
  <li>If the navigation performance cannot be met (alert, loss of GNSS, system failure), <strong>inform ATC</strong> — “unable RNAV due equipment” or the appropriate phrase — and request an alternative clearance.</li>
  <li>Follow the QRH / FCOM procedure for the navigation failure.</li>
  <li>Report the event.</li>
</ul>
""",
takeaways=["Load and cross-check the SID or STAR, including constraints.", "Keep flight technical error within half the navigation accuracy.", "If performance is lost, tell ATC and request another clearance."],
check=dict(q="On an RNAV 1 SID, the lateral flight technical error should normally be kept within:", options=["0.1 NM", "0.5 NM", "2 NM", "5 NM"], answer=1, explain="Typically within half the navigation accuracy: 0.5 NM for RNAV 1."),
),

dict(title="RNP Approaches: LNAV, LNAV/VNAV, LPV", minutes=8,
objectives=["Distinguish the RNP APCH minima lines.", "Apply the temperature limits for baro-VNAV.", "Fly RNP approaches with the correct technique and go-around criteria."],
body="""
<h2>Minima lines on an RNP chart</h2>
<div class="table-wrap"><table>
<tr><th>Minima</th><th>Guidance</th><th>Type</th></tr>
<tr><td>LNAV</td><td>Lateral only — flown with CDFA to an MDA</td><td>2D</td></tr>
<tr><td>LNAV/VNAV</td><td>Lateral + barometric vertical guidance (baro-VNAV) to a DA</td><td>3D</td></tr>
<tr><td>LP</td><td>Lateral SBAS guidance to an MDA</td><td>2D</td></tr>
<tr><td>LPV</td><td>Lateral + vertical SBAS guidance to a DA</td><td>3D</td></tr>
</table></div>
<p>Use only the minima line your aircraft is certified and the company is authorised for. In EASA rules, <strong>RNP APCH</strong> (LNAV, LNAV/VNAV, LP, LPV) does not need a specific approval, but crews must be trained; <strong>RNP AR APCH</strong> requires a specific approval (SPA.PBN).</p>

<h2>Temperature and baro-VNAV</h2>
<ul>
  <li>In cold air, the baro-VNAV path is <strong>lower and shallower</strong> than published; in hot air it is higher and steeper.</li>
  <li>Charts with LNAV/VNAV minima state a <strong>temperature limit</strong> — below it, LNAV/VNAV must not be used (use LNAV minima or another approach).</li>
  <li>Check the aerodrome temperature against the chart before every LNAV/VNAV approach.</li>
</ul>

<h2>Technique</h2>
<ul>
  <li>Brief the approach with the chart and the FMS: minima, vertical path angle, temperature limit, missed approach.</li>
  <li>Be stabilised by the company gates; use the autopilot and the appropriate vertical mode as your SOP requires.</li>
  <li>Monitor lateral and vertical deviations. Go around if the deviation limits in your SOP are exceeded, or on any navigation alert (e.g. loss of integrity) — unless the required visual references are established.</li>
  <li>The missed approach is part of the RNP procedure — fly it in LNAV as published.</li>
</ul>
""",
takeaways=["LNAV and LP = 2D to an MDA; LNAV/VNAV and LPV = 3D to a DA.", "RNP APCH: no specific EASA approval but training required; RNP AR: specific approval.", "Respect the chart temperature limit for baro-VNAV.", "Go around on excessive deviation or navigation alert."],
check=dict(q="The OAT is below the minimum temperature published for LNAV/VNAV on the chart. What do you do?", options=["Fly LNAV/VNAV anyway", "Do not use LNAV/VNAV minima — use LNAV or another approach", "Increase the DA by 50 ft", "Fly faster"], answer=1, explain="Below the temperature limit the baro-VNAV path is not protected."),
),

dict(title="Approvals, MEL and Crew Responsibilities", minutes=5,
objectives=["Identify the approvals and documents for PBN operations.", "Apply the MEL to navigation equipment.", "Summarise crew responsibilities in PBN operations."],
body="""
<h2>Documents and approvals</h2>
<ul>
  <li>The AFM states the aircraft's PBN capabilities. The OM B lists the company's PBN operations by fleet.</li>
  <li>The flight plan item 10 and item 18 (<code>PBN/</code>) codes must match the aircraft's actual capability and approvals.</li>
  <li>Specific approvals (for example RNP AR APCH) are listed in the operations specifications of the AOC.</li>
</ul>

<h2>MEL</h2>
<p>The MEL includes the dispatch requirements for systems that need a specific capability or approval — RNAV/PBN, RVSM and LVO. Check the MEL for FMS, GNSS receivers, IRS and display units before planning a PBN route or approach.</p>

<h2>Crew responsibilities</h2>
<ol class="steps">
  <li>Plan: NOTAMs, GNSS integrity, database currency, equipment and MEL.</li>
  <li>Load and cross-check procedures from the database.</li>
  <li>Fly with the required modes and monitor deviations and alerts.</li>
  <li>Act on alerts: inform ATC, apply the contingency, go around when required.</li>
  <li>Report navigation errors and GNSS interference.</li>
</ol>
""",
takeaways=["AFM + OM B + AOC specify PBN capability and approvals; flight plan codes must match.", "Check the MEL for FMS, GNSS, IRS and displays.", "Plan, load and check, fly and monitor, act on alerts, report."],
check=dict(q="Where are specific approvals such as RNP AR APCH recorded?", options=["In the AFM only", "In the operations specifications of the AOC", "In the flight plan", "On the chart"], answer=1, explain="Specific approvals appear in the operations specifications."),
),
]

QUESTIONS = [
Q(1, "Which ICAO document is the PBN Manual?", ["Doc 9613", "Doc 9574", "Doc 8168 only", "Doc 9817"], 0, "ICAO Doc 9613."),
Q(1, "What are the three elements of a PBN operation?", ["Pilot, aircraft, ATC", "Navigation specification, navaid infrastructure, navigation application", "GNSS, VOR, NDB", "FMS, autopilot, radar"], 1, "Navigation specification, navaid infrastructure and navigation application."),
Q(1, "RNP 1 means the aircraft must remain within:", ["1 NM of the path at least 95 % of the time", "1 km at all times", "0.1 NM", "10 NM"], 0, "±1 NM, 95 % of the flight time."),
Q(1, "RNAV 5 is typically used for:", ["Approaches", "En-route continental airspace", "Oceanic tracks only", "Taxi"], 1, "RNAV 5 (B-RNAV) is for continental en route."),
Q(2, "What is RAIM?", ["A radar mode", "Receiver autonomous integrity monitoring of GNSS", "A runway lighting system", "A type of chart"], 1, "RAIM monitors GNSS integrity."),
Q(2, "What is GNSS spoofing?", ["Loss of signal", "Transmission of false GNSS signals", "Satellite maintenance", "Database error"], 1, "Spoofing transmits false signals."),
Q(2, "May the final approach segment of an RNP approach be modified in the FMS?", ["Yes, freely", "No (except specific changes the procedure allows)", "Only by ATC", "Only at night"], 1, "Do not modify the final approach segment."),
Q(3, "If navigation performance cannot be met on an RNAV route, you should:", ["Continue silently", "Inform ATC and request an alternative clearance", "Turn off the FMS", "Climb"], 1, "Tell ATC and request another clearance."),
Q(3, "Are SID altitude and speed constraints part of the procedure?", ["No", "Yes — they must be respected", "Only at night", "Only for jets"], 1, "Constraints are part of the procedure."),
Q(4, "LNAV minima are:", ["3D to a DA", "2D to an MDA, flown with CDFA", "Only for SBAS", "CAT II"], 1, "LNAV is a 2D approach to an MDA."),
Q(4, "Which minima use barometric vertical guidance?", ["LNAV", "LNAV/VNAV", "LP", "Circling"], 1, "LNAV/VNAV uses baro-VNAV."),
Q(4, "In very cold air, the baro-VNAV path is:", ["Higher and steeper", "Lower and shallower", "Unchanged", "Curved"], 1, "Cold air puts the baro-VNAV path lower and shallower."),
Q(4, "Which PBN specification requires a specific approval under EASA rules?", ["RNAV 5", "RNP APCH (LNAV)", "RNP AR APCH", "RNAV 1"], 2, "RNP AR APCH requires a specific approval."),
Q(5, "Where is the PBN capability declared in the flight plan?", ["Item 7", "Items 10 and 18 (PBN/)", "Item 15 only", "It is not declared"], 1, "Items 10 and 18 (PBN/ codes)."),
Q(5, "Which document lists the dispatch requirements for FMS and GNSS failures?", ["The MEL", "The NOTAM", "The chart", "The load sheet"], 0, "The MEL."),
]

COURSE = dict(
    slug="pbn-refresher", title="PBN Refresher", header_title="PBN Refresher",
    tagline="Performance-based navigation: RNAV and RNP, GNSS integrity and interference, the navigation database, RNAV procedures and RNP approaches.",
    purpose="Refresh all flight crews' knowledge of PBN operations in line with ICAO Doc 9613 and PANS-OPS and EASA Part-CAT / Part-SPA.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200 (according to each fleet's PBN capability in the OM B).",
    objectives=["Explain the PBN concept and navigation specifications", "Manage GNSS integrity, interference and the database", "Fly RNAV SIDs, STARs and routes", "Fly RNP approaches to the correct minima", "Apply approvals, MEL and crew responsibilities"],
    icon="runway", cert_prefix="PBN", quiz_count=10, pass_mark=80, group="refresher", season="Winter", finale=None,
    modules=[dict(title="PBN Principles", summary="Concept, specifications, GNSS and the database", icon="runway", lessons=range(1, 3)),
             dict(title="PBN Operations", summary="RNAV procedures, RNP approaches, approvals and MEL", icon="plane", lessons=range(3, 6))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner following a curved RNP path", "PBN: the performance matters, not the sensor."),
            2: ("gen", "Airliner with a satellite link", "GNSS integrity — and interference — must be monitored."),
            3: ("gen", "Airliner climbing on an RNAV departure", "Fly the SID with LNAV and respect the constraints."),
            4: ("gen", "Airliner on an RNP approach to a runway", "LNAV, LNAV/VNAV or LPV: fly the minima you are authorised for."),
            5: ("gen", "Two pilots checking documents on the flight deck", "Plan, check, fly, monitor, act, report.")},
)
