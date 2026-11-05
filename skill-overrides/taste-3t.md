# 3T taste: overrides and additions to the TTM copy skill

Read after the TTM skill's own `references/taste.md`. Entries here win when they conflict. Same format: `3T-<nn> <default>` / strength / source / notes.

**3T-01 Danie is the reviewer.** Every "Tristan" in the TTM skill means Danie.
Strength: stated. Source: Danie, 2026-10-29.

**3T-02 US English and USD ($) by default.** Replaces TTM T38 (UK English, GBP). A brand file can override.
Strength: stated. Source: Danie, 2026-10-29.

**3T-03 Doc title: `Brand | Flow or Campaign | Path or Month`.** Replaces TTM `Client | Flow | Path`.
Strength: seen once (judgement, accepted with the setup). Source: setup session 2026-10-29.

**3T-04 The TTM copy doc IS the brief.** Use /ttm-email-copy-format for briefs; no separate MX brief unless asked.
Strength: stated. Source: Danie, 2026-10-31.

**3T-05 Each sale gets its own code.** Never reuse one sale's code in another sale's emails (Scent Pilot: Veterans Day REMEMBER15, Black Friday BLACKFRIDAY15).
Strength: seen once. Source: Danie, 2026-10-31 (F002).

**3T-06 Campaign brief layout follows Danie's TERRA example.** Heading `Campaign | <Type> | <Campaign Title>`; meta table has 3 rows only (Email name = heading + `| Designed` or `| Plain text`, Send date, Brief); Brief is 1 to 2 short sentences (audience + what the email does). Designer notes go in the Notes tab, not the meta table. Example: Drive doc "TERRA | Meet the Bike You Could Win".
Strength: stated. Source: Danie, 2026-10-31 (F004).

**3T-07 Deliver briefs into Danie's Google Doc, one tab per email.** No HTML files handed to Danie. The month's doc lives in the brand's Campaigns folder (Scent Pilot: "November 2026 -SP").
Strength: stated. Source: Danie, 2026-10-31 (F004).

**3T-08 Don't spell out obvious offer mechanics** (e.g. "free shipping over $50" needs no "after discount" note).
Strength: seen once. Source: Danie, 2026-10-31 (F005).

<!-- Next ID: 3T-09 -->

## 3T-09: Designed emails need supporting sections
Danie (2026-10-31): emails with only hero + one grid feel thin. Give designed campaigns 5 to 7 sections, reusing modules from the brand's approved past designs (for Scent Pilot: notes breakdown, How It Works steps, Testing Before Investing, Everywhere else vs Scent Pilot, size and price ladder, review card, offer icons). Every module still uses verified facts only.

## 3T-10: YouTube emails use a graded video frame, not the thumbnail
Danie (2026-11-05): the YouTube thumbnail (big text, cut-outs) makes classy emails look cheesy. Use a clean frame from the video (i.ytimg.com/vi/<id>/maxres1-3.jpg), graded with tools/video_frame.py, full-bleed in the SP Video Feature component with fades and a thin play ring ("WATCH ON YOUTUBE"). No borders, no thumbnail text. Pick a frame with a real human moment.

## 3T-11: Product sections carry no prices
Danie (2026-11-05): "Please don't include pricing in the email product sections." Use "Available in 2ml, 5ml and 10ml." Size ladders show sizes and their line, no price.

## 3T-12: Use people in designs
Danie (2026-11-05): use images of humans relevant to the topic; place the real bottle photo into the scene with fades where needed.

