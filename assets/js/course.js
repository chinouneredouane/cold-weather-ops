/* Domestic Airlines — Training Academy
   Course runtime: progress tracking, lesson completion, narration and knowledge checks.
   Progress is stored in the learner's own browser (localStorage), per course. */
(function () {
  'use strict';

  var body = document.body;
  var courseId = body.getAttribute('data-course');
  var total = parseInt(body.getAttribute('data-total'), 10) || 0;
  var lessonNum = parseInt(body.getAttribute('data-lesson'), 10) || 0;

  /* ---------- Storage (never throws) ---------- */
  var KEY = 'da-academy:' + courseId;
  function load() {
    try {
      var raw = window.localStorage.getItem(KEY);
      var data = raw ? JSON.parse(raw) : null;
      if (data && typeof data === 'object') {
        data.completed = Array.isArray(data.completed) ? data.completed : [];
        return data;
      }
    } catch (e) { /* storage unavailable */ }
    return { completed: [], quiz: null, name: '' };
  }
  function save(data) {
    try { window.localStorage.setItem(KEY, JSON.stringify(data)); } catch (e) { /* ignore */ }
  }
  var state = load();

  function isDone(n) { return state.completed.indexOf(n) !== -1; }
  function markDone(n) {
    if (!n || isDone(n)) return;
    state.completed.push(n);
    state.completed.sort(function (a, b) { return a - b; });
    state.last = n;
    save(state);
    render();
  }

  /* Expose a tiny API for quiz.js / certificate page */
  window.DACourse = {
    id: courseId,
    total: total,
    state: function () { return state; },
    saveQuiz: function (result) {
      // Keep the best attempt; a pass always beats a fail
      var prev = state.quiz;
      var attempts = (prev && prev.attempts ? prev.attempts : 0) + 1;
      var better = !prev || (result.passed && !prev.passed) ||
        (result.passed === !!prev.passed && result.pct >= prev.pct);
      if (better) state.quiz = result;
      state.quiz.attempts = attempts;
      save(state);
    },
    saveName: function (name) { state.name = name; save(state); }
  };

  /* ---------- Render progress everywhere ---------- */
  function render() {
    var done = state.completed.filter(function (n) { return n >= 1 && n <= total; }).length;
    var pct = total ? Math.round((done / total) * 100) : 0;

    var bar = document.getElementById('progressBar');
    if (bar) bar.style.width = pct + '%';

    document.querySelectorAll('[data-lesson-link]').forEach(function (el) {
      var n = parseInt(el.getAttribute('data-lesson-link'), 10);
      el.classList.toggle('is-done', isDone(n));
    });

    document.querySelectorAll('[data-module-progress]').forEach(function (el) {
      var list = el.getAttribute('data-module-progress').split(',').map(Number);
      var c = list.filter(isDone).length;
      el.textContent = c + ' / ' + list.length;
    });

    document.querySelectorAll('[data-progress-text]').forEach(function (el) {
      el.textContent = done + ' of ' + total + ' lessons completed';
    });
    document.querySelectorAll('[data-progress-pct]').forEach(function (el) {
      el.textContent = pct + '%';
    });
    var ring = document.getElementById('progressRing');
    if (ring) {
      var c = 2 * Math.PI * 26;
      ring.setAttribute('stroke-dasharray', c.toFixed(1));
      ring.setAttribute('stroke-dashoffset', (c * (1 - pct / 100)).toFixed(1));
    }

    var resume = document.getElementById('resumeBtn');
    if (resume) {
      var next = 1;
      for (var i = 1; i <= total; i++) { if (!isDone(i)) { next = i; break; } if (i === total) next = 0; }
      if (next === 0) {
        resume.textContent = 'Take the Final Quiz';
        resume.setAttribute('href', 'quiz.html');
      } else if (done > 0) {
        resume.textContent = 'Resume — Lesson ' + next;
        resume.setAttribute('href', 'lessons/lesson-' + (next < 10 ? '0' : '') + next + '.html');
      }
    }

    var quizNote = document.getElementById('quizGate');
    if (quizNote) {
      if (done >= total) {
        quizNote.textContent = 'All lessons completed — you are ready for the final quiz.';
        quizNote.className = 'callout';
      } else {
        quizNote.innerHTML = '<span class="label">Recommendation</span>You have completed ' + done + ' of ' + total +
          ' lessons. Complete all lessons before attempting the quiz. You may still start the quiz now.';
        quizNote.className = 'callout caution';
      }
    }

    var qs = document.getElementById('quizStatus');
    if (qs) {
      if (state.quiz && state.quiz.passed) {
        qs.innerHTML = 'Quiz passed with <b>' + state.quiz.pct + '%</b>. <a href="certificate.html">View your certificate</a>.';
      } else if (state.quiz) {
        qs.innerHTML = 'Last quiz attempt: <b>' + state.quiz.pct + '%</b> (pass mark 80%).';
      } else {
        qs.textContent = 'Quiz not attempted yet.';
      }
    }
  }

  /* ---------- Lesson completion ---------- */
  function setupLesson() {
    if (!lessonNum) return;
    // Completion is recorded when the learner reaches the end of the lesson
    var end = document.querySelector('.lesson-end');
    if (end && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { markDone(lessonNum); io.disconnect(); } });
      });
      io.observe(end);
    }
    // ...or when they move on with the Next button
    var next = document.getElementById('nextLesson');
    if (next) next.addEventListener('click', function () { markDone(lessonNum); });
  }

  /* ---------- Sidebar toggle (mobile) ---------- */
  function setupSidebar() {
    var btn = document.querySelector('.sidebar-toggle');
    var side = document.querySelector('.sidebar');
    if (!btn || !side) return;
    btn.addEventListener('click', function () {
      var open = side.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? 'Hide course contents' : 'Show course contents';
    });
  }

  /* ---------- Narration: recorded MP3 if present, otherwise text-to-speech ---------- */
  function setupAudio() {
    var block = document.querySelector('.audio-block');
    if (!block) return;
    var audio = block.querySelector('audio');
    var status = block.querySelector('.audio-status');
    var ttsBtn = block.querySelector('[data-tts]');
    var stopBtn = block.querySelector('[data-tts-stop]');
    var synth = window.speechSynthesis;

    function useTTS() {
      if (audio) audio.style.display = 'none';
      if (!synth || typeof SpeechSynthesisUtterance === 'undefined') {
        if (status) status.textContent = 'Narration is not available in this browser.';
        if (ttsBtn) ttsBtn.style.display = 'none';
        return;
      }
      if (ttsBtn) ttsBtn.style.display = '';
      if (status) status.textContent = 'Narration uses your browser voice. Press “Listen” to hear this lesson.';
    }

    if (audio) {
      var settled = false;
      audio.addEventListener('loadedmetadata', function () {
        settled = true;
        audio.style.display = '';
        if (ttsBtn) ttsBtn.style.display = 'none';
        if (stopBtn) stopBtn.style.display = 'none';
        if (status) status.textContent = 'Recorded narration for this lesson.';
      });
      audio.addEventListener('error', function () { settled = true; useTTS(); }, true);
      var src = audio.querySelector('source');
      if (src) src.addEventListener('error', function () { settled = true; useTTS(); });
      setTimeout(function () { if (!settled && audio.readyState === 0) useTTS(); }, 2500);
    } else {
      useTTS();
    }

    function pickVoice() {
      var voices = synth.getVoices() || [];
      var en = voices.filter(function (v) { return /^en(-|_|$)/i.test(v.lang); });
      var pref = en.filter(function (v) { return /GB|US/i.test(v.lang) && /natural|google|microsoft|samantha|daniel/i.test(v.name); });
      return pref[0] || en[0] || null;
    }
    function narrationText() {
      var parts = [];
      var h = document.querySelector('.lesson-head h1');
      if (h) parts.push(h.textContent);
      document.querySelectorAll('.lesson-body [data-narrate]').forEach(function (el) {
        var clone = el.cloneNode(true);
        clone.querySelectorAll('[data-skip-narration], figure, .table-wrap, .kc').forEach(function (x) { x.remove(); });
        parts.push(clone.textContent.replace(/\s+/g, ' ').trim());
      });
      return parts.join('. ');
    }
    function chunk(text) {
      // Long utterances get cut off in some browsers; speak sentence groups
      var sentences = text.match(/[^.!?]+[.!?]*/g) || [text];
      var out = [], cur = '';
      sentences.forEach(function (s) {
        if ((cur + s).length > 220) { if (cur) out.push(cur); cur = s; } else { cur += s; }
      });
      if (cur) out.push(cur);
      return out;
    }

    if (ttsBtn) ttsBtn.addEventListener('click', function () {
      if (synth.speaking && synth.paused) { synth.resume(); ttsBtn.textContent = 'Pause'; return; }
      if (synth.speaking) { synth.pause(); ttsBtn.textContent = 'Resume'; return; }
      var voice = pickVoice();
      var pieces = chunk(narrationText());
      pieces.forEach(function (p, i) {
        var u = new SpeechSynthesisUtterance(p);
        if (voice) u.voice = voice;
        u.lang = voice ? voice.lang : 'en-GB';
        u.rate = 0.98;
        if (i === pieces.length - 1) u.onend = function () { ttsBtn.textContent = 'Listen'; if (stopBtn) stopBtn.style.display = 'none'; };
        synth.speak(u);
      });
      ttsBtn.textContent = 'Pause';
      if (stopBtn) stopBtn.style.display = '';
    });
    if (stopBtn) stopBtn.addEventListener('click', function () {
      synth.cancel();
      if (ttsBtn) ttsBtn.textContent = 'Listen';
      stopBtn.style.display = 'none';
    });
    window.addEventListener('pagehide', function () { if (synth) synth.cancel(); });
  }

  /* ---------- Knowledge checks ---------- */
  function setupChecks() {
    document.querySelectorAll('.kc').forEach(function (kc) {
      var answer = parseInt(kc.getAttribute('data-answer'), 10);
      var fb = kc.querySelector('.fb');
      var buttons = kc.querySelectorAll('button.opt');
      buttons.forEach(function (b, i) {
        b.addEventListener('click', function () {
          buttons.forEach(function (x) { x.classList.remove('correct', 'wrong'); x.setAttribute('aria-pressed', 'false'); });
          b.setAttribute('aria-pressed', 'true');
          if (i === answer) {
            b.classList.add('correct');
            fb.innerHTML = '<strong>Correct.</strong> ' + kc.getAttribute('data-explain');
          } else {
            b.classList.add('wrong');
            fb.innerHTML = '<strong>Not quite.</strong> Review the lesson and try again.';
          }
        });
      });
    });
  }

  render();
  document.addEventListener('DOMContentLoaded', function () {
    render();
    setupLesson();
    setupSidebar();
    setupAudio();
    setupChecks();
  });
})();
