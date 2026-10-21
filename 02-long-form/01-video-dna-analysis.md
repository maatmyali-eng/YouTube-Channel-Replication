# Video DNA Analysis (Long-Form)

> **Purpose:** Turn one long-form video from the channel you are modelling into a list of reusable mechanics (hook, beats, open loops, interrupts, visual logic, sound, ending), without keeping any of its wording.  
> **Use when:** After you have picked 3 to 5 videos from the channel analysis, and before you write your first script.  
> **Time needed:** 45 to 60 minutes per video (watching plus one prompt run).  
> **Needs:** A browser, a free AI chat assistant, a plain-text editor, the [STYLE_BIBLE] draft if you have one.  
> **Cost:** $0  

Why this file exists: the Style Bible (see `../01-channel-dna/03-style-bible-template.md`) describes a channel in general. This file measures single videos so the Style Bible rests on evidence and so your scripts copy mechanics at the right timing. It never copies sentences, jokes, footage, or music. Copying those would be reused content, and YouTube's inauthentic-content clarification of 16 July 2026 targets generic, repetitive, template-based output (verified 2026-10-20). Copying mechanics is how every genre forms.

## Inputs

- [CHANNEL_URL], the channel you are modelling.
- [NICHE], [AUDIENCE], [LANGUAGE] from `../00-start-here/01-setup-card.md`.
- [VIDEO_LENGTH], the length of the video being analysed, for example `11:42`. For your own planned video it means your target length.
- [TRANSCRIPT], the transcript of the analysed video, with timestamps if possible.
- Defined in this file only: [VIDEO_TITLE] (the title as shown publicly), [WATCH_NOTES] (your timestamped notes from the watch passes below), [WORDS_PER_MINUTE] (default 150; use 140 for a calm voice, 170 for a fast voice).

## Steps

1. **Choose the videos.** Use the outlier picks from `../01-channel-dna/02-channel-analysis.md`. Take 2 outperformers, 1 typical video, and 1 weak video. Comparing strong with weak shows which mechanics matter. Skip videos under 6 minutes here; Shorts have their own file.
2. **Get the transcript from the public watch page.** Open the video on youtube.com. Under the video, click the description box (`...more`), then click **Show transcript**. In the transcript panel, open the three-dot menu and choose **Toggle timestamps** so timestamps are visible. Select all lines in the panel and copy. The exact button layout changes often: VERIFY BEFORE RELYING by checking YouTube Help, "Get a video transcript". Do not download the video, do not use rippers, and do not scrape at scale; that breaks YouTube's Terms of Service.
3. **Save it privately.** Paste into a text file at `transcripts-private/<video-id>.txt`. This folder is gitignored (see `../01-channel-dna/01-data-gathering.md`). Never publish or commit it. The transcript is another creator's text, used here only as analysis input.
4. **Do three watch passes** and write [WATCH_NOTES] as you go.
   - Pass 1, normal speed, no notes. Just watch as a viewer.
   - Pass 2, normal speed, with the notes table below. Note every visual change, on-screen text, music change, and sound effect.
   - Pass 3, muted at 1.5x speed. This isolates what the picture does by itself: cut rhythm, graphics, text.
5. **Check for "Most replayed".** On the watch page, hover over the progress bar. If YouTube shows a bumpy graph above it, note the 2 or 3 highest peaks in your notes. Only some videos show it. It is a public signal, not the full retention curve. VERIFY BEFORE RELYING that it still appears in your region.
6. **Run P-LONG-01** below. Paste [TRANSCRIPT] and [WATCH_NOTES] in the placeholders.
7. **Spot-check the output.** Pick 5 timestamps from the beat table and scrub the video to them. If more than 1 of 5 is wrong by more than 10 seconds, rerun with the timestamps-on transcript, or fix the table by hand. Do not build on a wrong beat map.
8. **Save the report** to `reports/video-dna-<video-id>.md`.
9. **Merge after 3 to 5 videos.** Add the reports as evidence when you run P-CDNA-02 in `../01-channel-dna/03-style-bible-template.md`. Rules that appear in every report become Style Bible rules. Rules that appear in one report stay as "optional".

### Watch notes template (copy into a text file)

```
VIDEO: [VIDEO_TITLE]  LENGTH: [VIDEO_LENGTH]
Format per line: mm:ss | VISUAL / TEXT / MUSIC / SFX | what changed

00:00 | VISUAL | 
00:00 | TEXT   | 
00:00 | MUSIC  | (none / starts / stops / swells / drops)
00:00 | SFX    | (whoosh / hit / click / ambience / none)

Overall music: genre, tempo feel, loudness relative to voice (under / equal / over)
Overall color and font look: 
Narration style: (to camera / voice only / mixed)
Most replayed peaks: 
```

If the video has no music, write `MUSIC: none` for the whole video. An honest "none" is data.

## Prompts

### P-LONG-01 — Video DNA Analysis

**Purpose:** Extract the transferable mechanics of one long-form video as tables and numbered rules, with no copied wording.

**Inputs:** [CHANNEL_URL], [VIDEO_TITLE], [VIDEO_LENGTH], [LANGUAGE], [NICHE], [AUDIENCE], [WORDS_PER_MINUTE], [TRANSCRIPT], [WATCH_NOTES].

```
You are a video-structure analyst. Your job is to extract the transferable MECHANICS of one long-form YouTube video so a different creator can build original videos in the same family of style. You are not summarizing the video's topic and you must not preserve its wording.

HARD RULES
1. Describe and paraphrase. Never quote more than 5 consecutive words from the transcript. Never reproduce jokes, catchphrases, named recurring segments, or full sentences.
2. Use only the evidence in the TRANSCRIPT and WATCH NOTES below. If something is not observable (for example music, when the watch notes contain no audio lines), write NOT OBSERVABLE. Do not guess and do not invent timestamps.
3. Timestamps use mm:ss. If the transcript has no timestamps, estimate them from word position (word count divided by [WORDS_PER_MINUTE] words per minute) and mark every such timestamp "est."
4. Every statement about audience retention is a HYPOTHESIS. Label it as one. You have no analytics for this video.
5. Do not judge whether the video is good. Describe what it does.

INPUTS
Channel being modelled: [CHANNEL_URL]
Video title: [VIDEO_TITLE]
Video length: [VIDEO_LENGTH]
Language: [LANGUAGE]
Niche: [NICHE]
Audience: [AUDIENCE]
Words per minute baseline: [WORDS_PER_MINUTE]

TRANSCRIPT
[TRANSCRIPT]

WATCH NOTES
[WATCH_NOTES]

PRODUCE THESE SECTIONS IN THIS ORDER

1. SNAPSHOT
Total words (count them). Words per minute (total words divided by length in minutes). Average sentence length in words (estimate from 20 sampled sentences and say you sampled). Grammatical person (I / you / we). Register (casual, expert, teacher, comedic, other). Jargon level (low / medium / high). The video's single promise to the viewer in one sentence of your own words.

2. HOOK (from 00:00 to the point where the main body starts, normally 15 to 45 seconds)
A table with columns: Time range | What happens (paraphrase) | Mechanic (cold-open claim, question, stakes, contrast, live demonstration, story-in, pattern break, other) | Purpose.
Then answer: What is promised? How many seconds until the viewer sees the first proof that the promise is being delivered? Does the hook restate the title or thumbnail promise? Then write the HOOK FORMULA as a fill-in-the-blank template using bracketed placeholders only, with no words from the original.

3. STRUCTURE BEATS
A table with columns: # | Start-End | Beat name (your label) | Function (setup, demonstration, proof, tension, payoff, recap, transition, call to action) | Approx words | Device used to move to the next beat.
Cover the whole video with no gaps.

4. OPEN-LOOP LEDGER
A table with columns: Loop # | Opened at | The question or tension raised (paraphrase) | How it is kept alive | Closed at | Gap in seconds.
Then state: average gap, longest gap, number of loops opened and never closed, and whether loops are nested or sequential.

5. PATTERN INTERRUPTS
A table with columns: Time | Type (visual change, tone shift, sound, speed change, direct address, question to viewer, reveal, humor, on-screen text) | Evidence source (transcript or watch notes).
Then state: average interrupts per minute and the longest stretch with none.

6. B-ROLL AND VISUAL LOGIC (use watch notes only)
A table with columns: Narration type (claim, step, story, statistic, opinion, transition) | Visual type used | Typical shot length in seconds. Then state: estimated cuts per minute, graphic style, how on-screen text is used, whether the creator appears on camera and when.

7. MUSIC AND SOUND CUES (use watch notes only)
Music: when it enters and leaves, volume relative to voice, how it changes at key beats. Sound effects: which moments get one and what type. Silence: where silence is used on purpose. Write NOT OBSERVABLE for anything the notes do not cover.

8. ENDING
Structure of the last 60 seconds. Type and placement of the call to action. Whether the ending loops back to the hook. Length of the outro. What the final line does (describe the function, do not quote it). What is on screen during the last 20 seconds.

9. RETENTION-CURVE HYPOTHESES
Give 4 to 6. For each: approximate time, expected dip or plateau, the structural reason from sections 2 to 8, confidence (low / medium / high) and how the owner could check it (for example "compare with the Most replayed peaks in the notes").

10. TRANSFERABLE RULES
Write 10 to 15 numbered rules in the form: "When [situation], do [mechanic] around [timing or frequency]." Each rule must work for a different topic and must contain no content from this video.

11. DO-NOT-COPY LIST
List the elements that are this creator's own protected expression or identity: catchphrases, recurring characters, signature jokes, named segments, sound stings, specific stories and examples, specific footage, music, logos. One line each, described rather than quoted.

12. FIT TO MY CHANNEL
For my niche [NICHE], mark each rule from section 10 as TRANSFERS, ADAPT (say how), or DOES NOT TRANSFER (say why, for example it depends on this creator's access, fame, or personality). 

END WITH "CONFIDENCE AND GAPS": a list of what you could not determine and what extra evidence would settle it.
```

**Expected output:** Twelve sections, mostly tables, 1,500 to 2,500 words, with timestamps that match the video within a few seconds and a final list of 10 to 15 rules.

**If the output is weak:** (a) If it is generic ("uses a strong hook"), reply: "Redo sections 2 to 5 using a table row for every 10 to 20 seconds of transcript, and paraphrase what happens in each row." (b) If the transcript is too long for the assistant, split it in three equal parts. Run sections 2 to 5 on each part, then ask: "Merge these three partial analyses into one set of sections 2 to 5 with continuous numbering." Run sections 1 and 6 to 12 once on the merged result. (c) If the assistant quotes the transcript, reply: "Rewrite with no quotation longer than 5 words."

## Done when

- [ ] You have a saved `reports/video-dna-<video-id>.md` for each of 3 to 5 videos.
- [ ] Five spot-checked timestamps per video are within 10 seconds of the real video.
- [ ] Every report has a hook formula, an open-loop ledger with a longest gap, and 10 or more transferable rules.
- [ ] No report contains a quotation longer than 5 words from the source video.
- [ ] Each report has a filled do-not-copy list.
- [ ] Rules that repeat across reports are marked for the Style Bible.

## Next

Continue to [02-script-prompt-chain.md](02-script-prompt-chain.md).
