/* Domestic Airlines — Training Academy
   Final quiz: draws N random questions from window.QUESTION_BANK, shuffles the answers,
   grades the attempt and shows a full review with explanations. */
(function () {
  'use strict';

  var body = document.body;
  var COUNT = parseInt(body.getAttribute('data-quiz-count'), 10) || 20;
  var PASS = parseInt(body.getAttribute('data-pass'), 10) || 80;
  var bank = window.QUESTION_BANK || [];

  var form = document.getElementById('quizForm');
  var submit = document.getElementById('submitQuiz');
  var retry = document.getElementById('retryQuiz');
  var result = document.getElementById('quizResult');
  var counter = document.getElementById('answeredCount');
  var current = [];

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }

  function build() {
    current = shuffle(bank.slice()).slice(0, Math.min(COUNT, bank.length)).map(function (q) {
      var order = shuffle(q.options.map(function (_, i) { return i; }));
      return {
        q: q.q,
        explain: q.explain,
        lesson: q.lesson,
        options: order.map(function (i) { return q.options[i]; }),
        answer: order.indexOf(q.answer)
      };
    });

    form.innerHTML = current.map(function (q, idx) {
      var name = 'q' + idx;
      return '<div class="card quiz-q" id="card-' + idx + '"><fieldset><legend>' + (idx + 1) + '. ' + esc(q.q) + '</legend>' +
        q.options.map(function (o, oi) {
          var id = name + '_' + oi;
          return '<label for="' + id + '"><input type="radio" name="' + name + '" id="' + id + '" value="' + oi + '"><span>' + esc(o) + '</span></label>';
        }).join('') + '</fieldset></div>';
    }).join('');

    result.innerHTML = '';
    result.className = '';
    submit.style.display = '';
    retry.style.display = 'none';
    updateCount();
  }

  function updateCount() {
    var n = form.querySelectorAll('input:checked').length;
    if (counter) counter.textContent = n + ' of ' + current.length + ' answered';
  }

  function grade() {
    var missing = [];
    current.forEach(function (q, idx) {
      var chosen = form.querySelector('input[name="q' + idx + '"]:checked');
      document.getElementById('card-' + idx).classList.toggle('unanswered', !chosen);
      if (!chosen) missing.push(idx);
    });
    if (missing.length) {
      var first = document.getElementById('card-' + missing[0]);
      first.scrollIntoView({ behavior: 'smooth', block: 'center' });
      if (counter) counter.textContent = 'Please answer all questions — ' + missing.length + ' remaining';
      return;
    }

    var correct = 0;
    current.forEach(function (q, idx) {
      var card = document.getElementById('card-' + idx);
      var chosen = parseInt(form.querySelector('input[name="q' + idx + '"]:checked').value, 10);
      var ok = chosen === q.answer;
      if (ok) correct++;
      card.classList.add(ok ? 'is-correct' : 'is-wrong');
      var labels = card.querySelectorAll('label');
      labels[q.answer].classList.add('right');
      if (!ok) labels[chosen].classList.add('chosen-wrong');
      card.querySelectorAll('input').forEach(function (i) { i.disabled = true; });
      var ex = document.createElement('div');
      ex.className = 'explain';
      ex.innerHTML = '<strong>' + (ok ? 'Correct.' : 'Incorrect.') + '</strong> ' + esc(q.explain) +
        (q.lesson ? ' <a href="lessons/lesson-' + (q.lesson < 10 ? '0' : '') + q.lesson + '.html">Review lesson ' + q.lesson + '</a>' : '');
      card.appendChild(ex);
    });

    var pct = Math.round((100 * correct) / current.length);
    var passed = pct >= PASS;
    if (window.DACourse) {
      window.DACourse.saveQuiz({ pct: pct, correct: correct, total: current.length, passed: passed, date: new Date().toISOString() });
    }

    result.className = 'card result ' + (passed ? 'pass' : 'fail');
    result.innerHTML =
      '<div class="score">' + pct + '%</div>' +
      '<p class="muted">' + correct + ' of ' + current.length + ' correct · pass mark ' + PASS + '%</p>' +
      (passed
        ? '<h2>Congratulations — you passed.</h2><p>Review the explanations below, then collect your certificate.</p>' +
          '<div class="btn-row" style="justify-content:center"><a class="btn primary" href="certificate.html">Get your certificate</a><a class="btn" href="finale.html">Watch the closing video</a></div>'
        : '<h2>Not yet — keep going.</h2><p>Review the questions you missed and the linked lessons, then try a new set of questions.</p>');

    submit.style.display = 'none';
    retry.style.display = '';
    result.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  if (!form) return;
  form.addEventListener('change', updateCount);
  submit.addEventListener('click', function (e) { e.preventDefault(); grade(); });
  retry.addEventListener('click', function (e) { e.preventDefault(); build(); window.scrollTo(0, 0); });
  build();
})();
