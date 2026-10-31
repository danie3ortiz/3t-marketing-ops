# Tools

## gdoc_brief_builder.py

Writes TTM-format briefs (TERRA layout) straight into a Google Doc tab through the Google Docs connector. It works out every insert position in advance, so one email = one `update_doc` batch, including nested card tables.

How Claude uses it:
1. Write the month's email content in a content file (example: `brands/scent-pilot/copy/2026-11-batch1-gdoc-content.py`) using the helpers: `H2`, `meta`, `subj`, `wire`, `cards`, `P` (`**bold**` markup; styles `b`, `i`, `hero`, `h15`, `ph`, `small`, `link`).
2. Create one tab per email with `addDocumentTab` (each new tab starts empty at index 1).
3. Run `python3 <content file> <email number> <tabId>` to print the requests, read the doc for the latest `revisionId`, then send the batch with `update_doc` and `writeControl.requiredRevisionId`.
4. Verify with Drive `read_file_content` and a PDF export render.

Only use it on an EMPTY tab: the positions assume the tab starts with a single empty paragraph.
