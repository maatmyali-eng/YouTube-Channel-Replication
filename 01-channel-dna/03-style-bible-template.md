# Style Bible: Prompt and Blank Template

> **Purpose:** Convert the audited channel report into one reusable Channel Style Bible that every later prompt reads as [STYLE_BIBLE].  
> **Use when:** After 02-channel-analysis.md, when P-CDNA-01 and P-CDNA-08 are done.  
> **Time needed:** 45 to 60 minutes.  
> **Needs:** The audited report, your Watch Notes, any free AI chat tool, a text editor.  
> **Cost:** $0  

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [HARDWARE] from 00-start-here/01-setup-card.md.
- The audited report from P-CDNA-01 and P-CDNA-08 (called [REPORT_A] in the prompt).
- [WATCH_NOTES] from the Watch Notes tab.
- The blank template below (called [BIBLE_TEMPLATE] in the prompt).
- Placeholder convention inside the template: `[FILL: ...]` marks a field you or the model must fill. Delete none of the section headings.

## Steps

1. Create a file named `style-bible.md` in your repo root. Paste the blank template from "Blank Channel Style Bible" below into it.
2. Open a new chat in your AI tool. Run P-CDNA-02 with [REPORT_A], [WATCH_NOTES], and [BIBLE_TEMPLATE] pasted in. If the paste is refused, run the prompt once for sections 1 to 10 and again for sections 11 to 21, then join the results.
3. Read the output against your own Watch Notes. For each field marked INFERRED, decide: confirm by watching, rewrite as your own rule, or delete.
4. Fill section 20 ("What we will do differently") yourself, with the model's suggestions as input only. This section is what separates your channel from the model channel. Write at least 6 concrete differences.
5. Fill section 19 (taboo list) from the imitation risk flags in report section 15, plus the rules in 00-start-here/02-principles-and-copy-line.md.
6. Check that every rule is testable: another person must be able to tell whether a script obeys it. "Fast pacing" fails. "A new visual or a new claim at least every 8 seconds" passes.
7. Save the full bible. Then save the 600-word compact version the prompt produces as `style-bible-compact.md`. Use the compact version where a free tool limits input length.
8. Copy the full text of `style-bible.md` into every later prompt wherever it says [STYLE_BIBLE]. If the tool limits input, paste the compact version and state "compact version" at the top.
9. Version it. Add a line at the top such as `v1, 2026-10-20`. After your first three published videos, compare your results to the bible and raise it to v2, changing only rules that your own data disproves.

## Prompts

### P-CDNA-02 — Fill the Style Bible

Purpose: Fill the template from the audited report without inventing visual or audio facts.
Inputs: [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [HARDWARE], [REPORT_A], [WATCH_NOTES], [BIBLE_TEMPLATE].

```
You are a script editor and brand-style analyst. Fill the Channel Style Bible template below for a NEW channel that will work in the same family of style as [CHANNEL_NAME] in the niche [NICHE], for the audience [AUDIENCE], language [LANGUAGE], presentation [FACE_OR_FACELESS], voice mode [VOICE_MODE], equipment [HARDWARE].

Rules:
1. Source of truth: the audited report and my watch notes. You cannot watch video. For every field write "Source pattern" (what the model channel does) and "Our rule" (what our channel will do).
2. Tag every Source pattern OBSERVED (in the report or notes), INFERRED (your reasoning, state why), or UNKNOWN. Write UNKNOWN instead of guessing, especially for visuals, color, typography, editing speed, and audio.
3. Our rules must be testable. Use numbers only when the report or notes contain them or when you mark the number "PROPOSED, to test".
4. Describe patterns, never reproduce wording. Do not copy catchphrases, jokes, slogans, character names, or channel branding. Replace each with the underlying pattern and a new original equivalent.
5. Section 20 must contain at least 6 differences from the model channel that add original value (own testing, data, demonstration, or structure).
6. Section 19 must include at least these taboos: reusing another creator's footage, audio, thumbnails, or script wording; mimicking a real person's voice or likeness; deceptive titles or thumbnails; templated videos that differ only by topic.
7. Keep every section brief. Total length of the full bible: 1,800 words or less.
8. After the bible, output a "Compact Bible" of 600 words or less that keeps every Our rule in the shortest testable form.
9. After that, list every UNKNOWN field and say how I check it by watching.

REPORT:
[REPORT_A]

WATCH NOTES:
[WATCH_NOTES]

TEMPLATE:
[BIBLE_TEMPLATE]
```

Expected output: The filled bible, a compact version, and a list of fields to verify.
If the output is weak: Fill the template in two halves, paste "Rules 1 to 9" again with each half, and add "Delete any rule you cannot trace to the report or notes."

## Blank Channel Style Bible

Copy everything inside the fence into `style-bible.md`.

```markdown
# Channel Style Bible: [FILL: your channel name]
Version: [FILL: v1, date]
Model channel studied: [FILL: [CHANNEL_NAME]] (analysis only; we never reuse its content)
Niche: [FILL: [NICHE]]   Audience: [FILL: [AUDIENCE]]   Language: [FILL: [LANGUAGE]]
Presentation: [FILL: [FACE_OR_FACELESS]]   Voice: [FILL: [VOICE_MODE]]
Evidence confidence: [FILL: low / medium / high, and why]

Field format for each section below:
Source pattern: [FILL: what the model channel does] (OBSERVED / INFERRED / UNKNOWN)
Our rule: [FILL: testable rule for our channel]

## 1. Positioning and promise
Source pattern: [FILL]
Our rule: [FILL: one-sentence promise, who it is for, what viewers get every video]

## 2. Audience
Source pattern: [FILL: knowledge level, needs, vocabulary]
Our rule: [FILL: viewer we write for, what we assume they know, what we explain]

## 3. Voice and diction
Source pattern: [FILL]
Our rule: [FILL: person (I/we/you), reading level, allowed and banned word types, contractions yes/no]

## 4. Sentence rhythm
Source pattern: [FILL]
Our rule: [FILL: typical sentence length range, when to use short punches, when to use long sentences]

## 5. Pacing
Source pattern: [FILL]
Our rule: [FILL: words per minute target, seconds per idea, pause usage]

## 6. Hook types
Source pattern: [FILL: hook categories used and their share]
Our rule: [FILL: primary hook type, backup types, what the first 5 seconds must contain, what the first 30 seconds must promise]

## 7. Structure beats
Source pattern: [FILL: beat map as % of runtime]
Our rule: [FILL: beats in order with % of runtime: hook, setup, segments, re-hooks, payoff, outro]

## 8. Open-loop habits
Source pattern: [FILL]
Our rule: [FILL: how many loops per video, where they open, where they close, forbidden unpaid loops]

## 9. Humor and tone rules
Source pattern: [FILL]
Our rule: [FILL: humor style, frequency, off-limits jokes, tone when something goes wrong]

## 10. Visual style
Source pattern: [FILL]
Our rule: [FILL: shot types, proportion of main footage versus inserts, framing, on-screen graphics rules]

## 11. Color and typography
Source pattern: [FILL]
Our rule: [FILL: palette as hex codes, fonts with free license, text size and placement rules]

## 12. Editing rhythm
Source pattern: [FILL]
Our rule: [FILL: maximum seconds between visual changes, transitions allowed, captions style]

## 13. Audio and music design
Source pattern: [FILL]
Our rule: [FILL: voice processing, music source and license, music level versus voice, sound effects rules, intro/outro sound]

## 14. CTA style
Source pattern: [FILL]
Our rule: [FILL: where CTAs appear, wording pattern, maximum count per video, forbidden manipulative CTAs]

## 15. Series structure
Source pattern: [FILL]
Our rule: [FILL: recurring series, naming pattern, episode template, cadence]

## 16. Title formulas
Source pattern: [FILL: formulas as fill-in slots]
Our rule: [FILL: 4 to 6 formulas with slots, length limit, promise rule, no deceptive claims]

## 17. Thumbnail formulas
Source pattern: [FILL]
Our rule: [FILL: composition, number of elements, text word limit, face or object rule, palette, what must match the video]

## 18. Description, chapters, and metadata habits
Source pattern: [FILL]
Our rule: [FILL: chapter naming, first two description lines, tags policy]

## 19. Taboo list
- Reusing another creator's footage, audio, thumbnails, or script wording
- Mimicking a real person's voice or likeness
- Deceptive titles, thumbnails, or metadata
- Videos that differ only by topic and voiceover
- [FILL: add model-channel signature elements we must not copy]
- [FILL: add topics we will not cover]
- [FILL: add words or claims we will not use]

## 20. What we will do differently
1. [FILL: original value we add, such as our own testing or data]
2. [FILL]
3. [FILL]
4. [FILL]
5. [FILL]
6. [FILL]

## 21. Compliance guardrails
- Disclosure: [FILL: rule for the YouTube "Altered or synthetic content" setting, copied from 00-start-here/03-compliance-master-checklist.md]
- Sensitive topics: [FILL: what we avoid or handle with sources]
- Sponsorships and affiliate links: [FILL: disclosure rule]

## 22. Unknowns to verify
- [FILL: each UNKNOWN field and how we check it]
```

## Done when

- `style-bible.md` has all 22 sections with no `[FILL: ...]` left.
- Every Our rule is testable.
- Section 20 has at least 6 differences you wrote or approved.
- You hold a compact version of 600 words or less.
- No catchphrase, slogan, or character from the model channel appears in the bible.

## Next

Continue to [04-style-bible-worked-example.md](04-style-bible-worked-example.md).
