"""S5 — Allowances for Inoperative Ground Equipment (summer season), all fleets.
Generic content from EASA CAT.OP.MPA.110 and its AMC (effect of failed or downgraded ground equipment on
landing minima), ICAO Doc 9365 and Annex 14 lighting. The applicable table is the one in the Domestic Airlines OM A."""


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


COMPANY = ('<div class="callout caution"><span class="label">Company table</span><p>The effect of each failed or downgraded item on the minima is given in the '
           '<strong>“failed or downgraded equipment” table of the Domestic Airlines OM A</strong>. Use that table — this course explains how it works, '
           'not its values.</p></div>')

LESSONS = [
dict(title="Why Ground Equipment Matters", minutes=5,
objectives=["Explain why published minima assume serviceable ground equipment.", "Identify how failures are notified.", "Describe the possible effects on an approach."],
body="""
<h2>Minima assume serviceable equipment</h2>
<p>Aerodrome operating minima are established for a runway with its navigation aids, lighting and RVR equipment serviceable (EASA CAT.OP.MPA.110; ICAO Doc 9365). When an item fails or is downgraded, the minima may have to be <strong>increased</strong>, or the approach may <strong>not be available</strong>.</p>

<h2>How you find out</h2>
<ul>
  <li><strong>NOTAM</strong> — planned or known outages (e.g. ILS glide path unserviceable, approach lights out of service).</li>
  <li><strong>ATIS and ATC</strong> — recent failures.</li>
  <li>Flight deck indications — loss of an ILS signal, flags, or visible lighting failures.</li>
</ul>

<h2>Possible effects</h2>
<ul>
  <li><strong>No effect</strong> — for example a failure that has an equivalent replacement (a marker replaced by a DME distance or another fix).</li>
  <li><strong>Higher minima</strong> — for example an increased RVR when approach lights are out.</li>
  <li><strong>Downgrade</strong> — for example from CAT II to CAT I, or from a 3D to a 2D approach (ILS to LOC only).</li>
  <li><strong>Approach not available</strong>.</li>
</ul>
""" + COMPANY,
takeaways=["Minima assume serviceable ground aids, lighting and RVR equipment.", "Failures come from NOTAM, ATIS / ATC or flight deck indications.", "Effects: none, higher minima, downgrade, or no approach."],
check=dict(q="The ILS glide path is out of service. What is the usual effect?", options=["No effect", "The approach becomes a localiser-only (2D) approach with higher minima", "CAT III becomes available", "The runway closes"], answer=1, explain="Without the glide path the ILS becomes a LOC-only 2D approach."),
),

dict(title="The Equipment and the Table", minutes=7,
objectives=["Identify the ground equipment covered by the table.", "Understand approach lighting classes.", "Read the failed equipment table correctly."],
body="""
<h2>Equipment covered</h2>
<ul>
  <li><strong>ILS / GLS components</strong> — localiser, glide path, standby transmitters, outer and middle markers or the DME replacing them.</li>
  <li><strong>Navigation aids</strong> for non-precision approaches — VOR, NDB, DME.</li>
  <li><strong>RVR assessment systems</strong> — touchdown zone, mid-point and stop-end sensors.</li>
  <li><strong>Lighting</strong> — approach lights, runway edge, threshold and end lights, runway centreline lights, touchdown zone lights, and standby power for lighting.</li>
</ul>

<h2>Approach lighting classes (EASA)</h2>
<div class="table-wrap"><table>
<tr><th>Class</th><th>Length of the approach lighting</th></tr>
<tr><td>FALS — full approach lighting</td><td>720 m or more</td></tr>
<tr><td>IALS — intermediate</td><td>420 m to 719 m</td></tr>
<tr><td>BALS — basic</td><td>210 m to 419 m</td></tr>
<tr><td>NALS — no approach lighting</td><td>less than 210 m, or none</td></tr>
</table></div>
<p>The minimum RVR for an approach depends on the lighting class. When part of the approach lighting fails, the class can change — and the RVR minimum increases.</p>

<h2>Reading the table</h2>
<ol class="steps">
  <li>Find the failed or downgraded item.</li>
  <li>Find the column for your type of approach (e.g. CAT II/III, CAT I, 2D).</li>
  <li>Read the effect: no effect, a modified condition, an increased RVR, or “not allowed”.</li>
  <li>Apply only <strong>one entry per failed item</strong>; if several items have failed, apply the most restrictive result, and check the notes in the table.</li>
</ol>
""" + COMPANY,
takeaways=["Covered: ILS components, navaids, RVR systems, lighting.", "Lighting classes FALS / IALS / BALS / NALS set the RVR minimum.", "Read the item, the approach type column and the effect; apply the most restrictive result for multiple failures."],
check=dict(q="Approach lights 450 m long belong to which class?", options=["FALS", "IALS", "BALS", "NALS"], answer=1, explain="IALS: 420 m to 719 m."),
),

dict(title="Applying the Allowances in Flight", minutes=5,
objectives=["Apply the table during planning and in flight.", "Brief the revised minima.", "Handle a failure during the approach."],
body="""
<h2>Planning</h2>
<ul>
  <li>Check the NOTAMs for the destination and alternates; apply the table to calculate the revised minima.</li>
  <li>Check that the weather allows the revised minima, with the planning minima for alternates.</li>
</ul>

<h2>In flight</h2>
<ul>
  <li>Get the ATIS, confirm the status of aids and lighting, recalculate the minima and <strong>brief</strong> them.</li>
  <li>If a failure is reported <strong>during the approach</strong>, assess the effect: on a precision approach, a failure of the guidance usually requires a go-around unless the required visual reference is already established, as your procedure states.</li>
  <li>Do not improvise minima — if in doubt, use the more restrictive value or go around.</li>
</ul>

<h2>Reporting</h2>
<p>Report any observed failure of aids or lighting to ATC; it may not have been detected on the ground.</p>
""" + COMPANY,
takeaways=["Apply the table at planning and again in flight with the latest ATIS.", "Brief the revised minima.", "If in doubt, use the more restrictive value or go around; report failures to ATC."],
check=dict(q="During an ILS approach, ATC reports the glide path unserviceable above the minimum. What do you do?", options=["Continue to the DA", "Assess and normally go around or change to the LOC approach and minima as the procedure states", "Descend faster", "Ignore it"], answer=1, explain="A failure of guidance on the approach usually requires a go-around or a change to the appropriate approach and minima."),
),
]

QUESTIONS = [
Q(1, "Published minima assume:", ["Any equipment state", "Serviceable navigation aids, lighting and RVR equipment", "Daylight only", "VMC"], 1, "Minima assume serviceable ground equipment."),
Q(1, "Where are planned ground equipment outages published?", ["TAF", "NOTAM", "Load sheet", "Flight plan"], 1, "NOTAM."),
Q(1, "A possible effect of an approach lighting failure is:", ["Lower minima", "Higher RVR minimum", "CAT III authorisation", "No effect ever"], 1, "Lighting failures usually increase the RVR minimum."),
Q(2, "Approach lighting of 720 m or more is classified as:", ["FALS", "IALS", "BALS", "NALS"], 0, "FALS."),
Q(2, "Approach lighting shorter than 210 m is classified as:", ["FALS", "IALS", "BALS", "NALS"], 3, "NALS."),
Q(2, "With several failed items, you should apply:", ["The least restrictive result", "The most restrictive result", "Only the first item", "None"], 1, "Apply the most restrictive result."),
Q(2, "Which of these is covered by the failed equipment table?", ["Cabin lighting", "RVR assessment systems", "Weather radar", "Fuel trucks"], 1, "RVR systems are covered."),
Q(3, "When should the revised minima be calculated?", ["Only after landing", "At planning and again in flight with the latest ATIS", "Never", "Only by ATC"], 1, "At planning and in flight."),
Q(3, "If in doubt about the effect of a failure, you should:", ["Use the lower minima", "Use the more restrictive value or go around", "Ask the passengers", "Continue"], 1, "Use the more restrictive value or go around."),
Q(3, "Where is the company table of failed or downgraded equipment?", ["OM A", "MEL", "CDL", "Technical log"], 0, "In OM A."),
]

COURSE = dict(
    slug="inop-ground-equipment", title="Inoperative Ground Equipment", header_title="Inoperative Ground Equipment",
    tagline="How failed or downgraded ground equipment — ILS components, navaids, RVR systems and lighting — affects approach minima, and how to apply the OM A table.",
    purpose="Refresh all flight crews' knowledge of the allowances for inoperative ground equipment in line with EASA CAT.OP.MPA.110 and ICAO Doc 9365, and of the use of the company table in OM A.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Explain why ground equipment status affects minima", "Identify the equipment and lighting classes in the table", "Apply the allowances at planning and in flight"],
    icon="search", cert_prefix="IGE", quiz_count=10, pass_mark=80, group="refresher", season="Summer", finale=None,
    modules=[dict(title="Inoperative Ground Equipment", summary="Why it matters, the table, and its application", icon="search", lessons=range(1, 4))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Runway with approach lights at dusk", "Minima assume serviceable aids and lighting."),
            2: ("gen", "Approach lighting system in front of a runway", "The lighting class sets the RVR minimum."),
            3: ("gen", "Airliner on final approach at night", "Recalculate and brief the minima with the latest ATIS.")},
)
