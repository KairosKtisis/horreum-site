/* Horreum — horreum.cloud · site.js (v2)
   No dependencies. The original three jobs — the mobile nav, the addresses the site quotes, and the
   forms (which post straight to the platform's guarded RPC) — plus the site's motion: the sky, the
   header that tightens on scroll, reveals, the pinned story, and the light that follows the pointer
   across a card. Everything decorative stands down under prefers-reduced-motion. */
(function () {
  'use strict';

  /* One place for the addresses the site quotes. Change them here, every page follows. */
  var HZ = {
    app: 'https://app.horreum.cloud',
    email: 'gabriel@horreum.cloud',
    support: 'gabriel@horreum.cloud',
    supabaseUrl: 'https://kecyxblkcuautnxdeutl.supabase.co',
    // The anon (publishable) key. Safe to ship: it can only call the one guarded RPC below.
    anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtlY3l4YmxrY3VhdXRueGRldXRsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI4MzU3MDgsImV4cCI6MjA5ODQxMTcwOH0.y3_83affF2m5y9nFDVaontMb9f3ZtEgAm1k9Tzvig2I'
  };
  window.HZ_SITE = HZ;

  /* fill the quoted price / year / emails wherever a page asks */
  function fill() {
    var nodes = document.querySelectorAll('[data-hz]');
    for (var i = 0; i < nodes.length; i++) {
      var k = nodes[i].getAttribute('data-hz');
      if (k === 'year') nodes[i].textContent = String(new Date().getFullYear());
      else if (k === 'email') { nodes[i].textContent = HZ.email; if (nodes[i].tagName === 'A') nodes[i].href = 'mailto:' + HZ.email; }
      else if (k === 'support') { nodes[i].textContent = HZ.support; if (nodes[i].tagName === 'A') nodes[i].href = 'mailto:' + HZ.support; }
    }
  }

  /* mobile nav */
  function nav() {
    var header = document.querySelector('.site-header'), btn = document.querySelector('.nav-toggle');
    if (!header || !btn) return;
    btn.addEventListener('click', function () {
      var open = header.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.documentElement.classList.toggle('nav-open', open);
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { header.classList.remove('open'); document.documentElement.classList.remove('nav-open'); btn.setAttribute('aria-expanded', 'false'); } });
    header.addEventListener('click', function (e) { if (e.target.closest && e.target.closest('.nav a, .header-cta a')) { header.classList.remove('open'); document.documentElement.classList.remove('nav-open'); } });
    /* mark the current page */
    var here = location.pathname.replace(/\/index(\.html)?$/, '/').replace(/\.html$/, '');
    var links = header.querySelectorAll('.nav a');
    for (var i = 0; i < links.length; i++) {
      var href = links[i].getAttribute('href').replace(/\.html$/, '');
      if (href === here || (here.endsWith('/') && href === here.slice(0, -1))) links[i].setAttribute('aria-current', 'page');
    }
  }

  /* forms → submit_site_lead (validation, honeypot and rate limits live server-side) */
  function forms() {
    var fs = document.querySelectorAll('form[data-lead]');
    for (var i = 0; i < fs.length; i++) wire(fs[i]);
  }
  function wire(form) {
    var msg = form.querySelector('.form-msg'), btn = form.querySelector('button[type="submit"]');
    var label = btn ? btn.textContent : '';
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = {};
      var els = form.elements;
      for (var i = 0; i < els.length; i++) { if (els[i].name) data[els[i].name] = els[i].value; }
      data.kind = (form.elements.kind && form.elements.kind.value) || form.getAttribute('data-lead') || 'contact';
      data.source_page = location.pathname;
      data.user_agent = navigator.userAgent.slice(0, 300);
      if (!data.name || data.name.trim().length < 2) return fail('Please tell us your name.');
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(data.email || '')) return fail('That email address doesn’t look right.');
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
      if (msg) { msg.textContent = ''; msg.classList.remove('ok'); }
      fetch(HZ.supabaseUrl + '/rest/v1/rpc/submit_site_lead', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'apikey': HZ.anonKey, 'Authorization': 'Bearer ' + HZ.anonKey },
        body: JSON.stringify({ p: data })
      }).then(function (r) {
        return r.json().then(function (j) { if (!r.ok) throw new Error((j && (j.message || j.hint)) || 'Something went wrong.'); return j; });
      }).then(function () {
        var done = document.createElement('div'); done.className = 'form-done';
        done.innerHTML = '<div class="eyebrow">Received</div><h3>' + (data.kind === 'demo' ? 'Thank you — we’ll be in touch.' : data.kind === 'pricing' ? 'Thank you — your number is on its way.' : 'Thank you — message received.') + '</h3>' +
          '<p class="small">' + (data.kind === 'demo' ? 'Expect a reply from a real person within one business day.' : data.kind === 'pricing' ? 'Expect pricing for your program from a real person the same business day.' : 'We read every message and reply within one business day.') + '</p>';
        form.parentNode.replaceChild(done, form);
      }).catch(function (err) {
        fail((err && err.message) || 'Something went wrong. Email us instead: ' + HZ.email);
        if (btn) { btn.disabled = false; btn.textContent = label; }
      });
    });
    function fail(t) { if (msg) { msg.textContent = t; msg.classList.remove('ok'); } }
  }


  var REDUCED = false; try { REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}

  /* the header tightens once the page leaves the top */
  function headerScroll() {
    var h = document.querySelector('.site-header'); if (!h) return;
    var on = function () { h.classList.toggle('scrolled', (window.scrollY || 0) > 24); };
    on(); window.addEventListener('scroll', on, { passive: true });
  }

  /* reveal on scroll: anything marked .rv, plus the common blocks so older page bodies get it for free */
  function reveals() {
    var auto = document.querySelectorAll('.sec .card, .sec .step, .sec .stat, .sec .price-card, .sec .phone, .sec h2, .sec .lead, .faq details, .phones figure, .hero .phone');
    for (var i = 0; i < auto.length; i++) { if (!auto[i].closest('.fan, .story-stage, .h-hero')) auto[i].classList.add('rv'); }
    var els = document.querySelectorAll('.rv');
    if (!('IntersectionObserver' in window) || REDUCED) { for (var j = 0; j < els.length; j++) els[j].classList.add('in'); return; }
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    /* siblings arrive one after another */
    for (var k = 0; k < els.length; k++) {
      var el = els[k], p = el.parentNode, idx = 0;
      if (p && (p.classList.contains('grid') || p.classList.contains('bento') || p.classList.contains('steps') || p.classList.contains('phones'))) idx = Array.prototype.indexOf.call(p.children, el);
      if (idx) el.style.setProperty('--d', Math.min(idx * 0.07, 0.42) + 's');
      io.observe(el);
    }
  }

  /* the light that follows the pointer across a card */
  function spotlight() {
    if (!window.matchMedia || !matchMedia('(hover: hover)').matches) return;
    document.addEventListener('pointermove', function (e) {
      var c = e.target && e.target.closest ? e.target.closest('.card') : null; if (!c) return;
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }, { passive: true });
  }

  /* the sky: the app's own night — a few hundred stars, most still, some breathing. One canvas per .sky. */
  function sky() {
    var cs = document.querySelectorAll('canvas.sky'); if (!cs.length) return;
    Array.prototype.forEach.call(cs, function (cv) {
      var ctx = cv.getContext('2d'), stars = [], w = 0, h = 0, dpr = Math.min(window.devicePixelRatio || 1, 2), raf = 0, visible = true, seed = 7;
      function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
      function size() {
        var r = cv.getBoundingClientRect(); w = r.width; h = r.height; cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        seed = 7; stars = []; var n = Math.round(Math.min(420, (w * h) / 5200));
        for (var i = 0; i < n; i++) { var m = rnd(); stars.push({ x: rnd() * w, y: rnd() * h, r: m < .9 ? .35 + rnd() * .7 : 1 + rnd() * .9, a: .25 + rnd() * .65, tw: rnd() < .3 ? .4 + rnd() * 1.2 : 0, ph: rnd() * 6.28, gold: rnd() < .22 }); }
        draw(0);
      }
      function draw(t) {
        ctx.clearRect(0, 0, w, h);
        for (var i = 0; i < stars.length; i++) { var s = stars[i], a = s.tw ? s.a * (.55 + .45 * Math.sin(t / 1000 * s.tw + s.ph)) : s.a;
          ctx.globalAlpha = a; ctx.fillStyle = s.gold ? '#F1D68F' : '#EAF0FF'; ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, 6.2832); ctx.fill(); }
        ctx.globalAlpha = 1;
      }
      function loop(t) { if (visible) draw(t); raf = requestAnimationFrame(loop); }
      size(); var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(size, 150); });
      if (REDUCED) return;
      if ('IntersectionObserver' in window) new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(cv);
      raf = requestAnimationFrame(loop);
    });
  }

  /* the pinned story: the phone stays, the chapters pass, the screen follows */
  function story() {
    var st = document.querySelector('.story'); if (!st) return;
    var ch = st.querySelectorAll('.chapter'), imgs = st.querySelectorAll('.story-stage .stack img');
    function show(i) { for (var k = 0; k < ch.length; k++) ch[k].classList.toggle('on', k === i); for (var j = 0; j < imgs.length; j++) imgs[j].classList.toggle('on', j === i); }
    show(0);
    if (!('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (en) { en.forEach(function (e) { if (e.isIntersecting) show(Array.prototype.indexOf.call(ch, e.target)); }); }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
    for (var i = 0; i < ch.length; i++) io.observe(ch[i]);
  }

  /* the hero's fan leans a little toward the pointer */
  function fan() {
    var f = document.querySelector('.fan'); if (!f || REDUCED || !window.matchMedia || !matchMedia('(hover: hover)').matches) return;
    var mid = f.querySelector('.phone:nth-child(2) .phone-body'); if (!mid) return;
    f.addEventListener('pointermove', function (e) { var r = f.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      mid.style.transform = 'rotateY(' + (x * 9).toFixed(2) + 'deg) rotateX(' + (-y * 6).toFixed(2) + 'deg)'; mid.style.transition = 'transform .15s ease-out'; });
    f.addEventListener('pointerleave', function () { mid.style.transition = 'transform .8s cubic-bezier(.22,1,.36,1)'; mid.style.transform = ''; });
  }

  /* prefill from the URL, e.g. /contact?kind=demo&venue=… */
  function prefill() {
    try {
      var q = new URLSearchParams(location.search);
      q.forEach(function (v, k) { var f = document.querySelector('form[data-lead] [name="' + k + '"]'); if (f) f.value = v; });
    } catch (e) {}
  }

  function safe(fn) { try { fn(); } catch (e) { try { console.warn(e); } catch (e2) {} } }
  document.addEventListener('DOMContentLoaded', function () {
    [fill, nav, forms, prefill, headerScroll, reveals, spotlight, sky, story, fan].forEach(safe);
    /* if anything above failed, nothing stays hidden */
    setTimeout(function () { var l = document.querySelectorAll('.rv:not(.in)'); for (var i = 0; i < l.length; i++) { var r = l[i].getBoundingClientRect(); if (r.top < innerHeight) l[i].classList.add('in'); } }, 1600);
  });
})();
