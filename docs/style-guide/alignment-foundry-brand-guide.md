# The Alignment Foundry: Proposed Brand Style Guide

**Source:** Extracted from production assets, captured 2026-08-08: logo icon
(`docs/assets/img/logo.svg`, gradient mark: `#FFFFFF` 50% to `#67FCF1` 100%),
compiled site stylesheet (`docs/assets/css/style.scss`), and the live site at
<https://alignment-foundry.github.io/alignment-foundry/>. All six hex tokens
were verified against the live compiled CSS on capture day.

**Status:** PROPOSED, for review. Not an official brand document. Confirm with
the brand owner before external use.

---

## 1. Brand Essence

The Alignment Foundry is Alex S. Moy's AI alignment workspace. The identity is
a precision instrument on a dark bench: deep institutional blue as the canvas,
one luminous aquamarine readout as the signal. Calm, technical, quietly
confident. Nothing decorative that does not earn its place; the brand gradient
is the single allowed flourish, reserved for the logo, hero backdrops, and
accent moments.

## 2. Logo

- **Mark:** the circular emblem with the "ASM" monogram, filled with the brand
  gradient: white at the 50% stop sweeping to aquamarine `#67FCF1` at 100%
  (bottom-right). The gradient lets the mark hold up on both dark and light
  backgrounds.
- **Clear space:** at least the height of the mark on all sides. In the site
  header the mark sits at 32 px; never run type into that zone.
- **Minimum size:** 32 px digital (the site nav size), 0.5 in print.
- **Do not:** recolor or flatten the gradient, stretch or rotate the circle,
  add drop shadows or outer glow beyond the approved glow token, crop the
  circle, or place it on busy photography.

## 3. Color Palette

### Primary

| Swatch | Name | HEX | RGB | Usage |
|--------|------|-----|-----|-------|
| ██████ | Deep Blue | `#0A2342` | 10, 35, 66 | Primary canvas, dominant color: page background, header, footer, hero |
| ██████ | Aquamarine | `#67FCF1` | 103, 252, 241 | Signature accent: links, CTAs, eyebrows, focus states, logo gradient end |
| ██████ | Charcoal | `#1C1C1E` | 28, 28, 30 | Near-black surfaces, code blocks, print-friendly depth |

### Secondary

| Swatch | Name | HEX | RGB | Usage |
|--------|------|-----|-----|-------|
| ██████ | Deep Aqua | `#14786C` | 20, 120, 108 | Supporting accent: hover states, scrollbar, gradient mid-stop, card accents |
| ██████ | Light Teal | `#96E5AC` | 150, 229, 172 | Secondary accent: alternate card accents, positive emphasis |
| ██████ | White | `#FFFFFF` | 255, 255, 255 | Text and headings on dark surfaces, card text, button hover |

**Brand gradient** (logo, hero backdrops, accent moments only, never behind
body text): `linear-gradient(135deg, #0A2342 0%, #14786C 55%, #67FCF1 100%)`.

Notes:

- Site body text is white at 92% opacity (`rgba(255,255,255,0.92)`), muted text
  at 65%; both composite comfortably above AA on Deep Blue (see Accessibility).
- No functional/status palette by design. Success, warning, and error colors
  are UI-state concerns, not brand; pick them per component and test contrast
  locally.
- Aquamarine and Light Teal are accents, not inks. On white backgrounds they
  fail WCAG contrast (1.25:1 and 1.49:1) and must never carry text.

## 4. Typography

**Hanken Grotesk** (weights 400 / 500 / 700) via Google Fonts is the only
typeface. Fallback stack: `'Hanken Grotesk', system-ui, sans-serif`.

| Role | Font | Weight | Size |
|------|------|--------|------|
| Display / H1 | Hanken Grotesk | 700 | clamp(2.5rem, 5.5vw, 4rem), line-height 1.05, tracking -0.025em |
| Section headings (H2) | Hanken Grotesk | 700 | clamp(1.75rem, 3vw, 2.25rem), accent rule above |
| H3 | Hanken Grotesk | 700 | 1.375rem |
| H4 | Hanken Grotesk | 700 | 1.125rem |
| Body | Hanken Grotesk | 400 | 1rem on an 18 px base, line-height 1.6, max 75ch |
| Lede / emphasis | Hanken Grotesk | 500 | 1.25rem |
| Labels / eyebrows | Hanken Grotesk | 500 / 700 | 0.72 to 0.8125rem, uppercase, tracking 0.08 to 0.1em |
| Code | ui-monospace, SFMono-Regular, Menlo, Consolas, monospace | 400 | 0.9em |

Headings render white on dark; H3 and link text render Aquamarine. Never go
below 14 px for body copy.

## 5. Voice & Tone

The site style, enforced in CI:

- **Plain-spoken and precise.** Short sentences, scannable, no jargon and no
  hype. Present the work and let it speak.
- **No em dashes, ever.** Use a colon for a title/subtitle split or an
  introduction, commas for asides, a semicolon or a full stop between
  independent clauses, and an en dash only for true numeric ranges
  (for example `2026-2030`). This is CI-enforced repo-wide.
- **Calm technical confidence.** First person where it is honest, never
  corporate filler, never fear-mongering about alignment risk.
- Accessible by default: honor `prefers-reduced-motion` and degrade gracefully
  without JavaScript.

## 6. Imagery & Iconography

- **Backdrops:** layered radial glows (Deep Aqua and Aquamarine at low alpha)
  over the Deep Blue canvas, a faint engineering grid masked to fade at the
  edges, a slow-drifting orb. These are the brand's visual signature.
- **Photography (when used):** dark, technical, macro detail: circuitry,
  materials, instruments, papers. Deep-blue color grade with teal highlights.
  No stocky corporate poses.
- **Iconography:** inline SVG, monoline, rounded terminals, single color:
  Aquamarine on dark, Deep Blue on white. 1.5 to 2 px stroke.
- **Motion:** scroll-reveal fade-ups, accent-bar cards, the header logo hover
  (slight rotate plus glow). Every animation is a 16 s or sub-half-second
  flourish, disabled under `prefers-reduced-motion`.

## 7. Layout & Spacing

- **Grid:** 1200 px max width, 48 px desktop gutter, 24 px tablet, 16 px
  mobile. An 8 px base spacing rhythm.
- **Radii:** 12 px cards, 6 px buttons, 3 px scrollbar.
- **Balance:** Deep Blue dominant, White and Charcoal in support, Aquamarine
  as accent. A 60-30-10 feel.
- **Cards:** accent-bar signature (a 3 px bar wipes across the top on hover);
  accent colors cycle Aquamarine, Light Teal, Deep Aqua across a grid.
- **Buttons:** solid Aquamarine with Deep Blue text (12.59:1), hover to White
  surface with Deep Blue text (15.77:1). Ghost variant: Aquamarine outline on
  dark.

## 8. Do / Don't

| ✅ Do | ❌ Don't |
|-------|----------|
| Use Deep Blue as the dominant canvas | Use Aquamarine or Light Teal as text on white |
| Use Aquamarine for links, CTAs, and eyebrows on Deep Blue | Put the brand gradient behind body text |
| Keep Hanken Grotesk for all type | Mix in serif or display fonts |
| Honor `prefers-reduced-motion` and no-JS fallbacks | Decorate purely for effect |
| Write plain-spoken copy, no em dashes | Use em dashes in any content |
| Test contrast (WCAG AA) before publishing | Place light accents on white unchecked |

## 9. Accessibility

Real WCAG 2.1 contrast ratios, computed from the exact hex tokens (relative
luminance method):

| Pair | Ratio | Result |
|------|-------|--------|
| White on Deep Blue | 15.77:1 | PASS, AAA |
| Charcoal on White | 17.01:1 | PASS, AAA |
| Aquamarine on Deep Blue | 12.59:1 | PASS, AAA |
| Deep Blue on Aquamarine (buttons) | 12.59:1 | PASS, AAA |
| Light Teal on Deep Blue | 10.59:1 | PASS, AAA |
| Aquamarine on Charcoal | 13.59:1 | PASS, AAA |
| White on Charcoal | 17.01:1 | PASS, AAA |
| White on Deep Aqua | 5.34:1 | PASS, AA (AAA for large text) |
| Deep Aqua on White | 5.34:1 | PASS, AA (AAA for large text) |
| Site body text (white 92% on Deep Blue) | 13.44:1 | PASS, AAA |
| Site muted text (white 65% on Deep Blue) | 7.35:1 | PASS, AAA |
| **Aquamarine on White** | **1.25:1** | **FAIL: accent or background only, never text** |
| **Light Teal on White** | **1.49:1** | **FAIL: accent or background only, never text** |

**Summary:** every pair the site actually uses for text passes AA, and all
headline pairs reach AAA. The two failing pairs are the light accents on white
backgrounds; keep them for fills, borders, and glows, never for text or icons
that must carry meaning.

Other requirements: visible keyboard focus (2 px Aquamarine outline, or the
skip-link pattern with Aquamarine surface and Deep Blue text at 12.59:1),
`prefers-reduced-motion` support, and readable focus/hover states on every
interactive element.

---

*Proposed guide compiled from observed production assets (logo.svg and the
compiled site CSS, 2026-08-08). Verify against any future official brand
guidelines before external use.*
