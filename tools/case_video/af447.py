# Case study video: Air France Flight 447, South Atlantic, 1 June 2009.
# Source: BEA Final Report on the accident on 1st June 2009 to the Airbus A330-203 registered F-GZCP
# operated by Air France, flight AF 447 Rio de Janeiro – Paris (July 2012). Times are UTC.
from courses.upset_recovery.diagrams import adi

TITLE = "Case Study — Air France Flight 447"
FOOTER = "Upset Prevention and Recovery · Case study"
COURSE = "upset_recovery"


def _adi(pitch, bank, extra=""):
    return f'<svg viewBox="0 0 300 300"><g font-family="Inter,Segoe UI,Arial">{adi(pitch, bank, cx=150, cy=150, r=135, uid=f"v{pitch}{bank}")}{extra}</g></svg>'


ART = {
"ocean": """<svg viewBox="0 0 400 300"><rect width="400" height="300" fill="none"/>
<path d="M150 230 Q160 130 220 110 Q215 50 270 45 Q300 10 340 40 Q390 50 380 120 Q400 170 385 230z" fill="#5b6876"/>
<path d="M120 50 Q260 20 400 50 Q330 62 260 60 Q190 62 120 50z" fill="#6f7c8a"/>
<path d="M285 150 l-18 40 l15 -4 l-20 46 l40 -55 l-16 4 l17 -31z" fill="#ffe680"/>
<rect x="0" y="230" width="400" height="70" fill="#0e2a44"/>
<g fill="#fff"><circle cx="40" cy="40" r="2"/><circle cx="90" cy="90" r="1.6"/><circle cx="60" cy="150" r="1.4"/><circle cx="110" cy="30" r="1.8"/></g>
<path d="M30 150 l40 -4 l10 -10 l6 2 l-4 10 l30 -2 l4 4 l-30 4 l-4 12 l-6 0 l-2 -10 l-40 4z" fill="#fff"/></svg>""",
"pitot": """<svg viewBox="0 0 300 300"><circle cx="150" cy="150" r="130" fill="#ffffff" opacity=".12"/>
<rect x="40" y="135" width="170" height="30" rx="10" fill="#cfd8dc"/><path d="M210 135 L268 143 L268 157 L210 165z" fill="#cfd8dc"/>
<circle cx="268" cy="150" r="6" fill="#2b3a44"/>
<g stroke="#bfe6ff" stroke-width="7" stroke-linecap="round"><path d="M230 90 l10 18"/><path d="M262 80 l0 22"/><path d="M290 96 l-10 16"/><path d="M286 210 l-10 -16"/><path d="M250 222 l2 -20"/></g>
<path d="M266 138 q20 12 0 24" stroke="#e6f6ff" stroke-width="10" fill="none"/>
<text x="150" y="270" text-anchor="middle" font-family="Inter,Segoe UI,Arial" font-size="22" font-weight="800" fill="#fff">ice crystals</text></svg>""",
"climb": _adi(12, -10),
"stall": _adi(15, 25, '<rect x="70" y="232" width="160" height="40" rx="8" fill="#111" opacity=".85"/><text x="150" y="259" text-anchor="middle" font-size="20" font-weight="800" fill="#ff5050">V/S −10,000</text>'),
"report": """<svg viewBox="0 0 300 300"><rect x="70" y="30" width="160" height="230" rx="10" fill="#fff"/>
<g stroke="#9fb5a8" stroke-width="8" stroke-linecap="round"><path d="M100 80h100M100 110h100M100 140h80M100 170h100M100 200h60"/></g>
<circle cx="205" cy="225" r="34" fill="#c8102e"/><text x="205" y="234" font-family="Inter,Segoe UI,Arial" font-size="26" font-weight="800" fill="#fff" text-anchor="middle">41</text></svg>""",
}

SLIDES = [
dict(kind="title",
     html="""<div class="kicker">Upset Prevention and Recovery · Closing case study</div>
<h1>Air France Flight 447</h1>
<p class="sub">Rio de Janeiro – Paris · South Atlantic · 1 June 2009</p>""",
     say="Upset Prevention and Recovery. Closing case study. Air France Flight 447, from Rio de Janeiro to Paris, on the first of June, 2009. "
         "This accident is one of the main reasons why upset prevention and recovery training exists today. "
         "Everything in this video comes from the final report of the French investigation authority, the B E A. "
         "As you watch, ask yourself: at which moment could this crew have stopped the chain?"),

dict(kind="split",
     html="""<div class="kicker">The flight</div><h2>A night crossing of the tropics</h2>
<ul><li><b>Airbus A330-200</b>, 216 passengers, 9 cabin crew, 3 pilots — a captain and two co-pilots</li>
<li>Cruise at <b>FL350</b>, at night, over the Atlantic</li>
<li>Crossing the inter-tropical convergence zone, with <b>powerful cumulonimbus clusters</b></li>
<li>At about 02:02 the captain left the flight deck for his rest, <b>without specific instructions</b> for crossing the weather</li></ul>""",
     art="ocean",
     say="The aircraft was an Airbus A 330, 200, with two hundred and sixteen passengers, nine cabin crew, and three pilots: a captain and two co-pilots. "
         "It was cruising at flight level 350, at night, over the Atlantic Ocean, crossing the inter-tropical convergence zone, where there were powerful clusters of cumulonimbus. "
         "At about two minutes past two, the captain left the flight deck for his rest. He did not leave specific instructions for crossing the weather ahead. "
         "A few minutes later, the crew turned twelve degrees to the left to avoid returns on the weather radar."),

dict(kind="split",
     html="""<div class="kicker">The trigger · 02:10:05</div><h2>Unreliable airspeed</h2>
<ul><li>The pitot probes were <b>obstructed by ice crystals</b></li>
<li>The measured airspeeds became inconsistent</li>
<li>The <b>autopilot and autothrust disconnected</b>, and the flight controls reverted to <b>alternate law</b> — with no angle of attack protection</li>
<li>The left speed display was wrong for only <b>29 seconds</b></li></ul>""",
     art="pitot",
     say="At ten minutes and five seconds past two, the pitot probes were obstructed by ice crystals, and the measured airspeeds became inconsistent. "
         "The autopilot, and then the autothrust, disconnected. The flight control law reverted to alternate law, in which there is no angle of attack protection. "
         "This was a known failure, with a procedure: unreliable airspeed. Hold the pitch attitude and the thrust, and the aircraft stays safe. "
         "In fact, the speed displayed on the left side was incorrect for only twenty-nine seconds."),

dict(kind="split",
     html="""<div class="kicker">The reaction</div><h2>Surprise — and a sharp nose-up input</h2>
<ul><li>The autopilot disconnection <b>surprised</b> the two co-pilots</li>
<li>The pilot flying made <b>excessive roll inputs</b> and a <b>sharp nose-up input</b></li>
<li>The aircraft began to climb and lose speed</li>
<li>The loss of speed was called out — but <b>no one called the “Unreliable IAS” procedure</b></li></ul>""",
     art="climb",
     say="The autopilot disconnection surprised the two co-pilots. In turbulence, at high altitude, the pilot flying made excessive roll inputs, and a sharp nose-up input. "
         "The aircraft began to climb, and to lose speed. The co-pilots identified and called out the loss of the airspeed indications. "
         "But neither of them called the unreliable airspeed procedure. "
         "Remember lesson seven: at high altitude, damping is low and small inputs have large effects. And lesson eighteen: pitch and power first."),

dict(kind="split",
     html="""<div class="kicker">02:10:51</div><h2>The approach to stall</h2>
<ul><li>The stall warning sounded <b>continuously for 54 seconds</b></li>
<li>The pilot flying selected <b>TO/GA thrust</b> and continued <b>nose-up inputs</b></li>
<li>The stabiliser trim moved from <b>3° to 13° nose-up</b> — and stayed there</li>
<li>The aircraft reached about <b>38,000 ft</b>. All three airspeeds were valid again — and <b>no one mentioned the stall warning</b></li></ul>""",
     art="climb",
     say="At ten minutes and fifty-one seconds past two, the stall warning triggered, and sounded continuously for fifty-four seconds. "
         "The pilot flying selected take-off and go-around thrust, and continued to make nose-up inputs. "
         "The trimmable horizontal stabiliser moved from three degrees to thirteen degrees nose-up, and stayed there until the end of the flight. "
         "The aircraft climbed to about thirty-eight thousand feet. By then, all three airspeed indications were valid and consistent again. "
         "Neither pilot made any reference to the stall warning, or to the buffet."),

dict(kind="split",
     html="""<div class="kicker">02:11:42</div><h2>A sustained stall</h2>
<ul><li>The captain returned to the flight deck, about 1 min 30 s after the disconnect</li>
<li>Angle of attack <b>above 40°</b>, vertical speed about <b>−10,000 ft/min</b>, pitch about 15° nose-up, thrust near maximum</li>
<li>Below 60 kt measured speed, angle of attack data was invalid, so <b>the stall warning stopped</b> — and returned when the nose was lowered</li>
<li>Control priority was taken <b>without callouts</b></li></ul>""",
     art="stall",
     say="At eleven minutes and forty-two seconds past two, the captain re-entered the flight deck, about one and a half minutes after the autopilot disconnected. "
         "The aircraft was now in a sustained stall. The angle of attack exceeded forty degrees. The vertical speed was about minus ten thousand feet per minute, "
         "while the pitch attitude was about fifteen degrees nose-up, and the engines were near maximum thrust. "
         "Here is a trap. By design, when the measured speed fell below sixty knots, the angle of attack values were invalidated, and the stall warning stopped. "
         "When the pilot later pushed the nose down, the angle of attack decreased, the speeds became valid, and the stall warning sounded again. "
         "The correct action produced the warning. And the two co-pilots took control priority from each other without any callout."),

dict(kind="split",
     html="""<div class="kicker">02:14:28</div><h2>Impact with the ocean</h2>
<ul><li>The stall lasted until the aircraft struck the sea</li>
<li>Last recorded values: pitch <b>16° nose-up</b>, vertical speed <b>−10,912 ft/min</b></li>
<li><b>All 228 people on board died</b></li>
<li>The flight recorders were recovered from the ocean floor <b>23 months later</b></li></ul>""",
     art="ocean",
     say="The stall lasted until the impact with the sea, at fourteen minutes and twenty-eight seconds past two. "
         "The last recorded values were a pitch attitude of sixteen degrees nose-up, and a vertical speed of nearly eleven thousand feet per minute down. "
         "All two hundred and twenty-eight people on board died. "
         "The flight recorders were found on the ocean floor twenty-three months later."),

dict(kind="split",
     html="""<div class="kicker">The investigation · BEA, July 2012</div><h2>A chain of events</h2>
<ul><li>Airspeed inconsistency from <b>iced pitot probes</b> → autopilot disconnect, alternate law</li>
<li><b>Inappropriate control inputs</b> that destabilised the flight path</li>
<li>No link made between the speed loss and the <b>procedure</b>; stall warning <b>not identified</b></li>
<li>Factors: <b>startle</b>, no high-altitude manual handling training, weakened task-sharing</li>
<li><b>41 safety recommendations</b> — on training, simulators, ergonomics and oversight</li></ul>""",
     art="report",
     say="The B E A published its final report in July 2012. It described a succession of events. "
         "A temporary airspeed inconsistency from iced pitot probes, which disconnected the autopilot and reverted the flight controls to alternate law. "
         "Inappropriate control inputs that destabilised the flight path. No link made between the loss of speed indications and the procedure. "
         "And a stall that was never identified, so no recovery inputs were made. "
         "Contributing factors included the startle effect, the absence of training in manual handling at high altitude, and task-sharing weakened by surprise. "
         "The B E A made forty-one safety recommendations, on pilot training, simulators, cockpit ergonomics and oversight."),

dict(kind="list",
     html="""<div class="kicker">What it teaches us</div><h2>The chain — and where to break it</h2>
<ol class="chain"><li><b>Unreliable airspeed</b> — pitch and power first, avoid large inputs <span>Lesson 18</span></li>
<li><b>High altitude</b> — small, smooth inputs; you cannot climb out of a stall <span>Lesson 7</span></li>
<li><b>Stall warning = stall</b> — reduce angle of attack, trim nose-down if needed <span>Lesson 20</span></li>
<li><b>Startle</b> — attitude first, breathe, then act on a plan <span>Lesson 14</span></li>
<li><b>CRM</b> — clear callouts, one pilot flying, no silent priority takeovers <span>Lesson 15</span></li></ol>""",
     say="What does this accident teach us? With unreliable airspeed, set the pitch and the power, and avoid large inputs. "
         "At high altitude, make small, smooth inputs, and remember that you cannot climb out of a stall. "
         "Treat the stall warning as a stall: reduce the angle of attack, and use nose-down trim if needed. "
         "Manage the startle effect: look at the attitude first, breathe, and then act on a plan. "
         "And use clear callouts, with only one pilot flying, and no silent takeovers of control."),

dict(kind="list",
     html="""<div class="kicker">Your turn</div><h2>What would you do?</h2>
<ol class="chain q"><li>At FL350 the autopilot disconnects and the airspeeds disagree. <b>What are your first three actions?</b></li>
<li>The stall warning sounds and the aircraft is climbing with decreasing speed. <b>What is your priority?</b></li>
<li>You are the pilot monitoring and the pilot flying keeps pulling back. <b>What do you say and do?</b></li></ol>""",
     say="Now it is your turn. First: at flight level 350, the autopilot disconnects and the airspeeds disagree. What are your first three actions? "
         "Second: the stall warning sounds, and the aircraft is climbing with decreasing speed. What is your priority? "
         "Third: you are the pilot monitoring, and the pilot flying keeps pulling back. What do you say, and what do you do? "
         "Pause the video, and discuss your answers with your crew or your instructor."),

dict(kind="list",
     html="""<div class="kicker">Course review</div><h2>The essential principles</h2>
<ol class="chain two"><li>Prevention first</li><li>Know the angle of attack</li><li>Respect the margins</li><li>Understand the automation</li>
<li>Manage startle</li><li>Communicate</li><li>Stall recovery first</li><li>The right recovery technique</li></ol>""",
     say="Let us finish with the eight principles of this course. One: prevention first. Two: know your angle of attack — the wing stalls at any speed and any attitude. "
         "Three: respect the margins of speed, buffet and g. Four: understand the automation, and expect it to hand you a problem when it disconnects. "
         "Five: manage startle. Six: communicate, with callouts and a clear transfer of control. "
         "Seven: stall recovery first — reduce the angle of attack and accept the altitude loss. "
         "And eight: use the right recovery technique for a nose-high or a nose-low upset."),

dict(kind="title",
     html="""<div class="kicker">Domestic Airlines — Training</div>
<h1>Fly the aircraft</h1>
<p class="sub">In memory of the 228 people on board Air France Flight 447, 1 June 2009.</p>""",
     say="Thank you for completing the Upset Prevention and Recovery course. "
         "This video is dedicated to the memory of the two hundred and twenty-eight people on board Air France Flight 447. "
         "Their story changed how pilots are trained around the world. Whatever happens: fly the aircraft."),
]
