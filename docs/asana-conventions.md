# Asana conventions

Inspected read-only 2026-10-31 from "Scent Pilot Monthly Email Campaign" (project 1219903511290453). The project was built from a template (project note: "This is an example of how to setup our monthly email campaign calendars. Please duplicate and rename for the client.").

Workspace: 3tgrowth.com (gid 1209393728012217).

## Structure
- Sections: "Client Folder Brand Assets. + Notes" (brand links), "Monthly Campaigns Section TEMPLATE" (do not edit), one section per month (Danie: name it like "November 2026").
- One parent task per email, including plain-text emails. Plain-text emails get no GD subtask. **Task name = the campaign title** (Danie, 2026-10-31).
- Each parent task has a design subtask named `GD: <campaign title>`. Send Date field format: M/D (e.g. 11/9). Template notes: "Please design this campaign: / Schedule: <M/D> @<time> <timezone>".
- Parent (copy) tasks go to Jeoff, due well ahead of the send (Danie sets the dates per month).
- Design subtasks: create them, but assign and date them only when Danie says so. Designer due dates, when set: 2 to 3 days before the send date (Danie, 2026-10-31). Claude's rule: 3 days before; if that falls on a weekend, 2 days before; if still a weekend, the Friday before.

## Custom fields (on every task)
| Field | Type | Options |
|---|---|---|
| Send Date | text | free text |
| Send Time | text | free text |
| Audience | multi-select | Tier 1, Tier 2, Tier 3, Everyone |
| Status | multi-select | Working On It, Assigned to Designer, Scheduled, Sent, Stuck |
| Exclusions | multi-select | Last 14 Day Buyers + Marked As Spam Or Bounced |

## Rules for Claude
- Never edit the TEMPLATE section or its tasks.
- Before creating, list the project's tasks and skip any that already exist with the same name in the same section.
- Show Danie the batch first; once approved, create the whole batch without asking per task.
