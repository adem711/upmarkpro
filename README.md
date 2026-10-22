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

The page HTML is generated. Edit the sources, then rebuild (needs Python 3 and Node for the esbuild minifier):

    python build.py

- `src/content.py`  page URLs, meta tags and copy for the new components (services, work cards, FAQ, offer, CTA, nav, footer)
- `src/<lang>/*.html`  finished sections (hero, promise, calculator, bio + process, contact form)
- `src/legal_content.py`  privacy notice and cookie page (draft)
- `src/shared.json`  icons and shared fragments
- `src/site.css`, `src/site.js`  shared by every page (source, not served)

`build.py` writes, for every language:

- every page, with the minified CSS **inlined** in `<head>` (no render-blocking request)
- `assets/site.js` (minified, loaded with `defer` and a `?v=` fingerprint) and `assets/concepts.js`
- `sitemap.xml`, `llms.txt`, `404.html` (a real 404 page also stops Cloudflare Pages from answering unknown URLs with the home page) and `_headers` (long cache lifetimes for fonts, vendor scripts and the fingerprinted JS)

Do not edit the generated `index.html` files, `assets/site.js` or `assets/concepts.js` by hand.
