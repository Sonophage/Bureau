#!/usr/bin/env python3
"""
Bureau release tool — one command to cut a release with every doc in sync.

THE ONE MANUAL STEP
  Add the new entry to README.md, directly under the "## Changelog" line, newest first:

      ## Changelog

      ### 2.5.4
      - What you changed.
      - Another bullet.

      ### 2.5.3
      ...

USAGE
  ./release.py 2.5.4              cut the release
  ./release.py 2.5.4 --dry-run    preview every change + the generated notes, touch nothing
  ./release.py 2.5.4 --yes        skip the final confirmation (true one-shot)

WHAT IT DOES (aborts on any failure; nothing is pushed until the confirm)
  preflight  -> repo sane, on main, gh authed, X.Y.Z semver, tag is new, README entry exists
  stamp      -> manifest.json version + the theme.css header version
  sync       -> regenerates the in-panel "What's new" note, prepends the entry to
                "Release history", and refreshes the "Creator Settings" import blob from
                the author's live vault config (all inside the @settings block)
  validate   -> theme.css braces balanced + the @settings YAML still parses
  ship       -> commit "Release X.Y.Z", tag X.Y.Z, push main + tag,
                gh release create X.Y.Z theme.css manifest.json  (notes = the README entry)

README's "## Changelog" stays the single source of truth; everything else is generated from it.
"""

import os
import re
import sys
import json
import subprocess

REPO = os.path.dirname(os.path.realpath(__file__))
THEME = os.path.join(REPO, "theme.css")
MANIFEST = os.path.join(REPO, "manifest.json")
README = os.path.join(REPO, "README.md")

# Constant footer appended to the "What's new" note (kept out of README so it isn't duplicated there).
WHATSNEW_FOOTER = (
    "Full release history is at the foot of this panel. **Updates:** install via the "
    "community-themes browser or [BRAT](https://github.com/TfTHacker/obsidian42-brat) to be "
    "notified automatically; otherwise re-download `theme.css` from the "
    "[releases page](https://github.com/Sonophage/Bureau)."
)

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

# Creator Settings: the author's live Bureau config, embedded as an importable JSON blob in the
# bu-creator-note info-text (users paste it into Style Settings → Import). Read from the vault's
# Style Settings data.json; override the path with BUREAU_VAULT_SS_DATA. Best-effort: if the file
# isn't present (a fresh clone, CI, another machine) the sync is skipped and the last-synced blob
# is left untouched, so the release never fails on account of it.
VAULT_SS_DATA = os.environ.get(
    "BUREAU_VAULT_SS_DATA",
    os.path.expanduser(
        "~/Documents/vaults/harker/.obsidian/plugins/obsidian-style-settings/data.json"
    ),
)


def die(msg):
    print(f"\n  ✗ {msg}\n", file=sys.stderr)
    sys.exit(1)


def step(msg):
    print(f"  · {msg}")


def run(args, **kw):
    return subprocess.run(args, cwd=REPO, text=True, capture_output=True, **kw)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# ── README changelog parsing ─────────────────────────────────────────────────
def changelog_entry(readme, version):
    """Return the markdown bullet block for '### {version}' under '## Changelog'."""
    m = re.search(r"^## Changelog\s*$", readme, re.M)
    if not m:
        die("README.md has no '## Changelog' section.")
    body = readme[m.end():]
    # the entry: from '### version' to the next '### ' or '## ' header (or EOF)
    em = re.search(
        rf"^### {re.escape(version)}\b.*?$\n(.*?)(?=^###\s|^##\s|\Z)",
        body, re.M | re.S,
    )
    if not em:
        die(
            f"README.md has no '### {version}' entry under '## Changelog'.\n"
            f"    Add it (newest first) before releasing — that's the one manual step."
        )
    block = em.group(1).strip("\n")
    bullets = [ln for ln in block.splitlines() if ln.strip()]
    if not bullets:
        die(f"The '### {version}' entry in README.md is empty.")
    return "\n".join(bullets)


# ── @settings info-text surgery ──────────────────────────────────────────────
def block_bounds(text, block_id):
    marker = f"  - id: {block_id}\n"
    start = text.find(marker)
    if start == -1:
        die(f"@settings block '{block_id}' not found in theme.css.")
    nxt = re.search(r"\n  - id: ", text[start + len(marker):])
    end = start + len(marker) + nxt.start() if nxt else text.find("\n*/", start)
    return start, end


def yaml_dquote(s):
    """A YAML double-quoted scalar (JSON escaping is a valid subset: \\n, \\\", \\\\)."""
    return json.dumps(s, ensure_ascii=False)


def set_line(block, key, new_value_literal):
    """Replace the single physical 'key: ...' line inside a block."""
    pat = re.compile(rf"^(    {re.escape(key)}: ).*$", re.M)
    if not pat.search(block):
        die(f"Could not find '{key}:' line in an @settings block.")
    return pat.sub(lambda m: m.group(1) + new_value_literal, block, count=1)


def sync_settings(theme, version, bullets):
    # 1) What's new — regenerate title + description
    whatsnew_desc = f"**Bureau v{version}**\n\n{bullets}\n\n{WHATSNEW_FOOTER}"
    s, e = block_bounds(theme, "bu-whatsnew-note")
    block = theme[s:e]
    block = set_line(block, "title", f"What's new — v{version}")
    block = set_line(block, "description", yaml_dquote(whatsnew_desc))
    theme = theme[:s] + block + theme[e:]

    # 2) Release history — prepend this version (idempotent: skip if already present)
    s, e = block_bounds(theme, "bu-changelog-full")
    block = theme[s:e]
    dm = re.search(r'^    description: "(.*)"\s*$', block, re.M)
    if not dm:
        die("Could not read the 'Release history' description line.")
    inner = dm.group(1)
    prepend = json.dumps(f"**v{version}**\n{bullets}\n\n", ensure_ascii=False)[1:-1]
    if f"**v{version}**" in inner:
        step(f"Release history already lists v{version} — leaving it.")
    else:
        block = set_line(block, "description", '"' + prepend + inner + '"')
        theme = theme[:s] + block + theme[e:]
    return theme


# ── Creator Settings blob ─────────────────────────────────────────────────────
def sync_creator(theme):
    """Refresh bu-creator-note's importable blob from the author's live vault config."""
    if not os.path.exists(VAULT_SS_DATA):
        step("Creator Settings: vault data.json absent, keeping the last-synced blob")
        return theme
    try:
        data = json.loads(read(VAULT_SS_DATA))
    except Exception as e:
        die(f"Creator Settings: could not parse {VAULT_SS_DATA}: {e}")
    bureau = {k: v for k, v in data.items() if k.startswith("bureau@@")}
    if not bureau:
        step("Creator Settings: no bureau@@ keys in the vault, keeping the last-synced blob")
        return theme
    blob = json.dumps(bureau, indent=2, ensure_ascii=False)
    desc = (
        "**Bureau, as its author runs it.** A snapshot of my own live setup, refreshed each "
        "release. To adopt it: copy the block below, open Style Settings' **Import** control "
        "(the import icon at the top of the Style Settings pane), and paste; it overwrites only "
        "your Bureau settings, nothing else.\n\n```json\n" + blob + "\n```"
    )
    s, e = block_bounds(theme, "bu-creator-note")
    block = theme[s:e]
    block = set_line(block, "description", yaml_dquote(desc))
    theme = theme[:s] + block + theme[e:]
    step(f"synced Creator Settings from vault ({len(bureau)} keys)")
    return theme


# ── validation ───────────────────────────────────────────────────────────────
def validate(theme):
    pre = theme.split("/* @settings")[0]
    if pre.count("{") != pre.count("}"):
        die(f"theme.css braces unbalanced: {{={pre.count('{')} }}={pre.count('}')}")
    m = re.search(r"/\* @settings\s*\n(.*?)\n\*/", theme, re.S)
    if not m:
        die("Could not locate the @settings block to validate.")
    try:
        import yaml  # noqa
        data = yaml.safe_load(m.group(1))
        ids = [s.get("id") for s in data["settings"]]
        dups = {i for i in ids if ids.count(i) > 1}
        if dups:
            die(f"Duplicate @settings ids: {sorted(dups)}")
        step(f"validated: braces balanced, @settings YAML ok ({len(ids)} settings)")
    except ImportError:
        step("validated: braces balanced (PyYAML absent — skipped YAML parse)")


# ── main ─────────────────────────────────────────────────────────────────────
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    flags = {a for a in sys.argv[1:] if a.startswith("-")}
    dry = "--dry-run" in flags or "-n" in flags
    assume_yes = "--yes" in flags or "-y" in flags

    if len(args) != 1 or not SEMVER.match(args[0]):
        die("usage: ./release.py X.Y.Z [--dry-run] [--yes]")
    version = args[0]

    print(f"\nBureau release · v{version}{'  (dry run)' if dry else ''}\n")

    # preflight
    if not (os.path.exists(THEME) and os.path.exists(MANIFEST)):
        die("theme.css / manifest.json not found next to release.py.")
    branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"]).stdout.strip()
    if branch != "main":
        die(f"on branch '{branch}', not 'main'. Switch first.")
    if run(["git", "tag", "-l", version]).stdout.strip() and not dry:
        die(f"tag {version} already exists. Bump the version.")
    if run(["gh", "auth", "status"]).returncode != 0 and not dry:
        die("gh is not authenticated (`gh auth login`).")

    readme = read(README)
    bullets = changelog_entry(readme, version)
    step(f"found README entry for {version} ({len(bullets.splitlines())} bullets)")

    # stamp
    theme = read(THEME)
    theme, n1 = re.subn(r"(· v)\d+\.\d+\.\d+", rf"\g<1>{version}", theme, count=1)
    if n1 != 1:
        die("could not find the '· vX.Y.Z' version stamp in the theme.css header.")
    manifest = read(MANIFEST)
    manifest2, n2 = re.subn(r'("version":\s*")\d+\.\d+\.\d+(")', rf"\g<1>{version}\g<2>", manifest, count=1)
    if n2 != 1:
        die('could not find "version" in manifest.json.')
    step("stamped manifest.json + theme.css header")

    # sync + validate
    theme = sync_settings(theme, version, bullets)
    theme = sync_creator(theme)
    validate(theme)

    if dry:
        print("\n— generated 'What's new' note —\n")
        sm = re.search(r'bu-whatsnew-note.*?description: "(.*?)"\n', theme, re.S)
        print(sm.group(1).replace("\\n", "\n") if sm else "(?)")
        print("\n— GitHub release notes (from README) —\n")
        print(bullets)
        print("\nDry run: no files written, nothing committed or pushed.\n")
        return

    write(THEME, theme)
    write(MANIFEST, manifest2)
    step("wrote files")

    # confirm before anything outward-facing
    status = run(["git", "status", "--short"]).stdout.strip()
    print("\nAbout to commit, tag, push to main, and publish the GitHub release.")
    print("Working-tree changes to be committed:\n" + (status or "  (none?)"))
    if not assume_yes:
        if input("\nProceed? [y/N] ").strip().lower() not in ("y", "yes"):
            die("aborted — files are stamped/synced locally but nothing was committed.")

    # ship
    run(["git", "add", "-A"]).check_returncode()
    subject = f"Release {version}"
    body = "\n".join(b.lstrip("- ").strip() if b.lstrip().startswith("-") else b for b in bullets.splitlines())
    msg = f"{subject}\n\n{body}\n\nCo-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
    r = run(["git", "commit", "-m", msg])
    if r.returncode:
        die(f"git commit failed:\n{r.stderr or r.stdout}")
    run(["git", "tag", "-a", version, "-m", f"Bureau {version}"]).check_returncode()
    step("committed + tagged")
    for push in (["git", "push", "origin", "main"], ["git", "push", "origin", version]):
        r = run(push)
        if r.returncode:
            die(f"{' '.join(push)} failed:\n{r.stderr}")
    step("pushed main + tag")
    r = run(["gh", "release", "create", version, THEME, MANIFEST,
             "--title", f"{version}", "--notes", bullets])
    if r.returncode:
        die(f"gh release create failed (commit/tag are pushed; finish the release by hand):\n{r.stderr}")
    print(f"\n  ✓ released v{version} → {r.stdout.strip()}\n")


if __name__ == "__main__":
    main()
