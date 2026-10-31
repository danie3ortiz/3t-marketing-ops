# Triple Threat Growth (3T): agency operating instructions

Claude Code reads this file at the start of every session in this repo. It holds agency-wide rules only. Brand facts live in `brands/<slug>/`, never here.

## Who we are

- Agency: **Triple Threat Growth (3T)**, an email and SMS marketing agency serving multiple DTC brands.
- Owner: **Danie** (danie@3tgrowth.com). Danie reviews and approves every copy doc, calendar and brief.
- Team: see `docs/team.md` (Joyce, Executive; Jeoff, Copywriter; Kheen and Jeson, Graphic Designers).
- Work: monthly email/SMS campaign calendars, automated flows, copywriting, design, Klaviyo implementation, reporting.

## Tools

| Tool | Role | Notes |
|---|---|---|
| Klaviyo | Campaigns, flows, segments, reporting | MCP connection reaches ONE account at a time (currently Scent Pilot). Always confirm which account is connected before touching data. |
| Figma | Email graphics and design | MCP connected as the Triple Threat Growth account (Starter plan, tighter MCP rate limits). Client review process: `docs/figma-review-workflow.md`. |
| Google Drive / Docs | Briefs and copy docs | Drive + Google Docs connectors. Briefs are written straight into Danie's monthly Google Doc, one tab per email, with `tools/gdoc_brief_builder.py` (see `tools/README.md`). Never hand Danie HTML files. |
| Atlassian | Jira / Confluence | Connected but not used for now. |
| Asana | Planning, assignments, deadlines, production tracking | Connected. Inspect existing project structure before creating anything. |
| Claude skills | `/mx` and `/ttm-email-copy-format` | See "How the two skills work together" below and `docs/skills-integration.md`. |

## Non-negotiable rules

1. **Truth rule.** Never invent brand details, products, prices, offers, codes, deadlines, links, claims, reviews, testimonials, metrics or integration capabilities. Write `missing info: <what>` and list it.
2. **Brand separation.** Only read the `brands/<slug>/` folder for the brand being worked on. Never carry voice, offers, links, reviews or lines from one brand into another. If the connected Klaviyo account does not match the brand being worked on, stop and say so.
3. **Approvals.**
   - Ask before: scheduling or sending any campaign, activating or editing a live flow, changing segments/lists/profiles, changing any live Klaviyo or account setting, sharing files outside 3T.
   - Safe without asking: reading data, drafting docs, creating Klaviyo drafts only when Danie asked for drafts.
   - Asana: once Danie authorizes a batch of updates, carry out the whole batch without asking per task. Before creating, inspect the existing projects and conventions and search for duplicates.
4. **Source of truth.** Approved calendars and briefs win over chat memory or earlier drafts.
5. **Language and format.** US English and USD ($) by default, unless a brand file says otherwise. ASCII punctuation only: no em dashes, en dashes or curly quotes.
6. **Check before claiming.** Verify which skills, files and integrations are actually available before saying something can be done.

## How Danie wants Claude to work

- Danie is new to Claude Code. Explain setup steps in plain language, one at a time.
- Do the work you can do instead of handing Danie manual steps.
- Ask focused questions only when needed; label assumptions.
- Keep the initial setup simple; propose automation only when it solves a clear, repeated problem.

## How the two skills work together

Use both. Read `docs/skills-integration.md` for the full reasoning. Short version:

| Stage | Skill | Output |
|---|---|---|
| Brand context | `/mx` brand research + voice analysis | `brands/<slug>/profile.md`, `voice.md`, `products.md`, `memories.md` |
| Monthly calendar | `/mx` calendar builder | MX one-sentence lineup PLUS a 3T planning table (date, channel, audience, objective, angle, confirmed offer, creative needs) because Danie asked for those fields |
| Briefs + copy | `/ttm-email-copy-format` | THE brief (Danie, 2026-10-31: "for the briefs I really want us to use /ttm-email-copy-format"). Google Doc wireframe: subject, preview, sender, every section, buttons, links, designer notes, Notes tab. Skip the MX internal spec unless Danie asks for it. |
| Review | Both | TTM review pass + checklist and taste check, plus MX six-lens checklist. One revision round, then surface what's left |
| Reporting | `/mx` report | Real Klaviyo data only; flag gaps |

### 3T overrides to the TTM skill (these beat the skill's defaults)

The TTM skill was written for ThriveTribe Media. 3T borrows its structure and quality bar with these changes:

- **Reviewer is Danie**, not Tristan. Read every "Tristan" in the skill as "Danie".
- **US English and $** by default (the skill defaults to UK English and GBP).
- **Doc title:** `Brand | Flow or Campaign | Path or Month`, for example `Scent Pilot | Campaign | November 2026`.
- **Share copy docs with the 3T team**, not "TTM".
- **Learning loop:** the skill's own files are read-only copies in cloud sessions, so corrections are logged in THIS repo: `skill-overrides/feedback-log.md` and `skill-overrides/taste-3t.md`. Read `taste-3t.md` after the skill's own `taste.md`; entries there win when they conflict.
- Brand voice files in `brands/<slug>/voice.md` and approved client lines beat both skills' defaults.

### 3T overrides to the MX skill

- MX brand context storage = `brands/<slug>/` in THIS repo (not the skill directory, not a Claude Project). Work artifacts go in `brands/<slug>/calendar/`, `briefs/`, `copy/`, `flows/`, `reports/`, named `YYYY-MM-DD-title.md`.
- Calendars include the 3T planning table described above (Danie explicitly requested audience, objective, angle, offer, creative needs).
- Final team-facing copy uses the TTM wireframe, not MX's `[LOGO]`/`---`/`[FOOTER]` markdown. MX's section labels still decide the section order.

## Repo map

```
CLAUDE.md                     agency rules (this file)
brands/index.md               registry of brands and their status
brands/_template/             blank brand files to copy for a new brand
brands/<slug>/                one folder per brand: profile, voice, products, memories + work artifacts
docs/setup-status.md          what's connected, what's verified, open setup steps
docs/skills-integration.md    full comparison of /mx and /ttm-email-copy-format and conflict resolutions
docs/session-log.md           dated log of what was done each session
skill-overrides/              3T taste and feedback log for the TTM copy skill
tools/                        helper scripts (Google Doc brief builder)
```

## End of every session

Update `docs/session-log.md` with what was done and what's next, then commit and push so nothing is lost (cloud sessions are wiped).
