---
title: Bureau — Kitchen Sink
status: testing
tags: [bureau, qa, sample]
rating: 87
date: 2026-06-02
link: "[[Some Other Note]]"
url: https://obsidian.md
---

> [!INFO] How to use this note
> Drop this file into a test vault running Bureau and flip through it in **dark**, **paper (light)**, and **inverted-editor** modes — in both **reading** and **live-preview**. It exercises every surface the theme styles, so a glance catches regressions after an edit. Toggle Effects Mode (Low/Medium/High) and the accent presets while you're here.

# Heading 1 — the case file
## Heading 2 — section
### Heading 3 — subsection
#### Heading 4
##### Heading 5
###### Heading 6

Body text with **bold**, *italic emphasis*, ==a highlight==, ~~strikethrough redaction~~, and `inline code`. A run of normal prose to check line-height, measure, and the phosphor text-glow at default strength. Secondary detail in a smaller voice tends to use the faint/muted tokens — make sure it stays legible.

An [internal link](#), an [[Unresolved Link]], and an [external link](https://obsidian.md) with its chip. A #tag and a #nested/tag for good measure.

## Lists & tasks

- Unordered item
  - Nested item
    - Deeper still
- Another item

1. Ordered item
2. Second item
   1. Nested ordered

- [ ] Open task (empty box)
- [x] Done task (box should be white-on-dark / black-on-paper, accent check)
- [ ] Another open task

## Quote & rule

> A blockquote. Concrete and steel that were never trying to be warm.
> — someone in the Bureau

---

## Code

```js
// fenced code block with a language chip
function bureau(noir = true) {
  const accent = noir ? "control-red" : "deus-gold";
  return `the building was ${accent ? "on your side" : "indifferent"}`;
}
```

```
plain fenced block, no language
```

## Table

| Field      | Value            | Score |
| ---------- | ---------------- | ----: |
| Atmosphere | heavy, redacted  |    9  |
| Legibility | holding its breath | 8   |
| Cohesion   | one bad bulb     |    7  |

## Callouts

> [!note] Note callout
> Body text inside a note callout.

> [!tip] Tip
> With **bold** that renders as a redaction stamp.

> [!warning] Warning
> Caution lives here.

> [!danger] Danger
> The red of a door you shouldn't open.

> [!question] Question
> Would I actually use this?

> [!example] Example
> A worked example.

## Math

Inline math: $e^{i\pi} + 1 = 0$ sits in the line.

$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$

## Footnotes

A claim that needs a source.[^1] And another.[^2]

[^1]: The first footnote, down in the divided block.
[^2]: The second, with a backref.

## Embed

![[Some Other Note]]

## Image

![alt text](https://obsidian.md/images/obsidian-logo-gradient.svg)
