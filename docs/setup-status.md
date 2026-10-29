# Setup status

Last checked: 2026-10-29 (cloud session). Re-check at the start of any session where it matters; connections change.

## Integrations

| Tool | Status | Verified | Limits / notes |
|---|---|---|---|
| Klaviyo | Connected | Read account details and 5 recent campaigns. Account: Scent Pilot (ID RvjE97), timezone US/Eastern. | One account per connection. Other brands not reachable yet. Tools exist to create drafts, schedule, send and edit flows: never schedule/send/activate without Danie's explicit approval. |
| Figma | Connected | `whoami`: handle Triple Threat Growth, manage@3tgrowth.com, plan "manage's team" (Starter), Full seat, admin. | Can read files, screenshot, create files, edit via Plugin API, generate images (costs Figma AI credits). Starter plan has tighter MCP rate limits. Not yet tested on a real file. |
| Google Drive | Connected | Listed recent files and the clients folder as danie@3tgrowth.com. | Can read, search, create Docs (HTML conversion), share. Cannot create Doc tabs (manual step). |
| Asana | Connected 2026-10-29 | `get_me`: Danie, danie@3tgrowth.com, one workspace (gid 1209393728012217). | Project structure not yet inspected. |
| GitHub | Repo `3t-marketing-ops` | See session log. | Holds this file. Cloud sessions are wiped; commit and push at the end of every session. |

## Skills

| Skill | Status |
|---|---|
| `/mx` | Installed, read in full |
| `/ttm-email-copy-format` | Installed, read in full |

## Brand information sources

- Claude Projects: NOT reachable from Claude Code.
- Google Drive clients folder contains folders for: Scent Pilot, Habituel, Valveman, GameFools, Welsford Co, FS Welsford, UpMatch, Retro Muscle, Little Hands and Nature, Carzan Local Meat (plus Archives, Agreements, SOP, Triple Threat Growth).
- Scent Pilot Drive docs seen (not yet read): "Value Offer Worksheet - SP", "Customer Avatar & Before After - SP.docx", folders "Campaigns" and "Flows".
- Habituel Drive docs seen (not yet read): "November 2026 - Habituel", "Habituel Brand Guidelines.pdf".

## Open setup steps (in order)

1. [ ] When starting a new Claude Code session, select the `3t-marketing-ops` repository so `CLAUDE.md` loads automatically. (Repo exists and is pushed as of 2026-10-29.)
2. [ ] For each brand: copy its Claude Project instructions + key knowledge into one Google Doc in that client's Drive folder, named `Brand Reference - <Brand>`. Claude then builds `brands/<slug>/` from it.
3. [ ] Add team names, roles and Asana assignees to `docs/team.md`.
4. [ ] Inspect Asana project structure and record conventions in `docs/asana-conventions.md` (read-only first).
5. [ ] Share the Figma email template file link(s) per brand.
6. [ ] Decide how to reach Klaviyo for brands other than Scent Pilot.
7. [ ] Run the pilot (one brand, one campaign, idea -> copy doc -> Figma support -> Asana task).
