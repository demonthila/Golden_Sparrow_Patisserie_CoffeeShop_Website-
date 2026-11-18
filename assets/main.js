/* Golden Sparrow Patisserie — interactions (vanilla JS, no libraries) */
(function () {
  var doc = document.documentElement;
  doc.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Intro: logo wipes in at centre, then glides into the header.
     Plays on every refresh and when arriving from another site; skipped when clicking between our own pages. ---------- */
  var intro = document.querySelector('.intro');
  var played = doc.classList.contains('intro-done');
  function startPage() { doc.classList.add('is-loaded'); }
  if (!intro || played || reduce) {
    if (intro) intro.remove();
    setTimeout(startPage, 60);
  } else {
    doc.classList.add('intro-running');
    var logo = intro.querySelector('.intro__logo');
    var EASE = 'cubic-bezier(0.76, 0, 0.24, 1)';
    var go = function () {
      requestAnimationFrame(function () {
        logo.style.transition = 'clip-path 1.1s ' + EASE;
        logo.style.clipPath = 'inset(0 0% 0 0)';
      });
      setTimeout(function () {
        var target = document.querySelector('.nav .logo img');
        var r = target.getBoundingClientRect(), w = logo.getBoundingClientRect().width;
        logo.style.transition = 'left 0.9s ' + EASE + ', top 0.9s ' + EASE + ', transform 0.9s ' + EASE;
        logo.style.left = (r.left + r.width / 2) + 'px';
        logo.style.top = (r.top + r.height / 2) + 'px';
        logo.style.transform = 'translate(-50%, -50%) scale(' + (r.width / w) + ')';
        intro.classList.add('intro--out');
        setTimeout(startPage, 350);
        setTimeout(function () { doc.classList.remove('intro-running'); doc.classList.add('intro-done'); intro.remove(); }, 1000);
      }, 1500);
    };
    if (logo.complete) go(); else { logo.addEventListener('load', go); logo.addEventListener('error', go); }
    setTimeout(function () { if (intro.isConnected) { intro.remove(); doc.classList.remove('intro-running'); startPage(); } }, 6000);
  }

  /* ---------- Smooth scrolling (Lenis), like the reference ---------- */
  if (window.Lenis && !reduce) {
    var lenis = new Lenis({ lerp: 0.1, smoothWheel: true, anchors: true });
    (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
    window.__lenis = lenis;
  }

  /* ---------- Coffee "photo" placeholders (SVG, replaced by real photos later) ---------- */
  var uid = 0;
  var drinks = {
    latte:      { liquid: ['#c89a6c', '#8a5a36'], art: 'heart' },
    flatwhite:  { liquid: ['#b8875a', '#7a4a28'], art: 'rosetta' },
    cappuccino: { liquid: ['#f2e6d6', '#d9c3a6'], art: 'cocoa' },
    espresso:   { liquid: ['#b3753f', '#5a2f14'], art: 'crema', small: true },
    longblack:  { liquid: ['#7a4a26', '#2a160b'], art: 'crema' },
    mocha:      { liquid: ['#9b6845', '#4b2a18'], art: 'heart' },
    chai:       { liquid: ['#e0bf93', '#b98a57'], art: 'spice' },
    iced:       { liquid: ['#d2a77a', '#9a6a43'], art: 'ice', glass: true },
    coldbrew:   { liquid: ['#6a3d1f', '#2b170a'], art: 'ice', glass: true },
    matcha:     { liquid: ['#b9cf86', '#6f8f3c'], art: 'heart' },
    hotchoc:    { liquid: ['#8f5a3a', '#4a2414'], art: 'cocoa2' },
    raffaello:  { liquid: ['#efe4d2', '#d6c2a3'], art: 'coconut' },
    icedchoc:   { liquid: ['#7a4a2c', '#3c1f10'], art: 'ice', glass: true }
  };
  function cupSVG(type) {
    var d = drinks[type] || drinks.latte; var id = 'c' + (++uid);
    var R = d.small ? 120 : 165, r = R - (d.glass ? 10 : 22);
    var cx = 300, cy = 300;
    var s = '<svg viewBox="0 0 600 600" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">' +
      '<defs>' +
      '<filter id="n' + id + '"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="' + uid + '"/><feColorMatrix values="0 0 0 0 .3  0 0 0 0 .25  0 0 0 0 .2  0 0 0 .09 0"/></filter>' +
      '<filter id="b' + id + '" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="18"/></filter>' +
      '<filter id="s' + id + '" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>' +
      '<radialGradient id="l' + id + '" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="' + d.liquid[0] + '"/><stop offset="1" stop-color="' + d.liquid[1] + '"/></radialGradient>' +
      '<radialGradient id="k' + id + '" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#ffffff"/><stop offset=".8" stop-color="#efe9e1"/><stop offset="1" stop-color="#d9d1c6"/></radialGradient>' +
      '</defs>' +
      '<rect width="600" height="600" fill="#e9e3d9"/>' +
      '<rect width="600" height="600" filter="url(#n' + id + ')"/>' +
      // window-light shadow bars
      '<g fill="#3b2a1c" opacity=".13" filter="url(#b' + id + ')"><polygon points="-40,120 640,-80 640,-10 -40,190"/><polygon points="-40,420 640,220 640,300 -40,500"/></g>' +
      // cup shadow
      '<ellipse cx="' + (cx + 34) + '" cy="' + (cy + 40) + '" rx="' + (R + 6) + '" ry="' + (R + 2) + '" fill="#2a1d12" opacity=".28" filter="url(#b' + id + ')"/>';
    if (!d.glass) {
      s += '<rect x="' + (cx + R - 18) + '" y="' + (cy - 26) + '" width="' + (R * 0.62) + '" height="52" rx="26" fill="url(#k' + id + ')"/>' +
        '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" fill="url(#k' + id + ')"/>' +
        '<circle cx="' + cx + '" cy="' + cy + '" r="' + (r + 6) + '" fill="#d8cfc3"/>';
    } else {
      s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" fill="#ffffff" opacity=".45"/>' +
        '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" fill="none" stroke="#ffffff" stroke-width="5" opacity=".8"/>';
    }
    s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="url(#l' + id + ')"/>';
    var foam = '#f6ead9';
    if (d.art === 'heart') {
      s += '<g filter="url(#s' + id + ')" fill="' + foam + '" opacity=".95"><path d="M300 395 C 225 345 205 300 225 268 C 245 238 285 245 300 275 C 315 245 355 238 375 268 C 395 300 375 345 300 395 Z"/></g>' +
        '<path d="M300 395 L300 230" stroke="' + d.liquid[1] + '" stroke-width="3" opacity=".5"/>';
    } else if (d.art === 'rosetta') {
      s += '<g fill="none" stroke="' + foam + '" stroke-linecap="round" filter="url(#s' + id + ')">';
      for (var i = 0; i < 6; i++) { var w = 78 - i * 10, y = 380 - i * 26; s += '<path d="M' + (300 - w) + ' ' + y + ' Q300 ' + (y - 46) + ' ' + (300 + w) + ' ' + y + '" stroke-width="' + (16 - i) + '"/>'; }
      s += '<circle cx="300" cy="210" r="16" fill="' + foam + '" stroke="none"/></g><path d="M300 400 L300 205" stroke="' + d.liquid[1] + '" stroke-width="3" opacity=".55"/>';
    } else if (d.art === 'cocoa' || d.art === 'cocoa2' || d.art === 'spice') {
      var col = d.art === 'spice' ? '#8a5126' : '#4a2a17', n = 90;
      if (d.art === 'cocoa') s += '<circle cx="300" cy="300" r="' + (r - 30) + '" fill="#ffffff" opacity=".35" filter="url(#b' + id + ')"/>';
      if (d.art === 'cocoa2') s += '<circle cx="300" cy="300" r="' + (r - 40) + '" fill="#f3e6d4" opacity=".9" filter="url(#s' + id + ')"/>';
      for (var j = 0; j < n; j++) { var a = j * 2.399, rr = Math.sqrt(j / n) * (r - 30); s += '<circle cx="' + (300 + Math.cos(a) * rr).toFixed(1) + '" cy="' + (300 + Math.sin(a) * rr).toFixed(1) + '" r="' + (1.5 + (j % 3)) + '" fill="' + col + '" opacity=".55"/>'; }
    } else if (d.art === 'coconut') {
      s += '<circle cx="300" cy="300" r="' + (r - 30) + '" fill="#fffaf2" opacity=".6" filter="url(#b' + id + ')"/>';
      for (var q = 0; q < 70; q++) { var a3 = q * 2.399, r3 = Math.sqrt(q / 70) * (r - 30); s += '<rect x="' + (300 + Math.cos(a3) * r3).toFixed(1) + '" y="' + (300 + Math.sin(a3) * r3).toFixed(1) + '" width="6" height="2.5" rx="1" transform="rotate(' + (q * 37 % 180) + ' ' + (300 + Math.cos(a3) * r3).toFixed(1) + ' ' + (300 + Math.sin(a3) * r3).toFixed(1) + ')" fill="#ffffff" opacity=".9"/>'; }
      s += '<circle cx="300" cy="300" r="22" fill="#c9a25e"/><circle cx="294" cy="294" r="7" fill="#e8cf96" opacity=".8"/>';
    } else if (d.art === 'crema') {
      s += '<circle cx="300" cy="300" r="' + (r - 4) + '" fill="none" stroke="#c78a4f" stroke-width="10" opacity=".55" filter="url(#s' + id + ')"/>';
      for (var k = 0; k < 40; k++) { var a2 = k * 2.399, r2 = Math.sqrt(k / 40) * (r - 20); s += '<circle cx="' + (300 + Math.cos(a2) * r2).toFixed(1) + '" cy="' + (300 + Math.sin(a2) * r2).toFixed(1) + '" r="' + (1 + (k % 2)) + '" fill="#e2a96d" opacity=".5"/>'; }
    } else if (d.art === 'ice') {
      var cubes = [[250, 250, 15], [345, 265, -20], [290, 340, 30], [215, 330, -10], [360, 345, 8]];
      cubes.forEach(function (c) { s += '<rect x="' + (c[0] - 34) + '" y="' + (c[1] - 34) + '" width="68" height="68" rx="16" transform="rotate(' + c[2] + ' ' + c[0] + ' ' + c[1] + ')" fill="#ffffff" opacity=".42" stroke="#ffffff" stroke-opacity=".7" stroke-width="2"/>'; });
      if (type === 'iced') s += '<path d="M220 300 C 260 260 330 330 380 290" stroke="#f6ead9" stroke-width="18" fill="none" opacity=".55" filter="url(#s' + id + ')"/>';
    }
    // rim highlight
    s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + (R - 2) + '" fill="none" stroke="#ffffff" stroke-width="2" opacity=".7"/>';
    return s + '</svg>';
  }
  document.querySelectorAll('[data-cup]').forEach(function (el) { el.innerHTML = cupSVG(el.getAttribute('data-cup')); });

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector('.nav__toggle');
  if (toggle) toggle.addEventListener('click', function () {
    var open = doc.classList.toggle('menu-open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* ---------- Open now status + today's hours (edit HOURS when Vani confirms) ---------- */
  // 0 = Sunday ... 6 = Saturday ; [open, close] in 24h, null = closed
  var HOURS = { 0: [7, 16], 1: [7, 17], 2: [7, 17], 3: [7, 17], 4: [7, 17], 5: [7, 17], 6: [7, 17] };
  function fmt(h) { var ap = h >= 12 ? 'pm' : 'am'; var x = h % 12 || 12; return x + ' ' + ap; }
  var now = new Date(), day = now.getDay(), hr = now.getHours() + now.getMinutes() / 60, today = HOURS[day];
  var isOpen = today && hr >= today[0] && hr < today[1];
  document.querySelectorAll('[data-open]').forEach(function (el) {
    var txt;
    if (isOpen) txt = 'Open today until ' + fmt(today[1]);
    else if (today && hr < today[0]) txt = 'Opens today at ' + fmt(today[0]);
    else { var nd = (day + 1) % 7; txt = 'Closed now · opens ' + (HOURS[nd] ? fmt(HOURS[nd][0]) : 'soon'); }
    el.innerHTML = '<span class="dot' + (isOpen ? '' : ' closed') + '"></span>' + txt;
  });
  document.querySelectorAll('.hours tr[data-day="' + day + '"]').forEach(function (tr) { tr.classList.add('today'); });

  /* ---------- Scroll reveal (fade up 32px, staggered) ---------- */
  document.querySelectorAll('[data-stagger]').forEach(function (group) {
    var step = parseFloat(group.getAttribute('data-stagger')) || 0.08;
    group.querySelectorAll(':scope > [data-reveal]').forEach(function (el, i) { el.style.setProperty('--d', (i * step).toFixed(2) + 's'); });
  });
  var items = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else { items.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- Parallax: images drift slower than the page ---------- */
  var parEls = [].slice.call(document.querySelectorAll('.ph.par > img, .footer__bg'));
  function parallax() {
    var vh = innerHeight;
    parEls.forEach(function (img) {
      var box = img.parentElement.getBoundingClientRect();
      if (box.bottom < -100 || box.top > vh + 100) return;
      var p = (box.top + box.height / 2 - vh / 2) / (vh / 2 + box.height / 2); // -1..1
      p = Math.max(-1, Math.min(1, p));
      var amt = img.classList.contains('footer__bg') ? 0.11 : 0.09;
      img.style.transform = 'translate3d(0,' + (p * amt * box.height).toFixed(1) + 'px,0)';
    });
  }
  if (parEls.length && !reduce) {
    if (window.__lenis) window.__lenis.on('scroll', parallax);
    else window.addEventListener('scroll', function () { requestAnimationFrame(parallax); }, { passive: true });
    window.addEventListener('resize', parallax); parallax();
  }

  /* ---------- Menu tabs: highlight the section in view ---------- */
  var tabs = document.querySelectorAll('.tabs a');
  if (tabs.length && 'IntersectionObserver' in window) {
    var map = {};
    tabs.forEach(function (t) { map[t.getAttribute('href').slice(1)] = t; });
    var cats = document.querySelectorAll('.menu-cat');
    var to = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          tabs.forEach(function (t) { t.classList.remove('active'); });
          var t = map[e.target.id]; if (t) { t.classList.add('active'); t.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' }); }
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    cats.forEach(function (c) { to.observe(c); });
  }

  /* ---------- FAQ: smooth open/close ---------- */
  document.querySelectorAll('.faq details').forEach(function (det) {
    var sum = det.querySelector('summary'), body = det.querySelector('.faq__a');
    if (det.open) body.style.height = 'auto';
    sum.addEventListener('click', function (ev) {
      ev.preventDefault();
      if (det.open) {
        body.style.height = body.scrollHeight + 'px';
        requestAnimationFrame(function () { body.style.height = '0px'; });
        body.addEventListener('transitionend', function f() { det.open = false; body.removeEventListener('transitionend', f); });
        sum.setAttribute('aria-expanded', 'false');
      } else {
        det.open = true;
        body.style.height = body.scrollHeight + 'px';
        body.addEventListener('transitionend', function f() { body.style.height = 'auto'; body.removeEventListener('transitionend', f); });
        sum.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ---------- Contact form status (after PHP redirect) ---------- */
  var msg = document.querySelector('.form__msg');
  if (msg) {
    var q = location.search;
    if (/sent=1/.test(q)) { msg.hidden = false; msg.className = 'form__msg ok'; msg.textContent = "Thank you! Your message has been sent. We'll get back to you soon."; }
    else if (/error=1/.test(q)) { msg.hidden = false; msg.className = 'form__msg err'; msg.textContent = 'Sorry, something went wrong. Please check your details or call us on 0452 209 929.'; }
    var form = msg.closest('form');
    form.addEventListener('submit', function (e) {
      if (!form.checkValidity()) { e.preventDefault(); msg.hidden = false; msg.className = 'form__msg err'; msg.textContent = 'Please fill in your name, a valid email and your message.'; }
    });
  }

  /* ---------- Footer word: split into letters that rise in ---------- */
  document.querySelectorAll('[data-letters]').forEach(function (el) {
    var t = el.textContent; el.textContent = '';
    t.split('').forEach(function (c, i) {
      var s = document.createElement('span');
      s.className = 'ch' + (c === ' ' ? ' sp' : '');
      s.textContent = c === ' ' ? '' : c;
      s.style.transitionDelay = (i * 0.035).toFixed(3) + 's';
      el.appendChild(s);
    });
    var box = el.parentElement;
    if ('IntersectionObserver' in window && !reduce) {
      var o = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { box.classList.add('in'); o.disconnect(); } }); }, { threshold: 0.3 });
      o.observe(box);
    } else box.classList.add('in');
  });

  /* ---------- Fit the footer word to the full width ---------- */
  function fit() {
    document.querySelectorAll('[data-fit]').forEach(function (el) {
      var box = el.parentElement, cs = getComputedStyle(box);
      var avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
      var size = 100;
      el.style.display = 'inline-block';
      for (var i = 0; i < 4; i++) {
        el.style.fontSize = size + 'px';
        var w = el.getBoundingClientRect().width;
        if (!w) break;
        size = size * avail / w;
      }
      el.style.fontSize = Math.floor(size * 100) / 100 + 'px';
      el.style.display = 'block';
    });
  }
  fit(); window.addEventListener('resize', fit); window.addEventListener('load', fit); setTimeout(fit, 800);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);

  /* ---------- Hero video: loop only the clean part of the clip; respect reduced motion ---------- */
  document.querySelectorAll('.hero__video').forEach(function (v) {
    var a = parseFloat(v.dataset.loopStart) || 0, z = parseFloat(v.dataset.loopEnd) || 0;
    if (reduce) { v.removeAttribute('autoplay'); v.pause(); return; }
    if (z) v.addEventListener('timeupdate', function () { if (v.currentTime >= z) v.currentTime = a; });
    var pr = v.play(); if (pr && pr.catch) pr.catch(function () {});
  });

  /* ---------- Coffee video: load when near, open up as you scroll, pause when away ---------- */
  document.querySelectorAll('.vid').forEach(function (sec) {
    var v = sec.querySelector('video'), frame = sec.querySelector('.vid__frame'), loaded = false;
    function load() { if (loaded) return; loaded = true; v.src = innerWidth > 1000 ? v.dataset.srcLg : v.dataset.srcSm; v.load(); }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting) { load(); if (!reduce) { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); } }
          else v.pause();
        });
      }, { rootMargin: '300px 0px' }).observe(sec);
    } else { load(); }
    function open() {
      var r = sec.getBoundingClientRect(), vh = innerHeight;
      var p = Math.max(0, Math.min(1, (vh - r.top) / (vh * 0.9)));
      if (reduce) p = 1;
      frame.style.setProperty('--vi-y', (6 * (1 - p)).toFixed(2) + '%');
      frame.style.setProperty('--vi-x', (8 * (1 - p)).toFixed(2) + '%');
      frame.style.setProperty('--vi-s', (1 + 0.12 * (1 - p)).toFixed(3));
    }
    if (window.__lenis) window.__lenis.on('scroll', open); else window.addEventListener('scroll', function () { requestAnimationFrame(open); }, { passive: true });
    window.addEventListener('resize', open); open();
  });

  /* ---------- Drag-to-scroll gallery ---------- */
  document.querySelectorAll('.gal__track').forEach(function (t) {
    var down = false, sx = 0, sl = 0;
    t.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse') return; down = true; sx = e.clientX; sl = t.scrollLeft; t.classList.add('drag'); });
    window.addEventListener('pointerup', function () { down = false; t.classList.remove('drag'); });
    t.addEventListener('pointermove', function (e) { if (!down) return; t.scrollLeft = sl - (e.clientX - sx); });
    t.setAttribute('data-lenis-prevent-wheel', '');
  });

  /* ---------- Footer year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
