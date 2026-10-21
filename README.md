# yt-style-system

> Purpose: replicate the style of any YouTube channel as new, original, policy-safe content | Use when: you want to model a channel you admire without copying it | Time needed: 60 minutes to set up a new channel | Needs: a browser, a free Google account, a free AI chat tool | Cost: $0

## What this repo is

yt-style-system is a set of guides, copy-paste prompts, templates, workflows and one checking script for building a YouTube channel in the style of a channel you choose. It covers long-form videos, Shorts, thumbnails, metadata, automation, and a plan to reach monetization as fast as the rules allow. Nothing in it is tied to one channel. Everything channel-specific is a square-bracket variable such as [CHANNEL_URL] or [STYLE_BIBLE], which you fill in once per channel.

It is for solo creators and small teams who have more time than money, want to run the process again for each new channel, and want a result that YouTube can monetize. It is not a tool for cloning a creator, and it does not hide anything from YouTube.

## The $0 promise and its limits

Every tool and method here is chosen because it has a free path. For each tool the files state the real free limits, whether output carries a watermark, whether commercial use is allowed, any paid trap, and a free fallback. Limits that hold at the time of writing:

- Free tiers change. A tool that is free today can add a watermark, a quota or a licence condition. Re-check before you depend on it.
- Free costs time. Several free tools need a capable computer or many hours of hands-on work. [HARDWARE] and [WEEKLY_HOURS] in the setup card decide which route fits you.
- Free does not include a paid shortcut. If a step cannot be done at $0, the file says so and gives the free alternative instead.

## The copy-the-style line

"Copy" means deep, systematic replication of a channel's style: tone, voice, script structure, hook mechanics, pacing, open loops, editing rhythm, audio design, colour and typography, thumbnail composition, title patterns, series structure and upload cadence. The output is always new content in the same family of style: new scripts, new visuals, new audio, new thumbnails.

It never reproduces another creator's words, footage, voiceover, music, thumbnails, logos, characters or likeness. That line is also what keeps a channel monetizable, because YouTube demonetizes copied and mass-produced content, not shared styles.

## Disclaimer

No income outcome and no policy outcome is guaranteed. YouTube's policies, thresholds and features change, and the files here describe them as they were on the dates shown. Any fact marked "verified" carries a date; anything marked VERIFY BEFORE RELYING must be checked on the official YouTube Help page named beside it. Monetization decisions are YouTube's, not this repo's. Nothing here is legal, tax or financial advice.

Example of a dated fact, because thresholds are the number people ask about most: the higher Partner Program tier (ads and Premium revenue share) currently needs 1,000 subscribers plus either 4,000 qualified public watch hours in 12 months or 10 million qualified Shorts views in 90 days. For new applicants from 1 February 2027, reporting says the bar becomes 8,000 watch hours or 20 million Shorts views, with the 1,000-subscriber requirement unchanged (verified 2026-10-21 against secondary sources; confirm on YouTube Help, "YouTube Partner Program overview & eligibility", before relying). Shorts views and long-form watch hours never combine. The full table, with disagreements between sources, is in [appendices/research-snapshot.md](appendices/research-snapshot.md).

## Quick map of every folder

| Folder | What it holds |
|---|---|
| [00-start-here/](00-start-here/01-setup-card.md) | Setup card, principles, compliance checklist, free tool stack |
| [01-channel-dna/](01-channel-dna/01-data-gathering.md) | Compliant data gathering, channel analysis, the Style Bible template and a worked example |
| [02-long-form/](02-long-form/01-video-dna-analysis.md) | Video analysis, script prompt chain, voice and audio, visuals, metadata, pre-publish gate |
| [03-shorts/](03-shorts/01-shorts-dna-analysis.md) | Shorts analysis, script chain, batch scripts, vertical editing, repurposing without reuse, gate |
| [04-thumbnails/](04-thumbnails/01-thumbnail-dna-analysis.md) | Thumbnail analysis, original generation, design workflow, A/B testing and safety |
| [05-originality-layer/](05-originality-layer/01-differentiation-method.md) | Differentiation method, scoring rubric, sensitive topics and personas |
| [06-automation/](06-automation/01-pipeline-architecture.md) | Pipeline design, no-code, bulk, human checkpoints, low-code, custom software, YouTube API |
| [07-build-your-own/](07-build-your-own/01-ideas-research-and-ideation.md) | Ideas for your own tools, plus a starter channel-style analyzer |
| [08-monetization/](08-monetization/01-reality-and-timeline-math.md) | Timeline maths, 30-day plan, parallel routes, KPIs, scenarios, mistakes |
| [09-operations/](09-operations/01-quick-start.md) | Quick start, troubleshooting FAQ, tracking sheet |
| [templates/](templates/content-calendar.md) | Content calendar and per-video checklist |
| [appendices/](appendices/research-snapshot.md) | Research snapshot and glossary |
| [scripts/](scripts/check_repo.py) | The repo checker and prompt-library generator |

## Master workflow: zero to growth

Work through the phases in order. Each phase ends at a "Done when" list inside the last file of that phase.

### Phase 1. Setup

1. Read [00-start-here/01-setup-card.md](00-start-here/01-setup-card.md) and fill in every variable. Keep the completed card; every later prompt takes its values from it.
2. Read [00-start-here/02-principles-and-copy-line.md](00-start-here/02-principles-and-copy-line.md).
3. Read [00-start-here/03-compliance-master-checklist.md](00-start-here/03-compliance-master-checklist.md).
4. Choose your tools from [00-start-here/04-free-tool-stack.md](00-start-here/04-free-tool-stack.md).

### Phase 2. Choose and analyze the channel

5. Gather data the permitted way: [01-channel-dna/01-data-gathering.md](01-channel-dna/01-data-gathering.md).
6. Run the channel analysis: [01-channel-dna/02-channel-analysis.md](01-channel-dna/02-channel-analysis.md).
7. Create your Style Bible from [01-channel-dna/03-style-bible-template.md](01-channel-dna/03-style-bible-template.md). The filled-in demonstration is in [01-channel-dna/04-style-bible-worked-example.md](01-channel-dna/04-style-bible-worked-example.md).

### Phase 3. Create long-form

8. Analyze reference videos: [02-long-form/01-video-dna-analysis.md](02-long-form/01-video-dna-analysis.md).
9. Write the script with the prompt chain: [02-long-form/02-script-prompt-chain.md](02-long-form/02-script-prompt-chain.md).
10. Produce voice and audio: [02-long-form/03-voice-and-audio.md](02-long-form/03-voice-and-audio.md).
11. Produce visuals and edit: [02-long-form/04-visual-production.md](02-long-form/04-visual-production.md).

### Phase 4. Create Shorts

12. Analyze Shorts: [03-shorts/01-shorts-dna-analysis.md](03-shorts/01-shorts-dna-analysis.md).
13. Write single scripts: [03-shorts/02-script-prompt-chain.md](03-shorts/02-script-prompt-chain.md). For weekly batches use [03-shorts/03-batch-scripts.md](03-shorts/03-batch-scripts.md).
14. Make vertical visuals and edit: [03-shorts/04-vertical-visuals-and-editing.md](03-shorts/04-vertical-visuals-and-editing.md).
15. Turn long-form into Shorts without reusing footage you should not reuse: [03-shorts/05-repurposing-without-reuse.md](03-shorts/05-repurposing-without-reuse.md).

### Phase 5. Thumbnails

16. Analyze thumbnail style: [04-thumbnails/01-thumbnail-dna-analysis.md](04-thumbnails/01-thumbnail-dna-analysis.md).
17. Generate original thumbnails: [04-thumbnails/02-original-generation.md](04-thumbnails/02-original-generation.md).
18. Build them in a repeatable workflow: [04-thumbnails/03-design-workflow-and-templates.md](04-thumbnails/03-design-workflow-and-templates.md).
19. Test and check safety: [04-thumbnails/04-ab-testing-and-safety.md](04-thumbnails/04-ab-testing-and-safety.md).

### Phase 6. Originality check

20. Apply the differentiation method: [05-originality-layer/01-differentiation-method.md](05-originality-layer/01-differentiation-method.md).
21. Score every video with the rubric: [05-originality-layer/02-scoring-rubric.md](05-originality-layer/02-scoring-rubric.md).
22. Check sensitive topics and AI personas before you commit to a topic: [05-originality-layer/03-sensitive-topics-and-personas.md](05-originality-layer/03-sensitive-topics-and-personas.md).

### Phase 7. Automation

23. Design the pipeline: [06-automation/01-pipeline-architecture.md](06-automation/01-pipeline-architecture.md).
24. Pick a build route: no-code in [06-automation/02-no-code-workflow.md](06-automation/02-no-code-workflow.md), low-code in [06-automation/05-low-code-workflow.md](06-automation/05-low-code-workflow.md), or your own software in [06-automation/06-custom-software.md](06-automation/06-custom-software.md).
25. Add bulk systems: [06-automation/03-bulk-systems.md](06-automation/03-bulk-systems.md).
26. Put human checkpoints in: [06-automation/04-human-checkpoints.md](06-automation/04-human-checkpoints.md). Automation here always ends in human review.
27. Read the API limits before you automate uploads: [06-automation/07-youtube-api-and-audit.md](06-automation/07-youtube-api-and-audit.md).
28. Optional extra ideas: [07-build-your-own/01-ideas-research-and-ideation.md](07-build-your-own/01-ideas-research-and-ideation.md), [07-build-your-own/02-ideas-script-and-voice.md](07-build-your-own/02-ideas-script-and-voice.md), [07-build-your-own/03-ideas-visuals-and-editing.md](07-build-your-own/03-ideas-visuals-and-editing.md), [07-build-your-own/04-ideas-publishing-and-analytics.md](07-build-your-own/04-ideas-publishing-and-analytics.md) and [07-build-your-own/05-channel-style-analyzer-starter.md](07-build-your-own/05-channel-style-analyzer-starter.md).

### Phase 8. Publish

29. Write titles, descriptions and tags: [02-long-form/05-metadata-and-seo.md](02-long-form/05-metadata-and-seo.md).
30. Pass the long-form gate: [02-long-form/06-prepublish-gate.md](02-long-form/06-prepublish-gate.md). For Shorts use [03-shorts/06-prepublish-gate.md](03-shorts/06-prepublish-gate.md).
31. Complete the per-video checklist: [templates/per-video-checklist.md](templates/per-video-checklist.md).

### Phase 9. Monetization

32. Understand the real timeline: [08-monetization/01-reality-and-timeline-math.md](08-monetization/01-reality-and-timeline-math.md).
33. Follow the 30-day plan: [08-monetization/02-30-day-plan.md](08-monetization/02-30-day-plan.md).
34. Open parallel routes: [08-monetization/03-parallel-routes.md](08-monetization/03-parallel-routes.md).
35. Track growth levers and KPIs: [08-monetization/04-growth-levers-and-kpis.md](08-monetization/04-growth-levers-and-kpis.md).
36. Read the scenarios and the mistakes list: [08-monetization/05-income-scenarios.md](08-monetization/05-income-scenarios.md) and [08-monetization/06-mistakes-to-avoid.md](08-monetization/06-mistakes-to-avoid.md).

### Phase 10. Weekly operation

37. Run the quick start: [09-operations/01-quick-start.md](09-operations/01-quick-start.md).
38. Plan the week in [templates/content-calendar.md](templates/content-calendar.md) and log results in [09-operations/03-tracking-sheet.md](09-operations/03-tracking-sheet.md).
39. When something goes wrong, open [09-operations/02-troubleshooting-faq.md](09-operations/02-troubleshooting-faq.md). Unknown terms are in [appendices/glossary.md](appendices/glossary.md).

The full list of prompts, with IDs, is in [prompt-library.md](prompt-library.md), generated by the checker script.

## How to run this repo for a new channel in 60 minutes

This gets you from nothing to a first script and thumbnail brief. It assumes you have already chosen a reference channel.

1. Minutes 0 to 10: copy the repo, then fill in the setup card ([00-start-here/01-setup-card.md](00-start-here/01-setup-card.md)).
2. Minutes 10 to 15: skim the compliance checklist ([00-start-here/03-compliance-master-checklist.md](00-start-here/03-compliance-master-checklist.md)) and note any topic that is off limits for your niche.
3. Minutes 15 to 25: collect the public data for the reference channel by the methods in [01-channel-dna/01-data-gathering.md](01-channel-dna/01-data-gathering.md).
4. Minutes 25 to 40: run the channel analysis prompt and the Style Bible prompt (P-CDNA-01 and P-CDNA-02, in [01-channel-dna/02-channel-analysis.md](01-channel-dna/02-channel-analysis.md) and [01-channel-dna/03-style-bible-template.md](01-channel-dna/03-style-bible-template.md)). Save the result as your [STYLE_BIBLE].
5. Minutes 40 to 55: run the topic, outline and hook prompts in [02-long-form/02-script-prompt-chain.md](02-long-form/02-script-prompt-chain.md).
6. Minutes 55 to 60: score the draft with [05-originality-layer/02-scoring-rubric.md](05-originality-layer/02-scoring-rubric.md) and enter the video in [09-operations/03-tracking-sheet.md](09-operations/03-tracking-sheet.md).

Voice, visuals, editing and publishing take further sessions; the phases above cover them.

## Which files to reuse unchanged

Copy these into every new channel without editing. Re-verify the dated facts in them each month.

- [00-start-here/02-principles-and-copy-line.md](00-start-here/02-principles-and-copy-line.md) and [00-start-here/03-compliance-master-checklist.md](00-start-here/03-compliance-master-checklist.md)
- [00-start-here/04-free-tool-stack.md](00-start-here/04-free-tool-stack.md) (tool limits and licences change; check the monthly list below)
- The method files: everything in 02-long-form, 03-shorts, 04-thumbnails, 05-originality-layer, 06-automation and 07-build-your-own, because their prompts take your variables rather than channel facts
- Everything in 08-monetization, apart from the dates and numbers you refresh
- [09-operations/02-troubleshooting-faq.md](09-operations/02-troubleshooting-faq.md), [appendices/glossary.md](appendices/glossary.md) and [scripts/check_repo.py](scripts/check_repo.py)

## Which files to refill per channel

Make a fresh copy of each of these for every channel.

- [00-start-here/01-setup-card.md](00-start-here/01-setup-card.md): all variables
- Your saved outputs from [01-channel-dna/02-channel-analysis.md](01-channel-dna/02-channel-analysis.md) and [01-channel-dna/03-style-bible-template.md](01-channel-dna/03-style-bible-template.md): the analysis and the [STYLE_BIBLE]
- [09-operations/03-tracking-sheet.md](09-operations/03-tracking-sheet.md): the sheet you build from it
- [templates/content-calendar.md](templates/content-calendar.md) and [templates/per-video-checklist.md](templates/per-video-checklist.md): one filled copy per video or per month

[01-channel-dna/04-style-bible-worked-example.md](01-channel-dna/04-style-bible-worked-example.md) stays as a reference. Do not edit it for your channel.

## How to keep it current

Re-verify the research snapshot every month. Put a repeating reminder in your calendar for the first day of the month and do this:

1. Open [appendices/research-snapshot.md](appendices/research-snapshot.md). For each row, open the source named in that row. For policy and threshold rows the official page is YouTube Help; for tool rows it is the tool's own licence and pricing page.
2. Change the figure, change the "verified" date, or write VERIFY BEFORE RELYING if you cannot reach the official page. Use the comparison prompt in that file (P-OPS-06) if you want help checking a pasted page against a row.
3. Search the repo for the old figure and update every file that repeats it. Common repeats: Partner Program thresholds, the 1 February 2027 change, AI disclosure wording, API upload limits and tool licences.
4. Re-check these items by hand because they have changed or been reported inconsistently: the Partner Program requirement after 1 February 2027, whether AI voice or music needs a disclosure label, the API upload quota cost, the date of the inauthentic-content clarification, and the licence of the Piper voice engine (its maintained repository is now reported as GPL-3.0-or-later; check the wording in [00-start-here/04-free-tool-stack.md](00-start-here/04-free-tool-stack.md) and [02-long-form/03-voice-and-audio.md](02-long-form/03-voice-and-audio.md) against the licence file in the repository).
5. Run the checker script (next section) and fix anything it reports.

## How to run the checker script

The script uses only the Python 3 standard library. Run it from the repo root, or from anywhere by giving the path:

```bash
python3 scripts/check_repo.py
python3 scripts/check_repo.py --root /path/to/yt-style-system
python3 scripts/check_repo.py --strict
python3 scripts/check_repo.py --no-write
```

What it does, in order:

1. Scans every Markdown file for prompt headings in the exact form "### P-CODE-NN — Name" and writes [prompt-library.md](prompt-library.md) as a table of ID, name, file and folder, sorted by folder and then ID.
2. Warns when two prompts share an ID, or when a heading starts with "### P-" but does not match the required form.
3. Confirms every file in the repo tree exists.
4. Confirms every relative Markdown link resolves to a real file, with the exact letter case that GitHub uses.
5. Warns when a file contains the placeholder markers for unfinished work (the to-do marker, the to-be-decided marker) or the abbreviation that means "and so on".
6. Prints PASS or FAIL. Missing files and broken links make it FAIL and return exit code 1. Warnings alone still PASS, unless you pass `--strict`, which turns warnings into failures. `--no-write` checks everything without rewriting prompt-library.md.

Run it after every edit session and before you share or publish the repo.
