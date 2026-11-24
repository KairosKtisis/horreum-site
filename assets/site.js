/* Horreum — horreum.cloud · site.js (v2)
   No dependencies. The original three jobs — the mobile nav, the addresses the site quotes, and the
   forms (which post straight to the platform's guarded RPC) — plus two quiet pieces of motion: a
   gentle reveal on scroll and the pinned story. Both stand down under prefers-reduced-motion. */
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
        done.innerHTML = '<div class="eyebrow">Received</div><h3>' + (data.kind === 'demo' ? 'Thank you — we’ll be in touch.' : data.kind === 'pricing' ? 'Thank you — we’ll be in touch.' : 'Thank you — message received.') + '</h3>' +
          '<p class="small">' + (data.kind === 'demo' ? 'Expect a reply from a real person within one business day.' : data.kind === 'pricing' ? 'Expect a reply from a real person within one business day.' : 'We read every message and reply within one business day.') + '</p>';
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
    for (var i = 0; i < auto.length; i++) { if (!auto[i].closest('.trio, .story-stage, .h-hero')) auto[i].classList.add('rv'); }
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


  /* prefill from the URL, e.g. /contact?kind=demo&venue=… */
  function prefill() {
    try {
      var q = new URLSearchParams(location.search);
      q.forEach(function (v, k) { var f = document.querySelector('form[data-lead] [name="' + k + '"]'); if (f) f.value = v; });
    } catch (e) {}
  }

  function safe(fn) { try { fn(); } catch (e) { try { console.warn(e); } catch (e2) {} } }
  document.addEventListener('DOMContentLoaded', function () {
    [fill, nav, forms, prefill, headerScroll, reveals, story].forEach(safe);
    /* if anything above failed, nothing stays hidden */
    setTimeout(function () { var l = document.querySelectorAll('.rv:not(.in)'); for (var i = 0; i < l.length; i++) { var r = l[i].getBoundingClientRect(); if (r.top < innerHeight) l[i].classList.add('in'); } }, 1600);
  });
})();

/* Gabe, Nov 24 2026, 12:24 AM: "The app should not rotate with my phone, should always be portrait. Ensure this is true across
   ios, android, the web app and the website." A browser gives a page no way to lock rotation, so on a phone held sideways the
   page stays put under one plain line, "Turn your phone upright", until it is. Phones only - a tablet or a laptop turns freely.
   The same guard as the app's assets/hz-upright.js (horreum-platform R878); the phone test reads the screen, not the window. */
(function () {
  'use strict';
  if (window.__hzUpright) return;
  window.__hzUpright = 1;
  try { if (window.Capacitor && window.Capacitor.isNativePlatform && window.Capacitor.isNativePlatform()) return; } catch (e) {}
  var coarse = window.matchMedia ? window.matchMedia('(pointer: coarse)') : null;
  function phone() {
    var s = Math.min(screen.width || 0, screen.height || 0);   // the short side, whichever way the phone is held
    return s > 0 && s < 500 && (!coarse || coarse.matches);
  }
  function sideways() {
    var t = screen.orientation && screen.orientation.type;
    if (t) return t.indexOf('landscape') === 0;
    if (typeof window.orientation === 'number') return Math.abs(window.orientation) === 90;
    return window.innerWidth > window.innerHeight;
  }
  var el = null;
  function build() {
    var st = document.createElement('style');
    st.textContent =
      '#hz-upright{display:none;position:fixed;inset:0;z-index:2147483000;flex-direction:column;align-items:center;justify-content:center;' +
      'gap:14px;padding:24px;text-align:center;-webkit-user-select:none;user-select:none;touch-action:none}' +
      'html.hz-sideways #hz-upright{display:flex}html.hz-sideways,html.hz-sideways body{overflow:hidden}' +
      '#hz-upright svg{width:34px;height:34px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;opacity:.7}' +
      '#hz-upright p{margin:0;font:400 21px/1.3 var(--display,"Playfair Display",Georgia,serif);letter-spacing:.01em}';
    document.head.appendChild(st);
    el = document.createElement('div');
    el.id = 'hz-upright';
    el.setAttribute('role', 'alert');
    el.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="2.5" width="10" height="19" rx="2.2"/><path d="M11 18.5h2"/></svg><p>Turn your phone upright</p>';
    document.body.appendChild(el);
  }
  function solid(c) { return c && c !== 'transparent' && !/rgba\([^)]*,\s*0\)$/.test(c); }
  function paint() {   /* the page's own ground and ink, whatever theme it wears */
    var b = getComputedStyle(document.body), h = getComputedStyle(document.documentElement);
    el.style.background = solid(b.backgroundColor) ? b.backgroundColor : (solid(h.backgroundColor) ? h.backgroundColor : '#0B0C11');
    el.style.color = b.color || '#EFE6D6';
  }
  function apply() {
    if (!document.body) return;
    var on = phone() && sideways();
    document.documentElement.classList.toggle('hz-sideways', on);
    if (!on) return;
    if (!el) build();
    paint();
    try { var a = document.activeElement; if (a && a !== document.body && a.blur) a.blur(); } catch (e) {}   // the keyboard goes down too
  }
  function soon() { apply(); setTimeout(apply, 250); }   // some phones report the new orientation a beat late
  if (screen.orientation && screen.orientation.addEventListener) screen.orientation.addEventListener('change', soon);
  window.addEventListener('orientationchange', soon);
  window.addEventListener('resize', apply);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', apply); else apply();
})();
