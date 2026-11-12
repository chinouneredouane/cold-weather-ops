"""W6 — MEL (winter season), all fleets. Generic content from ICAO Annex 6 Part I (MEL provisions),
EASA ORO.MLR.105, CS-MMEL / CS-GEN-MMEL (rectification interval categories). The Domestic Airlines MEL and its
preamble apply for every actual item."""


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


LESSONS = [
dict(title="MMEL, MEL and CDL", minutes=6,
objectives=["Explain the purpose of the MMEL and the MEL.", "Describe how the MEL is produced and approved.", "Distinguish the MEL from the CDL."],
body="""
<h2>Why a MEL?</h2>
<p>A transport aeroplane has redundant systems. The <strong>Minimum Equipment List (MEL)</strong> allows the operator to dispatch an aircraft with certain equipment inoperative, for a limited time and under defined conditions, while keeping an acceptable level of safety (ICAO Annex 6 Part I; EASA ORO.MLR.105).</p>
<ul>
  <li>The <strong>MMEL</strong> (Master MEL) is produced by the aircraft manufacturer and approved by the State of design (for EASA, as part of the operational suitability data).</li>
  <li>The operator's <strong>MEL</strong> is based on the MMEL, adapted to its aircraft configuration, operations and procedures, and approved by its authority. It <strong>must not be less restrictive</strong> than the MMEL.</li>
  <li>Equipment <strong>not listed</strong> in the MEL that is required for the flight must be operative — otherwise no dispatch (unless a specific procedure applies).</li>
</ul>

<h2>CDL</h2>
<p>The <strong>Configuration Deviation List (CDL)</strong>, part of the AFM, allows dispatch with certain external parts missing (for example a panel, fairing or static discharger), usually with performance penalties.</p>

<h2>When the MEL applies</h2>
<p>The MEL applies to dispatch — up to the point defined in the MEL preamble (commonly the start of the flight or the take-off roll). After that point, a failure is handled with the <strong>QRH / FCOM / AOM</strong> non-normal procedures, and the commander decides on continuation using the AFM and good airmanship.</p>
""",
takeaways=["MMEL from the manufacturer; MEL from the operator — never less restrictive.", "Required equipment not in the MEL must work.", "CDL covers missing external parts, often with performance penalties.", "After the point defined in the preamble, use the QRH, not the MEL."],
check=dict(q="Can an operator's MEL be less restrictive than the MMEL?", options=["Yes", "No", "Only for short flights", "Only with captain's approval"], answer=1, explain="The MEL must not be less restrictive than the MMEL."),
),

dict(title="Reading an MEL Item", minutes=7,
objectives=["Read the columns and conditions of an MEL item.", "Apply the rectification interval categories.", "Apply (M) and (O) procedures and placards."],
body="""
<h2>The columns</h2>
<div class="table-wrap"><table>
<tr><th>Column</th><th>Meaning</th></tr>
<tr><td>System / item (ATA chapter)</td><td>The equipment, by ATA reference (e.g. 28 fuel, 73 engine fuel and control)</td></tr>
<tr><td>Rectification interval category</td><td>The time allowed to repair the item (A, B, C or D)</td></tr>
<tr><td>Number installed</td><td>How many are fitted</td></tr>
<tr><td>Number required for dispatch</td><td>How many must work</td></tr>
<tr><td>Remarks or exceptions</td><td>The conditions, limitations and procedures for dispatch</td></tr>
</table></div>

<h2>Rectification interval categories</h2>
<div class="table-wrap"><table>
<tr><th>Category</th><th>Interval</th></tr>
<tr><td>A</td><td>No standard interval — as stated in the remarks of the item</td></tr>
<tr><td>B</td><td>3 consecutive calendar days, excluding the day of discovery</td></tr>
<tr><td>C</td><td>10 consecutive calendar days, excluding the day of discovery</td></tr>
<tr><td>D</td><td>120 consecutive calendar days, excluding the day of discovery</td></tr>
</table></div>
<p>A one-time extension of categories B, C or D may be allowed under a procedure approved by the authority — never by the crew.</p>

<h2>(M), (O) and placards</h2>
<ul>
  <li><strong>(M)</strong> — a maintenance procedure must be performed before dispatch (e.g. deactivating or securing the item).</li>
  <li><strong>(O)</strong> — an operational procedure must be applied by the crew (e.g. a performance penalty, a fuel requirement, a procedure in flight).</li>
  <li>The inoperative item must be <strong>placarded</strong> and recorded in the technical log.</li>
</ul>
<div class="callout info"><span class="label">Example — B737-800 MEL 28-01-03-01 (from the company LOFT)</span>
<p>(M)(O) One main tank aft boost pump may be inoperative provided that: (a) both main tank forward pumps operate normally; (b) at the start of take-off, fuel in the associated tank is not less than 7,500 lb (3,402 kg); (c) a minimum of 2,500 lb (1,134 kg) is maintained in the associated tank; and (d) the boost pump is deactivated. — Training example only; always use the current MEL.</p></div>
""",
takeaways=["Read every column: category, installed, required, remarks.", "Categories: A as stated, B 3 days, C 10 days, D 120 days (excluding day of discovery).", "(M) maintenance and (O) operational procedures; placard and log the item."],
check=dict(q="What is the rectification interval for a category C item?", options=["3 days", "10 calendar days excluding the day of discovery", "120 days", "As stated in the remarks"], answer=1, explain="Category C: 10 consecutive calendar days, excluding the day of discovery."),
),

dict(title="Using the MEL for Dispatch", minutes=6,
objectives=["Apply the MEL dispatch process as a crew.", "Combine several MEL items correctly.", "Recognise items that affect specific approvals and performance."],
body="""
<h2>The dispatch process</h2>
<ol class="steps">
  <li>Read the <strong>technical log</strong>: open defects and deferred items.</li>
  <li>Find each item in the MEL and read the <strong>preamble and definitions</strong> if in doubt.</li>
  <li>Check the <strong>number required</strong>, the <strong>category and expiry date</strong>, and the remarks.</li>
  <li>Confirm that the <strong>(M) procedure</strong> has been completed and the placard fitted.</li>
  <li>Apply the <strong>(O) procedure</strong>: performance penalties, fuel, flight planning restrictions, in-flight actions.</li>
  <li>Brief the crew on the effect of the item.</li>
</ol>

<h2>Several items together</h2>
<p>The MEL items are written independently. When several items are inoperative, the commander must consider their <strong>combined effect</strong> — some combinations are not acceptable even if each item alone is. Check the MEL preamble guidance on multiple items.</p>

<h2>Specific approvals and performance</h2>
<ul>
  <li>The MEL contains the dispatch requirements for systems that need a specific approval or capability: <strong>RVSM, RNAV/PBN, LVO</strong>, and others. An item can remove a capability (for example: no RVSM, no CAT II).</li>
  <li>Many items carry <strong>performance penalties</strong> — more critical on hot days and short runways.</li>
  <li>Some items restrict operation in icing conditions or at night.</li>
</ul>
<div class="callout"><span class="label">Commander's decision</span><p>Dispatch under the MEL is allowed, not obligatory. The commander may refuse an aircraft if, in the actual conditions, the combination of items is unsafe.</p></div>
""",
takeaways=["Tech log → MEL item → category and expiry → (M) done and placard → (O) applied → brief.", "Consider the combined effect of several items.", "MEL items can remove RVSM, PBN or LVO capability and add performance penalties."],
check=dict(q="Two MEL items are each acceptable alone. What must the commander consider?", options=["Nothing more", "Their combined effect on safety in the actual conditions", "Only the item with the longer interval", "Only the newer item"], answer=1, explain="The combined effect of multiple items must be considered."),
),

dict(title="Failures After Dispatch and Good Practice", minutes=5,
objectives=["Handle failures after the MEL no longer applies.", "Report defects correctly.", "Avoid common MEL errors."],
body="""
<h2>Failures after dispatch</h2>
<ul>
  <li>After the point defined in the MEL preamble, use the <strong>QRH / FCOM / AOM</strong> non-normal procedures.</li>
  <li>The decision to continue, return or divert is taken by the commander, based on the AFM limitations, the procedures and the situation — the MEL can help to assess the consequences, but does not authorise continuation by itself.</li>
  <li>Record every defect in the technical log after the flight.</li>
</ul>

<h2>Common errors</h2>
<ul>
  <li>Dispatching with an expired rectification interval.</li>
  <li>Forgetting the (O) procedure — for example a fuel or performance penalty.</li>
  <li>Misreading “number required”.</li>
  <li>Not checking the effect on RVSM, PBN or LVO capability.</li>
  <li>Not informing the other crew member of the restrictions.</li>
</ul>
<div class="callout caution"><span class="label">Company MEL</span><p>Always use the current Domestic Airlines MEL for your fleet (e.g. MEL Ed.02) and its preamble. This course explains the principles; the MEL decides.</p></div>
""",
takeaways=["After the MEL point, use QRH / FCOM / AOM and commander's judgment.", "Record every defect in the technical log.", "Watch expiry dates, (O) procedures, number required and capability effects."],
check=dict(q="A system fails during the climb. Which document do you use first?", options=["The MEL", "The QRH / FCOM / AOM non-normal procedure", "The CDL", "The OM D"], answer=1, explain="After dispatch, failures are handled with the non-normal procedures."),
),
]

QUESTIONS = [
Q(1, "Who produces the MMEL?", ["The operator", "The aircraft manufacturer (approved by the State of design)", "ATC", "The airport"], 1, "The MMEL comes from the manufacturer."),
Q(1, "Which ICAO Annex contains the MEL provisions for commercial operators?", ["Annex 2", "Annex 6", "Annex 14", "Annex 19"], 1, "Annex 6 Part I."),
Q(1, "What does the CDL cover?", ["Inoperative cabin equipment", "Missing external parts of the airframe", "Crew deviations", "ATC deviations"], 1, "The CDL covers missing external parts."),
Q(1, "Required equipment that is not listed in the MEL:", ["May be inoperative", "Must be operative for dispatch", "Can be deferred by the crew", "Is never required"], 1, "Unlisted required equipment must work."),
Q(2, "Category B rectification interval:", ["1 day", "3 consecutive calendar days excluding day of discovery", "10 days", "120 days"], 1, "Category B: 3 days."),
Q(2, "Category D rectification interval:", ["10 days", "30 days", "120 consecutive calendar days excluding day of discovery", "No limit"], 2, "Category D: 120 days."),
Q(2, "What does (O) mean in an MEL item?", ["Optional", "An operational procedure the crew must apply", "Overhaul", "Only on the ground"], 1, "(O) = operational procedure."),
Q(2, "What does (M) mean?", ["A maintenance procedure before dispatch", "Monitor only", "Manual flying", "Minimum fuel"], 0, "(M) = maintenance procedure."),
Q(2, "Who may extend a rectification interval?", ["The crew", "The operator under a procedure approved by the authority", "ATC", "Nobody, ever"], 1, "Only under an approved procedure."),
Q(3, "Which capabilities can an MEL item remove?", ["Only the galley", "RVSM, PBN or LVO capability", "Only cabin lighting", "None"], 1, "The MEL includes dispatch requirements for specific approvals."),
Q(3, "Is dispatch under the MEL obligatory for the commander?", ["Yes", "No — the commander may refuse if unsafe in the actual conditions", "Only at night", "Only for B items"], 1, "MEL dispatch is permitted, not obligatory."),
Q(4, "After the point defined in the MEL preamble, a failure is handled with:", ["The MEL", "The QRH / FCOM / AOM", "The CDL", "The flight plan"], 1, "Use the non-normal procedures."),
Q(4, "Which is a common MEL error?", ["Reading the preamble", "Forgetting the (O) procedure", "Placarding the item", "Briefing the crew"], 1, "Forgetting the (O) procedure is common."),
]

COURSE = dict(
    slug="mel-refresher", title="MEL Refresher", header_title="MEL Refresher",
    tagline="MMEL, MEL and CDL: reading an item, rectification intervals, (M) and (O) procedures, dispatch, multiple items and failures after dispatch.",
    purpose="Refresh all flight crews' knowledge of the MEL principles in line with ICAO Annex 6 and EASA ORO.MLR.105, and of the correct use of the company MEL.",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Explain the MMEL, MEL and CDL", "Read an MEL item and its rectification category", "Apply the MEL dispatch process", "Handle failures after dispatch and avoid common errors"],
    icon="gear", cert_prefix="MEL", quiz_count=10, pass_mark=80, group="refresher", season="Winter", finale=None,
    modules=[dict(title="MEL Principles", summary="MMEL, MEL, CDL and reading an item", icon="gear", lessons=range(1, 3)),
             dict(title="Using the MEL", summary="Dispatch, multiple items, failures after dispatch", icon="people", lessons=range(3, 5))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner on the apron before departure", "The MEL allows safe dispatch with some equipment inoperative."),
            2: ("gen", "Flight deck during preparation", "Read every column of the MEL item."),
            3: ("gen", "Two pilots preparing the flight", "Tech log, MEL, (M), (O), brief."),
            4: ("gen", "Airliner climbing after take-off", "After dispatch: QRH, not MEL.")},
)
