---
name: landing-page-design
description: "Complete system for building high converting landing pages: intake questions, page structure, layout selection, conversion copywriting, SEO, plus strict visual rules for typography, spacing, corner radius, backgrounds, hero layout, icons, and motion. Use this skill whenever building, editing, styling, reviewing, or writing copy for ANY landing page, marketing site, web UI, page section, component, or prototype, even when the user does not mention design, conversion, tokens, or a design system. Always consult it before choosing page sections, headlines, CTAs, fonts, font sizes, spacing values, border radii, background colors, icons, or transitions."
---

# Landing Page Design

A landing page is not a homepage. A homepage serves multiple intents. A landing page wins one intent:

**one offer → one audience → one primary action.**

This skill has two halves. **Part A** decides what the page says and how it is structured. **Part B** is the non negotiable visual system. Work through A before touching B.

## Scope

Apply to all web UI work: landing pages, marketing sites, components, dashboards, prototypes, and design reviews. When a rule here conflicts with a framework default, this file wins. When the user's explicit prompt conflicts with a rule, the user wins.

---

# PART A — Strategy and structure

## A1. Intake
- Primary action: trial, demo, buy, waitlist, download
- Clear ICP & specific objection handling
- Real proof points (logos, stats, verified outcomes)

## A2. Page Structure
1. Headline (outcome + audience)
2. Subheadline (clarifies how + adds specificity)
3. Primary CTA (clear verb + what they get)
4. Proof signal (logo strip, stat, or short testimonial)
5. Hero visual (product screenshot, interactive canvas)
6. Problem to solution
7. Benefits (3-5 outcome-driven bullets)
8. How it works (3 steps)
9. Social proof & FAQ
10. Final CTA

## A4. Conversion Rules
- Be specific: Never say "Save time and streamline"; say "Cut your weekly reporting from 4 hours to 15 minutes".
- Reduce risk: free trial, no credit card required, cancel anytime.
- Benefit bullets: Bold benefit first, then the proof/detail.

---

# PART B — Visual system

## B1. Typography
- **Fonts to use:** Geist, Manrope, Geist Mono, Poppins.
- **Never use:** Inter, Roboto, Arial, Open Sans, Helvetica.
- **Never use italic fonts** anywhere in the interface.
- **One typeface per site.**
- **No hyphens in text.**
- **No orphaned words.** `text-wrap: balance` for headings, `text-wrap: pretty` for body.
- **Type Scale:** Snap strictly to Tailwind's default type scale (`text-xs` to `text-6xl`).

## B2. Spacing Tokens
- Spacing-0 (0), Spacing-25 (2px), Spacing-50 (4px), Spacing-75 (8px), Spacing-100 (12px), Spacing-200 (16px), Spacing-300 (24px), Spacing-400 (32px), Spacing-500 (40px), Spacing-600 (48px), Spacing-700 (64px), Spacing-800 (80px), Spacing-900 (96px).
- Main buttons: 8px vertical padding (`py-2`), 12px horizontal padding (`px-3.5` or `px-4`).

## B3. Corner Radius Formula
- **Nested radius formula:** When a shape sits inside another and gap is < 32px:
  `inner radius = outer radius - gap`

## B4. Borders & Backgrounds
- Borders go all the way around or not at all (never single-sided).
- **Never use gradients in backgrounds.** Backgrounds are flat.
- **Dark mode background colors:** Only `#000000`, `#181818`, `#1F1F1F`, `#272727`, `#313131`, `#131209`.

## B5. Hero Section
- **Heading text color (Dark theme):** Left-to-right text gradient: `#FFFFFF` → `#9B9B9B`.
- Heading and subheading max-width: **680px**.
- Break lines at meaningful points.

## B6. Icons
- **Use:** Phosphor, Solar, or Iconamoon.
- **Never use:** Material Icons, Material Symbols.

## B7. Motion
- **Base curve:** `ease-[cubic-bezier(0.22,1,0.36,1)]` with `duration-500`.

## B8. Content Realism
- Real copy only. No "Your headline here", no filler words ("revolutionize", "supercharge", "cutting edge", "effortless", "elevate").
- Believable names, real decimal metrics.
