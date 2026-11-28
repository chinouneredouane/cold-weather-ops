"""CRM/TEM — Crew Resource Management and Threat and Error Management, initial and recurrent.

Built on the company OM D (MANEX D Ed. 04): 1.5 Human factors and CRM/TEM training (key elements, depth per course type,
12 h initial / 6 h recurrent, DCC, command course) and 2.4.5 recurrent CRM/TEM (all elements in depth over a 3-year cycle),
2.6.68 CRM/TEM non-technical skills assessment form.

Sources: company CRM 2024 presentation (diagrams); ICAO, "Threat and Error Management (TEM)", Capt. D. Maurino, CASS 2005;
Lund University School of Aviation, "CRM, TEM and Assessment of CRM Skills", report for the Swedish CAA (diagrams);
AOPA Luxembourg 2024 TEM presentation (Prepare–Repair–Recover model and TG461 case diagrams, airline logos removed);
TEM instructor booklet (Mentalpilote, ideas only — its pictures are not reproduced: private-use copyright).
Interactive parts: flip cards for definitions and countermeasures; TEM sorter (threat / error / undesired aircraft state)."""
from courses.perf_common import Q

_CO = "Domestic Airlines CRM course"
_ICAO = "ICAO — TEM, D. Maurino (CASS 2005)"
_LUSA = "Lund University School of Aviation, report for the Swedish CAA"
_AOPA = "AOPA Luxembourg TEM presentation (2024)"


def fig(img, caption, src=_CO):
    return (f'<figure class="lesson-figure"><img src="../media/images/{img}.jpg" alt="{caption}" loading="lazy">'
            f'<figcaption>{caption} <span class="muted">Source: {src}.</span></figcaption></figure>')


def cards(items, hint="Tap a card to turn it over.", quiz=False):
    out = []
    for front, sub, back in items:
        s = f"<small>{sub}</small>" if sub else ""
        out.append(f'<button type="button" class="flipcard" aria-pressed="false"><span class="fc-inner">'
                   f'<span class="fc-face fc-front">{front}{s}</span><span class="fc-face fc-back">{back}</span></span></button>')
    return f'<p class="flip-hint">{hint}</p><div class="flipcards{" quiz" if quiz else ""}">{"".join(out)}</div>'


_LBL = {"threat": "Threat", "error": "Error", "uas": "Undesired aircraft state"}


def sort(items):
    """TEM sorter. items: (situation, answer in threat/error/uas, explanation)."""
    out = []
    for text, ans, why in items:
        btns = "".join(f'<button type="button" data-c="{k}">{v}</button>' for k, v in _LBL.items())
        out.append(f'<div class="tem-item" data-answer="{ans}"><p class="tem-q">{text}</p><div class="tem-btns">{btns}</div>'
                   f'<p class="tem-why" hidden><b>{_LBL[ans]}</b> — {why}</p></div>')
    return ('<p class="flip-hint">Classify each situation: tap Threat, Error or Undesired aircraft state.</p>'
            f'<div class="tem-sort">{"".join(out)}<p class="tem-score" aria-live="polite"></p></div>')


LESSONS = [
# 1 ===================================================================== MODULE 1
dict(title="CRM: Origins, Generations and the OM D Programme", minutes=12,
objectives=["Explain why CRM was created.", "Describe the generations of CRM up to TEM.", "Describe the company CRM/TEM training programme in the OM D."],
body="""
<h2>Why CRM?</h2>
<p>The study of dozens of air disasters in the 1970s showed the large share of <strong>non-technical</strong> factors: the most frequent human errors concerned <strong>communication, decision making and leadership</strong> — not flying skill. Technically competent crews had accidents because the team did not work.</p>
<p>The first question CRM had to answer: how can a young, inexperienced co-pilot tell an experienced captain that he is wrong — and how can the captain listen? The same question applies to a junior cabin crew member and the senior cabin crew member.</p>
<h2>Generations of CRM</h2>
""" + fig("crm-gen1", "The beginnings: two pilots who interact — Cockpit Resource Management.") + """
<p>At the end of the 1980s CRM introduced the notion of a <strong>crew</strong> on the flight deck: Cockpit Resource Management became <strong>Crew</strong> Resource Management, with team building, stress management and situation awareness.</p>
""" + fig("crm-gen2", "Second generation: the crew on the flight deck.") + """
<h2>CRM is not only for pilots</h2>
<p>In the 1990s CRM extended to cabin crew, maintenance, dispatch and ATC. It was then understood as a way to improve <strong>teamwork</strong> — and teamwork is one of the means to the end: <strong>fewer errors in flight</strong>.</p>
""" + fig("crm-gen3", "CRM extended to other trades: cabin crew, maintenance, ground staff.") + """
<h2>Today: TEM</h2>
<p>The latest generation widens the pilot's view to the environment and to <strong>time</strong>: which threats could become errors or undesired states, and how to anticipate them? TEM grew out of CRM line observations, which showed that anticipation is a keystone of safety — a move from a reactive to a <strong>proactive</strong> approach.</p>
""" + cards([
    ("CRM", "Crew Resource Management", "The effective use of <b>all available resources</b> — people, equipment, information — to achieve a safe and efficient flight."),
    ("TEM", "Threat and Error Management", "A safety concept and model: detect and manage <b>threats</b>, <b>errors</b> and <b>undesired aircraft states</b> before they reduce safety margins."),
    ("Non-technical skills", "NTS", "Co-operation, leadership and management, situation awareness, decision making — the skills observed and assessed in CRM."),
    ("TEM is the goal", "", "<b>CRM is the way to it.</b> CRM skills are the countermeasures that make TEM work."),
]) + """
<h2>The company programme (OM D 1.5 and 2.4.5)</h2>
<table><thead><tr><th>Course</th><th>Duration</th></tr></thead><tbody>
<tr><td>Initial CRM/TEM (joining the company)</td><td>12 h</td></tr>
<tr><td>DCC — change of type</td><td>6 h</td></tr>
<tr><td>DCC — change of operator</td><td>6 h</td></tr>
<tr><td>Command course</td><td>9 h</td></tr>
<tr><td>Recurrent training</td><td>6 h each year; all initial elements in depth over a <strong>3-year cycle</strong></td></tr>
</tbody></table>
<p>The recurrent programme is updated from the results of crew CRM/TEM assessments. Crew members are <strong>not assessed</strong> on the CRM/TEM elements of recurrent training (OM D 2.4.5.2.5); CRM/TEM is observed in the simulator and on the line with the non-technical skills form (OM D 2.6.68).</p>
<h2>OM D key elements and this course</h2>
<table><thead><tr><th>OM D key element (1.5.3)</th><th>Lessons</th></tr></thead><tbody>
<tr><td>Human error and reliability; error chain; prevention and detection</td><td>2, 5</td></tr>
<tr><td>Company safety culture; SOPs; organisational factors</td><td>3</td></tr>
<tr><td>Threat and error management</td><td>4–7</td></tr>
<tr><td>Information acquisition and processing; situation awareness; workload management</td><td>8</td></tr>
<tr><td>Decision making; stress, stress management, fatigue and vigilance</td><td>9</td></tr>
</tbody></table>
<h2>OM D key elements and this course (2)</h2>
<table><thead><tr><th>OM D key element (1.5.3)</th><th>Lessons</th></tr></thead><tbody>
<tr><td>Communication and co-ordination inside and outside the flight deck; leadership and team behaviour; synergy</td><td>10</td></tr>
<tr><td>Automation and philosophy of the use of automation</td><td>11</td></tr>
<tr><td>Assessment of non-technical skills (2.6.68)</td><td>12</td></tr>
<tr><td>Case studies</td><td>7, 11, 13</td></tr>
</tbody></table>
""",
takeaways=["CRM was born from accidents caused by communication, decision and leadership failures.", "Cockpit → Crew → all trades → TEM: from reactive to proactive.",
           "OM D: initial 12 h, DCC 6 h, command 9 h, recurrent 6 h with every element in depth over 3 years."],
check=dict(q="According to the OM D, how long is the initial CRM/TEM course?", options=["6 h", "9 h", "12 h", "18 h"], answer=2, explain="12 h initial; 6 h recurrent and DCC; 9 h for the command course."),
),
# 2
dict(title="Human Error, Reliability and the Error Chain", minutes=12,
objectives=["Explain why human error is normal and how it is managed.", "Describe the error chain and the defences.", "Distinguish error causality from error management."],
body="""
<h2>Error is normal</h2>
<p>About 80 % of aviation accidents involve pilot error — committed by qualified, experienced and trained crews. Error is part of human performance: the aim is not zero error, but <strong>errors detected and managed before they matter</strong>.</p>
<h2>Human factors</h2>
<p>Human factors is the science of the interaction between people, technology and organisation. Its areas range from the human–machine interface to teams and communication, procedures and roles, training, organisation and staffing — and recovery from failures.</p>
""" + fig("hf-areas", "Areas of human factors: recovery from failures, human–machine interaction, organisation and staffing, training and development, procedures and roles, teams and communication.", _LUSA) + """
<h2>The error chain</h2>
<p>An accident is rarely one error. It is a <strong>chain</strong>: a threat, a first error, an error that is not detected, a second error, an undesired state, an outcome. Each link is an opportunity to break the chain. Defences exist at three moments:</p>
""" + fig("avoid-trap-mitigate", "Defences against threats and errors over time: avoid, trap, mitigate.", _LUSA) + cards([
    ("Avoid", "before", "Prevent the error: planning, briefing, SOPs, anticipation of threats."),
    ("Trap", "during", "Catch the error before it has consequences: monitoring, cross-checking, checklists, callouts."),
    ("Mitigate", "after", "Limit the consequences of an error that got through: recovery, go-around, emergency procedures."),
]) + """
<h2>From causality to management</h2>
<p>TEM looks less at <em>why</em> an error was made and more at <strong>whether it was detected and how the crew responded</strong>. An error detected and corrected in time — that does not lead to an undesired aircraft state — is operationally <strong>inconsequential</strong>. A <strong>mismanaged</strong> error is one that leads to another error or to an undesired aircraft state.</p>
""" + fig("tem-funnel", "Threats and errors, the strategies that resist and resolve them, and the consequence.", _LUSA) + """
<div class="callout info"><span class="label">Good practice</span><p>Expect errors — your own and your colleague's. Say what you do, check what the other does, and treat each detected error as a success of the crew, not a failure of a person.</p></div>
""",
takeaways=["Error is part of human performance; the goal is detection and management.", "Break the chain: avoid, trap, mitigate.",
           "A detected and corrected error is inconsequential; a mismanaged error leads to another error or a UAS."],
check=dict(q="What is a mismanaged error?", options=["Any error", "An error that leads to an additional error or an undesired aircraft state", "An error made by ATC", "An intentional violation only"], answer=1,
           explain="TEM defines a mismanaged error by its consequence: another error or a UAS."),
),
# 3
dict(title="Safety Culture, SOPs and Organisational Factors", minutes=11,
objectives=["Describe a positive safety culture.", "Explain the role of SOPs and the gap between procedures and reality.", "Recognise organisational (latent) threats."],
body="""
<h2>Safety culture</h2>
<p>The safety culture of a company is "how we do things here when nobody is watching". A positive culture is <strong>reporting</strong> (errors are reported), <strong>just</strong> (honest errors are not punished; reckless behaviour is), <strong>learning</strong> (data change the procedures and the training) and <strong>informed</strong> (management knows the real risks).</p>
<h2>SOPs</h2>
<p>Standard operating procedures make crews predictable to each other: any two pilots of the company can fly together. SOPs are systemic countermeasures — but they describe the work as <em>imagined</em>. Line observation (LOSA) and checks show the work as <em>done</em>.</p>
""" + fig("sop-reality", "From the SOP to reality: proficiency checks (OPC) and line observations (LOSA) reveal the gap between procedures and everyday operations.", _LUSA) + """
<h2>Organisational threats</h2>
<p>Organisational threats can be removed or minimised at source by the company. They are often <strong>latent</strong>: not visible from the flight deck until a safety analysis uncovers them.</p>
""" + cards([
    ("Operational pressure", "", "Delays, late arrivals, short turn-arounds, schedule changes."),
    ("Aircraft", "", "Malfunctions, automation anomalies, MEL/CDL items."),
    ("Cabin / maintenance / ground", "", "Cabin events, maintenance errors, ground handling and de-icing events."),
    ("Dispatch and documentation", "", "Paperwork errors, manual or chart errors, incomplete documentation."),
    ("Organisation", "", "Culture and organisational changes, crew scheduling, equipment design issues."),
    ("Crew remains the last line", "", "But the organisation has <b>earlier</b> opportunities to remove these threats — report them."),
]) + """
<div class="callout caution"><span class="label">Intentional non-compliance</span><p>Skipping a required checklist "because we are late" turns an organisational threat (pressure) into an error. Reporting the pressure is the professional answer; adapting the procedure on your own is not.</p></div>
""",
takeaways=["Positive culture: reporting, just, learning, informed.", "SOPs = systemic countermeasure; LOSA shows the gap between SOP and reality.",
           "Organisational threats are often latent — report them so they can be removed at source."],
check=dict(q="Who can remove organisational threats at source?", options=["Only the captain", "The aviation organisation itself", "ATC", "Nobody"], answer=1, explain="Organisational threats can be controlled by the organisation; crews remain the last line of defence."),
),
# 4 ===================================================================== MODULE 2 TEM
dict(title="The TEM Model and Threats", minutes=13,
objectives=["Describe the three components of the TEM model.", "Define a threat and its types (anticipated, unexpected, latent; environmental, organisational).",
            "Classify threats in practice."],
body="""
<h2>The TEM model</h2>
<p>The TEM model is a conceptual framework to understand, from an operational point of view, the relationship between safety and human performance in a dynamic context. It is <strong>descriptive</strong> (it captures normal operations) and <strong>diagnostic</strong> (it quantifies the context and the human response). It is used for accident analysis, line audits (LOSA), licensing and training.</p>
""" + fig("tem-model-prr", "TEM model: threats → errors → undesired aircraft state → accident/incident, with the barriers that return to safe operation: prepare, repair, recover.", _AOPA) + """
<h2>Threats</h2>
<p><strong>Threats</strong> are "events or errors that occur beyond the influence of the flight crew, increase operational complexity, and must be managed to maintain the margins of safety". Threats come <em>at</em> the crew; errors come <em>from</em> the crew.</p>
""" + cards([
    ("Anticipated threat", "expected or known", "Thunderstorms, icing, windshear forecast; congested airports; complex SIDs/STARs. <b>Brief them in advance.</b>"),
    ("Unexpected threat", "without warning", "In-flight malfunction, unforecast turbulence, ATC re-route, last-minute changes, sudden crew change, airport closure."),
    ("Latent threat", "not directly visible", "Organisational culture and changes, incorrect documentation, equipment design, operational pressure, optical illusions, fatigue, stress. Uncovered by safety analysis."),
    ("Environmental threat", "", "Weather, ATC, airport, terrain — managed in real time by the crew."),
    ("Organisational threat", "", "Pressure, aircraft, cabin, maintenance, ground, dispatch, documentation — can be removed at source by the organisation."),
]) + """
<h2>Examples of environmental threats</h2>
<ul>
  <li><strong>Weather</strong>: thunderstorms, turbulence, icing, windshear, cross/tailwind, very low or high temperatures.</li>
  <li><strong>ATC</strong>: traffic congestion, TCAS RA/TA, ATC error, language difficulty, non-standard phraseology, runway change, units (QFE, metres).</li>
  <li><strong>Airport</strong>: contaminated or short runway, confusing or faded signs, birds, aids unserviceable, construction.</li>
  <li><strong>Terrain</strong>: high ground, slope, lack of references, "black hole". <strong>Other</strong>: similar call signs.</li>
</ul>
<h2>Practice: is it a threat?</h2>
""" + sort([
    ("Thunderstorms are forecast at destination for the time of arrival.", "threat", "Anticipated environmental threat — brief the response before descent."),
    ("ATC changes the landing runway during the descent.", "threat", "Unexpected environmental threat (ATC) — re-brief, check the FMS and the performance."),
]) + """
<h2>Practice: is it a threat? (2)</h2>
""" + sort([
    ("A similar call sign is on the frequency.", "threat", "Environmental threat — listen carefully and confirm the call sign."),
    ("The load sheet arrives late and the crew is under pressure to leave on time.", "threat", "Organisational threat (operational pressure) — it can lead to errors if not managed."),
]) + """
<div class="callout info"><span class="label">Measure of success</span><p>Threat management is measured by whether threats are <strong>detected with enough anticipation</strong> to deploy countermeasures. It is the most proactive option to keep the margins of safety.</p></div>
""",
takeaways=["TEM model: threats, errors, undesired aircraft states — and countermeasures.", "Threats come at the crew: anticipated, unexpected, latent; environmental or organisational.",
           "Detect threats early enough to plan the countermeasures."],
check=dict(q="A threat is:", options=["An action of the crew that leads to a deviation", "An event outside the influence of the crew that increases complexity", "An aircraft deviation induced by the crew", "An accident"], answer=1,
           explain="Threats occur beyond the influence of the flight crew."),
),
# 5
dict(title="Errors and Error Management", minutes=12,
objectives=["Define a flight crew error.", "Classify errors: aircraft handling, procedural, communication.", "Describe error detection and response."],
body="""
<h2>Definition</h2>
<p><strong>Errors</strong> are "actions or inactions by the flight crew that lead to deviations from organisational or flight crew intentions or expectations". They reduce safety margins and increase the probability of adverse events. Errors can be spontaneous, linked to a threat, or part of an error chain.</p>
<h2>Three categories — by the primary interaction</h2>
""" + cards([
    ("Aircraft handling error", "the crew interacts with the aircraft", "Manual flying (vertical, lateral, speed deviations, flaps, speedbrakes, power); automation (wrong altitude, speed, heading, mode, entries); systems (packs, anti-ice, altimeter, fuel, speed bugs, frequency); ground navigation (wrong taxiway, too fast, failure to hold short)."),
    ("Procedural error", "the crew interacts with a procedure", "SOPs (no cross-verification of automation inputs); checklists (missed items, wrong time); callouts omitted; briefings omitted; documentation (wrong weight and balance, fuel, ATIS, clearance, logbook, MEL)."),
    ("Communication error", "the crew interacts with people", "Crew to external: missed calls, misinterpreted instructions, wrong read-back, wrong clearance/taxiway/runway. Pilot to pilot: miscommunication or misinterpretation."),
    ("Intentional non-compliance", "a sub-set", "Deliberate deviation from SOPs or regulations — inside any of the three categories, not a separate one."),
    ("Proficiency", "a sub-set", "Skill or knowledge deficiencies, training deficiencies — underlying any of the three categories."),
]) + """
<h2>Error management</h2>
<p>What matters is whether the error is <strong>detected</strong>, by whom, how the crew <strong>responds</strong>, and the <strong>outcome</strong>. Predictive monitoring identifies threats; <strong>reactive monitoring</strong> identifies errors. Systemic countermeasures (TCAS, GPWS, windshear warning, SOPs, checklists, briefings) and human-skill countermeasures (knowledge, monitoring, teamwork, workload management) resist and resolve errors.</p>
<h2>Practice: threat or error?</h2>
""" + sort([
    ("The PF selects a wrong altitude in the MCP after the clearance.", "error", "Aircraft handling error (automation) — trapped by the PM cross-check."),
    ("The crew misses an item of the before-take-off checklist.", "error", "Procedural error (checklist)."),
    ("The PM reads back the wrong runway and nobody notices.", "error", "Communication error (crew to external)."),
]) + """
<h2>Practice: threat or error? (2)</h2>
""" + sort([
    ("The controller gives a clearance into terrain by mistake.", "threat", "An ATC error is a <b>threat</b> for the flight crew — it is outside their influence."),
    ("The crew enters the zero-fuel weight in place of the take-off weight in the FMS.", "error", "Procedural error (documentation / data entry) — cross-check the performance data."),
]),
takeaways=["Errors come from the crew: actions or inactions leading to deviations.", "Handling, procedural, communication — by the primary interaction.",
           "Non-compliance and proficiency are sub-sets, not categories.", "Detect, respond, check the outcome."],
check=dict(q="The flight attendant makes an error that affects the flight. For the flight crew this is:", options=["A flight crew error", "A threat", "An undesired aircraft state", "An outcome"], answer=1,
           explain="Errors of other people (ATC, cabin, maintenance) are threats for the flight crew."),
),
# 6
dict(title="Undesired Aircraft States and Outcomes", minutes=11,
objectives=["Define an undesired aircraft state (UAS).", "Distinguish a UAS from an outcome.", "Explain why the crew must switch from error management to UAS management."],
body="""
<h2>Definition</h2>
<p><strong>Undesired aircraft states</strong> are "flight crew-induced aircraft position or speed deviations, misapplication of flight controls, or incorrect systems configuration, associated with a reduction in margins of safety". An upset caused by a sudden technical failure, with no crew contribution, is a <strong>threat</strong>, not a UAS.</p>
""" + cards([
    ("Aircraft handling UAS", "", "Attitude; vertical, lateral or speed deviations; unnecessary weather penetration; unauthorised airspace; outside limitations; <b>unstable approach</b>; continued landing after an unstable approach; long, floated, firm or off-centreline landing."),
    ("Ground navigation UAS", "", "Proceeding towards the wrong taxiway or runway; wrong taxiway, ramp, gate or hold spot."),
    ("Incorrect configuration UAS", "", "Systems, flight controls, automation, engine or weight and balance configuration incorrect."),
]) + """
<h2>UAS and outcome</h2>
<p>A UAS is a <strong>transitional</strong> state: the crew can still recover and restore the margins. An <strong>outcome</strong> is an end state: back to safe operation, an additional error, or an incident/accident. Example: stabilised approach (normal) → unstable approach (UAS) → runway excursion (outcome).</p>
<h2>Switch to UAS management</h2>
<p>A crew selects a wrong approach in the FMC, sees it before the FAF, and both pilots start reprogramming. The aircraft goes through the localiser, descends late and becomes unstable. They were <strong>locked in error management</strong>. When the aircraft is in an undesired state, the first task is to <strong>fly the aircraft</strong> — basic modes or manual — and recover the state; fix the error later.</p>
""" + fig("tem-past-present-future", "Dealing with threats is predicting the future; dealing with errors is correcting the past; dealing with a UAS is managing the present.", _AOPA) + """
<h2>Practice: error or UAS?</h2>
""" + sort([
    ("The approach is unstable at 500 ft: 15 kt fast and above the glide path.", "uas", "Aircraft handling UAS — go around."),
    ("The crew forgets to arm the speedbrakes before landing.", "error", "Procedural error — it becomes a UAS only if the configuration is wrong when it matters."),
    ("The aircraft lines up on a taxiway instead of the runway for take-off.", "uas", "Ground navigation UAS — stop and verify."),
]) + """
<h2>Practice: error or UAS? (2)</h2>
""" + sort([
    ("Flaps not set for take-off when starting the take-off roll.", "uas", "Incorrect configuration UAS (the warning is a systemic countermeasure)."),
    ("Severe turbulence suddenly rolls the aircraft past 45° of bank.", "threat", "No crew contribution: a threat. A UAS appears only if the crew response creates the deviation."),
]),
takeaways=["UAS: crew-induced deviation or configuration reducing margins.", "UAS is transitional; an outcome is final.",
           "Fly the aircraft first: switch from error management to UAS management."],
check=dict(q="An unstable approach is:", options=["A threat", "An error", "An undesired aircraft state", "An outcome"], answer=2, explain="It is a crew-induced aircraft state reducing margins — still recoverable by a go-around."),
),
# 7
dict(title="Countermeasures and a TEM Case Study", minutes=14,
objectives=["Distinguish systemic and individual/team countermeasures.", "Apply planning, execution and review countermeasures.", "Analyse a case with the TEM model."],
body="""
<h2>Countermeasures</h2>
<p>Up to <strong>70 %</strong> of crew activity may be countermeasure-related. <strong>Systemic</strong> countermeasures are "hard" resources in place before the flight: ACAS, GPWS, SOPs, checklists, briefings, training. <strong>Individual and team</strong> countermeasures are the skills, knowledge and attitudes developed by CRM training.</p>
""" + cards([
    ("SOP briefing", "Planning", "Concise, not rushed, interactive; bottom lines established."),
    ("Plans stated", "Planning", "Plans and decisions communicated and acknowledged — everybody on the same page."),
    ("Workload assignment", "Planning", "Roles and responsibilities defined for normal and non-normal situations."),
    ("Contingency management", "Planning", "Threats and their consequences anticipated; all resources used."),
]) + """
<h2>Execution and review countermeasures</h2>
""" + cards([
    ("Monitor / cross-check", "Execution", "Aircraft position, settings and crew actions verified."),
    ("Workload management", "Execution", "Tasks prioritised; no task fixation; no overload."),
    ("Automation management", "Execution", "Automation set-up briefed; effective recovery from automation anomalies."),
    ("Evaluation of plans", "Review", "Plans reviewed and modified when necessary; decisions openly analysed."),
    ("Inquiry", "Review", "Ask questions to clarify plans; nothing taken for granted."),
    ("Assertiveness", "Review", "Critical information stated with appropriate persistence; speak up without hesitation."),
]) + """
<h2>Prepare – Repair – Recover</h2>
<ul>
  <li><strong>Prepare</strong> (threats): identify and prepare — <strong>verbalise, verify, monitor</strong> (threat briefing, situation awareness, FOR-DEC).</li>
  <li><strong>Repair</strong> (errors): identify and repair — <strong>resist, resolve</strong>.</li>
  <li><strong>Recover</strong> (UAS): identify and recover — <strong>switch to UAS recovery</strong>, upset recovery techniques.</li>
</ul>
<h2>Case study: B777 non-precision approach, night</h2>
<p>VOR approach, good visibility, autopilot in LNAV/VNAV, first officer flying. The approach ended about 1,000 ft below the path at 6.4 NM, and the go-around instruction from the tower was followed about 50 seconds late.</p>
""" + fig("tg461-55", "Threat: being below the path on a non-precision approach. Tool: predictive monitoring and enhanced situation awareness.", _AOPA) + fig("tg461-57", "Error: the crew interprets an autopilot malfunction and starts a descent without controlling the rate of descent.", _AOPA) + fig("tg461-58", "Trigger: use of FLCH (LVL CHG) for the approach — not to be used on final approach below 1,000 ft.", _AOPA) + fig("tg461-59", "UAS: aircraft below the profile.", _AOPA) + """
<h2>Classify the chain</h2>
""" + sort([
    ("At 3,300 ft the autopilot changes from VNAV SPEED to VNAV PATH and starts a climb to intercept the computed path.", "threat", "Automation behaviour not anticipated by the crew: an <b>automation surprise</b> — a threat."),
    ("The crew changes the target altitude to 970 ft and selects FLCH for the descent.", "error", "Aircraft handling error (automation mode) against the procedure."),
]) + """
<h2>Classify the chain (2)</h2>
""" + sort([
    ("The aircraft is about 1,000 ft below the approach path at 6.4 NM.", "uas", "Aircraft handling UAS — recover the flight path."),
    ("The tower instructs a go-around; the crew replies 'climbing' but continues for about 50 seconds.", "error", "Communication and procedural error — a go-around instruction must be followed promptly."),
]) + """
<h2>Lessons of the case</h2>
<div class="callout warn"><span class="label">Lessons</span><p>Monitor the flight path closely; cross-check actual against published altitudes; use appropriate automation modes; redirect attention to the priority task; follow a go-around instruction promptly.</p></div>
""",
takeaways=["Systemic + individual/team countermeasures; about 70 % of crew activity.", "Planning, execution, review countermeasures.",
           "Prepare (threats), repair (errors), recover (UAS)."],
check=dict(q="Which is a REVIEW countermeasure?", options=["SOP briefing", "Monitoring and cross-checking", "Inquiry and assertiveness", "Workload assignment"], answer=2,
           explain="Review: evaluation of plans, inquiry, assertiveness."),
),
# 8 ===================================================================== MODULE 3 NTS
dict(title="Situation Awareness, Information Processing and Workload", minutes=12,
objectives=["Define situation awareness and its three levels.", "Describe how information is acquired and processed.", "Apply workload management."],
body="""
<h2>The CRM skills</h2>
""" + fig("crm-skills-wheel", "Crew Resource Management skills: communication, leadership and management, co-operation, situation awareness, decision making.") + """
<h2>Situation awareness</h2>
""" + cards([
    ("Level 1 — Perceive", "", "Gather the relevant information: instruments, outside, radio, crew, cabin."),
    ("Level 2 — Understand", "", "Give it meaning: what does this mean for my flight?"),
    ("Level 3 — Project", "", "Anticipate: what will happen next, and what will I do if…?"),
    ("Loss of SA", "warning signs", "Ambiguity, confusion, fixation, nobody flying, deviations, unresolved discrepancies, \"what is it doing now?\"."),
]) + """
<p>The best situation awareness keeps the smallest gap between the crew's picture and reality. The NOTECHS elements are: <strong>awareness of aircraft systems, of the external environment, and of time</strong>.</p>
<h2>Information acquisition and processing</h2>
<ul>
  <li>Attention is limited: we sample information, and under stress the sampling narrows.</li>
  <li>Expectation shapes perception: we hear the clearance we expect, and see the runway we expect.</li>
  <li>Verbalise: thinking aloud lets the other pilot check your picture ("verbalise, verify, monitor").</li>
  <li>Use "What if…?" to keep projecting ahead.</li>
</ul>
<h2>Workload management</h2>
<p>Priorities do not change: <strong>aviate, navigate, communicate, manage systems</strong>. Plan the high-workload phases early (briefings before top of descent), delegate tasks, use the automation level that reduces workload, and say when you are saturated. Avoid task fixation: one pilot always flies the aircraft.</p>
<div class="callout caution"><span class="label">Under-load</span><p>Low workload is also a threat: vigilance drops on long cruise phases at night. Keep monitoring routines and planned cross-checks.</p></div>
""",
takeaways=["SA: perceive, understand, project.", "Awareness of systems, environment and time.", "Aviate, navigate, communicate — plan, delegate, avoid fixation."],
check=dict(q="Which is the third level of situation awareness?", options=["Perception", "Comprehension", "Projection — anticipating the future", "Communication"], answer=2, explain="Perceive, understand, project."),
),
# 9
dict(title="Decision Making, Stress, Fatigue and Vigilance", minutes=12,
objectives=["Apply a structured decision-making model.", "Recognise the effects of stress and manage them.", "Manage fatigue and vigilance."],
body="""
<h2>Decision making</h2>
<p>NOTECHS assesses three elements: <strong>problem definition and diagnosis, option generation, risk assessment and option selection</strong>. A structured model helps when time allows:</p>
""" + cards([
    ("F — Facts", "FOR-DEC", "What is the situation? Gather the facts with the other crew members."),
    ("O — Options", "FOR-DEC", "What can we do? Generate more than one option."),
    ("R — Risks", "FOR-DEC", "What are the risks and benefits of each option?"),
    ("DE — Decision", "FOR-DEC", "Decide — the captain decides, the crew agrees."),
    ("E — Execution", "FOR-DEC", "Who does what, when?"),
    ("C — Check", "FOR-DEC", "Is the decision still right? Review."),
]) + """
<h2>Traps in decisions</h2>
<ul>
  <li><strong>Plan continuation</strong> ("get-there-itis"): the destination becomes the goal; signs of deterioration are ignored.</li>
  <li><strong>Confirmation bias</strong>: we look for information that supports what we already think.</li>
  <li><strong>Illusion of experience</strong>: years without an event make us underestimate risk.</li>
  <li><strong>Pressure</strong>: time, commercial or social pressure pushes to accept more risk. Know how to say no.</li>
  <li>Always keep a <strong>plan B</strong> — and a plan C.</li>
</ul>
<h2>Stress</h2>
<p>Some stress improves performance; too much narrows attention, slows perception, and makes us fall back on routines that may not fit the situation ("regression"). Under high stress: slow down, follow the priorities, use the checklist, share the load, verbalise.</p>
<h2>Fatigue and vigilance</h2>
<p>Fatigue causes errors — slower reactions, poorer decisions, micro-sleeps. Know the window of circadian low (WOCL), use the company fatigue procedures, and use controlled rest only as the OM allows. Report fatigue: being unfit to fly is a professional decision. See also the Algerian Regulations and Duty Time course.</p>
""",
takeaways=["FOR-DEC: facts, options, risks, decision, execution, check.", "Watch plan continuation, confirmation bias, pressure; keep a plan B.",
           "Stress narrows attention; fatigue causes errors — manage and report."],
check=dict(q="What is 'plan continuation'?", options=["Good planning", "Continuing the original plan despite signs that it should change", "A NOTECHS element", "A checklist"], answer=1,
           explain="Get-there-itis — a major factor in weather and unstable approach accidents."),
),
# 10
dict(title="Communication, Leadership, Teamwork and Synergy", minutes=12,
objectives=["Apply effective communication inside and outside the flight deck.", "Use authority and assertiveness appropriately.", "Build and maintain an effective team."],
body="""
<h2>Communication</h2>
<ul>
  <li>Clear, concise, standard phraseology; closed loop: message → read-back → confirmation.</li>
  <li>Inside the flight deck: share the plan, the intentions, the doubts. Outside: ATC, cabin crew, maintenance, dispatch, ground staff.</li>
  <li>Barriers: hierarchy, culture, language, noise, workload, assumptions.</li>
</ul>
<h2>Speaking up</h2>
<p>How does a young first officer tell an experienced captain that he is wrong? With a graded, persistent message:</p>
""" + cards([
    ("1. Get attention", "", "\"Captain…\""),
    ("2. State the concern", "", "\"We are 20 knots fast and above the path…\""),
    ("3. State the problem", "", "\"…we will not be stable at 500 feet…\""),
    ("4. Propose a solution", "", "\"…I suggest we go around.\""),
    ("5. Obtain agreement", "", "\"Do you agree?\" — and repeat, more firmly, if needed."),
]) + """
<h2>Leadership and authority</h2>
<p>NOTECHS leadership and managerial skills: <strong>use of authority and assertiveness, providing and maintaining standards, planning and co-ordination, workload management</strong>. The cockpit gradient should be neither too steep (the first officer does not dare to speak) nor too flat (nobody decides). The captain sets the tone in the briefing: "If you see anything you don't like, tell me."</p>
<h2>Co-operation and synergy</h2>
<p>NOTECHS co-operation: <strong>team building and maintaining, consideration of others, support of others, conflict solving</strong>. Synergy: a crew performs better than the sum of its members when information is shared and every member is used.</p>
<h2>Practice: communication</h2>
""" + sort([
    ("ATC clears 'descend FL120'; the PM reads back 'FL110' and the controller does not correct it.", "error", "Communication error by the crew — and the uncorrected read-back is an ATC threat. Closed-loop communication traps it."),
    ("The cabin crew does not report smoke smell because 'the pilots are busy'.", "threat", "For the flight crew, a cabin event not reported is a threat; the cure is a joint briefing that invites communication."),
]),
takeaways=["Closed-loop, standard, shared communication.", "Speak up: attention, concern, problem, solution, agreement.",
           "Balanced authority gradient; co-operation, support, conflict solving."],
check=dict(q="Which is NOT a NOTECHS leadership/managerial element?", options=["Use of authority and assertiveness", "Planning and co-ordination", "Awareness of time", "Workload management"], answer=2,
           explain="Awareness of time belongs to situation awareness."),
),
# 11
dict(title="Automation and the Philosophy of its Use", minutes=11,
objectives=["Define an automation surprise.", "Apply the company philosophy of automation use.", "Recognise when to downgrade the level of automation."],
body="""
<h2>Automation surprise</h2>
<p>An <strong>automation surprise</strong> is a behaviour of the automation not anticipated by the pilot. It may come from internal logic, inadequate manipulation, lack of transparency or lack of understanding, and it can seriously load the pilot's cognitive capacity — "what is it doing now?".</p>
<h2>Principles</h2>
<ul>
  <li><strong>Brief the automation</strong>: who sets what, which modes are planned for the approach.</li>
  <li><strong>Verbalise and verify the FMA</strong>: every mode change is announced and checked.</li>
  <li><strong>Use the appropriate level</strong>: the highest level that reduces workload is not always the best; if the automation does not do what you want, <strong>take a lower level</strong> — basic modes or manual flight.</li>
  <li><strong>Cross-check entries</strong>: performance data, FMS routes and approach selection are verified by the other pilot.</li>
  <li>Keep <strong>manual flying skills</strong>: see the UPRT course.</li>
</ul>
<h2>Back to the B777 case</h2>
""" + fig("tg461-56", "Trigger: the autopilot captures VNAV PATH and starts a climb — an automation surprise.", _AOPA) + fig("tg461-60", "Trigger: failure to comply with the instruction to go around.", _AOPA) + cards([
    ("What should the crew have done?", "", "Verbalise the FMA change, understand VNAV PATH logic, keep VNAV or use V/S with path monitoring, and never FLCH on final below 1,000 ft."),
    ("When the aircraft was low?", "", "Switch from error management to UAS management: fly the path, stop the descent, go around."),
], hint="Think, then tap.", quiz=True),
takeaways=["Automation surprise = unanticipated behaviour; ask 'what is it doing now?'.", "Brief, verbalise, verify the FMA; cross-check entries.",
           "If the automation does not do what you want, take a lower level."],
check=dict(q="The automation does something you do not understand on final approach. Best action?", options=["Keep reprogramming the FMS", "Take a lower level of automation and fly the path; go around if needed", "Ignore it", "Ask ATC"], answer=1,
           explain="Fly the aircraft first — reduce the level of automation."),
),
# 12 ==================================================================== MODULE 4
dict(title="Assessing Non-Technical Skills (NOTECHS)", minutes=11,
objectives=["Describe the four NOTECHS categories and their elements.", "Use the rating scale of the company form (OM D 2.6.68).",
            "Explain the observation and feedback cycle."],
body="""
<h2>The four categories</h2>
""" + fig("notechs-elements", "NOTECHS element checklist: co-operation, leadership and managerial skills, situation awareness, decision making.", _LUSA) + cards([
    ("Co-operation", "", "Team building and maintaining · consideration of others · support of others · conflict solving."),
    ("Leadership and managerial skills", "", "Use of authority and assertiveness · providing and maintaining standards · planning and co-ordination · workload management."),
    ("Situation awareness", "", "Awareness of aircraft systems · of the external environment · of time."),
    ("Decision making", "", "Problem definition and diagnosis · option generation · risk assessment and option selection."),
]) + """
<h2>The rating scale</h2>
<p>The company form (OM D 2.6.68) rates each crew member by sector or simulator session, from very poor to very good, with comments:</p>
""" + fig("notechs-scale", "Rating scale: very poor — behaviour directly endangered flight safety; poor — could endanger; acceptable — does not endanger but needs improvement; good — enhances safety; very good — optimally enhances safety, an example for other pilots.", _LUSA) + """
<h2>Principles of assessment</h2>
<ul>
  <li>Only <strong>observable behaviour</strong> is rated — not personality or attitude.</li>
  <li>A rating must be linked to a <strong>technical consequence</strong> to be "unacceptable".</li>
  <li>Repeated behaviour is needed to conclude a problem.</li>
  <li>The behaviour must be explained in the debriefing.</li>
</ul>
""" + fig("crm-eval-cycle", "Observations of CRM skills feed the evaluation of the observations and of CRM training, which updates the CRM training.", _LUSA) + """
<div class="callout info"><span class="label">In the company</span><p>Recurrent CRM/TEM elements are not assessed; non-technical skills are observed by TRI/TRE in simulator and line checks, and the recurrent programme is updated from these crew assessments (OM D 2.4.5).</p></div>
""",
takeaways=["NOTECHS: co-operation, leadership/managerial, situation awareness, decision making.", "Rate observable behaviour, with the technical consequence.",
           "Observations update the training — a continuous cycle."],
check=dict(q="'Option generation' belongs to which NOTECHS category?", options=["Co-operation", "Leadership", "Situation awareness", "Decision making"], answer=3, explain="Decision making: problem definition, option generation, risk assessment and selection."),
),
# 13
dict(title="Case Studies: CRM That Saved the Day", minutes=12,
objectives=["Analyse three events where CRM contributed to a safe outcome.", "Identify the threats, errors, UAS and countermeasures in each."],
body="""
<h2>Qantas 32 — A380, uncontained engine failure (2010)</h2>
<p>After an uncontained failure of engine 2 shortly after take-off from Singapore, the crew faced dozens of ECAM messages. With five pilots on the flight deck, they shared the workload, verified the systems status, calculated the landing performance and landed safely. All 469 occupants survived. The FAA described the crew performance as an example of CRM at its best.</p>
""" + cards([
    ("Threats", "", "Engine explosion, multiple system failures, fuel leaks, heavy weight, degraded braking."),
    ("Countermeasures", "", "Fly first, then manage; clear leadership; delegation; cross-checking the ECAM against reality; performance verification; no rush."),
]) + """
<h2>Northwest 85 — B747-400, rudder hard-over (2002)</h2>
<p>Over the Bering Sea, a lower rudder jammed. For tens of minutes the crew fought to keep the aircraft stable, then diverted and landed in Anchorage. The captain said it was "a classic application of CRM": four pilots shared the physical and mental work and kept everyone informed.</p>
""" + cards([
    ("Threat", "", "Sudden rudder hard-over — a technical failure, not a UAS."),
    ("Countermeasures", "", "Workload sharing between four pilots; communication with company and ATC; planning the diversion and the landing."),
]) + """
<h2>US Airways 1549 — A320, Hudson River (2009)</h2>
<p>After a bird strike caused the loss of both engines, the crew ditched in the Hudson River; all 155 occupants survived. The NTSB noted that crew teamwork and CRM contributed to the outcome: the captain flew, the first officer ran the checklist, and decisions were made in seconds.</p>
""" + cards([
    ("Threats", "", "Birds, dual engine failure, low altitude, dense urban area."),
    ("Countermeasures", "", "Clear task sharing (\"my aircraft\"), checklist use, rapid decision on the best option, cabin crew coordination."),
]) + """
<h2>Your turn</h2>
""" + sort([
    ("A bird strike causes the loss of both engines.", "threat", "An external event beyond the crew's influence."),
    ("Both pilots try to restart the engines and nobody flies the aircraft.", "error", "A workload management error — the countermeasure is task sharing: one flies."),
    ("The aircraft decelerates below the minimum speed during the troubleshooting.", "uas", "A crew-induced speed deviation reducing margins."),
]),
takeaways=["In every case: fly first, share the workload, communicate, decide, verify.", "CRM turns individual skills into crew performance.",
           "Use TEM to analyse any event: threats, errors, UAS, countermeasures."],
check=dict(q="What did the three crews have in common?", options=["Luck only", "Clear task sharing, communication and structured decisions", "Automation alone", "No checklists"], answer=1,
           explain="CRM skills: leadership, workload sharing, communication and decision making."),
),
]

QUESTIONS = [
Q(1, "CRM was created after studies showed that most accidents involved failures of:", ["Engines", "Communication, decision making and leadership", "Navigation equipment", "Weather forecasting"], 1, "Non-technical skills."),
Q(1, "In the OM D, the recurrent CRM/TEM course lasts:", ["2 h", "6 h", "9 h", "12 h"], 1, "6 h, all elements in depth over 3 years."),
Q(1, "Are crew members assessed on the CRM/TEM elements of recurrent training?", ["Yes, with a written test", "No (OM D 2.4.5.2.5)", "Only captains", "Only after an incident"], 1, "They are not assessed."),
Q(1, "In the 1980s, 'Cockpit' Resource Management became:", ["Cabin Resource Management", "Crew Resource Management", "Company Resource Management", "Control Resource Management"], 1, "The crew notion was introduced."),
Q(2, "Which sequence describes the defences against error over time?", ["Trap, avoid, mitigate", "Avoid, trap, mitigate", "Mitigate, trap, avoid", "Detect, report, punish"], 1, "Avoid, then trap, then mitigate."),
Q(2, "An error detected and corrected before it leads to a UAS is:", ["An accident", "Operationally inconsequential", "Always reportable", "A threat"], 1, "Proper error management."),
Q(3, "LOSA is used to:", ["Punish crews", "Observe normal operations and see the gap between SOPs and reality", "Replace checks", "Train ATC"], 1, "Line Operations Safety Audit."),
Q(3, "Operational pressure (delays, short turn-around) is:", ["An environmental threat", "An organisational threat", "A crew error", "A UAS"], 1, "Organisational, often latent."),
Q(4, "Threats come ____ the crew; errors come ____ the crew.", ["from / at", "at / from", "from / from", "at / at"], 1, "Threats come at the crew; errors come from the crew."),
Q(4, "Optical illusions and equipment design issues are examples of:", ["Anticipated threats", "Latent threats", "Errors", "UAS"], 1, "Latent threats."),
Q(4, "A forecast of thunderstorms at destination is:", ["An unexpected threat", "An anticipated threat", "An error", "A UAS"], 1, "Brief it in advance."),
Q(5, "Error categories in the TEM model are based on:", ["The phase of flight", "The primary interaction at the moment of the error", "The seniority of the pilot", "The aircraft type"], 1, "Aircraft handling, procedural, communication."),
Q(5, "A wrong read-back of a clearance is:", ["Aircraft handling error", "Procedural error", "Communication error", "Threat"], 2, "Crew to external communication."),
Q(5, "A missed checklist item is:", ["Communication error", "Procedural error", "UAS", "Threat"], 1, "Procedural error."),
Q(5, "An error by the controller is, for the flight crew:", ["A crew error", "A threat", "A UAS", "An outcome"], 1, "Outside the crew's influence."),
Q(6, "An unstable approach is:", ["A threat", "An error", "An undesired aircraft state", "An accident"], 2, "Transitional state — go around."),
Q(6, "The difference between a UAS and an outcome is that a UAS is:", ["Final", "Transitional and still recoverable", "Always an accident", "Not crew-induced"], 1, "Outcome = end state."),
Q(6, "When the aircraft is in an undesired state, the crew should first:", ["Find the cause of the error", "Manage the UAS — fly the aircraft", "Call maintenance", "Write a report"], 1, "Switch to UAS management."),
Q(7, "About what share of crew activity may be countermeasure-related?", ["10 %", "30 %", "70 %", "100 %"], 2, "Up to 70 %."),
Q(7, "TCAS, GPWS and checklists are:", ["Individual countermeasures", "Systemic countermeasures", "Threats", "Errors"], 1, "Hard resources in the system."),
Q(7, "'Plans stated' and 'workload assignment' are:", ["Planning countermeasures", "Execution countermeasures", "Review countermeasures", "Threats"], 0, "Planning."),
Q(7, "Monitoring and cross-checking is a/an:", ["Planning countermeasure", "Execution countermeasure", "Review countermeasure", "Systemic countermeasure only"], 1, "Execution."),
Q(8, "The three levels of situation awareness are:", ["See, say, do", "Perceive, understand, project", "Plan, act, review", "Aviate, navigate, communicate"], 1, "Perception, comprehension, projection."),
Q(8, "The priorities of workload management are:", ["Communicate, navigate, aviate", "Aviate, navigate, communicate, manage systems", "Systems first", "Cabin first"], 1, "Fly the aircraft first."),
Q(9, "In FOR-DEC, 'R' stands for:", ["Radio", "Risks", "Report", "Review"], 1, "Facts, Options, Risks, Decision, Execution, Check."),
Q(9, "High stress tends to:", ["Widen attention", "Narrow attention and slow perception", "Improve all decisions", "Have no effect"], 1, "Tunnel vision and regression to routines."),
Q(9, "Get-there-itis is a form of:", ["Good airmanship", "Plan continuation bias", "Fatigue", "Automation surprise"], 1, "Plan continuation."),
Q(10, "In a graded speaking-up message, after stating the concern and the problem you should:", ["Stop", "Propose a solution and obtain agreement", "Take the controls", "Call ATC"], 1, "Solution and agreement."),
Q(10, "A too steep authority gradient means:", ["Nobody decides", "The first officer does not dare to speak up", "The crew is perfect", "ATC is in charge"], 1, "Balance is needed."),
Q(10, "Conflict solving belongs to which NOTECHS category?", ["Co-operation", "Leadership", "Situation awareness", "Decision making"], 0, "Co-operation."),
Q(11, "An automation surprise is:", ["A failure of the autopilot", "A behaviour of the automation not anticipated by the pilot", "A TCAS RA", "An ATC error"], 1, "Unanticipated behaviour."),
Q(11, "If the automation does not do what you want on final approach:", ["Keep reprogramming", "Take a lower level of automation and fly the path", "Disconnect everything and wait", "Ask the cabin crew"], 1, "Fly the aircraft first."),
Q(12, "NOTECHS has how many categories?", ["2", "4", "6", "8"], 1, "Co-operation, leadership/managerial, situation awareness, decision making."),
Q(12, "'Very poor' on the rating scale means the behaviour:", ["Needs improvement", "Directly endangered flight safety", "Enhanced safety", "Was not observed"], 1, "Very poor = directly endangered safety."),
Q(12, "CRM assessment should rate:", ["Personality", "Observable behaviour", "Rank", "Experience"], 1, "Only observable behaviour."),
Q(13, "In US Airways 1549, the bird strike was:", ["A crew error", "A threat", "A UAS", "An outcome"], 1, "External event beyond the crew's influence."),
Q(13, "The common factor in QF32, NW85 and US1549 is:", ["Automation alone", "Effective CRM: task sharing, communication, decisions", "Luck", "Short flights"], 1, "CRM made the difference."),
]

COURSE = dict(
    slug="crm-tem",
    title="CRM/TEM — Initial and Recurrent",
    header_title="CRM/TEM",
    tagline="Crew Resource Management and Threat and Error Management following the OM D: human error, safety culture, the TEM model with interactive threat/error/UAS exercises, situation awareness, decision making, communication, automation, NOTECHS and case studies.",
    purpose="Deliver the company CRM/TEM training of OM D 1.5 (initial 12 h, DCC 6 h, command 9 h) and 2.4.5 (recurrent 6 h, all elements in depth over a 3-year cycle) in e-learning form, to increase crew communication and management skills and the practical use of TEM.",
    audience="Flight crew of all fleets (B737-800, Q400, Q200); cabin crew and operations staff for the common elements.",
    objectives=["Explain human error and the error chain", "Describe safety culture and organisational factors", "Apply the TEM model: threats, errors, undesired aircraft states, countermeasures",
                "Maintain situation awareness and manage workload", "Make structured decisions under stress and fatigue", "Communicate, lead and co-operate as a crew",
                "Use automation according to the company philosophy", "Understand NOTECHS assessment", "Analyse case studies with TEM"],
    icon="people", cert_prefix="CRM", quiz_count=20, pass_mark=80,
    group="refresher", season="Additional",
    finale=None,
    modules=[dict(title="CRM Foundations", summary="Origins and programme, human error and reliability, safety culture and SOPs", icon="people", lessons=range(1, 4)),
             dict(title="Threat and Error Management", summary="The TEM model, threats, errors, undesired aircraft states, countermeasures — interactive", icon="search", lessons=range(4, 8)),
             dict(title="Non-Technical Skills", summary="Situation awareness and workload, decision making, stress and fatigue, communication and leadership, automation", icon="people", lessons=range(8, 12)),
             dict(title="Assessment and Case Studies", summary="NOTECHS and three CRM case studies", icon="plane", lessons=range(12, 14))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("photo", "Generations of CRM", "Generations of CRM."), 2: ("photo", "Areas of human factors", "Areas of human factors."), 3: ("photo", "From SOP to reality", "From SOP to reality."), 4: ("photo", "The TEM model", "The TEM model."), 5: ("photo", "Threats, errors and strategies", "Threats, errors and strategies."), 6: ("photo", "Past, present, future", "Past, present, future."), 7: ("photo", "Avoid, trap, mitigate", "Avoid, trap, mitigate."), 8: ("photo", "Crew Resource Management skills", "Crew Resource Management skills."), 9: ("photo", "Two pilots who interact", "Two pilots who interact."), 10: ("photo", "CRM extended to other trades", "CRM extended to other trades."), 11: ("photo", "Automation surprise", "Automation surprise."), 12: ("photo", "NOTECHS elements", "NOTECHS elements."), 13: ("photo", "Observation and training cycle", "Observation and training cycle.")},
)
