"""CPDLC course (additional recurrent course). Based on the company CPDLC presentation, updated:
EU data link rules now in Commission Implementing Regulation (EU) 2023/1770 (which repealed Regulation (EC) No 29/2009),
and ICAO Doc 10037 (GOLD) added as the global operational reference."""
from courses.upset_recovery.diagrams import FONT, INK, MUTED, LINE, GREEN, GREEN_D, RED, AMBER, BLUE, arrow_defs


def exchange_diagram():
    svg = f"""{arrow_defs(9)}
<rect x="20" y="40" width="170" height="210" rx="14" fill="{BLUE}" opacity=".12" stroke="{BLUE}"/>
<text x="105" y="30" text-anchor="middle" font-weight="700" fill="{BLUE}">Controller (ATSU)</text>
<rect x="510" y="40" width="170" height="210" rx="14" fill="{GREEN}" opacity=".12" stroke="{GREEN}"/>
<text x="595" y="30" text-anchor="middle" font-weight="700" fill="{GREEN_D}">Flight deck</text>
<g font-size="13">
<path d="M190 75 L508 75" stroke="{BLUE}" stroke-width="3" marker-end="url(#ar9)"/><text x="350" y="68" text-anchor="middle">1. Uplink: CLIMB TO FL360</text>
<path d="M510 120 L192 120" stroke="{AMBER}" stroke-width="3" marker-end="url(#ar9)"/><text x="350" y="113" text-anchor="middle">2. Downlink (optional): STANDBY</text>
<path d="M510 165 L192 165" stroke="{GREEN}" stroke-width="3" marker-end="url(#ar9)"/><text x="350" y="158" text-anchor="middle">3. Downlink: WILCO — dialogue closed</text>
<path d="M190 215 L508 215" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#ar9)"/><text x="350" y="208" text-anchor="middle" fill="{MUTED}">technical acknowledgement / message status in the ATC log</text>
</g>
<text x="350" y="285" text-anchor="middle" fill="{RED}" font-weight="700">Read the whole message, cross-check with the other pilot, then respond — and only then act.</text>"""
    return f"""<figure class="diagram"><svg viewBox="0 0 700 300" role="img" aria-label="CPDLC dialogue"><title>A CPDLC dialogue</title>
<desc>An uplink clearance, an optional STANDBY and a WILCO response that closes the dialogue.</desc>
<g {FONT} font-size="13" fill="{INK}">{svg}</g></svg>
<figcaption>A typical CPDLC dialogue. The response closes the dialogue; STANDBY keeps it open.</figcaption></figure>"""


LESSONS = [
dict(title="CPDLC: Definition, References and Benefits", minutes=7,
objectives=["Define CPDLC and describe its purpose.", "Identify the ICAO and European references.", "List the expected benefits and limitations."],
body="""
<h2>Definition</h2>
<p><strong>Controller–Pilot Data Link Communications (CPDLC)</strong> is a means of communication between controller and pilot using data link for ATC communications (ICAO Doc 4444, PANS-ATM). It is a two-way system by which controllers can send <strong>non-urgent, strategic messages</strong> to an aircraft as an alternative to voice. The message is displayed on a flight deck display.</p>
<ul>
  <li>Controllers can issue clearances (levels, routes and deviations, speeds), frequency assignments and requests for information.</li>
  <li>Pilots can respond to messages, request and receive clearances and information, and send reports.</li>
  <li>A <strong>free text</strong> capability exchanges information that does not fit the standard formats.</li>
</ul>

<h2>References</h2>
<div class="table-wrap"><table>
<tr><th>Reference</th><th>Content</th></tr>
<tr><td>ICAO Annex 10, Volume III</td><td>Communication systems, including data link</td></tr>
<tr><td>ICAO Doc 4444 (PANS-ATM)</td><td>CPDLC procedures and the CPDLC message set</td></tr>
<tr><td>ICAO Doc 10037 — GOLD (Global Operational Data Link) Manual</td><td>The global operational guidance for flight crews, operators and ATS on data link operations</td></tr>
<tr><td>Commission Implementing Regulation (EU) 2023/1770</td><td>Current EU requirements for aircraft equipment and data link services in Single European Sky airspace. It <strong>repealed</strong> the original Data Link Services Implementing Rule, Regulation (EC) No 29/2009.</td></tr>
<tr><td>Aircraft manuals</td><td>FCOM / AFM limitations and the CMU operating procedures for your type</td></tr>
</table></div>

<h2>A short history in Europe</h2>
<p>The Data Link Services Implementing Rule (Regulation (EC) No 29/2009) mandated CPDLC above FL285 in European airspace. Its implementation was affected by technical problems — random disconnections called <strong>provider aborts</strong>. An EASA investigation found that they came from a combination of factors linked to the radio-frequency environment and the single-frequency data link infrastructure, and recommended a multi-frequency infrastructure. The dates of application were therefore deferred (Regulation (EU) 2015/310 and later amendments). In 2023 the requirements were consolidated in Regulation (EU) 2023/1770.</p>

<h2>Benefits</h2>
<ul>
  <li>Less voice traffic on the frequency and increased sector capacity;</li>
  <li>more pilot requests handled at the same time;</li>
  <li>fewer misunderstandings — for example call sign confusion;</li>
  <li>safer frequency changes and fewer loss-of-communication events.</li>
</ul>
<div class="callout caution"><span class="label">Limitation</span><p>CPDLC latency is much longer than voice — a response can take up to several minutes. Use it only for <strong>non-time-critical</strong> communications. Check your aircraft limitations: on the B737 with protected-mode CPDLC (PM-CPDLC), the installation is intended for use in the <strong>cruise</strong> phase and for non-critical messages only.</p></div>
""",
takeaways=["CPDLC: data link ATC messages for non-urgent, strategic communications.", "References: Annex 10 Vol III, PANS-ATM, ICAO GOLD (Doc 10037), EU Regulation 2023/1770.", "Benefits: less frequency congestion, fewer misunderstandings; limitation: latency — not for time-critical messages."],
check=dict(q="Which regulation now contains the EU data link requirements, replacing Regulation (EC) No 29/2009?", options=["Regulation (EU) 965/2012", "Commission Implementing Regulation (EU) 2023/1770", "Regulation (EU) 2015/340", "ICAO Doc 4444"], answer=1,
           explain="Regulation (EU) 2023/1770 repealed Regulation (EC) No 29/2009."),
),

dict(title="Data Link Services", minutes=6,
objectives=["Describe the data link services available to the flight crew.", "Explain the logon (DLIC) process.", "Identify the services mandated in Europe."],
body="""
<h2>The services</h2>
<div class="table-wrap"><table>
<tr><th>Service</th><th>Purpose</th></tr>
<tr><td><strong>DLIC</strong> — Data Link Initiation Capability</td><td>Provides the information needed to establish data link communications between an ATS unit and the aircraft. It is done <strong>before any other data link service</strong> (the logon).</td></tr>
<tr><td><strong>ACM</strong> — ATC Communications Management</td><td>Automated assistance for the transfer of ATC communications (voice and CPDLC) between sectors and units.</td></tr>
<tr><td><strong>ACL</strong> — ATC Clearances</td><td>Operational exchanges: pilots send requests and reports; controllers issue clearances, instructions and notifications.</td></tr>
<tr><td><strong>AMC</strong> — ATC Microphone Check</td><td>Lets the controller send one instruction to all CPDLC aircraft on a frequency to check that none is blocking the voice channel (stuck microphone).</td></tr>
<tr><td><strong>DCL</strong> — Departure Clearance</td><td>Requesting and delivering departure clearances by data link.</td></tr>
<tr><td><strong>DSC</strong> — Downstream Clearance</td><td>Obtaining a clearance from an ATS unit that is not yet in control of the aircraft, when it cannot be obtained through unit-to-unit coordination.</td></tr>
</table></div>
<p>The European data link rules mandated the first four services: <strong>DLIC, ACM, ACL and AMC</strong>.</p>

<h2>Logon</h2>
<ul>
  <li>The logon uses the <strong>ICAO code of the ATS unit</strong> and must match the flight plan data (aircraft identification and registration). Errors in the flight plan or the FMS cause logon failures.</li>
  <li>Log on in good time before entering the CPDLC airspace, as published in the AIP.</li>
  <li>Only one ATS unit is the <strong>current data authority</strong> at any time — a controlled flight is under the control of only one ATC unit at a time (ICAO Annex 11).</li>
</ul>
""",
takeaways=["DLIC (logon) comes first; then ACM, ACL and AMC — the four mandated services in Europe.", "DCL and DSC add departure and downstream clearances.", "Logon details must match the flight plan; only one current data authority at a time."],
check=dict(q="What does the AMC service do?", options=["Sends weather reports", "Lets the controller check that no aircraft is blocking the voice frequency", "Assigns squawk codes", "Manages the logon"], answer=1,
           explain="The ATC Microphone Check service detects a stuck microphone blocking the frequency."),
),

dict(title="Principles of CPDLC Exchanges and Message Composition", minutes=7,
objectives=["Apply the principles for choosing voice or CPDLC.", "Understand single- and multi-element messages.", "Respond correctly to messages."],
body="""
<h2>Principles</h2>
<ul>
  <li><strong>Voice and data link co-exist.</strong> CPDLC supplements voice; it does not replace it.</li>
  <li>CPDLC is used only for <strong>non-time-critical</strong> communications. Time-criticality depends on the traffic situation, the end-to-end performance (systems and human response times) and the recovery time.</li>
  <li>The choice of voice or CPDLC is at the discretion of the controller and the pilot.</li>
  <li>Usually, a CPDLC message is answered by CPDLC and a voice message by voice.</li>
</ul>
""" + exchange_diagram() + """
<h2>Message composition</h2>
<ul>
  <li>Messages use a <strong>standard format</strong> from the ICAO message set, in plain language or abbreviations — without non-essential words.</li>
  <li>A message can have a <strong>single element</strong> (for example <code>CLIMB TO FL360</code>) or <strong>several elements</strong> (for example <code>CLIMB TO FL360, CLIMB AT 1000 FT PER MINUTE MINIMUM</code>). The maximum number of elements depends on the system and the airspace.</li>
  <li>A single response to a multi-element message applies to <strong>all elements</strong>. If any part cannot be complied with, respond <strong>UNABLE</strong> to the whole message.</li>
  <li>Only one open dialogue of the same type with the same aircraft is allowed at a time: horizontal profile, vertical profile, speed, or SSR code. A speed and a level dialogue can be open together; a heading and a direct-route dialogue cannot.</li>
  <li>Systems must handle unsupported messages correctly, normally with an error message.</li>
</ul>

<h2>Responses</h2>
<div class="table-wrap"><table>
<tr><th>Response</th><th>Meaning</th></tr>
<tr><td>WILCO</td><td>I will comply with the clearance or instruction.</td></tr>
<tr><td>UNABLE</td><td>I cannot comply (with the whole message).</td></tr>
<tr><td>STANDBY</td><td>Wait — the message is being considered; a further response will follow. The dialogue stays open.</td></tr>
<tr><td>AFFIRM / NEGATIVE</td><td>Yes / no to a question.</td></tr>
<tr><td>ROGER</td><td>Message received (for information messages).</td></tr>
</table></div>
""",
takeaways=["Voice and CPDLC co-exist; CPDLC for non-time-critical messages only.", "One response applies to all elements of a multi-element message — UNABLE if any part cannot be done.", "Only one open dialogue of each type at a time."],
check=dict(q="You receive a two-element message and can comply with only one element. What do you respond?", options=["WILCO", "UNABLE for the whole message", "ROGER", "AFFIRM"], answer=1,
           explain="If any element cannot be complied with, respond UNABLE to the whole message."),
),

dict(title="Reverting to Voice, Phraseology and Failures", minutes=6,
objectives=["Recognise when to revert from CPDLC to voice.", "Use CPDLC-related voice phraseology.", "Handle message failures and CPDLC system failures."],
body="""
<h2>When to revert to voice</h2>
<ul>
  <li>To clarify an unexpected, inappropriate or ambiguous CPDLC message.</li>
  <li>To make sure an instruction is executed in time.</li>
  <li>To correct an unintended message that has been sent.</li>
  <li>When a time-out or an error occurs for a CPDLC message.</li>
  <li>Always for urgent or emergency situations.</li>
</ul>

<h2>Phraseology</h2>
<div class="table-wrap"><table>
<tr><th>Situation</th><th>Phraseology</th></tr>
<tr><td>Correcting a CPDLC message by voice</td><td>“(call sign) DISREGARD CPDLC (message content or type) MESSAGE, BREAK, (corrected message)”<br><span class="muted">Example: “DOMESTIC 3012, DISREGARD CPDLC CLIMB MESSAGE, BREAK, CLIMB FLIGHT LEVEL 360.”</span></td></tr>
<tr><td>Failure of a single message</td><td>Confirm by voice the action that will be taken, prefaced with “CPDLC MESSAGE FAILURE” — or resend the message by CPDLC.</td></tr>
<tr><td>CPDLC has failed</td><td>Revert to voice and inform the other party: “CPDLC FAILURE”.</td></tr>
<tr><td>Complete ground system failure</td><td>Controller: “ALL STATIONS CPDLC FAILURE (unit name)”.</td></tr>
<tr><td>Stop sending requests</td><td>“((call sign) or ALL STATIONS) STOP SENDING CPDLC REQUESTS [UNTIL ADVISED] [(reason)]”</td></tr>
<tr><td>Resume normal use</td><td>“((call sign) or ALL STATIONS) RESUME NORMAL CPDLC OPERATIONS”</td></tr>
</table></div>
<div class="callout"><span class="label">Good practice</span><p>Keep listening to the voice frequency at all times while using CPDLC. A clearance received by voice takes precedence over a pending CPDLC message on the same subject — clarify if in doubt.</p></div>
""",
takeaways=["Revert to voice to clarify, to ensure timely execution, to correct, after a time-out or error, and always in an emergency.", "Use “DISREGARD CPDLC … MESSAGE, BREAK …”, “CPDLC MESSAGE FAILURE”, “CPDLC FAILURE”.", "Keep a listening watch on voice."],
check=dict(q="A CPDLC message times out without a response. What should you do?", options=["Send it again repeatedly", "Revert to voice to confirm the clearance", "Ignore it", "Switch off the CMU"], answer=1, explain="After a time-out or error, revert to voice."),
),

dict(title="Using the CMU-900 on the Boeing 737-800", minutes=7,
objectives=["Navigate the main CPDLC pages of the CMU-900 on the CDU.", "Respond to uplinked messages.", "Use the ATC log and the reports and requests pages."],
body="""
<h2>The application</h2>
<p>On our Boeing 737-800, the <strong>CMU-900</strong> CPDLC application allows digital communication between the aircraft and an ATC centre through the Aeronautical Telecommunication Network (ATN), using the CDU.</p>
<ul>
  <li><strong>LOGON/STATUS</strong> page — initiates the logon to a specified ATS facility and displays the data link status.</li>
  <li><strong>REPORTS/REQUESTS</strong> menu — creates downlink requests: altitude, speed or direct (REQ ALT/SPD/DIR), weather deviation (REQ WX DEV) and facility monitoring (MONITORING).</li>
  <li><strong>ATC LOG</strong> — lists all uplinks and downlinks sent and received.</li>
</ul>

<h2>Receiving a message</h2>
<ul>
  <li>When an uplink is received, a <strong>Hi/Lo chime</strong> sounds and <strong>•ATC MSG</strong> appears at LSK 6R on the CDU. The prompt remains while any uplink is pending.</li>
  <li>Open the message, read it <strong>in full</strong>, and cross-check it with the other pilot.</li>
  <li>Respond with the appropriate prompt: <strong>WILCO, STANDBY, AFFIRM, UNABLE, ROGER or NEGATIVE</strong>.</li>
  <li>Selecting <strong>STANDBY</strong> sends a downlink and restarts the alert timer; the message is not closed until another response is sent. Selecting ROGER after STANDBY replaces STANDBY with ACCEPTED, and the message is completed.</li>
</ul>

<h2>ATC log</h2>
<ul>
  <li>Shows, for each message: uplink or downlink, time, source, tracking number, status and the first 22 characters of the text.</li>
  <li>Select the message text to display the complete message with its response.</li>
  <li>Status annunciations show whether a message is open, accepted, rejected, failed or timed out — check them when in doubt.</li>
</ul>

<h2>Dash 8 fleets</h2>
<p>Q400 and Q200 crews: check whether your aircraft is CPDLC equipped. If not, this course gives awareness of CPDLC operations used by other traffic and ATC.</p>
<p class="muted">Button names and page layouts depend on the installed software — always use your FCOM.</p>
""",
takeaways=["CMU-900 pages: LOGON/STATUS, REPORTS/REQUESTS, ATC LOG.", "Uplink: chime + •ATC MSG at LSK 6R; read in full, cross-check, then respond.", "STANDBY keeps the dialogue open; check the status annunciations in the ATC log."],
check=dict(q="On the CMU-900, how is the receipt of an uplink message indicated?", options=["Master caution only", "A Hi/Lo chime and •ATC MSG at LSK 6R on the CDU", "A message on the PFD only", "No indication"], answer=1, explain="A Hi/Lo chime sounds and •ATC MSG is displayed at LSK 6R."),
),

dict(title="Good Practice and Common Errors", minutes=5,
objectives=["Apply crew procedures that prevent CPDLC errors.", "Recognise common CPDLC errors.", "Manage workload when using CPDLC."],
body="""
<h2>Crew procedures</h2>
<ol class="steps">
  <li><strong>Read the whole message</strong> — aloud or silently, as the SOP requires. Conditional clauses (“AT … CLIMB TO …”, “AFTER PASSING …”) are easy to miss.</li>
  <li><strong>Cross-check</strong> it with the other pilot before responding.</li>
  <li><strong>Respond</strong> — then set the clearance in the FCU/MCP or FMS, and cross-check the result.</li>
  <li>If anything is unclear, <strong>revert to voice</strong>.</li>
</ol>

<h2>Common errors</h2>
<ul>
  <li>Executing a message before responding, or responding WILCO without both pilots reading it.</li>
  <li>Missing a condition in a conditional clearance.</li>
  <li>Responding to the wrong message when several are pending.</li>
  <li>Logon failures caused by wrong flight plan or FMS data.</li>
  <li>Heads-down work with CPDLC at a critical moment — only one pilot should be heads-down at any time.</li>
</ul>
<div class="callout"><span class="label">Workload</span><p>CPDLC reduces frequency congestion, but it can increase heads-down time. Plan its use for cruise and for non-urgent exchanges, and keep the pilot flying focused on the flight path.</p></div>
""",
takeaways=["Read in full, cross-check, respond, then act — and verify the result.", "Watch for conditional clauses and multiple pending messages.", "Only one pilot heads-down; revert to voice when in doubt."],
check=dict(q="What is the correct order when handling a CPDLC clearance?", options=["Act, then read, then respond", "Read in full, cross-check, respond, then act and verify", "Respond, then read", "Act without responding"], answer=1, explain="Read, cross-check, respond, then act and verify."),
),
]


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


QUESTIONS = [
Q(1, "CPDLC is intended for:", ["Time-critical communications", "Non-urgent, strategic communications", "Emergency communications only", "Company messages only"], 1, "CPDLC is for non-time-critical communications."),
Q(1, "Which ICAO document is the global operational data link manual?", ["Doc 4444", "Doc 10037 (GOLD)", "Doc 9574", "Doc 8168"], 1, "Doc 10037 is the GOLD manual."),
Q(1, "Where is the CPDLC message set published?", ["ICAO Doc 4444 (PANS-ATM)", "Annex 6", "Doc 9613", "The MEL"], 0, "The message set is in PANS-ATM."),
Q(1, "What were ‘provider aborts’?", ["Pilot rejections of clearances", "Random disconnections of data link communications", "ATC strikes", "Software updates"], 1, "Random disconnections that delayed the European mandate."),
Q(1, "Which regulation repealed Regulation (EC) No 29/2009?", ["(EU) 2015/310", "(EU) 2023/1770", "(EU) 965/2012", "(EU) 1332/2011"], 1, "Regulation (EU) 2023/1770."),
Q(2, "Which service must be completed before any other data link service?", ["ACL", "DLIC (logon)", "AMC", "DSC"], 1, "DLIC is executed before any other data link application."),
Q(2, "Which four services were mandated in Europe?", ["DLIC, ACM, ACL, AMC", "DCL, DSC, ACL, AMC", "DLIC, DCL, DSC, ACM", "ACL only"], 0, "DLIC, ACM, ACL and AMC."),
Q(2, "How many ATS units can be the current data authority at the same time?", ["One", "Two", "Three", "Unlimited"], 0, "A flight is under the control of only one ATC unit at a time."),
Q(3, "A single response to a multi-element message applies to:", ["The first element only", "All elements", "The last element only", "None"], 1, "A response applies to all elements."),
Q(3, "What does STANDBY do?", ["Closes the dialogue", "Indicates the message is being considered; the dialogue stays open", "Rejects the message", "Requests voice contact"], 1, "STANDBY keeps the dialogue open."),
Q(3, "Can a heading dialogue and a direct-route dialogue be open at the same time with one aircraft?", ["Yes", "No — both are horizontal profile", "Only in cruise", "Only with voice backup"], 1, "Only one open dialogue of each type is allowed."),
Q(4, "How do you correct a CPDLC message by voice?", ["“Cancel data”", "“(call sign) DISREGARD CPDLC … MESSAGE, BREAK, (corrected message)”", "“Ignore last”", "“Correction CPDLC”"], 1, "Use the DISREGARD CPDLC phraseology."),
Q(4, "The controller says “ALL STATIONS STOP SENDING CPDLC REQUESTS”. What do you do?", ["Send requests by free text", "Stop sending CPDLC requests until advised; use voice", "Log off", "Switch off the transponder"], 1, "Stop sending requests until advised."),
Q(4, "In an emergency, which means of communication should be used?", ["CPDLC free text", "Voice", "ACARS company channel", "Either, it does not matter"], 1, "Urgent and emergency communications use voice."),
Q(5, "On the B737 CMU-900, where are the logon and data link status found?", ["ATC LOG", "LOGON/STATUS page", "REPORTS/REQUESTS", "PROG page"], 1, "The LOGON/STATUS page."),
Q(5, "What does selecting ROGER after STANDBY do on the CMU-900?", ["Deletes the message", "Replaces STANDBY with ACCEPTED and completes the message", "Sends UNABLE", "Opens a new dialogue"], 1, "ROGER after STANDBY shows ACCEPTED and completes the message."),
Q(5, "How many characters of message text does the ATC LOG list show?", ["The full text", "The first 22 characters", "10 characters", "None"], 1, "The first 22 characters; select it for the full text."),
Q(6, "What is the correct crew sequence with a CPDLC clearance?", ["Act, then respond", "Read in full, cross-check, respond, then act and verify", "Respond immediately", "Ask the cabin"], 1, "Read, cross-check, respond, act, verify."),
Q(6, "Which is a common CPDLC error?", ["Reading the whole message", "Missing a conditional clause", "Cross-checking with the other pilot", "Reverting to voice when unsure"], 1, "Conditional clauses are easy to miss."),
]

COURSE = dict(
    slug="cpdlc",
    title="CPDLC — Controller-Pilot Data Link",
    header_title="CPDLC",
    tagline="Controller-pilot data link communications: references, data link services, message principles, phraseology, failures and the B737 CMU-900.",
    purpose="Give flight crews an operational understanding of CPDLC and its safety issues, in line with ICAO PANS-ATM and GOLD (Doc 10037) and current EU data link rules.",
    audience="All flight crew. CMU-900 operation applies to the Boeing 737-800; Dash 8 crews take it for awareness unless their aircraft is equipped.",
    objectives=["Define CPDLC, its references and its benefits", "Describe the data link services and the logon", "Apply the principles of CPDLC exchanges and responses",
                "Revert to voice and use CPDLC phraseology", "Operate the CMU-900 CPDLC pages on the B737-800", "Avoid common CPDLC errors"],
    icon="people", cert_prefix="CPDLC", quiz_count=10, pass_mark=80,
    group="refresher", season="Additional",
    finale=None,
    modules=[dict(title="CPDLC Principles", summary="Definition, references, services, message principles", icon="people", lessons=range(1, 4)),
             dict(title="Procedures and Practice", summary="Voice reversion, phraseology, failures, CMU-900 and good practice", icon="gear", lessons=range(4, 7))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner cruising with a data link connection to ground", "CPDLC: data link messages between controller and pilot."),
            2: ("gen", "Flight deck at cruise", "Log on before entering CPDLC airspace."),
            3: ("gen", "Airliner in cruise above clouds", "Read the whole message before responding."),
            4: ("gen", "Two pilots communicating on the flight deck", "When in doubt, revert to voice."),
            5: ("gen", "Flight deck with the control display unit", "On the B737-800, CPDLC runs through the CMU-900 on the CDU."),
            6: ("gen", "Airliner in level cruise at sunset", "Only one pilot heads-down at any time.")},
)
