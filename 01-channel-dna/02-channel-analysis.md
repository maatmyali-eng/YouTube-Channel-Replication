# Channel Analysis: Master Report, Comparison, Gaps, and Safety Screen

> Purpose: Turn the collected data into a structured, honest report on one channel's style and strategy.
> Use when: After 01-data-gathering.md is complete, and before filling the Style Bible.
> Time needed: 60 to 90 minutes per channel.
> Needs: Your Google Sheet, saved transcripts, Watch Notes, any free AI chat tool.
> Cost: $0

## Inputs

- [CHANNEL_URL], [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [COUNTRY], [HARDWARE], [WEEKLY_HOURS], [FACE_OR_FACELESS], [TRANSCRIPT] from 00-start-here/01-setup-card.md and 01-data-gathering.md.
- Outputs of P-CDNA-03 and P-CDNA-04.

## Steps

### Step 1. Read the bias warning

A text-only model cannot watch video. It never sees the pacing, the cuts, the color, the thumbnail, the music, the voice, or the face. Any claim about those from a transcript alone is a guess dressed as analysis. Three further biases apply: you picked the top videos, so you see survivors; views are confounded by promotion and timing; and the model fills gaps with the typical YouTuber from its training data. Compensate this way:

1. Give the model your Watch Notes (cut counts, music, colors, fonts, face) as [WATCH_NOTES]. These are your direct observations and are the only reliable source for visuals and audio.
2. Require the three evidence labels in the prompt: OBSERVED (stated in the data you pasted), INFERRED (reasoned from the data), UNKNOWN (needs a human check). The model must never present an INFERRED item as OBSERVED.
3. Run P-CDNA-08 on the finished report to strip unsupported claims.
4. Check every UNKNOWN by watching two videos yourself with the checklist in the Watch Notes tab.
5. Optional: if Google's own AI products accept a YouTube link and summarize the video, that gives some visual coverage. Terms and free limits change, so VERIFY BEFORE RELYING at https://ai.google.dev/gemini-api/docs/video-understanding, and still treat the result as unverified until you check it.

### Step 2. Prepare the inputs

1. [TRANSCRIPT]: paste only the parts that reveal structure: the first 90 seconds, the last 60 seconds, and two mid-video samples of about 200 words each. Do this for the 6 best and 3 worst videos. Free chat tools limit input length, so if the paste is refused, split the work: run the prompt once with the best videos, once with the worst, then ask the model to merge the two reports.
2. [SHEET_SUMMARY]: copy the `Picks` tab, the `Cadence` tab, and the pillar and title_formula columns for all rows.
3. [WATCH_NOTES]: copy the `Watch Notes` tab.
4. [COMMENT_THEMES]: paste the output of P-CDNA-04.

### Step 3. Screen the channel before investing

Run P-CDNA-07 on every channel you are considering. Do not model a channel rated AVOID. A CAUTION channel needs the listed modifications written into your plan.

### Step 4. Run the master analysis

1. Open a new chat in your tool of choice. Paste P-CDNA-01 with the inputs filled.
2. Save the report as `reports/[CHANNEL_NAME]-analysis.md`.
3. Run P-CDNA-08 in the same chat.
4. Fix the UNKNOWN items by hand and edit the saved report.

### Step 5. Optional multi-channel work

1. To pick a model from three candidates, run P-CDNA-01 for each, then run P-CDNA-05 with the three reports.
2. To find opportunities, run P-CDNA-06 on the final report or on the P-CDNA-05 output.

## Prompts

### P-CDNA-01 — Channel Analysis Master

Purpose: Produce a structured, evidence-labeled report on one channel.
Inputs: [CHANNEL_URL] (a label only), [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [TRANSCRIPT], [SHEET_SUMMARY], [WATCH_NOTES], [COMMENT_THEMES].

```
You are a senior YouTube strategist and script analyst. I am studying the channel [CHANNEL_NAME] ([CHANNEL_URL], used only as a label; do not try to open it). Niche: [NICHE]. Intended audience for my own channel: [AUDIENCE]. Language: [LANGUAGE].

You cannot watch video. You see only the text I paste. Label every finding as one of:
OBSERVED = stated in the data below.
INFERRED = your reasoning from the data; say what it is based on.
UNKNOWN = cannot be determined from text; say what a human must check.
Never present INFERRED as OBSERVED. Never invent numbers, dates, or quotes. When citing a transcript, use a maximum of 8 words in quotation marks; otherwise describe it.

DATA
Transcript samples: [TRANSCRIPT]
Video table summary: [SHEET_SUMMARY]
My direct viewing notes: [WATCH_NOTES]
Comment themes: [COMMENT_THEMES]

Write the report with these exact sections:
1. Evidence inventory: how many videos, transcripts, and comments you saw, and the confidence level (low, medium, high) for each later section.
2. Positioning: the promise in one sentence, the viewer's problem it solves, the channel's angle versus others in [NICHE].
3. Audience: who watches, what they already know, what they want, with the evidence for each.
4. Content pillars: a table with pillar, share of uploads, average outlier ratio, example titles.
5. Cadence and formats: upload frequency, long versus Shorts mix, length bands, series.
6. Title patterns: 5 to 8 title formulas written as fill-in slots, with how many titles match each and which have the highest outlier ratio.
7. Thumbnail patterns: only what my notes support. Mark all else UNKNOWN.
8. Hook mechanics: for each sampled video, classify the first 30 seconds (question, bold claim, story, result-first, problem, pattern interrupt, other) and note the promise, the stakes, and the first open loop.
9. Retention structure: a beat map as percentages of runtime (hook, setup, body segments, re-hooks, payoff, outro and CTA) with the average, and the typical position of open loops and re-hooks.
10. Voice and diction: sentence length, person (I, we, you), vocabulary level, humor, catchphrases described as patterns, not quoted.
11. Topic-selection logic: how topics seem to be chosen (search demand, trends, audience requests, series continuation) with evidence.
12. Outlier analysis: what the best videos share and the worst videos lack, with confounders listed.
13. Monetization model: which revenue routes are visible (ads, sponsorships, affiliate, products, memberships). Do not estimate income.
14. Weaknesses and gaps: at least 8 specific, fixable weaknesses (pacing, repetition, thin sourcing, unclear promises, audience requests unanswered).
15. Imitation risk flags: elements that would be unsafe to copy (reused footage, templated formats, sensitive topics, personas, signature phrases, characters, music) and what to do instead.
16. Ten style facts that must go into a Style Bible, each tagged OBSERVED or INFERRED.
17. UNKNOWN list: every item a human must check by watching.
Be specific. No filler. Do not give advice outside these sections.
```

Expected output: A 17-section report with evidence labels and a unknown list.
If the output is weak: Reduce the transcript samples to 3 videos, rerun, then merge; add "if a section lacks evidence, write UNKNOWN and stop that section" to the end.

### P-CDNA-05 — Compare Three Channels

Purpose: Find which traits are shared genre conventions and which are one channel's signature, then design a blend.
Inputs: [REPORT_A], [REPORT_B], [REPORT_C] (outputs of P-CDNA-01), [NICHE], [FACE_OR_FACELESS], [HARDWARE].

```
You are a YouTube strategist. Below are three analysis reports of channels in the niche [NICHE]. Each uses evidence labels OBSERVED, INFERRED, UNKNOWN. Keep those labels.

Report A: [REPORT_A]
Report B: [REPORT_B]
Report C: [REPORT_C]

Produce:
1. A comparison table with rows: positioning, audience, pillars, cadence, average length, title formulas, hook types, retention beat map, voice, visual style, audio design, monetization routes, main weakness. One column per channel.
2. Shared traits: elements all three use. Treat them as genre conventions that are safe to adopt.
3. Signature traits: elements only one channel uses. Mark each "do not clone". Describe the underlying principle I can apply in my own way.
4. Where the channels disagree and which side the evidence favors (using outlier data only).
5. A blended style recommendation for my channel with [FACE_OR_FACELESS] and the equipment limits [HARDWARE]: which traits to take from which channel and what must be original.
6. Three positioning statements for the blend, each in one sentence.
Do not invent data. If the reports do not support a claim, say so.
```

Expected output: Comparison table, shared and signature trait lists, blend recommendation, three positioning statements.
If the output is weak: Shorten each report to its sections 4, 6, 8, 9, 10, and 14 and rerun.

### P-CDNA-06 — Find Open Gaps

Purpose: Identify what the channel leaves undone so your channel adds value instead of copying.
Inputs: [REPORT_A] (the P-CDNA-01 report or the P-CDNA-05 output), [COMMENT_THEMES], [NICHE], [AUDIENCE], [HARDWARE], [WEEKLY_HOURS], [FACE_OR_FACELESS].

```
You are a content strategist. Using the report and comment themes below, find gaps I can fill in the niche [NICHE] for the audience [AUDIENCE].

Report: [REPORT_A]
Comment themes: [COMMENT_THEMES]
My limits: hardware [HARDWARE], [WEEKLY_HOURS] hours per week, [FACE_OR_FACELESS].

Produce:
1. Gap list in five groups: unanswered audience questions, topics covered shallowly, formats missing (for example comparisons, tests, case studies, beginner series), underserved viewer segments, and production-quality weaknesses. Every gap must cite its evidence (a report section or comment theme).
2. For each gap, a feasibility score from 1 to 5 for my limits, with one sentence of reasoning.
3. Ten video angle candidates built from the top gaps. Each has a working title, the viewer problem, the original value I add (my own testing, data, demonstration, or explanation), and the demonetization risk (low, medium, high) with a reason.
4. A validation step for each angle that I can do for free by hand (type the topic into YouTube search and read the autocomplete, check how many recent videos exist, read comments on competitors).
Do not claim search volume, demand, or income. Say clearly that every angle is a hypothesis until I validate it.
```

Expected output: Grouped gap list with evidence, scores, ten angles, and validation steps.
If the output is weak: Add a list of five competitor video titles you saw to the prompt and tell it to avoid angles those titles already cover.

### P-CDNA-07 — Channel Safety Screen

Purpose: Decide whether a channel is safe to model before you invest in it.
Inputs: [CHANNEL_NAME], [NICHE], [CHANNEL_FACTS] (your notes: upload frequency, formats, how the videos appear to be made, topics, whether the videos look templated, whether they use clips or footage from others, whether an AI voice or AI presenter is used, whether the audience is children), [HARDWARE], [WEEKLY_HOURS].

```
You are a YouTube policy-aware strategist. Evaluate whether the channel [CHANNEL_NAME] in the niche [NICHE] is a safe style to model. Facts I observed: [CHANNEL_FACTS]. My resources: [HARDWARE], [WEEKLY_HOURS] hours per week.

Context to apply (YouTube's inauthentic-content clarification of July 2026, verified 2026-10-20): three categories are non-monetizable: (1) generic, repetitive, or template-based content with little variation between videos; (2) off-putting or distressing content; (3) AI personas discussing sensitive topics such as health and finance. The target is mass production, not AI itself. AI voiceover can qualify when the video has original commentary, education, or entertainment value. The reused-content policy is separate and unchanged. Faceless slideshow, stock-footage-plus-text-to-speech, and templated Shorts formats are high risk.

Score each item from 0 (no concern) to 3 (serious concern) and give one sentence of reasoning, writing UNKNOWN when my facts do not say:
1. Saturation: many near-identical channels, same topics, same format.
2. Template risk: videos that differ only by topic and voiceover.
3. Reused content reliance: compilations, reactions, clips, news recaps, or lifted footage.
4. Sensitive topics: health, finance, legal, news, politics, tragedies, children.
5. AI persona risk: synthetic presenters or voices discussing sensitive subjects.
6. Licensing dependence: needs copyrighted music, footage, brands, or characters.
7. Reproducibility at $0 with my hardware and hours.
8. Dependence on one monetization route that is hard for a new channel.
9. Content directed at children (made-for-kids designation limits features and monetization; VERIFY BEFORE RELYING at https://support.google.com/youtube).

Output: a table of the 9 scores, a total, a verdict of SAFE (total 0 to 6), CAUTION (7 to 13), or AVOID (14 or more), and for CAUTION the exact modifications my version needs (more original commentary, different format, added demonstrations, different topic scope). State that the verdict is a screening aid, not a policy decision by YouTube.
```

Expected output: Score table, total, verdict, and a modification list for CAUTION.
If the output is weak: Add more facts to [CHANNEL_FACTS], especially how the videos look and how many upload per week.

### P-CDNA-08 — Report Evidence Audit

Purpose: Strip guesses and unsupported claims from a finished report.
Inputs: [REPORT_A] (the P-CDNA-01 output), [WATCH_NOTES], [SHEET_SUMMARY].

```
You are a skeptical editor. Audit the report below against the data I have. Do not add new analysis.

Report: [REPORT_A]
My watch notes: [WATCH_NOTES]
My sheet summary: [SHEET_SUMMARY]

Tasks:
1. List every claim about visuals, color, typography, editing speed, music, sound effects, voice, or thumbnails. Mark each SUPPORTED (my watch notes or sheet contain it) or UNSUPPORTED (a guess).
2. List every number in the report and mark whether it appears in my data.
3. List every claim labeled OBSERVED that is actually INFERRED, and relabel it.
4. List overgeneralizations (a pattern claimed from fewer than 3 examples).
5. Rewrite the report's section 16 (ten style facts) keeping only SUPPORTED items, and list the replacements I must verify by watching.
Be strict.
```

Expected output: A claim audit, a corrected label list, and a cleaned style-facts section.
If the output is weak: Paste section 7 and section 16 only and rerun the audit on those.

## Done when

- A report exists at `reports/[CHANNEL_NAME]-analysis.md` with all 17 sections.
- P-CDNA-07 returned SAFE, or CAUTION with modifications written into your plan.
- P-CDNA-08 has been run and every UNSUPPORTED claim is removed or marked to verify.
- Every UNKNOWN item has either been checked by watching or is listed as unverified.
- If you compared channels, you have a blended style recommendation and three positioning statements.

## Next

Continue to [03-style-bible-template.md](03-style-bible-template.md).
