# Upmarkpro website

Static multi-page site (EN / FR / IT), served by Cloudflare Pages. No build step on the server:
the generated `index.html` files are committed.

## Pages

| Page | EN | FR | IT |
|---|---|---|---|
| Home | `/` | `/fr/` | `/it/` |
| Services | `/services/` | `/fr/services/` | `/it/servizi/` |
| Work | `/work/` | `/fr/projets/` | `/it/progetti/` |
| About | `/about/` | `/fr/a-propos/` | `/it/chi-sono/` |
| Contact | `/contact/` | `/fr/contact/` | `/it/contatto/` |
| Privacy | `/privacy/` | `/fr/confidentialite/` | `/it/privacy/` |
| Cookies | `/cookies/` | `/fr/cookies/` | `/it/cookie/` |

`/ciao` redirects (301) to `/it/?utm_source=biglietto&utm_medium=qr` (`_redirects`).

## Editing

The page HTML is generated. Edit the sources, then rebuild:

    python build.py

- `src/content.py`  page URLs, meta tags and copy for the new components (services, work cards, FAQ, offer, CTA, nav, footer)
- `src/<lang>/*.html`  finished sections (hero, promise, before/after, calculator, bio + process, contact form)
- `src/legal_content.py`  privacy notice and cookie page (draft)
- `src/shared.json`  icons and shared fragments
- `assets/site.css`, `assets/site.js`  shared by every page; `assets/concepts.js` is generated

`build.py` also writes `sitemap.xml`. Do not edit the generated `index.html` files by hand.
