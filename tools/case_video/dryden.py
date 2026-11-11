# Case study video: Air Ontario Flight 1363, Dryden, 10 March 1989.
# Sources: Commission of Inquiry into the Air Ontario Crash at Dryden, Ontario (Moshansky, 1992);
# FAA Lessons Learned, C-FONF. Each slide: html (rendered at 1280x720) + narration.

TITLE = "Case Study — Air Ontario Flight 1363"

SLIDES = [
dict(kind="title",
     html="""<div class="kicker">Cold Weather Operations · Closing case study</div>
<h1>Air Ontario Flight 1363</h1>
<p class="sub">Dryden, Ontario · 10 March 1989</p>""",
     say="Cold Weather Operations. Closing case study. Air Ontario Flight 1363, Dryden, Ontario, the tenth of March, 1989. "
         "This accident changed how the world thinks about winter operations. As you watch, ask yourself one question: "
         "at which point would you have stopped this chain of events?"),

dict(kind="split",
     html="""<div class="kicker">The flight</div><h2>A routine winter sector</h2>
<ul><li><b>Aircraft:</b> Fokker F28 Mk 1000, a twin jet with rear-mounted engines and <b>no leading-edge slats</b></li>
<li><b>Route:</b> Thunder Bay → Dryden → Winnipeg</li>
<li><b>On board:</b> 65 passengers and 4 crew</li>
<li><b>Experienced crew:</b> both pilots had thousands of flight hours</li></ul>""",
     art="route",
     say="The aircraft was a Fokker F 28, a twin jet with engines mounted at the rear of the fuselage. Its wing had no leading edge slats, "
         "which makes it particularly sensitive to contamination. The flight operated from Thunder Bay to Winnipeg, with an intermediate stop at Dryden. "
         "On board were sixty-five passengers and four crew members. The pilots were experienced. Nothing about this flight looked unusual."),

dict(kind="split",
     html="""<div class="kicker">Threat 1</div><h2>An unserviceable APU</h2>
<ul><li>The APU had been unserviceable for several days</li>
<li>Dryden had <b>no ground start unit</b> for the F28</li>
<li>If both engines were shut down, the aircraft could not be restarted</li>
<li>So one engine was kept running on the ground — including during <b>refuelling with passengers on board</b></li></ul>""",
     art="apu",
     say="The first threat was technical. The auxiliary power unit had been unserviceable for several days. "
         "At Dryden there was no ground start unit for the F 28. If the crew shut down both engines, they could not restart them. "
         "So one engine was kept running on the ground, even while the aircraft was being refuelled with passengers on board. "
         "Remember lesson twenty-five: an M E L item that looks harmless in summer can remove your options in winter."),

dict(kind="split",
     html="""<div class="kicker">Threat 2</div><h2>Weather and time pressure</h2>
<ul><li>The flight was already running late</li>
<li>Extra passengers and fuel were added at Dryden</li>
<li>During the stop, <b>snow began to fall</b> and became heavier</li>
<li>Snow settled on the wings while the aircraft waited</li></ul>""",
     art="snow",
     say="The second threat was weather combined with time pressure. The flight was already late when it arrived at Dryden. "
         "Extra passengers and fuel were added, and the stop took longer than planned. During the stop, snow began to fall, and it became heavier. "
         "Snow settled on the wings while the aircraft waited on the ground."),

dict(kind="split",
     html="""<div class="kicker">The decision</div><h2>No de-icing</h2>
<ul><li>De-icing with an engine running was <b>not permitted</b></li>
<li>Shutting the engine down meant the aircraft could not be restarted at Dryden</li>
<li>The aircraft was <b>not de-iced</b></li>
<li>The crew decided to depart</li></ul>""",
     art="stop",
     say="Now the threats combined into a decision. De-icing an aircraft with an engine running was not permitted. "
         "But shutting the engine down meant the aircraft could not be restarted at Dryden. The aircraft was not de-iced. "
         "The crew decided to depart. This is the moment where the Clean Aircraft Concept should have stopped the flight: "
         "no frost, ice, snow or slush on critical surfaces at take-off. There are no exceptions for a difficult day."),

dict(kind="split",
     html="""<div class="kicker">The missed warning</div><h2>Seen in the cabin — not reported</h2>
<ul><li>Passengers and a flight attendant <b>saw snow on the wings</b></li>
<li>Off-duty pilots travelling as passengers were concerned</li>
<li>The information <b>never reached the flight deck</b></li>
<li>Cabin crew were unsure whether it was their place to speak up</li></ul>""",
     art="cabin",
     say="There was a last chance. People in the cabin could see snow on the wings. A flight attendant noticed it, "
         "and off-duty pilots travelling as passengers were concerned. But the information never reached the flight deck. "
         "The cabin crew were unsure whether it was their place to question the captain about the aircraft. "
         "This is why lesson twenty-six is so clear: any crew member who sees contamination reports it, immediately and directly, to the commander."),

dict(kind="split",
     html="""<div class="kicker">The take-off</div><h2>It would not climb</h2>
<ul><li>The aircraft lifted off, but <b>failed to climb</b> and lost speed</li>
<li>It struck trees beyond the end of the runway and crashed</li>
<li><b>24 people died</b>, including both pilots and a flight attendant</li>
<li>45 people survived</li></ul>""",
     art="takeoff",
     say="The take-off roll was longer than normal. The aircraft lifted off, but it failed to climb and began to lose speed, "
         "exactly as we described in lesson five: a contaminated wing produces less lift and stalls at a lower angle of attack. "
         "It struck trees beyond the end of the runway and crashed. Twenty-four people died, including both pilots and a flight attendant. Forty-five people survived."),

dict(kind="split",
     html="""<div class="kicker">The inquiry</div><h2>Not just a pilot error</h2>
<ul><li>A Commission of Inquiry led by Justice <b>Virgil Moshansky</b> reported in 1992</li>
<li>Direct cause: take-off with <b>snow and ice contamination on the wings</b></li>
<li>But the crew were the last link in a <b>failing system</b>: company, maintenance, training and regulatory oversight</li>
<li><b>191 recommendations</b> — they reshaped de-icing rules worldwide</li></ul>""",
     art="report",
     say="A Commission of Inquiry, led by Justice Virgil Moshansky, published its final report in 1992. "
         "It found that the direct cause was the decision to take off with snow and ice contamination on the wings. "
         "But the commission went further. The crew were the last link in a failing system. Company organisation, maintenance, training, "
         "and regulatory oversight had all allowed the situation to develop. The report made one hundred and ninety-one recommendations, "
         "and it reshaped de-icing rules and safety thinking around the world."),

dict(kind="list",
     html="""<div class="kicker">What it teaches us</div><h2>The chain — and where to break it</h2>
<ol class="chain"><li><b>MEL in winter</b> — an inoperative APU removed the ability to de-ice <span>Lesson 25</span></li>
<li><b>Clean Aircraft Concept</b> — no take-off with contamination, without exception <span>Lesson 5</span></li>
<li><b>Inspection</b> — look at the wings before take-off <span>Lesson 13</span></li>
<li><b>Cabin crew reporting</b> — what the cabin sees, the flight deck must hear <span>Lesson 26</span></li>
<li><b>Pressure and decision points</b> — late, full, and snowing is exactly when to slow down <span>Lesson 27</span></li></ol>""",
     say="What does this accident teach us? It was a chain, and every link could have been broken. "
         "An inoperative A P U, accepted without thinking about winter, removed the ability to de-ice. "
         "The Clean Aircraft Concept was not applied. The wings were not checked before take-off. "
         "What the cabin could see, the flight deck never heard. "
         "And time pressure pushed the crew forward, when late, full, and snowing is exactly the moment to slow down."),

dict(kind="list",
     html="""<div class="kicker">Your turn</div><h2>What would you do?</h2>
<ol class="chain q"><li>The APU is unserviceable and your next stop has no ground start unit. Snow is forecast. <b>What do you plan before departure?</b></li>
<li>You cannot be de-iced. Snow is settling on the wings. <b>What is your decision?</b></li>
<li>You are a flight attendant and you see snow on the wing during taxi. <b>What do you do?</b></li></ol>""",
     say="Now it is your turn. First: the A P U is unserviceable, and your next stop has no ground start unit. Snow is forecast. What do you plan before departure? "
         "Second: you cannot be de-iced, and snow is settling on the wings. What is your decision? "
         "Third: you are a flight attendant, and during taxi you see snow on the wing. What do you do? "
         "Pause the video, and discuss your answers with your crew or your instructor."),

dict(kind="list",
     html="""<div class="kicker">Course review</div><h2>The essential principles</h2>
<ol class="chain two"><li>Clean aircraft — always</li><li>Holdover time is an estimate</li><li>Check — do not assume</li><li>Closed-loop communication</li>
<li>The right performance data</li><li>Protect the systems</li><li>Correct for cold</li><li>Decide early — resist pressure</li></ol>""",
     say="Let us finish with the eight principles of this course. One: a clean aircraft, always. Two: holdover time is an estimate, not a guarantee. "
         "Three: check, do not assume. Four: use closed-loop communication with the de-icing crew, A T C and the cabin. "
         "Five: use the right performance data for the runway you actually have. Six: protect the aircraft systems from the cold. "
         "Seven: correct your altimeter for cold temperatures. And eight: decide early, and resist pressure. When in doubt, return for de-icing."),

dict(kind="title",
     html="""<div class="kicker">Domestic Airlines — Training</div>
<h1>Fly safe this winter</h1>
<p class="sub">In memory of the 24 people who lost their lives at Dryden on 10 March 1989.</p>""",
     say="Thank you for completing the Cold Weather Operations course. This video is dedicated to the memory of the twenty-four people "
         "who lost their lives at Dryden on the tenth of March, 1989. Their story is the reason these rules exist. Fly safe this winter."),
]
