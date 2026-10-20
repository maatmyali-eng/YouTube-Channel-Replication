# Human-in-the-Loop Checkpoints

> Purpose: Define eight checkpoints, C1 to C8, that a person must pass before a video moves on, so that automation never publishes unreviewed content.
> Use when: Always. Every video and every Short passes these gates.
> Time needed: About 2.5 hours of checking per 10-minute long video, 25 to 35 minutes per Short.
> Needs: The `Pipeline` sheet, the video folder, `review-log.md`.
> Cost: $0

## The main risk, stated plainly

Fully automated publishing of unreviewed videos is the main demonetization risk in this repo. YouTube's inauthentic content policy, clarified 16 July 2026, covers three categories that are not monetizable: generic, repetitive, or template-based content with little variation between videos; off-putting or distressing content; and AI personas discussing sensitive topics such as health and finance (verified 2026-10-20). The policy targets mass production, not AI use. AI voiceover can qualify when the video has original commentary, education, or entertainment value, and the separate reused-content policy did not change (verified 2026-10-20). A pipeline that creates, uploads, and publishes without a person reading, listening, and watching is the exact pattern the policy describes. The gates below exist so that a named person has looked at every video before it can go live. No tool in this repo is allowed to pass a gate for you.

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE]
- The status system in `03-bulk-systems.md`
- The folder of the video being checked

## The checkpoint table

Time costs are for a 10-minute long video. Scale the watch and listen times to the real length. The pass criteria and fail actions are this repo's rules, not YouTube's.

| Gate | Stage | Who or what checks | Time cost | Pass criteria | Fail action |
|---|---|---|---|---|---|
| C1 Idea | Ideation | You. An LLM may rank ideas but cannot approve | 10 min | First-hand angle is real and producible this week. At least 3 of the 5 Value Stack layers, one of them first-hand. Topic is not copied from one source video. Not a sensitive-persona topic without qualification | Status stays IDEA. Rewrite the angle, or set KILLED |
| C2 Script | Script | You, reading aloud, plus P-LONG-07 and P-AUTO-09 as aids | 45 min | Every `[OWNER TO ADD]` and `[CHECK]` is resolved. Every factual claim has a primary source in `factcheck.md`. Script differs from the last five in hook type or structure. Contains your own explanation or demonstration | Status stays SCRIPTED. Revise. Two failed rounds means HOLD |
| C3 Voice | Voice | You, listening to the full audio | 20 min | No mispronunciations, no robotic stretches, no cloned real person's voice, voice mode matches the setup card, disclosure decision noted | Re-render or re-record. Do not move to Visuals |
| C4 Visuals | Visuals | You, with `thumbnails/asset-log.csv` | 30 min | Every asset has a source, a licence, and `commercial_ok` filled. No footage, thumbnails, logos, characters, or music taken from another creator. Real people shown only if they are yours or licensed. Nothing distressing without purpose | Replace the asset. Unknown licence means do not use |
| C5 Thumbnail | Thumbnail | You | 10 min | Resemblance audit shows at least 4 of 8 attributes changed versus the source. Text 4 words or fewer. Promise is delivered by the video. No faces of real people you lack rights to | Rebuild. Run P-THUMB-03 again |
| C6 Metadata | Metadata | You | 10 min | Title, description, and chapters match the video. MISMATCH CHECK is empty. No deceptive tags, no other creator's names used for traffic | Edit. Never publish a title the video cannot support |
| C7 Disclosure | Metadata | You | 10 min | Decision recorded in `disclosure.md` against the table in `02-long-form/03-voice-and-audio.md`. Realistic altered or synthetic content set to "Altered or synthetic content" in Studio. Paid promotion declared | Set the Studio toggle, or change the content so it is not realistic synthetic media |
| C8 Final watch | Review | You, once, at normal speed, ideally a day after editing | Video length + 20 min | Rubric P-ORIG-01 scores 80 or more with no hard gate failed. The video is something you would be comfortable defending as original to a reviewer | Fix and re-watch the changed parts. Under 65 or any gate failed means reject |

Total for a 10-minute long video: about 2 hours 35 minutes (10 + 45 + 20 + 30 + 10 + 10 + 10 + 10 + 20 minutes plus the 10-minute watch, which is already counted in C8's video length). For a Short, run C1, C2, C4, C6, C7, and C8 in a compressed form of 25 to 35 minutes.

## What the three policy categories mean for each gate

1. **Generic, repetitive, or template-based.** Checked at C1 (first-hand angle), C2 (P-AUTO-09 sameness check), C4 (visuals not a stock slideshow), C5 (template rotation). A faceless slideshow, stock-footage-plus-text-to-speech, or templated Shorts format is high risk in this repo's reading of the policy. The defense is visible original work: your own test, your own numbers, your own demonstration, and your own explanation.
2. **Off-putting or distressing.** Checked at C2, C4, and C8. Ask whether shock is the purpose of any scene. If it is, cut the scene.
3. **AI personas on sensitive topics, such as health and finance.** Checked at C1. Run P-ORIG-03 in `05-originality-layer/03-sensitive-topics-and-personas.md` and stop if it says to. Do not publish medical or financial advice from an AI voice or a synthetic character.

## Steps

1. For every video, create `review-log.md` in its folder at the moment the row reaches APPROVED. Paste the template below into it.

```
# Review log: [slug]
Reviewer: [your name or initials]

C1 Idea:        date ____  pass/fail ____  note ________________
C2 Script:      date ____  pass/fail ____  note ________________
C3 Voice:       date ____  pass/fail ____  note ________________
C4 Visuals:     date ____  pass/fail ____  note ________________
C5 Thumbnail:   date ____  pass/fail ____  note ________________
C6 Metadata:    date ____  pass/fail ____  note ________________
C7 Disclosure:  date ____  pass/fail ____  note ________________
C8 Final watch: date ____  pass/fail ____  minutes watched ____  rubric score ____
Evidence: one thing I changed because of this gate: ________________
```

2. At each gate, do the check by hand. Write the date, pass or fail, and one concrete note. A gate with an empty note does not count as passed.
3. Run P-AUTO-10 before C2 and C8 to get a checklist of claims and sensitive flags to examine. The prompt output is a list for your attention, not a decision.
4. Change the status in column C only after the gate line is filled. Statuses that carry a gate are written by you and by nothing else (see `03-bulk-systems.md`).
5. Enter your initials in column R of the `Pipeline` sheet only at C8.
6. For C8, watch the entire video once at normal playback speed with sound on, without editing. Pause only to note a timestamp. Skimming at faster speed does not count.
7. Do the C7 disclosure decision with the current YouTube Help wording open. Sources disagree on whether AI voiceover and AI music need a label, so open the YouTube Help article on disclosing altered or synthetic content and quote its present wording into `disclosure.md`. YouTube can also add the label itself, and undisclosed branded content such as sponsorships can be auto-labeled since announcements of 3 September 2026 (verified 2026-10-20). Mark the decision VERIFY BEFORE RELYING until you have read the page that day.
8. If a gate fails, apply the fail action in the table, then repeat only that gate. Do not skip ahead.
9. Once a week, run P-AUTO-11 on the week's review logs to find gates that were passed too quickly.

## Rules that make the gates real

- **No LLM passes a gate.** An LLM may produce a checklist or a score. A person writes pass or fail.
- **No same-session approval.** For C2 and C8, take a break of at least one hour, ideally one night, between finishing the work and approving it.
- **Time floors.** C2 takes at least half the script's reading time to check claims, and C8 takes at least the video's full running time. If your log shows less, the gate did not happen.
- **One failed gate blocks scheduling.** The Schedule stage in Studio is allowed only for rows at REVIEW_PASSED.
- **Never connect the API to publish.** The API route in `07-youtube-api-and-audit.md` ends in human review followed by manual or Studio-scheduled publishing. An unaudited API project created after 28 July 2020 has `videos.insert` uploads locked to private until a compliance audit passes, and the default upload bucket is about 100 `videos.insert` calls per day (verified 2026-10-20). Do not build around the audit to publish unreviewed.
- **Batch does not shorten gates.** Doing six scripts in one sitting means six separate C2 checks. See `03-bulk-systems.md`.

## Prompts

### P-AUTO-10 — Gate Evidence Checklist

Purpose: Produce a checklist of claims, risks, and sensitive flags for you to verify at C2 or C8. It does not decide anything.
Inputs: [CHANNEL_NAME], [NICHE], [LANGUAGE], [GATE] (C2 or C8), [VIDEO_MATERIAL] (the script text for C2, or the script plus final metadata plus your list of assets for C8).

```
You are a compliance reviewer's assistant for the YouTube channel [CHANNEL_NAME] ([NICHE], [LANGUAGE]).
Gate: [GATE]. Material: [VIDEO_MATERIAL]

Do not approve or reject. Produce a checklist for a human to verify:
1. FACTS: every factual claim, number, date, or named source, one per line, with what primary source would confirm it.
2. SENSITIVE: any content touching health, finance, legal advice, safety, children, violence, or distress, one per line, with why it matters.
3. ORIGINALITY: places where the video appears to be generic, repetitive, or template-based, and the first-hand material that exists in the script (list it, or write NONE FOUND).
4. DISCLOSURE: any realistic synthetic or altered media, synthetic voice, or paid promotion, one per line, with a reminder to decide the Studio setting.
5. DECEPTION: any title, description, or thumbnail claim the video does not deliver.
6. LICENCES: every outside asset, sound, image, or clip named in the material, with the licence information still needed.

End with the single most likely reason this video could be flagged as inauthentic content. Do not invent facts or sources. If you cannot tell, write UNKNOWN.
```

Expected output: Six lists and one closing risk line.
If the output is weak: Add the Style Bible and the last five video summaries so the originality section has something to compare against.

### P-AUTO-11 — Weekly Gate Audit

Purpose: Find gates that were passed too fast, too uniformly, or without evidence.
Inputs: [REVIEW_LOG_TEXT] (paste the week's `review-log.md` files), [PIPELINE_ROWS] (columns A, C, Q, R, V from `Pipeline`).

```
You audit a one-person YouTube production log for rubber-stamping.
Review logs: [REVIEW_LOG_TEXT]
Sheet rows: [PIPELINE_ROWS]

Report:
1. Any gate with an empty note, or a note that is generic ("ok", "fine", "looks good").
2. Any video where two or more gates carry the same date and time of day.
3. Any C8 where the minutes watched is less than the video length.
4. Any video where the status in the sheet is ahead of the last passed gate in its log.
5. Any video with no recorded change made because of a gate ("one thing I changed").
6. A rubric score pattern: list videos scoring exactly the pass mark or higher by only a few points.
For each finding give the slug, the gate, and the action: redo the gate, or accept with a reason.
End with a verdict for the week: GATES HELD or GATES SLIPPED. Be strict, and do not soften findings.
```

Expected output: Numbered findings per slug and a weekly verdict.
If the output is weak: Include the timestamps from your file system for the log files and the rendered video so date checks have real data.

## Done when

- [ ] Every video folder has a `review-log.md` with all eight gate lines filled in by a person.
- [ ] No row is at SCHEDULED without a C8 line and a rubric score of 80 or more.
- [ ] Disclosure decisions are written in `disclosure.md` against the current YouTube Help wording.
- [ ] No scenario, script, or API call in your setup can publish, and none can set a gate status.
- [ ] You ran P-AUTO-11 at least once and resolved each finding.
- [ ] You can state in one sentence why unreviewed automated publishing is the main demonetization risk.

## Next

[05-low-code-workflow.md](05-low-code-workflow.md)
