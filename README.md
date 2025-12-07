
# Domestic Airlines — Cold Weather Operations e‑Learning

This is a complete static site ready to deploy (Netlify, GitHub Pages, static S3 bucket).

## Structure
- `index.html` — landing/overview page with syllabus and course progress.
- `lessons/lesson01.html` … `lessons/lesson30.html` — 30 lesson pages. Each includes a picture and auto‑narration (after enabling audio).
- `quiz.html` — 20 random questions drawn from a bank of 50. Pass mark: 80%.
- `finale.html` — closing video page. Put your MP4 at `assets/finale.mp4`.
- `assets/logo.png` — logo (top & bottom). Replace with your provided logo file if needed.
- `assets/images/lessonXX.png` — generated placeholder images (replace with real images if desired).
- `assets/audio/beep.wav` — fallback audio tone in case Speech Synthesis is unavailable.
- `css/style.css`, `js/main.js`, `js/quiz.js` — styling and interactivity.

## Audio Autoplay
Browsers may block autoplay with sound. Click **Enable audio** once (top right). After that, each lesson auto‑narrates using the browser's Speech Synthesis API. If unavailable, a short tone plays as a fallback.

## Progress & Unlock
As you open lessons, they are tracked in `localStorage`. Once all 30 are visited, the **Take Quiz** button on the home page is highlighted. You can still open the quiz at any time.

## Customize
- Replace placeholder lesson images under `assets/images/`.
- Put your closing video at `assets/finale.mp4`.
- Replace or refine quiz questions in `data/questions.json`.
- Edit colors or layout in `css/style.css`.

## Deploy
Upload the folder to a static host (e.g., Netlify). Set the publish directory to the root of this project. No server required.
