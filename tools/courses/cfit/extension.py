"""CFIT course extension (Nov 2026) from the documents provided by the training department:
- ICAO Doc 10004, Global Aviation Safety Plan (GASP) 2026-2028 — CFIT is a global high-risk category (G-HRC);
- IATA, CFIT — A Study of TAWS Capability and Human Factors in CFIT Accidents 2005-2014 (1st edition, 2016);
- IATA, CFIT workshop: CFIT Detailed Implementation Plan (DIP) and accident analysis (October 2024);
- Flight Safety Foundation CFIT Checklist (reprint permitted with credit to the Foundation);
- SKYbrary, Controlled Flight Into Terrain (CFIT) — scenarios, contributing factors, defences, recent events.

The course grows from 9 to 13 lessons. Existing lessons keep their content; new sections are inserted.
"""
import re

IMG = "../media/images/"
IATA_STUDY = "IATA, CFIT — A Study of TAWS Capability and Human Factors in CFIT Accidents 2005–2014"
IATA_DIP = "IATA CFIT workshop — CFIT Detailed Implementation Plan (2024)"


def pic(img, caption, src):
    return (f'<figure class="lesson-figure"><img src="{IMG}{img}.jpg" alt="{caption}" loading="lazy">'
            f'<figcaption>{caption} <span class="muted">Source: {src}.</span></figcaption></figure>')


def after_section(body, h2, html):
    """Append html at the end of the named section."""
    tag = f"<h2>{h2}</h2>"
    assert tag in body, h2
    i = body.index(tag) + len(tag)
    j = body.find("<h2>", i)
    j = len(body) if j < 0 else j
    return body[:j] + html + "\n" + body[j:]


# ------------------------------------------------------------------ additions to existing lessons
L1_ADD = """
<h2>A global high-risk category</h2>
<p>ICAO's <strong>Global Aviation Safety Plan (Doc 10004, 2026–2028)</strong> aims at <strong>zero fatal accidents in commercial operations by 2030 and beyond</strong>. It names five <strong>global high-risk categories (G-HRC)</strong>, on which States, regions and operators must concentrate:</p>
<ol class="steps">
  <li><strong>Controlled flight into terrain (CFIT)</strong></li>
  <li>Loss of control in flight (LOC-I)</li>
  <li>Mid-air collision (MAC)</li>
  <li>Runway excursion (RE)</li>
  <li>Runway incursion (RI)</li>
</ol>
<p>The same categories apply to turboprops and jets alike. National and company safety plans (NASP, SMS) must address them.</p>

<h2>What the data say</h2>
<div class="table-wrap"><table>
<tr><th>IATA study, 67 CFIT accidents 2005–2014</th><th></th></tr>
<tr><td>Fatalities</td><td><strong>1,346</strong></td></tr>
<tr><td>Hull loss</td><td><strong>99 %</strong> of CFIT accidents</td></tr>
<tr><td>Accidents with fatalities</td><td><strong>88 %</strong></td></tr>
<tr><td>Occupants surviving</td><td>about <strong>18 %</strong></td></tr>
<tr><td>Phase of flight</td><td>approach <strong>47.7 %</strong>, landing <strong>16.4 %</strong></td></tr>
</table></div>
""" + pic("iata-study-p16", "CFIT accidents 2006–2015: share of all accidents and rate per million sectors.", IATA_STUDY + ", Figure 0.1") + """
<p>CFIT is rare, but when it happens it is almost never survivable. It remains one of the two leading causes of fatal commercial accidents, with loss of control in flight.</p>
""" + pic("iata-slide-03", "CFIT accidents worldwide 2014–2024: accidents and fatalities by year, region and phase of flight.", IATA_DIP) + """
<p class="muted">IATA notes that 24 % of CFIT accidents worldwide in 2014–2024 could not be fully classified because of insufficient data — three of them involved operators in the AFI region. Reporting matters.</p>
"""

L5_ADD = """
<h2>The briefing: the first defence</h2>
<p>IATA's CFIT implementation plan stresses that a thorough briefing lets the crew know the main features of the departure, descent, approach and missed approach, the terrain and the hazards. Brief:</p>
<div class="table-wrap"><table>
<tr><th>Departure briefing</th><th>Approach briefing</th></tr>
<tr><td>Significant terrain and obstacles along the departure route; the SID and the MSA; the engine-out procedure</td><td>Descent profile and energy management; terrain and approach hazards; the elements of an unstable approach; the missed approach; MSA and the applicable minima (visibility, RVR, ceiling); the go-around altitude</td></tr>
</table></div>
"""

L6_ADD = """
<h2>Keeping the system effective (IATA CFIT plan)</h2>
<ul>
  <li><strong>Up-to-date software and databases</strong> — terrain, obstacle and runway databases updated as issued by the manufacturer, under one department's responsibility and a formal process.</li>
  <li><strong>GNSS position source</strong> — the EGPWS should use GPS/GNSS position; without it, the look-ahead depends on the FMS position.</li>
  <li><strong>Terrain display policy</strong> — at least one pilot selects the terrain display in critical phases (climb, and descent below MSA); both pilots when weather is not a threat.</li>
  <li><strong>Always active and serviceable</strong> — procedures ensure the EGPWS is never left inhibited.</li>
  <li><strong>GPS interference</strong> — report GNSS jamming or spoofing and radio altimeter anomalies immediately to ATC and the authority: they degrade the EGPWS.</li>
</ul>
<div class="callout warn"><span class="label">Not a navigation tool</span><p>The EGPWS is <strong>not</strong> a primary reference for terrain or obstacle avoidance. The crew remains responsible for terrain clearance — and, on a visual approach, for its own separation from terrain and obstacles.</p></div>
"""

L8_ADD = """
<h2>What the accidents show</h2>
<p>The IATA study found that, where fitted, the GPWS/EGPWS <strong>performed as designed</strong>. In accidents with a working terrain warning system, the system gave enough time to react — but the crew <strong>delayed the response or made an inadequate avoidance manoeuvre</strong>. The warning works only if the response is immediate and complete.</p>
"""

# ------------------------------------------------------------------ new lessons
L_HOW = dict(title="How CFIT Happens: Scenarios, Precursors and Defences", minutes=9,
objectives=["Describe typical pilot-induced and ATC-induced CFIT scenarios.", "List the contributing factors found in CFIT accidents.", "Explain precursors and the layered defences against CFIT."],
body="""
<h2>Two typical scenarios</h2>
<div class="table-wrap"><table>
<tr><th>Pilot-induced</th><th>ATC-induced</th></tr>
<tr><td>Weather is worse than forecast. To keep or regain visual contact in very low cloud, the pilot descends below the MSA and strikes the ground — often relying on GPS and losing terrain awareness.</td><td>During radar vectors at 210 kt, the controller gives a heading towards the ILS but, distracted, fails to give the intercept heading. The crew, unfamiliar with the approach, do not query it in time; the aircraft flies through the localiser into high terrain.</td></tr>
</table></div>
<p class="muted">Scenarios from SKYbrary, Controlled Flight Into Terrain.</p>

<h2>What the investigations found</h2>
<p>The IATA analysis of CFIT accidents identified, again and again:</p>
<ul>
  <li>CFIT in most phases, but mostly in <strong>approach and landing</strong>, often on <strong>non-precision approaches</strong>;</li>
  <li><strong>descent below MDA or DA</strong> without adequate visual reference;</li>
  <li><strong>lack of positional awareness</strong>;</li>
  <li><strong>CRM failure</strong> — cross-check, communication, coordination, leadership;</li>
  <li>no response, or a <strong>delayed response</strong>, to ground proximity warnings;</li>
  <li><strong>non-adherence to SOPs</strong>, improvised approaches in IMC, operation in low cloud and poor visibility;</li>
  <li>early GPWS equipment, or none.</li>
</ul>

<h2>Contributing factors</h2>
<ul>
  <li><strong>Weather</strong>: rain, turbulence and icing raise workload; poor visibility and night cause disorientation.</li>
  <li><strong>Approach design and charts</strong>: unclear step-down fixes; approaches close to terrain for noise or airspace reasons.</li>
  <li><strong>Non-standard phraseology</strong> leading to confusion — altitude versus flight level, QNH versus QFE.</li>
  <li><strong>Fatigue and disorientation</strong> in a demanding phase of flight.</li>
</ul>

<h2>Precursors and defences</h2>
<p>A <strong>precursor</strong> is a warning that a defence is weak: an unexpected EGPWS alert, a level bust near terrain, a wrong altimeter setting, an unstable approach continued. Report every one — they show where to strengthen the defences:</p>
<ol class="steps">
  <li>SOPs and briefings; terrain awareness.</li>
  <li>Stabilised approaches and CDFA; radio altimeter use.</li>
  <li>ATC minimum safe altitude warning (MSAW) and good phraseology.</li>
  <li>EGPWS / TAWS with current terrain and obstacle data (eTOD).</li>
  <li>Training, reporting and a just culture.</li>
</ol>
""",
takeaways=["Pilot-induced: descending below MSA to stay visual; ATC-induced: a vector into terrain not queried.", "Investigations: NPA, descent below minima, lost position awareness, CRM failure, late EGPWS response, SOP deviation.", "Precursors are warnings — report them to strengthen the defences."],
check=dict(q="Which is a CFIT precursor that should be reported?", options=["A normal ILS approach", "An unexpected EGPWS alert on approach", "A smooth landing", "A routine level change"], answer=1, explain="An unexpected EGPWS alert shows a weak defence and must be reported."),
)

L_HF = dict(title="Human Factors in CFIT Accidents", minutes=9,
objectives=["Use the 'dirty dozen' and the ICAO pilot competencies to analyse CFIT accidents.", "Identify the competencies most often deficient in CFIT accidents.", "Apply threat and error management to terrain threats."],
body="""
<h2>Two human factors models</h2>
<p>The IATA CFIT study analysed each accident with two models: the twelve human error precursors (Dupont's "dirty dozen") and the <strong>ICAO pilot competencies</strong> used in competency-based and evidence-based training (PANS-TRG, Doc 9868).</p>
""" + pic("iata-study-p20", "The 'dirty dozen' human error precursors and the ICAO pilot competencies.", IATA_STUDY + ", Tables 0.2 and 0.3") + """
<h2>What went wrong</h2>
<ul>
  <li><strong>Situational awareness</strong> was deficient in <strong>every</strong> accident.</li>
  <li><strong>Application of procedures</strong>, <strong>communication</strong> and <strong>leadership and teamwork</strong> were frequently deficient.</li>
  <li>Among the "dirty dozen", <strong>lack of awareness</strong>, <strong>lack of knowledge</strong>, <strong>lack of communication</strong> and <strong>lack of teamwork</strong> came first.</li>
</ul>
""" + pic("iata-competencies", "Deficient pilot competencies in the CFIT accidents analysed: situational awareness and application of procedures lead.", IATA_STUDY + ", Chart 1") + """
<h2>Precursors in each accident</h2>
""" + pic("iata-study-p55", "Competencies and 'dirty dozen' precursors combined, accident by accident: every accident had several.", IATA_STUDY + ", Chart 3") + """
<h2>Threat and error management</h2>
<p>CFIT accidents follow the TEM chain: <strong>threats</strong> (terrain, weather, ATC, charts) and <strong>errors</strong> (wrong altitude, wrong setting, wrong mode) lead to an <strong>undesired aircraft state</strong> (below the profile, off track) — and then to terrain. Each step is a chance to stop the chain.</p>
""" + pic("iata-tem", "Threat and error management: prevent threats and errors from becoming an undesired aircraft state (UAS).", IATA_DIP) + """
""",
takeaways=["Situational awareness was deficient in every CFIT accident analysed.", "Procedures, communication and teamwork were the next most deficient competencies.", "TEM: stop the chain at the threat, the error or the undesired state."],
check=dict(q="Which competency was found deficient in every CFIT accident analysed by IATA?", options=["Workload management", "Situational awareness", "Manual flight path management", "Communication"], answer=1, explain="Situational awareness was deficient in all cases."),
)

L_CASES = dict(title="CFIT Case Studies", minutes=10,
objectives=["Learn from CFIT accidents analysed by IATA.", "Recognise the near-CFIT events on Dash 8 aircraft.", "Relate each case to the defences in this course."],
body="""
<h2>Accidents analysed by IATA (de-identified)</h2>
<div class="table-wrap"><table>
<tr><th>Case</th><th>What happened</th><th>Lesson</th></tr>
<tr><td><strong>Jet, mountain, 2005</strong> — VOR/DME approach, snowstorm, 105 killed</td><td>Did not proceed to the VOR as instructed and descended below the assigned altitude before being established on any segment of the approach.</td><td>Never descend before being established on a published segment.</td></tr>
<tr><td><strong>Twin turboprop, ridge, 2005</strong> — RNAV (GNSS) NPA in IMC, 15 killed</td><td>Departed from the descent path and did not follow the chart's constant-angle descent points; descended below the 2,060 ft segment minimum after the FAF.</td><td>Fly the constant angle (CDFA); check each step altitude.</td></tr>
<tr><td><strong>Jet, sea, 2006</strong> — night IMC approach, 113 killed</td><td>Night flight after poor daytime rest; loss of situational awareness during the approach and go-around.</td><td>Fatigue and night approaches multiply the CFIT risk.</td></tr>
<tr><td><strong>Jet, mountain, 2010</strong> — circling in monsoon rain, 152 killed</td><td>During a circling approach the selected altitude was reduced below the circling minimum, contrary to SOP; the aircraft hit high ground.</td><td>Never descend below circling minima until on final with the runway in sight.</td></tr>
</table></div>

<h2>Accidents analysed by IATA (continued)</h2>
<div class="table-wrap"><table>
<tr><th>Case</th><th>What happened</th><th>Lesson</th></tr>
<tr><td><strong>Jet, hill, 2011</strong> — ILS/DME approach in low cloud, 12 killed</td><td>The aircraft drifted off the localiser; a go-around was started only 2 seconds before impact.</td><td>When the approach is not right, go around early.</td></tr>
<tr><td><strong>Jet, sea, 2013</strong> — VOR/DME NPA in rain, all survived</td><td>Continued below MDA without the required visual reference; the go-around was called at 20 ft.</td><td>No visual reference at MDA: go around immediately.</td></tr>
<tr><td><strong>Cargo jet, short of runway, 2013</strong> — night localiser NPA</td><td>Only the shorter runway with a non-precision approach was available; the descent continued below MDA without visual reference.</td><td>Brief NOTAMs and the approach options; respect the MDA.</td></tr>
</table></div>
<p class="muted">Summarised from {IATA_STUDY}, sections 7–15.</p>

<h2>Dash 8 near-CFIT events</h2>
<div class="table-wrap"><table>
<tr><th>Event</th><th>What happened</th><th>Lesson</th></tr>
<tr><td><strong>DHC-8, Svolvær, Norway, 2022</strong></td><td>On final in cloud, the aircraft came within less than 300 ft of terrain. An <strong>incorrect altimeter setting</strong> put the approach 700 ft below the profile. The crew responded to a valid EGPWS warning and went around.</td><td>Read back and cross-check every altimeter setting; trust the EGPWS.</td></tr>
<tr><td><strong>DHC-8, Val-d'Or, Canada, 2023</strong></td><td>The captain made an <strong>incorrect FMS entry</strong>; the first officer (PF) continued an excessively steep, off-track descent without visual reference until terrain alerts ended the approach.</td><td>Verify FMS entries; monitor the vertical and lateral path; PM speaks up.</td></tr>
</table></div>
<p class="muted">Source: SKYbrary, Controlled Flight Into Terrain — accidents and incidents.</p>
""".replace("{IATA_STUDY}", IATA_STUDY),
takeaways=["Descending before being established, below step or circling minima, or below MDA without visual reference: the recurring trap.", "Fatigue, night and IMC multiply the risk.", "Dash 8 lessons: wrong altimeter setting, wrong FMS entry — cross-check and trust the EGPWS."],
check=dict(q="In the 2022 Svolvær Dash 8 event, what put the approach 700 ft below the profile?", options=["Icing", "An incorrect altimeter setting", "An engine failure", "A wrong runway"], answer=1, explain="An incorrect altimeter setting; a valid EGPWS warning prompted the go-around."),
)

# Flight Safety Foundation CFIT Checklist — interactive (reprinted with credit to the Foundation)
_P1_GROUPS = [
    ("Airport and approach control capabilities", "radio", [("ATC approach radar with MSAWS", 0), ("ATC minimum radar vectoring charts", 0), ("ATC radar only", -10), ("ATC radar coverage limited by terrain masking", -15), ("No radar coverage available", -30), ("No ATC service", -30)]),
    ("Expected approach", "radio", [("ILS", 0), ("VOR/DME", -15), ("Non-precision approach, slope FAF–TD shallower than 2.75°", -20), ("NDB", -30), ("Visual night 'black-hole' approach", -30)]),
    ("Terrain", "check", [("Airport located in or near mountainous terrain", -20)]),
    ("Runway lighting", "radio", [("Complete approach lighting system", 0), ("Limited lighting system", -30)]),
    ("Controller / pilot language", "check", [("Controllers and pilots speak different primary languages", -20), ("Controllers' spoken English or ICAO phraseology poor", -20), ("Pilots' spoken English poor", -20)]),
    ("Departure", "check", [("No published departure procedure", -10)]),
]
_MULT_GROUPS = [
    ("Type of operation", [("Scheduled", 1.0), ("Nonscheduled", 1.2), ("Corporate", 1.3), ("Charter", 1.5), ("Regional", 2.0), ("Freight", 2.5), ("Domestic", 1.0), ("International", 3.0)]),
    ("Departure / arrival airport region (highest)", [("Africa", 8.0), ("Western Europe", 1.3), ("Middle East", 1.1), ("United States / Canada", 1.0), ("Euro-Asia", 3.0), ("Southeast Asia", 3.0), ("South America / Caribbean", 5.0)]),
    ("Weather / night", [("Day, no IMC", 0.0), ("Night — no moon", 2.0), ("IMC", 3.0), ("Night and IMC", 5.0)]),
    ("Crew", [("Two-pilot crew, normal duty", 0.0), ("Duty day at maximum, ending with a night non-precision approach", 1.2), ("Crew crossed five or more time zones", 1.2)]),
]


def _fsf_calc():
    import html as _h
    def opts(gi, kind, items, prefix):
        out = []
        mult = prefix == "mg"
        for k, (t, v) in enumerate(items):
            typ = "radio" if kind == "radio" else "checkbox"
            chk = " checked" if (kind == "radio" and k == 0) else ""
            out.append(f'<label class="fsf-o"><input type="{typ}" name="{prefix}{gi}" value="{v}"{chk}> {_h.escape(t)} <b>{("×" + format(v, "g")) if mult else format(v, "+g")}</b></label>')
        return "".join(out)
    p1 = "".join(f'<fieldset><legend>{_h.escape(g)}</legend>{opts(i, kind, items, "p1g")}</fieldset>' for i, (g, kind, items) in enumerate(_P1_GROUPS))
    mu = "".join(f'<fieldset><legend>{_h.escape(g)}</legend>{opts(i, "radio", items, "mg")}</fieldset>' for i, (g, items) in enumerate(_MULT_GROUPS))
    return """
<figure class="diagram dtcalc fsfcalc" id="fsfcalc">
<style>
.fsfcalc fieldset{border:1px solid #dbe5df;border-radius:8px;margin:0 0 10px;padding:8px 12px}
.fsfcalc legend{font-weight:700;color:#125a2b;font-size:.9rem}
.fsfcalc .fsf-o{display:block;font-size:.9rem;margin:3px 0;color:#24342b}
.fsfcalc .fsf-o b{color:#5b6b62;font-weight:600;margin-left:4px}
.fsfcalc .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.fsfcalc .res{background:#f3f9f5;border-radius:10px;padding:12px 14px;margin-top:10px;font-size:1rem;color:#24342b}
.fsfcalc .res .big{font-size:1.5rem;font-weight:800}
.fsfcalc .neg{color:#c8102e} .fsfcalc .pos{color:#1d7a3e}
.fsfcalc input[type=number]{width:90px;padding:6px;border:1px solid #cfdcd4;border-radius:6px}
</style>
<h3 style="margin-top:0;color:#14231b">Flight Safety Foundation CFIT Checklist — score a flight</h3>
<p style="color:#24342b;font-size:.9rem">Part I: choose the conditions of the flight (destination factors and risk multipliers). Part II: enter your company's risk-reduction totals from the full FSF checklist (company culture, flight standards, hazard awareness and training, aircraft equipment).</p>
<div class="cols"><div><h4 style="color:#14231b">Part I — Destination CFIT risk factors</h4>""" + p1 + """</div>
<div><h4 style="color:#14231b">Part I — Risk multiplier</h4>""" + mu + """
<h4 style="color:#14231b">Part II — Risk-reduction factors (company totals)</h4>
<label class="fsf-o">Company culture (max 130) <input type="number" id="fsf-cc" value="105"></label>
<label class="fsf-o">Flight standards (max 335) <input type="number" id="fsf-fs" value="270"></label>
<label class="fsf-o">Hazard awareness and training (max 315) <input type="number" id="fsf-ht" value="250"></label>
<label class="fsf-o">Aircraft equipment (max 195) <input type="number" id="fsf-ae" value="155"></label>
</div></div>
<div class="res" id="fsf-res"></div>
<p class="muted" style="font-size:.82rem">FSF CFIT Checklist © 1994 Flight Safety Foundation — reprinted for training with credit to the Foundation, as the checklist permits. A training tool to understand which factors raise or reduce CFIT risk; it does not replace the company risk assessment.</p>
<script>
(function(){
  var root=document.getElementById('fsfcalc');
  function val(name){var s=0;root.querySelectorAll('input[name="'+name+'"]:checked').forEach(function(e){s+=parseFloat(e.value)});return s}
  function num(id){return parseFloat(document.getElementById(id).value)||0}
  function rate(v,a,b,c){return v>=a?'tops':v>=b?'good':v>=c?'improvement needed':'high CFIT risk'}
  function calc(){
    var dest=0;for(var i=0;i<""" + str(len(_P1_GROUPS)) + """;i++)dest+=val('p1g'+i);
    var mult=0;for(var j=0;j<""" + str(len(_MULT_GROUPS)) + """;j++)mult+=val('mg'+j);
    var p1=dest*mult, cc=num('fsf-cc'), fs=num('fsf-fs'), ht=num('fsf-ht'), ae=num('fsf-ae'), p2=cc+fs+ht+ae, score=p1+p2;
    var h='Destination factors <b>'+dest+'</b> × risk multiplier <b>'+mult.toFixed(1)+'</b> = Part I <b class="neg">'+Math.round(p1)+'</b><br>';
    h+='Part II = '+cc+' + '+fs+' + '+ht+' + '+ae+' = <b class="pos">'+p2+'</b><br>';
    h+='<span class="big '+(score<0?'neg':'pos')+'">CFIT risk score '+(score>0?'+':'')+Math.round(score)+'</span><br>';
    h+=score<0?'<b class="neg">Negative score: significant CFIT threat — review the risk-reduction factors and mitigate before the flight (briefing, alternate, timing, crew).</b>':'<b class="pos">Positive score: the defences outweigh the risk factors — keep them in place.</b>';
    h+='<br><span style="font-size:.88rem">Company culture: '+rate(cc,115,105,80)+' · Flight standards: '+rate(fs,300,270,200)+' · Training: '+rate(ht,285,250,190)+' · Equipment: '+rate(ae,175,155,115)+'</span>';
    document.getElementById('fsf-res').innerHTML=h;
  }
  root.addEventListener('change',calc); root.addEventListener('input',calc); calc();
})();
</script>
</figure>
"""


L_RISK = dict(title="CFIT Risk Assessment: the FSF CFIT Checklist", minutes=10,
objectives=["Identify the destination factors that raise CFIT risk.", "Explain how the risk multipliers (operation, region, night, IMC, crew) work.", "Score a flight with the Flight Safety Foundation CFIT Checklist and decide on mitigations."],
body="""
<h2>Why assess CFIT risk</h2>
<p>The Flight Safety Foundation CFIT Checklist turns the lessons of CFIT accidents into numbers. <strong>Part I</strong> scores the risk of a flight (negative values); <strong>Part II</strong> scores the defences of the company (positive values); <strong>Part III</strong> adds them. A <strong>negative total</strong> means a significant CFIT threat.</p>
<ul>
  <li>Biggest destination penalties: <strong>no radar or no ATC</strong> (−30), <strong>NDB</strong> or <strong>night black-hole visual approach</strong> (−30), <strong>limited runway lighting</strong> (−30), <strong>mountainous terrain</strong> (−20).</li>
  <li>The penalties are <strong>multiplied</strong>: night and IMC (×5 together), the region of operation, the type of operation and a crew at maximum duty ending with a night non-precision approach.</li>
  <li>Defences that score high: management that places <strong>safety before schedule</strong> and puts no stigma on a <strong>diversion or missed approach</strong>; procedures for <strong>terrain review</strong> and <strong>independent altitude checks</strong>; annual <strong>CFIT case reviews</strong> and <strong>GPWS escape practice</strong> in the simulator; full EGPWS and radio altimeter callouts.</li>
</ul>

<h2>Score a flight</h2>
""" + _fsf_calc() + """
<h2>Use the result</h2>
<ol class="steps">
  <li>Try a day ILS to a radar-equipped airport, then a night NDB approach in mountainous terrain: see how the score changes.</li>
  <li>A negative score is not a "no-go" by itself — it is a call to <strong>mitigate</strong>: brief the terrain and the MSA, use the best approach available, consider timing (daylight), fuel and alternate, and the most experienced crew.</li>
  <li>Report the factors that the company can improve through the safety reporting system.</li>
</ol>
""",
takeaways=["Part I (risk, negative) × multipliers + Part II (defences, positive) = CFIT risk score.", "Night + IMC, no radar, NDB/black-hole approaches and mountainous terrain raise the risk most.", "A negative score calls for mitigation before the flight."],
check=dict(q="In the FSF CFIT Checklist, what does a negative CFIT risk score indicate?", options=["No risk", "A significant CFIT threat that requires mitigation", "The flight is cancelled automatically", "An error in the checklist"], answer=1, explain="A negative score indicates a significant threat; review and mitigate."),
)

L_PREVENT_ADD = """
<h2>The IATA CFIT implementation plan</h2>
<div class="table-wrap"><table>
<tr><th>Who</th><th>What is required</th></tr>
<tr><td><strong>Safety management</strong></td><td>Leadership commitment and a positive safety culture; FDM/FOQA monitoring of crew responses to EGPWS events; awareness of the consequences of deviating from procedures</td></tr>
<tr><td><strong>Training</strong></td><td>Gap analysis against the latest EGPWS training guidance (IATA, EASA, FAA, ICAO, manufacturers); competency-based and evidence-based training</td></tr>
<tr><td><strong>Flight operations</strong></td><td>Terrain display policy; immediate response to EGPWS warnings; reporting of GPS interference to ATC and authorities</td></tr>
<tr><td><strong>Engineering and maintenance</strong></td><td>EGPWS software and terrain database kept up to date; GNSS as position source</td></tr>
<tr><td><strong>Pilots</strong></td><td>Situational awareness at all times; thorough briefings; responsibility for terrain clearance, including on visual approaches; tell ATC when unable to maintain clearance</td></tr>
</table></div>
<h2>IATA study recommendations for operators</h2>
<ul>
  <li>Review <strong>CRM</strong>, <strong>situational awareness</strong> and <strong>SOP compliance</strong> training — with emphasis on emergency checklists in all situations.</li>
  <li>Procedures that let the <strong>pilot monitoring</strong> easily and quickly initiate a <strong>go-around</strong> when circumstances dictate.</li>
  <li>Use <strong>flight data analysis</strong> to identify CFIT precursors and feed them into training.</li>
  <li>One department owns the <strong>terrain database updates</strong>, with a formal process for EGPWS software.</li>
</ul>
"""


def extend(COURSE):
    L = COURSE["lessons"]
    old = list(L)
    old[0] = dict(old[0], title="CFIT in the World: Definition, Data and Priorities", minutes=10,
                  body=after_section(old[0]["body"], "Definition", L1_ADD),
                  objectives=["Define controlled flight into terrain (CFIT).", "State why ICAO lists CFIT as a global high-risk category.", "Describe the CFIT statistics and where CFIT accidents happen."])
    old[3] = dict(old[3], body=old[3]["body"] + L5_ADD, minutes=10)
    old[4] = dict(old[4], body=old[4]["body"] + L6_ADD, minutes=11)
    old[6] = dict(old[6], body=old[6]["body"] + L8_ADD, minutes=10)
    # split the old lesson 9: training -> prevention lesson, accidents -> case studies
    b9 = old[8]["body"]
    acc_i = b9.index("<h2>Lessons from accidents</h2>")
    con_i = b9.index("<h2>Conclusion</h2>")
    training, accidents, conclusion = b9[:acc_i], b9[acc_i:con_i], b9[con_i:]
    cases = dict(L_CASES, body=L_CASES["body"] + accidents.replace("<h2>Lessons from accidents</h2>", "<h2>Classic CFIT accidents</h2>"))
    prevent = dict(old[8], title="Preventing CFIT: Training, the IATA Plan and the Company Role", minutes=10,
                   body=training + L_PREVENT_ADD + conclusion,
                   objectives=["Describe the CFIT ground and simulator training content.", "Apply the IATA CFIT implementation plan at operator and pilot level.", "Summarise the key CFIT prevention principles."],
                   takeaways=["Ground training builds awareness; simulator training builds the escape manoeuvre.", "IATA plan: safety culture, FDM, current EGPWS databases, GNSS position, terrain display policy, immediate response.", "SOPs, terrain awareness, a PM who can call a go-around, and immediate response to warnings prevent CFIT."],
                   check=dict(q="According to the IATA CFIT plan, how should operators monitor crew responses to EGPWS events?", options=["They should not", "With flight data monitoring (FDM / FOQA)", "By asking passengers", "Only after accidents"], answer=1, explain="FDM/FOQA data show how crews respond to EGPWS events."))
    COURSE["lessons"] = [old[0], L_HOW, old[1], old[2], old[3], old[4], old[5], old[6], old[7], L_HF, cases, L_RISK, prevent]
    remap = {1: 1, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 11}
    for q in COURSE["questions"]:
        q["lesson"] = remap[q["lesson"]]
    Q = lambda lesson, q, o, a, e: dict(lesson=lesson, q=q, options=o, answer=a, explain=e)
    COURSE["questions"] += [
        Q(1, "Which ICAO plan lists CFIT as a global high-risk category?", ["Doc 4444", "Doc 10004 — Global Aviation Safety Plan", "Annex 14", "Doc 8168"], 1, "The GASP (Doc 10004) names five G-HRC, including CFIT."),
        Q(1, "What is the GASP ambition?", ["Fewer delays", "Zero fatal accidents in commercial operations by 2030 and beyond", "More airports", "Single-pilot operations"], 1, "Zero fatal accidents by 2030 and beyond."),
        Q(1, "In the IATA study 2005–2014, what share of CFIT accidents resulted in hull loss?", ["50 %", "75 %", "99 %", "20 %"], 2, "99 % hull loss, 88 % with fatalities."),
        Q(1, "Which phase accounted for nearly half of CFIT accidents (IATA 2005–2014)?", ["Take-off", "Cruise", "Approach", "Taxi"], 2, "Approach: 47.7 %."),
        Q(2, "In the typical pilot-induced CFIT scenario, the pilot:", ["Climbs above MSA", "Descends below MSA to keep visual contact in low cloud", "Follows the ILS", "Diverts early"], 1, "Descending below MSA to stay visual is the classic trap."),
        Q(2, "A CFIT precursor is:", ["A sign that a defence is weak, which should be reported", "A type of approach", "A navigation aid", "A clearance"], 0, "Precursors reveal weak defences."),
        Q(6, "What position source should the EGPWS use (IATA plan)?", ["VOR/DME only", "GPS / GNSS", "Dead reckoning", "ATC radar"], 1, "GNSS gives the look-ahead an accurate position."),
        Q(6, "IATA terrain display policy: in critical phases,", ["Nobody selects it", "At least one pilot selects the terrain display", "Only the captain in cruise", "Only on the ground"], 1, "At least one pilot; both when weather is not a threat."),
        Q(6, "Is the EGPWS a primary means of terrain avoidance?", ["Yes", "No — the crew remains responsible for terrain clearance", "Only at night", "Only on visual approaches"], 1, "It is a safety net, not a navigation tool."),
        Q(8, "In accidents with a working EGPWS, IATA found that:", ["The system failed", "The crew delayed the response or made an inadequate manoeuvre", "There was no warning", "ATC cancelled the warning"], 1, "Delayed or inadequate response."),
        Q(10, "Which two human factors models did the IATA CFIT study use?", ["SHELL and Reason", "The 'dirty dozen' and the ICAO pilot competencies", "HFACS and TEM", "FORDEC and DECIDE"], 1, "Dupont's dirty dozen and the ICAO competencies."),
        Q(10, "In TEM, being below the vertical profile near terrain is:", ["A threat", "An error", "An undesired aircraft state", "A countermeasure"], 2, "It is an undesired aircraft state."),
        Q(11, "In the 2023 Val-d'Or Dash 8 event, what started the unsafe descent?", ["Icing", "An incorrect FMS entry", "An engine failure", "A wrong runway"], 1, "An incorrect FMS entry, then an off-track steep descent."),
        Q(11, "The 2010 circling accident teaches that you should:", ["Descend early to see the runway", "Never descend below the circling minimum until on final with the runway in sight", "Circle at night only", "Use VS mode"], 1, "Respect the circling minimum."),
        Q(12, "In the FSF CFIT Checklist, which condition gives the highest weather/night multiplier?", ["Night only", "IMC only", "Night and IMC", "Day VMC"], 2, "Night and IMC together: × 5."),
        Q(12, "Which destination factor carries −30 in the FSF CFIT Checklist?", ["ILS", "NDB approach", "Complete approach lighting", "Radar with MSAW"], 1, "NDB, black-hole approaches, no radar and limited lighting carry −30."),
        Q(13, "IATA recommends procedures that let the pilot monitoring:", ["Take over the radio only", "Easily and quickly initiate a go-around", "Switch off the EGPWS", "Change the flight plan"], 1, "The PM must be able to initiate a go-around quickly."),
        Q(13, "Who should own the terrain database updates in an airline (IATA)?", ["Each pilot", "A single department with a formal process", "ATC", "Nobody"], 1, "One department, formal process."),
    ]
    COURSE["modules"] = [
        dict(title="Understanding CFIT", summary="Global data and priorities, how CFIT happens, altimetry, ATC and complacency", icon="search", lessons=range(1, 5)),
        dict(title="Prevention and EGPWS / TAWS", summary="SOPs and CDFA, the EGPWS system, basic modes, enhanced functions and crew response", icon="plane", lessons=range(5, 9)),
        dict(title="Escape, Human Factors and Risk", summary="Escape manoeuvre, human factors, case studies, the FSF risk checklist and prevention", icon="people", lessons=range(9, 14)),
    ]
    COURSE["quiz_count"] = 20
    COURSE["tagline"] = ("Controlled flight into terrain, an ICAO global high-risk category: data and scenarios, altimetry, CDFA, EGPWS modes and the escape manoeuvre, "
                         "human factors and case studies, and the interactive FSF CFIT risk checklist.")
    COURSE["purpose"] = ("Prevent CFIT in Domestic Airlines operations: ICAO GASP (Doc 10004) priorities, the IATA CFIT study and implementation plan, "
                         "the Flight Safety Foundation CFIT Checklist and the company SOPs and EGPWS procedures for each fleet.")
    COURSE["objectives"] = ["Explain why CFIT is a global high-risk category and what the data show", "Recognise CFIT scenarios, contributing factors and precursors",
                            "Apply altimeter, safe altitude, briefing and CDFA procedures", "Explain the EGPWS system, modes and enhanced functions",
                            "Respond immediately and correctly to EGPWS warnings", "Analyse CFIT accidents with human factors models", "Assess CFIT risk with the FSF checklist"]
    im = COURSE["images"]
    COURSE["images"] = {1: im[1], 2: ("gen", "Airliner descending in cloud towards hills", "Most CFIT accidents follow the same few traps."),
                        3: im[2], 4: im[3], 5: im[4], 6: im[5], 7: im[6], 8: im[7], 9: im[8],
                        10: ("gen", "Two pilots on the flight deck at night", "Situational awareness was lost in every CFIT accident analysed."),
                        11: ("gen", "Airliner approaching a coastal airport in rain", "Every CFIT lesson was learned the hard way."),
                        12: ("gen", "Approach chart and mountains at dusk", "Score the risk before the flight — then mitigate."),
                        13: im[9]}
    return COURSE
