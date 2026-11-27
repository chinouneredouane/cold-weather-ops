"""Global Reporting Format (GRF) — runway surface condition assessment and reporting.

Follows the company GRF course syllabus (4 h 15): Module 1 The GRF (1 h 50) · Module 2 The RCAM (60 min) ·
Module 3 The RCR (60 min) · Module 4 Transmission of the information (25 min) · Evaluation (30–45 min),
completed with a lesson for flight crews on aircraft performance (Airbus, EASA GRF webinar).

Sources: company GRF course (photos, tables and diagrams), RCAM (French version), RCR form and RCR drafting aid, GRF
summary flowchart, Airbus "GRF — Reporting of runway conditions relevant to aeroplane performance" (EASA webinar 2021);
ICAO Annex 14, PANS-Aerodromes (Doc 9981), Circular 355; EU 139/2014 ADR.OPS.A.057/A.060/A.065, ADR.OPS.B.037; EU 2020/469.
Definitions are presented as interactive flip cards. Only pictures from the course material are used."""
from courses.perf_common import Q

_C = "Domestic Airlines GRF course"
_AB = "Airbus, EASA GRF webinar (2021)"


def fig(img, caption, src=_C):
    return (f'<figure class="lesson-figure"><img src="../media/images/{img}.jpg" alt="{caption}" loading="lazy">'
            f'<figcaption>{caption} <span class="muted">Source: {src}.</span></figcaption></figure>')


def cards(items, hint="Tap a card to turn it over.", quiz=None):
    """Flip cards: (front, small text under the front or '', back)."""
    out = []
    for front, sub, back in items:
        s = f"<small>{sub}</small>" if sub else ""
        out.append(f'<button type="button" class="flipcard" aria-pressed="false"><span class="fc-inner">'
                   f'<span class="fc-face fc-front">{front}{s}</span><span class="fc-face fc-back">{back}</span></span></button>')
    quiz = ("tap" in hint.lower() and hint != "Tap a card to turn it over.") if quiz is None else quiz
    return f'<p class="flip-hint">{hint}</p><div class="flipcards{" quiz" if quiz else ""}">{"".join(out)}</div>'


LESSONS = [
# 1 ------------------------------------------------------------------ MODULE 1
dict(title="Why the GRF? Runway Excursions and ICAO Objectives", minutes=12,
objectives=["Explain why runway excursions drive the GRF.", "Describe the limits of the former reporting system based on friction measurements.",
            "State the objectives pursued by ICAO."],
body="""
<h2>Course overview</h2>
<p>This course follows the company GRF syllabus — about 4 h 15 in the classroom:</p>
<table><thead><tr><th>Module</th><th>Subject</th><th>Time</th></tr></thead><tbody>
<tr><td>1</td><td>The Global Reporting Format (GRF)</td><td>1 h 50</td></tr>
<tr><td>2</td><td>The Runway Condition Assessment Matrix (RCAM)</td><td>60 min</td></tr>
<tr><td>3</td><td>The Runway Condition Report (RCR)</td><td>60 min</td></tr>
<tr><td>4</td><td>Transmission of the information (SNOWTAM, ATS, ATIS) and aircraft performance</td><td>25 min +</td></tr>
<tr><td>—</td><td>Evaluation</td><td>30–45 min</td></tr>
</tbody></table>
<p>Five questions guide the course: <strong>Why the GRF? What are the impacts? How is the RCAM used? How is an RCR written? Which information goes to whom?</strong></p>
<h2>Runway excursions</h2>
<p>Runway and taxiway excursions represent about <strong>22 % of all accidents</strong> and are the third accident category by number of victims (IATA runway safety analysis 2010–2014, 415 accidents over five years). An excursion can be <strong>lateral</strong> (veer-off) or <strong>longitudinal</strong> (overrun), at take-off or at landing — about 90 % of them at landing.</p>
""" + fig("photo-tyres", "Braking: the tyre-to-runway interface is where the runway condition becomes aircraft performance.") + """
<h2>Limits of the former system</h2>
<ul>
  <li>Runway friction was estimated with a <strong>friction measuring device</strong> (μ) and reported as good, medium-good… (Annex 14, Attachment A).</li>
  <li>Several devices existed; at least three measurements were needed and an average μ was transmitted.</li>
  <li>The readings were <strong>not reliable and not correlated</strong> with aircraft braking performance, and there was no consensus on their use.</li>
</ul>
<p>Aircraft braking performance depends on the <strong>runway surface condition</strong> and on the <strong>environmental conditions</strong>: the quality of the contamination information is essential. The European Action Plan for the Prevention of Runway Excursions (EAPPRE) asked aerodromes for contaminant removal programmes, assessment whenever contamination appears or changes, and robust communication.</p>
<h2>What ICAO wants</h2>
<ul>
  <li><strong>Improve safety</strong> for aircraft operating on runways, in particular contaminated runways.</li>
  <li>Provide a <strong>harmonised method</strong> to assess and report the runway surface condition, worldwide, linked directly to aircraft performance data.</li>
  <li>Make the report <strong>interpretable by pilots</strong> and reliable thanks to <strong>pilot feedback</strong>.</li>
</ul>
<p>The regulatory chain: ICAO Annex 14 and Annex 15, PANS-Aerodromes and Circular 355 for aerodromes; Annexes 6, 8 and 15 for the other actors; in Europe, regulations (EU) 2018/1139 and 139/2014. More information: icao.int/safety/Pages/GRF.aspx.</p>
""" + fig("photo-snow-clearing", "Implementing the GRF concerns aerodrome operators, air traffic services, aeronautical information services, aircraft manufacturers and operators.") + """
<div class="callout info"><span class="label">Applicability</span><p>The GRF was planned for 5 November 2020 and became applicable worldwide on <strong>4 November 2021</strong> (EASA rules from 12 August 2021).</p></div>
""",
takeaways=["Runway excursions ≈ 22 % of accidents, mostly at landing.", "Friction measurements were unreliable and not correlated with aircraft braking.",
           "GRF: one harmonised, performance-related method to assess and report the runway condition, reinforced by pilot reports."],
check=dict(q="What does ICAO pursue with the GRF? (choose the best answer)", options=["Each State develops its own criteria", "A harmonised method linked to aircraft performance, improving safety on contaminated runways", "Removing all risks of runway contamination", "More friction measurements"], answer=1,
           explain="Harmonised assessment and reporting, directly usable for aircraft performance — to improve safety."),
),
# 2
dict(title="The New System: Actors and Key Changes", minutes=12,
objectives=["Describe the role of each actor in the GRF.", "List the main changes: definitions, RCAM, RWYCC, RCR, SNOWTAM.",
            "Describe the general process from inspection to publication."],
body="""
<h2>Who does what</h2>
<table><thead><tr><th>Actor</th><th>Role</th></tr></thead><tbody>
<tr><td>Aerodrome operator</td><td>Inspects the movement area, assesses the surface, assigns the RWYCC with the RCAM, writes the RCR, requests the SNOWTAM, collects pilot reports</td></tr>
<tr><td>Air traffic services (ATS)</td><td>Pass the RCR to pilots by radio and ATIS; pass AIREPs to the aerodrome operator</td></tr>
<tr><td>Aeronautical information service (AIS)</td><td>Publishes the SNOWTAM (new format)</td></tr>
<tr><td>Pilots</td><td>Use the information; report the braking action (AIREP) to ATS</td></tr>
<tr><td>Aircraft manufacturer</td><td>Provides performance data linked to the RWYCC (Annex 8)</td></tr>
<tr><td>Airline</td><td>Assesses aircraft braking performance; updates its procedures (Annex 6)</td></tr>
</tbody></table>
""" + fig("photo-cockpit-2", "Pilots use the RCR for the landing performance assessment and send AIREPs on braking action.") + """
<h2>Key definitions</h2>
""" + cards([
    ("RWYCC", "Runway condition code", "A number from <b>6</b> (dry) to <b>0</b> (less than poor) for <b>each third</b> of the runway, assigned with the RCAM."),
    ("RCAM", "Runway Condition Assessment Matrix", "The matrix that links the observed contaminant, depth and temperature to a RWYCC, and pilot braking reports to a downgrade."),
    ("RCR", "Runway Condition Report", "The standardised report of the runway surface condition: a performance section (per third) and a situational awareness section."),
    ("SNOWTAM", "Special series NOTAM", "The NOTAM that publishes the RCR. New format since the GRF; valid 8 hours at most."),
    ("AIREP", "Special air-report of braking action", "Pilot report of braking action — GOOD, GOOD TO MEDIUM, MEDIUM, MEDIUM TO POOR, POOR, LESS THAN POOR."),
    ("Runway third", "Tiers de piste", "The runway (TORA) divided in three equal parts; the first third starts at the lower runway designator."),
]) + """
<h2>The main changes</h2>
<ul>
  <li><strong>New definitions</strong>: four runway surface states (dry, wet, slippery wet, contaminated) and standard contaminant descriptors.</li>
  <li><strong>RCAM</strong> to assign a <strong>RWYCC</strong> per third, and compare the aerodrome's observations with pilot reports.</li>
  <li><strong>RCR</strong>, evolving with the situation and used by pilots, published all year — not only in winter.</li>
  <li><strong>New SNOWTAM format</strong>, new information content and new update criteria.</li>
  <li><strong>Friction measurements</strong> are no longer reported.</li>
</ul>
<h2>The general process</h2>
<ol>
  <li>Runway inspection and analysis of the observations (coverage criteria).</li>
  <li>Characterisation of the situation with the RCAM: initial RWYCC (Module 2).</li>
  <li>Collection of data (AIREPs…) and adjustment of the RWYCC (Module 2).</li>
  <li>Writing the RCR (Module 3).</li>
  <li>Transmission of the information (SNOWTAM, ATS, ATIS) and follow-up of its accuracy (Module 4).</li>
</ol>
""" + fig("grf-flowchart", "GRF summary flowchart: from the inspection to the RWYCC, the RCR and its transmission.", "Company GRF documentation — summary flowchart"),
takeaways=["Aerodrome assesses and reports; ATS and AIS transmit; pilots use and report.", "New: RCAM, RWYCC per third, RCR all year, new SNOWTAM, no friction values.",
           "Process: inspect → RCAM → adjust with AIREPs → RCR → SNOWTAM/ATS → follow-up."],
check=dict(q="May runway inspectors use their own definitions of the surface condition in a GRF RCR?", options=["Yes", "No — standard descriptors are mandatory", "Only in summer", "Only for the situational awareness section"], answer=1,
           explain="The GRF uses standardised terms and codes only."),
),
# 3
dict(title="Runway Surface States and Contaminant Identification", minutes=15,
objectives=["Define the four runway surface states.", "Identify the eight contaminant descriptors from observations and photos.",
            "Explain the impact of the GRF on runway inspection work."],
body="""
<h2>Four runway surface states</h2>
""" + cards([
    ("DRY", "Sèche", "A runway clear of contaminants and visible moisture within the required length and width."),
    ("WET", "Mouillée", "Surface covered by any visible dampness or water up to and including <b>3 mm</b>. A damp runway is reported WET."),
    ("SLIPPERY WET", "Mouillée glissante", "A wet runway whose surface friction is degraded — rubber deposits in the touchdown zone, poor texture, poor drainage. Identified by measurements, prior methods or AIREPs."),
    ("CONTAMINATED", "Contaminée", "A significant part of the surface (more than 25 % of a third in use) covered by one or more contaminant descriptors."),
]) + """
<h2>Fluid and hard contaminants</h2>
<p>Eight descriptors exist (Annex 1 of EU 139/2014). They can be <strong>combined</strong> to describe the surface — for example dry snow on top of ice.</p>
""" + cards([
    ("STANDING WATER", "Eau stagnante — fluid", "Water deeper than <b>3 mm</b>. Often only in puddles: check the coverage."),
    ("SLUSH", "Neige fondante — fluid", "Water-saturated snow: water runs when you squeeze it and splashes when you step on it. Typically 0 to +5 °C."),
    ("WET SNOW", "Neige mouillée — fluid", "Snow with liquid water: it forms a compact ball, but no water runs out. Not to be confused with slush."),
    ("DRY SNOW", "Neige sèche — fluid", "Falls in cold weather (around −5 °C or below). Light flakes that do not stick: it will not form a ball."),
    ("COMPACTED SNOW", "Neige compactée — hard", "Snow compressed into a solid mass: a vehicle does not sink in; it breaks into lumps when picked up."),
    ("FROST", "Gelée / givre — hard", "Ice crystals formed from airborne moisture on a surface below 0 °C: granular texture, often after calm, clear nights."),
    ("ICE", "Glace — hard", "Frozen water: thicker than frost, very slippery, not shiny; removal is difficult."),
    ("WET ICE", "Glace mouillée — hard", "Ice with water on top, or melting ice — often after freezing rain when the temperature rises above 0 °C. Shiny and wet."),
]) + """
<h2>Contaminants in pictures (1)</h2>
""" + fig("photo-dry-snow", "Dry snow on an apron: light and loose, it falls apart when you blow on it.") + fig("photo-wet-snow", "Wet snow: ice crystals with liquid water — compact, but no water runs out.") + fig("photo-compacted-snow", "Compacted snow on a runway after a snowfall without decontamination: the vehicle does not sink in.") + """
<h2>Contaminants in pictures (2)</h2>
""" + fig("photo-slush", "Slush: water runs out when it is squeezed and splashes under the foot.") + fig("photo-ice", "Ice: very slippery, not shiny, after hours well below 0 °C.") + fig("photo-wet-ice", "Wet ice: shiny and wet, after freezing rain when the temperature has just become positive.") + """
<h2>Contaminants in pictures (3)</h2>
""" + fig("photo-frost", "Frost: granular texture, more deposit on metal parts; calm wind, ground well below 0 °C.") + fig("photo-standing-water", "Standing water: only in puddles, deeper than 3 mm, positive temperature.") + """
<h2>Exercise: identify the contaminant</h2>
""" + cards([
    ("Clue 1", "After snowfall · a vehicle does not sink in · it breaks in lumps · OAT &lt; 0 °C", "<b>COMPACTED SNOW</b>"),
    ("Clue 2", "Very slippery but not shiny · OAT well below 0 °C for hours", "<b>ICE</b>"),
    ("Clue 3", "After snowfall · forms a compact ball, no water runs out · OAT near 0 °C", "<b>WET SNOW</b>"),
    ("Clue 4", "After snowfall · water runs when squeezed, splashes under the foot · OAT about +5 °C", "<b>SLUSH</b>"),
    ("Clue 5", "After freezing rain · shiny and wet · negative for hours, just became positive", "<b>WET ICE</b>"),
    ("Clue 6", "Cold, dry weather · will not form a ball · falls apart when blown", "<b>DRY SNOW</b>"),
    ("Clue 7", "No wind · granular texture · more on metal signs · ground well below 0 °C", "<b>FROST</b>"),
    ("Clue 8", "After rain · only in puddles · more than 3 mm · positive temperature", "<b>STANDING WATER</b>"),
], hint="Read the clues, decide, then tap to check.") + """
<h2>Impact on the aerodrome operator</h2>
<ul>
  <li><strong>Before</strong>: in case of doubt a friction measurement or decelerometer was used. <strong>Now</strong>: the surface is described precisely with predefined codes and terms; friction values are not reported.</li>
  <li>The operator issues the NOTAM / SNOWTAM, monitors the runway and performs as many inspections as necessary (ADR.OPS.B.037).</li>
  <li>Contamination is no longer only a winter problem: an RWYCC and an RCR are published <strong>all year</strong>.</li>
  <li>New procedures, new training, consistency between reality and what is published, consistency between actors, reliable exchanges with ATS (AIREP, RCR) and AIS (NOTAM, SNOWTAM).</li>
</ul>
<div class="callout warn"><span class="label">Decision aids</span><p>Use the meteorological data and the reports of previous inspections to identify the contaminant. Pilots should know these descriptors: they are the words of the RCR.</p></div>
""",
takeaways=["Four states: DRY, WET (≤ 3 mm), SLIPPERY WET, CONTAMINATED.", "Eight descriptors: standing water, slush, wet snow, dry snow, compacted snow, frost, ice, wet ice — can be combined.",
           "Identification uses observation, temperature and the history of the day."],
check=dict(q="After freezing rain, the surface is shiny and wet; the temperature has just become positive. The contaminant is:", options=["Frost", "Wet ice", "Slush", "Standing water"], answer=1,
           explain="Freezing rain followed by a rise above 0 °C gives wet ice."),
),
# 4 ------------------------------------------------------------------ MODULE 2
dict(title="The RCAM — Key Elements", minutes=12,
objectives=["Describe the structure of the RCAM.", "Read the matrix to assign a RWYCC.", "Recognise the different RCAM versions."],
body="""
<h2>What the regulation requires</h2>
<p>When contaminants are present, the aerodrome operator (ADR.OPS.B.037) inspects the runway, assigns a <strong>RWYCC</strong> per third with the <strong>RCAM</strong>, and uses <strong>AIREPs</strong> to trigger a reassessment. The number of inspections is not fixed: as many as necessary.</p>
<h2>Structure of the matrix</h2>
<ul>
  <li><strong>Assessment criteria</strong> (at the inspection): runway surface description — contaminant type, depth, outside air temperature → <strong>RWYCC 6 to 0</strong>.</li>
  <li><strong>Downgrade assessment criteria</strong>: aeroplane deceleration or directional control observation, and the pilot report of braking action (AIREP).</li>
</ul>
""" + fig("rcam-fr", "Runway Condition Assessment Matrix — French version used in the course.", "RCAM (company GRF documentation)") + """
<h2>The codes</h2>
<table><thead><tr><th>RWYCC</th><th>Runway surface description</th><th>AIREP</th></tr></thead><tbody>
<tr><td>6</td><td>DRY</td><td>—</td></tr>
<tr><td>5</td><td>FROST · WET (≤ 3 mm) · up to 3 mm: SLUSH, DRY SNOW, WET SNOW</td><td>GOOD</td></tr>
<tr><td>4</td><td>COMPACTED SNOW at −15 °C OAT or colder (also specially prepared winter runway)</td><td>GOOD TO MEDIUM</td></tr>
<tr><td>3</td><td>SLIPPERY WET · DRY or WET SNOW on top of COMPACTED SNOW · more than 3 mm: DRY SNOW, WET SNOW · COMPACTED SNOW above −15 °C</td><td>MEDIUM</td></tr>
<tr><td>2</td><td>More than 3 mm of STANDING WATER or SLUSH</td><td>MEDIUM TO POOR</td></tr>
<tr><td>1</td><td>ICE</td><td>POOR</td></tr>
<tr><td>0</td><td>WET ICE · WATER on top of COMPACTED SNOW · DRY or WET SNOW on top of ICE</td><td>LESS THAN POOR</td></tr>
</tbody></table>
<h2>Reading examples</h2>
""" + cards([
    ("Wet runway, water ≤ 3 mm", "RWYCC?", "<b>RWYCC 5</b>"),
    ("Compacted snow, OAT −10 °C", "RWYCC?", "<b>RWYCC 3</b> — compacted snow above −15 °C."),
    ("Standing water 6 mm", "RWYCC?", "<b>RWYCC 2</b>"),
    ("Compacted snow, OAT −20 °C", "RWYCC?", "<b>RWYCC 4</b>"),
    ("Dry snow on top of ice", "RWYCC?", "<b>RWYCC 0</b> — less than poor."),
    ("Frost", "RWYCC?", "<b>RWYCC 5</b>"),
], hint="Find the code in the matrix, then tap to check.") + """
<h2>RCAM versions</h2>
<ul>
  <li>Vertical or horizontal presentation, with or without snow and ice conditions. A <strong>simplified matrix</strong> exists for aerodromes never exposed to snow or ice.</li>
  <li>The matrix chosen must be <strong>integrated into the local procedures</strong> of the aerodrome operator.</li>
  <li>No RCAM refers to <strong>friction coefficient measurements</strong>; non-meteorological contaminants (sand, oil, rubber…) are not in the matrix.</li>
</ul>
""" + fig("rcam-easa-horizontal", "Horizontal presentation of the RCAM (EASA).", "EASA AMC1 ADR.OPS.B.037, from the company GRF course") + fig("rcam-fr-simplified", "Simplified RCAM for aerodromes never exposed to snow or ice.", "RCAM (company GRF documentation)"),
takeaways=["RCAM: contaminant + depth + OAT → RWYCC; AIREP and observations → downgrade.", "6 dry · 5 wet/frost/thin snow · 4 compacted ≤ −15 °C · 3 slippery wet/deep snow · 2 > 3 mm water or slush · 1 ice · 0 wet ice.",
           "Different presentations give the same codes; no friction values in the RCAM."],
check=dict(q="Which RWYCC corresponds to more than 3 mm of standing water?", options=["5", "3", "2", "1"], answer=2, explain="Standing water or slush deeper than 3 mm → RWYCC 2 (MEDIUM TO POOR)."),
),
# 5
dict(title="Applying the RCAM — Thirds, Coverage, Depth and Temperature", minutes=12,
objectives=["Define the runway thirds, including displaced thresholds and reduced length or width.", "Apply the 10 % and 25 % coverage criteria and the reported coverage values.",
            "Apply the 3 mm depth threshold and the −15 °C criterion."],
body="""
<h2>Why runway thirds?</h2>
<p>Information is collected per third to decide whether the matrix applies and to let pilots prepare for braking and directional control in each part of the runway.</p>
<ul>
  <li>The thirds are based on the runway length available for the take-off run (<strong>TORA</strong>); stopways, clearways and displaced thresholds are not considered.</li>
  <li>The <strong>first third</strong> starts at the end with the <strong>lower runway designator</strong> (for runway 08/26, at the beginning of 08, even if 26 is in use).</li>
  <li>If part of the length or width is declared unusable, the thirds and the coverage are assessed on the <strong>usable</strong> part only.</li>
</ul>
""" + fig("diagram-reduced-lda", "Runway with reduced length: the thirds are defined on the remaining length (here 1,800 m).") + """
<h2>Is the runway contaminated?</h2>
""" + cards([
    ("Coverage below 10 %", "of a third", "RWYCC <b>6</b> for that third. Contaminant: NR. Coverage: NR."),
    ("Coverage 10 % to 25 %", "of a third", "RWYCC <b>6</b> for that third. Contaminant reported. Coverage reported: <b>25</b>."),
    ("Coverage more than 25 %", "of a third", "Use the <b>RCAM</b>: report the contaminant, the coverage (50, 75 or 100) and the RWYCC."),
    ("Why 25 %?", "", "If the aircraft is in a contaminated patch for a short time (250 m at 220 km/h ≈ 4 s), the dry performance margins cover it."),
]) + """
<h2>Reported coverage</h2>
""" + fig("table-coverage-reported", "Estimated coverage → reported coverage: 0–9 % NR · 10–25 % 25 · 26–50 % 50 · 51–75 % 75 · 76–100 % 100.") + """
<h2>Depth</h2>
<p>The depth is measured precisely enough to know whether the <strong>3 mm threshold</strong> is crossed — not to the millimetre. Below 3 mm a fluid contaminant drains from the tyre footprint (no dynamic aquaplaning); above 3 mm the runway is contaminated and aquaplaning becomes possible. Dry and wet snow use the same 3 mm threshold.</p>
""" + fig("table-depth-reported", "Measured depth → reported depth: wet runway 1–3 mm NR; standing water ≥ 4 mm measured value; slush, wet snow, dry snow 1–3 mm 03, ≥ 4 mm measured value.") + """
<h2>Temperature</h2>
<p>Compacted snow is RWYCC 4 at −15 °C or colder, RWYCC 3 above. The −15 °C value comes from historical industry testing and is probably conservative; braking action correlates better with the <strong>surface</strong> temperature than with the OAT.</p>
""" + fig("airbus-12", "Temperature: compacted snow gives better braking below −15 °C.", _AB) + """
<div class="callout caution"><span class="label">Several contaminants</span><p>When several contaminants are found, all of them are recorded in the inspection report; the RCR reports the descriptor(s) for each third.</p></div>
""",
takeaways=["Thirds on the TORA, starting from the lower runway designator; usable part only.", "< 10 % → NR, RWYCC 6; 10–25 % → coverage 25, RWYCC 6; > 25 % → RCAM.",
           "3 mm threshold for depth; compacted snow −15 °C."],
check=dict(q="Runway 04/22 with TORA 3,000 m (RWY 04 ASDA 3,100 m). Which length defines the thirds?", options=["3,100 m", "3,000 m (TORA)", "3,100 m for 04 and 3,000 m for 22", "LDA only"], answer=1,
           explain="The thirds are defined on the TORA; stopways and clearways are not used."),
),
# 6
dict(title="Pilot Reports (AIREP) and Adjusting the RWYCC", minutes=12,
objectives=["Describe the AIREP and its role in the GRF.", "Apply the reassessment triggers.",
            "Apply the upgrade and downgrade rules for the RWYCC."],
body="""
<h2>Special air-reports of braking action</h2>
<p>Pilots report braking action on the frequency to the controller, using the standard RCAM terms. An AIREP depends on the aircraft's braking and control during the landing, applies to part of the runway, and may differ from one aircraft to another (for example a Q400 followed by a B777). There is no AIREP for RWYCC 6.</p>
""" + cards([
    ("GOOD", "", "Braking deceleration normal; directional control normal — corresponds to <b>RWYCC 5</b>."),
    ("GOOD TO MEDIUM", "", "Between good and medium — <b>RWYCC 4</b>."),
    ("MEDIUM", "", "Braking deceleration or directional control noticeably reduced — <b>RWYCC 3</b>."),
    ("MEDIUM TO POOR", "", "Between medium and poor — <b>RWYCC 2</b>."),
    ("POOR", "", "Braking deceleration or directional control significantly reduced — <b>RWYCC 1</b>."),
    ("LESS THAN POOR", "", "Braking deceleration minimal to non-existent, or directional control uncertain — <b>RWYCC 0</b>."),
]) + """
<h2>Three situations</h2>
<ol>
  <li><strong>First inspection of the day</strong>, no pilot report yet: inspect, apply the matrix, adjust with AIREPs when they arrive, publish.</li>
  <li><strong>A RWYCC is already published</strong> and the situation evolves (AIREP different from the published code…): inspect, apply the matrix, adjust, publish.</li>
  <li><strong>After a decontamination action</strong> (chemical treatment, snow clearing): inspect, apply the matrix, adjust with new AIREPs, publish.</li>
</ol>
""" + fig("photo-snowplough", "After snow clearing or chemical treatment, the runway is inspected again and the RWYCC reassessed.") + """
<h2>When must the runway be reassessed?</h2>
<p>A new assessment of the surface (new inspection) is required after <strong>two consecutive POOR</strong> AIREPs, or <strong>one LESS THAN POOR</strong> AIREP (AMC1 ADR.OPS.B.037(c)). AIREPs are used to trigger reassessments, confirm the initial assessment, and adjust the RWYCC.</p>
<h2>Upgrade and downgrade</h2>
""" + cards([
    ("Downgrade", "lower the RWYCC", "Possible when evidence or criteria in the procedures (AIREPs, measurements…) show worse conditions than the visual assessment."),
    ("Upgrade from 2 or more", "raise the RWYCC", "<b>Not allowed.</b>"),
    ("Upgrade from 0 or 1", "raise the RWYCC", "Allowed <b>up to RWYCC 3 at most</b>, only with evident proof defined in the procedures (e.g. friction measurements showing wet-runway equivalence, number of AIREPs above a threshold)."),
    ("After an upgrade", "", "Frequent reassessment is mandatory to make sure the RWYCC does not get worse — typically after decontamination."),
]) + """
<h2>Worked example 1 — snow</h2>
<p>Runway 04R/22L, 22L in use, 3,000 m, OAT +3 °C. Third 1: dry snow 4 mm, 75 %. Third 2: dry snow 1–3 mm, 50 %. Third 3: wet snow 3 mm, 50 %.</p>
""" + cards([
    ("Initial RWYCC?", "per third", "<b>3 / 5 / 5</b> — dry snow more than 3 mm gives 3; up to 3 mm gives 5."),
    ("AIREPs: GOOD, GOOD, GOOD TO MEDIUM, GOOD", "Change the codes?", "<b>No.</b> No upgrade (initial ≥ 2). No downgrade: one GOOD TO MEDIUM (code 4) without other evidence is not enough."),
], hint="Decide, then tap.") + """
<h2>Worked example 2 — water</h2>
<p>Same runway, OAT +10 °C. Third 1: dry. Third 2: water 2 mm, 40 %. Third 3: standing water 4 mm, 90 %.</p>
""" + cards([
    ("Initial RWYCC?", "per third", "<b>6 / 5 / 2</b>"),
    ("AIREPs: MEDIUM, MEDIUM, MEDIUM, GOOD TO MEDIUM", "Change the codes?", "<b>Consider a downgrade</b> of thirds 1 and 2: MEDIUM (code 3) is worse than the codes assessed. No upgrade of third 3 (initial ≥ 2)."),
], hint="Decide, then tap."),
takeaways=["AIREP terms = RCAM braking action terms; no AIREP for 6.", "Reassess after 2 consecutive POOR or 1 LESS THAN POOR.",
           "Downgrade with evidence; upgrade only from 0 or 1, up to 3, with evident proof."],
check=dict(q="The visual assessment gives RWYCC 1. Can the operator upgrade it?", options=["No, never", "Yes, up to 3 at most, with evident proof defined in the procedures", "Yes, to 5 with one GOOD AIREP", "Only to 6"], answer=1,
           explain="Upgrades are possible only from 0 or 1, up to 3, with evident proof."),
),
# 7 ------------------------------------------------------------------ MODULE 3
dict(title="The RCR — Principles and Triggers", minutes=12,
objectives=["Describe the two sections of the RCR.", "List the events that require a new RCR.",
            "Apply the significant change criteria for coverage and depth."],
body="""
<h2>Two sections</h2>
""" + cards([
    ("Aeroplane performance calculation section", "mandatory", "Per runway third: <b>RWYCC</b>, coverage, depth and contaminant type, plus the width to which the codes apply if reduced."),
    ("Situational awareness section", "optional", "Qualitative information: reduced length, drifting snow, loose sand, chemical treatment, snowbanks, taxiway and apron conditions, free text."),
]) + fig("airbus-05", "Content of the RCR and a SNOWTAM example: performance section per third, then situational awareness.", _AB) + """
<h2>When to write an RCR</h2>
<ul>
  <li>A contaminant <strong>appears</strong> (e.g. water on a dry runway).</li>
  <li>The contaminant <strong>type changes</strong> (e.g. thin dry snow turns to water).</li>
  <li>The <strong>reported coverage</strong> changes.</li>
  <li>The <strong>reported depth</strong> changes significantly.</li>
  <li><strong>New relevant information</strong> arrives: AIREPs, weather, decontamination, one LESS THAN POOR or two consecutive POOR.</li>
</ul>
<p>The need for an RCR triggers an inspection — and an inspection can trigger an RCR. Inspections are either scheduled or "special".</p>
<h2>Coverage changes</h2>
""" + cards([
    ("Third: 20 % → 40 %", "", "<b>New RCR</b>: the reported coverage changes from 25 to 50."),
    ("Third: 80 % → 100 %", "", "<b>No new RCR</b>: the reported coverage stays 100."),
], hint="Is a new RCR needed? Tap to check.") + """
<h2>Depth changes</h2>
<p>A change of depth is significant when it changes the RWYCC, or when the increase of the reported depth reaches a fixed value:</p>
""" + fig("table-depth-change", "Significant change of the reported depth: standing water 3 mm · slush 3 mm · wet snow 5 mm · dry snow 20 mm.") + cards([
    ("Dry snow 5 mm → 15 mm", "same area", "<b>No new RCR required</b>: +10 mm is below the 20 mm fixed value (if the RWYCC does not change)."),
    ("Standing water 5 mm → 8 mm", "", "<b>New RCR</b>: +3 mm reaches the 3 mm value."),
], hint="Is a new RCR needed? Tap to check."),
takeaways=["RCR = mandatory performance section + optional situational awareness section.", "New RCR: new contaminant, type change, reported coverage change, significant depth change, new information.",
           "Significant depth change: water 3 mm, slush 3 mm, wet snow 5 mm, dry snow 20 mm."],
check=dict(q="The coverage on a third increases from 80 % to 100 %. Is a new RCR required for this reason?", options=["Yes", "No — the reported coverage remains 100", "Only at night", "Only if the RWYCC is 6"], answer=1,
           explain="The reported value is already 100: no change in the RCR."),
),
# 8
dict(title="Writing the RCR", minutes=14,
objectives=["Fill in the performance section in the correct format.", "Use the standard expressions of the situational awareness section.",
            "Write RCRs for typical situations."],
body="""
<h2>Performance section — format</h2>
<table><thead><tr><th>Item</th><th>Format</th><th>Example</th></tr></thead><tbody>
<tr><td>Aerodrome location indicator (Doc 7910)</td><td>nnnn</td><td>DAAG</td></tr>
<tr><td>Date and time of assessment (UTC)</td><td>MMDDhhmm</td><td>01030723</td></tr>
<tr><td>Lower runway designator</td><td>nn[L/C/R]</td><td>05</td></tr>
<tr><td>RWYCC per third</td><td>n/n/n</td><td>5/5/2</td></tr>
<tr><td>Coverage per third</td><td>NR, 25, 50, 75, 100</td><td>100/100/75</td></tr>
<tr><td>Depth per third</td><td>NR or 2–3 digits</td><td>NR/NR/06</td></tr>
<tr><td>Contaminant per third</td><td>CAPITALS</td><td>WET/WET/STANDING WATER</td></tr>
<tr><td>Width to which the codes apply, if less than published</td><td>nn</td><td>30</td></tr>
</tbody></table>
""" + fig("rcr-form", "RCR form — aeroplane performance calculation section and situational awareness section.", "Company GRF documentation — RCR form") + """
<h2>Typical RCRs</h2>
""" + cards([
    ("After a shower: whole runway, water &lt; 3 mm", "write the codes", "<b>5/5/5 100/100/100 NR/NR/NR WET/WET/WET</b>"),
    ("Temperature and wind have dried the runway", "write the codes", "<b>6/6/6 NR/NR/NR NR/NR/NR DRY/DRY/DRY</b>"),
    ("Rubber in the touchdown zone, poor texture", "write the codes", "<b>3/3/3 100/100/100 NR/NR/NR SLIPPERY WET/SLIPPERY WET/SLIPPERY WET</b>"),
    ("Mixed: 09R", "wet · slush 6 mm 50 % · slush 6 mm 75 %", "<b>09R 5/2/2 100/50/75 NR/06/06 WET/SLUSH/SLUSH</b>"),
], hint="Write it on paper, then tap to compare.") + """
<h2>Situational awareness section</h2>
<ul>
  <li>RWY nn LDA REDUCED TO [n]nnn · RWY nn DRIFTING SNOW · RWY nn LOOSE SAND · RWY nn CHEMICALLY TREATED</li>
  <li>RWY nn SNOWBANK Lnn / Rnn / LRnn FM CL · TWY nn SNOWBANK · RWY nn ADJ SNOWBANKS</li>
  <li>TWY nn POOR · APRON nnnn POOR · free-text remarks</li>
  <li><strong>UPGRADED</strong> or <strong>DOWNGRADED</strong> to report an adjustment of the RWYCC.</li>
</ul>
<p>Only CAPITAL letters and digits. In the performance section, a <strong>space</strong> separates the items and "/" the thirds; in the situational awareness section a <strong>full stop</strong> separates the groups. Example: <strong>RWY 22L LDA REDUCED TO 1450. RWY 02R LOOSE SAND. TWY B POOR.</strong></p>
<h2>The drafting aid</h2>
""" + fig("rcr-guide", "RCR drafting aid: launch, coverage criteria per third, characterisation of each third with the RCAM, RCR and SNOWTAM.", "Company GRF documentation — RCR drafting aid"),
takeaways=["Performance section: aerodrome, MMDDhhmm, lower designator, RWYCC, coverage, depth, contaminant — per third.", "Capitals and digits only; space between items, full stop between situational awareness groups.",
           "UPGRADED / DOWNGRADED report an adjustment."],
check=dict(q="How is a whole wet runway (less than 3 mm) reported?", options=["6/6/6 DRY", "5/5/5 100/100/100 NR/NR/NR WET/WET/WET", "2/2/2 STANDING WATER", "5/5/5 NR/NR/NR 03/03/03"], answer=1,
           explain="WET, RWYCC 5, coverage 100, depth not reported."),
),
# 9 ------------------------------------------------------------------ MODULE 4
dict(title="Transmission of the Information — SNOWTAM, ATS and ATIS", minutes=12,
objectives=["Describe the SNOWTAM rules (format, language, validity, replacement).", "Apply the SNOWTAM publication criteria.",
            "Describe how ATS and ATIS pass the RCR to pilots and how AIREPs come back."],
body="""
<h2>The information flow</h2>
<p>The aerodrome operator sends the <strong>RCR</strong> to the air traffic services and requests a <strong>SNOWTAM</strong> from the aeronautical information service. ATS pass the information to pilots <strong>by radio and ATIS</strong>; pilots send <strong>AIREPs</strong> back through ATS.</p>
""" + fig("photo-tower", "Air traffic services transmit the RCR to pilots and pass their AIREPs to the aerodrome operator.") + """
<h2>SNOWTAM rules</h2>
""" + cards([
    ("SNOWTAM", "definition", "A special series NOTAM, in a standard format, that publishes the RCR — new format since the GRF (EU 2020/469)."),
    ("Language", "", "Issued in <b>English</b> (national language in addition if necessary)."),
    ("Validity", "", "<b>8 hours maximum.</b> A new SNOWTAM is issued with each new RCR and replaces the previous one."),
    ("Times", "", "Filing time is <b>after</b> the observation time — ideally as close as possible."),
    ("Error", "", "Issue a new SNOWTAM and cancel the previous one; check the accuracy of what is published and inform the personnel concerned."),
    ("Two SNOWTAMs?", "", "Never: the new one replaces the old one."),
]) + """
<h2>Example</h2>
<p>SNOWTAM 0131, EADD:<br><strong>02170055 09L 5/5/5 100/100/100 NR/NR/03 WET/WET/WET SNOW</strong><br><strong>02170135 09R 5/2/2 100/50/75 NR/06/06 WET/SLUSH/SLUSH</strong></p>
<p>One SNOWTAM can contain the RCR of one or several runways, each with its own observation time.</p>
<h2>When is a SNOWTAM published?</h2>
<table><thead><tr><th>Runway</th><th>Action</th></tr></thead><tbody>
<tr><td>Contaminated (standing water, snow, slush, ice, frost) on at least part</td><td>SNOWTAM via AIS <strong>and</strong> RCR to ATS</td></tr>
<tr><td>Dry, wet or slippery wet after removal or treatment of snow, slush, ice or frost</td><td>SNOWTAM via AIS and RCR to ATS</td></tr>
<tr><td>Wet or slippery wet in other cases (e.g. a dry runway becomes wet)</td><td>RCR to ATS (controller or AFIS) only</td></tr>
</tbody></table>
<h2>ATS and ATIS</h2>
<ul>
  <li>ATS transmit the RCR information <strong>in the landing direction</strong> of the runway in use, by radio and on the ATIS.</li>
  <li>Basic rule: when the runway is not dry, ATS request <strong>AIREPs</strong> from pilots.</li>
  <li>Pilots report the braking action when it is equal to or worse than the reported condition.</li>
</ul>
""" + fig("photo-fms-braking", "On board: braking action computed and the reminder to report if equal to or worse than given by ATS."),
takeaways=["RCR → ATS (radio, ATIS); RCR → AIS → SNOWTAM.", "SNOWTAM: English, 8 h maximum, new one replaces old, filed after observation.",
           "Runway not dry → ATS request AIREPs."],
check=dict(q="What is the maximum validity of a SNOWTAM?", options=["4 hours", "8 hours", "12 hours", "24 hours"], answer=1, explain="8 hours maximum; a new RCR gives a new SNOWTAM that replaces the previous one."),
),
# 10
dict(title="For Flight Crews — GRF and Aircraft Performance", minutes=12,
objectives=["Explain how contaminants affect acceleration and braking.", "Use the RWYCC as a direct input to the landing performance assessment at the time of arrival.",
            "Describe the effects on dispatch and take-off, and the robustness margins."],
body="""
<h2>Effects of contaminants on performance</h2>
<ul>
  <li><strong>Braking reduced</strong>: lower wheel-to-ground friction, aquaplaning.</li>
  <li><strong>Acceleration reduced</strong>: contaminant drag — displacement/compression drag and spray impingement drag.</li>
</ul>
""" + fig("airbus-02", "Runway condition and aircraft performance: macrotexture, microtexture, contamination, rubber, rutting, water accumulation.", _AB) + fig("airbus-03", "Effects on performance: spray impingement drag, displacement/compression drag, reduced braking (μB), aquaplaning.", _AB) + """
<h2>Why the 3 mm and 25 % values?</h2>
""" + fig("airbus-10", "Depth: up to 3 mm the tyre drains the fluid (WET, no dynamic aquaplaning); above 3 mm CONTAMINATED and aquaplaning above the aquaplaning speed. Some evidence shows slippery conditions even below 3 mm.", _AB) + fig("airbus-11", "Coverage: reported for each third; contaminated in terms of performance above 25 %.", _AB) + """
<h2>Landing — assessment at the time of arrival</h2>
<p>The <strong>RWYCC is a direct input</strong> to the in-flight landing distance computation, together with OAT, approach speed, autoland, autobrake and reverse thrust. A <strong>15 % margin</strong> is applied to the in-flight landing distance.</p>
""" + fig("airbus-16", "Performance at time of landing: RWYCC 6 to 1, OAT, approach speed, autobrake, reverse thrust — with a 15 % margin.", _AB) + fig("airbus-17", "The RWYCC is selected directly in the performance application (RWY COND list).", _AB) + """
<h2>Robustness to misreported RWYCC</h2>
<p>The computation is not always robust to an <strong>optimistic error of one code</strong>. Pay particular attention to the transitions <strong>dry to wet (6 to 5)</strong>, <strong>wet to standing water (5 to 2)</strong> and <strong>to POOR or LESS THAN POOR (1 or 0)</strong>.</p>
""" + fig("airbus-14", "Increase in landing distance for an optimistic RWYCC by one code: the transitions 6→5, 5→2 and to 1/0 are critical.", _AB) + """
<h2>Dispatch and take-off</h2>
<ul>
  <li><strong>Dispatch</strong> is nominally unchanged. Crosscheck the dispatch result with the landing distance at time of arrival before every flight; compute again in flight only in case of changes (runway, weather or surface condition, failures).</li>
  <li><strong>Take-off</strong> performance for contaminated surfaces follows EASA AMC 25.1591; some RCAM contaminant types are missing in the data, and a downgraded RWYCC with fluid contaminants needs care — enter both contaminant type and depth, and the RWYCC.</li>
</ul>
<h2>Benefits for operators</h2>
""" + cards([
    ("One global standard", "", "The same terms and codes everywhere — easier to understand than the old SNOWTAM."),
    ("Direct link to performance", "", "The RWYCC is entered directly into the landing performance computation."),
    ("Same information everywhere", "", "RCR, SNOWTAM, ATIS and ATC give the same picture."),
    ("Continuous observation", "", "AIREPs from crews keep the report close to reality — report braking action."),
]),
takeaways=["Contaminants: less braking (friction, aquaplaning) and less acceleration (drag).", "RWYCC = direct input at time of arrival; add 15 %.",
           "Beware optimistic codes at 6→5, 5→2 and to 1/0; report braking action."],
check=dict(q="Which margin is applied to the in-flight landing distance at the time of arrival?", options=["0 %", "15 %", "40 %", "67 %"], answer=1, explain="Pilots apply a 15 % margin to the landing distance assessment at time of arrival."),
),
]

QUESTIONS = [
Q(1, "Runway excursions represent about what share of all accidents (IATA 2010–2014)?", ["5 %", "22 %", "50 %", "90 %"], 1, "About 22 %, the third category by victims."),
Q(1, "Why were friction measurements abandoned in GRF reports?", ["Too cheap", "Poor reliability and poor correlation with aircraft braking", "ICAO banned all devices", "Pilots requested it"], 1, "Different devices, averages and no correlation."),
Q(1, "Which two objectives does ICAO pursue with the GRF?", ["Each State its own criteria; remove all risk", "Improve safety on contaminated runways; harmonised assessment and reporting", "More friction tests; fewer reports", "Winter only reporting"], 1, "Safety and harmonisation."),
Q(2, "Who assigns the RWYCC?", ["The pilot", "The aerodrome operator, with the RCAM", "ATC", "The aircraft manufacturer"], 1, "Aerodrome operator after inspection."),
Q(2, "Who transmits AIREPs to the aerodrome operator?", ["AIS", "Air traffic services", "The airline", "Nobody"], 1, "Pilots report to ATS, which pass them on."),
Q(2, "With the GRF, the RCR is published:", ["In winter only", "All year", "Only at night", "Only for snow"], 1, "Wet and slippery wet runways are reported all year."),
Q(2, "Which key changes does the GRF bring for the aerodrome operator?", ["Pilot information only", "Use of the RCAM and information from both the aerodrome operator and pilots", "A fixed report frequency", "Friction values"], 1, "RCAM plus AIREPs."),
Q(3, "A wet runway has water up to and including:", ["1 mm", "3 mm", "5 mm", "10 mm"], 1, "Above 3 mm: standing water."),
Q(3, "How many contaminant descriptors are used?", ["4", "6", "8", "12"], 2, "Eight, which can be combined."),
Q(3, "Snow that forms a compact ball with no water running out, near 0 °C, is:", ["Dry snow", "Wet snow", "Slush", "Compacted snow"], 1, "Wet snow."),
Q(3, "Granular deposit, calm wind, more on metal signs, ground well below 0 °C:", ["Ice", "Frost", "Dry snow", "Wet ice"], 1, "Frost."),
Q(3, "Snow that a vehicle does not sink into and that breaks into lumps:", ["Slush", "Compacted snow", "Wet snow", "Dry snow"], 1, "Compacted snow."),
Q(4, "What does the RCAM NOT contain?", ["Contaminant type", "Depth", "Friction coefficient values", "AIREP terms"], 2, "No friction values in any RCAM."),
Q(4, "Compacted snow at OAT −20 °C gives RWYCC:", ["5", "4", "3", "2"], 1, "−15 °C or colder → 4."),
Q(4, "Ice gives RWYCC:", ["3", "2", "1", "0"], 2, "Ice → 1 (POOR)."),
Q(4, "Wet ice gives RWYCC:", ["2", "1", "0", "3"], 2, "Wet ice → 0 (LESS THAN POOR)."),
Q(4, "Slippery wet gives RWYCC:", ["5", "4", "3", "2"], 2, "Slippery wet → 3."),
Q(5, "The first third of the runway starts at:", ["The threshold in use", "The end with the lower runway designator", "The displaced threshold", "The stopway"], 1, "Always from the lower designator."),
Q(5, "Water covers 20 % of a third. The RWYCC of this third is:", ["5", "6, with coverage reported 25", "2", "Not reported"], 1, "10–25 % → RWYCC 6, coverage 25."),
Q(5, "Estimated coverage 60 % is reported as:", ["50", "60", "75", "100"], 2, "51–75 % → 75."),
Q(5, "The depth must be measured:", ["To the millimetre", "Precisely enough to know whether 3 mm is exceeded", "Only for ice", "Never"], 1, "The 3 mm threshold matters."),
Q(6, "Which AIREP corresponds to RWYCC 2?", ["MEDIUM", "MEDIUM TO POOR", "POOR", "GOOD TO MEDIUM"], 1, "MEDIUM TO POOR = 2."),
Q(6, "A reassessment of the runway is required after:", ["One GOOD AIREP", "Two consecutive POOR or one LESS THAN POOR", "Any AIREP", "Every hour"], 1, "AMC1 ADR.OPS.B.037(c)."),
Q(6, "An initial RWYCC of 3 can be upgraded with AIREPs:", ["Yes, to 5", "No — no upgrade from 2 or more", "Yes, to 6", "Only at night"], 1, "Upgrades only from 0 or 1."),
Q(6, "From RWYCC 1, the maximum upgrade with evident proof is to:", ["2", "3", "5", "6"], 1, "Up to 3."),
Q(6, "Pilots send AIREPs to:", ["The aerodrome operator directly", "The air traffic controller", "AIS", "The airline only"], 1, "On the frequency to ATC."),
Q(7, "Which RCR section is mandatory?", ["Situational awareness", "Aeroplane performance calculation", "Both are optional", "Free text"], 1, "Performance section is mandatory."),
Q(7, "Dry snow depth increases from 5 to 15 mm on the same area (RWYCC unchanged):", ["New RCR required", "No new RCR required — below the 20 mm fixed value", "SNOWTAM cancelled", "RWYCC 0"], 1, "Dry snow significant change: 20 mm."),
Q(7, "A new contaminant appears during an inspection:", ["No RCR", "A new RCR is issued", "Only if RWYCC increases", "Only a NOTAM"], 1, "Appearance of a contaminant → new RCR."),
Q(7, "Significant depth change for standing water is:", ["1 mm", "3 mm", "5 mm", "20 mm"], 1, "3 mm."),
Q(8, "The date and time in the RCR use the format:", ["DDMMYY", "MMDDhhmm (UTC)", "hh:mm local", "YYYYMMDD"], 1, "MMDDhhmm UTC."),
Q(8, "In the situational awareness section, groups are separated by:", ["A comma", "A full stop", "A slash", "A dash"], 1, "Full stop."),
Q(8, "Which expression reports an adjustment of the RWYCC?", ["CHANGED", "UPGRADED / DOWNGRADED", "CORRECTED", "AMENDED"], 1, "Standard expression."),
Q(9, "A SNOWTAM must be issued in:", ["The national language only", "English", "French only", "Any language"], 1, "English (national language in addition if needed)."),
Q(9, "Can two SNOWTAMs for the same aerodrome coexist?", ["Yes", "No — the new one replaces the old one", "Only for two runways", "Only for 1 hour"], 1, "A new SNOWTAM replaces the previous one."),
Q(9, "A dry runway becomes wet after a shower. The aerodrome:", ["Issues a SNOWTAM", "Sends an RCR to ATS", "Does nothing", "Closes the runway"], 1, "Wet in other cases: RCR to ATS only."),
Q(9, "ATS give the RCR to pilots:", ["In the lower designator order", "In the landing direction of the runway in use", "Only on request", "Only by SNOWTAM"], 1, "In the landing direction, by radio and ATIS."),
Q(10, "Contaminant drag mainly reduces:", ["Braking", "Acceleration", "Lift", "Visibility"], 1, "Displacement and spray drag reduce acceleration."),
Q(10, "Which transition is particularly critical if misreported?", ["4 to 3", "5 to 2 (wet to standing water)", "3 to 3", "6 to 6"], 1, "Also 6→5 and to 1/0."),
Q(10, "Dispatch landing performance with the GRF:", ["Is fully replaced", "Is nominally unchanged; crosscheck with the landing distance at time of arrival", "Uses friction values", "Is not required"], 1, "Dispatch unchanged; assessment at time of arrival."),
]

COURSE = dict(
    slug="grf",
    title="Global Reporting Format (GRF)",
    header_title="Global Reporting Format (GRF)",
    tagline="Runway surface condition assessment and reporting with the GRF: why it exists, contaminants, the RCAM and RWYCC, pilot reports, the RCR, SNOWTAM and ATS — and what it means for aircraft performance. Definitions as interactive flip cards.",
    purpose="Explain the ICAO Global Reporting Format so that every actor — aerodrome operator, ATS, AIS and flight crews — understands the runway condition report and its transmission, following the company GRF syllabus (4 h 15) and completed with the flight crew performance perspective.",
    audience="Flight crew of all fleets (B737-800, Q400, Q200), flight operations and ground staff concerned by runway condition reporting.",
    objectives=["Identify the objectives pursued by ICAO", "Describe the main characteristics of the new system", "Identify runway surface states and contaminants",
                "Assign a RWYCC with the RCAM", "Adjust the RWYCC with pilot reports", "Write and update a runway condition report", "Describe the SNOWTAM and the information flow",
                "Use the RWYCC in the landing performance assessment"],
    icon="snow", cert_prefix="GRF", quiz_count=20, pass_mark=80,
    group="refresher", season="Additional",
    finale=None,
    modules=[dict(title="The Global Reporting Format", summary="Why the GRF, actors and changes, surface states and contaminants", icon="search", lessons=range(1, 4)),
             dict(title="The RCAM", summary="Matrix, thirds, coverage, depth, temperature, AIREPs and RWYCC adjustment", icon="snow", lessons=range(4, 7)),
             dict(title="The RCR", summary="Principles, triggers and writing the report", icon="runway", lessons=range(7, 9)),
             dict(title="Transmission and Performance", summary="SNOWTAM, ATS, ATIS — and the RWYCC in the landing performance", icon="plane", lessons=range(9, 11))],
    lessons=LESSONS, questions=QUESTIONS,
    images={1: ("photo", "Snow clearing vehicle on a runway", "Why the GRF?"),
            2: ("photo", "Pilots on the flight deck", "Every actor has a role."),
            3: ("photo", "Frost on the pavement", "Name the contaminant correctly."),
            4: ("photo", "Snow-covered runway seen from the flight deck", "Contaminant, depth, temperature → RWYCC."),
            5: ("photo", "Standing water on the taxiway", "Thirds, coverage, depth."),
            6: ("photo", "Pilots during the landing", "Report braking action."),
            7: ("photo", "Snow ploughs clearing the runway", "A significant change means a new RCR."),
            8: ("photo", "Wet snow close-up", "Capitals, codes, thirds."),
            9: ("photo", "Control tower", "SNOWTAM, radio and ATIS."),
            10: ("photo", "Aircraft landing through spray", "The RWYCC goes straight into the performance.")},
)
