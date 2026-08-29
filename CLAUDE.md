# Upmarkpro Website Improvement Plan — Project Instructions

## Context
Upmarkpro (upmarkpro.com) is a branding and web design agency for local trades and service businesses (plumbers, electricians, roofers, tilers, painters, restaurants, barbers, salons, dental clinics). Target clients are non-technical business owners who respond to loss-aversion messaging (competitors outranking them, broken sites losing bookings), not generic design-quality appeals.

## Core Focus & Scope
The website baseline has been restored. Focus on targeted high-impact improvements:
1. **Performance Optimization**: Core Web Vitals (LCP/CLS/INP), WebP assets, code splitting, lightweight animation loops, SEO & LocalBusiness schema.
2. **Services Section Update**: Outcome-led packaging ("More Calls Website Design", "Brand Identity", "Shopify Store Design"), interactive inclusion lists, clear visual hierarchy.
3. **Advanced Features & UX**: Polished micro-interactions, kinetic typography watermark, interactive Lead Calculator widget, seamless mobile navigation, magnetic CTAs.

## Brand System (Strict Guidelines)
- Near-black navy: `#0A0E14`
- Neon lime: `#D6FF00`
- Electric blue: `#3B6EFF`
- Aesthetic: Swiss / brutalist, flat, high-contrast, clean grid overlay
- Typography: Bold, condensed sans-serif
- Tone & Copy: Outcome-led (e.g., "More Calls Website"). Avoid technical jargon like "web development" or "static website" in client-facing text.

## Tech Stack
- **Framework**: React + Vite + TypeScript
- **Styling**: Tailwind CSS
- **Animations**: GSAP (ScrollTrigger, staggered reveals, magnetic hooks — lightweight & performant)

## Key Requirements & Tasks

### 1. Performance & Core Web Vitals
- Optimize LCP/CLS/INP, eliminate layout shifts.
- Convert images to WebP with responsive `srcset` and explicit width/height dimensions.
- Implement lazy loading for non-critical assets and dynamic route code-splitting.
- Enhanced SEO: Meta tags, OpenGraph data, semantic HTML5 structure, structured data (`LocalBusiness` schema), sitemap.

### 2. Services Section Update
- Rebuild/upgrade the Services component (`src/components/sections/Services.tsx`).
- Every service card must clearly display inclusions for:
  - Brand Identity
  - Website Design ("More Calls Website")
  - Shopify Store Design
- Outcome-led headlines, loss-aversion hooks, interactive card highlights, clear CTA routing.

### 3. Advanced Features & UX Polish
- **Kinetic Watermark & Micro-animations**: Subtle background kinetic stroke text ("MORE CALLS"), smooth GSAP scroll-triggered reveals.
- **Interactive Lead Calculator**: High-converting interactive widget estimating missed calls & revenue for trade owners.
- **Header & Navigation**: Sticky glass header with mobile drawer menu, active section highlighting, and header "Contact" link.
- **Accessibility**: Visible keyboard focus rings, semantic landmark elements, checked contrast ratios (lime on navy & blue on navy).

### 4. Copy Guidelines (Reference)
- Service category term: **"Website Design"** (never "web development" or "static website").
- Outcome-driven naming: "More Calls Website", "Booked Jobs Page", "Local Visibility Site".
- No negotiable pricing ("prix négociable") anywhere.
- Loss-aversion framing over feature-selling in headlines and CTAs.

## Process
**Produce a written plan before major code edits.** Outline component breakdown, performance metrics, and task sequence. Confirm before major structural refactorings.

