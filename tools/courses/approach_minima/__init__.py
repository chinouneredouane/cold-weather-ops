"""S4 — Approaches Authorised by the Authority: Ceiling and Visibility (summer season), all fleets.
Generic content from ICAO Annex 6 (classification of instrument approach operations) and Doc 9365
(All Weather Operations), EASA CAT.OP.MPA.110 (aerodrome operating minima), CAT.OP.MPA.305 (approach ban) and
Part-SPA (SPA.LVO). The approaches each fleet may fly are in the AOC operations specifications (DACM) and OM A / OM C."""
from courses.upset_recovery.diagrams import FONT, INK, MUTED, GREEN, GREEN_D, RED, AMBER, BLUE


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


COMPANY = ('<div class="callout caution"><span class="label">Company authorisation</span><p>The approach operations each fleet is authorised for — '
           'for example CAT I only, or CAT II for a fleet and crew with the approval — are listed in the <strong>AOC operations specifications</strong> '
           'issued by the <strong>DACM</strong>. The method and values for minima are in <strong>OM A</strong>; the aerodrome minima are in <strong>OM C</strong> and the charts.</p></div>')

LESSONS = [
dict(title="Classification of Instrument Approach Operations", minutes=7,
objectives=["Classify instrument approach operations as 2D or 3D, Type A or Type B.", "State the CAT I, CAT II and CAT III criteria.", "Identify which operations need a specific approval."],
body="""
<h2>2D and 3D</h2>
<ul>
  <li><strong>2D</strong> operation — lateral guidance only (e.g. VOR, NDB, LOC, LNAV, LP), flown to an <strong>MDA/H</strong>, using the CDFA technique.</li>
  <li><strong>3D</strong> operation — lateral and vertical guidance (e.g. ILS, GLS, LNAV/VNAV, LPV), flown to a <strong>DA/H</strong>.</li>
</ul>

<h2>Type A and Type B (ICAO Annex 6, adopted by EASA)</h2>
<div class="table-wrap"><table>
<tr><th>Type</th><th>Minimum height</th><th>Category</th><th>Criteria</th></tr>
<tr><td><strong>Type A</strong></td><td>MDH or DH at or above 250 ft</td><td>—</td><td>Non-precision and some 3D approaches with higher minima</td></tr>
<tr><td rowspan="3"><strong>Type B</strong></td><td rowspan="3">DH below 250 ft</td><td>CAT I</td><td>DH not lower than 200 ft, and visibility not less than 800 m or RVR not less than 550 m</td></tr>
<tr><td>CAT II</td><td>DH lower than 200 ft but not lower than 100 ft, and RVR not less than 300 m</td></tr>
<tr><td>CAT III</td><td>DH lower than 100 ft or no DH, and RVR less than 300 m or no RVR limitation</td></tr>
</table></div>
<p>The former subdivisions CAT IIIA, IIIB and IIIC are no longer used: all are now <strong>CAT III</strong>. Operations below CAT I (CAT II, CAT III), and some operational credits, need a <strong>specific approval</strong> (EASA SPA.LVO).</p>
""" + COMPANY,
takeaways=["2D to MDA/H (CDFA); 3D to DA/H.", "Type A: 250 ft or above. Type B: below 250 ft — CAT I, II, III.", "CAT I: DH ≥ 200 ft, VIS ≥ 800 m or RVR ≥ 550 m.", "CAT II / III need a specific approval."],
check=dict(q="An ILS with a DH of 200 ft and RVR 550 m is classified as:", options=["Type A", "Type B, CAT I", "Type B, CAT II", "CAT III"], answer=1, explain="DH 200 ft and RVR 550 m are the CAT I limits, which is a Type B operation."),
),

dict(title="Aerodrome Operating Minima", minutes=7,
objectives=["Explain how aerodrome operating minima are established.", "Distinguish DA/H, MDA/H, RVR, visibility and ceiling.", "Apply take-off and circling minima."],
body="""
<h2>Establishing minima</h2>
<p>The operator establishes aerodrome operating minima (EASA CAT.OP.MPA.110) for each aerodrome, taking into account: the aircraft type and performance, the crew, the runway characteristics and lighting, the navigation and visual aids, obstacles (the OCA/H of the procedure), the type of approach and the means of reporting the weather. The minima <strong>must not be lower</strong> than those established by the State of the aerodrome, unless specifically approved.</p>

<h2>The elements</h2>
<ul>
  <li><strong>DA/H</strong> — the altitude or height at which a go-around must be started on a 3D approach if the required visual reference has not been established.</li>
  <li><strong>MDA/H</strong> — the minimum on a 2D approach (with CDFA, a go-around is started at or slightly above it as the company specifies).</li>
  <li><strong>RVR</strong> — runway visual range, measured along the runway; <strong>VIS</strong> — reported meteorological visibility.</li>
  <li><strong>CMV</strong> — converted meteorological visibility: a reported visibility converted to an RVR-equivalent value when RVR is not available, using the company table.</li>
  <li><strong>Ceiling</strong> — used mainly for <strong>planning</strong> (destination and alternate) and for circling and some non-precision approaches as the OM A specifies.</li>
</ul>

<h2>Take-off and circling</h2>
<ul>
  <li><strong>Take-off minima</strong> are expressed as RVR or visibility, sometimes with a ceiling — and depend on the runway lighting and the aircraft's ability to return or reach a take-off alternate.</li>
  <li><strong>Circling minima</strong> (MDH and visibility) depend on the aircraft approach category (A to D). Keep visual reference with the runway throughout.</li>
</ul>
""" + COMPANY,
takeaways=["Operator minima: never lower than the State's, unless approved.", "DA/H for 3D, MDA/H for 2D; RVR, VIS, CMV; ceiling mainly for planning.", "Take-off and circling minima are separate — check them."],
check=dict(q="May the operator's minima be lower than those published by the State of the aerodrome?", options=["Yes, always", "No, unless specifically approved", "Only at night", "Only for CAT I"], answer=1, explain="Minima must not be lower than the State's, unless specifically approved."),
),

dict(title="Planning Minima and the Approach Ban", minutes=6,
objectives=["Apply planning minima for destination and alternates.", "Apply the approach ban rule.", "Make the go-around decision at the minimum."],
body="""
<h2>Planning</h2>
<p>At the planning stage, the weather at the destination and the alternates must be at or above the <strong>planning minima</strong> for the expected time of use (often with a time window before and after the ETA). Planning minima for alternates are higher than the landing minima — the values are in OM A (based on CAT.OP.MPA.185 / 245).</p>

<h2>The approach ban</h2>
<div class="callout warn"><span class="label">Approach ban (EASA CAT.OP.MPA.305)</span>
<p>The commander shall not continue an approach <strong>below 1,000 ft above the aerodrome</strong> (or into the final approach segment) if the reported RVR or visibility is <strong>less than the applicable minimum</strong>. If it falls below the minimum after passing 1,000 ft, the approach may be continued to the DA/H or MDA/H.</p></div>

<h2>At the minimum</h2>
<ul>
  <li>Continue below the DA/H or MDA/H only if the <strong>required visual reference</strong> is established and can be maintained — for example elements of the approach lights, the threshold, the touchdown zone or their lights.</li>
  <li>Otherwise, go around — and fly the published missed approach.</li>
  <li>If visual reference is lost below the minimum, go around immediately.</li>
</ul>
""" + COMPANY,
takeaways=["Plan with planning minima (higher than landing minima) for destination and alternates.", "Approach ban: no continuing below 1,000 ft if reported RVR / VIS is below minima.", "Below DA/MDA only with the required visual reference."],
check=dict(q="At 1,500 ft above the aerodrome, the reported RVR drops below your minimum. What applies?", options=["Continue to the DA anyway", "The approach ban: do not continue below 1,000 ft above the aerodrome", "Land without reference", "Request CAT III"], answer=1, explain="Below 1,000 ft the approach may not be continued if the reported RVR is below the minimum."),
),

dict(title="Low-Visibility Operations Overview", minutes=6,
objectives=["Describe the requirements for CAT II and CAT III operations.", "Explain low-visibility procedures at aerodromes.", "Recognise when LVO capability is lost."],
body="""
<h2>Requirements</h2>
<ul>
  <li>A <strong>specific approval</strong> (SPA.LVO) for the operator, with the aircraft certified, the crew trained and qualified, and procedures in the Operations Manual.</li>
  <li>The aerodrome with <strong>low-visibility procedures (LVP)</strong> in force, and the required ground equipment serviceable.</li>
  <li>The aircraft equipment required for the category serviceable — check the MEL and the AFM.</li>
</ul>

<h2>Low-visibility procedures</h2>
<p>When LVP are in force, ATC protects the ILS sensitive and critical areas, increases spacing and uses specific taxi routes. Low-visibility take-off (LVTO) below the standard take-off minima also needs approval and suitable runway lighting.</p>

<h2>Loss of capability</h2>
<ul>
  <li>Aircraft failures (autopilot channels, autothrottle, displays) can downgrade the approach category — the FCOM / AOM gives the effect.</li>
  <li>Ground equipment failures can also raise the minima — see the next course on inoperative ground equipment.</li>
  <li>Fog: know the types (radiation, advection) and their trends for planning.</li>
</ul>
""" + COMPANY,
takeaways=["CAT II / III: approval, aircraft, crew, procedures, aerodrome LVP and equipment.", "LVP protect ILS areas and increase spacing.", "Aircraft or ground failures can downgrade the category."],
check=dict(q="Which is NOT required to fly a CAT II approach?", options=["Operator specific approval", "LVP in force at the aerodrome", "Trained and qualified crew", "A weather radar image of the fog"], answer=3, explain="A weather radar image is not a requirement."),
),
]

QUESTIONS = [
Q(1, "A 2D approach is flown to:", ["A DA/H", "An MDA/H, using CDFA", "No minimum", "An RVR only"], 1, "2D approaches are flown to an MDA/H."),
Q(1, "Type A approach operations have a minimum height of:", ["Below 200 ft", "250 ft or above", "100 ft", "No minimum"], 1, "Type A: MDH/DH at or above 250 ft."),
Q(1, "CAT I minimum DH:", ["100 ft", "150 ft", "200 ft", "250 ft"], 2, "CAT I: DH not lower than 200 ft."),
Q(1, "CAT I minimum RVR:", ["300 m", "550 m", "800 m", "1,500 m"], 1, "CAT I: RVR not less than 550 m (or VIS 800 m)."),
Q(1, "CAT II DH range:", ["Below 100 ft", "Below 200 ft but not below 100 ft", "250 ft and above", "200 to 250 ft"], 1, "CAT II: DH below 200 ft, not below 100 ft."),
Q(1, "Which approaches require a specific approval?", ["CAT I ILS", "CAT II and CAT III", "VOR approaches", "Circling"], 1, "Lower than CAT I needs SPA.LVO approval."),
Q(2, "What is CMV?", ["Ceiling minimum value", "Converted meteorological visibility", "Circling minimum visibility", "Category minimum variation"], 1, "CMV converts visibility to an RVR-equivalent."),
Q(2, "Circling minima depend on:", ["The runway length", "The aircraft approach category", "The fuel on board", "The time of day only"], 1, "Circling minima depend on approach category."),
Q(3, "What is the approach ban height?", ["500 ft above aerodrome", "1,000 ft above aerodrome", "2,000 ft", "The DA"], 1, "1,000 ft above the aerodrome (EASA)."),
Q(3, "Are alternate planning minima higher than landing minima?", ["No", "Yes", "Only for CAT II", "Only at night"], 1, "Planning minima for alternates are higher."),
Q(3, "At DA without the required visual reference, you must:", ["Continue 100 ft", "Go around", "Level off", "Ask ATC"], 1, "Go around."),
Q(4, "When LVP are in force, ATC:", ["Reduces spacing", "Protects the ILS sensitive and critical areas", "Closes the airport", "Stops all departures"], 1, "LVP protect ILS areas."),
Q(4, "Where are the approaches authorised for each fleet listed?", ["NOTAM", "AOC operations specifications", "TAF", "Load sheet"], 1, "In the operations specifications."),
]

COURSE = dict(
    slug="approach-minima", title="Approach Operations and Minima", header_title="Approach Operations and Minima",
    tagline="Classification of approach operations (2D/3D, Type A/B, CAT I–III), aerodrome operating minima, ceiling and visibility, the approach ban and LVO.",
    purpose="Refresh all flight crews' knowledge of the approach operations authorised by the authority and of ceiling and visibility requirements, in line with ICAO Annex 6 / Doc 9365 and EASA CAT.OP.MPA.110 and .305.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Classify approach operations", "Apply aerodrome operating minima, ceiling and visibility", "Apply planning minima and the approach ban", "Describe LVO requirements and loss of capability"],
    icon="runway", cert_prefix="APM", quiz_count=10, pass_mark=80, group="refresher", season="Summer", finale=None,
    modules=[dict(title="Approach Operations", summary="Classification, minima, approach ban and LVO", icon="runway", lessons=range(1, 5))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner on an ILS approach in low cloud", "Type A or Type B — know what you are flying."),
            2: ("gen", "Runway approach lights in fog", "Minima: DA/H or MDA/H, RVR or visibility."),
            3: ("gen", "Airliner on approach", "Approach ban: 1,000 ft above the aerodrome."),
            4: ("gen", "Airliner landing in fog", "CAT II and III need a specific approval.")},
)
