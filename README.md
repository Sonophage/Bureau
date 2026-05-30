# Bureau

A dark, noir-bureau theme for [Obsidian](https://obsidian.md) — a worn case-file
on a concrete desk, wired to a humming CRT terminal.

I've always been fond of the *bureau-redacted* look — the noiresque elements, the
brutalism of it: heavy type, stamped labels, blacked-out lines, concrete and
steel. I wanted a UI that felt like a brutalist-noir interface that was actually
*cohesive* — not a pile of effects, but a single room you could work inside.
Bureau is that attempt.

Its mood is stitched from three places:

- **Control** — the austere institutional dread of the Federal Bureau of Control (the default **red** accent).
- **The Magnus Archives** — dusty archives and quiet wrongness (the **green** accent, *Magnus*).
- **Deus Ex** — black-and-gold cyber-renaissance (the **gold** accent, *Deus*).

![screenshot](screenshot.png)

Dark-only. Every texture is procedural SVG (no embedded images), the whole UI
reads from a single accent colour, and there's an optional CRT layer —
scanlines, phosphor glow, a flickering scan line, a power-on when you open a
note.

## Install

**Community themes:** Settings → Appearance → Manage → search **Bureau**.

**Manual:**
1. Download `theme.css` and `manifest.json`.
2. Drop them into `<vault>/.obsidian/themes/Bureau/`.
3. Settings → Appearance → Themes → **Bureau**.

> **Install the [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) plugin.**
> Everything below lives there, under one **Bureau** panel.

## Controls

All controls are in **Settings → Style Settings → Bureau**. The panel preserves
your choices — switching presets never overwrites them.

### Mode
A quick preset that layers over everything else:

| Mode | Result |
| --- | --- |
| **Low** | Base styling only — no textures, glow, CRT, or motion |
| **Medium** | Textures + ambient glow; no CRT or animation |
| **High** | Everything on |
| **Custom** | Use the individual toggles below (your saved settings) |

### Color & accent
- **Accent preset** — *Control* (red) · *Magnus* (green) · *Deus* (gold) · *Custom*. The one colour the whole UI, glow, and highlights read from.
- **Custom accent** — your own colour, used when the preset is *Custom*.

### Atmosphere
- **Glow intensity / reach** — the accent glow rising from the bottom of the window.
- **Film grain** (+ intensity) — fine grain over the whole window.
- **Sidebar texture** (+ strength) — concrete grain on the panels behind the cards.
- **Vignette** (+ amount) — darkened window edges.

### CRT
- **CRT scanlines** (+ spacing) — faint horizontal lines over the editor.
- **CRT text glow** (+ brightness) — phosphor bloom on body text.
- **Typewriter tooltips** — tooltips type in character by character.
- **Fullscreen CRT mode** — in fullscreen, a curved tube vignette, amped scanlines/glow, and chrome that recedes until hover.
- **Focus line** (+ dim amount) — dims every editor line but the one you're on, with an accent edge marker.

### Cards & layout
- **Cards layout** — float every pane as a bordered card on a dark desk.
- **Card gap / rounding / shadow darkness**.

### Tabs
- **Tab shape** — *Folder* (connected file-folder tabs) or *Pill* (fully rounded).
- **Main / Left sidebar / Right sidebar tab content** — Icons · Labels · Icons + Labels.
- **Pinned tabs → icon only**.

### Hide / Focus
- **Focus Mode** — hides the tab bar, window buttons, and status bar at once. Bind a hotkey to *Style Settings → Toggle Focus Mode*.
- À-la-carte: hide the **status bar**, **breadcrumbs**, **tab close button**, **left/right sidebar toggles**, **folder collapse arrow**, **command-palette instructions**.

### Animation
Restrained and CRT-flavoured — eased, never bouncy. A master **Animations**
toggle gates everything, with a **speed** slider (400–1000 ms; hover/state runs
snappier).

- **CRT power-on** — content fades in from black when a note/pane opens.
- **Channel-change crossfade** — fade-from-black + scan-line wipe on note switch.
- **Boot scan-sweep** — a bright line wipes down once at launch.
- **Scanning line** — a faint white line scans slowly down the editor and glitches like a loose wire (sliders for **brightness**, **glitch interval**, and **glitch depth**).
- **Breathe the ambient glow**, **ease the phosphor glow**, **fade menus & modals**.
- **Terminal block caret**, **hover bloom** (accent glow on hover), **active-line scan**, **CRT flicker**, **CRT loading throbber**, **eased checkbox tick**.
- **MOBILE — disable animations**.

### Daily notes
Per-weekday colour schemes (Sun–Sat), each with its own **accent**, **text**,
and **background**. Add the `cssclass: daily` (or a weekday class) to a note to
key its palette. Disable the old "Daily Note Themes" snippet — Bureau owns this.

## Credits

Bureau borrows ideas, gratefully, from:

- **[blobob](https://github.com/kazi-aidah/blobob)** — the hiding/focus options, the animation principles, and the tab styling approach.
- **[Daily Note Themes](https://github.com/CyanVoxel/Obsidian-Daily-Themes)** (CyanVoxel) — the per-weekday colour-scheme idea.
- **[Elysian](https://github.com/matothetomato/elysian)** — styling inspiration.
- **[Minimalist Paradise](https://github.com/bellebasso/Minimalists-Paradise)** — styling inspiration.

Fonts (loaded via Google Fonts, with system fallbacks): **Urbanist** and
**Courier Prime**, both OFL.

## Development

The theme is a single `theme.css`. Edit it and reload Obsidian (hard-reload, or
toggle the theme off/on — Obsidian caches `theme.css`). Retheme from the
`.theme-dark` token block at the top; the Style Settings config lives in the
`@settings` block at the foot.

## License

MIT
