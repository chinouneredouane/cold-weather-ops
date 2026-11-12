"""RVSM refresher (summer season). Based on the company RVSM recurrent training presentation, updated to
ICAO Doc 9574 / PANS-ATM and EASA Part-SPA (SPA.RVSM); TCAS II updated to version 7.1."""
from courses.upset_recovery.diagrams import FONT, INK, MUTED, LINE, GREEN, GREEN_D, RED, AMBER, BLUE


def levels_diagram():
    rows = []
    for i, fl in enumerate(range(280, 430, 10)):
        y = 30 + (420 - fl) * 2.4
        rvsm = 290 <= fl <= 410
        new = fl in (300, 320, 340, 360, 380, 400)
        col = GREEN_D if new else (INK if rvsm else MUTED)
        rows.append(f'<line x1="90" y1="{y:.0f}" x2="560" y2="{y:.0f}" stroke="{LINE if not rvsm else "#b9d7c3"}" stroke-width="{2 if new else 1}"/>'
                    f'<text x="80" y="{y+4:.0f}" text-anchor="end" font-weight="{800 if new else 500}" fill="{col}">FL{fl}</text>')
        if new:
            rows.append(f'<text x="570" y="{y+4:.0f}" fill="{GREEN_D}" font-size="12">new level</text>')
    y290 = 30 + (420 - 290) * 2.4
    y410 = 30 + (420 - 410) * 2.4
    svg = (f'<rect x="90" y="{y410-6:.0f}" width="470" height="{y290-y410+12:.0f}" fill="{GREEN}" opacity=".07"/>' + "".join(rows) +
           f'<text x="330" y="{y410-14:.0f}" text-anchor="middle" font-weight="700" fill="{GREEN_D}">RVSM airspace FL290 – FL410: 1,000 ft separation</text>'
           f'<text x="330" y="{y290+26:.0f}" text-anchor="middle" fill="{MUTED}">Below FL290 and above FL410: conventional separation rules apply</text>')
    return f"""
<figure class="diagram"><svg viewBox="0 0 660 400" role="img" aria-label="RVSM flight levels"><title>RVSM flight levels</title>
<desc>Flight levels between FL290 and FL410 separated by 1,000 ft; FL300, 320, 340, 360, 380 and 400 are the six levels added by RVSM.</desc>
<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg>
<figcaption>RVSM reduces vertical separation from 2,000 ft to 1,000 ft between FL290 and FL410, adding six flight levels (in green).</figcaption></figure>"""


def fleet_table():
    return """<div class="table-wrap"><table>
<tr><th>Fleet</th><th>RVSM</th><th>Notes</th></tr>
<tr><td><strong>Boeing 737-800</strong></td><td>✅ RVSM approved</td><td>All RVSM procedures in this course apply. Check the MEL for RVSM-related items before every flight.</td></tr>
<tr><td><strong>Dash 8-Q400</strong></td><td>— Not applicable</td><td>Operates below RVSM airspace (maximum operating altitude below FL290). This course gives awareness of RVSM traffic, phraseology and TCAS.</td></tr>
<tr><td><strong>Dash 8-Q200</strong></td><td>— Not applicable</td><td>Operates below RVSM airspace. Awareness only, as for the Q400.</td></tr>
</table></div>"""


LESSONS = [
dict(title="RVSM Airspace, Approval and Equipment", minutes=7,
objectives=["Define RVSM airspace and its benefits.", "List the equipment required for RVSM operations.", "State which Domestic Airlines fleets are RVSM approved."],
body="""
<h2>What is RVSM?</h2>
<p><strong>Reduced Vertical Separation Minimum (RVSM)</strong> airspace is any airspace or route between <strong>FL290 and FL410 inclusive</strong> where aircraft are separated vertically by <strong>1,000 ft (300 m)</strong> instead of 2,000 ft (600 m).</p>
""" + levels_diagram() + """
<p>The reduction adds six flight levels — FL300, FL320, FL340, FL360, FL380 and FL400 — giving significant benefits in fuel economy and en-route airspace capacity.</p>

<h2>Approval</h2>
<p>ICAO requires States to approve operators and aircraft for RVSM and to establish <strong>initial and recurrent training programmes</strong> for flight crews (ICAO Doc 9574, Manual on a 300 m (1 000 ft) Vertical Separation Minimum; Annex 6). In Europe this is a specific approval under <strong>EASA Part-SPA (SPA.RVSM)</strong>. Both the aircraft (airworthiness) and the operator (procedures and training) must be approved.</p>
""" + fleet_table() + """
<h2>Required equipment</h2>
<ul>
  <li><strong>Two independent altitude measurement systems;</strong></li>
  <li>one <strong>SSR transponder</strong> with altitude reporting, connected to the altitude measurement system in use for height-keeping;</li>
  <li>an <strong>altitude alerting system</strong>;</li>
  <li>an <strong>automatic altitude control system</strong> (autopilot).</li>
</ul>
<p>The minimum aircraft system performance specification (MASPS) sets tight limits on altimetry system error — of the order of <strong>80 ft</strong> — and requires the automatic altitude control to hold the cleared level within about <strong>±65 ft</strong> in normal conditions; altitude excursions of more than about <strong>200 ft</strong> must not occur in level flight. Exact values are in your AFM RVSM statement.</p>
""",
takeaways=["RVSM: FL290–FL410 inclusive, 1,000 ft separation, six extra levels.", "Approval required for both aircraft and operator (ICAO Doc 9574, EASA SPA.RVSM).", "Equipment: two altimetry systems, transponder, altitude alerter, autopilot with altitude hold.", "B737-800: RVSM approved. Q400 and Q200: operate below RVSM airspace."],
check=dict(q="Which flight levels are included in RVSM airspace?", options=["FL250 to FL450", "FL290 to FL410 inclusive", "FL300 to FL400 only", "All levels above FL180"], answer=1,
           explain="RVSM airspace extends from FL290 to FL410 inclusive."),
),

dict(title="Flight Planning and Pre-flight", minutes=6,
objectives=["Complete the flight plan correctly for an RVSM flight.", "Perform the RVSM pre-flight checks.", "Apply the MEL to RVSM equipment."],
body="""
<h2>Flight planning</h2>
<ul>
  <li>In the ICAO flight plan, insert the letter <strong>“W”</strong> in item 10 to indicate RVSM approval (and in a repetitive flight plan, the letter <strong>“Q”</strong> where required by the procedure).</li>
  <li>Verify that the aircraft is RVSM compliant and that no RVSM-related item is open in the technical log.</li>
  <li>Check forecast and reported weather — especially severe turbulence and mountain wave activity at cruise levels.</li>
  <li>Check the <strong>MEL</strong>: the MEL contains the dispatch requirements for systems that need a specific approval, such as RVSM, RNAV and LVO.</li>
  <li>Check any RVSM operating limitations in the AFM.</li>
</ul>

<h2>Pre-flight at the aircraft</h2>
<ul>
  <li>Review the maintenance logs and forms for the serviceability of RVSM equipment.</li>
  <li>During the exterior inspection, check the <strong>static ports</strong> and the condition of the fuselage skin around the pitot-static sources. Damage, dents or residue near the static ports can cause altimetry errors.</li>
  <li>On the ground, compare the altimeters with the known aerodrome elevation. The difference must not exceed the limit in your FCOM (typically about <strong>75 ft</strong>).</li>
  <li>Before take-off, confirm that the RVSM equipment is operative.</li>
</ul>
<div class="callout"><span class="label">Good practice</span><p>Brief the RVSM status in the departure briefing: equipment state, MEL items, expected cruise level and any turbulence or mountain wave forecast.</p></div>
""",
takeaways=["Flight plan item 10: “W” for RVSM approval.", "Check MEL, weather and technical log before an RVSM flight.", "Inspect static ports; compare altimeters with aerodrome elevation (FCOM limit, typically 75 ft)."],
check=dict(q="Which letter in the ICAO flight plan indicates RVSM approval?", options=["R", "W", "Y", "Z"], answer=1, explain="The letter W in item 10 indicates RVSM approval."),
),

dict(title="Entering and Flying in RVSM Airspace", minutes=7,
objectives=["List the equipment that must be operating before entering RVSM airspace.", "Apply the en-route height-keeping procedures.", "Perform and record the altimeter cross-checks."],
body="""
<h2>Before entering RVSM airspace</h2>
<p>The following equipment must be operating normally:</p>
<ul><li>two primary altitude measurement systems;</li><li>one automatic altitude control system;</li><li>one altitude alerting device;</li><li>the transponder.</li></ul>
<p>If any of this equipment fails before entry, <strong>request a new clearance</strong> to avoid RVSM airspace, or follow the established contingency procedures.</p>

<h2>En-route procedures</h2>
<ul>
  <li>Fly at the <strong>cleared flight level (CFL)</strong>. Make sure every ATC clearance is fully understood, read back and cross-checked by both pilots.</li>
  <li>Except in an emergency, do not intentionally leave the CFL without an ATC clearance.</li>
  <li>Use the <strong>automatic altitude capture</strong> for level changes. Overshoots and undershoots should not exceed <strong>150 ft</strong>.</li>
  <li>Reduce the vertical rate to <strong>less than 1,500 ft/min in the last 1,000 ft</strong> before the cleared level, especially when traffic is at the adjacent level (see Lesson 5).</li>
  <li>In cruise, fly with the <strong>automatic altitude control engaged</strong>, except when the aircraft must be re-trimmed or in turbulence where the procedure requires otherwise.</li>
</ul>

<h2>Altimeter cross-checks</h2>
<ul>
  <li>At intervals of about <strong>one hour</strong>, cross-check the primary and standby altimeters.</li>
  <li>The two primary altimeters must agree within <strong>200 ft</strong>.</li>
  <li><strong>Record</strong> at least the initial cross-check — on the operational flight plan (Jetplan).</li>
  <li>Normally, the altimetry system controlling the autopilot should also be the source for the transponder's altitude reporting. If not, report the system as defective and notify ATC.</li>
</ul>
""",
takeaways=["Before entry: two altimetry systems, autopilot altitude hold, altitude alerter, transponder.", "Fly the CFL with altitude hold engaged; overshoot or undershoot less than 150 ft.", "Less than 1,500 ft/min in the last 1,000 ft before the cleared level.", "About every hour: primary altimeters within 200 ft; record the initial check."],
check=dict(q="What is the maximum difference allowed between the two primary altimeters in RVSM airspace?", options=["75 ft", "150 ft", "200 ft", "300 ft"], answer=2, explain="The primary altimeters must agree within 200 ft."),
),

dict(title="Contingencies and Special Situations", minutes=9,
objectives=["Recognise the contingencies that must be reported to ATC.", "Apply the pilot actions for equipment failures, turbulence, wake and mountain waves.", "Explain the 2,000 ft separation cases."],
body="""
<h2>Tell ATC as soon as possible</h2>
<p>An in-flight contingency is any unforeseen circumstance that affects the ability to meet the RVSM height-keeping requirements. Inform ATC as soon as possible of:</p>
<ul>
  <li>failure of the automatic altitude control system;</li>
  <li>loss of redundancy of the primary altimetry systems, or loss of all primary altimeters;</li>
  <li>loss of thrust requiring a descent;</li>
  <li>failure of any other equipment affecting height-keeping;</li>
  <li>an encounter with <strong>greater than moderate turbulence</strong>.</li>
</ul>
<p>Obtain a revised clearance <strong>before</strong> deviating from the cleared route or level whenever possible. If that is not possible, obtain it as soon as possible afterwards. If you cannot contact ATC, follow the regional contingency procedures.</p>
<p>When the aircraft no longer meets RVSM requirements, ATC treats it as <strong>non-RVSM</strong> and applies <strong>2,000 ft</strong> vertical separation or a horizontal separation minimum.</p>

<h2>Scenarios</h2>
<div class="table-wrap"><table>
<tr><th>Scenario</th><th>Pilot actions</th></tr>
<tr><td>Loss of automatic altitude control, altitude alerter or all primary altimeters</td><td>Tell ATC: <strong>“Unable RVSM due equipment.”</strong> Request a clearance out of RVSM airspace unless the operational situation dictates otherwise.</td></tr>
<tr><td>Only one primary altimeter remains</td><td>Cross-check it with the standby altimeter. Notify ATC of operation with a single primary altimeter. If its accuracy cannot be confirmed, act as for the loss of all primary altimeters.</td></tr>
<tr><td>Transponder failure</td><td>Contact ATC and request authority to continue at the cleared level. Comply with any revised clearance.</td></tr>
<tr><td>Severe turbulence</td><td>Tell ATC: <strong>“Unable RVSM due turbulence.”</strong> Request a vector clear of traffic if not offered, and a level change or re-route if desired. ATC applies horizontal separation or 2,000 ft.</td></tr>
<tr><td>Wake turbulence</td><td>Usually moderate or less at RVSM levels; the wind decides the risk. Request a vector, a level change or a lateral offset (where authorised).</td></tr>
<tr><td>Mountain wave activity</td><td>Report it to ATC. If traffic is called at an adjacent level, request a vector to avoid merging targets; request a level change or re-route if desired.</td></tr>
</table></div>

<h2>Special cases</h2>
<ul>
  <li><strong>Communication failure</strong>: ICAO procedures apply 2,000 ft vertical separation between the aircraft with the failure and other aircraft in RVSM airspace, unless horizontal separation exists.</li>
  <li><strong>RVSM suspension</strong>: in a portion of airspace where RVSM is suspended (for example in widespread severe turbulence), 2,000 ft separation is applied to all aircraft.</li>
  <li><strong>State aircraft</strong>: non-RVSM-approved State (e.g. military) aircraft may be accommodated; ATC applies 2,000 ft separation to them.</li>
  <li><strong>Non-RVSM aircraft</strong> climbing or descending through RVSM levels to or from FL430 and above are handled workload permitting, and must be able to climb or descend continuously at a normal rate.</li>
  <li><strong>Regional differences</strong>: RVSM is global, but contingency procedures can differ between regions. The commander must know the procedures of the region being flown.</li>
</ul>
""",
takeaways=["Report to ATC: autopilot altitude hold, altimetry, thrust or height-keeping failures, and turbulence greater than moderate.", "Phrases: “Unable RVSM due equipment” / “Unable RVSM due turbulence”.", "Non-RVSM status, communication failure and RVSM suspension mean 2,000 ft separation.", "Know the regional contingency procedures."],
check=dict(q="In RVSM airspace you encounter severe turbulence. What do you tell ATC?", options=["“Request block altitude”", "“Unable RVSM due turbulence”", "“Mayday, mayday, mayday”", "“Negative RVSM”"], answer=1,
           explain="The standard phrase is “Unable RVSM due turbulence”. ATC will then apply horizontal separation or 2,000 ft."),
),

dict(title="TCAS / ACAS II in RVSM Airspace", minutes=6,
objectives=["Describe the ACAS II version 7.1 changes.", "Apply procedures that avoid nuisance resolution advisories at adjacent levels.", "Respond correctly to a resolution advisory."],
body="""
<h2>ACAS II version 7.1</h2>
<p>ACAS II (TCAS II) version 7.1 is the standard required by ICAO and EASA, replacing version 7.0. The main operational change for crews:</p>
<ul>
  <li>The <strong>“ADJUST VERTICAL SPEED, ADJUST”</strong> resolution advisory has been replaced by <strong>“LEVEL OFF, LEVEL OFF”</strong>, which always requires the vertical rate to be reduced to <strong>0 ft/min</strong>.</li>
  <li>The <strong>reversal logic</strong> has been improved, so that an RA can reverse when the other aircraft does not follow its own RA.</li>
</ul>
<p>Operate TCAS in <strong>TA/RA</strong> mode during RVSM operations, including in the transition areas.</p>

<h2>Avoiding nuisance RAs at adjacent levels</h2>
<p>With only 1,000 ft between aircraft, a high vertical rate close to the cleared level can trigger an RA in an aircraft at the adjacent level. ICAO procedures therefore recommend that when a pilot is aware of traffic at an adjacent level (for example from the traffic display), the aircraft climbs or descends at <strong>less than 1,500 ft/min throughout the last 1,000 ft</strong> before the assigned level — especially with the autopilot engaged.</p>

<h2>Responding to an RA</h2>
<ul>
  <li><strong>Follow the RA promptly and accurately</strong>, even if it conflicts with an ATC clearance or instruction. Never manoeuvre in the opposite sense to an RA.</li>
  <li>Tell ATC as soon as possible: “(call sign), TCAS RA.”</li>
  <li>When clear: “(call sign), clear of conflict, returning to (assigned clearance)” — then return promptly to the clearance.</li>
  <li>File the company report after any RA.</li>
</ul>
<div class="callout warn"><span class="label">Remember</span><p>A TCAS RA takes precedence over ATC instructions. Following an ATC instruction against an RA has caused mid-air collisions.</p></div>
""",
takeaways=["ACAS II v7.1: “LEVEL OFF, LEVEL OFF” replaces “ADJUST VERTICAL SPEED”; improved reversal logic.", "TA/RA mode in RVSM airspace.", "Less than 1,500 ft/min in the last 1,000 ft when traffic is at an adjacent level.", "Always follow the RA, then inform ATC."],
check=dict(q="What does the ACAS II 7.1 resolution advisory “LEVEL OFF, LEVEL OFF” require?", options=["Reduce vertical speed by half", "Reduce vertical speed to 0 ft/min", "Climb at 1,500 ft/min", "Return to the ATC clearance"], answer=1,
           explain="“LEVEL OFF, LEVEL OFF” always requires the vertical rate to be reduced to 0 ft/min."),
),

dict(title="Phraseology, Reporting and Crew Knowledge", minutes=6,
objectives=["Use the standard RVSM phraseology.", "Complete the post-flight entries and reports.", "Review the RVSM knowledge items required for recurrent training."],
body="""
<h2>Standard phraseology</h2>
<div class="table-wrap"><table>
<tr><th>Circumstance</th><th>Phraseology</th></tr>
<tr><td>ATC asks the RVSM status of a flight</td><td>“Confirm RVSM approved.”</td></tr>
<tr><td>Pilot: the flight is RVSM approved</td><td>“Affirm RVSM.”</td></tr>
<tr><td>Pilot: the flight is not RVSM approved</td><td>“Negative RVSM.”</td></tr>
<tr><td>Pilot of a State aircraft that is not RVSM approved</td><td>“Negative RVSM, State aircraft.”</td></tr>
<tr><td>ATC denies entry to RVSM airspace</td><td>“Unable clearance into RVSM airspace, maintain (or descend to, or climb to) flight level …”</td></tr>
<tr><td>Pilot: weather prevents height-keeping (e.g. severe turbulence)</td><td>“Unable RVSM due turbulence.”</td></tr>
<tr><td>Pilot: equipment degraded below RVSM requirements</td><td>“Unable RVSM due equipment.”</td></tr>
<tr><td>ATC asks to be told when RVSM can be resumed</td><td>“Report able to resume RVSM.”</td></tr>
<tr><td>Pilot: able to resume after a contingency</td><td>“Ready to resume RVSM.”</td></tr>
</table></div>

<h2>After the flight</h2>
<ul>
  <li>Enter in the technical log any problem with altitude-keeping, transponder failures, or altimeter differences greater than <strong>200 ft</strong>.</li>
  <li>File the <strong>altitude deviation report</strong> for any deviation of <strong>300 ft or more</strong> from the cleared level.</li>
  <li>File the <strong>wake turbulence encounter report</strong> after any significant wake encounter.</li>
</ul>

<h2>What every crew member must know (recurrent training items)</h2>
<ol>
  <li>Airworthiness documents and the aircraft's RVSM approval;</li>
  <li>operating practices and procedures, the Operations Manual and checklists;</li>
  <li>the MEL items for RVSM;</li>
  <li>standard ATC phraseology and cross-checking of clearances;</li>
  <li>use of the standby altimeter in contingencies;</li>
  <li>problems of visual perception of other aircraft only 1,000 ft away;</li>
  <li>characteristics of the altitude capture system;</li>
  <li>the relationship between altimetry, automatic altitude control and transponder in normal and abnormal conditions;</li>
  <li>any airframe operating restrictions for RVSM.</li>
</ol>
""",
takeaways=["Know the standard phrases: Affirm / Negative RVSM, Unable RVSM due turbulence / equipment, Ready to resume RVSM.", "Technical log: altimeter differences over 200 ft, altitude-keeping or transponder problems.", "Report altitude deviations of 300 ft or more, and wake turbulence encounters."],
check=dict(q="ATC asks “Confirm RVSM approved”. Your aircraft is approved. What do you reply?", options=["“Roger”", "“Affirm RVSM”", "“Wilco RVSM”", "“RVSM capable”"], answer=1, explain="The standard reply is “Affirm RVSM”."),
),
]


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


QUESTIONS = [
Q(1, "RVSM airspace extends between:", ["FL250 and FL450", "FL290 and FL410 inclusive", "FL300 and FL400", "FL280 and FL420"], 1, "RVSM applies from FL290 to FL410 inclusive."),
Q(1, "How many flight levels does RVSM add?", ["Three", "Four", "Six", "Eight"], 2, "FL300, 320, 340, 360, 380 and 400 — six levels."),
Q(1, "Which is NOT required equipment for RVSM?", ["Two independent altimetry systems", "An altitude alerting system", "An automatic altitude control system", "A weather radar"], 3, "Weather radar is not an RVSM requirement."),
Q(1, "Which Domestic Airlines fleet operates in RVSM airspace?", ["Q200", "Q400", "Boeing 737-800", "All three"], 2, "Only the B737-800 is RVSM approved; the Dash 8 fleets operate below RVSM airspace."),
Q(1, "Which ICAO document is the RVSM manual?", ["Doc 9574", "Doc 9613", "Doc 4444 only", "Doc 9640"], 0, "ICAO Doc 9574 is the manual on the 1,000 ft vertical separation minimum."),
Q(2, "What does “W” in item 10 of the flight plan indicate?", ["RNAV approval", "RVSM approval", "Weather radar", "Wake category"], 1, "W indicates RVSM approval."),
Q(2, "During the walk-around, which item is particularly important for RVSM?", ["Tyre pressure", "Static ports and the skin around pitot-static sources", "Cargo door seals", "Navigation lights"], 1, "Damage near the static ports can cause altimetry errors."),
Q(2, "Before take-off, the altimeters are compared with:", ["Each other only", "The known aerodrome elevation, within the FCOM limit", "The GPS altitude", "The radio altimeter"], 1, "Altimeters are compared with aerodrome elevation (typically within 75 ft)."),
Q(3, "One autopilot altitude hold fails before entering RVSM airspace (none remaining). What should you do?", ["Continue and hand-fly", "Request a new clearance to avoid RVSM airspace or apply contingency procedures", "Climb above FL410", "Switch off the transponder"], 1, "Without automatic altitude control, request a clearance to avoid RVSM airspace."),
Q(3, "What is the maximum overshoot or undershoot during a level capture?", ["50 ft", "150 ft", "300 ft", "500 ft"], 1, "Altitude transitions should not over- or undershoot by more than 150 ft."),
Q(3, "How often should the primary and standby altimeters be cross-checked in cruise?", ["Every 15 minutes", "At about one-hour intervals", "Only before descent", "Never in cruise"], 1, "Cross-check at approximately one-hour intervals."),
Q(3, "The primary altimeters must agree within:", ["75 ft", "150 ft", "200 ft", "500 ft"], 2, "200 ft is the maximum difference."),
Q(4, "When ATC considers an aircraft non-RVSM, what separation is applied?", ["500 ft", "1,000 ft", "2,000 ft (or horizontal separation)", "4,000 ft"], 2, "Non-RVSM aircraft are given 2,000 ft vertical or horizontal separation."),
Q(4, "Which turbulence must be reported because it affects RVSM height-keeping?", ["Light", "Greater than moderate", "Any chop", "Only clear-air turbulence"], 1, "Turbulence greater than moderate must be reported."),
Q(4, "With only one primary altimeter remaining, the pilot should:", ["Continue without telling ATC", "Cross-check it with the standby and notify ATC", "Descend immediately", "Switch off the autopilot"], 1, "Cross-check with the standby altimeter and notify ATC."),
Q(4, "In case of communication failure in RVSM airspace, ICAO procedures apply a vertical separation of:", ["1,000 ft", "2,000 ft", "3,000 ft", "500 ft"], 1, "2,000 ft unless horizontal separation exists."),
Q(5, "In ACAS II version 7.1, which RA replaced “ADJUST VERTICAL SPEED, ADJUST”?", ["“MONITOR VERTICAL SPEED”", "“LEVEL OFF, LEVEL OFF”", "“CLIMB, CLIMB”", "“CLEAR OF CONFLICT”"], 1, "“LEVEL OFF, LEVEL OFF” replaced the AVSA RA."),
Q(5, "To avoid nuisance RAs with traffic at an adjacent level, the vertical rate in the last 1,000 ft should be less than:", ["500 ft/min", "1,000 ft/min", "1,500 ft/min", "3,000 ft/min"], 2, "Less than 1,500 ft/min in the last 1,000 ft."),
Q(5, "An RA conflicts with an ATC instruction. What do you do?", ["Follow ATC", "Follow the RA", "Ask ATC which to follow", "Do nothing"], 1, "Always follow the RA, then inform ATC."),
Q(6, "Your equipment no longer meets RVSM requirements. What do you tell ATC?", ["“Negative RVSM”", "“Unable RVSM due equipment”", "“Request descent”", "“RVSM suspended”"], 1, "The standard phrase is “Unable RVSM due equipment”."),
Q(6, "An altitude deviation report is filed for a deviation from the cleared level of:", ["100 ft or more", "200 ft or more", "300 ft or more", "500 ft or more"], 2, "Deviations of 300 ft or more are reported."),
]

COURSE = dict(
    slug="rvsm-refresher",
    title="RVSM Refresher",
    header_title="RVSM Refresher",
    tagline="Reduced vertical separation minimum: airspace, equipment, procedures, contingencies, ACAS II and phraseology.",
    purpose="Refresh flight crew knowledge of RVSM operations in line with ICAO Doc 9574, PANS-ATM and EASA SPA.RVSM, as required for recurrent training.",
    audience="All flight crew. Full procedures apply to the Boeing 737-800; Q400 and Q200 crews take it for awareness of RVSM traffic, phraseology and ACAS II.",
    objectives=["Define RVSM airspace and the required equipment", "Plan and prepare an RVSM flight", "Apply en-route height-keeping procedures and altimeter checks",
                "Handle RVSM contingencies and special situations", "Use ACAS II version 7.1 correctly in RVSM airspace", "Use RVSM phraseology and reporting"],
    icon="runway", cert_prefix="RVSM", quiz_count=10, pass_mark=80,
    group="refresher", season="Summer",
    finale=None,
    modules=[dict(title="RVSM Operations", summary="Airspace, approval, planning and en-route procedures", icon="runway", lessons=range(1, 4)),
             dict(title="Contingencies, ACAS II and Phraseology", summary="Failures, turbulence, TCAS 7.1, phraseology and reporting", icon="people", lessons=range(4, 7))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Two airliners cruising 1,000 ft apart above the clouds", "RVSM: 1,000 ft between aircraft from FL290 to FL410."),
            2: ("gen", "Flight-deck view at dawn before departure", "Plan the RVSM flight: flight plan, MEL, weather and equipment."),
            3: ("gen", "Airliner in level cruise at high altitude", "Fly the cleared flight level with the autopilot altitude hold engaged."),
            4: ("gen", "Airliner cruising past mountain wave clouds", "Turbulence, mountain waves and equipment failures must be reported to ATC."),
            5: ("gen", "Two aircraft at adjacent levels", "Reduce vertical speed near the cleared level when traffic is at the adjacent level."),
            6: ("gen", "Two pilots on the flight deck", "Standard phraseology and reporting complete the RVSM picture.")},
)
