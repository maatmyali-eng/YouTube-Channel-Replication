# Metadata and SEO (Long-Form)

> **Purpose:** Produce honest titles, description, chapters, pinned comment, end-screen plan, and upload settings, and pair the title with the thumbnail so they make one promise.
> **Use when:** The video is exported and captions are ready, before you open the upload page.
> **Time needed:** 30 to 45 minutes per video.
> **Needs:** Final script, final exported video, `music-log.csv`, the thumbnail concept (see `../04-thumbnails/02-original-generation.md`), a free AI chat assistant.
> **Cost:** $0

Metadata is the packaging, and packaging that overpromises damages retention and can break platform rules. Every instruction below assumes the video delivers what the title and thumbnail say. If it does not, fix the video or the packaging; never write metadata to hide the gap. Misleading titles, thumbnails, and descriptions are a policy risk, and this repo does not use them.

## Inputs

- [CHANNEL_NAME] (your channel), [NICHE], [AUDIENCE], [LANGUAGE], [VIDEO_TOPIC], [STYLE_BIBLE] (title and description habits).
- The final script ([SCRIPT_V3]) and the ANGLE from P-LONG-02 (`02-script-prompt-chain.md`).
- Defined here: [CHAPTER_TIMESTAMPS] (made in Step 1), [ATTRIBUTIONS] (the attribution text lines from `music-log.csv`), [LINKS] (links you actually want in the description), [SPONSOR_STATUS] ("none" or a description of any paid promotion, free product, or affiliate link), [TITLE_PATTERNS] (the title-pattern section of your channel analysis from `../01-channel-dna/02-channel-analysis.md`), [THUMBNAIL_CONCEPT] (one sentence on the planned thumbnail).

## Steps

1. **Make chapter timestamps from the exported video.** In DaVinci Resolve's **Edit** page, put the playhead at the start of each beat from the outline and press **M** to add a marker. Open **Timeline > Markers** (or the marker list in the Index panel) to read the times. Check them against the exported file in a player. Write them as `00:00 Name`, one per line, in a text file `chapters.txt`. YouTube's chapter rules: the first timestamp must be 00:00, there must be at least three timestamps, and each chapter must last at least 10 seconds; otherwise chapters will not appear. This is reported by YouTube Help and third-party guides: VERIFY BEFORE RELYING at YouTube Help, "Add chapters to videos". Chapter names must describe what the section contains, not tease it.
2. **Collect the licence lines.** Open `music-log.csv`. Copy every `attribution_text` for tracks that need credit into [ATTRIBUTIONS]. Do not edit, shorten, or reword them.
3. **Settle [SPONSOR_STATUS].** If you were paid, given a free product, or use affiliate links, say so in the video and tick the paid-promotion setting in Studio (Step 9). YouTube announced on 3 September 2026 that it can auto-label undisclosed branded content (verified 2026-10-20), so disclosing yourself costs nothing. If you have none, write "none".
4. **Write the title and thumbnail pair** with the pairing method below, then run P-LONG-09.
5. **Check the output against reality.** Read each title and the first 150 characters of the description. For each claim, point to the second in the video where it is delivered. No second, no claim.
6. **Apply the packaging rules.**
   - **Title.** Put the main idea and the viewer's benefit in the first 55 to 60 characters, because longer titles are often cut off in the browse feed (heuristic; the hard limit is 100 characters, VERIFY BEFORE RELYING at YouTube Help). Use one clear promise. No ALL-CAPS words except an acronym, no fake numbers, no "SHOCKING" or "you won't believe", no other creator's name used to borrow reach.
   - **Description.** First two lines: what the viewer gets and for whom, in plain words, since those lines show before "Show more". Then a 2 to 4 sentence summary that naturally uses the key phrases viewers search for. Then chapters, links, credits, disclosures. Keep it under YouTube's 5,000-character limit (VERIFY BEFORE RELYING). No keyword lists, no unrelated trending names, no repeated phrases.
   - **Chapters.** Descriptive, 2 to 6 words, one per beat that a viewer might jump to.
   - **Tags.** Treat tags as nearly irrelevant. YouTube Help says tags play a minimal role in discovery and are mainly useful for commonly misspelled terms in your video (VERIFY BEFORE RELYING at YouTube Help, "Add tags to videos"). Add 3 to 8 accurate tags: your main topic phrase, a common misspelling if one exists, and your channel's name. Never add competitor channel names, unrelated viral terms, or tags for things not in the video; that counts as deceptive metadata.
   - **Hashtags.** Zero to three, relevant, placed at the end of the description. YouTube shows up to three above the title.
   - **Pinned comment.** One useful note: a correction list, a resource link, a real question inviting viewers to share their experience. Never ask for subscriptions in a way that implies a reward, and never post fake comments from other accounts.
   - **End screen.** Plan the last 5 to 20 seconds; the video must be at least 25 seconds long. Up to four elements are allowed (video, playlist, subscribe, link). Pick one relevant next video and one subscribe element (verified 2026-10-20 for the 5 to 20 second and 25-second rules).
   - **Cards.** Add at most two, at the moment the video mentions something relevant, such as a related video.
7. **Pairing method for title and thumbnail** (do this before you finalize either):
   1. Write the single promise of the video in one plain sentence: "After this video, the viewer will know/see/be able to ___."
   2. Split the promise. The **thumbnail** carries one image and at most 3 to 4 words of text showing the result or the tension. The **title** carries the topic and the specific benefit. They must not repeat each other word for word; together they should answer "What is this, and why should I care?"
   3. Build a small grid: three title options across, three thumbnail concepts down. Cross each pair and score it 0 to 2 on four questions: Is the promise clear in two seconds? Is the curiosity gap honest (the video answers it)? Do the title and thumbnail add information to each other? Would the viewer feel cheated after watching? Reject any pair with a 0 on honesty.
   4. Choose the highest-scoring pair that also fits the Style Bible's thumbnail and title habits.
   5. If you test packaging inside YouTube Studio, use `../04-thumbnails/04-ab-testing-and-safety.md`, and VERIFY BEFORE RELYING on the feature's current availability and rules.
   6. After 48 hours, compare impressions click-through rate and average view duration (YouTube Studio > **Analytics > Reach** and **Engagement**) against your channel's recent videos. A high click-through rate with weak retention suggests overpromising; fix the packaging, not the video.
8. **Open the upload page** and fill it in with the checklist below. Menu names change, so VERIFY BEFORE RELYING as you go.
9. **Upload settings, in order.** In YouTube Studio click **Create > Upload videos** and select the file.
   - **Details tab:** paste Title and Description. Upload the thumbnail. Add to a playlist. **Audience:** choose whether the video is made for kids (this is a legal setting; answer truthfully). Click **Show more** for: **Paid promotion** (tick only if it applies), **Altered content** (decide with the table in `03-voice-and-audio.md`), **Tags**, **Language and caption certification**, **Category**, and comment settings.
   - **Video elements tab:** add subtitles (upload the SRT), an end screen, and cards.
   - **Checks tab:** wait for the copyright and monetization checks to finish. Do not publish while a check is still running unless you are prepared to edit afterward.
   - **Visibility tab:** choose **Schedule** and set the date and time, or **Public**. Click **Save** or **Schedule**.
10. **After publishing,** add the pinned comment: write the comment, click the three dots beside it, choose **Pin**. Play the video once on the public page to check chapters, captions, and end screen.

## Prompts

### P-LONG-09 — Metadata Pack

**Purpose:** Generate honest title options, a full description with chapters and disclosures, tags, a pinned comment, and an end-screen plan.

**Inputs:** [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [VIDEO_TOPIC], [STYLE_BIBLE] (title and description habits), [TITLE_PATTERNS], [THUMBNAIL_CONCEPT], [CHAPTER_TIMESTAMPS], [ATTRIBUTIONS], [LINKS], [SPONSOR_STATUS], [SCRIPT_V3].

```
You are a YouTube packaging editor. Write metadata for a long-form video on the channel [CHANNEL_NAME] in [NICHE], for [AUDIENCE], in [LANGUAGE].
Topic: [VIDEO_TOPIC]
The video's full script (this is the ground truth of what the video contains): [SCRIPT_V3]
Style Bible habits for titles and descriptions: [STYLE_BIBLE]
Title patterns observed in the modelled channel (patterns only; never reuse its titles): [TITLE_PATTERNS]
Planned thumbnail: [THUMBNAIL_CONCEPT]
Chapter timestamps (final, from the exported video): [CHAPTER_TIMESTAMPS]
Credit lines that must appear unchanged: [ATTRIBUTIONS]
Links to include: [LINKS]
Sponsorship, free products, or affiliate links: [SPONSOR_STATUS]

HARD RULES
1. Every claim in any title, description, chapter, or comment must be delivered in the video. Check against the script. Mark any claim you cannot confirm and remove it.
2. No misleading, exaggerated, or fear-based wording; no fake urgency; no all-caps words other than acronyms; no other creator's name; no keyword stuffing; no unrelated trending terms.
3. Do not invent statistics, testimonials, or results.
4. Do not copy any title from another channel; use only the structural pattern.

OUTPUT
1. TITLES: eight options, each with character count, pattern used, the second in the script where the promise is delivered, and an honesty score (0 = fully delivered, 1 = partly, 2 = not delivered). Keep each at or under 60 characters where possible. Then recommend the best three and say why.
2. THUMBNAIL TEXT: three options of at most 4 words each that do not repeat the title.
3. PAIRING GRID: for the top three titles and the planned thumbnail concept, score each pair 0 to 2 on clarity, honest curiosity, added information, and no-regret, and pick one pair.
4. DESCRIPTION: first two lines for the viewer (benefit and audience), a 2 to 4 sentence summary using the phrases a viewer would search, then the chapters exactly as given, then links, then the credit lines exactly as given, then a disclosure line for any synthetic narration or sponsorship where it applies, then 0 to 3 hashtags.
5. TAGS: 3 to 8 accurate tags and the reason for each. Do not include competitor names or unrelated terms.
6. PINNED COMMENT: one useful comment that adds value (a resource, a correction note, or a question about the viewer's own experience). No sub-for-sub, no incentives.
7. END SCREEN AND CARDS PLAN: what to link at which second, assuming the end screen occupies the last 20 seconds and shows at most four elements.
8. STUDIO SETTINGS CHECKLIST: audience setting, paid promotion (yes/no and why), altered content (yes/no and why, based on the script's use of AI voice and visuals as listed), language, category, comments.
9. A FINAL HONESTY REVIEW: a list of any phrase in the above that a viewer could feel misled by after watching, and a rewrite.
```

**Expected output:** Eight titles with scores, thumbnail text, a pair, a ready-to-paste description, tags, pinned comment, end-screen plan, a settings checklist, and an honesty review.

**If the output is weak:** If titles are bland, reply: "Rewrite titles using the pattern from [TITLE_PATTERNS] but make each state a specific result or number taken from my script." If anything is overpromised, reply: "Rewrite the flagged phrases so each is true at a stated second in the script."

## Done when

- [ ] One title and thumbnail pair is chosen, with every claim matched to a second in the video.
- [ ] Description has the benefit in the first two lines, chapters in `00:00` format (first at 00:00, three or more, each at least 10 seconds), credits unchanged, and disclosures.
- [ ] Tags are 3 to 8 and accurate, with no competitor names.
- [ ] Altered content, paid promotion, and made-for-kids settings are answered deliberately.
- [ ] Subtitle SRT and end screen are added.
- [ ] A pinned comment is ready.

## Next

Continue to [06-prepublish-gate.md](06-prepublish-gate.md).
