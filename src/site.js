const currentLang = document.documentElement.lang || 'en';

/* ── Mobile nav drawer ── */
const ham = document.getElementById('ham');
const mobNav = document.getElementById('mob-nav');
function setMenu(open) {
  if (!ham || !mobNav) return;
  mobNav.classList.toggle('open', open);
  ham.classList.toggle('open', open);
  ham.setAttribute('aria-expanded', String(open));
  ham.setAttribute('aria-label', open ? ham.dataset.labelClose : ham.dataset.labelOpen);
  document.body.classList.toggle('menu-open', open);
  document.body.style.overflow = open ? 'hidden' : '';           // lock the page behind the drawer
  if (open) setTimeout(() => { const f = mobNav.querySelector('.mob-link'); if (f) f.focus({ preventScroll: true }); }, 60);
}
if (ham) ham.addEventListener('click', () => setMenu(!mobNav.classList.contains('open')));
function closeMob() { setMenu(false); }
document.addEventListener('keydown', e => {
  if (!mobNav || !mobNav.classList.contains('open')) return;
  if (e.key === 'Escape') { setMenu(false); ham.focus(); return; }
  if (e.key !== 'Tab') return;                                    // keep keyboard focus inside the open drawer
  const f = [ham, ...mobNav.querySelectorAll('a[href]')], first = f[0], last = f[f.length - 1];
  if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
  else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
});
window.addEventListener('resize', () => { if (window.innerWidth > 680) setMenu(false); });

/* ── Scroll reveal ── */
const obs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('on'); obs.unobserve(e.target); } });
}, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });
document.querySelectorAll('.rev').forEach(el => obs.observe(el));


/* ── Char counter ── */
const msgArea = document.getElementById('f-msg');
const charCount = document.getElementById('char-count');
if (msgArea) {
  msgArea.addEventListener('input', () => {
    charCount.textContent = msgArea.value.length;
    charCount.style.color = msgArea.value.length > 550 ? '#ff6b6b' : 'var(--dim)';
  });
}

/* ── Contact form submit — WhatsApp redirect ── */
const contactForm = document.getElementById('contact-form');
if (contactForm) contactForm.addEventListener('submit', function(e) {
  e.preventDefault();
  const btn   = document.getElementById('form-submit');
  const name  = document.getElementById('f-name').value.trim();
  const email = document.getElementById('f-email').value.trim();
  const biz   = document.getElementById('f-biz').value.trim();
  const svc   = document.getElementById('f-service').value;
  const msg   = document.getElementById('f-msg').value.trim();

  const consent = document.getElementById('f-consent');
  const consentOk = !consent || consent.checked;

  if (!name || !email || !svc || !msg || !consentOk) {
    if (!consentOk) {
      const lbl = consent.nextElementSibling;
      lbl.style.color = '#ff6b6b';
      consent.addEventListener('change', () => { lbl.style.color = ''; }, { once: true });
    }
    [['f-name',name],['f-email',email],['f-service',svc],['f-msg',msg]].forEach(([id,val]) => {
      if (!val) {
        const el = document.getElementById(id);
        el.style.borderColor = '#ff6b6b';
        el.style.boxShadow = '0 0 0 3px rgba(255,107,107,.12)';
        el.addEventListener('input', () => { el.style.borderColor = ''; el.style.boxShadow = ''; }, { once: true });
      }
    });
    return;
  }

  const MSG = {
    en: { hello:'Hello Upmarkpro!',  name:'Name: ', email:'Email: ', biz:'Business: ',   svc:'Service: ',  msg:'Message:\n' },
    fr: { hello:'Bonjour Upmarkpro !', name:'Nom : ', email:'Email : ', biz:'Entreprise : ', svc:'Service : ', msg:'Message :\n' },
    it: { hello:'Ciao Upmarkpro!',   name:'Nome: ', email:'Email: ', biz:'Attività: ',   svc:'Servizio: ', msg:'Messaggio:\n' },
  }[currentLang] || { hello:'Hello Upmarkpro!', name:'Name: ', email:'Email: ', biz:'Business: ', svc:'Service: ', msg:'Message:\n' };
  const lines = [
    MSG.hello,
    '',
    MSG.name  + name,
    MSG.email + email,
    biz ? MSG.biz + biz : null,
    MSG.svc   + svc,
    '',
    MSG.msg   + msg,
  ].filter(l => l !== null).join('\n');

  const waUrl = 'https://wa.me/393882576789?text=' + encodeURIComponent(lines);

  btn.classList.add('loading');
  btn.disabled = true;

  window.open(waUrl, '_blank');

  setTimeout(() => {
    document.getElementById('contact-form').style.display = 'none';
    document.getElementById('form-success').classList.add('show');
  }, 600);
});

/* ── Process steps staggered scroll reveal ── */
const stepsObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.querySelectorAll('.ap-step').forEach((step, i) => {
      setTimeout(() => step.classList.add('step-visible'), i * 130);
    });
    stepsObs.unobserve(e.target);
  });
}, { threshold: 0.15 });
const apSteps = document.querySelector('.ap-steps');
if (apSteps) stepsObs.observe(apSteps);

/* ── Nav darken + back-to-top ── */
const backTop = document.getElementById('back-top');
window.addEventListener('scroll', () => {
  const y = window.scrollY;
  document.getElementById('nav').style.background =
    y > 24 ? 'rgba(10,14,20,.96)' : 'rgba(10,14,20,.6)';
  backTop.classList.toggle('visible', y > 400);
}, { passive: true });

/* ── Form reset ── */
const formResetBtn = document.getElementById('form-reset-btn');
if (formResetBtn) formResetBtn.addEventListener('click', () => {
  document.getElementById('contact-form').reset();
  document.getElementById('contact-form').style.display = '';
  const btn = document.getElementById('form-submit');
  btn.disabled = false;
  btn.classList.remove('loading');
  document.getElementById('form-success').classList.remove('show');
});

/* ── Motion/input capability checks ── */
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const fineHover     = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
const hasGsap       = typeof gsap !== 'undefined';

/* ── Kinetic watermark strip ── */
(function initKinetic() {
  const track = document.getElementById('kinetic-track');
  if (!track) return;
  let html = '';
  for (let i = 0; i < 10; i++) {
    html += `<span${i % 3 === 0 ? ' class="accent"' : ''}>MORE CALLS</span><span>•</span>`;
  }
  track.innerHTML = html;
  if (hasGsap && !reducedMotion) {
    // scroll-scrubbed drift: a few lines instead of a separate plugin download
    const strip = track.closest('.kinetic-strip') || track;
    const xTo = gsap.quickTo(track, 'xPercent', { duration: 1, ease: 'none' });
    let queued = false;
    const update = () => {
      queued = false;
      const r = strip.getBoundingClientRect(), vh = window.innerHeight;
      xTo(-14 * Math.min(1, Math.max(0, (vh - r.top) / (vh + r.height))));
    };
    window.addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(update); } }, { passive: true });
    requestAnimationFrame(update);      // first measurement after the browser's own first layout
  }
})();

/* ── Equal-height service cards: align description + chip rows within each row of cards ── */
(function equalizeServices() {
  const cards = [...document.querySelectorAll('#services .svc')];
  if (cards.length < 2) return;
  const parts = [c => c.querySelector(':scope > p'), c => c.querySelector('.svc-chips')];
  function run() {
    parts.forEach(get => cards.forEach(c => { const el = get(c); if (el) el.style.minHeight = ''; }));
    if (window.innerWidth <= 680) return; // single column
    const rows = {};
    cards.forEach(c => { (rows[c.offsetTop] = rows[c.offsetTop] || []).push(c); });
    // read every height first, then write them: one layout pass instead of one per element
    const plan = [];
    Object.values(rows).forEach(group => parts.forEach(get => {
      const els = group.map(get).filter(Boolean);
      plan.push([els, Math.max(...els.map(el => el.getBoundingClientRect().height))]);
    }));
    plan.forEach(([els, h]) => els.forEach(el => { el.style.minHeight = h + 'px'; }));
  }
  let t;
  window.addEventListener('resize', () => { clearTimeout(t); t = setTimeout(run, 120); });
  window.addEventListener('load', run);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(run);
  requestAnimationFrame(run);
})();

/* ── Cursor spotlight (desktop, fine pointer, motion allowed) ── */
(function initCursorGlow() {
  if (!hasGsap || !fineHover || reducedMotion) return;
  const glow = document.createElement('div');
  glow.className = 'cursor-glow';
  glow.setAttribute('aria-hidden', 'true');
  document.body.appendChild(glow);
  const xTo = gsap.quickTo(glow, 'x', { duration: 0.6, ease: 'power3' });
  const yTo = gsap.quickTo(glow, 'y', { duration: 0.6, ease: 'power3' });
  window.addEventListener('mousemove', e => { glow.classList.add('on'); xTo(e.clientX); yTo(e.clientY); }, { passive: true });
  document.addEventListener('mouseleave', () => glow.classList.remove('on'));
})();

/* ── Kinetic monospace scrambler on section labels (hover) ── */
(function initScramble() {
  if (!fineHover || reducedMotion) return;
  const CH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/_<>#';
  document.querySelectorAll('.eyebrow, .rs-header-label, .calc-stat-label, .work-meta-count').forEach(el => {
    if (el.children.length) return;
    const text = el.textContent;
    let raf = 0;
    el.addEventListener('mouseenter', () => {
      if (raf) return;
      const t0 = performance.now(), dur = 520;
      (function tick(now) {
        const p = Math.min(1, (now - t0) / dur), reveal = Math.floor(p * text.length);
        el.textContent = text.split('').map((c, i) => (i < reveal || c === ' ' || (i === 0 && c === '/')) ? c : CH[(Math.random() * CH.length) | 0]).join('');
        if (p < 1) raf = requestAnimationFrame(tick); else { el.textContent = text; raf = 0; }
      })(t0);
    });
  });
})();

/* ── Sticky mobile quick-action dock: shown after the hero, hidden while the contact form is in view ── */
(function initDock() {
  const dock = document.getElementById('m-dock');
  if (!dock) return;
  const hero = document.getElementById('hero');
  let pastTop = false, contactIn = false;
  const sync = () => {
    const on = pastTop && !contactIn;
    dock.classList.toggle('show', on);
    document.body.classList.toggle('dock-on', on);
  };
  if (hero) new IntersectionObserver(([e]) => { pastTop = !e.isIntersecting && e.boundingClientRect.top < 0; sync(); }).observe(hero);
  else { const onScroll = () => { pastTop = window.scrollY > 480; sync(); }; window.addEventListener('scroll', onScroll, { passive: true }); onScroll(); }
  const contactForm = document.getElementById('contact-form');
  if (contactForm) new IntersectionObserver(([e]) => { contactIn = e.isIntersecting; sync(); }, { rootMargin: '0px 0px -25% 0px' }).observe(contactForm);
})();

/* ── Magnetic CTAs ── */
if (hasGsap && fineHover && !reducedMotion) {
  document.querySelectorAll('[data-magnetic]').forEach(btn => {
    const xTo = gsap.quickTo(btn, 'x', { duration: 0.4, ease: 'power3' });
    const yTo = gsap.quickTo(btn, 'y', { duration: 0.4, ease: 'power3' });
    btn.addEventListener('mousemove', e => {
      const r = btn.getBoundingClientRect();
      xTo((e.clientX - r.left - r.width / 2) * 0.35);
      yTo((e.clientY - r.top - r.height / 2) * 0.35);
    });
    btn.addEventListener('mouseleave', () => { xTo(0); yTo(0); });
  });
}

/* ── Lead calculator ── */
function calcCurrencyFmt() {
  return new Intl.NumberFormat(({ fr: 'fr-FR', it: 'it-IT' })[currentLang] || 'en-GB', { style: 'currency', currency: 'EUR', maximumFractionDigits: 0, useGrouping: 'always' });
}
function calcAnimateNumber(el, target, fmt) {
  const prev = el._calcVal ?? target;
  if (!hasGsap || reducedMotion) { el.textContent = fmt.format(Math.round(target)); el._calcVal = target; return; }
  const obj = { v: prev };
  gsap.to(obj, {
    v: target, duration: 0.5, ease: 'power2.out',
    onUpdate: () => { el.textContent = fmt.format(Math.round(obj.v)); },
    onComplete: () => { el._calcVal = target; }
  });
}
function calcLocale() { return ({ fr: 'fr-FR', it: 'it-IT' })[currentLang] || 'en-GB'; }
// Hypothetical model (shown as such on the page): ~15% of mobile visitors leave per second beyond the first
const CALC_LEAVE_PER_SEC = 0.15, CALC_FAST_SECONDS = 1.5;
function calcStay(sec) { return Math.pow(1 - CALC_LEAVE_PER_SEC, Math.max(0, sec - 1)); }
let calcState = null;
function calcUpdate() {
  const callsInput = document.getElementById('calc-calls');
  const valueInput = document.getElementById('calc-value');
  if (!callsInput || !valueInput) return;
  const calls = +callsInput.value;
  const value = +valueInput.value;
  const fmt = calcCurrencyFmt();
  document.getElementById('calc-calls-val').textContent = calls;
  document.getElementById('calc-value-val').textContent = fmt.format(value);
  const CLOSE_RATE = 0.4, WEEKS_PER_MONTH = 4.33;
  const monthly = calls * WEEKS_PER_MONTH * value * CLOSE_RATE;
  calcAnimateNumber(document.getElementById('calc-monthly'), monthly, fmt);
  calcAnimateNumber(document.getElementById('calc-annual'), monthly * 12, fmt);

  const speedInput = document.getElementById('calc-speed');
  let speedTxt = '';
  if (speedInput) {
    const sec = +speedInput.value;
    const num = new Intl.NumberFormat(calcLocale(), { minimumFractionDigits: 1, maximumFractionDigits: 1 });
    const pct = new Intl.NumberFormat(calcLocale(), { style: 'percent', maximumFractionDigits: 0 });
    speedTxt = num.format(sec) + ' s';
    document.getElementById('calc-speed-val').textContent = speedTxt;
    const you = calcStay(sec), fast = calcStay(CALC_FAST_SECONDS);
    document.getElementById('calc-bar-you').style.width = (you * 100).toFixed(1) + '%';
    document.getElementById('calc-bar-fast').style.width = (fast * 100).toFixed(1) + '%';
    document.getElementById('calc-bar-you-val').textContent = pct.format(you);
    document.getElementById('calc-bar-fast-val').textContent = pct.format(fast);
  }
  calcState = { calls, value: fmt.format(value), monthly: fmt.format(Math.round(monthly)), annual: fmt.format(Math.round(monthly * 12)), speed: speedTxt };
}

/* Export the audit to WhatsApp (pre-filled with the exact slider values) */
const CALC_MSG = {
  en: d => `Hello Upmarkpro! I ran the leak audit:\n- Missed calls per week: ${d.calls}\n- Average job value: ${d.value}\n- Lost per month: ${d.monthly}\n- Lost per year: ${d.annual}\n- Mobile load time: ${d.speed}\n\nI'd like to talk about fixing this.`,
  fr: d => `Bonjour Upmarkpro ! J'ai fait l'audit :\n- Appels manqués par semaine : ${d.calls}\n- Valeur moyenne d'un travail : ${d.value}\n- Perdu par mois : ${d.monthly}\n- Perdu par an : ${d.annual}\n- Temps de chargement mobile : ${d.speed}\n\nJ'aimerais en parler.`,
  it: d => `Ciao Upmarkpro! Ho provato lo strumento:\n- Chiamate perse a settimana: ${d.calls}\n- Valore medio di un lavoro: ${d.value}\n- Perso al mese: ${d.monthly}\n- Perso all'anno: ${d.annual}\n- Tempo di caricamento da telefono: ${d.speed}\n\nVorrei parlarne.`,
};
const calcExport = document.getElementById('calc-export');
if (calcExport) calcExport.addEventListener('click', () => {
  calcUpdate();
  const msg = (CALC_MSG[currentLang] || CALC_MSG.en)(calcState);
  window.open('https://wa.me/393882576789?text=' + encodeURIComponent(msg), '_blank', 'noopener');
});
['calc-calls', 'calc-value', 'calc-speed'].forEach(id => {
  const el = document.getElementById(id);
  if (el) el.addEventListener('input', calcUpdate);
});

/* ── Concept showroom: desktop / mobile device viewer with feature pins ──
   Pins only mark things that exist on the captured concept sites (positions measured from the live DOM).
   Coordinates are % of the captured image (desktop 1440 x 2700 css px, mobile 390 x 1700 css px). */
(function initShowroom() {
  const root = document.getElementById('showroom');
  if (!root || !window.CONCEPTS) return;

  const DATA = [
    { id: 'ifct',         url: 'https://ifct.vercel.app/',                             schema: 'EducationalOrganization',
      d: [{ t: 'hdr', x: 91.81, y: 0.89 }, { t: 'wa', x: 25.97, y: 21.41 }],        m: [{ t: 'wa', x: 94.36, y: 29.82 }] },
    { id: 'digitalpower', url: 'https://digitalpower-seven.vercel.app/',               schema: 'ProfessionalService',
      d: [{ t: 'phone', x: 80.62, y: 0.81 }, { t: 'hero', x: 26.67, y: 22.33 }],        m: [{ t: 'hero', x: 69.74, y: 31.0 }], bar: { w: 585, h: 110, hpct: 8.65 } },
    { id: 'dental',       url: 'https://cabinet-dentaire-drmeriem-hamza.vercel.app/', schema: 'Dentist',
      d: [{ t: 'hdr', x: 87.92, y: 0.81 }, { t: 'hero', x: 24.65, y: 18.59 }],        m: [{ t: 'hero', x: 94.36, y: 23.88 }],    bar: { w: 585, h: 110, hpct: 8.65 } },
    { id: 'ldbatiment',   url: 'https://ld-batiment-carrelage.vercel.app/',            schema: 'HomeAndConstructionBusiness',
      d: [{ t: 'hdr', x: 89.58, y: 0.74 }, { t: 'hero', x: 44.1, y: 23.0 }],         m: [{ t: 'hero', x: 94.36, y: 32.12 }] },
    { id: 'bilelcoiff',   url: 'https://bilelcoiff.vercel.app/',                       schema: 'HairSalon',
      d: [{ t: 'phone', x: 76.46, y: 1.56 }, { t: 'hero', x: 48.89, y: 21.52 }],     m: [{ t: 'hero', x: 93.33, y: 26.88 }],    bar: { w: 585, h: 100, hpct: 7.94 } },
    { id: 'meryouma',     url: 'https://meryouma-events-3l2d.vercel.app/',             schema: 'EventPlanner',
      d: [{ t: 'hdr', x: 89.58, y: 1.0 }, { t: 'hero', x: 29.38, y: 24.52 }],      m: [{ t: 'hero', x: 92.31, y: 44.41 }],    bar: { w: 585, h: 114, hpct: 9 } },
  ];

  const S = {
    en: {
      group: 'Concept projects', desk: 'Desktop', mob: 'Mobile', scroll: 'Scrollable preview of the concept site',
      hint: 'Scroll inside the screen · tap the pins',
      concept: "Concept site — not the business's official website.",
      verified: 'On this concept',
      f_cta: 'Call, booking or WhatsApp buttons', f_bar: 'Sticky action bar on mobile', f_schema: s => `Local business structured data (${s})`,
      open: 'Open live demo ↗', req: 'Request a site like this on WhatsApp',
      msg: t => `Hello! I'd like a site like your "${t}".`,
      alt: (t, dev) => `Preview of the concept site — ${t} (${dev})`,
      pin: { hdr: 'Call-to-action always in the header', phone: 'Phone number one tap away', hero: 'Main action above the fold', wa: 'WhatsApp action above the fold', bar: 'Sticky action bar on mobile' },
    },
    fr: {
      group: 'Projets démonstratifs', desk: 'Ordinateur', mob: 'Mobile', scroll: 'Aperçu défilant du site concept',
      hint: "Faites défiler l'écran · touchez les repères",
      concept: "Site concept — ce n'est pas le site officiel de cette entreprise.",
      verified: 'Sur ce concept',
      f_cta: "Boutons d'appel, de réservation ou WhatsApp", f_bar: 'Barre d\'action fixe sur mobile', f_schema: s => `Données structurées d'entreprise locale (${s})`,
      open: 'Ouvrir la démo ↗', req: 'Demander un site comme celui-ci sur WhatsApp',
      msg: t => `Bonjour ! J'aimerais un site comme votre « ${t} ».`,
      alt: (t, dev) => `Aperçu du site concept — ${t} (${dev})`,
      pin: { hdr: "Bouton d'action toujours dans l'en-tête", phone: 'Numéro de téléphone à un toucher', hero: "Action principale dès l'arrivée", wa: "Action WhatsApp dès l'arrivée", bar: "Barre d'action fixe sur mobile" },
    },
    it: {
      group: 'Progetti dimostrativi', desk: 'Desktop', mob: 'Mobile', scroll: 'Anteprima scorrevole del sito concept',
      hint: 'Scorri nello schermo · tocca i punti',
      concept: "Sito concept — non è il sito ufficiale dell'attività.",
      verified: 'In questo concept',
      f_cta: 'Pulsanti per chiamare, prenotare o scrivere su WhatsApp', f_bar: 'Barra di azione fissa su mobile', f_schema: s => `Dati strutturati per attività locale (${s})`,
      open: 'Apri la demo ↗', req: 'Richiedi un sito come questo su WhatsApp',
      msg: t => `Ciao! Vorrei un sito come il vostro «${t}».`,
      alt: (t, dev) => `Anteprima del sito concept — ${t} (${dev})`,
      pin: { hdr: 'Pulsante di azione sempre nell\'intestazione', phone: 'Numero di telefono a un tocco', hero: 'Azione principale subito visibile', wa: 'Azione WhatsApp subito visibile', bar: 'Barra di azione fissa su mobile' },
    },
  }[currentLang] || null;
  if (!S) return;

  const items = DATA.map(p => {
    const c = window.CONCEPTS[p.id], L = (c && c[currentLang]) || {};
    return { ...p, title: L.title || p.id, niche: L.niche || '' };
  });

  const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
  const state = { i: 0, device: 'desktop' };

  root.innerHTML = `
    <div class="sr-top">
      <div class="sr-tabs" role="group" aria-label="${esc(S.group)}">
        ${items.map((p, i) => `<button type="button" class="sr-tab" data-i="${i}" aria-pressed="false">${esc(p.niche)}</button>`).join('')}
      </div>
      <div class="sr-toggle" role="group" aria-label="${esc(S.desk)} / ${esc(S.mob)}">
        <button type="button" class="sr-dev" data-dev="desktop" aria-pressed="true">${esc(S.desk)}</button>
        <button type="button" class="sr-dev" data-dev="mobile" aria-pressed="false">${esc(S.mob)}</button>
      </div>
    </div>
    <div class="sr-body">
      <div class="sr-stage">
        <div class="sr-device sr-desktop">
          <div class="sr-chrome" aria-hidden="true"><i></i><i></i><i></i><span class="sr-url"></span></div>
          <div class="sr-screen">
            <div class="sr-scroll" tabindex="0" role="region" aria-label="${esc(S.scroll)}">
              <div class="sr-canvas"><img width="1000" height="1875" decoding="async" loading="lazy" alt=""></div>
            </div>
          </div>
        </div>
        <div class="sr-device sr-mobile">
          <div class="sr-screen">
            <span class="sr-notch" aria-hidden="true"></span>
            <div class="sr-scroll" tabindex="0" role="region" aria-label="${esc(S.scroll)}">
              <div class="sr-canvas"><img width="585" height="2550" decoding="async" loading="lazy" alt=""></div>
            </div>
            <div class="sr-fixed"></div>
          </div>
        </div>
      </div>
      <aside class="sr-info">
        <span class="sr-pill"></span>
        <h3 class="sr-title"></h3>
        <p class="sr-note">${esc(S.concept)}</p>
        <p class="sr-note sr-lang"></p>
        <p class="sr-hint">${esc(S.hint)}</p>
        <div class="sr-facts"><p class="sr-facts-h">${esc(S.verified)}</p><ul></ul></div>
        <div class="sr-actions">
          <a class="btn-lime sr-open" target="_blank" rel="noopener" data-magnetic>${esc(S.open)}</a>
          <a class="btn-outline sr-req" target="_blank" rel="noopener">${esc(S.req)}</a>
        </div>
      </aside>
    </div>`;

  const $ = sel => root.querySelector(sel);
  const stage = $('.sr-stage'), info = $('.sr-info');
  const dImg = $('.sr-desktop img'), mImg = $('.sr-mobile img');
  const dCanvas = $('.sr-desktop .sr-canvas'), mCanvas = $('.sr-mobile .sr-canvas'), mFixed = $('.sr-fixed');

  const pinHTML = (type, x, y, extra = '', style = '') => {
    const label = S.pin[type];
    const cls = (x > 60 ? ' tip-l' : x < 22 ? ' tip-r' : '') + (y != null && y < 6 ? ' tip-b' : '');
    const pos = style || `left:${x}%;top:${y}%`;
    return `<button type="button" class="sr-pin${cls}${extra}" style="${pos}" aria-label="${esc(label)}"><span class="sr-dot"></span><span class="sr-tip" role="tooltip">${esc(label)}</span></button>`;
  };

  function fill() {
    const p = items[state.i];
    root.querySelectorAll('.sr-tab').forEach((b, i) => b.setAttribute('aria-pressed', String(i === state.i)));
    root.querySelectorAll('.sr-dev').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.dev === state.device)));
    root.dataset.device = state.device;

    const base = `/assets/projects/${p.id}/`;
    if (state.device === 'desktop') {
      dImg.alt = S.alt(p.title, S.desk);
      dImg.sizes = '(max-width: 680px) 50vw, 700px';   // phones show it ~350px wide: the 640px file is plenty
      dImg.srcset = `${base}desktop-full-640.webp 640w, ${base}desktop-full.webp 1000w`;
      dImg.src = base + 'desktop-full.webp';
      dCanvas.querySelectorAll('.sr-pin').forEach(n => n.remove());
      dCanvas.insertAdjacentHTML('beforeend', p.d.map(q => pinHTML(q.t, q.x, q.y)).join(''));
      dCanvas.parentElement.scrollTop = 0;
      $('.sr-url').textContent = new URL(p.url).host;
    } else {
      mImg.alt = S.alt(p.title, S.mob); mImg.src = base + 'mobile-full.webp';
      mCanvas.querySelectorAll('.sr-pin').forEach(n => n.remove());
      mCanvas.insertAdjacentHTML('beforeend', p.m.map(q => pinHTML(q.t, q.x, q.y)).join(''));
      mFixed.innerHTML = p.bar
        ? `<img class="sr-bar" src="${base}mobile-bar.webp" width="${p.bar.w}" height="${p.bar.h}" alt="" decoding="async" loading="lazy">` +
          pinHTML('bar', 90, null, ' sr-pin-bar tip-l', `left:90%;bottom:${p.bar.hpct}%`)
        : '';
      mCanvas.parentElement.scrollTop = 0;
    }

    $('.sr-pill').textContent = 'Concept · ' + p.niche;
    $('.sr-title').textContent = p.title;
    const note = $('.sr-lang');
    note.textContent = currentLang === 'it' ? 'Sito in francese' : '';
    note.hidden = currentLang !== 'it';
    const facts = [S.f_cta];
    if (p.bar) facts.push(S.f_bar);
    facts.push(S.f_schema(p.schema));
    $('.sr-facts ul').innerHTML = facts.map(f => `<li>${esc(f)}</li>`).join('');
    $('.sr-open').href = p.url;
    $('.sr-req').href = 'https://wa.me/393882576789?text=' + encodeURIComponent(S.msg(p.title));
  }

  function update() {
    if (!hasGsap || reducedMotion) { fill(); return; }
    gsap.to([stage, info], {
      opacity: 0, y: 6, duration: 0.16, ease: 'power1.in',
      onComplete: () => { fill(); gsap.fromTo([stage, info], { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.36, ease: 'power2.out', clearProps: 'transform' }); }
    });
  }

  root.addEventListener('click', e => {
    const tab = e.target.closest('.sr-tab');
    if (tab) { const i = +tab.dataset.i; if (i !== state.i) { state.i = i; update(); } return; }
    const dev = e.target.closest('.sr-dev');
    if (dev) { if (dev.dataset.dev !== state.device) { state.device = dev.dataset.dev; update(); } return; }
    const pin = e.target.closest('.sr-pin');
    root.querySelectorAll('.sr-pin.open').forEach(n => { if (n !== pin) n.classList.remove('open'); });
    if (pin) pin.classList.toggle('open');
  });
  document.addEventListener('click', e => { if (!root.contains(e.target)) root.querySelectorAll('.sr-pin.open').forEach(n => n.classList.remove('open')); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') root.querySelectorAll('.sr-pin.open').forEach(n => n.classList.remove('open')); });

  // the preview button of each Work card selects that concept in the viewer (the "View concept" link opens the live demo)
  document.querySelectorAll('.wcard[data-concept] .wcard-pick').forEach(btn => {
    const i = items.findIndex(p => p.id === btn.closest('.wcard').dataset.concept);
    if (i < 0) return;
    btn.addEventListener('click', () => {
      if (i !== state.i) { state.i = i; update(); }
      root.scrollIntoView({ behavior: reducedMotion ? 'auto' : 'smooth', block: 'start' });
    });
  });

  fill();
})();

/* ── Hero niche switcher: cross-fades the hero mockup to the real capture of the chosen niche ── */
(function initHeroNiches() {
  const wrap = document.getElementById('hero-niches');
  const R = document.querySelector('.hero-right');
  const badge = R && R.querySelector('.hero-card-2');
  if (!wrap || !R || !badge || !window.CONCEPTS) return;

  // Things verified on each concept site (call/booking/WhatsApp elements present in the capture)
  const FACT = {
    en: { ifct: 'WhatsApp enrolment button', digitalpower: 'Phone number in the header', dental: 'Sticky call bar on mobile', ldbatiment: 'Booking button in the header', bilelcoiff: 'Sticky booking bar on mobile', meryouma: 'Sticky call bar on mobile' },
    fr: { ifct: "Bouton d'inscription WhatsApp", digitalpower: "Numéro de téléphone dans l'en-tête", dental: "Barre d'appel fixe sur mobile", ldbatiment: "Bouton de réservation dans l'en-tête", bilelcoiff: 'Barre de réservation fixe sur mobile', meryouma: "Barre d'appel fixe sur mobile" },
    it: { ifct: 'Pulsante di iscrizione su WhatsApp', digitalpower: "Numero di telefono nell'intestazione", dental: 'Barra per chiamare fissa su mobile', ldbatiment: "Pulsante di prenotazione nell'intestazione", bilelcoiff: 'Barra di prenotazione fissa su mobile', meryouma: 'Barra per chiamare fissa su mobile' },
  }[currentLang] || {};
  const TOP = { en: 'On this concept', fr: 'Sur ce concept', it: 'In questo concept' }[currentLang] || 'Concept';
  const ALT = { en: 'Preview of the concept site', fr: 'Aperçu du site concept', it: 'Anteprima del sito concept' }[currentLang] || '';

  const info = {};
  Object.keys(window.CONCEPTS).forEach(id => {
    const L = window.CONCEPTS[id][currentLang];
    if (!L) return;
    info[id] = { id, title: L.title, niche: L.niche, fact: FACT[id] || '' };
  });

  const pills = [...wrap.querySelectorAll('.hn-pill')];
  const collage = [...R.querySelectorAll('.hv-card')];
  const bTop = badge.querySelector('.hc-top'), bVal = badge.querySelector('.hc-val');
  const orig = { top: bTop.textContent, val: bVal.textContent };
  const anim = hasGsap && !reducedMotion;

  const solo = document.createElement('div');
  solo.className = 'hv-card hv-card-solo';
  solo.setAttribute('aria-hidden', 'true');
  solo.innerHTML = '<div class="hv-img"><img width="960" height="600" decoding="async" alt=""></div><div class="hv-info"><span class="hv-cat">Concept</span><span class="hv-name"></span></div>';
  R.insertBefore(solo, badge);
  const sImg = solo.querySelector('img'), sCat = solo.querySelector('.hv-cat'), sName = solo.querySelector('.hv-name');

  const prev = document.createElement('div');           // compact version for screens where the hero mockup is hidden
  prev.className = 'hero-preview'; prev.hidden = true;
  prev.innerHTML = '<img width="960" height="600" decoding="async" alt=""><div class="hp-cap"><span class="sr-pill"></span><span class="hp-fact"></span></div>';
  wrap.insertAdjacentElement('afterend', prev);
  const pImg = prev.querySelector('img'), pPill = prev.querySelector('.sr-pill'), pFact = prev.querySelector('.hp-fact');

  const swapSolo = p => {
    const src = `/assets/projects/${p.id}/hero.webp`;
    sImg.src = src; sImg.alt = `${ALT} — ${p.title}`;
    sCat.textContent = 'Concept · ' + p.niche; sName.textContent = p.title;
    pImg.src = src; pImg.alt = sImg.alt; pPill.textContent = 'Concept · ' + p.niche; pFact.textContent = p.fact;
  };
  const swapBadge = p => { bTop.textContent = p ? TOP : orig.top; bVal.textContent = p ? p.fact : orig.val; };

  let cur = 'all';
  function go(id) {
    if (id === cur) return;
    const fromAll = cur === 'all';
    cur = id;
    pills.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.niche === id)));
    const p = id === 'all' ? null : info[id];
    R.classList.toggle('is-solo', !!p);

    if (!anim) {
      if (p) swapSolo(p);
      collage.forEach(c => { if (c !== solo) c.style.opacity = p ? '0' : ''; });
      solo.style.visibility = p ? 'visible' : 'hidden'; solo.style.opacity = p ? '1' : '0';
      swapBadge(p); prev.hidden = !p;
      return;
    }
    gsap.killTweensOf([solo, badge, prev, ...collage]);
    const others = collage.filter(c => c !== solo);
    if (!p) {
      gsap.to(solo, { opacity: 0, y: 12, duration: 0.25, ease: 'power1.in', onComplete: () => { solo.style.visibility = 'hidden'; } });
      gsap.to(others, { opacity: 1, duration: 0.45, stagger: 0.06, delay: 0.15, ease: 'power2.out', clearProps: 'opacity' });
      gsap.to(prev, { opacity: 0, duration: 0.2, onComplete: () => { prev.hidden = true; } });
    } else if (fromAll) {
      gsap.to(others, { opacity: 0, duration: 0.3, stagger: 0.04, ease: 'power1.in' });
      swapSolo(p); solo.style.visibility = 'visible';
      gsap.fromTo(solo, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.5, delay: 0.18, ease: 'power2.out' });
      prev.hidden = false; gsap.fromTo(prev, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.45, ease: 'power2.out' });
    } else {
      gsap.to([solo, prev], { opacity: 0, y: -8, duration: 0.18, ease: 'power1.in', onComplete: () => {
        swapSolo(p); prev.hidden = false;
        gsap.fromTo([solo, prev], { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power2.out' });
      } });
    }
    gsap.to(badge, { opacity: 0, duration: 0.15, onComplete: () => { swapBadge(p); gsap.to(badge, { opacity: 1, duration: 0.3 }); } });
  }
  wrap.addEventListener('click', e => { const b = e.target.closest('.hn-pill'); if (b) go(b.dataset.niche); });
})();

/* ── Redesign before/after: the range input drives --pos (CSS) and the spoken value ── */
(function initBeforeAfter() {
  document.querySelectorAll('[data-ba]').forEach(root => {
    const range = root.querySelector('.ba-range');
    if (!range) return;
    const sync = () => {
      const v = Number(range.value);
      root.style.setProperty('--pos', v + '%');
      range.setAttribute('aria-valuetext', root.dataset.vt.replace('{a}', v).replace('{b}', 100 - v));
    };
    range.addEventListener('input', sync);
    sync();
  });
})();

/* ── Init ── */
calcUpdate();
setTimeout(() => {
  document.querySelectorAll('.rev').forEach(el => {
    if (el.getBoundingClientRect().top < innerHeight) el.classList.add('on');
  });
}, 60);
