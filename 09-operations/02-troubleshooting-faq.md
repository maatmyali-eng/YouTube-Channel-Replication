# Troubleshooting and FAQ

> **Purpose:** Find your symptom, apply the fix, record what happened.
> **Use when:** Something is rejected, flagged, slow, locked, or sounds wrong.
> **Time needed:** 5 to 30 minutes per problem.
> **Needs:** Access to YouTube Studio and your [tracking sheet](03-tracking-sheet.md).
> **Cost:** $0

## Inputs

- The exact message, email text, or Studio status you are seeing (copy it, do not paraphrase).
- [CHANNEL_NAME], [NICHE], [LANGUAGE], [COUNTRY], [HARDWARE].
- Prompt-specific placeholders, defined in P-OPS-02: [SYMPTOM], [EXACT_NOTICE_TEXT], [WHAT_I_ALREADY_TRIED], [VIDEO_LIST].

## Steps

1. Find the group below that matches the symptom (Monetization, Copyright, Retention, CTR, Tool limits, Voice, API, Account).
2. Apply the fix in order. Do not skip the first line of each answer; it tells you what the problem usually is.
3. Where an answer says VERIFY BEFORE RELYING, open the named official YouTube Help page before acting. Policy wording and Studio menu names change.
4. Log the symptom, the fix, and the date in your tracking sheet's Notes column.
5. If nothing here fits, run P-OPS-02.

Facts below carry a verification date. "(verified 2026-10-21)" means I re-checked it against a current source on that date; "(verified 2026-10-20)" means it comes from the repo snapshot only. See [research snapshot](../appendices/research-snapshot.md) for sources and re-verification steps.

### Group A: Monetization and YPP

**Q1. My YPP application says "not enough" even though my dashboard looks right.**
Only public long-form videos (including podcasts) and archived livestreams count toward qualified watch hours. Private, unlisted, deleted, ad-viewed, Shorts, and non-archived live stream hours do not count (verified 2026-10-21; source: YouTube Blog, 12 Aug 2026). Open Studio → Earn and read the progress bars, not the Analytics total.

**Q2. I have 1,000 subscribers, 2,500 watch hours, and 6 million Shorts views. Can I combine them?**
No. Long-form watch hours and Shorts views are separate paths and never combine (verified 2026-10-20). Pick the path you are closer to and concentrate there. Use the pace math in [reality and timeline math](../08-monetization/01-reality-and-timeline-math.md).

**Q3. My Shorts views are high but eligibility shows fewer.**
Qualified Shorts views must be public and engaged: the viewer stayed past the initial seconds, and loops do not count (verified 2026-10-21). Check engaged views per video in YouTube Analytics. Fix the first two seconds of your Shorts so viewers stay; see [Shorts DNA](../03-shorts/01-shorts-dna-analysis.md).

**Q4. Will the 1 February 2027 change affect me?**
It affects NEW applicants to Tier 2: 8,000 watch hours or 20 million Shorts views instead of 4,000 or 10 million. Applying before that date uses the lower numbers (verified 2026-10-21; air.io and vidiq.com, announced 10 Aug 2026). Existing members keep the old threshold but, from the same date, keeping Shorts revenue requires 10 million qualified Shorts views per rolling 90 days. Whether the subscriber count stays at 1,000 is reported by two secondary sources only: VERIFY BEFORE RELYING on the YouTube Help partner program page.

**Q5. I was rejected for "inauthentic content." What do I change?**
The policy targets mass-produced, template-based content with little variation between videos, off-putting or distressing content, and AI personas discussing sensitive topics such as health and finance (verified 2026-10-21; techcrunch.com, 20 Jul 2026). Enforcement looks at patterns across the channel. Fix: (1) list your last 10 uploads and compare titles, structure, and visuals; if more than half share one skeleton, change structure per [differentiation method](../05-originality-layer/01-differentiation-method.md); (2) add original commentary, a personal experiment, or a real demonstration to every video; (3) delete or make private videos that are pure stock-footage-plus-TTS; (4) reapply only after at least 5 new videos show visible variety. The reapply waiting period is in your rejection notice: VERIFY BEFORE RELYING on any number from third-party sites.

**Q6. I was rejected for "reused content."**
This is a separate policy from inauthentic content and did not change in July 2026 (verified 2026-10-20). It covers clips, compilations, and reaction material without enough transformation. Remove other people's footage, audio, and images entirely, or add substantial commentary that cannot stand without your contribution. Then follow [repurposing without reuse](../03-shorts/05-repurposing-without-reuse.md).

**Q7. A video has a yellow "limited ads" icon.**
It means advertiser-friendly guidelines flagged it for limited ads, not that the channel is demonetized. Open Studio → Content, hover the icon, and choose the review option if you believe it is wrong. Then check the title, thumbnail, and first 30 seconds against [sensitive topics](../05-originality-layer/03-sensitive-topics-and-personas.md). Menu wording: VERIFY BEFORE RELYING.

**Q8. YouTube auto-labeled my video as paid promotion.**
YouTube can auto-label undisclosed branded content as of announcements dated 3 Sep 2026 (verified 2026-10-21). Fix: tick the "paid promotion" disclosure in Studio whenever you received money, a free product, or any other compensation, and say so in the video. Do not remove the label by re-uploading.

**Q9. Do I need to label AI voice and AI music?**
The disclosure covers realistic altered or synthetic content. Sources disagree on AI voice and music, so use this table and quote the current YouTube Help page (VERIFY BEFORE RELYING):

| Situation | Label? |
|---|---|
| A real person's voice or face cloned or simulated | Yes, and do not do it without their written permission |
| Realistic scene of an event that did not happen | Yes |
| Generic text-to-speech voice reading a truthful script | Not named on the Help page; one secondary source says no label needed |
| AI-generated music | One secondary source says yes; the Help page is unclear, so label if unsure |
| Animation, clearly unrealistic imagery, minor edits | No |
| AI help with script, title, thumbnail, or outline | No |

Labeling costs nothing and YouTube can add the label itself (since May 2026, verified 2026-10-20). When in doubt, tick the disclosure.

### Group B: Strikes and copyright claims

**Q10. I got a Content ID claim. Is that a strike?**
No. A claim affects that video (revenue, visibility, sometimes blocking) and does not count toward termination (verified 2026-10-21; secondary guides, VERIFY BEFORE RELYING on the Help page). Fix: open Studio → Content → the video → Copyright. Choose to remove the claimed segment with the editor, replace the audio, or accept the claim. Dispute only if you hold a written license for that exact material.

**Q11. I got a copyright strike.**
A strike follows a removal request. Three active strikes within 90 days can lead to termination; each strike expires 90 days after it is issued if you complete Copyright School and have fewer than three (verified 2026-10-21; secondary sources, official page VERIFY BEFORE RELYING). Fix: complete Copyright School; do not re-upload the video; contact the claimant only if you hold a license; use a counter-notification only if you are confident the takedown was a mistake, because it carries legal risk.

**Q12. A royalty-free music track got claimed.**
Free libraries still get claimed when someone registers the same track. Save the license page, the download date, and the track URL for every file in the project. Dispute with that proof. Next time use tracks you can verify under [voice and audio](../02-long-form/03-voice-and-audio.md), or your own recordings.

**Q13. Can I rely on "fair use"?**
No. Fair use is a legal defense decided case by case, not a setting. This repo never depends on it. Make new content that needs no one else's material, per [principles](../00-start-here/02-principles-and-copy-line.md).

**Q14. I got a Community Guidelines strike.**
Read the notice, and remove or edit the flagged content. A first Community Guidelines violation is often a warning, and strikes carry temporary feature limits; exact durations: VERIFY BEFORE RELYING on the YouTube Help strikes page. Appeal in Studio only if you believe the call was wrong, and quote the policy section that you think does not apply.

**Q15. Someone says my content simulates their face or voice.**
YouTube accepts privacy requests for synthetic content that simulates an identifiable person (verified 2026-10-20, repo snapshot; YouTube's responsible-AI announcement). Take the video down at once. Rebuild it with an original character or your own voice.

### Group C: Low retention

**Q16. Viewers leave in the first 30 seconds.**
Open Studio → Analytics → Engagement → Audience retention. If the curve falls sharply early, rewrite the hook with P-LONG-05 in [script chain](../02-long-form/02-script-prompt-chain.md): state the payoff, show proof in the first sentence, and cut the channel intro.

**Q17. Retention is fine at the start but drops in the middle.**
Mark the timestamp of the drop and read the script at that point. Fix: cut the slowest 10 to 15 percent, add an open loop before the dip, and change visuals every few seconds using P-LONG-06.

**Q18. Average view duration is low on long videos.**
Shorten the video to the length where retention stays stable, and remove tangents. A shorter video with higher percentage viewed usually beats a padded one for qualified watch hours per viewer. Compare your numbers with the thresholds in [growth levers and KPIs](../08-monetization/04-growth-levers-and-kpis.md).

**Q19. My Shorts have views but nobody stays.**
Cut the first line to one visual action plus one spoken promise, remove logo stings, and end without a pause. See [Shorts vertical visuals and editing](../03-shorts/04-vertical-visuals-and-editing.md).

### Group D: Low click-through rate

**Q20. CTR is low on every video.**
Check whether thumbnail and title promise the same thing. Rework with P-THUMB-02 in [original generation](../04-thumbnails/02-original-generation.md): one subject, three to five words, strong contrast. Do not change thumbnails before enough impressions accumulate; the minimum is set in [growth levers and KPIs](../08-monetization/04-growth-levers-and-kpis.md).

**Q21. CTR is high but retention is bad.**
Your title or thumbnail over-promises. Rewrite them so the first minute actually delivers the promise. Deceptive metadata can also violate policy.

**Q22. Impressions are very low.**
Recent uploads with low CTR and retention get little distribution. Publish consistently, cover search-intent topics with [metadata and SEO](../02-long-form/05-metadata-and-seo.md), and avoid changing the topic family between videos.

**Q23. Should I test thumbnails on the same video?**
Only with the safe method in [A/B testing and safety](../04-thumbnails/04-ab-testing-and-safety.md). Record each change and date in the sheet so you can read results.

### Group E: Free tools hit limits

**Q24. My free AI chat tool says I reached my limit.**
Limits change. Write prompts once, run them in batches, and switch to a second free tool from [free tool stack](../00-start-here/04-free-tool-stack.md). Save the Style Bible in a document so any tool can load it.

**Q25. The free video generator adds a watermark or forbids commercial use.**
Do not publish watermarked or non-commercial output. Read the tool's terms page for commercial-use status before generating. Free fallback: create visuals with Canva free, DaVinci Resolve free, or your own screen recordings and photos.

**Q26. Colab or a free GPU disconnects mid-render.**
Save checkpoints to Google Drive after each scene, render in short clips, and join them in DaVinci Resolve. If your [HARDWARE] can run CPU tools, use Piper or Kokoro locally.

**Q27. n8n or GitHub Actions runs fail or stop.**
Self-hosted n8n costs nothing in software but needs a machine that stays on. GitHub Actions free minutes are limited and the allowance can change: VERIFY BEFORE RELYING on GitHub's billing page. Move long jobs to a schedule you control.

**Q28. CapCut or Canva free shows a "Pro" item.**
Skip it. Filter for free elements, or export only after removing Pro assets. A Pro asset left in the timeline is the usual cause of an export being blocked.

### Group F: Robotic voice

**Q29. Text-to-speech sounds flat.**
Split long sentences, write contractions, use commas where a person would breathe, and vary sentence length. Re-record the weakest 20 percent. See [voice and audio](../02-long-form/03-voice-and-audio.md).

**Q30. It mispronounces names and terms.**
Respell the word phonetically in the script only (for example, write the sound, not the spelling), then check the audio. Keep a pronunciation list in your Style Bible.

**Q31. Can I use my own voice cloned by AI?**
Only your own voice, with disclosure if realistic and required. Never clone another person's voice. A plain recording of yourself is safer and more distinctive.

### Group G: API uploads stuck private

**Q32. My API uploads stay private even though I set public.**
This is the unaudited-project rule: videos uploaded with videos.insert from unverified API projects created after 28 July 2020 are restricted to private, and setting public does not change that (verified 2026-10-21; singhamandeep.com, upload-post.com). Fix: upload through YouTube Studio by hand or schedule there; pursue the audit only if you truly need API publishing. See [YouTube API and audit](../06-automation/07-youtube-api-and-audit.md).

**Q33. I get a quota error.**
Uploads have a bucket of about 100 videos.insert calls per day, separate from the 10,000 shared units for other endpoints; both reset at midnight Pacific (verified 2026-10-21). Wait for reset or lower your call count. Quota belongs to the project, not the channel.

**Q34. My OAuth token stops working after a few days.**
Apps left in Google's "Testing" status can have refresh tokens that expire quickly. VERIFY BEFORE RELYING on Google's OAuth documentation. Reauthorize, and keep a human in the loop per [human checkpoints](../06-automation/04-human-checkpoints.md).

### Group H: Account problems

**Q35. Studio says I cannot apply because 2-Step Verification is off.**
Turn it on at myaccount.google.com → Security → 2-Step Verification, then return to Studio → Earn.

**Q36. AdSense will not verify.**
Check name and address match your bank and ID, enter the PIN when it arrives, and do not create a second AdSense account. Verification amounts, tax forms, and withholding rules differ by [COUNTRY]: VERIFY BEFORE RELYING on Google AdSense Help.

**Q37. My channel was terminated.**
Use the appeal link in the termination email once. Do not create a new channel to evade the ban. Appeal windows differ in sources (one gives 90 days for strikes); VERIFY BEFORE RELYING on YouTube Help.

**Q38. I cannot upload long videos or set custom thumbnails.**
Complete phone verification in Studio → Settings → Channel → Feature eligibility. Menu name: VERIFY BEFORE RELYING.

## Prompts

### P-OPS-02 — Diagnose my channel problem

**Purpose:** Get a ranked list of likely causes and fixes for a symptom this FAQ does not cover.

**Inputs:** [SYMPTOM] (one sentence), [EXACT_NOTICE_TEXT] (pasted from Studio or email, or "none"), [WHAT_I_ALREADY_TRIED], [VIDEO_LIST] (titles with dates and views for the last 10 uploads), plus [NICHE], [LANGUAGE], [COUNTRY].

```
You are a YouTube channel troubleshooter. You do not guess policy wording.

Symptom: [SYMPTOM]
Exact notice text: [EXACT_NOTICE_TEXT]
What I already tried: [WHAT_I_ALREADY_TRIED]
Last 10 uploads: [VIDEO_LIST]
Niche: [NICHE]  Language: [LANGUAGE]  Country: [COUNTRY]

Return exactly these sections:
1. Classification: one of monetization, copyright, retention, CTR, tools, voice, API, account, other.
2. Top 3 likely causes, each with the evidence in my data that supports it and the evidence that would disprove it.
3. For each cause, a numbered fix I can do today in YouTube Studio or in my files, with exact menu paths where you are confident, and the words "VERIFY BEFORE RELYING" plus the name of the official page where you are not.
4. What NOT to do: list any fix that would break YouTube policy (evasion, re-uploading removed content, deceptive metadata, cloning someone's voice).
5. One measurement I should check in 7 days to know whether the fix worked.

Do not invent policy numbers, thresholds, or dates. Do not promise results.
```

**Expected output:** Five labeled sections tied to your pasted data.

**If the output is weak:** Add your retention and CTR numbers for the last 3 videos, and paste the notice again word for word.

## Done when

- [ ] The symptom is classified and one fix was applied.
- [ ] The date, symptom, and fix are logged in the tracking sheet.
- [ ] Any VERIFY BEFORE RELYING item was checked on the named official page.
- [ ] A 7-day re-check is scheduled.

## Next

[Tracking sheet](03-tracking-sheet.md)
