# Originality Scoring Rubric

> **Purpose:** Score a finished script or video plan out of 100 and decide to publish, revise, or reject.  
> **Use when:** Before publishing any long video or Short, and when reviewing a batch.  
> **Time needed:** 10 minutes per video.  
> **Needs:** The script or a timestamped summary, a source log, the asset log, a free chat AI.  
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [VIDEO_TOPIC], [VIDEO_LENGTH], [FACE_OR_FACELESS], [VOICE_MODE]
- [SCRIPT_OR_SUMMARY]: the full script, or a timestamped summary with what is on screen and what is said
- [VALUE_STACK_PLAN]: the output of P-ORIG-02
- [LAST_FIVE_SUMMARY]: from 01-differentiation-method.md
- [ASSET_LOG]: music, footage, image, and voice sources with license notes (from 02-long-form/04-visual-production.md and 04-thumbnails/02-original-generation.md)
- [TITLE_AND_THUMBNAIL]: the exact title and the thumbnail text

## Steps

1. Gather the five inputs above. If the asset log is missing, score criterion 6 at 0 and fix that first.
2. Run P-ORIG-01 below. Paste the answer into `videos/<slug>/orig-score.md`.
3. Read the **hard gates** table. Any hard gate marked FAIL means REJECT, whatever the score is.
4. Read the total, then apply the thresholds table.
5. If the verdict is REVISE, do the fixes the AI lists, then rescore. Maximum two revision rounds; after that, either REJECT or change the video's angle.
6. Copy the score and verdict into the Publish-Log or your tracking sheet (09-operations/03-tracking-sheet.md).
7. Channel check, once per week: average the last 5 scores. If the average is under 75, stop adding new formats and spend the next upload rebuilding the Value Stack from scratch.

All numbers here are this repo's decision rules. They are not YouTube's numbers and they cannot predict what YouTube will decide. Their job is to force honest checking.

## The 100-point rubric

| # | Criterion | Max | Full marks mean | Zero means |
|---|---|---|---|---|
| 1 | Original angle | 12 | A defensible thesis or question that you can state in one sentence and that the competition does not already cover in the same way | The topic and framing are the standard ones for the niche |
| 2 | First-hand experience and evidence | 15 | At least two pieces of proof you produced (tests, receipts, own footage, measurements) that appear on screen | Nothing first-hand |
| 3 | Structural uniqueness | 10 | Structure and segment order differ from the last 5 uploads and from the source channel | Same structure as the previous upload |
| 4 | Voiced judgment | 12 | Commentary decides, ranks, warns, and explains reasoning at key moments in your words | Narration only restates facts |
| 5 | Viewer value | 10 | A viewer can do, decide, or understand something new after watching; the payoff matches the promise | A summary of public information |
| 6 | Asset and source independence | 10 | Every clip, image, sound, and music file is yours or licensed, logged, and every borrowed fact is paraphrased and cited | Unlicensed or unlogged assets, copied wording or footage |
| 7 | Production variation | 8 | At least 3 of 6 variables changed versus the last 5 uploads | All 6 identical |
| 8 | Honest packaging and accuracy | 8 | Title, thumbnail, and hook promise exactly what is delivered; every claim is checked | Packaging promises something the video does not show |
| 9 | Sensitive-topic and persona compliance | 8 | No AI persona giving health, finance, legal, or news guidance; no distressing content; see 03-sensitive-topics-and-personas.md | A rule is broken |
| 10 | Disclosure and policy hygiene | 7 | Altered or synthetic realistic content is disclosed; sponsorships are declared; music and stock licenses are recorded | Realistic synthetic media is undisclosed, or paid promotion is undeclared |

Maximum 100.

### Hard gates (any FAIL means REJECT)

| Gate | Fails when |
|---|---|
| G1 Reused content | The video contains another creator's footage, audio, voice, or music without a license, or merely re-presents it with minimal change |
| G2 Likeness | The video uses a cloned voice or synthetic likeness of a real person without permission |
| G3 Persona | An AI persona gives health, finance, legal, or news advice as if it were an expert |
| G4 Evidence | A claimed test, number, quote, or interview was invented |
| G5 Disclosure | Realistic altered or synthetic content is not disclosed in YouTube Studio |
| G6 Deception | Title, thumbnail, or metadata misleads viewers on the content |
| G7 Template | Criterion 3 and criterion 7 scored 0 each |

### Thresholds

| Total | Verdict | Action |
|---|---|---|
| 80 to 100 and no gate failed | PUBLISH | Upload after the pre-publish gate in 02-long-form/06-prepublish-gate.md or 03-shorts/06-prepublish-gate.md |
| 65 to 79 | REVISE | Fix the lowest three criteria, rescore, maximum two rounds |
| Under 65, or any gate failed | REJECT | Do not publish. Change the angle or build new proof, then restart at the Value Stack |

Additional floors (also repo rules): criterion 2 below 6 of 15 caps the verdict at REVISE; criterion 6 below 6 of 10 caps the verdict at REVISE.

## Prompts

### P-ORIG-01 — Originality scoring run

Purpose: Score one video against the 100-point rubric, check the hard gates, and list the fixes.

Inputs: [CHANNEL_NAME], [NICHE], [AUDIENCE], [VIDEO_TOPIC], [VIDEO_LENGTH], [FACE_OR_FACELESS], [VOICE_MODE], [SCRIPT_OR_SUMMARY], [VALUE_STACK_PLAN], [LAST_FIVE_SUMMARY], [ASSET_LOG], [TITLE_AND_THUMBNAIL].

```
You are a strict compliance and quality reviewer for a YouTube channel. Score only what the materials show. If something is not in the materials, treat it as missing, not as present. Never give credit for a claim I made but did not show.

Channel: [CHANNEL_NAME] | Niche: [NICHE] | Audience: [AUDIENCE]
Video topic: [VIDEO_TOPIC] | Length: [VIDEO_LENGTH] | On screen: [FACE_OR_FACELESS] | Voice: [VOICE_MODE]
Script or timestamped summary: [SCRIPT_OR_SUMMARY]
Planned Value Stack: [VALUE_STACK_PLAN]
Last five uploads: [LAST_FIVE_SUMMARY]
Asset log: [ASSET_LOG]
Title and thumbnail text: [TITLE_AND_THUMBNAIL]

Score with this 100-point rubric:
1 Original angle (max 12); 2 First-hand experience and evidence (15); 3 Structural uniqueness versus my last 5 uploads (10); 4 Voiced judgment (12); 5 Viewer value (10); 6 Asset and source independence (10); 7 Production variation, at least 3 of 6 variables changed: hook type, structure, length band, voice delivery, visual treatment, segment order (8); 8 Honest packaging and accuracy (8); 9 Sensitive-topic and persona compliance (8); 10 Disclosure and policy hygiene (7).

Hard gates, answer PASS or FAIL for each: G1 reused footage, audio, voice, or music without license; G2 cloned voice or likeness of a real person without permission; G3 AI persona giving health, finance, legal, or news advice; G4 invented test, number, quote, or interview; G5 realistic altered or synthetic content not disclosed; G6 misleading title, thumbnail, or metadata; G7 criteria 3 and 7 both scored 0.

Output:
A. SCORE TABLE: criterion, points, evidence quoted in 12 words or fewer from my materials, and the single fix that would raise it.
B. GATE TABLE with PASS or FAIL and a reason.
C. TOTAL out of 100.
D. VERDICT: PUBLISH if total is 80 or more and no gate failed; REVISE if 65 to 79; REJECT if under 65 or any gate failed. Apply the caps: criterion 2 under 6 or criterion 6 under 6 limits the verdict to REVISE.
E. FIX LIST: the lowest three criteria, each with a concrete change and the proof I must create, ordered by points gained per hour.
F. QUESTIONS: anything I must answer because the materials were missing it.
Be blunt. No praise. Do not invent facts about my video.
```

Expected output: A score table with evidence, a gate table, a total, one verdict, a ranked fix list, and any missing-information questions.

If the output is weak: (1) If scores are all high with no evidence, say "quote evidence for every score in 12 words or fewer or score 0". (2) If it skips gates, say "answer G1 to G7 individually". (3) If it is too generous, say "score as a reviewer who wants to demonetize this channel; assume anything unproven is absent".

## Example: scored video

Neutral niche: home cooking on a budget. Video: "I Ate on $1.50 a Meal for a Week" (10 minutes, face on camera, own voice).

Materials in short: receipts for 21 meals, daily time logs, two failed dishes shown, one side-by-side of dried versus canned beans, own hands footage, own music from a licensed free library logged in the asset log. Structure: same countdown format as the previous two uploads. Hook: question hook as in the previous upload. Same length band as the last three. Title says "Ate on $1.50 a Meal"; the real average was $1.62.

| # | Criterion | Score | Reason |
|---|---|---|---|
| 1 | Original angle | 9 / 12 | Fixed-price week is common; the receipts framing is the differentiator |
| 2 | First-hand evidence | 11 / 15 | Receipts and logs are strong; taste notes are only the creator's |
| 3 | Structural uniqueness | 5 / 10 | Third countdown format in a row |
| 4 | Voiced judgment | 8 / 12 | Good ranking of meals, weak explanation of why prices differ |
| 5 | Viewer value | 7 / 10 | Viewer cannot reproduce the plan without a shopping list |
| 6 | Asset independence | 9 / 10 | All assets logged; one stock clip missing its license URL |
| 7 | Production variation | 4 / 8 | Hook, structure, and length band repeat the last upload |
| 8 | Honest packaging | 6 / 8 | Title rounds $1.62 down to $1.50 |
| 9 | Sensitive-topic compliance | 8 / 8 | No health claims, no AI persona |
| 10 | Disclosure | 5 / 7 | Sponsor mention of a store lacks a paid-promotion declaration (the creator got a free gift card) |
| | Total | 72 / 100 | |

Gates: G1 to G7 all PASS. Verdict: REVISE (65 to 79).

Fixes from the list, ordered by points per hour: (a) change the title to the true average ($1.62) and rework the thumbnail text, +2; (b) declare the gift card as paid promotion in Studio and on screen, +2; (c) switch to a "mistake-by-mistake" structure and a cold-open hook, +3 on criterion 3 and +3 on criterion 7; (d) add a one-page shopping list link and a 20-second explanation of why the beans priced differently, +2 on criterion 4 and +1 on criterion 5; (e) add the stock clip license URL, +1. Rescored after fixes: 84. Verdict: PUBLISH.

## Done when

- Each video has `orig-score.md` with a table, gate results, total, and verdict.
- No video is published below 80 or with a failed gate.
- The 5-upload average is 75 or higher.
- Every REVISE or REJECT verdict has a dated fix list you completed or a recorded decision to drop the video.

## Next

Continue to [03-sensitive-topics-and-personas.md](03-sensitive-topics-and-personas.md).
