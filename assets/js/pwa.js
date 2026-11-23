/* DAL TRAINING – install as an app and use offline.
   Registers sw.js (built by tools/pwa.py), shows the "Add to Home Screen" guide on iPhone/iPad,
   offers updates, and adds a "Save this course for offline" button on each course home page. */
(function () {
  'use strict';
  if (!('serviceWorker' in navigator) || !/^https?:$/.test(location.protocol)) return;

  var script = document.currentScript;
  var ROOT = script ? script.src.replace(/assets\/js\/pwa\.js(\?.*)?$/, '') : '/';
  var APP = 'DAL TRAINING';
  var ICON = ROOT + 'assets/img/icons/apple-touch-icon.png';
  var standalone = window.navigator.standalone === true || window.matchMedia('(display-mode: standalone)').matches;
  var isIOS = /iP(hone|ad|od)/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var isSafari = /Safari/.test(navigator.userAgent) && !/CriOS|FxiOS|EdgiOS|OPiOS|GSA/.test(navigator.userAgent);
  var path = location.pathname.slice(new URL(ROOT).pathname.length);
  var courseMatch = /^courses\/([^/]+)\/(index\.html)?$/.exec(path);
  var isPortal = path === '' || path === 'index.html';
  var deferredPrompt = null;

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function el(tag, attrs, html) { var e = document.createElement(tag); for (var k in attrs || {}) e.setAttribute(k, attrs[k]); if (html != null) e.innerHTML = html; return e; }
  function mb(bytes) { return bytes >= 1e9 ? (bytes / 1e9).toFixed(1) + ' GB' : Math.max(1, Math.round(bytes / 1e6)) + ' MB'; }

  var css = '' +
    '.dal-banner{display:flex;align-items:center;gap:12px;max-width:1100px;margin:14px auto 0;padding:12px 14px;background:#fff;border:1px solid #d6e3da;border-radius:14px;box-shadow:0 2px 8px rgba(0,0,0,.06);font:15px/1.35 system-ui,-apple-system,sans-serif;color:#10301c}' +
    '.dal-banner img{width:46px;height:46px;border-radius:11px;flex:none}' +
    '.dal-banner .t{flex:1;text-align:left;background:none;border:0;padding:0;font:inherit;color:inherit;cursor:pointer}' +
    '.dal-banner .t b{display:block;font-size:16px}' +
    '.dal-banner .x{flex:none;width:36px;height:36px;border-radius:50%;border:0;background:#eef4f0;color:#456;font-size:16px;cursor:pointer}' +
    '.dal-veil{position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:9998}' +
    '.dal-sheet{position:fixed;left:0;right:0;bottom:0;z-index:9999;max-width:560px;margin:0 auto;background:#fff;color:#10301c;border-radius:20px 20px 0 0;padding:12px 22px calc(22px + env(safe-area-inset-bottom));font:16px/1.5 system-ui,-apple-system,sans-serif;box-shadow:0 -6px 30px rgba(0,0,0,.25)}' +
    '.dal-sheet .h{display:flex;gap:14px;align-items:center;margin-top:8px}.dal-sheet .h img{width:60px;height:60px;border-radius:14px}' +
    '.dal-sheet h2{margin:0;font-size:21px}.dal-sheet .s{color:#5a6b60;font-size:14px}' +
    '.dal-sheet ol{padding-left:1.3em;margin:16px 0}.dal-sheet li{margin:9px 0}' +
    '.dal-sheet .share{display:inline-flex;vertical-align:-4px;color:#1d7a3e}' +
    '.dal-btn{display:block;width:100%;min-height:50px;border-radius:12px;border:1px solid #cfe0d4;background:#eef4f0;color:#10301c;font:600 16px system-ui,-apple-system,sans-serif;cursor:pointer;margin-top:8px}' +
    '.dal-btn.p{background:#1d7a3e;border-color:#1d7a3e;color:#fff}' +
    '.dal-update{position:fixed;left:12px;right:12px;top:calc(env(safe-area-inset-top) + 12px);z-index:9997;max-width:560px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px;background:#10301c;color:#fff;border-radius:14px;padding:10px 10px 10px 16px;font:15px system-ui,-apple-system,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.3)}' +
    '.dal-update button{min-height:40px;padding:0 16px;border:0;border-radius:10px;background:#7fd39b;color:#0b2414;font-weight:700;cursor:pointer}' +
    '.dal-offline{margin-top:14px;padding:14px 16px;border-radius:14px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);font:15px/1.4 system-ui,-apple-system,sans-serif;max-width:560px}' +
    '.dal-offline .row{display:flex;align-items:center;gap:12px;flex-wrap:wrap}' +
    '.dal-offline .msg{flex:1;min-width:180px}' +
    '.dal-offline button{min-height:44px;padding:0 16px;border-radius:10px;border:0;background:#fff;color:#125a2b;font-weight:700;cursor:pointer}' +
    '.dal-offline button.ghost{background:transparent;color:inherit;border:1px solid rgba(255,255,255,.5);font-weight:600}' +
    '.dal-offline .bar{height:6px;border-radius:9px;background:rgba(255,255,255,.25);margin-top:10px;overflow:hidden}.dal-offline .bar i{display:block;height:100%;background:#7fd39b;width:0}';
  document.head.appendChild(el('style', {}, css));

  // ---------------------------------------------------------------- install guide
  var shareSvg = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="M7 8l5-5 5 5"/><path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7"/></svg>';
  function openGuide() {
    var veil = el('div', { 'class': 'dal-veil' });
    var steps = isIOS
      ? '<ol>' + (isSafari ? '' : '<li>Open this page in <b>Safari</b> (copy the link and paste it in Safari).</li>') +
        '<li>Tap the <b>Share</b> button <span class="share">' + shareSvg + '</span> (bottom of the screen on iPhone, top right on iPad).</li>' +
        '<li>Scroll down and tap <b>Add to Home Screen</b> ➕.</li>' +
        '<li>Tap <b>Add</b>. ' + APP + ' now appears on your home screen.</li></ol>'
      : (deferredPrompt ? '<p>Install ' + APP + ' on this device to open it like an app, even without internet.</p>'
        : '<ol><li>Open your browser menu (⋮ or ⋯).</li><li>Choose <b>Install app</b> or <b>Add to Home screen</b>.</li></ol>');
    var sheet = el('section', { 'class': 'dal-sheet', role: 'dialog', 'aria-modal': 'true', 'aria-label': 'Install ' + APP },
      '<div class="h"><img src="' + ICON + '" alt=""><div><h2>Install ' + APP + '</h2><div class="s">Free · works offline · keeps your progress</div></div></div>' + steps +
      (deferredPrompt ? '<button class="dal-btn p" data-act="install">Install app</button>' : '') +
      '<button class="dal-btn" data-act="close">Not now</button>');
    function close() { veil.remove(); sheet.remove(); }
    veil.onclick = close;
    sheet.onclick = function (e) {
      var act = e.target.getAttribute('data-act');
      if (act === 'close') close();
      if (act === 'install' && deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.finally(function () { deferredPrompt = null; close(); var b = document.querySelector('.dal-banner'); if (b) b.remove(); });
      }
    };
    document.body.appendChild(veil);
    document.body.appendChild(sheet);
  }

  function showBanner() {
    if (standalone || store('dal-install-dismissed') === '1' || document.querySelector('.dal-banner')) return;
    if (!isPortal && !courseMatch) return;
    if (!isIOS && !deferredPrompt) return;
    var b = el('div', { 'class': 'dal-banner' },
      '<img src="' + ICON + '" alt=""><button class="t"><b>Install ' + APP + '</b>Add it to your home screen and use it like an app, even offline.</button>' +
      '<button class="x" aria-label="Dismiss">✕</button>');
    b.querySelector('.t').onclick = openGuide;
    b.querySelector('.x').onclick = function () { store('dal-install-dismissed', '1'); b.remove(); };
    var anchor = document.querySelector('.progress') || document.querySelector('header');
    if (anchor && anchor.parentNode) anchor.parentNode.insertBefore(b, anchor.nextSibling);
    else document.body.insertBefore(b, document.body.firstChild);
  }
  window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); deferredPrompt = e; showBanner(); });
  window.dalInstall = openGuide;

  // ---------------------------------------------------------------- service worker
  var swReady = navigator.serviceWorker.register(ROOT + 'sw.js', { scope: ROOT }).then(function (reg) {
    function offer(w) {
      if (document.querySelector('.dal-update')) return;
      var bar = el('div', { 'class': 'dal-update', role: 'status' }, '<span>New training content is available.</span><button>Update</button>');
      bar.querySelector('button').onclick = function () { w.postMessage('skipWaiting'); bar.remove(); };
      document.body.appendChild(bar);
    }
    if (reg.waiting && navigator.serviceWorker.controller) offer(reg.waiting);
    reg.addEventListener('updatefound', function () {
      var w = reg.installing;
      if (w) w.addEventListener('statechange', function () { if (w.state === 'installed' && navigator.serviceWorker.controller) offer(w); });
    });
    document.addEventListener('visibilitychange', function () { if (!document.hidden) reg.update().catch(function () {}); });
    return navigator.serviceWorker.ready;
  });
  var reloading = false;
  navigator.serviceWorker.addEventListener('controllerchange', function () {
    if (reloading || !window.__dalHadController) return;
    reloading = true; location.reload();
  });
  window.__dalHadController = !!navigator.serviceWorker.controller;
  if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {});

  // ---------------------------------------------------------------- save a course for offline
  function offlinePanel(slug) {
    var host = document.querySelector('.hero .wrap') || document.querySelector('main');
    if (!host) return;
    var box = el('div', { 'class': 'dal-offline', 'aria-live': 'polite' },
      '<div class="row"><span class="msg">Checking offline status…</span></div><div class="bar" hidden><i></i></div>');
    host.appendChild(box);
    var msg = box.querySelector('.msg'), row = box.querySelector('.row'), bar = box.querySelector('.bar'), fill = bar.querySelector('i');
    var sw = null;
    function send(m) { if (sw) sw.postMessage(m); }
    function setButtons(html) {
      Array.prototype.forEach.call(row.querySelectorAll('button'), function (b) { b.remove(); });
      if (html) row.insertAdjacentHTML('beforeend', html);
    }
    row.onclick = function (e) {
      var act = e.target.getAttribute && e.target.getAttribute('data-act');
      if (act === 'save') { setButtons(''); msg.textContent = 'Saving narration and documents…'; bar.hidden = false; send({ type: 'saveCourse', course: slug }); }
      if (act === 'remove' && confirm('Remove the saved narration and documents of this course from this device?')) send({ type: 'removeCourse', course: slug });
    };
    navigator.serviceWorker.addEventListener('message', function (e) {
      var d = e.data || {};
      if (d.course !== slug) return;
      if (d.type === 'courseStatus') {
        bar.hidden = true;
        if (!d.total) { box.remove(); return; }
        if (d.saved >= d.total) {
          msg.innerHTML = '✅ <b>Saved for offline.</b> Narration and documents work without internet.';
          setButtons('<button class="ghost" data-act="remove">Remove</button>');
        } else {
          msg.innerHTML = '✈️ <b>Using it in flight?</b> Save this course\'s narration and documents (' + mb(d.bytes) + ')' +
            (d.saved ? ' · ' + d.saved + ' of ' + d.total + ' already saved' : '') + '.';
          setButtons('<button data-act="save">Save for offline</button>');
        }
      }
      if (d.type === 'saveProgress') {
        fill.style.width = Math.round(((d.done + d.failed) / d.total) * 100) + '%';
        msg.textContent = 'Saving… ' + (d.done + d.failed) + ' of ' + d.total + ' files';
      }
      if (d.type === 'saveDone') {
        if (d.failed) { msg.textContent = d.failed + ' file(s) could not be saved. Check your connection and try again.'; setButtons('<button data-act="save">Try again</button>'); bar.hidden = true; }
        else send({ type: 'courseStatus', course: slug });
      }
    });
    swReady.then(function (reg) { sw = reg.active; send({ type: 'courseStatus', course: slug }); });
  }

  function init() {
    showBanner();
    if (courseMatch) offlinePanel(courseMatch[1]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
