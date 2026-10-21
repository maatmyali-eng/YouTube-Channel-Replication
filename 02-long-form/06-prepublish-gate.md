# Pre-Publish Gate (Long-Form)

> **Purpose:** Make a final go, fix, or stop decision on one long-form video using quality and compliance checks before you publish.  
> **Use when:** The video is exported, metadata is drafted, and the upload page is open but you have not pressed Publish or Schedule.  
> **Time needed:** 20 to 30 minutes.  
> **Needs:** The video folder with all outputs, `music-log.csv`, `visuals-log.csv`, `../00-start-here/03-compliance-master-checklist.md`, `../05-originality-layer/02-scoring-rubric.md`.  
> **Cost:** $0  

This gate exists because the cost of publishing a weak or non-compliant video is not one failed video. YouTube's inauthentic-content enforcement reportedly looks at patterns across a channel's recent uploads, so one bad habit can affect monetization channel-wide (reported by third-party coverage of the 16 July 2026 clarification; VERIFY BEFORE RELYING on YouTube Help, "YouTube channel monetization policies"). Nothing in this gate guarantees approval or income; it only raises the odds and removes avoidable mistakes.

## Inputs

- All outputs in the video's folder: `01-owner-assets.md` to `08-originality.md`, `voice.wav`, final video, `chapters.txt`, `music-log.csv`, `visuals-log.csv`, the metadata pack from P-LONG-09, captions.
- [CHANNEL_NAME], [LANGUAGE], [VOICE_MODE], [FACE_OR_FACELESS].
- Defined here: [GATE_FACTS] (the filled block from Step 2), [ORIG_SCORE] (the result of running P-ORIG-01), [GATE_NOTES] (any worry you have).

## Steps

1. **Watch the whole video once, in full, as a viewer would,** on your phone at normal speed. Write the time of every moment where you felt bored, confused, or doubtful of a claim. This takes the length of the video and cannot be replaced by skimming.
2. **Fill the facts block** (copy into `gate.md`, answer from the real files, not from memory):

```
VIDEO: <title>   LENGTH: <mm:ss>   DATE CHECKED: <yyyy-mm-dd>
Original-value items in the video (with timestamps):
Spoken words / target words (from the script):
Own-visual share of runtime (from the shot list):
Longest stretch without a visual change or interrupt (seconds):
Claims tagged [CLAIM-nn]: total / verified at a source I opened / rewritten:
Unfilled [OWNER TO ADD] markers remaining:
Music and effects: files used / rows in music-log.csv / screenshots in proof/:
Loudness measured: integrated LUFS / true peak dBTP:
Synthetic voice used (yes/no); realistic synthetic visuals used (yes/no):
Sponsorship, free product, or affiliate link (yes/no):
Overlap script result (shared 6-word sequences with the modelled video):
Previous 2 videos with the same structure and visuals (yes/no):
Sensitive topic (health, finance, legal, news, children, safety) (yes/no):
```

3. **Run the quality checklist.** Tick only what is true.

   **Content value**
   - [ ] The title and thumbnail promise is delivered, and the video states it in the first 30 seconds.
   - [ ] The video contains at least 1 original-value item per 2 minutes, at least 5 in total, one in the first 90 seconds, one in the last third, all true (this repo's rule, see `02-script-prompt-chain.md`).
   - [ ] No unfilled [OWNER TO ADD] remains.
   - [ ] No loop opened in the video is left unanswered.
   - [ ] The video has a point of view or a demonstration that a viewer cannot get from reading the first five search results.

   **Delivery**
   - [ ] Voice is clear on a phone speaker and has no clicks, mispronunciations, or robotic runs.
   - [ ] Integrated loudness is -15 to -13 LUFS and true peak at or below -1 dBTP (see `03-voice-and-audio.md`).
   - [ ] Music is under the voice and never masks words.
   - [ ] Visual changes occur at the interval in your Style Bible, and the five tests in `04-visual-production.md` Step 9 pass.
   - [ ] Captions are corrected against the script.
   - [ ] The last 20 seconds are clear for an end screen.

   **Metadata**
   - [ ] Every claim in title, description, chapters, and pinned comment is delivered at a second in the video.
   - [ ] Chapters begin at 00:00, number three or more, and each lasts at least 10 seconds.
   - [ ] Credits and attribution lines appear exactly as in the music log.
   - [ ] Tags are accurate and include no competitor names.

4. **Run the compliance checklist.** Open `../00-start-here/03-compliance-master-checklist.md` and complete it for this video. Do not skip an item because "it passed last time." Then confirm these video-specific points:
   - [ ] **Copying line.** No sentence, joke, catchphrase, footage, music, thumbnail, logo, character, or likeness from the modelled channel is in the video. The overlap check shows no shared 6-word sequence beyond common phrases and names.
   - [ ] **Licences.** Every music, effect, stock, and image file has a row in the log, a licence URL, and a screenshot of the licence page from the download day. No non-commercial licence is used.
   - [ ] **Voice.** No cloned voice of a real person. If [VOICE_MODE] used TTS, the voice is a stock engine voice whose model licence allows commercial use, and the disclosure decision from `03-voice-and-audio.md` is recorded.
   - [ ] **Altered content.** The Studio setting matches the table decision; realistic AI visuals are disclosed (verified 2026-10-20 that YouTube requires disclosure of realistic synthetic content, and that disclosure does not limit reach or monetization).
   - [ ] **Paid promotion.** Any sponsorship, free product, or affiliate link is disclosed in the video and in Studio (YouTube can auto-label undisclosed branded content since 3 September 2026; verified 2026-10-20).
   - [ ] **Inauthentic-content categories** (verified 2026-10-20): (1) not generic, repetitive, or template-based compared with the last two videos; (2) nothing off-putting or distressing for shock value; (3) no AI persona giving health, finance, or similar sensitive advice. If the topic is sensitive, read `../05-originality-layer/03-sensitive-topics-and-personas.md` and confirm each rule it lists.
   - [ ] **Privacy and safety.** No private information, license plates, children's faces, or addresses visible. Made-for-kids setting answered honestly.
   - [ ] **Factual accuracy.** All high-stakes claims were checked at sources you opened.

5. **Score originality.** Run P-ORIG-01 from `../05-originality-layer/02-scoring-rubric.md`, which returns the [ORIG_SCORE]. Use its pass mark as written in that file. If you have not run it, you cannot reach GO.
6. **Run P-LONG-14** below with the filled facts block, your watch-through notes, and the ORIG_SCORE.
7. **Apply the decision rule.**

| Decision | When it applies | What you do |
|---|---|---|
| **GO** | All quality and compliance boxes are ticked; no unfilled markers; P-ORIG-01 meets the pass mark in the rubric; no red flag below | Publish or schedule. Log the video in `../09-operations/03-tracking-sheet.md` |
| **FIX** | One or more boxes unticked, but each can be fixed in under 2 hours without changing the video's topic, and no red flag applies | Fix the items, re-run Steps 3, 4, and 5 for changed parts only, re-run P-LONG-14, then decide again. A FIX decision may be repeated at most twice; a third failure becomes STOP |
| **STOP** | Any red flag below | Do not publish. Decide whether to rework the video from the script stage or discard it |

   **Red flags that force STOP**
   - Use of another creator's words, footage, music, thumbnail, voice, or likeness.
   - A cloned or impersonated real person's voice or likeness.
   - A licence you cannot prove for any asset.
   - Realistic synthetic footage presented as real, or fabricated quotes, testimonials, or results.
   - Health, finance, legal, or safety advice given by an AI persona without sourced, qualified framing.
   - Metadata that promises what the video does not deliver.
   - Two or more of your last three videos have nearly identical structure, visuals, and opening with only the topic changed, and you have no variation planned.
   - No original-value item in the video, or an original-value item that is not true.
   - The overlap check shows copied sequences you cannot rewrite.

8. **Record the decision** with the date in `gate.md`. If you scheduled the video, set a reminder to check the first 48 hours of analytics (click-through rate, average view duration) as described in `05-metadata-and-seo.md`.

## Prompts

### P-LONG-14 — Gate Review

**Purpose:** Get an independent, strict reading of your facts block and notes and a GO / FIX / STOP recommendation with a minimal fix list.

**Inputs:** [GATE_FACTS] (your filled block), [GATE_NOTES] (watch-through notes and any worries), [ORIG_SCORE] (the P-ORIG-01 result), [METADATA_PACK] (the P-LONG-09 output you plan to use), [CHANNEL_NAME], [NICHE], [VOICE_MODE], [FACE_OR_FACELESS], [LANGUAGE].

```
You are a strict pre-publication reviewer for a YouTube channel called [CHANNEL_NAME] in [NICHE], written in [LANGUAGE]. The channel uses voice mode [VOICE_MODE] and presentation [FACE_OR_FACELESS]. Decide whether this video is ready to publish. Be critical and specific. Do not flatter.

FACTS ABOUT THIS VIDEO
[GATE_FACTS]

WATCH-THROUGH NOTES AND WORRIES
[GATE_NOTES]

ORIGINALITY SCORE RESULT
[ORIG_SCORE]

METADATA TO BE PUBLISHED
[METADATA_PACK]

REVIEW RULES
- Base every judgement only on the facts, notes, score, and metadata above. If a fact is missing or blank, treat it as a failed check and list it as missing.
- Use these rules (this repository's gate): at least 1 original-value item per 2 minutes and at least 5 in total; no unfilled owner markers; every claim verified at a source the owner opened; integrated loudness -15 to -13 LUFS and true peak at or below -1 dBTP; all music, effects, and visuals logged with licence proof; no cloned voice; realistic synthetic visuals disclosed; sponsorships disclosed; not templated against the previous two videos; sensitive topics handled with sourced, qualified framing; metadata matches the video.
- RED FLAGS FORCE STOP: copied expression from another creator; cloned or impersonated voice or likeness; an unprovable licence; realistic synthetic footage presented as real; fabricated quotes or results; AI persona giving sensitive advice; metadata promising what the video does not deliver; a repeated template with only the topic changed; no true original-value item.
- Do not suggest evading detection, hiding AI use, or tricking review systems. Do not guarantee approval or income.

OUTPUT
1. DECISION: GO, FIX, or STOP, on the first line.
2. TABLE of checks: Check | Pass / Fail / Missing | Evidence from the inputs.
3. FIX LIST: numbered, smallest set of changes needed to reach GO, with an estimated time for each. If the decision is STOP, say whether to rework from the script stage or discard, and why.
4. TOP THREE RISKS to monetization or policy standing if the video were published as is, ranked.
5. ONE-SENTENCE NOTE on what to do differently in the next video to avoid the same weakness.
```

**Expected output:** A one-word decision, a pass/fail table, a short fix list with times, three ranked risks, and a note for the next video.

**If the output is weak:** If the decision is GO but there are blanks in your facts block, reply: "Treat every blank as Missing and recompute the decision." If the review is vague, reply: "Cite the exact field from the facts block for each failed check."

## Done when

- [ ] `gate.md` exists with the filled facts block, the ticked checklists, and a dated GO, FIX, or STOP.
- [ ] The compliance master checklist is completed for this video.
- [ ] P-ORIG-01 has been run and meets the pass mark in the rubric.
- [ ] P-LONG-14 returned GO, or the FIX list has been completed and re-reviewed.
- [ ] The video is logged in the tracking sheet, and a 48-hour analytics check is scheduled.

## Next

Long-form production is complete for this video. Continue to Shorts with [../03-shorts/01-shorts-dna-analysis.md](../03-shorts/01-shorts-dna-analysis.md), or return to [../09-operations/01-quick-start.md](../09-operations/01-quick-start.md) for the weekly routine.
