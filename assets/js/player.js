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
    var prevHref = root.getAttribute('data-prev');
    var audio = document.querySelector('.audio-block audio');
    var cues = []; try { cues = JSON.parse(root.getAttribute('data-cues') || '[]'); } catch (e) { cues = []; }
    var synth = window.speechSynthesis || null;
    var playing = false, muted = false;
    // ---- interactive cards: each card has its own clip, played only when the learner taps it
    var clipsOn = root.getAttribute('data-clips') === '1', clipBase = root.getAttribute('data-clipbase') || '';
    var cardAudio = new Audio(); cardAudio.preload = 'none';
    function stopCard() { try { cardAudio.pause(); } catch (e) { /* ignore */ } if (synth && !hasMp3()) synth.cancel(); }
    function cardText(el) {
      var c = el.cloneNode(true);
      c.querySelectorAll('.tem-btns, .tem-score').forEach(function (x) { x.remove(); });
      return (c.textContent || '').replace(/\s+/g, ' ').trim();
    }
    function playCard(el) {
      stopCard();
      if (hasMp3() && !audio.paused) audio.pause();             // the card takes over from the slide narration
      if (synth) synth.cancel();
      if (muted || !el) return;
      var no = el.getAttribute('data-clip');
      if (clipsOn && no) { cardAudio.src = clipBase + no + '.mp3'; cardAudio.currentTime = 0; cardAudio.play().catch(function () {}); }
      else if (synth) { var u = new SpeechSynthesisUtterance(cardText(el)); u.lang = 'en-GB'; synth.speak(u); }
    }
    document.addEventListener('pl:card', function (e) { playCard(e.detail); });
    document.addEventListener('pl:cardstop', function () { stopCard(); });
    function hasCards(k) { return !!(slides[k] && slides[k].querySelector('.flipcard, .tem-item')); }

    function hasMp3() { return !!audio && audio.style.display !== 'none'; }
    function synced() { return hasMp3() && cues.length === total; }
    function cue(k) { return k >= 0 && k < cues.length ? cues[k] : null; }

    // ---- slide menu
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

    // ---- narration that follows the slide
    function seek(t) {
      if (!audio) return;
      if (audio.readyState > 0) { try { audio.currentTime = t; } catch (e) { /* ignore */ } }
      else { var f = function () { try { audio.currentTime = t; } catch (e) { /* ignore */ } audio.removeEventListener('loadedmetadata', f); }; audio.addEventListener('loadedmetadata', f); }
    }
    function slideText(k) {
      var c = slides[k].cloneNode(true);
      c.querySelectorAll('figure, .table-wrap, table, .kc, .next-up, script, style, .dtcalc, .flipcards, .tem-sort, .flip-hint').forEach(function (x) { x.remove(); });
      return (c.textContent || '').replace(/\s+/g, ' ').trim();
    }
    function speak(k) {
      if (!synth) return;
      synth.cancel();
      var text = slideText(k);
      if (!text || muted) return;
      var u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-GB'; u.rate = 1;
      u.onend = function () { if (playing && i === k && !hasCards(k)) { if (k < total - 1) show(k + 1); else setPlay(false); } };
      synth.speak(u);
    }
    function follow() {                       // called after the learner changes slide
      if (!playing) return;
      if (hasMp3()) {
        if (!synced()) return;                // no cues: keep the lesson narration running
        var t = cue(i);
        if (t === null) { audio.pause(); setPlay(false); return; }   // knowledge check: no narration
        seek(t); audio.play();
      } else { speak(i); }
    }

    function show(k, fromAudio) {
      i = Math.max(0, Math.min(total - 1, k));
      stopCard();
      slides.forEach(function (s, n) { s.classList.toggle('on', n === i); });
      var figmode = slides[i].classList.contains('has-fig');
      var tall = !figmode && !!slides[i].querySelector('figure, .table-wrap, table, .kc, .dtcalc');
      panel.classList.toggle('tall', tall);
      panel.classList.toggle('figmode', figmode);
      if (panel.parentNode) { panel.parentNode.classList.toggle('wide', tall); panel.parentNode.classList.toggle('figmode', figmode); }
      fit();
      panel.scrollTop = 0;
      $('plCount').textContent = (i + 1) + '/' + total;
      $('plProg').style.width = ((i + 1) / total * 100) + '%';
      document.querySelectorAll('#plSlides .pl-item').forEach(function (e, n) { e.classList.toggle('cur', n === i); });
      crumbs();
      try { history.replaceState(null, '', '#s' + (i + 1)); } catch (e) { /* ignore */ }
      if (!fromAudio) follow();
    }

    // shrink the text (never the picture) until the slide fits the screen without scrolling
    function fit() {
      var sl = slides[i]; if (!sl) return;
      var box = sl.classList.contains('has-fig') ? sl.querySelector('.fig-text') : panel;
      var size = 17; sl.style.fontSize = size + 'px';
      var guard = 0;
      while (box.scrollHeight > box.clientHeight + 2 && size > 12.5 && guard++ < 20) { size -= 0.5; sl.style.fontSize = size + 'px'; }
    }
    window.addEventListener('resize', function () { fit(); });
    document.addEventListener('pl:refit', function () { fit(); });
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

    $('plPlay').addEventListener('click', function () {
      if (playing) {
        setPlay(false);
        if (hasMp3()) audio.pause(); else if (synth) synth.cancel();
        return;
      }
      setPlay(true);
      if (hasMp3()) {
        audio.muted = muted;
        if (synced()) {
          var a = cue(i), b = cue(i + 1);
          if (a === null) { show(0); return; }                         // on the knowledge check: start the lesson again
          if (audio.currentTime < a - 0.3 || (b !== null && audio.currentTime >= b)) seek(a);
        }
        audio.play();
      } else { speak(i); }
    });
    if (audio) {
      audio.addEventListener('timeupdate', function () {
        if (!playing || !synced()) return;
        var nxt = cue(i + 1);
        if (nxt !== null && audio.currentTime >= nxt - 0.05) {
          if (hasCards(i)) { audio.pause(); seek(nxt); return; }      // cards: wait for the learner, then Next
          show(i + 1, true);                                            // slides follow the narration
        }
      });
      audio.addEventListener('ended', function () {
        setPlay(false);
        if (synced()) show(total - 1, true);                           // end of narration: knowledge check
      });
    }
    $('plMute').addEventListener('click', function () {
      muted = !muted; this.classList.toggle('on', muted);
      if (audio) audio.muted = muted;
      if (muted && !hasMp3() && synth) synth.cancel();
      if (!muted && playing && !hasMp3()) speak(i);
    });
    $('plReplay').addEventListener('click', function () {
      if (hasMp3()) seek(0);
      show(0);
    });
    $('plPrev').addEventListener('click', function () { go(-1); });
    $('plNext').addEventListener('click', function () { go(1); });
    $('plMenu').addEventListener('click', function () { openDrawer('plMenuDrawer'); });
    document.addEventListener('keydown', function (e) {
      if (e.target && /INPUT|SELECT|TEXTAREA/.test(e.target.tagName)) return;
      if (e.key === 'ArrowRight' || e.key === 'PageDown') go(1);
      if (e.key === 'ArrowLeft' || e.key === 'PageUp') go(-1);
    });
    var x0 = null;
    panel.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    panel.addEventListener('touchend', function (e) {
      if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 70) go(dx < 0 ? 1 : -1);
    });
    window.addEventListener('pagehide', function () { if (synth) synth.cancel(); });
    var m = /#s(\d+)/.exec(location.hash);
    show(m ? (+m[1] - 1) : 0, true);
  }

  document.addEventListener('DOMContentLoaded', function () { setupDrawers(); setupPlayer(); });
})();

/* Flip cards: tap or press Enter/Space to turn a definition card over. */
(function () {
  document.addEventListener('click', function (e) {
    var c = e.target.closest && e.target.closest('.flipcard');
    if (!c) return;
    c.classList.toggle('flipped');
    var on = c.classList.contains('flipped');
    c.setAttribute('aria-pressed', on ? 'true' : 'false');
    document.dispatchEvent(on ? new CustomEvent('pl:card', { detail: c }) : new Event('pl:cardstop'));
  });
})();

/* TEM sorter: pick Threat / Error / UAS; feedback and running score per block. */
(function () {
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.tem-btns button');
    if (!b) return;
    var item = b.closest('.tem-item');
    if (!item || item.classList.contains('done')) return;
    var ok = b.getAttribute('data-c') === item.getAttribute('data-answer');
    item.classList.add('done', ok ? 'ok' : 'ko');
    b.classList.add('pick', ok ? 'right' : 'wrong');
    if (!ok) { var r = item.querySelector('.tem-btns button[data-c="' + item.getAttribute('data-answer') + '"]'); if (r) r.classList.add('right'); }
    var why = item.querySelector('.tem-why'); if (why) why.hidden = false;
    document.dispatchEvent(new Event('pl:refit'));
    document.dispatchEvent(new CustomEvent('pl:card', { detail: item }));
    var box = item.closest('.tem-sort'), all = box.querySelectorAll('.tem-item'), done = box.querySelectorAll('.tem-item.done');
    var s = box.querySelector('.tem-score');
    if (s && done.length === all.length) s.textContent = 'Score: ' + box.querySelectorAll('.tem-item.ok').length + ' / ' + all.length;
  });
})();
