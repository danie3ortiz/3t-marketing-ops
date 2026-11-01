# Setup status

Last checked: 2026-10-29 (cloud session). Re-check at the start of any session where it matters; connections change.

## Integrations

| Tool | Status | Verified | Limits / notes |
|---|---|---|---|
| Klaviyo | Connected | Read account details and 5 recent campaigns. Account: Scent Pilot (ID RvjE97), timezone US/Eastern. | One account per connection. Other brands not reachable yet. Tools exist to create drafts, schedule, send and edit flows: never schedule/send/activate without Danie's explicit approval. |
| Figma | Connected | `whoami`: handle Triple Threat Growth, manage@3tgrowth.com, plan "manage's team" (Starter), Full seat, admin. | Can read files, screenshot, create files, edit via Plugin API, generate images (costs Figma AI credits). Starter plan has tighter MCP rate limits. Read-tested on the Scent Pilot file 2026-10-31 (metadata, variables, inline screenshots). Image downloads to the container are blocked by the network; use inline screenshots. 2026-11-01: the Scent Pilot file sits in another Figma team where manage@3tgrowth.com has no Full seat, so edits there are refused (read-only works). Claude drafts go in the 3T file "Scent Pilot | 3T Design Drafts" (key Je4icun0HdikTq1AlQp6es, manage's team); a designer copies frames into the client file. |
| Google Drive | Connected | Listed recent files and the clients folder as danie@3tgrowth.com. | Read, search, create, export. |
| Google Docs | Connected 2026-10-31 | Wrote 4 email tabs + Notes into "November 2026 -SP" (tables, nested card tables, styles). | read_doc output is large (saved to file); use `tools/gdoc_brief_builder.py`. |
| Network | scentpilot.com allowed 2026-10-31; youtube.com and mcp.figma.com (Figma image uploads) allowed 2026-11-01 | products.json and product pages (with Loox reviews server-rendered) readable. | loox.io still blocked (403); not needed because reviews render on product pages. Figma image downloads blocked; use inline screenshots. |
| Asana | Connected 2026-10-29 | `get_me`: Danie, danie@3tgrowth.com, one workspace (gid 1209393728012217). | Conventions in `docs/asana-conventions.md`. |
| Atlassian (Jira/Confluence) | Connected 2026-10-30 | Not used. | Danie: may be handy later, not needed now. |
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
2. [ ] (Scent Pilot done 2026-10-31) For each brand: copy its Claude Project instructions + key knowledge into one Google Doc in that client's Drive folder, named `Brand Reference - <Brand>`. Claude then builds `brands/<slug>/` from it.
3. [x] Team names and roles in `docs/team.md` (2026-10-31). Asana user IDs still to add.
4. [x] Asana conventions recorded in `docs/asana-conventions.md` (2026-10-31).
5. [x] Scent Pilot Figma file shared and reviewed (2026-10-31). Other brands: share links when needed.
6. [ ] Decide how to reach Klaviyo for brands other than Scent Pilot.
7. [ ] Run the pilot (one brand, one campaign, idea -> copy doc -> Figma support -> Asana task).
