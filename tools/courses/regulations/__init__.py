"""W5 — Operations Manual (MANEX) and Regulations (winter season), all fleets.
Generic content from the ICAO framework (Chicago Convention, Annexes, SARPs) and the EASA Air Operations structure
(Regulation (EU) 965/2012: Part-ORO, Part-CAT, Part-SPA; AMC1 ORO.MLR.100 Operations Manual structure).
Company and national (DACM) specifics are in the Domestic Airlines Operations Manual."""


def Q(lesson, q, options, answer, explain):
    return dict(lesson=lesson, q=q, options=options, answer=answer, explain=explain)


COMPANY = ('<div class="callout caution"><span class="label">Company documents</span><p>This lesson explains the international framework. '
           'The exact company rules are in the <strong>Domestic Airlines Operations Manual</strong> and the national regulations of the <strong>DACM</strong> — '
           'always refer to the current edition.</p></div>')

LESSONS = [
dict(title="The International Framework: ICAO", minutes=6,
objectives=["Describe the role of ICAO and the Chicago Convention.", "Distinguish Standards, Recommended Practices and guidance material.", "Identify the ICAO Annexes most relevant to flight crews."],
body="""
<h2>ICAO and the Chicago Convention</h2>
<p>The <strong>Convention on International Civil Aviation</strong> (Chicago, 1944) created the International Civil Aviation Organization (ICAO). Contracting States agree to apply ICAO <strong>Standards and Recommended Practices (SARPs)</strong>, published in the Annexes, and to notify ICAO of any <strong>differences</strong> (published in the AIP).</p>
<ul>
  <li><strong>Standards</strong> — “shall”: necessary for safety or regularity; States must comply or notify a difference.</li>
  <li><strong>Recommended Practices</strong> — “should”: desirable; States endeavour to comply.</li>
  <li><strong>PANS</strong> (e.g. PANS-OPS Doc 8168, PANS-ATM Doc 4444) — procedures with a wider level of detail.</li>
  <li><strong>Manuals and circulars</strong> — guidance material (e.g. Doc 9613 PBN, Doc 9574 RVSM, Doc 10011 UPRT).</li>
</ul>

<h2>Annexes most relevant to flight crew</h2>
<div class="table-wrap"><table>
<tr><th>Annex</th><th>Subject</th></tr>
<tr><td>1</td><td>Personnel licensing</td></tr>
<tr><td>2</td><td>Rules of the air</td></tr>
<tr><td>3</td><td>Meteorological service</td></tr>
<tr><td>6</td><td>Operation of aircraft (Part I: international commercial air transport — aeroplanes)</td></tr>
<tr><td>8</td><td>Airworthiness</td></tr>
<tr><td>10 / 11</td><td>Aeronautical telecommunications / Air traffic services</td></tr>
<tr><td>12, 13</td><td>Search and rescue, Accident and incident investigation</td></tr>
<tr><td>14</td><td>Aerodromes</td></tr>
<tr><td>15</td><td>Aeronautical information services</td></tr>
<tr><td>17, 18, 19</td><td>Security, Dangerous goods, Safety management</td></tr>
</table></div>
""",
takeaways=["The Chicago Convention created ICAO; States apply SARPs or notify differences.", "Standards (“shall”), Recommended Practices (“should”), PANS and guidance manuals.", "Annex 6 Part I is the core operational Annex for commercial air transport."],
check=dict(q="What must a State do if it cannot comply with an ICAO Standard?", options=["Nothing", "Notify ICAO of the difference (published in the AIP)", "Leave ICAO", "Ask the operator to decide"], answer=1, explain="Differences from Standards must be notified to ICAO."),
),

dict(title="EASA Air Operations Structure", minutes=6,
objectives=["Describe the structure of the EASA Air Operations Regulation.", "Distinguish implementing rules, AMC and GM.", "Explain how national rules relate to EASA and ICAO."],
body="""
<h2>The regulation</h2>
<p>In Europe, the Basic Regulation (EU) 2018/1139 sets the framework, and <strong>Regulation (EU) No 965/2012</strong> (Air Operations) contains the detailed requirements in Annexes:</p>
<div class="table-wrap"><table>
<tr><th>Annex</th><th>Part</th><th>Content</th></tr>
<tr><td>I</td><td>Definitions</td><td>Terms used throughout</td></tr>
<tr><td>II</td><td>Part-ARO</td><td>Requirements for authorities</td></tr>
<tr><td>III</td><td>Part-ORO</td><td>Organisation requirements: management system, manuals (MLR), flight crew (FC), cabin crew (CC), flight time limitations (FTL)</td></tr>
<tr><td>IV</td><td>Part-CAT</td><td>Commercial air transport operations: operating procedures (OP), performance (POL), instruments and equipment (IDE)</td></tr>
<tr><td>V</td><td>Part-SPA</td><td>Specific approvals: PBN (RNP AR), MNPS/HLA, RVSM, LVO, ETOPS, dangerous goods, NVIS…</td></tr>
</table></div>
<ul>
  <li><strong>Implementing rules</strong> are binding.</li>
  <li><strong>AMC</strong> (acceptable means of compliance) — one way to comply; alternatives need approval.</li>
  <li><strong>GM</strong> (guidance material) — explanations.</li>
</ul>

<h2>National regulations</h2>
<p>Domestic Airlines operates under the regulations and oversight of its national authority, the <strong>DACM</strong>, which implement the ICAO SARPs. Many national requirements follow the EASA structure, which is why our Operations Manual uses the same organisation and references. The AOC and its operations specifications define what the company is authorised to do.</p>
""" + COMPANY,
takeaways=["Regulation (EU) 965/2012: Part-ARO, ORO, CAT, SPA (and others).", "Implementing rules are binding; AMC is one accepted way to comply; GM explains.", "Domestic Airlines operates under DACM regulations and its AOC / operations specifications."],
check=dict(q="In Regulation (EU) 965/2012, which Part covers commercial air transport operating procedures and performance?", options=["Part-ARO", "Part-CAT", "Part-FCL", "Part-145"], answer=1, explain="Part-CAT covers CAT operations, performance and equipment."),
),

dict(title="The Operations Manual", minutes=6,
objectives=["Describe the structure of the Operations Manual.", "Find information quickly in each part.", "Apply the rules on amendments and availability."],
body="""
<h2>Structure (AMC1 ORO.MLR.100)</h2>
<div class="table-wrap"><table>
<tr><th>Part</th><th>Content</th></tr>
<tr><td><strong>OM A — General / Basic</strong></td><td>All non-type-related policies and procedures: organisation, responsibilities, crew composition, flight time limitations, operating procedures, dangerous goods, security, accident and incident handling, rules of the air.</td></tr>
<tr><td><strong>OM B — Aircraft operating matters</strong></td><td>Type-related: limitations, normal, abnormal and emergency procedures, performance, flight planning, mass and balance, loading, MEL, systems.</td></tr>
<tr><td><strong>OM C — Route and aerodrome</strong></td><td>Route and aerodrome instructions and information: minimum altitudes, aerodrome operating minima, communications, navigation facilities, special procedures, aerodrome categories.</td></tr>
<tr><td><strong>OM D — Training</strong></td><td>Training programmes and checking for all operations personnel.</td></tr>
</table></div>

<h2>Using the manual</h2>
<ul>
  <li>The Operations Manual must be <strong>kept up to date</strong>; the crew is responsible for using the current revision.</li>
  <li>Relevant parts must be <strong>available on board</strong> (paper or approved electronic format).</li>
  <li>Read and acknowledge every <strong>amendment, temporary revision and operations notice</strong> as the company requires.</li>
  <li>If the Operations Manual and the manufacturer's documents differ, follow the company's rule on precedence, normally stated in OM A.</li>
</ul>
""" + COMPANY,
takeaways=["OM A general, OM B aircraft, OM C route and aerodrome, OM D training.", "Use the current revision; acknowledge amendments and notices.", "Know where to find information under time pressure."],
check=dict(q="Where would you normally find the aerodrome operating minima and route information?", options=["OM A", "OM B", "OM C", "OM D"], answer=2, explain="OM C contains route and aerodrome information, including minima."),
),

dict(title="Commander's Authority, Duties and Key Rules", minutes=7,
objectives=["State the authority and responsibilities of the commander.", "Review key operational rules found in OM A.", "Recognise the documents to be carried on board."],
body="""
<h2>The commander</h2>
<ul>
  <li>Responsible for the safety of the aircraft, persons and cargo on board, and for the conduct of the flight (ICAO Annex 6; EASA CAT.GEN.MPA.105).</li>
  <li>Has the authority to give all commands necessary for safety, to disembark persons or cargo that may be a hazard, and to refuse to carry inadmissible passengers or unsafe cargo.</li>
  <li>May deviate from rules, procedures and methods in an emergency requiring immediate decision and action, in the interest of safety — and must report it.</li>
  <li>Must not start the flight unless satisfied that all operational requirements are met: aircraft airworthiness, documents, crew fitness, weather and NOTAMs, fuel, mass and balance, MEL.</li>
</ul>

<h2>Key OM A subjects to review each year</h2>
<ul>
  <li>Crew composition and designation of the commander; in-flight relief;</li>
  <li>flight and duty time limitations and rest (ORO.FTL), fatigue reporting;</li>
  <li>fuel policy and in-flight fuel management;</li>
  <li>aerodrome selection, operating minima and the inoperative ground equipment table;</li>
  <li>stabilised approach and go-around policy; sterile flight deck;</li>
  <li>dangerous goods, security and the handling of accidents and occurrences (reporting).</li>
</ul>

<h2>Documents on board</h2>
<p>Typical documents include: certificate of registration and certificate of airworthiness (with ARC), noise certificate, AOC copy and operations specifications, radio licence, insurance, journey log / technical log, crew licences and medical certificates, relevant parts of the Operations Manual, the AFM, the MEL, charts, the operational flight plan, mass and balance documentation, NOTAMs and weather, and the NOTOC when dangerous goods are carried. The exact list is in OM A.</p>
""" + COMPANY,
takeaways=["The commander is responsible for safety and has the authority to act for it.", "Emergency deviation from procedures is allowed in the interest of safety — and must be reported.", "Review OM A each year: FTL, fuel policy, minima, stabilised approach, DG, security, reporting."],
check=dict(q="In an emergency requiring immediate action, may the commander deviate from the Operations Manual?", options=["Never", "Yes, in the interest of safety, and must report it", "Only with ATC permission", "Only on the ground"], answer=1, explain="Deviation is permitted in the interest of safety, followed by a report."),
),
]

QUESTIONS = [
Q(1, "Which treaty created ICAO?", ["The Warsaw Convention", "The Chicago Convention (1944)", "The Montreal Protocol", "The Tokyo Convention"], 1, "The Chicago Convention of 1944."),
Q(1, "An ICAO Recommended Practice is expressed with:", ["“shall”", "“should”", "“must”", "“may never”"], 1, "Recommended Practices use “should”."),
Q(1, "Which Annex covers the operation of aircraft?", ["Annex 2", "Annex 6", "Annex 14", "Annex 18"], 1, "Annex 6."),
Q(1, "Which Annex covers safety management?", ["Annex 13", "Annex 17", "Annex 19", "Annex 1"], 2, "Annex 19."),
Q(2, "Which EASA Part contains the requirements for the operator's organisation, including the manuals and FTL?", ["Part-CAT", "Part-ORO", "Part-SPA", "Part-ARO"], 1, "Part-ORO."),
Q(2, "What is AMC?", ["A binding rule", "Acceptable means of compliance — one accepted way to comply", "A type of aircraft", "An ATC procedure"], 1, "AMC are acceptable means of compliance."),
Q(2, "Which Part covers specific approvals such as RVSM and LVO?", ["Part-SPA", "Part-CAT", "Part-ORO", "Part-21"], 0, "Part-SPA."),
Q(3, "Which part of the Operations Manual is type-related?", ["OM A", "OM B", "OM C", "OM D"], 1, "OM B — aircraft operating matters."),
Q(3, "Where are the training programmes described?", ["OM A", "OM B", "OM C", "OM D"], 3, "OM D."),
Q(3, "Who is responsible for using the current revision of the manual?", ["The authority", "The crew", "The manufacturer", "The handling agent"], 1, "Crew members must use the current revision."),
Q(4, "Who is responsible for the safety of the aircraft and persons on board?", ["The dispatcher", "The commander", "ATC", "The cabin manager"], 1, "The commander."),
Q(4, "Which document must be carried when dangerous goods are on board?", ["NOTOC", "Noise certificate only", "Passenger list only", "Catering list"], 0, "The NOTOC (notification to captain)."),
Q(4, "Before starting a flight, the commander must be satisfied about:", ["Only the weather", "Airworthiness, documents, crew, weather, NOTAMs, fuel, mass and balance and MEL", "Only the fuel", "Only the passengers"], 1, "All operational requirements must be met."),
]

COURSE = dict(
    slug="regulations-om", title="Operations Manual and Regulations", header_title="Operations Manual and Regulations",
    tagline="ICAO and EASA regulatory framework, the Operations Manual structure (OM A–D), the commander's authority and the key rules reviewed each year.",
    purpose="Refresh all flight crews' knowledge of the regulatory framework and the structure and use of the Operations Manual (MANEX).",
    audience="All flight crew: Boeing 737-800, Dash 8-Q400 and Dash 8-Q200.",
    objectives=["Describe the ICAO framework and SARPs", "Describe the EASA Air Operations structure and national oversight", "Use the Operations Manual parts A to D", "Apply the commander's authority and the key OM A rules"],
    icon="search", cert_prefix="REG", quiz_count=10, pass_mark=80, group="refresher", season="Winter", finale=None,
    modules=[dict(title="Regulations", summary="ICAO and EASA framework", icon="search", lessons=range(1, 3)),
             dict(title="The Operations Manual", summary="OM structure, commander's authority and key rules", icon="people", lessons=range(3, 5))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("gen", "Airliner in flight above clouds", "ICAO SARPs are the foundation of every national rule."),
            2: ("gen", "Airliner at cruise", "Implementing rules, AMC and GM — and national oversight."),
            3: ("gen", "Two pilots on the flight deck", "Know where to find it: OM A, B, C and D."),
            4: ("gen", "Flight deck at dusk before departure", "The commander's authority — and responsibility.")},
)
