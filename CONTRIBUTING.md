# Contributing to Bureau

Thanks for prying the lid off. Bureau is a small, opinionated room, and it stays
livable because the rules are few and held to. Here's how to file a report, send
a change, and not break the lights on your way out.

## Reporting a problem

Open an [issue](https://github.com/Sonophage/Bureau/issues). The useful ones tell
me:

- **Obsidian version** (Settings → About) and **Bureau version** (`manifest.json`, or the *What's new* note in Style Settings).
- **Platform** — desktop (and OS) or mobile.
- Whether the [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) plugin is installed, and which Bureau options you've changed.
- What you saw vs. what you expected. A screenshot is worth a paragraph.
- The smallest steps that reproduce it. "It's broken" is a mood, not a bug report.

If it only happens with a *particular* plugin or another theme element layered on
top, say so — Bureau aims for a plugin-independent baseline, so those cases are
worth knowing about.

## Sending a change

1. Fork, branch off `main`.
2. Edit `theme.css`. **It's one file** — there's no build step, no preprocessor, no `src/` to compile. What you edit is what ships.
3. Reload to see it. Obsidian caches the stylesheet and will lie to you about whether your change took — hard-reload, or toggle the theme off and back on.
4. Open a pull request against `main` with a short note on *what* changed and *why*. Before/after screenshots for anything visual.

Keep a PR to one idea. A focused diff gets read and merged; a grab-bag sits.

## House rules

These aren't style preferences — they're what keeps the theme coherent and the
reviewers happy. Hold to them:

- **One accent, one palette.** The whole UI reads from `--bu-accent` and the token block at the top of the `.theme-dark` / `.theme-light` sections. Retheme from there; don't hard-code colours mid-file.
- **No `!important`.** The theme ships with zero of them and clears every Obsidian linter warning. If you think you need one, you've usually lost a specificity fight that's better won another way — raise it in the PR.
- **Avoid `:has()` and other broadly-invalidating selectors.** They're flagged in review for the selector-invalidation cost — re-evaluating big swaths of the DOM on every mutation. Reach for a class, a combinator, or a small JS-set body class before a `:has()` that spans editor leaves or the workspace.
- **Atmosphere is opt-in.** CRT, scanlines, glow, animation — all of it defaults to off-or-quiet and lives behind a slider. Nothing decorative should be load-bearing or on by default.
- **Mobile stays sane.** There's a hard plugin-independent mobile baseline with real touch targets. Don't regress it.
- **Match the room.** Comments in `theme.css` explain the *why*, not the obvious *what*. If a rule is a workaround for an Obsidian quirk, leave a note saying so — there are plenty already; mirror their tone and density.

## The `@settings` block

Every Bureau option lives in one `@settings` YAML block at the **foot** of
`theme.css`. It looks like a comment and it is not — it's parsed by the Style
Settings plugin, and a malformed block silently kills the whole panel. Two scars
worth not reopening:

- **Never put a bare `: ` (colon-space) inside a `description:`** — it breaks the YAML and takes the entire panel down with it. Reword, or quote the string.
- **Set `quotes: false` on `variable-text` inputs** that take a URL (e.g. the wallpaper), or Style Settings wraps the value in quotes and the pasted `url()` breaks.

If you add or rename an option, validate before you commit — `./release.py <ver> --dry-run` runs the same brace + `@settings` YAML check the real release does, without touching anything.

## Releasing (maintainer)

The `## Changelog` in the [README](README.md) is the single source of truth. To
cut a release: add the new `### X.Y.Z` entry to the top of it, then run
`./release.py X.Y.Z`. The script stamps `manifest.json` and the `theme.css`
header, regenerates the in-panel *What's new* note, prepends the entry to *Release
history*, validates the CSS, then commits, tags, pushes `main` + the tag, and
publishes the GitHub release with `theme.css` + `manifest.json` attached. Use
`--dry-run` to preview, `--yes` to skip the confirmation. Tags carry **no `v`
prefix** — Obsidian matches them to the manifest.

## License

Bureau is [MIT](LICENSE). By contributing, you agree your work ships under the
same. Take it apart, build your own room.
