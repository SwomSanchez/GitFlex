## Overview

Wise — the global money-transfer brand — wears its identity in a single signature pairing: a vivid lime-green `{colors.primary}` (`#9fe870`) used as the CTA pill and brand accent, set against a pale sage-tinted canvas `{colors.canvas-soft}` (`#e8ebe6`) that runs across the hero band, and a near-black ink `{colors.ink}` (`#0e0f0c`) with a hint of warmth from the brand's underlying olive cast. The brand reads more like a calm Scandinavian magazine than a bank — generous whitespace, large rounded cards, and an unusually heavy display sans set at weight 900 carrying every hero headline.

Display typography is the second decisive voice. The proprietary `Wise Sans` family carries hero displays at weight 900 in scales from 64 px up to 126 px on the largest hero. The brand pairs Wise Sans 900 with Inter at weight 600 for sub-displays — the contrast between the chunky proprietary face and Inter's neutrality creates a particular hierarchy: Wise Sans for the brand moment, Inter for everything else.

Cards are universally pill-rounded — `{rounded.xl}` 24 px is the brand's signature card radius. Buttons take the same 24 px pill-rectangle shape. The brand never uses sharp corners on UI elements; the visual softness is part of the friendly fintech voice.

**Key Characteristics:**

- A single lime-green CTA accent `{colors.primary}` (`#9fe870`) — the brand's universal primary action color. No second accent.
- Two-face display typography — Wise Sans (proprietary, weight 900, hero scale) + Inter (weight 600, sub-display scale). The contrast is the brand's typographic story.
- `{rounded.xl}` 24 px is the canonical card and button radius. Generous, friendly.
- Sage-tinted canvas `{colors.canvas-soft}` (`#e8ebe6`) is the brand's hero surface; white `{colors.canvas}` is reserved for cards within the sage band.
- A full semantic palette: positive green family, warning yellow family, negative red family — each documented with content / hover / active variants for in-product use.
- Currency-converter card on the hero — the brand's signature interactive component, hosting from/to amount inputs.

## Colors

### Brand & Accent

- **Wise Green** (`{colors.primary}` — `#9fe870`): The brand's universal CTA color. Every primary button, every "Send money" pill, the brand's logo accent.
- **Wise Green Hover** (`{colors.primary-active}` — `#cdffad`): The lighter green for active state.
- **Wise Green Neutral** (`{colors.primary-neutral}` — `#c5edab`): A mid-saturation green used as a neutral active fill.
- **Wise Green Pale** (`{colors.primary-pale}` — `#e2f6d5`): The lightest green for soft surface tints / badge backgrounds.

### Surface

- **Canvas** (`{colors.canvas}` — `#ffffff`): Pure white for card interiors.
- **Canvas Soft** (`{colors.canvas-soft}` — `#e8ebe6`): The sage-tinted page background. Defining mood of the brand.

### Text

- **Ink** (`{colors.ink}` — `#0e0f0c`): Near-black with a hint of olive warmth — the brand's default text and headings color.
- **Ink Deep** (`{colors.ink-deep}` — `#163300`): A deep forest-green ink used on positive-state surfaces.
- **Body** (`{colors.body}` — `#454745`): Secondary body text.
- **Mute** (`{colors.mute}` — `#868685`): Lowest-priority text — captions, placeholder, fine print.

### Semantic

- **Positive** (`{colors.positive}` — `#2ead4b`): Success indicator.
- **Positive Deep** (`{colors.positive-deep}` — `#054d28`): Pressed positive state.
- **Warning** (`{colors.warning}` — `#ffd11a`): Caution indicator.
- **Warning Deep** (`{colors.warning-deep}` — `#b86700`): Pressed warning.
- **Warning Content** (`{colors.warning-content}` — `#4a3b1c`): Text on warning surfaces.
- **Negative** (`{colors.negative}` — `#d03238`): Destructive / error red.
- **Negative Deep** (`{colors.negative-deep}` — `#a72027`): Pressed destructive.
- **Negative Darkest** (`{colors.negative-darkest}` — `#a7000d`): Highest-emphasis destructive text.
- **Negative Bg** (`{colors.negative-bg}` — `#320707`): Dark maroon for destructive callout backgrounds.

### Brand Accent — Tertiary

- **Accent Orange** (`{colors.accent-orange}` — `#ffc091`): Bright peach used inside illustrative content / pricing cards.
- **Accent Cyan** (`{colors.accent-cyan}` — `#38c8ff`): Bright sky-blue used as a tertiary illustration accent.

## Typography

### Font Family

Two faces ladder the system:

1. **Wise Sans** — proprietary geometric sans with an unusually heavy weight 900 used for all hero displays. The face is the brand's typographic signature. Always at weight 900, never lighter on the marketing surface.
2. **Inter** — used for sub-displays (weight 600), all body, and form labels. Loaded with `font-feature-settings: "calt"` for contextual alternates.

### Hierarchy

| Token                         | Size  | Weight | Line Height | Letter Spacing | Use                              |
| ----------------------------- | ----- | ------ | ----------- | -------------- | -------------------------------- |
| `{typography.display-mega}`   | 126px | 900    | 107.1px     | 0              | Hero stencil at maximum scale.   |
| `{typography.display-xxl}`    | 96px  | 900    | 81.6px      | 0              | Sub-hero scale.                  |
| `{typography.display-xl}`     | 64px  | 900    | 54.4px      | 0              | Standard hero headline.          |
| `{typography.display-lg}`     | 47px  | 400    | 70.5px      | -0.108px       | Lighter sub-display.             |
| `{typography.display-md}`     | 40px  | 900    | 34px        | 0              | Section / card headlines.        |
| `{typography.display-sm}`     | 32px  | 600    | 38.4px      | -0.96px        | Inter-rendered section headings. |
| `{typography.display-xs}`     | 24px  | 600    | 31.2px      | -0.48px        | Sub-section displays.            |
| `{typography.body-lg}`        | 20px  | 400    | 30px        | 0              | Lead paragraphs.                 |
| `{typography.body-md}`        | 16px  | 400    | 24px        | 0              | Default body.                    |
| `{typography.body-md-strong}` | 16px  | 600    | 24px        | 0              | Bold inline body.                |
| `{typography.body-sm}`        | 14px  | 400    | 20px        | 0              | Secondary body.                  |
| `{typography.body-sm-strong}` | 14px  | 600    | 20px        | 0              | Bold caption / nav-link.         |
| `{typography.caption}`        | 12px  | 400    | 16px        | 0              | Fine print.                      |
| `{typography.button-md}`      | 16px  | 600    | 24px        | 0              | Button label.                    |

### Principles

- **Weight 900 for hero, weight 600 for everything else.** The brand's display ceiling is full-black weight; everything below is semibold.
- **Wise Sans for the brand voice, Inter for utility.** Strict role separation.

### Note on Font Substitutes

Wise Sans is proprietary. Open-source substitutes:

- **Display** — _Inter_ at weight 900 or _Manrope_ at weight 800 / 900 captures the geometric heaviness. _Geist_ weight 800 is a passable second choice.
- **Sub-display + body** — _Inter_ is the brand's actual second face.

## Layout

### Spacing System

- **Base unit**: 4 px.
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 24 px · `{spacing.2xl}` 32 px · `{spacing.3xl}` 48 px.
- **Section padding**: bands use `{spacing.3xl}` 48 px top/bottom on desktop.
- **Card interior**: cards at `{spacing.xl}` 24 px.

### Grid & Container

- Marketing container centres at ~1200 px.
- Hero: split layout (headline left, currency-converter card right) at desktop; stacked at mobile.
- Feature grids: 2-up / 3-up at desktop.

### Responsive Strategy

#### Breakpoints

| Name    | Width      | Key Changes                                                        |
| ------- | ---------- | ------------------------------------------------------------------ |
| Mobile  | < 768px    | Hero stacks; converter card full-width below headline; grids 1-up. |
| Tablet  | 768–1023px | Grids 2-up.                                                        |
| Desktop | ≥ 1024px   | Hero split; full grids.                                            |

#### Touch Targets

Buttons render ~48 px tall (12 vertical padding + 24 line). WCAG AAA at all widths.

#### Image Behavior

Photography is sparse; the brand prefers illustrative SVGs and product mockups inside cards. Country flag thumbnails appear inside currency rows.

## Elevation & Depth

| Level                      | Treatment                                                                                   | Use                                    |
| -------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------- |
| Level 0 — Flat             | No shadow, no border.                                                                       | Default.                               |
| Level 1 — Hairline on Dark | 1 px solid `{colors.ink}` border.                                                           | Tertiary outline buttons, form inputs. |
| Level 2 — Soft Card        | Implicit Level 0 white card sitting on sage canvas — the surface contrast IS the elevation. | Cards on the sage hero band.           |

The brand uses surface contrast (`{colors.canvas-soft}` background vs `{colors.canvas}` cards) as the primary elevation cue.

## Shapes

### Border Radius Scale

| Token            | Value  | Use                                         |
| ---------------- | ------ | ------------------------------------------- |
| `{rounded.none}` | 0px    | Full-bleed bands.                           |
| `{rounded.sm}`   | 8px    | Inline pills, small badges.                 |
| `{rounded.md}`   | 12px   | Form inputs, smaller chrome.                |
| `{rounded.lg}`   | 16px   | Mid-size cards.                             |
| `{rounded.xl}`   | 24px   | The brand's canonical button + card radius. |
| `{rounded.pill}` | 9999px | Status pills and full-radius accents.       |
| `{rounded.full}` | 9999px | Circular icon containers.                   |

## Components

### Buttons

**`button-primary`** — the lime-green CTA pill.

- Background `{colors.primary}`, text `{colors.on-primary}`, label `{typography.button-md}`, padding `{spacing.md} {spacing.xl}`, shape `{rounded.xl}` 24 px.

**`button-secondary`** — the sage-tinted secondary.

- Background `{colors.canvas-soft}`, text `{colors.ink}`, same typography / padding / shape.

**`button-tertiary`** — the white outline tertiary.

- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, same typography / padding / shape.

**`button-icon-circular`** — the circular icon button.

- Background `{colors.canvas}`, ink icon, shape `{rounded.full}`.

### Cards & Containers

**`card-content`** — the default white card.

- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.xl}`, shape `{rounded.xl}`. No border, sits on sage canvas.

**`card-feature-sage`** — the sage-tinted feature card.

- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.xl}`, shape `{rounded.xl}`.

**`card-feature-green`** — the soft-green feature card.

- Background `{colors.primary-pale}`, text `{colors.ink}`, padding `{spacing.xl}`, shape `{rounded.xl}`.

**`card-feature-dark`** — the polarity-flipped dark card with green text.

- Background `{colors.ink}`, text `{colors.primary}` (Wise green!), padding `{spacing.xl}`, shape `{rounded.xl}`. Used for promotional moments.

**`currency-converter-card`** — the brand's signature interactive widget.

- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, padding `{spacing.xl}`, shape `{rounded.xl}`. Hosts from/to amount inputs + currency selectors.

### Inputs & Forms

**`text-input`** — the canonical text input.

- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, body in `{typography.body-md}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.md}`.

### Navigation

**`nav-bar`** — the sticky top nav.

- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.xl}`.

**`nav-link`** — link items inside nav.

- Text `{colors.ink}`, set in `{typography.body-sm-strong}`.

**`footer`** — the dark footer band.

- Background `{colors.ink}`, text `{colors.canvas-soft}`, padding `{spacing.3xl} {spacing.xl}`. Body in `{typography.body-sm}`.

### Signature Components

**`hero-band`** — the sage-canvas hero band.

- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.xl}`. Headline in `{typography.display-mega}` (Wise Sans weight 900).

**`hero-band-dark`** — the polarity-flipped dark hero.

- Background `{colors.ink}`, text `{colors.primary}` (Wise green headline on near-black!), same padding / scale.

**`content-band`** — the white content band that follows hero.

- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.xl}`. Section headline in `{typography.display-md}`.

**`badge-positive`** — the positive status pill.

- Background `{colors.primary-pale}`, text `{colors.positive-deep}`, body in `{typography.body-sm-strong}`, padding `{spacing.xs} {spacing.md}`, shape `{rounded.pill}`.

**`badge-negative`** — the negative status pill.

- Background `{colors.negative-bg}`, text white, body in `{typography.body-sm-strong}`, padding `{spacing.xs} {spacing.md}`, shape `{rounded.pill}`.

### Examples (illustrative)

> Auto-derived kit-mirror demonstration surfaces (`scripts/derive-examples-block.mjs`). Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently. `TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface.

- Properties: `backgroundColor`, `textColor`, `borderColor`, `rounded`, `padding`

**`ex-pricing-tier-featured`** — Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode).

- Properties: `backgroundColor`, `textColor`, `rounded`, `padding`

**`ex-product-selector`** — What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery).

- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-cart-drawer`** — Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart).

- Properties: `backgroundColor`, `rounded`, `padding`, `item-divider`

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.

- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.

- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.

- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.

- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-empty-state-card`** — Empty-state illustration frame.

- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.

- Properties: `backgroundColor`, `rounded`, `padding`, `typography`

## Do's and Don'ts

### Do

- Reserve `{colors.primary}` Wise green for every primary CTA. The lime-green pill IS the brand's conversion signature.
- Set hero headlines in `{typography.display-mega}` / `{typography.display-xl}` Wise Sans weight 900. Never lighter.
- Use `{rounded.xl}` 24 px for buttons and cards. The generous radius is the brand's friendliness signature.
- Cycle page surfaces in `{colors.canvas-soft}` sage canvas → `{colors.canvas}` white cards. Surface contrast carries elevation.
- Use the full semantic palette (positive / warning / negative) for in-product status — never repurpose Wise green as success indicator since it IS the brand CTA.

### Don't

- Don't introduce a second brand accent. Wise green is the sole identity colour.
- Don't render the hero in weight 700 or lighter. The brand's display weight is 900.
- Don't render CTAs as sharp rectangles. The 24 px pill geometry is non-negotiable.
- Don't pair the green CTA with a green background. The brand always sits Wise green on neutral surfaces (sage / white / ink).
- Don't replace Wise Sans with a generic geometric sans for hero typography — the proprietary face IS the brand's voice.
