# Bureau

A noir theme for [Obsidian](https://obsidian.md). A worn case-file on a concrete
desk, wired to a CRT terminal that hums whether or not you're listening.

> [!IMPORTANT]
> **Install the [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) plugin to access all of Bureau's settings.** Every option — accent & colours, borders, scrollbars, tabs, atmosphere, animation — lives in one **Bureau** panel there (Settings → Style Settings → Bureau). The theme still runs without it, but only on its built-in defaults.

I've always been fond of the *bureau-redacted* look. The noiresque of it, the
brutalism: heavy type that doesn't apologize, stamped labels, lines blacked out
by someone who decided you didn't need them, concrete and steel that were never
trying to be warm. Most themes are a pile of effects in a trench coat —
beautiful in the screenshot, incoherent the moment you live in them. I didn't
want effects. I wanted a room. One you could sit inside at 2 AM and feel like
the work mattered and the building was on your side, even if the building was
indifferent. Bureau is that attempt. It performs *home* the way a rental
performs it: clean, lit, holding its breath, hoping you don't look too closely
at the ceiling fan.

Its mood was stolen, in equal parts, from three places:

- **Control** — the institutional dread of the Federal Bureau of Control, the red of a door you shouldn't open (the default **red** accent).
- **The Magnus Archives** — dust, quiet wrongness, a tape still running (the **green** accent, *Magnus*).
- **Deus Ex** — black-and-gold cyber-renaissance, conspiracy with good lighting (the **gold** accent, *Deus*).

![screenshot](screenshot.png)

It used to be dark only — and that was the whole creed. It isn't anymore, and the
change turned out to *be* the point. Most themes pick a side: all-dark or
all-light, and they defend it like an identity. Bureau runs both — a near-black
**noir**, and a daylight **case-file in paper** — but the real room is the ground
between them. You can run the editor in the *opposite* palette to its chrome: a
lit page on a dark desk, or a dark page in a lit room. That isn't indecision.
It's **chiaroscuro** — the picture lives in the seam where light meets dark, not
in either alone. A compromise, and a deliberate one: light *and* dark, noir *and*
its negative, held in the same frame.

Every texture is procedural SVG, drawn by the stylesheet, not photographed and
dragged in. The whole UI reads from a single accent colour, the way a room reads
from a single bad bulb. And there's a CRT layer — scanlines, phosphor glow, a
white line that scans down the page and glitches like a loose wire, a power-on
that fades up from black every time you open a note. None of it is load-bearing.
All of it is there if you want the machine to feel haunted. And on a phone it
quiets itself down without being asked.

## Install

The straight way, no ceremony:

**Community themes:** Settings → Appearance → Manage → search **Bureau**.

**Manual:**
1. Download `theme.css` and `manifest.json`.
2. Drop them into `<vault>/.obsidian/themes/Bureau/`.
3. Settings → Appearance → Themes → **Bureau**.

> **Install the [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) plugin.**
> Everything below lives there, in one **Bureau** panel. Without it the theme
> still runs, but it runs the way the house came — someone else's defaults, the
> thermostat set to a temperature that isn't yours.

## Controls

All of it is in **Settings → Style Settings → Bureau**. The panel remembers what
you told it; switching presets never paves over your choices. It keeps your
fingerprints.

### Mode

The blunt instrument. One dial that decides how haunted the room gets, layered
over everything else:

| Mode | What you get |
| --- | --- |
| **Low** | The bones. Styling only — no texture, no glow, no CRT, no motion. The lights are on and nothing is breathing. |
| **Medium** | Texture and the ambient glow. The room is lived-in. No CRT, no animation. |
| **High** | Everything awake. The machine knows you're here. |
| **Custom** | Your own arrangement — every toggle below, exactly as you left it. |

And the **Inverted editor** toggle — the chiaroscuro switch. Turn it on and the
editor pane takes the *opposite* palette to the rest of the UI: in dark mode, a
paper page on a dark desk; in light mode, a dark page in a lit room. The caret,
the texture, the ink all flip with it. Flip Obsidian's own light/dark appearance
to swap which side is which — that dial is Obsidian's, not the theme's, so the
theme can't throw it for you.

> **Light or dark** is Obsidian's own switch (Settings → Appearance). Bureau
> dresses both: a full **daylight** variant — aged paper, a black marginalia
> ledger, dark ink — sits behind the light mode, the same way the noir sits
> behind the dark.

### Color & accent
- **Accent preset** — *Control* (red) · *Magnus* (green) · *Deus* (gold) · *Custom*. The single colour the whole UI, the glow, and every highlight read from. Change it and the building changes allegiance.
- **Custom accent** — your own colour, used when the preset is *Custom*. Bring your own bad bulb.
- **Native accent** — Bureau no longer forces Obsidian's built-in accent, so the startup / "loading" colour and native UI follow **Settings → Appearance → Accent color**. Set that to match your Bureau accent for a seamless launch (the startup screen is painted before Style Settings loads, so it can only follow the native colour).
- **Text colour — dark / light** — set the body-text ink for each mode independently.
- **Black level / White level** — how black the darkest surface goes in dark mode, how white the paper gets in light. Set the floor and the ceiling.

### Atmosphere
- **Glow intensity / reach** — the accent light bleeding up from the bottom of the window, like something is on fire one floor down.
- **Film grain** (+ intensity) — fine grain over everything. Proof the image was developed, not generated.
- **Sidebar texture** (+ strength) — concrete grain on the panels behind the cards. The walls the cards are pinned to.
- **Vignette** (+ amount) — the edges of the window darkened, the way attention darkens at the edges.
- **Accent halo** (+ strength, 0 = off) — a soft accent ring that breathes outward from the centre behind the UI. A slow pulse, like a signal you can't quite hear. Stills to a faint ring under reduced-motion.

### CRT
The tube. Optional, and quietly the whole point.
- **CRT scanlines** (strength + spacing, 0 = off) — faint horizontal lines laid over the editor, the ghost of a screen that was never really there.
- **CRT text glow** (brightness, 0 = off) — phosphor bloom on the body text. The letters sweat a little.
- **Fullscreen CRT mode** — go fullscreen and the screen curves: a tube vignette, scanlines and glow turned up, and all the chrome receding into the dark until you reach for it.
- **Focus line** (+ dim amount) — every line dims except the one you're on, which gets an accent mark in the margin. The rest of the page waits in the next room.

### Cards & layout
- **Cards layout** — every pane floats as a bordered card on a dark desk. Paper on concrete.
- **Card gap / rounding / shadow darkness** — how far apart, how soft the corners, how deep the shadow they cast. The cards now carry a faint glass bevel — a lit top-left lip and a shaded bottom-right edge — so they read as slabs, not stickers.
- **Horizontal settings nav** — reflow the settings window's left tab list into a scrolling strip across the top. Desktop only.
- **Reading line width / line height / paragraph spacing** — the density dials.

### Resize handles
The divider lines between the sidebars and the editor.
- **Remove resize handles** — drop the split divider lines for a seamless edge.
- **Custom resize-handle colour** (+ **Resize-handle colour**) — recolour the divider lines instead of the theme default. *Remove* wins if both are on.

### Pill editor card
The floating editor card in *Pill terminal* mode (needs Pill terminal on).
- **Remove editor card border** — drop the card outline so only its shadow defines the edge.
- **Custom editor card border colour** (+ **Editor card border colour**) — recolour the outline instead of the theme default. *Remove* wins if both are on.
- **Editor card rounding** — corner radius of the floating card (0–28 px); drives the clip-path too, so corners clip cleanly.

### Scrollbars
- **Hide scrollbars** — gone, but the content still scrolls (wheel, trackpad, keys).
- **Scrollbar width** — thickness in pixels (2–20).
- **Custom scrollbar colour** (+ **Scrollbar colour**) — recolour the resting thumb; the active/dragged thumb keeps the accent.
- **Fade scrollbars** (+ **Fade-out delay**) — the thumb stays invisible until the pointer is over the scroll area, then lingers and fades out after the delay. *Covers wheel, trackpad and dragging the grip; a true touch idle-timer needs a plugin, and some builds snap rather than tween the fade.*
- **Accent the thumb while scrolling** — the thumb flushes to the accent while gripped or hovered, easing back to its resting colour.

### Floating & glass
Optional soft looks layered over the brutalist base — all off by default, so the standard theme is untouched.
- **Heavier card float** — a deeper shadow + more space, so panes lift higher off the desk.
- **Frosted glass panes** — translucent, blurred editor and sidebar panes; the stage (or your wallpaper) shows through.
- **Pill terminal (floating editor)** — the full Ultra-Lobster move: the view-header breaks into flat pills on the desk, the title bar goes transparent, and the **editor floats as its own rounded card** below the chrome (status bar splits into pills too). Best with Cards layout on.
- **Pill terminal — hover to reveal** — the header pills *collapse* until you hover or focus the row, reclaiming that vertical space for the note. The desk clears until you reach for it.
- **Editor-only cards (flush sidebars)** — only the editor floats as a card; the sidebars sit flush.
- **Custom background image** (+ URL + dim) — a wallpaper behind the workspace, visible through the frosted glass. **Just paste the address** (`https://…` or a vault path) — no `url(…)` wrapping; the dim keeps text legible.

### Tabs
- **Tab shape** — *Folder* (connected, like a real file drawer) or *Pill* (fully rounded, for people who've made peace with it). The **active tab fills solid accent and rises taller** than the rest; **inactive tabs invert** — black-on-white / white-on-black — and they're **editor-aware**, flipping with *Inverted editor* so they always track the editor's palette, not the window's. Labels sit **dead-centre** and stay put when the close button appears.
- **Main / Left sidebar / Right sidebar tab content** — Icons · Labels · Icons + Labels. Decide per dock how much each tab is willing to admit about itself.
- **Pinned tabs → icon only** — the ones you've decided to keep say less.

### Hide / Focus
For when the room has too much furniture.
- **Focus Mode** — kills the tab bar, the window buttons, and the status bar in one move. Bind a hotkey to *Style Settings → Toggle Focus Mode* and you can clear the desk without looking down.
- À-la-carte, hide any of: the **status bar**, **breadcrumbs**, **tab close button**, **left/right sidebar toggles**, **folder collapse arrow**, **command-palette instructions**. Each one a thing you decided you didn't need to see again.

### Animation
Restrained, CRT-flavoured, eased — never bouncy. Nothing here springs at you; it
arrives, the way weather arrives. A master **Animations** toggle gates all of it,
with a **speed** slider (400–1000 ms; hover and state changes run snappier than
entrances).

- **CRT power-on** — content fades up from black when a note or pane opens. The tube warming.
- **Channel-change crossfade** — fade-from-black plus a scan-line wipe when you switch notes. Changing the channel.
- **Scanning line** — a faint white line drifts slowly down the editor and, every so often, glitches in and out like a connection that isn't seated right. Sliders for **brightness**, **glitch interval**, and **glitch depth** — how visible, how often, how bad.
- **Breathe the ambient glow**, **ease the phosphor glow**, **fade menus & modals** — the slow involuntary motions of a machine that's idling, not dead.
- **Typewriter tooltips** — tooltips reveal left-to-right, struck out one character at a time like a line on a platen.
- **Rolodex** — tabs and file-list rows lift toward you on hover with a heavy, springy overshoot and a real drop-shadow, so flicking through them feels tactile; the selected row holds its lift.
- **Terminal block caret**, **active-line scan**, **CRT flicker**, **eased checkbox tick** — the small tics. The wobble in the fan.
- **Limelight** — spotlight the pane you're in; every other note and sidebar dims until you look at it. Hover a dimmed pane to peek without taking focus.
- On **mobile**, the theatre dims itself: grain, scanlines, glow, motion, and the heavy shadows drop automatically on phones and tablets — no toggle, no Style Settings required — and tap targets grow. The device that can't afford the show doesn't have to sit through it.

### Daily notes
One **accent per weekday** (Sun–Sat) — so Tuesday doesn't get to look like
Friday — and its text and background **derive from that accent automatically**,
in light *and* dark. Add the weekday class (e.g. `cssclass: monday`) to a note to
key its palette. If you ran the old "Daily Note Themes" snippet, switch it off —
Bureau owns this room now.

## Changelog

### 2.5.3
- **Resize handles** section added — **remove** the sidebar split divider lines outright or **recolour** them, on a single `--bu-handle-border` lever.
- **Pill editor card** section added — **remove** or **recolour** the floating editor card's border, plus an **Editor card rounding** slider (drives both `border-radius` and the `clip-path` inset). Scoped to `body.bu-pill-chrome .workspace-split .view-content`.
- **Scrollbars** section added — **hide** scrollbars, set their **width**, a custom **thumb colour**, **fade** them in on hover (with a **fade-out delay**), and **accent** the thumb while it's gripped.
- **Tabs** — labels now sit dead-centre via a 3-column grid (close button no longer shoves them), larger uppercase title (0.79em / 0.09em tracking), active-tab label re-centred in the raised tab, and the faint native tab-divider line removed.
- **Nested modals** (Settings → Browse themes / community plugins) now blur the panel underneath directly, so it no longer reads through.
- **Inline text** — *italic* renders in the accent, ***bold italic*** is a paper-fill / accent-ink / accent-ring stamp, **bold** gets a clean white highlight on the light palette, and the **www chip** is back on external links **and** bare URLs.
- **Typewriter tooltips** restored (Animation section) — tooltips reveal left-to-right.
- **Native accent** is no longer forced — Obsidian's *Appearance → Accent color* drives the startup/"loading" colour and native UI, so set it to match your Bureau accent for a seamless launch.
- **Panel** — a *What's new* note at the top, a full **Changelog / Release history** at the foot, and the **Mode** section now starts collapsed.
- **Mobile fix** — the file explorer / Notebook Navigator no longer render blank until tapped (a power-on animation was out-specifying the mobile motion-kill and stranding off-screen drawer panes at `opacity:0`).

### 2.5.1
- Every Style Settings **heading now carries a one-line description**, so the panel reads uniformly section to section.

### 2.5.0 — Pill terminal & the reading surface
- **Pill terminal** (renamed from Pill chrome) is now the full Ultra-Lobster floating layout: the header rides the desk as flat pills, the title bar and active-leaf header go transparent (no black slab), and the **editor floats as its own rounded card** — corners clipped cleanly via `clip-path` so CodeMirror's ledger can't square them off.
- **Hover-to-reveal** now *reclaims* the header's space instead of just hiding it.
- **Tabs** rebuilt: active = solid accent + taller; inactive = inverted (black-on-white / white-on-black) and **editor-aware** (flips with *Inverted editor*). No more hover recolour.
- **Status bar** is editor-aware and inverts with the editor; each section is its own pill.
- **Colour controls added**: per-mode **text colour** and **black / white levels**.
- **Wallpaper** takes a **bare URL** now (no `url(…)` wrapping) via `image-set`.
- **Reading surface**: callout **bold** renders as a redaction stamp, callouts lift on a deeper shadow, **highlights** use the accent, **external links + bare URLs** become accent chips (the `www` tag retired), and **tables** punch the accent harder.
- **Settings & command palette** regained their backdrop **blur + accent glow**.
- **Removed**: the "Hover bloom" accent-glow-on-hover (replaced by the tactile Rolodex lift). Many cryptic settings gained descriptions.

## Credits

Bureau picked these pockets, gratefully:

- **[blobob](https://github.com/kazi-aidah/blobob)** — the hide/focus options, the animation principles, the way the tabs are handled.
- **[Daily Note Themes](https://github.com/CyanVoxel/Obsidian-Daily-Themes)** (CyanVoxel) — the per-weekday colour-scheme idea, lifted wholesale and grateful for it.
- **[Elysian](https://github.com/matothetomato/elysian)** — styling it taught me by example.
- **[Minimalist Paradise](https://github.com/bellebasso/Minimalists-Paradise)** — same debt, different teacher.
- **[Limelight](https://github.com/smikula/obsidian-limelight)** (smikula) — the spotlight-the-active-pane idea, rebuilt here in pure CSS.
- **[Ultra-Lobster](https://github.com/7368697661/Ultra-Lobster)** (7368697661) — the floating-card glass UI: frosted panes, a custom wallpaper behind them, and pill chrome.

Fonts, loaded via Google Fonts with system fallbacks when the wire goes dead:
**Urbanist** (the labels, the stamps) and **Courier Prime** (the body, the
mono). Both OFL.

## Development

It's one `theme.css`. Edit it and reload Obsidian — hard-reload, or toggle the
theme off and back on, because Obsidian caches the stylesheet and will lie to you
about whether your change took. Retheme from the `.theme-dark` token block at the
top, where the whole palette lives in one place. The Style Settings config is the
`@settings` block at the foot — it looks like a comment and it is not; leave it
alone unless you mean it.

## License

MIT. Take it apart. Build your own room.
