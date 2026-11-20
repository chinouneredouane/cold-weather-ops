/* Domestic Airlines — slide player for lessons + "All courses" drawer on every page.
   Works with course.js (progress, SCORM, narration, knowledge checks), which must load first. */
(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var veil;
  function closeAll() {
    document.querySelectorAll('.pl-drawer').forEach(function (d) { d.classList.remove('open'); });
    if (veil) veil.classList.remove('on');
  }
  function openDrawer(id) { var d = $(id); if (!d) return; d.classList.add('open'); veil.classList.add('on'); var b = d.querySelector('button'); if (b) b.focus(); }

  function setupDrawers() {
    // Inside the company LMS each SCORM package holds one course only: hide links to the other courses.
    if (window.DALMS) {
      var t = $('allBtn'); if (t) t.style.display = 'none';
      document.querySelectorAll('.pl-ctrl a[aria-label="Close"]').forEach(function (a) { a.setAttribute('href', '../index.html'); a.title = 'Close — course home'; });
    }
    veil = $('plVeil');
    if (!veil) return;
    veil.addEventListener('click', closeAll);
    document.querySelectorAll('[data-pl-close]').forEach(function (b) { b.addEventListener('click', closeAll); });
    var all = $('allBtn');
    if (all) all.addEventListener('click', function () { openDrawer('plAll'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });
  }

  var ICON_PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';
  var ICON_PAUSE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3v14H7zm7 0h3v14h-3z"/></svg>';

  function setupPlayer() {
    var root = document.querySelector('.player');
    if (!root) return;
    var slides = Array.prototype.slice.call(root.querySelectorAll('.pl-slide'));
    var panel = $('plPanel'), i = 0, total = slides.length;
    var prevHref = root.getAttribute('data-prev'), nextHref = root.getAttribute('data-next');
    var audio = document.querySelector('.audio-block audio');
    var tts = document.querySelector('[data-tts]'), ttsStop = document.querySelector('[data-tts-stop]');
    var playing = false, muted = false;

    // menu of slides
    var list = $('plSlides');
    if (list) {
      list.innerHTML = slides.map(function (s, k) { return '<div class="pl-item" data-k="' + k + '">' + (k + 1) + '. ' + s.getAttribute('data-title') + '</div>'; }).join('');
      list.addEventListener('click', function (e) { var k = e.target.getAttribute('data-k'); if (k !== null) { show(+k); closeAll(); } });
    }

    function crumbs() {
      var c = $('plCrumbs'); if (!c) return;
      var t = function (k) { return slides[k] ? slides[k].getAttribute('data-title') : null; };
      var parts = [];
      if (t(i - 1)) parts.push('<span>' + t(i - 1) + '</span>');
      parts.push('<strong>' + t(i) + '</strong>');
      if (t(i + 1)) parts.push('<span>' + t(i + 1) + '</span>');
      c.innerHTML = parts.join('<i>|</i>');
    }

    function show(k) {
      i = Math.max(0, Math.min(total - 1, k));
      slides.forEach(function (s, n) { s.classList.toggle('on', n === i); });
      panel.classList.toggle('tall', !!slides[i].querySelector('figure, .table-wrap, table, .kc, .dtcalc'));
      panel.scrollTop = 0;
      $('plCount').textContent = (i + 1) + '/' + total;
      $('plProg').style.width = ((i + 1) / total * 100) + '%';
      document.querySelectorAll('#plSlides .pl-item').forEach(function (e, n) { e.classList.toggle('cur', n === i); });
      crumbs();
      try { history.replaceState(null, '', '#s' + (i + 1)); } catch (e) { /* ignore */ }
    }

    function go(d) {
      var k = i + d;
      if (k >= total) { var nx = document.getElementById('nextLesson'); if (nx) nx.click(); return; }
      if (k < 0) { if (prevHref) location.href = prevHref; return; }
      show(k);
    }

    function setPlay(on) {
      playing = on;
      var b = $('plPlay'); b.classList.toggle('on', on); b.innerHTML = on ? ICON_PAUSE : ICON_PLAY;
      b.setAttribute('aria-label', on ? 'Pause narration' : 'Play narration');
    }
    function hasMp3() { return audio && audio.style.display !== 'none'; }
    $('plPlay').addEventListener('click', function () {
      if (hasMp3()) {
        if (audio.paused) { audio.muted = muted; audio.play(); setPlay(true); } else { audio.pause(); setPlay(false); }
      } else if (tts && tts.style.display !== 'none') {
        if (!playing) { tts.click(); setPlay(true); } else { if (ttsStop) ttsStop.click(); setPlay(false); }
      }
    });
    if (audio) audio.addEventListener('ended', function () { setPlay(false); });
    $('plMute').addEventListener('click', function () {
      muted = !muted; this.classList.toggle('on', muted);
      if (audio) audio.muted = muted;
      if (muted && !hasMp3() && playing && ttsStop) { ttsStop.click(); setPlay(false); }
    });
    $('plReplay').addEventListener('click', function () {
      show(0);
      if (hasMp3()) { audio.currentTime = 0; if (playing) audio.play(); }
    });
    $('plPrev').addEventListener('click', function () { go(-1); });
    $('plNext').addEventListener('click', function () { go(1); });
    $('plMenu').addEventListener('click', function () { openDrawer('plMenuDrawer'); });
    document.addEventListener('keydown', function (e) {
      if (e.target && /INPUT|SELECT|TEXTAREA/.test(e.target.tagName)) return;
      if (e.key === 'ArrowRight' || e.key === 'PageDown') go(1);
      if (e.key === 'ArrowLeft' || e.key === 'PageUp') go(-1);
    });
    // swipe on touch screens
    var x0 = null;
    panel.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    panel.addEventListener('touchend', function (e) {
      if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 70) go(dx < 0 ? 1 : -1);
    });
    var m = /#s(\d+)/.exec(location.hash);
    show(m ? (+m[1] - 1) : 0);
  }

  document.addEventListener('DOMContentLoaded', function () { setupDrawers(); setupPlayer(); });
})();
