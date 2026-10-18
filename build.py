#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the static multi-page Upmarkpro site (EN / FR / IT).

    python build.py

Reads  src/content.py, src/legal_content.py, src/shared.json and the section partials in src/<lang>/*.html
Writes <page>/index.html for every page, assets/concepts.js and sitemap.xml.
The generated files are committed: Cloudflare Pages serves them as-is (no build step on the server).
"""
import html as _html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'src'))
from content import *            # noqa: E402,F401,F403
import legal_content             # noqa: E402

BASE = 'https://upmarkpro.com'
WA = 'https://wa.me/393882576789'
SH = json.load(open(os.path.join(ROOT, 'src', 'shared.json'), encoding='utf-8'))
PUBLIC_PAGES = ['home', 'services', 'work', 'about', 'contact', 'privacy', 'cookies']
STALE = ['privacy.html', 'cookies.html', 'fr/confidentialite.html', 'fr/cookies.html', 'it/privacy.html', 'it/cookie.html']


# ───────────────────────── helpers ─────────────────────────
def esc(s):  return _html.escape(s, quote=False)
def attr(s): return _html.escape(s, quote=True)
def url(page, lang): return PAGES[page][lang]
def partial(lang, name): return open(os.path.join(ROOT, 'src', lang, name + '.html'), encoding='utf-8').read()
def has_partial(lang, name): return os.path.exists(os.path.join(ROOT, 'src', lang, name + '.html'))

def write(rel, text):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline='\n').write(text)

def out_path(page, lang):
    u = url(page, lang)
    return u.strip('/') + '/index.html' if u != '/' else 'index.html'

def fix_links(h, lang):
    """In-page anchors of the old single page -> real page URLs; legal links -> folder URLs."""
    m = {'#contact': url('contact', lang), '#work': url('work', lang), '#progetti': url('work', lang), '#services': url('services', lang),
         '#approach': url('about', lang), '#offerta': url('contact', lang) + '#offerta'}
    h = re.sub(r'href="(#(?:contact|work|progetti|services|approach|offerta))"', lambda x: f'href="{m[x.group(1)]}"', h)
    for pg in ('privacy', 'cookies'):
        bare = url(pg, lang).rstrip('/')
        h = h.replace(f'href="{bare}"', f'href="{url(pg, lang)}"')
    return h

def first_sentence(s):
    return re.split(r'(?<=[.!?])\s+', s.strip(), maxsplit=1)[0]

def delay(i): return ['', ' d1', ' d2', ' d3'][i % 4]


# ───────────────────────── header / footer / dock ─────────────────────────
def switcher(lang, page):
    def a(l, label):
        on = l == lang
        return (f'<a class="lang-btn{" on" if on else ""}" href="{url(page, l)}" hreflang="{l}" lang="{l}"'
                + (' aria-current="page"' if on else '') + f'>{label}</a>')
    return '<div class="lang-switch">' + a('en', 'EN') + a('fr', 'FR') + a('it', 'IT') + '</div>'

def wa_icon(lang):
    return (f'<a href="{WA}" target="_blank" rel="noopener" class="nav-wa" aria-label="{attr(NAV[lang]["wa_aria"])}">'
            f'<svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="{SH["wa_path"]}"/></svg></a>')

def pills(lang, page):
    return ''.join(f'<a class="mob-pill{" on" if l == lang else ""}" href="{url(page, l)}" hreflang="{l}" lang="{l}"' + (' aria-current="true"' if l == lang else '') + f'>{l.upper()}</a>' for l in LANGS)

def nav(lang, page):
    n = NAV[lang]; dr = DRAWER[lang]
    items = ''.join(f'<li><a href="{url(k, lang)}"{" aria-current=\"page\"" if page == k else ""}>{n[k]}</a></li>' for k in ('services', 'work', 'about', 'contact'))
    cta = url('contact', lang) + '#offerta'
    mob = ''.join(
        f'<li><a class="mob-link" href="{url(k, lang)}" onclick="closeMob()"{" aria-current=\"page\"" if page == k else ""}>'
        f'<span class="mob-idx">0{i} /</span><span>{n[k]}</span></a></li>'
        for i, k in enumerate(('services', 'work', 'about', 'contact'), 1))
    wa_svg = f'<svg width="22" height="22" viewBox="0 0 24 24" fill="#25D366" aria-hidden="true"><path d="{SH["wa_path"]}"/></svg>'
    tel_svg = f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{SH["phone_path"]}"/></svg>'
    return f'''<!-- NAV -->
<nav id="nav">
  <div class="nav-in">
    <a href="{url('home', lang)}" class="logo">
      <div class="logo-mark">
        {SH['logo']}
      </div>
      <span class="logo-name"><em>Up</em>markpro</span>
    </a>
    <ul class="nav-ul">
      {items}
      <li>
        {switcher(lang, page)}
      </li>
      <li>{wa_icon(lang)}</li>
      <li><a href="{cta}" class="nav-cta" data-magnetic>{n['cta']}</a></li>
    </ul>
    <div class="nav-mobile-group">
      <div class="nav-mobile-actions">
        {switcher(lang, page)}
        {wa_icon(lang)}
      </div>
      <button class="ham" id="ham" type="button" aria-label="{attr(dr['menu'])}" aria-expanded="false" aria-controls="mob-nav" data-label-open="{attr(dr['menu'])}" data-label-close="{attr(dr['close'])}"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
<div id="mob-nav" role="dialog" aria-modal="true" aria-label="{attr(dr['menu'])}">
  <ul class="mob-list">{mob}</ul>
  <div class="mob-lang" role="group" aria-label="{attr(dr['lang'])}">{pills(lang, page)}</div>
  <div class="mob-contact">
    <a class="mob-btn mob-wa" href="{WA}" target="_blank" rel="noopener">{wa_svg}<span>{dr['wa']}</span></a>
    <a class="mob-btn mob-tel" href="tel:+393882576789">{tel_svg}<span>{dr['call']}</span></a>
    <a class="mob-mail" href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>
  </div>
  <a href="{cta}" class="btn-lime mob-cta" onclick="closeMob()">{dr['cta']}</a>
</div>
'''

def footer(lang, page):
    f = FOOT[lang]; svc = SERVICE_SHORT[lang]
    ids = [m[0] for m in SERVICE_META]
    svc_links = ''.join(f'<a href="{url("services", lang)}#{i}">{esc(t)}</a>' for i, t in zip(ids, svc))
    nav_links = ''.join(f'<a href="{url(k, lang)}">{esc(t)}</a>' for k, t in
                        (('home', f['home']), ('services', NAV[lang]['services']), ('work', NAV[lang]['work']), ('about', NAV[lang]['about']), ('contact', NAV[lang]['contact'])))
    piva = '\n      <!-- P.IVA: add when registered -->' if lang == 'it' else ''
    return f'''<!-- FOOTER -->
<footer id="footer" aria-label="{attr(f['aria'])}">
  <div class="ft">
    <div class="ft-brand">
      <a href="{url('home', lang)}" class="logo">
        <div class="logo-mark">{SH['logo']}</div>
        <span class="logo-name"><em>Up</em>markpro</span>
      </a>
      <p>{esc(f['desc'])}</p>
      {SH['social']}
    </div>
    <div>
      <p class="ft-col-h">{f['cols'][0]}</p>
      <div class="ft-links">{svc_links}</div>
    </div>
    <div>
      <p class="ft-col-h">{f['cols'][1]}</p>
      <div class="ft-links">{nav_links}</div>
    </div>
    <div>
      <p class="ft-col-h">{f['cols'][2]}</p>
      <div class="ft-links"><a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a><a href="tel:+393882576789">+39 388 257 6789</a><span>upmarkpro.com</span></div>{piva}
    </div>
  </div>
  <div class="ft-bot">
    <span class="ft-copy-wrap"><span>{f['copy']}</span><span class="ft-legal"><a href="{url('privacy', lang)}">{f['privacy']}</a><a href="{url('cookies', lang)}">{f['cookies']}</a></span></span>
    {switcher(lang, page)}
  </div>
</footer>
'''

def dock(lang, page):
    d = DOCK[lang]
    quote = '#contact-form' if page == 'contact' else url('contact', lang)
    return f'''<!-- Mobile conversion bar -->
<nav class="m-dock" id="m-dock" aria-label="{attr(d['aria'])}">
  <a href="{WA}" target="_blank" rel="noopener" class="m-dock-wa">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{SH['wa_path']}"/></svg>
    <span class="m-dock-wa-txt"><b>WhatsApp</b><small><i class="m-dock-live" aria-hidden="true"></i>{esc(d['replies'])}</small></span>
  </a>
  <a href="{quote}" class="m-dock-cta">{esc(d['quote'])}</a>
</nav>
'''

def jsonld(lang):
    desc = {'en': 'Website design, brand identity and Shopify stores for local trade and service businesses, working remotely with clients across Italy.',
            'fr': "Design web, identité de marque et boutiques Shopify pour les artisans et prestataires locaux, à distance, partout en Italie.",
            'it': 'Siti web, branding, visibilità su Google e negozi online Shopify per attività locali, studi professionali ed e-commerce, a distanza in tutta Italia.'}[lang]
    cat = {'en': 'Design & Website Services', 'fr': 'Services de design et de sites web', 'it': 'Servizi di siti web, branding e negozi online'}[lang]
    social = re.findall(r'href="(https://www\.(?:facebook|instagram)\.com/[^"]+)"', SH['social'])
    data = {
        '@context': 'https://schema.org', '@type': 'ProfessionalService', '@id': BASE + '/#business', 'name': 'Upmarkpro',
        'url': BASE + url('home', lang), 'description': desc, 'telephone': '+393882576789', 'email': 'hello@upmarkpro.com',
        'areaServed': {'@type': 'Country', 'name': 'Italia'}, 'availableLanguage': ['it', 'en', 'fr'], 'inLanguage': lang, 'sameAs': social,
        'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': cat, 'itemListElement': [
            {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': s['title'], 'description': s['p']}} for s in SERVICES[lang]]},
    }
    return '<script type="application/ld+json">\n  ' + json.dumps(data, ensure_ascii=False, indent=2).replace('\n', '\n  ') + '\n  </script>'

def head(lang, page, m, ld=False):
    title = m['title']; desc = m['desc']
    alts = ''.join(f'  <link rel="alternate" hreflang="{l}" href="{BASE}{url(page, l)}">\n' for l in LANGS)
    alts += f'  <link rel="alternate" hreflang="x-default" href="{BASE}{url(page, "en")}">\n'
    others = ''.join(f'  <meta property="og:locale:alternate" content="{LOCALE[l]}">\n' for l in LANGS if l != lang)
    kw = f'  <meta name="keywords" content="{attr(m["keywords"])}">\n' if m.get('keywords') else ''
    return f'''<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{esc(title)}</title>
  <meta name="description" content="{attr(desc)}">
  <!-- Favicon & theme -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/favicon.svg">
  <meta name="theme-color" content="#0A0E14">

  <!-- SEO -->
  <meta name="author" content="Upmarkpro">
  <meta name="robots" content="index, follow">
{kw}  <link rel="canonical" href="{BASE}{url(page, lang)}">
{alts}
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Upmarkpro">
  <meta property="og:title" content="{attr(title)}">
  <meta property="og:description" content="{attr(m.get('og_desc', desc))}">
  <meta property="og:url" content="{BASE}{url(page, lang)}">
  <meta property="og:locale" content="{LOCALE[lang]}">
{others}
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{attr(m.get('tw_title', title))}">
  <meta name="twitter:description" content="{attr(m.get('tw_desc', desc))}">
{('  <!-- JSON-LD structured data -->\n  ' + jsonld(lang) + chr(10)) if ld else ''}
  <!-- Fonts (self-hosted) -->
  <link rel="preload" href="/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/hanken-grotesk-var.woff2" as="font" type="font/woff2" crossorigin>

  <link rel="stylesheet" href="/assets/site.css">
</head>'''

def page_html(lang, page, main, m, ld=False, concepts=False, body_class=''):
    scripts = ['/assets/vendor/gsap.min.js', '/assets/vendor/ScrollTrigger.min.js'] + (['/assets/concepts.js'] if concepts else []) + ['/assets/site.js']
    bt = SH['backtop'].replace('aria-label="Back to top"', f'aria-label="{attr(BACKTOP[lang])}"')
    return f'''<!DOCTYPE html>
<html lang="{lang}">
{head(lang, page, m, ld)}
<body{(' class="' + body_class + '"') if body_class else ''}>

{nav(lang, page)}
<main>

{main}
</main>

{footer(lang, page)}
{dock(lang, page)}
<!-- Back to top -->
{bt}

''' + ''.join(f'<script src="{s}"></script>\n' for s in scripts) + '''</body>
</html>
'''


# ───────────────────────── components ─────────────────────────
def svc_card(lang, i, mode):
    sid, cls, ico, num = SERVICE_META[i]
    d = SERVICES[lang][i]; ui = SERVICES_UI[lang]
    badge = SH['partner_badge'] if sid == 'shopify' else ''
    head_ = f'''<span class="svc-ghost" aria-hidden="true">{num}</span>
        {badge}'''
    if mode == 'sum':
        return f'''      <a class="svc svc-sum {cls} rev{delay(i)}" href="{url('services', lang)}#{sid}">
        {head_}
        <div class="svc-head">
          <div class="svc-ico">{SH[ico]}</div>
          <h3>{esc(d['title'])}</h3>
        </div>
        <p>{esc(d['p'])}</p>
        <span class="svc-sum-link">{esc(ui['incl'])} →</span>
      </a>'''
    chips = '\n'.join(f'          <span class="svc-chip">{esc(c)}</span>' for c in d['chips'])
    lis = '\n'.join(f'            <li>{SH["check"]}<span>{esc(t)}</span></li>' for t in d['items'])
    return f'''      <div class="svc {cls} rev{delay(i)}" id="{sid}">
        {head_}
        <div class="svc-ico">
          {SH[ico]}
        </div>
        <h3>{esc(d['title'])}</h3>
        <p>{esc(d['p'])}</p>
        <div class="svc-chips">
{chips}
        </div>
        <details class="svc-more" open>
          <summary><span>{esc(ui['incl'])}</span> {SH['arrow']}</summary>
          <ul class="svc-more-list">
{lis}
          </ul>
        </details>
      </div>'''

def services_summary(lang):
    ui = SERVICES_UI[lang]
    cards = '\n\n'.join(svc_card(lang, i, 'sum') for i in range(4))
    return f'''<!-- SERVICES (summary) -->
<section id="services" aria-label="{attr(ui['aria'])}">
  <div class="container">
    <div class="sh rev">
      <div>
        <span class="eyebrow">{esc(ui['eyebrow'])}</span>
        <h2>{esc(ui['h'])}</h2>
      </div>
      <p>{esc(ui['sub'])}</p>
    </div>
    <div class="svc-grid svc-grid-2">

{cards}

    </div>
    <div class="sec-cta rev"><a href="{url('services', lang)}" class="btn-outline">{esc(ui['explore'])}</a></div>
  </div>
</section>
'''

def services_full(lang):
    ui = SERVICES_UI[lang]
    cards = '\n\n'.join(svc_card(lang, i, 'full') for i in range(4))
    return f'''<!-- SERVICES (full) -->
<section id="services" class="page-first" aria-label="{attr(ui['aria'])}">
  <div class="container">
    <div class="sh rev">
      <div>
        <span class="eyebrow">{esc(ui['eyebrow'])}</span>
        <h1>{esc(ui['h'])}</h1>
      </div>
      <p>{esc(ui['sub'])}</p>
    </div>
    <h2 class="sr-only">{esc(ui['list_h'])}</h2>
    <div class="svc-grid svc-grid-2">

{cards}

    </div>
  </div>
</section>
'''

WHO_ICONS = {  # lightweight inline icons (stroke = currentColor)
    'trades': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    'practices': '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/>',
    'online': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
}
WHO_ACCENT = ['who-lime', 'who-blue', 'who-lime']

def per_chi(lang):
    d = PER_CHI[lang]
    cards = []
    for i, c in enumerate(d['cards']):
        tags = chr(10).join(f'          <li class="who-tag">{esc(t)}</li>' for t in c['tags'])
        cards.append(f'''    <article class="who-card {WHO_ACCENT[i % 3]} rev{delay(i)}">
      <header class="who-head">
        <span class="who-ico" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{WHO_ICONS[c['icon']]}</svg></span>
        <span class="who-badge">{esc(c['badge'])}</span>
      </header>
      <h3 class="who-title">{esc(c['title'])}</h3>
      <ul class="who-tags" role="list" aria-label="{attr(c['title'])}">
{tags}
      </ul>
      <div class="who-outcome">
        <span class="who-outcome-label">{esc(c['outcome_label'])}</span>
        <p>{esc(c['outcome_desc'])}</p>
      </div>
    </article>''')
    return f'''<!-- WHO I WORK FOR -->
<section id="per-chi" aria-label="{attr(d['aria'])}">
  <div class="rs-header">
    <h2 class="rs-header-label">{esc(d['label'])}</h2>
    <div class="rs-header-line"></div>
  </div>
  <div class="who-grid">
{chr(10).join(cards)}
  </div>
</section>
'''

def concept_card_link(lang, cid):
    c = CONCEPTS[cid]; w = WORK_UI[lang]; t = c['title'][lang]
    note = f'\n            <p class="wcard-note">{esc(w["note"])}</p>' if w['note'] else ''
    return f'''      <a class="wcard" href="{c['url']}" target="_blank" rel="noopener">
        <div class="wcard-thumb">
          <img src="/assets/projects/{cid}/hero.webp" alt="{attr(w['alt'] + ' — ' + t.split(' — ')[0])}" width="960" height="600" loading="lazy" decoding="async">
          <span class="wcard-cat">Concept · {esc(c['niche'][lang])}</span>
          <div class="wcard-overlay">
            <div class="wcard-overlay-btn">{esc(w['view'])}</div>
          </div>
        </div>
        <div class="wcard-info">
          <div>
            <h3>{esc(t)}</h3>{note}
          </div>
          <div class="wcard-arrow" aria-hidden="true">↗</div>
        </div>
      </a>'''

def concept_card_split(lang, cid):
    c = CONCEPTS[cid]; w = WORK_UI[lang]; t = c['title'][lang]
    note = f'\n            <p class="wcard-note">{esc(w["note"])}</p>' if w['note'] else ''
    return f'''      <article class="wcard wcard-split" data-concept="{cid}">
        <button type="button" class="wcard-thumb wcard-pick">
          <img src="/assets/projects/{cid}/hero.webp" alt="{attr(w['alt'] + ' — ' + t.split(' — ')[0])}" width="960" height="600" loading="lazy" decoding="async">
          <span class="wcard-cat">Concept · {esc(c['niche'][lang])}</span>
          <span class="wcard-overlay"><span class="wcard-overlay-btn">{esc(w['preview'])}</span></span>
        </button>
        <div class="wcard-info">
          <div>
            <h3>{esc(t)}</h3>{note}
          </div>
          <a class="wcard-link btn-outline" href="{c['url']}" target="_blank" rel="noopener">{esc(w['view'])}</a>
        </div>
      </article>'''

def work_featured(lang):
    w = WORK_UI[lang]
    cards = '\n'.join(concept_card_link(lang, cid) for cid in FEATURED)
    return f'''<!-- FEATURED CONCEPTS -->
<section id="work" aria-label="{attr(w['aria'])}">
  <div class="container">
    <div class="sh rev">
      <div>
        <span class="eyebrow">{esc(w['eyebrow'])}</span>
        <h2>{esc(w['h'])}</h2>
        <p>{esc(w['intro'])}</p>
      </div>
    </div>
    <div class="wgrid">
{cards}
    </div>
    <div class="sec-cta rev"><a href="{url('work', lang)}" class="btn-lime">{esc(w['all'])}</a></div>
  </div>
</section>
'''

def work_page(lang):
    w = WORK_UI[lang]
    cards = '\n'.join(concept_card_split(lang, cid) for cid in CONCEPTS)
    return f'''<!-- WORK -->
<section id="work" class="page-first" aria-label="{attr(w['aria'])}">
  <div class="container">
    <div class="sh rev">
      <div>
        <span class="eyebrow">{esc(w['eyebrow'])}</span>
        <h1>{esc(w['h'])}</h1>
        <p>{esc(w['intro'])}</p>
      </div>
    </div>
    <div class="work-meta rev">
      <span class="work-meta-count">{esc(w['count'])}</span>
    </div>
    <p class="concept-note rev" role="note">{esc(w['disclaimer'])}</p>
    <h2 class="sr-only">{esc(w['viewer'])}</h2>
    <div class="showroom rev" id="showroom" data-device="desktop" role="region" aria-label="{attr(SHOWROOM_ARIA[lang])}"></div>
    <h2 class="sr-only">{esc(w['list_h'])}</h2>
    <div class="wgrid" id="wgrid">
{cards}
    </div>
  </div>
</section>
'''

def bio_parts(lang):
    ap = partial(lang, 'approach')
    bio = re.search(r'<div class="ap-bio">(.*?)</div>', ap, re.S).group(1)
    return (re.search(r'<span class="eyebrow">(.*?)</span>', bio).group(1), re.search(r'<h2>(.*?)</h2>', bio, re.S).group(1),
            re.findall(r'<p>(.*?)</p>', bio, re.S))

def about_teaser(lang):
    eb, h, ps = bio_parts(lang)
    ui = ABOUT_UI[lang]
    return f'''<!-- ABOUT TEASER -->
<section id="about-teaser" aria-label="{attr(ui['aria'])}">
  <div class="container">
    <div class="ap-bio about-teaser-in rev">
      <span class="eyebrow">{eb}</span>
      <h2>{h}</h2>
      <p>{ps[0]}</p>
      <p>{first_sentence(ps[1])}</p>
      <a href="{url('about', lang)}" class="btn-outline">{esc(ui['teaser_link'])}</a>
    </div>
  </div>
</section>
'''

def cta_banner(lang, quote=False):
    ct = partial(lang, 'contact')
    eb = re.search(r'<span class="eyebrow">(.*?)</span>', ct).group(1)
    h = re.search(r'<h2>(.*?)</h2>', ct, re.S).group(1)
    sub = re.search(r'<p class="cf-intro-sub">(.*?)</p>', ct, re.S).group(1)
    c = CTA[lang]
    href = url('contact', lang) + ('#offerta' if lang == 'it' and not quote else '')
    return f'''<!-- CTA BANNER -->
<section class="cta-banner" aria-label="{attr(c['aria'])}">
  <div class="container">
    <div class="cta-card rev">
      <div class="cta-text">
        <span class="eyebrow">{eb}</span>
        <h2 class="cta-h">{h}</h2>
        <p>{sub}</p>
      </div>
      <div class="cta-actions">
        <a href="{href}" class="btn-lime" data-magnetic>{esc(c['quote'] if quote else c['go'])}</a>
        <a href="{WA}" target="_blank" rel="noopener" class="btn-outline">{esc(c['wa'])}</a>
      </div>
    </div>
  </div>
</section>
'''

def faq(lang):
    d = FAQ[lang]
    items = '\n'.join(f'''      <details class="faq-item">
        <summary><span>{esc(q)}</span> {SH['arrow']}</summary>
        <p>{esc(a)}</p>
      </details>''' for q, a in d['qa'])
    return f'''<!-- FAQ -->
<section id="faq" aria-label="{attr(d['aria'])}">
  <div class="container">
    <div class="sh rev">
      <div>
        <span class="eyebrow">{esc(d['eyebrow'])}</span>
        <h2>{esc(d['h'])}</h2>
      </div>
    </div>
    <div class="faq-list rev">
{items}
    </div>
  </div>
</section>
'''

def first_clients(lang):
    d = FIRST_CLIENTS.get(lang)
    if not d: return ''
    return f'''<!-- FIRST CLIENTS -->
<section id="primi-clienti" aria-label="{attr(d['aria'])}">
  <div class="container">
    <div class="rc offer-first rev">
      <h2 class="rc-title">{esc(d['h'])}</h2>
      <p class="rc-desc">{esc(d['p'])}</p>
    </div>
  </div>
</section>
'''

def offer_card(lang):
    from urllib.parse import quote
    o = OFFER[lang]
    link = WA + '?text=' + quote(o['wa'], safe="-_.!~*'()")
    return f'''<div class="calc-card rev">
      <div class="calc-intro">
        <span class="eyebrow">{esc(o['eyebrow'])}</span>
        <h2>{esc(o['h'])}</h2>
        <p>{esc(o['p'])}</p>
      </div>
      <div class="calc-body">
        <a href="{link}" target="_blank" rel="noopener" class="btn-lime offer-btn" data-magnetic>{esc(o['btn'])}</a>
        <p class="offer-small">{esc(o['small'])}</p>
      </div>
    </div>'''


# ───────────────────────── pages ─────────────────────────
def build_home(lang):
    parts = [fix_links(partial(lang, n), lang) for n in ('hero', 'promise')]
    if has_partial(lang, 'kinetic'): parts.append(partial(lang, 'kinetic'))
    parts += [services_summary(lang), work_featured(lang), about_teaser(lang), cta_banner(lang)]
    return page_html(lang, 'home', '\n'.join(parts), META['home'][lang], ld=True, concepts=True)

def build_services(lang):
    parts = [services_full(lang), per_chi(lang), fix_links(partial(lang, 'calculator'), lang), cta_banner(lang, quote=True)]
    return page_html(lang, 'services', '\n'.join(parts), META['services'][lang])

def build_work(lang):
    return page_html(lang, 'work', work_page(lang), META['work'][lang], concepts=True)

def build_about(lang):
    ap = fix_links(partial(lang, 'approach'), lang)
    ap = ap.replace('<section id="approach"', '<section id="approach" class="page-first"', 1)
    ap = re.sub(r'(<div class="ap-bio">\s*<span class="eyebrow">.*?</span>\s*)<h2>(.*?)</h2>', r'\1<h1>\2</h1>', ap, count=1, flags=re.S)
    ap = ap.replace('<h3>', '<h2>', 1).replace('</h3>', '</h2>', 1)                  # process title
    ap = ap.replace('<h4>', '<h3>').replace('</h4>', '</h3>')                         # process steps
    parts = [ap, first_clients(lang), faq(lang), cta_banner(lang)]
    return page_html(lang, 'about', '\n'.join(p for p in parts if p), META['about'][lang])

def build_contact(lang):
    ct = fix_links(partial(lang, 'contact'), lang)
    ct = ct.replace('<section id="contact"', '<section id="contact" class="page-first"', 1)
    ct = re.sub(r'(<div class="cf-intro rev">.*?)<h2>(.*?)</h2>', r'\1<h1>\2</h1>', ct, count=1, flags=re.S)
    grid = '    <div class="cf-grid">'
    assert grid in ct, 'cf-grid marker missing in contact partial'
    ct = ct.replace(grid, f'    <div class="contact-offer" id="offerta">\n    {offer_card(lang)}\n    </div>\n\n' + grid, 1)
    return page_html(lang, 'contact', ct, META['contact'][lang])

def build_legal(lang, kind):
    c = legal_content.C[lang]; d = c[kind]
    body = '\n'.join(f'      <h2>{h}</h2>\n' + '\n'.join(p if p.startswith('<ul>') else f'      <p>{p}</p>' for p in ps) for h, ps in d['sections'])
    main = f'''<div class="legal legal-wrap">
    <div class="legal-draft" role="note"><strong>{c['draft_h']}</strong> {c['draft']}</div>
    <h1>{d['title']}</h1>
    <p class="legal-updated">{c['updated']}</p>
{body}
  </div>'''
    page = 'privacy' if kind == 'privacy' else 'cookies'
    m = dict(title=f"{d['title']} | Upmarkpro", desc=d['meta'])
    return page_html(lang, page, main, m)


def build_all():
    for f in STALE:
        p = os.path.join(ROOT, f)
        if os.path.exists(p): os.remove(p)
    n = 0
    for lang in LANGS:
        for key, fn in (('home', build_home), ('services', build_services), ('work', build_work), ('about', build_about), ('contact', build_contact)):
            write(out_path(key, lang), fn(lang)); n += 1
        write(out_path('privacy', lang), build_legal(lang, 'privacy')); n += 1
        write(out_path('cookies', lang), build_legal(lang, 'cookie')); n += 1
    # concept data shared with site.js (hero niche switcher + device viewer)
    data = {cid: dict(url=c['url'], **{l: dict(niche=c['niche'][l], title=c['title'][l]) for l in LANGS}) for cid, c in CONCEPTS.items()}
    write('assets/concepts.js', '/* generated by build.py */\nwindow.CONCEPTS = ' + json.dumps(data, ensure_ascii=False, indent=1) + ';\n')
    # sitemap with hreflang alternates
    rows = []
    for key in PUBLIC_PAGES:
        prio, freq = ('1.0', 'monthly') if key == 'home' else (('0.8', 'monthly') if key in ('services', 'work', 'about', 'contact') else ('0.3', 'yearly'))
        for lang in LANGS:
            alts = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{BASE}{url(key, l)}"/>' for l in LANGS)
            alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{url(key, "en")}"/>'
            rows.append(f'  <url>\n    <loc>{BASE}{url(key, lang)}</loc>\n    <lastmod>2026-10-17</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>{alts}\n  </url>')
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n')
    print(f'built {n} pages, assets/concepts.js, sitemap.xml ({len(rows)} urls)')


if __name__ == '__main__':
    build_all()
