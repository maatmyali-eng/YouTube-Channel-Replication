# Shorts Pre-Publish Gate

> **Purpose:** Decide GO, FIX, or STOP for each Short before it goes public, and understand how Shorts views relate to the monetization thresholds.
> **Use when:** Every Short is finished and exported, before you upload it publicly.
> **Time needed:** 15 to 25 minutes per Short.
> **Needs:** The exported file, the script table, `music-log.csv`, `visuals-log.csv`, a free AI chat assistant.
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [STYLE_BIBLE], [SHORTS_DNA].
- The final script table (`shorts/<slug>/script.md`) and the Unlisted test upload from `04-vertical-visuals-and-editing.md`.
- The originality score from P-ORIG-01 (run it from [../05-originality-layer/02-scoring-rubric.md](../05-originality-layer/02-scoring-rubric.md) on the Short's script, and use that file's pass mark).
- Prompt-specific placeholders: [GATE_FACTS] (the filled form in Step 1), [METADATA_PACK] (title, description, hashtags), [ORIG_SCORE] (the P-ORIG-01 result), [GATE_NOTES] (anything unusual).

## Steps

1. **Fill the gate form.** Create `shorts/<slug>/gate.md` and fill every line honestly. Write "n/a" only where the line truly does not apply.

```
GATE FORM
slug:
length_s:            aspect (must be vertical or square):
file name:           resolution:
hook_code:           structure_code:           loop_code:
first spoken line:
last spoken line:
claim (one sentence):
payoff (one sentence):
proof asset (what I filmed or made):
own-asset share of seconds (percent):
source is my own long video? (yes / no; if yes, P-SHORT-10 result):
music option (A none / B Audio Library / C Shorts picker / D own):
tracks logged in music-log.csv? (yes / no):
third-party visuals logged in visuals-log.csv? (yes / no / none used):
synthetic voice? (yes / no):   realistic synthetic person, voice, or scene? (yes / no):
sponsor, affiliate, free product, or paid promotion? (yes / no):
topic touches health, money, law, or safety? (yes / no):
numbers and safety claims verified in an official source? (list the sources):
P-SHORT-09 verdict:      P-ORIG-01 score and pass mark:
variety plan check (batch rules) result:
title (60 characters or fewer):
description:
hashtags (3 or fewer):
```

2. **Run P-ORIG-01** and paste the result into the form. A score below the pass mark defined in the scoring file is a FIX at minimum.
3. **Run P-SHORT-06** with the form as [GATE_FACTS]. Read the table. Resolve every STOP before anything else.
4. **Apply the rule.**

| Verdict | Rule | What you do |
|---|---|---|
| STOP | One or more STOP items fail | Do not publish. Rework the Short or discard it. Re-run the gate on the new version. |
| FIX | No STOP items fail, but one to three FIX items fail | Repair the listed items and re-run only those checks, then run P-SHORT-06 once more. |
| STOP (by count) | More than three FIX items fail | Treat as STOP. A Short with that many problems needs a rewrite, not patching. |
| GO | No STOP and no FIX | Upload. |

**STOP items** (this repo's gate, built from YouTube's policies; each one stands alone):

| # | Check | Fails when |
|---|---|---|
| S1 | Synthetic media | A real person's voice or likeness is cloned or imitated, or a realistic synthetic person, voice, or scene has no disclosure plan. YouTube requires disclosure of realistic altered or synthetic content in Studio ("Altered content" or "Altered or synthetic content", wording VERIFY BEFORE RELYING); it does not require it for clearly unrealistic, animated, or minor edits (verified 2026-10-20, `appendices/research-snapshot.md`). |
| S2 | Third-party material | Any footage, audio, script text, thumbnail, logo, or character from another creator, a film, a TV show, or a song is in the Short, or any third-party asset is missing from the logs. |
| S3 | Music claim risk | Any music outside options A, B, C, or D. A Short over 1 minute with claimed content is blocked and not eligible for monetization (verified 2026-10-20). |
| S4 | Reused or templated | The Short is a straight crop of any video, or fails P-SHORT-10, or fails the variety rules for the batch. |
| S5 | Bait | The title, hook, or on-screen text promises something the Short does not deliver. |
| S6 | Unverified high-stakes claim | A health, money, legal, or safety claim stated as certain without an official source (see [../05-originality-layer/03-sensitive-topics-and-personas.md](../05-originality-layer/03-sensitive-topics-and-personas.md); AI personas discussing sensitive topics such as health or finance are a named non-monetizable category, verified 2026-10-20). |
| S7 | Undisclosed promotion | A sponsor, affiliate relationship, free product, or paid promotion exists and is not disclosed. YouTube can auto-label undisclosed branded content (announced 3 September 2026, `appendices/research-snapshot.md`). |
| S8 | Guideline violation | The content breaks YouTube's Community Guidelines or advertiser-friendly guidelines, shows minors in a risky or exploitative way, or is graphic or distressing. |

**FIX items:**

| # | Check | Fails when |
|---|---|---|
| F1 | Format | Not vertical or square, or longer than 3 minutes (it would publish as a regular video), or not 1080 x 1920 |
| F2 | Hook | The first second lacks a hook in picture and in sound or text together |
| F3 | Promise | The promise is not clear by the third second |
| F4 | Loop | The loop seam is audible or visible, or the Short feels incomplete without it |
| F5 | Word budget | Voiceover above its budget, or the table has time gaps |
| F6 | Own proof | Less than 50 percent of seconds show your own material, or the proof asset is missing |
| F7 | Safe zone | Any caption, face, or key object sits in the margins from [SAFE_ZONE_RULE], or the important line sits below y = 1248 |
| F8 | Audio | Voice peaks above -1 dBTP, music not 15 to 20 dB under the voice, or clipping |
| F9 | Metadata | Title above 60 characters, misleading wording, or description copied from another video; more than 3 hashtags (the limits are this repo's; YouTube's own hashtag limits are VERIFY BEFORE RELYING) |
| F10 | Logs | `music-log.csv` or `visuals-log.csv` incomplete |
| F11 | Similarity | The Short repeats a claim, hook skeleton, or first picture of any of your last 5 Shorts |
| F12 | Originality | P-ORIG-01 score below its pass mark |
| F13 | Phone check | Not watched on a phone with the description expanded |

5. **Upload the passing Short.** In YouTube Studio click Create > Upload videos > select the file > Title > Description > Audience: choose "No, it's not made for kids" unless it is (menu wording VERIFY BEFORE RELYING). Answer the "Altered content" question per S1. Next through the checks step (wait for the copyright check to finish; if it flags anything, you have a STOP: remove the audio, re-export, re-upload). On the visibility step choose Schedule and set the date and time from your calendar, or Public.
6. **Log after publishing.** At 48 hours and at 7 days, copy numbers into the `Publish-Log` tab of `shorts-batch-plan` (see `03-batch-scripts.md`) and into [../09-operations/03-tracking-sheet.md](../09-operations/03-tracking-sheet.md). Use Studio > Analytics > Content > Shorts, and record both total views and engaged views (Advanced mode, VERIFY BEFORE RELYING).

## What Shorts views do and do not do for monetization

(verified 2026-10-20, from YouTube's 10 August 2026 announcement as reported by vidIQ, AIR, and others, plus `appendices/research-snapshot.md`; confirm every number on YouTube Help, "YouTube Partner Program overview and eligibility", before you rely on it, VERIFY BEFORE RELYING.)

**Shorts watch hours do not count.** Shorts views and long-form watch hours never combine. Shorts watch time does not count toward the 3,000, 4,000, or 8,000 watch-hour paths, and long-form watch hours do not count toward the Shorts-view path. You must meet one route in full. For example, 7 million Shorts views plus 2,500 long-form hours does not qualify for the 10 million views or 4,000 hours route.

| Stage | Subscribers and uploads | Performance route (choose one) | Window |
|---|---|---|---|
| Tier 1: fan funding, shopping | 500 subscribers and 3 public uploads in 90 days | 3,000 public watch hours, or 3 million Shorts views | 12 months for hours, 90 days for views |
| Tier 2 before 1 Feb 2027 (ads and Premium share) | 1,000 subscribers | 4,000 public watch hours, or 10 million Shorts views | 12 months for hours, 90 days for views |
| Tier 2 for new applicants from 1 Feb 2027 | 1,000 subscribers | 8,000 public watch hours, or 20 million Shorts views | 12 months for hours (reported as 365 days), 90 days for views |
| Shorts revenue sharing from 1 Feb 2027 | Partner Program member who accepted the Shorts Monetization Module | 10 million Shorts views in the previous 90 days | Rolling 90 days |

Applying before 1 February 2027 uses the lower Tier 2 thresholds. As of 2026-10-20 that date is 104 days away. Tier 1 core eligibility is reported as unchanged. Shorts ad revenue comes from the Shorts feed and is separate from long-form revenue, and views from before you accept the Shorts Monetization Module do not earn Shorts revenue (verified 2026-10-20, YouTube Help).

Two cautions. First, YouTube said in March 2025 that earnings and eligibility stay based on "engaged views", the metric that replaced the old Shorts view count, while public view counts now include every start and replay (verified 2026-10-20, TechCrunch, 26 March 2025). Check which metric YouTube's current eligibility page uses. Second, only "qualified public" views count, so private, unlisted, deleted, or policy-violating Shorts do not help.

**Timeline arithmetic.** A route that needs 90 days of views is a pace, not a date. The table divides each target by the 90-day window and by the number of Shorts you publish in it. Rounded to the nearest whole view.

| Target in 90 days | Per day | Average views needed per Short if you publish 30 | 60 | 90 |
|---|---|---|---|---|
| 3 million (Tier 1 route) | 33,333 | 100,000 | 50,000 | 33,333 |
| 10 million (Tier 2 before Feb 2027, or Shorts revenue sharing) | 111,111 | 333,333 | 166,667 | 111,111 |
| 20 million (Tier 2 from Feb 2027) | 222,222 | 666,667 | 333,333 | 222,222 |

How to read it. Views are not spread evenly. A few Shorts usually produce most views, so an average of 33,333 views per Short might come from one or two breakout Shorts and many small ones. Publishing 90 Shorts in 90 days to reach a target is also the mass-production pattern the inauthentic-content policy targets, so the number of Shorts is limited by the quality and variety you can sustain, not by the formula. This file makes no income or timeline promise. The 10 to 30 day income plan in this repo does not depend on the Shorts-view routes; read [../08-monetization/01-reality-and-timeline-math.md](../08-monetization/01-reality-and-timeline-math.md) and [../08-monetization/03-parallel-routes.md](../08-monetization/03-parallel-routes.md) for the routes that do not need these thresholds.

## Prompts

### P-SHORT-06 — Shorts Gate Review

**Purpose:** Apply the STOP and FIX checks to one Short and return a verdict.
**Inputs:** [CHANNEL_NAME], [NICHE], [LANGUAGE], [GATE_FACTS] (the filled gate form), [SCRIPT_TABLE], [METADATA_PACK], [ORIG_SCORE], [GATE_NOTES].

```
You are a strict pre-publish reviewer for YouTube Shorts on the channel [CHANNEL_NAME] (niche [NICHE], language [LANGUAGE]). Your job is to find reasons NOT to publish. Do not praise and do not guess; if the information to judge a check is missing, mark it MISSING and treat it as FAIL.

GATE FORM: [GATE_FACTS]
SCRIPT AND BEAT TABLE: [SCRIPT_TABLE]
TITLE, DESCRIPTION, HASHTAGS: [METADATA_PACK]
ORIGINALITY SCORE AND PASS MARK: [ORIG_SCORE]
NOTES: [GATE_NOTES]

STOP CHECKS (any FAIL means STOP)
S1 Synthetic media: no cloned or imitated real person's voice or likeness; any realistic synthetic person, voice, or scene has a disclosure plan.
S2 Third-party material: no footage, audio, script text, logo, character, or likeness from another creator, film, TV show, or song; all third-party assets logged.
S3 Music: only option A none, B YouTube Audio Library, C Shorts sound picker, or D music I own; for any Short over 60 seconds only A, B, or D.
S4 Reused or templated: not a straight crop of any video; if derived from my own long video it passed the five-point difference test; it passes the batch variety rules.
S5 Bait: the title, hook, and text promise only what the Short delivers.
S6 High-stakes claims: any health, money, legal, or safety claim is general and tied to an official source.
S7 Promotion: any sponsor, affiliate, free product, or paid promotion is disclosed.
S8 Guidelines: nothing violates Community Guidelines or advertiser-friendly guidelines.

FIX CHECKS (more than 3 FAIL means STOP by count)
F1 Vertical or square, 3 minutes or less, 1080 x 1920. F2 Hook in picture and sound or text in the first second. F3 Promise clear by the third second. F4 Loop seam clean and the Short is complete without it. F5 Voiceover within budget and table has no time gaps. F6 At least 50 percent own material. F7 Safe zone respected (x 60 to 880, y 290 to 1440, key caption above y 1248). F8 Audio peaks below -1 dBTP and music 15 to 20 dB under voice. F9 Title 60 characters or fewer, not misleading, description original, 3 hashtags or fewer. F10 Logs complete. F11 No repeat of claim, hook skeleton, or first picture from the last 5 Shorts. F12 Originality score at or above its pass mark. F13 Watched on a phone with the description expanded.

OUTPUT
1. A table with columns Check | PASS, FAIL, or MISSING | Evidence from the form (quote the form line) | Exact fix.
2. The count of STOP fails and FIX fails.
3. One verdict word: STOP, FIX, or GO. STOP if any S check fails or if FIX fails exceed 3. FIX if 1 to 3 F checks fail and no S check fails. GO otherwise.
4. A one-sentence reason and, for FIX or STOP, the single most important next action.
5. A final line: "Confirm the altered-content answer and every numeric threshold on YouTube Help before you publish."
```

**Expected output:** A check table, counts, one verdict word, and the next action.
**If the output is weak:** If it returns GO while a form line is blank, reply: "Re-run the review and mark every blank form line MISSING, which counts as FAIL."

## Done when

- `shorts/<slug>/gate.md` is filled with no blank line that applies to the Short.
- P-SHORT-06 returned GO, or every FIX item was repaired and the review re-run and returned GO.
- You confirmed the Altered content answer and the Shorts-view and watch-hour thresholds on YouTube Help on the date you published.
- The Short is scheduled with a date from your cadence plan, and the 48 hour and 7 day log entries are in your calendar.
- You know that Shorts watch time does not count toward any watch-hour route and that no route here is promised on a date.

## Next

Continue to [../04-thumbnails/01-thumbnail-dna-analysis.md](../04-thumbnails/01-thumbnail-dna-analysis.md).
