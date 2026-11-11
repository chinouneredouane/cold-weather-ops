# Domestic Airlines — Training Academy

A static e-learning website for Domestic Airlines. It hosts several courses on one domain. Each course has lessons, narration, knowledge checks, a final quiz, a printable certificate and a closing video.

**First course:** Cold Weather Operations. It has 30 lessons in 6 modules, takes about 4 hours, and has a final quiz of 20 questions drawn from a bank of 57 (pass mark 80 %).

## Site structure

```
index.html                         Portal: list of all courses
assets/                            Shared by every course
  css/academy.css                  Styles
  js/course.js                     Progress tracking, narration, knowledge checks
  js/quiz.js                       Final quiz engine
  img/logo.png                     Logo
courses/
  cold-weather-operations/
    index.html                     Course home and syllabus
    lessons/lesson-01.html … 30    Lessons
    quiz.html                      Final quiz
    certificate.html               Certificate (after passing)
    finale.html                    Closing video
    data/questions.js              Question bank
    narration/lesson-XX.txt        Scripts for recording voice-over
    media/audio/                   Optional lesson-XX.mp3 narration files
    media/video/                   Optional finale.mp4
tools/
  build.py                         Generates every page from the course content
  courses/cold_weather/            Cold Weather Operations content (lessons + questions)
```

## Editing content

The lesson text and quiz questions are in `tools/courses/cold_weather/`:

- `lessons_a.py`, `lessons_b.py`, `lessons_c.py`: lessons 1–10, 11–20 and 21–30
- `questions.py`: the final quiz bank

After editing, rebuild the site (requires Python 3.8 or later, with no extra packages):

```bash
python3 tools/build.py
```

The build also validates the content. It checks that every lesson belongs to a module and that every answer index is valid.

## Adding a new course

1. Copy `tools/courses/cold_weather/` to a new folder, for example `tools/courses/upset_recovery/`, and change the `COURSE` definition (slug, title, modules, lessons, questions).
2. In `tools/build.py`, import it and add it to `COURSES`. Remove it from `UPCOMING` if it is listed there.
3. Run `python3 tools/build.py`. The course appears on the portal at `courses/<slug>/`.

## Narration and video

- **Narration:** every lesson has a recorded MP3 in `courses/<slug>/media/audio/`, generated with the open-source Kokoro neural voice by `tools/make_audio.py` (the setup steps are at the top of that file). The lesson page shows an audio player when its MP3 exists. If the MP3 is missing, the page offers a *Listen* button that uses the device's own voice instead; on iPhone that voice is silent while the phone is in Silent mode. To use a human voice-over, record from the scripts in `courses/<slug>/narration/` and replace the MP3 files. **After changing a lesson's text, regenerate its MP3:** `--lessons 5` regenerates lesson 5 only.
- **Closing video:** put `finale.mp4` in `courses/<slug>/media/video/`.

## Progress and certificates

Progress, quiz results and the learner's name are stored in the learner's own browser (`localStorage`), separately for each course. No server or account is needed. Progress does not move between devices. If you later need central records, the courses can be packaged for an LMS (SCORM).

## Publishing on your domain

The site is plain HTML, CSS and JavaScript, so it runs on any static host:

- **GitHub Pages:** go to *Settings → Pages → Deploy from a branch → main / (root)*. To use your own domain, add it under *Custom domain* and create the DNS records GitHub shows.
- **Netlify, Cloudflare Pages, or any web server:** publish the repository root. There is no build step on the server, because the generated HTML is committed.

Every link is relative, so the site also works from a sub-folder, for example `https://training.example.com/academy/`.

## Content disclaimer

This is training material based on ICAO, EASA, FAA, Transport Canada and SAE guidance. It does not replace the AFM, FCOM, QRH, MEL or the Domestic Airlines Operations Manual. A qualified instructor must review the content against company procedures and the aircraft types operated before it is used for official training.
