# Differentiation Method

> Purpose: Give every upload real added value so no two videos look templated, which is what YouTube's inauthentic-content rules target.
> Use when: Before scripting any video or Short, and again when you review the last five uploads.
> Time needed: 20 minutes per video; 30 minutes for the five-upload audit.
> Needs: Your last 5 uploads (or planned ones), a Google Sheet, a free chat AI.
> Cost: $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [VIDEO_TOPIC], [VIDEO_LENGTH], [WEEKLY_HOURS], [STYLE_BIBLE]
- [LAST_FIVE_SUMMARY]: one line per recent upload giving title, hook type, structure, length, voice, visual style, and the original value it carried. Defined in Step 1.
- [AVAILABLE_PROOF]: what you can actually do or show this week (things you can cook, test, build, visit, measure, interview, draw, or record). Defined in P-ORIG-02.

## Why this matters (verified 2026-10-20)

YouTube's inauthentic-content wording was clarified in mid-July 2026 (reports date the announcement between 14 and 16 July). Three categories are not monetizable: generic, repetitive, or template-based content with little variation between videos; off-putting or distressing content; and AI personas discussing sensitive topics such as health and finance. YouTube says the target is mass production, not AI itself, and that AI voiceover can qualify when the video has original commentary, education, or entertainment value. The reused-content policy did not change. One secondary source says enforcement works at channel level across recent uploads, not per video; VERIFY BEFORE RELYING at YouTube Help, search "Inauthentic content". Plan for that: the pattern across your uploads is judged, so variation must exist across videos, not only inside one.

Copying a channel's style is allowed and is the goal of this repo. Copying a channel's format so closely that your uploads are interchangeable with each other and with theirs is what fails. This method keeps the style family and changes the substance.

## The method: Value Stack and Variation Budget

Both are this repo's rules, not YouTube numbers.

**Value Stack.** Each video must carry at least 3 of these 5 layers, and at least 1 of the 3 must be first-hand (layers B or C):

- A. Original angle: a thesis, question, or constraint that is yours.
- B. Personal experience: something you did, tried, failed at, or learned.
- C. Real evidence: a test, measurement, comparison, receipt, photo, recording, or dataset you made.
- D. Voiced judgment: commentary that decides, ranks, warns, or explains why, in your own words.
- E. Structure or format: a shape of the video that differs from your previous uploads.

**Variation Budget.** Compare each new video with your last 5. Change at least 3 of these 6 variables: hook type, structure, length band, voice delivery (pace, tone), visual treatment, and segment order. No single variable stays identical for more than 3 uploads in a row.

## Steps

1. **Audit the last five uploads.** In a sheet named `variation-log` create columns `slug, date, hook code, structure code, length (min), voice, visual treatment, value layers (A to E), first-hand proof, template risk (H/M/L)`. Fill 5 rows. Use the hook (H1 to H10) and structure (S1 to S10) codes from 03-shorts/01-shorts-dna-analysis.md for Shorts, and the channel's own labels for long videos. Paste the rows as [LAST_FIVE_SUMMARY].
2. **Mark template risk.** A row is High if 3 or more variables match the previous upload, Medium if 2 match, Low otherwise. Two High rows in a row means the next upload must change 4 variables.
3. **List [AVAILABLE_PROOF].** Write 5 real things you can produce in the next 7 days. If the list is empty, you have nothing first-hand to add; spend a day creating one thing before scripting.
4. **Run P-ORIG-02** to build the Value Stack for the next video. Save the result in `videos/<slug>/value-stack.md`.
5. **Build the proof first.** Do the test, take the photos, record the screen, gather the receipts before writing. A script written first invites invented evidence.
6. **Script with the stack in view.** Paste the stack into the script prompt (02-long-form/02-script-prompt-chain.md, P-LONG-04) so the video shows each layer on screen or in the voiceover.
7. **Score before publishing** with 02-scoring-rubric.md. Target 80 or higher.
8. **Update `variation-log`** after publishing so the next audit is accurate.

## The 15 tactics

Each tactic removes a template signal. Examples use the neutral niche "home cooking on a budget". Choose at least one first-hand tactic per video.

1. **Constraint challenge (A, E).** Add a rule that forces different choices each time: one pot, no oven, only pantry items. The rule changes the recipes, the shots, and the script. Cost $0.
2. **Real receipts (C).** Show your shopping receipt and compute the cost per serving on screen. Do it at a real store with your real prices. It cannot be copied from another video because the numbers are yours.
3. **Failed attempt segment (B).** Film or describe one thing that went wrong and what you changed. A failure is hard to fake and shows real work.
4. **Side-by-side test (C).** Make two versions (cheap versus store-brand, 10 minutes versus 40 minutes) and record the measurable difference: time, weight, taste notes from three named tasters in your own words.
5. **Personal history hook (B, D).** Start from a real situation you or your viewer faced, such as the week before payday. The hook comes from lived facts, not a formula.
6. **Viewer question answered with a test (A, C).** Take a real comment from your channel, test the answer, and show the result. Keep the commenter anonymous unless they agree.
7. **Own measurements and data (C).** Weigh portions, time every step, log the cost across four weeks, and show a simple chart you made in Google Sheets. Never use another channel's numbers.
8. **Opinionated ranking (D).** Rank five options and defend the order with reasons. A ranking carries a decision, which a summary does not.
9. **Myth check with evidence (A, C).** Pick one claim common in your niche, run a small test, and report what you saw, including when the myth holds. Do not turn this into health claims; see 03-sensitive-topics-and-personas.md.
10. **Voiced commentary over every key moment (D).** Whether on camera or by [VOICE_MODE] voiceover, explain your reasoning at each decision: why this pan, why this swap. A voiceover reading a script of facts with stock visuals is high risk (verified 2026-10-20 snapshot). A voiceover that reasons over footage you shot is not.
11. **Rotating structure (E).** Alternate structures across uploads: countdown, one long build, A versus B, mistake-by-mistake, Q and A from comments. Use a different one from the last upload.
12. **Original visuals you made (C, E).** Draw your own diagrams, film your own hands, record your own screen, shoot your own photos. For AI images, log them as in 04-thumbnails/02-original-generation.md. Footage taken from others is never allowed.
13. **Varied length and pacing (E).** Mix a tight 6-minute video with an 11-minute walk-through. Change the hook length and the cut rhythm. Identical length and rhythm across uploads is a template signal.
14. **Expert or user input you really obtain (B, C).** Ask a real cook, a market seller, or a family member a specific question, record permission in writing, and use their words as they gave them. Do not invent quotes, and do not use an AI to pose as a person.
15. **Follow-up and update (A, B).** Return to an old video with a new result: "I repeated it six weeks later; prices changed by X". This ties your catalog together and shows continued first-hand work.

## Prompts

### P-ORIG-02 — Value Stack planner

Purpose: Build a Value Stack and Variation Budget for the next video from what you can really do this week.

Inputs: [CHANNEL_NAME], [NICHE], [AUDIENCE], [VIDEO_TOPIC], [VIDEO_LENGTH], [FACE_OR_FACELESS], [VOICE_MODE], [WEEKLY_HOURS], [STYLE_BIBLE], [LAST_FIVE_SUMMARY], [AVAILABLE_PROOF].

```
You are an editorial planner for a YouTube channel. Use only facts I give you. Do not invent experiences, tests, interviews, or data. If something is missing, say what I must create first.

Channel: [CHANNEL_NAME] | Niche: [NICHE] | Audience: [AUDIENCE]
Next video topic: [VIDEO_TOPIC] | Length: [VIDEO_LENGTH] | On screen: [FACE_OR_FACELESS] | Voice: [VOICE_MODE]
Time I have per week: [WEEKLY_HOURS] hours
Style rules to keep: [STYLE_BIBLE]
My last five uploads: [LAST_FIVE_SUMMARY]
Things I can really do, test, show, or record this week: [AVAILABLE_PROOF]

Rules:
- The Value Stack must contain at least 3 of these 5 layers, and at least one of B or C: A original angle, B personal experience, C real evidence I produce, D voiced judgment, E structure or format that differs from my last uploads.
- The Variation Budget: change at least 3 of 6 variables versus my last five: hook type, structure, length band, voice delivery, visual treatment, segment order. No variable stays identical for more than 3 uploads in a row.
- Choose from these 15 tactics only: constraint challenge, real receipts, failed attempt, side-by-side test, personal history hook, viewer question answered with a test, own measurements and data, opinionated ranking, myth check, voiced commentary on decisions, rotating structure, original visuals, varied length and pacing, real expert or user input, follow-up and update.

Output, with these headings:
1. TEMPLATE RISK ON MY LAST FIVE (table: upload, matching variables, risk H/M/L)
2. VALUE STACK FOR THIS VIDEO (table: layer A to E, what it is, which tactic, the proof I must create, where it appears in the video)
3. VARIATION BUDGET (table: variable, what my last uploads did, what this video does)
4. PROOF TO CREATE FIRST (checklist with time estimates that fit my weekly hours)
5. ANGLE IN ONE SENTENCE (a thesis I can defend)
6. WHAT NOT TO DO (3 template signals to avoid in this video)
If the video cannot reach the Stack minimum with my proof list, say "NOT READY" and list exactly what I need to create.
```

Expected output: Six labeled sections, a Stack with at least 3 layers including a first-hand one, and either a ready plan or NOT READY with a to-do list.

If the output is weak: (1) If it invents experiences, say "remove everything not in my proof list and mark gaps as NOT READY". (2) If layers are vague, say "for each layer give the exact scene, the exact line type, and the timestamp range". (3) If the variation table repeats my last uploads, say "change structure and hook type first, then length".

## Done when

- `variation-log` has your last 5 uploads with template-risk ratings.
- The next video has a Value Stack with 3 or more layers, one of them first-hand, and proof already created.
- At least 3 of 6 variables differ from the last 5 uploads.
- No variable is identical for more than 3 uploads in a row.
- Score of 80 or higher in the rubric (next file).

## Next

Continue to [02-scoring-rubric.md](02-scoring-rubric.md).
