DOMESTIC AIRLINES — TRAINING ACADEMY
SCORM 1.2 PACKAGES FOR THE COMPANY LMS — INSTRUCTIONS FOR IT
==============================================================

CONTENTS OF THIS ZIP
  13 course packages (SCORM 1.2), one .zip per course — do NOT unzip them:

   1. Cold Weather Operations                    30 lessons   pass mark 80%    56.7 MB   cold-weather-operations-scorm12.zip
   2. Upset Prevention and Recovery              24 lessons   pass mark 80%    42.1 MB   upset-prevention-recovery-scorm12.zip
   3. RVSM Refresher                              6 lessons   pass mark 80%     7.4 MB   rvsm-refresher-scorm12.zip
   4. CFIT and EGPWS Refresher                    7 lessons   pass mark 80%     8.1 MB   cfit-egpws-refresher-scorm12.zip
   5. Hot Weather Operations                      6 lessons   pass mark 80%     6.3 MB   hot-weather-operations-scorm12.zip
   6. CPDLC — Controller-Pilot Data Link          6 lessons   pass mark 80%     6.5 MB   cpdlc-scorm12.zip
   7. Windshear and Thunderstorm Avoidance        5 lessons   pass mark 80%     5.1 MB   windshear-thunderstorm-scorm12.zip
   8. PBN Refresher                               5 lessons   pass mark 80%     4.8 MB   pbn-refresher-scorm12.zip
   9. Operations Manual and Regulations           4 lessons   pass mark 80%     4.1 MB   regulations-om-scorm12.zip
  10. MEL Refresher                               4 lessons   pass mark 80%     3.7 MB   mel-refresher-scorm12.zip
  11. Wind Limitations                            3 lessons   pass mark 80%     2.5 MB   wind-limitations-scorm12.zip
  12. Approach Operations and Minima              4 lessons   pass mark 80%     3.9 MB   approach-minima-scorm12.zip
  13. Inoperative Ground Equipment                3 lessons   pass mark 80%     2.5 MB   inop-ground-equipment-scorm12.zip

HOW TO IMPORT (each package)
  1. In the LMS, create a course or activity of type "SCORM package".
  2. Upload the course .zip as it is (the imsmanifest.xml is at the root of each zip).
  3. Recommended settings:
       - Display: new window or full screen (the course has its own navigation).
       - Grading method: highest grade / highest attempt.
       - Attempts: unlimited (pilots may retake the final quiz).
       - Mastery score: already set in each package (80 %).
  4. Enrol the pilots (groups B737-800, Q400, Q200). Pilots sign in with their
     existing LMS username and password — the packages contain no login and no
     passwords.

WHAT EACH PACKAGE REPORTS TO THE LMS (SCORM 1.2)
  cmi.core.lesson_status   incomplete while studying; passed / failed after the final quiz
  cmi.core.score.raw       best final-quiz score, 0-100 (score.min 0, score.max 100)
  cmi.core.lesson_location last lesson opened (bookmark)
  cmi.suspend_data         lessons completed and quiz result (resume where the pilot stopped)
  cmi.core.exit            "suspend" when the pilot leaves before finishing
  Reads cmi.core.student_name to print the pilot's name on the course page certificate.

CERTIFICATE
  The LMS issues the official company certificate on completion ("passed").
  Each course also has an optional printable course certificate page.

TECHNICAL NOTES
  - Pure HTML/CSS/JavaScript, no server code, no external tracking. Works offline
    inside the LMS. Audio (MP3), video (MP4) and PDF handbooks are included.
  - Tested with a SCORM 1.2 API simulator: initialise, status, score,
    bookmark and resume all reported correctly.
  - Also note: the LMS address https://talexam.tassiliairlines.com presented an HTTPS
    certificate that could not be verified from outside (self-signed, expired or
    incomplete chain). Please check the certificate so pilots do not see warnings.

UPDATES
  New or updated courses will be delivered as new packages with the same names.
  Re-upload them on the existing SCORM activity to keep the pilots' records.
