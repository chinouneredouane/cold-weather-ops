#!/usr/bin/env python3
"""Build a demo of the "slide player" course layout (demo/player-demo.html) from real lessons.

Layout only: full-width picture, section bar, content banner over the picture, duration tag, bottom control bar,
slide menu, and a left-side "All courses" tab. Domestic Airlines logo, colours and content.
Usage: python3 tools/make_layout_demo.py [course_slug] [lessons]   e.g. cold-weather-operations 1,2,3
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build  # noqa: E402

slug = sys.argv[1] if len(sys.argv) > 1 else "cold-weather-operations"
lessons = [int(x) for x in (sys.argv[2] if len(sys.argv) > 2 else "1,2,3").split(",")]
course = next(c for c in build.COURSES if c["slug"] == slug)
base = f"../courses/{slug}/"

slides = []
for n in lessons:
    L = course["lessons"][n - 1]
    img = f"{base}media/images/lesson-{n:02d}.jpg"
    parts = re.split(r"<h2>(.*?)</h2>", L["body"])
    intro = parts[0].strip()
    obj = "<ul>" + "".join(f"<li>{html.escape(o)}</li>" for o in L["objectives"]) + "</ul>"
    slides.append(dict(lesson=n, ltitle=L["title"], section="Objectives", img=img, minutes=L["minutes"],
                       audio=f"{base}media/audio/lesson-{n:02d}.mp3", html=(intro + "<h3>Learning objectives</h3>" + obj)))
    for i in range(1, len(parts), 2):
        body = parts[i + 1].replace('src="../media/', f'src="{base}media/')
        slides.append(dict(lesson=n, ltitle=L["title"], section=re.sub("<[^>]+>", "", parts[i]), img=img, minutes=L["minutes"],
                           audio=f"{base}media/audio/lesson-{n:02d}.mp3", html=body))
    slides.append(dict(lesson=n, ltitle=L["title"], section="Key takeaways", img=img, minutes=L["minutes"],
                       audio=f"{base}media/audio/lesson-{n:02d}.mp3",
                       html="<ul class='take'>" + "".join(f"<li>{html.escape(t)}</li>" for t in L["takeaways"]) + "</ul>"))

all_courses = [(c["title"], f"../courses/{c['slug']}/index.html") for c in build.COURSES] + [(e["title"], "../" + e["href"]) for e in build.EXTERNAL]

ICON = {
 "replay": '<path d="M12 5V2L7 6l5 4V7a5 5 0 1 1-5 5H5a7 7 0 1 0 7-7z"/>',
 "menu": '<path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h16v2H4z"/>',
 "home": '<path d="M12 3l9 8h-3v9h-5v-6h-2v6H6v-9H3z"/>',
 "prev": '<path d="M15.5 5l-7 7 7 7-1.6 1.6L5.3 12l8.6-8.6z"/>',
 "next": '<path d="M8.5 5l7 7-7 7 1.6 1.6 8.6-8.6-8.6-8.6z"/>',
 "pause": '<path d="M7 5h3v14H7zm7 0h3v14h-3z"/>',
 "play": '<path d="M8 5v14l11-7z"/>',
 "audio": '<path d="M4 9v6h4l5 4V5L8 9zm12.5 3a4.5 4.5 0 0 0-2.5-4v8a4.5 4.5 0 0 0 2.5-4z"/>',
 "close": '<path d="M6.4 5L12 10.6 17.6 5 19 6.4 13.4 12 19 17.6 17.6 19 12 13.4 6.4 19 5 17.6 10.6 12 5 6.4z"/>',
 "grid": '<path d="M4 4h7v7H4zm9 0h7v7h-7zM4 13h7v7H4zm9 0h7v7h-7z"/>',
}
def svg(name):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICON[name]}</svg>'

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Layout demo — {html.escape(course['title'])}</title>
<style>
:root{{--g:#1d7a3e;--gd:#125a2b;--gdeep:#0c3d1e;--band:rgba(12,61,30,.92);--ink:#14231b;--line:#dbe5df;--font:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}}
*{{box-sizing:border-box}} html,body{{margin:0;height:100%;font-family:var(--font);color:var(--ink);background:#e9efeb}}
.player{{position:fixed;inset:0;display:grid;grid-template-rows:auto 1fr auto;background:#fff}}
/* top bar */
.top{{display:flex;align-items:stretch;justify-content:space-between;border-bottom:3px solid var(--g);min-height:58px}}
.brand{{display:flex;align-items:center;gap:12px;padding:8px 16px 8px 56px}}
.brand img{{height:34px}} .brand b{{font-size:1.05rem;color:var(--gd)}}
.crumbs{{background:var(--g);color:#d9efe0;display:flex;align-items:center;gap:10px;padding:0 22px;font-size:.95rem;clip-path:polygon(18px 0,100% 0,100% 100%,0 100%);padding-left:36px;max-width:65%;overflow:hidden;white-space:nowrap}}
.crumbs span{{opacity:.85}} .crumbs strong{{color:#fff}} .crumbs i{{opacity:.6;font-style:normal}}
/* stage */
.stage{{position:relative;overflow:hidden;background:#0c3d1e}}
.stage .bg{{position:absolute;inset:0;background-size:cover;background-position:center;transition:opacity .5s}}
.stage .shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.05),rgba(0,0,0,.15) 55%,rgba(0,0,0,.35))}}
.lessontag{{position:absolute;left:22px;top:18px;background:rgba(255,255,255,.92);color:var(--gd);padding:6px 12px;border-radius:6px;font-weight:700;font-size:.9rem}}
.panel{{position:absolute;left:0;right:0;bottom:46px;background:var(--band);color:#fff;padding:16px 22px 18px;max-height:58%;overflow:auto}}
.panel h2{{margin:0 0 8px;font-size:1.15rem;letter-spacing:.2px}}
.panel p,.panel li{{line-height:1.5;font-size:1rem}} .panel ul,.panel ol{{margin:6px 0 0 1.1em;padding:0}}
.panel a{{color:#bfe8cc}} .panel strong{{color:#fff}}
.panel table{{border-collapse:collapse;width:100%;background:rgba(255,255,255,.06);margin:8px 0}} .panel td,.panel th{{border:1px solid rgba(255,255,255,.25);padding:6px 8px;text-align:left;font-size:.92rem}}
.panel figure{{background:#fff;border-radius:8px;padding:8px;margin:10px 0;color:var(--ink)}} .panel figure img,.panel figure svg{{max-width:100%;height:auto;display:block;margin:0 auto}}
.panel .callout{{border-left:4px solid #9fd4b0;padding:6px 12px;margin:10px 0;background:rgba(255,255,255,.07)}} .panel .label{{display:block;font-weight:700;font-size:.8rem;text-transform:uppercase;letter-spacing:.6px;color:#bfe8cc}}
.panel .take li{{margin-bottom:6px}}
.duration{{position:absolute;right:0;bottom:8px;background:#f1f4f2;color:var(--gd);font-weight:700;padding:7px 16px;font-size:.95rem}}
/* bottom bar */
.bar{{display:flex;justify-content:space-between;align-items:stretch;background:var(--gdeep);min-height:56px}}
.bar .fill{{flex:1}}
.ctrl{{display:flex;align-items:center;gap:6px;background:#f1f4f2;padding:6px 10px}}
.ctrl button{{width:40px;height:40px;border:2px solid var(--g);background:#fff;border-radius:8px;display:grid;place-items:center;cursor:pointer;padding:0}}
.ctrl button:hover{{background:#e7f3eb}} .ctrl button svg{{width:22px;height:22px;fill:var(--gd)}}
.ctrl button.on{{background:var(--g)}} .ctrl button.on svg{{fill:#fff}}
.count{{min-width:64px;text-align:center;font-weight:700;color:var(--gd)}}
.sep{{width:12px}}
.progress{{position:absolute;left:0;right:0;bottom:0;height:4px;background:rgba(255,255,255,.25)}} .progress i{{display:block;height:100%;background:#7fd09a;width:0;transition:width .3s}}
/* drawers */
.drawer{{position:fixed;top:0;bottom:0;width:min(360px,88vw);background:#fff;box-shadow:0 0 40px rgba(0,0,0,.25);transform:translateX(-105%);transition:transform .25s;z-index:20;display:flex;flex-direction:column}}
.drawer.right{{right:0;transform:translateX(105%)}} .drawer.open{{transform:none}}
.drawer header{{background:var(--g);color:#fff;padding:14px 16px;font-weight:700;display:flex;justify-content:space-between;align-items:center}}
.drawer header button{{background:none;border:0;color:#fff;font-size:1.4rem;cursor:pointer}}
.drawer nav{{overflow:auto;padding:8px 0}}
.drawer a,.drawer .item{{display:block;padding:10px 18px;color:var(--ink);text-decoration:none;border-bottom:1px solid #eef3f0;cursor:pointer;font-size:.95rem}}
.drawer a:hover,.drawer .item:hover{{background:#f3f9f5}} .drawer .item.cur{{background:#e7f3eb;font-weight:700}}
.drawer .grp{{padding:12px 18px 4px;font-size:.78rem;text-transform:uppercase;letter-spacing:.6px;color:#5b6b62;font-weight:700}}
.veil{{position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:15;display:none}} .veil.on{{display:block}}
/* left "all courses" tab */
.alltab{{position:fixed;left:0;top:12px;z-index:12;width:42px;height:42px;border:0;border-radius:0 10px 10px 0;background:var(--g);display:grid;place-items:center;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.2)}}
.alltab svg{{width:22px;height:22px;fill:#fff}} .alltab:hover{{width:48px}}
.demo-note{{position:fixed;right:10px;top:64px;z-index:11;background:#fff5e0;color:#7a4c00;border:1px solid #e8c88a;padding:4px 10px;border-radius:6px;font-size:.78rem}}
@media (max-width:760px){{
  .brand{{padding-left:52px}} .brand b{{font-size:.95rem}} .crumbs{{display:none}}
  .stage{{display:flex;flex-direction:column}} .stage .bg{{position:relative;height:34vh;flex:none}} .stage .shade{{display:none}}
  .panel{{position:relative;bottom:auto;max-height:none;flex:1;overflow:auto}} .duration{{top:calc(34vh - 40px);bottom:auto}}
  .bar .fill{{display:none}} .ctrl{{width:100%;justify-content:space-between;padding:6px 4px;gap:2px}} .ctrl button{{width:32px;height:32px;border-width:1.5px}} .ctrl button svg{{width:18px;height:18px}} .count{{min-width:44px;font-size:.85rem}} .sep{{display:none}}
  .demo-note{{top:auto;bottom:70px}} .duration{{font-size:.8rem;padding:5px 10px}} .lessontag{{font-size:.8rem;left:12px;right:12px;top:10px}}
}}
</style></head>
<body>
<button class="alltab" id="allBtn" title="All courses" aria-label="All courses">{svg('grid')}</button>
<div class="demo-note">Layout demo</div>
<div class="player">
  <div class="top">
    <div class="brand"><img src="../assets/img/logo.png" alt="Domestic Airlines"><b>{html.escape(course['title'])}</b></div>
    <div class="crumbs" id="crumbs"></div>
  </div>
  <div class="stage">
    <div class="bg" id="bg"></div><div class="shade"></div>
    <div class="lessontag" id="ltag"></div>
    <div class="panel" id="panel"></div>
    <div class="duration" id="dur"></div>
    <div class="progress"><i id="prog"></i></div>
  </div>
  <div class="bar"><div class="fill"></div>
    <div class="ctrl">
      <button id="bReplay" title="Restart lesson">{svg('replay')}</button>
      <button id="bMenu" title="Slide menu">{svg('menu')}</button>
      <button id="bHome" title="Course home">{svg('home')}</button>
      <button id="bPrev" title="Previous">{svg('prev')}</button>
      <span class="count" id="count"></span>
      <button id="bNext" title="Next">{svg('next')}</button>
      <span class="sep"></span>
      <button id="bPause" title="Play / pause narration">{svg('play')}</button>
      <button id="bAudio" title="Narration on / off">{svg('audio')}</button>
      <button id="bClose" title="Close">{svg('close')}</button>
    </div>
  </div>
</div>
<div class="veil" id="veil"></div>
<aside class="drawer right" id="menu"><header>Slides <button data-close>×</button></header><nav id="menuList"></nav></aside>
<aside class="drawer" id="all"><header>All courses <button data-close>×</button></header><nav>
  <a href="../index.html"><strong>Academy home</strong></a>
  {''.join(f'<a href="{h}">{html.escape(t)}</a>' for t, h in all_courses)}
</nav></aside>
<audio id="au" preload="none"></audio>
<script>
var S={json.dumps(slides)}, i=0, au=document.getElementById('au'), audioOn=true, curLesson=null;
var $=function(id){{return document.getElementById(id)}};
function show(k){{
  i=Math.max(0,Math.min(S.length-1,k)); var s=S[i];
  $('bg').style.backgroundImage='url("'+s.img+'")';
  var secs=S.filter(function(x){{return x.lesson==s.lesson}});
  $('crumbs').innerHTML='<span>Lesson '+s.lesson+'</span><i>|</i>'+secs.slice(Math.max(0,secs.indexOf(s)-1),secs.indexOf(s)+2).map(function(x){{return x===s?'<strong>'+x.section+'</strong>':'<span>'+x.section+'</span>'}}).join('<i>|</i>');
  $('ltag').textContent='Lesson '+s.lesson+' — '+s.ltitle;
  $('panel').innerHTML='<h2>'+s.section+'</h2>'+s.html; $('panel').scrollTop=0;
  $('dur').textContent='Duration: '+s.minutes+' min';
  $('count').textContent=(i+1)+'/'+S.length; $('prog').style.width=((i+1)/S.length*100)+'%';
  document.querySelectorAll('#menuList .item').forEach(function(e,k){{e.classList.toggle('cur',k==i)}});
  if(s.lesson!==curLesson){{curLesson=s.lesson;au.src=s.audio;au.pause();$('bPause').classList.remove('on');$('bPause').innerHTML='{svg('play')}'}}
}}
var ml='',last=null;S.forEach(function(s,k){{if(s.lesson!==last){{ml+='<div class="grp">Lesson '+s.lesson+' — '+s.ltitle+'</div>';last=s.lesson}}ml+='<div class="item" data-k="'+k+'">'+s.section+'</div>'}});
$('menuList').innerHTML=ml;
$('menuList').onclick=function(e){{var k=e.target.dataset.k;if(k!=null){{show(+k);closeAll()}}}};
function open(id){{$(id).classList.add('open');$('veil').classList.add('on')}}
function closeAll(){{document.querySelectorAll('.drawer').forEach(function(d){{d.classList.remove('open')}});$('veil').classList.remove('on')}}
document.querySelectorAll('[data-close]').forEach(function(b){{b.onclick=closeAll}}); $('veil').onclick=closeAll;
$('bMenu').onclick=function(){{open('menu')}}; $('allBtn').onclick=function(){{open('all')}};
$('bPrev').onclick=function(){{show(i-1)}}; $('bNext').onclick=function(){{show(i+1)}};
$('bReplay').onclick=function(){{var f=S.findIndex(function(x){{return x.lesson==S[i].lesson}});show(f);au.currentTime=0}};
$('bHome').onclick=function(){{location.href='../courses/{slug}/index.html'}};
$('bClose').onclick=function(){{location.href='../index.html'}};
$('bPause').onclick=function(){{if(!audioOn)return;if(au.paused){{au.play();this.classList.add('on');this.innerHTML='{svg('pause')}'}}else{{au.pause();this.classList.remove('on');this.innerHTML='{svg('play')}'}}}};
$('bAudio').onclick=function(){{audioOn=!audioOn;this.classList.toggle('on',!audioOn);if(!audioOn){{au.pause();$('bPause').innerHTML='{svg('play')}';$('bPause').classList.remove('on')}}}};
document.addEventListener('keydown',function(e){{if(e.key=='ArrowRight')show(i+1);if(e.key=='ArrowLeft')show(i-1);if(e.key=='Escape')closeAll()}});
show(0);
</script>
</body></html>"""

os.makedirs(os.path.join(ROOT, "demo"), exist_ok=True)
out = os.path.join(ROOT, "demo", "player-demo.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(page)
print(f"wrote {os.path.relpath(out, ROOT)}: {len(slides)} slides from lessons {lessons}")
