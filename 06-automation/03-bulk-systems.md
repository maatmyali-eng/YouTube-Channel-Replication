# Bulk Systems: Batch Research, Scripts, Shorts, Thumbnails, and Metadata

> Purpose: Run the pipeline in weekly batches with one workspace, one naming scheme, one status system, and a routine sized to [WEEKLY_HOURS].
> Use when: Your first video has passed all eleven stages by hand (see `01-pipeline-architecture.md`) and you want to repeat the work faster.
> Time needed: 60 minutes to set up the workspace, then one weekly batch routine.
> Needs: The `Pipeline` sheet from `02-no-code-workflow.md`, the [STYLE_BIBLE], a folder on your computer or Google Drive.
> Cost: $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [WEEKLY_HOURS], [FACE_OR_FACELESS], [VOICE_MODE], [VIDEO_LENGTH], [STYLE_BIBLE]
- The `Pipeline` tab with its 22 headers and the status dropdown

## The rule that keeps bulk work monetizable

YouTube's inauthentic content policy, clarified 16 July 2026, names generic, repetitive, or template-based content with little variation between videos as non-monetizable (verified 2026-10-20). It targets mass production, not AI. Batching is a scheduling method. It becomes mass production when the batch has the same hook, the same structure, the same thumbnail layout, and no first-hand material in every item. Every batch in this file therefore has a caps rule and a variation check. The caps below are this repo's rules, not YouTube numbers.

## Steps

### Part 1. Create the workspace

1. Create a folder named `[CHANNEL_NAME]-workspace` on your computer or in Google Drive. Create the subfolders below. The file names inside each video folder match the output names in `01-pipeline-architecture.md`.

```
[CHANNEL_NAME]-workspace/
  dna/
    style-bible.md
    video-dna.md
    shorts-dna.md
    pipeline-plan.md
  batches/
    2026-W43/
      batch-plan.md
      topics.tsv
      shorts-plan.tsv
      thumb-briefs.tsv
  videos/
    L012-lentil-stew-under-3-dollars/
      topic.md
      value-stack.md
      outline.md
      script.md
      factcheck.md
      voice.wav
      captions.srt
      clips/
      edit-notes.md
      final.mp4
      metadata.md
      disclosure.md
      orig-score.md
      review-log.md
    S031-three-pantry-swaps/
      (same files, shorter)
  thumbnails/
    thumb-dna-[CHANNEL_NAME].md
    asset-log.csv
    L012-lentil-stew-under-3-dollars/
      thumb-A.jpg
      thumb-B.jpg
      thumb-C.jpg
  archive/
```

2. Put the link to the `[CHANNEL_NAME] Pipeline` sheet in a text file named `sheet-link.txt` at the workspace root.

### Part 2. Naming conventions

| Item | Pattern | Example |
|---|---|---|
| Long video slug | `L` + three digits + `-` + 3 to 6 lowercase words with hyphens | `L012-lentil-stew-under-3-dollars` |
| Short slug | `S` + three digits + the same | `S031-three-pantry-swaps` |
| Counters | Never reused, never renumbered, even when a video is killed | `L013` stays unused if killed |
| Batch folder | ISO week: year + `-W` + two digits | `2026-W43` |
| Drafts | Add `-v2`, `-v3`; the file without a suffix is the approved version | `script.md`, `script-v2.md` |
| Dates inside files | `YYYY-MM-DD` | `2026-10-20` |
| Thumbnails | `thumb-A.jpg`, `thumb-B.jpg`, `thumb-C.jpg` | |
| Language suffix | Add only when you make a second language | `script.es.md` |

The slug in column A of the `Pipeline` sheet must equal the folder name exactly.

### Part 3. The status column system

Column C of `Pipeline` holds one status per row. A status means "this step is complete". The next step may not start until the status is set.

| Status | Set by | Gate passed | Next action | Stale after |
|---|---|---|---|---|
| IDEA | You or P-AUTO-02 | none | Fill columns F and G | 14 days |
| APPROVED | You only | C1 | Run script draft | 7 days |
| SCRIPTED | Make or you | none | Edit, fact-check, run P-ORIG-01 | 7 days |
| SCRIPT_OK | You only | C2 | Voice | 5 days |
| VOICED | You only | C3 | Visuals | 5 days |
| VISUALS_DONE | You only | C4 | Edit | 5 days |
| EDITED | You | none | Thumbnails | 3 days |
| THUMB_DONE | You only | C5 | Metadata | 3 days |
| META_DONE | You only | C6 and C7 | Review | 3 days |
| REVIEW_PASSED | You only | C8 | Schedule in Studio | 3 days |
| SCHEDULED | You | none | Wait for publish date | none |
| PUBLISHED | You | none | Record URL in column T | none |
| ANALYSED | You | none | Feed results to `dna/` | none |
| HOLD | You | none | Write the reason in column U | 14 days |
| KILLED | You | none | Move the folder to `archive/` | none |

Steps:

3. Add a conditional format so stale rows are visible. Select column C. Open **Format > Conditional formatting**. Under **Format rules** choose **Custom formula is** and enter `=AND($C2<>"",$C2<>"PUBLISHED",$C2<>"ANALYSED",$C2<>"KILLED",$C2<>"SCHEDULED",TODAY()-$V2>7)`. Set a red fill. Any red row is a video you are about to abandon or rush.
4. Apply a work-in-progress limit: no more than 3 videos may sit between SCRIPT_OK and REVIEW_PASSED at one time. If you reach 3, finish one before you approve another.
5. Only you change statuses that carry a gate. The scenarios in `02-no-code-workflow.md` write only SCRIPTED (Scenario 1) and leave THUMB_DONE unchanged (Scenario 2).

### Part 4. Batch operations

**Batch topic research.**
6. Collect ideas in the `Intake` form during the week. On batch day, run P-AUTO-02 from `02-no-code-workflow.md`, paste the rows into `batches/<week>/topics.tsv`, and discard any row whose first-hand angle you cannot actually produce this week.
7. Approve no more topics than you can finish in the next three weeks, using the time table in Part 5.

**Batch scripts.**
8. Set the approved rows to APPROVED and press **Run once** on Scenario 1, with the row limit at 3. Run it again for the next 3.
9. Edit each draft by hand. Use P-LONG-07 in `02-long-form/02-script-prompt-chain.md` for fact-checks. Run P-AUTO-09 below on the whole batch before you set any row to SCRIPT_OK.

**Batch Shorts.**
10. Use P-AUTO-07 to plan the week's Shorts. Each Short either comes from its own topic row, or comes from a long video you made yourself, re-scripted for a new hook and a new payoff under `03-shorts/05-repurposing-without-reuse.md`. Posting the same clip with a new caption is reused content and is not allowed by this repo.
11. Cap Shorts at the number in the time table. A week with many Shorts and no new long video should still keep the first-hand layer in every Short.

**Batch thumbnails.**
12. Use P-AUTO-08 to write briefs for the week's thumbnails into `batches/<week>/thumb-briefs.tsv`. Then follow `04-thumbnails/02-original-generation.md` and `04-thumbnails/03-design-workflow-and-templates.md` to produce three variants per video.
13. Keep this repo's rule: no thumbnail template (T1 to T5) used for more than 2 uploads in a row.

**Batch metadata.**
14. Set each finished row to THUMB_DONE, press **Run once** on Scenario 2, then check the MISMATCH CHECK line in each result before you accept a title.

### Part 5. Weekly batch routine for [WEEKLY_HOURS]

Planning estimates of human time per item, based on a first-draft pass with free tools. Replace them with your measured times from Step 4 of `01-pipeline-architecture.md`.

| Item | Estimate |
|---|---|
| Long video (research, script edit, voice, visuals, edit, thumbnail, metadata, review) | 5.75 hours |
| One Short inside a batch | 0.9 hours |
| Weekly planning plus analytics | 1 hour |

| [WEEKLY_HOURS] | Weekly output plan | Notes |
|---|---|---|
| 5 | 4 Shorts, or 1 long video every second week | Pick one mode. Do not split into half-finished videos |
| 10 | 1 long video + 3 Shorts | About 9.5 hours |
| 15 | 2 long videos + 2 Shorts | About 14.3 hours |
| 20 | 3 long videos + 1 Short, or 2 long videos + 7 Shorts | About 19 to 19.2 hours |

If [WEEKLY_HOURS] is above 20, add Shorts or rest time. Do not shorten the review gates to fit more output.

Routine, in this order, for a 10-hour week. Scale the blocks for other values.

| Block | Minutes | Work | Output |
|---|---|---|---|
| 1 Plan and analytics | 60 | Review last week's metrics. Run P-AUTO-06. Run P-AUTO-02. Approve topics (C1) | `batch-plan.md`, APPROVED rows |
| 2 Scripts | 120 | Scenario 1, edit drafts, P-LONG-07, P-AUTO-09 (C2) | SCRIPT_OK rows |
| 3 Voice | 45 | Record or render, listen to all (C3) | `voice.wav`, `captions.srt` |
| 4 Visuals | 120 | Gather or generate assets, log licences (C4) | `clips/`, asset log rows |
| 5 Edit | 120 | Assemble and trim | `final.mp4` |
| 6 Thumbnails and metadata | 75 | P-AUTO-08, three variants each, Scenario 2 (C5, C6, C7) | thumbnails, `metadata.md` |
| 7 Review and schedule | 60 | P-ORIG-01, final watch (C8), schedule in Studio | SCHEDULED rows |

Spread the blocks over the week. Do not run blocks 2 to 7 on the same day for the same videos, because a rested final watch catches more than a tired one.

## Prompts

### P-AUTO-06 — Weekly Batch Planner

Purpose: Turn [WEEKLY_HOURS] and the sheet state into this week's batch plan.
Inputs: [WEEKLY_HOURS], [CHANNEL_NAME], [PIPELINE_ROWS] (paste columns A to D and V from `Pipeline`), [ISO_WEEK] (for example 2026-W43).

```
You are a production scheduler for the YouTube channel [CHANNEL_NAME].
Week: [ISO_WEEK]. Hours available: [WEEKLY_HOURS].
Planning times: long video 5.75 hours, Short 0.9 hours, planning and analytics 1 hour.
Current rows (slug, format, status, topic, last updated): [PIPELINE_ROWS]

Output:
1. A table of what to work on this week: slug, current status, target status by Sunday, hours needed.
2. Total hours versus [WEEKLY_HOURS]. If over, remove work until it fits. Remove new videos first. Never remove a review gate.
3. A list of stale rows (see: IDEA 14 days, APPROVED 7, SCRIPTED 7, SCRIPT_OK 5, VOICED 5, VISUALS_DONE 5, EDITED 3, THUMB_DONE 3, META_DONE 3, REVIEW_PASSED 3) and for each one, a decision: continue, HOLD, or KILLED, with one reason.
4. The 7 blocks of the weekly routine with start-time suggestions spread across the week.

Rules: no more than 3 videos between SCRIPT_OK and REVIEW_PASSED. Never schedule publishing for a video that has not passed C8. No automatic publishing.
```

Expected output: A fitted weekly plan with stale-row decisions.
If the output is weak: Paste your real measured hours per stage and ask for a plan rebuilt on those numbers.

### P-AUTO-07 — Batch Shorts Planner

Purpose: Plan a week of Shorts that differ from each other and are not reused clips.
Inputs: [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [SHORTS_DNA] (the 350-word block from P-SHORT-01), [SHORT_COUNT], [LONG_VIDEO_SUMMARIES] (summaries of long videos you made yourself, or "none"), [LAST_FIVE_SHORT_HOOKS].

```
You plan Shorts for [CHANNEL_NAME], a [NICHE] channel for [AUDIENCE], in [LANGUAGE].
Shorts style rules: [SHORTS_DNA]
My own long videos (source material I own): [LONG_VIDEO_SUMMARIES]
Hooks used in my last five Shorts: [LAST_FIVE_SHORT_HOOKS]
Number of Shorts to plan: [SHORT_COUNT]

For each Short output one tab-separated row:
slug_suggestion | hook (first 3 seconds, written out) | hook_type | one-sentence payoff | first_hand_element | source (NEW TOPIC or the long video it expands, with a new angle)

Rules:
1. No two hooks in this batch may share a hook_type, and none may reuse a hook_type from my last five Shorts when [SHORT_COUNT] is 5 or fewer.
2. Each Short needs its own payoff. A Short that only trims a long video without a new hook and payoff is not allowed.
3. Every Short needs a first_hand_element I can film or show myself. If I could not produce it, replace the Short.
4. No other creator's footage, audio, or catchphrases. Match the rhythm and structure only.
5. No health, finance, or legal advice.
```

Expected output: [SHORT_COUNT] rows with different hook types.
If the output is weak: Add the weakest two hooks to the prompt and ask for replacements that use a different hook_type from the ones you name.

### P-AUTO-08 — Batch Thumbnail Briefs

Purpose: Write one thumbnail brief row per video with a rotating template and palette.
Inputs: [THUMB_DNA] (the 350-word block from P-THUMB-01), [BATCH_TITLES], [LAST_TEMPLATES], [LAST_PALETTES].

```
You write thumbnail briefs for an original channel. Style rules: [THUMB_DNA]
Videos this week (title and one-line promise): [BATCH_TITLES]
Templates used on my last uploads, most recent first: [LAST_TEMPLATES]
Palettes used on my last uploads: [LAST_PALETTES]

For each video output one tab-separated row:
slug | template (T1 to T5) | palette | focal subject | thumbnail text (max 4 words) | what the thumbnail promises | proof in the video that delivers it

Rules:
1. No template may repeat more than twice in a row, counting my last uploads.
2. The text must be 4 words or fewer and the promise must appear in the video.
3. Describe original compositions only. Never describe another creator's thumbnail, face, logo, character, or exact layout.
4. Do not include real people's faces or likenesses.
```

Expected output: One row per video.
If the output is weak: Paste the previous thumbnails' descriptions and ask for a palette that differs from all of them.

### P-AUTO-09 — Batch Variation Guard

Purpose: Catch the template-like sameness that triggers the inauthentic-content category.
Inputs: [CHANNEL_NAME], [BATCH_SCRIPTS] (all of this week's hooks and beat lists, not full text), [LAST_FIVE_SUMMARY] (hook, structure and thumbnail template of the last five published videos).

```
You audit a batch of YouTube scripts for the channel [CHANNEL_NAME] for sameness.
This week's scripts (hook and beat list for each): [BATCH_SCRIPTS]
Last five published videos (hook type, structure, thumbnail template): [LAST_FIVE_SUMMARY]

Report:
1. A table comparing each script's hook type, structure, opening line pattern, closing line pattern, and first-hand element.
2. Every pair of scripts, or script versus a recent video, that share the same hook type AND the same structure. Mark each pair RED.
3. Every script whose first-hand element is generic or missing. Mark each RED.
4. A verdict per script: PASS, REVISE (say what to change), or HOLD.

Rules: Be strict. Do not rewrite the scripts. If everything looks the same, say so plainly.
```

Expected output: A comparison table, RED flags, and a verdict per script.
If the output is weak: Add the full opening paragraph of each script and run it again.

## Done when

- [ ] The workspace folders and the naming scheme exist, and every slug in the sheet matches a folder.
- [ ] All 15 statuses are in the dropdown, stale-row formatting works, and the work-in-progress limit of 3 is written on the sheet.
- [ ] You ran one full weekly batch and recorded the real hours per stage.
- [ ] P-AUTO-09 returned no RED pair that you left unresolved.
- [ ] No thumbnail template repeats more than twice in a row.
- [ ] Every Short in the batch has its own hook, payoff, and first-hand element.

## Next

[04-human-checkpoints.md](04-human-checkpoints.md)
