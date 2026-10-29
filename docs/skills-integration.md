# How /mx and /ttm-email-copy-format work together

Both skills were read in full on 2026-10-29 (cloud session). Invocation names: `/mx` and `/ttm-email-copy-format` (lowercase).

## What each one contributes

**/mx** (DTC email/SMS skill library)
- Brand research, voice analysis, monthly calendars, campaign briefs, flow plans and briefs, short-form copy, reports.
- Strict truth rules, a library of canonical email sections, text-based frameworks and SMS message types, flow templates (welcome, cart, checkout, browse, post-purchase, winback, sunset, VIP, replenishment, review request).
- Program doctrine: opt-in form, campaign volume, core flows first; segment later.
- Brand context contract: exactly four files per brand (profile, voice, products, memories).

**/ttm-email-copy-format** (ThriveTribe Media copy skill, borrowed by 3T)
- Writes and reviews email copy: S.C.E (skimmable, clear, engaging), one job per email, hooks not labels, 3 to 5 sentence hero subheadlines, reviews quoted in full, real deadlines, buttons that say what happens next.
- Delivers a Google Doc wireframe: one tab per email, meta table, subject table, single-column wireframe with nested card tables, Notes tab. Built as HTML, converted in Drive.
- Has a learning loop (taste defaults + feedback log) and a Python checker for the HTML.

## When each applies

| Task | Use |
|---|---|
| New brand onboarding, voice rules | /mx |
| Monthly calendar | /mx (+ 3T planning table) |
| Internal campaign/flow spec | /mx |
| Copy, subject/preview, team-facing brief doc | /ttm-email-copy-format |
| SMS copy | /mx (TTM skill says it is not for SMS-only work) |
| Copy review | both checklists |
| Reporting | /mx |

## Conflicts found and how 3T resolves them

| # | Conflict | Resolution |
|---|---|---|
| 1 | TTM skill is ThriveTribe Media's house style: Tristan reviews, UK English and GBP, doc title `Client \| Flow \| Path`. | Danie reviews. US English and $ by default. Title `Brand \| Flow or Campaign \| Path or Month`. (Confirmed by Danie 2026-10-29.) |
| 2 | MX briefs forbid subject lines, sample copy, voice and design direction. Danie's team brief needs all of those. | MX brief = short internal spec. TTM copy doc = the team-facing brief. Never stuff copy into the MX brief. |
| 3 | MX calendar = one sentence per send, explicitly no audience or creative notes unless asked. Danie asked for audiences, objectives, angles, offers, creative needs. | Keep the MX lineup and add a 3T planning table with those columns. |
| 4 | MX copy format (`[LOGO]`, `---`, `[FOOTER]`) vs TTM wireframe tables. | TTM wireframe for anything the team builds from. MX section labels still drive section order. |
| 5 | Two review systems: MX six-lens checklist (default verdict NEEDS REVISION, one revision max) and TTM review pass + pre-delivery checklist + taste check. | Compatible. Run both, allow one revision round, surface remaining findings to Danie. |
| 6 | Storage: MX wants `brand/<slug>/` in the skill folder or a Claude Project; TTM writes corrections into its own files. In cloud sessions skill files are synced copies, so neither persists. | Brand files live in `brands/<slug>/` in this repo. TTM corrections go to `skill-overrides/` in this repo. |
| 7 | Hero subheadline length: TTM wants 3 to 5 sentences; MX says stop when the point lands. | TTM rule for designed story/offer heroes; short for countdown/type-led heroes (TTM T26). Brand voice file can override. |

## Open questions to settle during the pilot

- Does the TTM HTML-to-Google-Doc conversion keep table widths when created through the Drive connector (TTM "route C")? Test on the pilot.
- Which designer will receive the doc, and should Figma work start from an existing brand template file?
