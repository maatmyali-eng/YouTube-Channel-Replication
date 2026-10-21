# Script Prompt Chain (Long-Form)

> **Purpose:** Take a video from topic to a fact-checked, original-checked script through seven linked prompts, P-LONG-02 to P-LONG-08.  
> **Use when:** You have a Style Bible and at least one video DNA report, and you are ready to make a video.  
> **Time needed:** 2 to 4 hours for the first video, about 90 minutes once you know the chain.  
> **Needs:** [STYLE_BIBLE], a free AI chat assistant (ideally one with web search for P-LONG-07), a plain-text editor, a folder per video.  
> **Cost:** $0  

The chain is deliberately not one-click. Each prompt produces a file that the next prompt consumes, and a human step sits between them. The human steps are where your original value gets added, and original value is what separates a channel from the "generic, repetitive, or template-based" category that YouTube treats as non-monetizable (clarified 16 July 2026; verified 2026-10-20).

## Inputs

- [STYLE_BIBLE] (see `../01-channel-dna/03-style-bible-template.md`). Paste the sections on voice, script structure, hooks, pacing, and compliance guardrails if the whole document is too long for the assistant.
- [NICHE], [AUDIENCE], [LANGUAGE], [VIDEO_LENGTH], [FACE_OR_FACELESS], [VOICE_MODE], [VIDEO_TOPIC] from the setup card. [VIDEO_TOPIC] can be empty before P-LONG-02.
- The video DNA reports from `01-video-dna-analysis.md`.
- Defined here: [OWNER_ASSETS] (the sheet you fill in step 2), [WORDS_PER_MINUTE], and the placeholders named inside each prompt.

## Steps

1. **Make a folder** named for the video, for example `videos/2026-11-03-budget-rice-meals/`. Save every output below with the number shown: `02-topic.md`, `03-outline.md`, `04-script-v1.md`, `05-hooks.md`, `06-script-v2.md`, `07-factcheck.md`, `08-originality.md`.
2. **Fill the [OWNER_ASSETS] sheet before you prompt anything.** Copy this block into `01-owner-assets.md` and fill every line with true things only. Write "none" where you have nothing. The prompts are built to leave gaps rather than invent.

```
EXPERIENCES I have really had on this topic (what, when, what happened):
TESTS I have run or will run before recording (what I will measure, result if done):
REAL EXAMPLES I can show on screen (my own screen, kitchen, files, receipts, notes):
OPINIONS I hold and the reasons for them:
THINGS I CANNOT show or claim (equipment I lack, expertise I do not have):
SOURCES I trust for facts in this niche (official pages, textbooks, studies):
```

3. **Set the speaking rate.** Record 60 seconds of yourself reading any text aloud (or use the TTS voice you will use, see `03-voice-and-audio.md`). Count the words read. That number is your [WORDS_PER_MINUTE]. If you cannot test yet, use 150.
4. **Compute the word budget** with the table below. Spoken words equal minutes times [WORDS_PER_MINUTE], times 0.9. The 0.9 reserves about 10 percent of runtime for silent visual beats, pauses, and music-only moments.

| Video length | At 130 wpm | At 150 wpm | At 170 wpm |
|---|---|---|---|
| 5 min | 585 | 675 | 765 |
| 8 min | 936 | 1,080 | 1,224 |
| 10 min | 1,170 | 1,350 | 1,530 |
| 12 min | 1,404 | 1,620 | 1,836 |
| 15 min | 1,755 | 2,025 | 2,295 |

   For other lengths: minutes × wpm × 0.9, rounded down.
5. **Apply the original-value rule.** This is this repo's own quality rule, not a YouTube number. An *original-value item* is something a viewer cannot get by reading the top five search results: (a) a first-hand experience, (b) your own test with a measured result, (c) a real example with real data you gathered, (d) your own reasoned opinion or decision rule, (e) an original visual you made that shows something real. Targets: at least 1 item per 2 minutes of runtime, at least 5 per video, at least 1 inside the first 90 seconds, at least 1 in the final third. Every item must be true. If you cannot reach the target, shorten the video; never pad with invented anecdotes. Invented experiences are deceptive and are exactly what the policy is aimed at.
6. **Run the prompts in order in one chat.** If the assistant loses earlier context, re-paste the output files it needs. Review each output yourself before moving on, using the "Check" line under each prompt.
7. **Free-tier room.** Free assistants cap message length and daily use, and limits change: VERIFY BEFORE RELYING on the assistant's own pricing or help page. P-LONG-04 is written to produce one third of the script per message so it fits small limits.
8. After P-LONG-08, continue to `06-prepublish-gate.md` once audio and visuals are done. Voice and visual work happen between script v2 and the gate.

## Prompts

### P-LONG-02 — Topic and Angle Selection

**Purpose:** Produce scored topic candidates and one chosen angle that you can honestly deliver.

**Inputs:** [STYLE_BIBLE], [NICHE], [AUDIENCE], [LANGUAGE], [VIDEO_TOPIC] (optional seed), [OWNER_ASSETS], [PAST_TITLES] (titles of your last 10 videos, or "none").

```
You are a YouTube content strategist for a channel in [NICHE] for [AUDIENCE], written in [LANGUAGE]. The channel follows this Style Bible: [STYLE_BIBLE]

The owner can truthfully offer only what is in this sheet: [OWNER_ASSETS]
Seed idea (may be empty): [VIDEO_TOPIC]
Titles already published: [PAST_TITLES]

TASK
1. Propose 10 video topics that fit the Style Bible and the owner's real assets. For each give: working title (honest, no exaggeration), the viewer problem or desire it serves, the owner asset that supplies original value, and what a viewer already gets from the usual search results for this topic.
2. Score each 1 to 5 on: viewer demand (is this something people look for or would click when browsed), fit with the Style Bible, original-value potential from the owner's assets, ease of production for one person, and risk (sensitive topic, policy or copyright exposure; 5 = low risk). Show the sum.
3. Reject any topic that needs facts or experiences the owner does not have, and any topic that is health, finance, legal or other sensitive advice unless it can be told as clearly sourced education from real experience; name the reason.
4. Choose the best topic. Write the ANGLE: (a) one-sentence promise to the viewer, (b) the viewer it is for, (c) what makes this version different from the usual coverage, in one sentence, (d) the proof the owner will show, (e) three risks and how to avoid each.
5. Output the final block exactly as:
SELECTED_TOPIC: ...
ANGLE: ...
OWNER_PROOF: ...
Do not claim search volumes or competitor numbers; you have no data. Say what the owner should check on YouTube search suggestions before committing.
```

**Expected output:** Ten scored candidates and a final block with SELECTED_TOPIC, ANGLE, and OWNER_PROOF. Feeds P-LONG-03 as [VIDEO_TOPIC] and [ANGLE].

**Check:** Type the chosen topic into YouTube search and note the top five results. If your angle is the same as theirs, ask the assistant for the second-best topic.

**If the output is weak:** Add more detail to [OWNER_ASSETS] (specific tests you can run) and re-run. Generic assets give generic topics.

### P-LONG-03 — Outline and Beat Sheet

**Purpose:** Convert the angle into a timed beat sheet with loops, interrupts, and value items placed on purpose.

**Inputs:** [STYLE_BIBLE], [VIDEO_TOPIC], [ANGLE] (from P-LONG-02), [VIDEO_LENGTH], [WORDS_PER_MINUTE], [OWNER_ASSETS], [DNA_RULES] (the merged transferable rules from your video DNA reports; paste sections 3, 4, 5 and 10 of the best report if you have no merged list).

```
Build the outline for one long-form YouTube video.
Topic: [VIDEO_TOPIC]
Angle: [ANGLE]
Length: [VIDEO_LENGTH]
Speaking rate: [WORDS_PER_MINUTE] words per minute. Spoken word budget = minutes x rate x 0.9.
Style Bible: [STYLE_BIBLE]
Structural rules learned from the modelled channel (mechanics only): [DNA_RULES]
Owner's real assets: [OWNER_ASSETS]

OUTPUT
A. A table of beats covering the full runtime with no gaps: # | Start-End | Beat name | Function | Word budget | What the viewer learns or feels | Visual idea | Source needed (yes/no and what kind).
B. The open-loop plan: each loop, where it opens, where it closes. No loop may stay open longer than the longest gap in [DNA_RULES], and every loop must close inside the video.
C. Pattern-interrupt plan: list planned interrupts with time and type, so the longest stretch without one matches the modelled channel.
D. Original-value ledger: list at least 1 item per 2 minutes (and at least 5), each tagged a to e (experience, test, real example, opinion, original visual), the beat it sits in, and the exact owner asset it uses. If the owner sheet cannot supply an item, write "OWNER TO CREATE: ..." with a concrete task. Never invent an experience.
E. Ending plan and call to action that fit the Style Bible and ask for one thing only.
F. A one-paragraph honesty check: what the title and thumbnail will promise and which beats deliver it.
Use the modelled channel's timing patterns, never its content, wording, or examples.
```

**Expected output:** A beat table, loop plan, interrupt plan, value ledger, ending, and honesty paragraph. Feeds P-LONG-04 as [OUTLINE].

**Check:** Add up the word budgets; the total must be within 5 percent of the budget from the table. Do any "OWNER TO CREATE" tasks exist? Do them now.

**If the output is weak:** Ask: "Rewrite table A with beats no longer than 90 seconds and add one concrete visual for each."

### P-LONG-04 — Full Script

**Purpose:** Write the full spoken script in your voice, one third at a time, with gaps for what only you can supply.

**Inputs:** [STYLE_BIBLE], [OUTLINE] (the P-LONG-03 output), [VIDEO_LENGTH], [LANGUAGE], [WORDS_PER_MINUTE], [OWNER_ASSETS], [FACE_OR_FACELESS], [VOICE_MODE].

```
Write the script for one long-form YouTube video in [LANGUAGE].
Outline: [OUTLINE]
Style Bible: [STYLE_BIBLE]
Owner's real assets: [OWNER_ASSETS]
Presentation: [FACE_OR_FACELESS]; voice: [VOICE_MODE]; length [VIDEO_LENGTH]; rate [WORDS_PER_MINUTE] wpm.

PROCESS: Write only the first third of the beats now, then stop and wait for me to type NEXT. After NEXT write the second third, then after NEXT the final third and the closing tables.

FORMAT for each beat:
[mm:ss-mm:ss] BEAT NAME (word target: N)
VOICE: the exact words to be spoken
SCREEN: what the viewer sees (be concrete and say whether it is the owner's own capture, original graphic, licensed stock, or AI-generated)
SOUND: music or effect cue, or "none"

RULES
1. Write for the ear: spoken contractions, sentences mostly under 20 words, one idea per sentence, numbers written as they are said.
2. Where the outline asks for an experience, test, or example that the owner sheet does not contain, write [OWNER TO ADD: describe exactly what to add]. Never invent experiences, results, quotes, statistics, or people.
3. Every factual statement that a viewer could dispute gets a tag like [CLAIM-07] directly after it. Do not make up sources.
4. Do not copy wording, jokes, or examples from any other creator. Use only the structure and timing rules in the Style Bible.
5. Keep each beat within 10 percent of its word target.
6. No promise in the hook or beats that the video does not pay off.
7. For [VOICE_MODE] using text-to-speech: avoid hard-to-pronounce strings; spell out symbols and units the way they should be spoken, and add a line "PRONUNCIATION:" under any beat that contains a proper noun or unusual word.

AFTER THE FINAL THIRD, OUTPUT
- A table of beat | target words | actual words.
- A list of every [OWNER TO ADD] with its beat.
- A list of every [CLAIM-nn] with the claim in one line.
- The total word count versus the budget.
```

**Expected output:** Three messages of beats in the voice/screen/sound format, then the closing tables. Save the joined text as `04-script-v1.md`.

**Check:** Fill every [OWNER TO ADD] with a true detail before continuing. If one cannot be filled, delete the sentence and shorten the beat.

**If the output is weak:** If it sounds like an essay, reply: "Rewrite beat 3 so every sentence could be said aloud in one breath, with the Style Bible's person, tense, and humor level." If it sounds generic, add one more true detail to [OWNER_ASSETS] and rerun that third.

### P-LONG-05 — Hook Variants

**Purpose:** Generate five honest alternative openings and pick the two best for a trial.

**Inputs:** [STYLE_BIBLE], [ANGLE], [HOOK_V1] (the first 45 seconds of script v1), [DNA_HOOK_FORMULA] (section 2 of your video DNA report), [TITLE_AND_THUMBNAIL_PROMISE] (the working title and one sentence describing the planned thumbnail).

```
Write five alternative hooks, each 20 to 30 seconds spoken, for a video with this angle: [ANGLE]
Current hook: [HOOK_V1]
Mechanic formula observed in the modelled channel (structure only): [DNA_HOOK_FORMULA]
Title and thumbnail promise: [TITLE_AND_THUMBNAIL_PROMISE]
Style Bible: [STYLE_BIBLE]

Each hook must use a different mechanic (for example cold-open result, question with stakes, contrast, live demonstration, brief story-in). For each hook output: the spoken text; the mechanic; the exact promise it makes; the second at which the viewer sees first proof; an honesty rating from 0 (fully delivered in the video) to 2 (promises more than the video gives); one sentence on what is lost compared with the current hook.
Rules: no hook may promise something the outline does not deliver; no fake urgency; no claims you cannot back; do not copy any other creator's wording.
Finish by recommending the best two, and describe how the first 8 seconds of each should look on screen.
```

**Expected output:** Five hooks with the five attributes each, and a top-two recommendation. Choose one, write it into the script as `06-script-v2.md` (the P-LONG-06 prompt will take it).

**Check:** Read the winner aloud and time it. Over 35 seconds, trim it.

**If the output is weak:** Reply: "All five feel similar. Rewrite hooks 3 to 5 using a mechanic not used in hooks 1 and 2."

### P-LONG-06 — Retention Edit

**Purpose:** Tighten the script for pace, interrupts, and closed loops without adding bait.

**Inputs:** [SCRIPT_V1_WITH_NEW_HOOK], [WORDS_PER_MINUTE], [VIDEO_LENGTH], [MAX_GAP_SECONDS] (longest stretch without an interrupt; use your DNA report's value, default 45), [TARGET_CUT_PERCENT] (default 10), [OUTLINE].

```
You are a script editor focused on viewer retention. Edit this script: [SCRIPT_V1_WITH_NEW_HOOK]
Original outline (for loops and value items): [OUTLINE]
Length [VIDEO_LENGTH]; speaking rate [WORDS_PER_MINUTE]; longest allowed stretch without an interrupt [MAX_GAP_SECONDS] seconds; cut about [TARGET_CUT_PERCENT] percent of words unless that would remove an original-value item.

STEP 1: DIAGNOSE. A table: Time | Problem (slow start, repeated point, abstract claim without an example, stretch longer than the allowed gap without an interrupt, loop opened but not closed, filler phrase) | Fix.
STEP 2: REWRITE. Produce the full revised script in the same VOICE / SCREEN / SOUND format. Keep every [CLAIM-nn] tag and every original-value item. Keep [OWNER TO ADD] text if it is still unfilled and flag it. Add interrupts that serve the viewer (a visual change, a question, a demonstration, a change in speed). Do not add fake cliffhangers, teasers that are not paid off, or invented drama.
STEP 3: CHECK TABLE. Loops opened/closed; longest gap between interrupts; words vs budget; original-value items count with their timestamps.
Never add outside facts. If an edit would change the meaning of a claim, leave it and flag it.
```

**Expected output:** Diagnosis table, full revised script, check table. Save as `06-script-v2.md`.

**Check:** The check table must show zero unclosed loops and a longest gap within [MAX_GAP_SECONDS]. If the words are under 85 percent of the budget, the video will run short; record fewer seconds of padding rather than adding filler.

**If the output is weak:** Reply: "You changed claims. Restore the original wording of every sentence containing a CLAIM tag and redo the pacing edits around them."

### P-LONG-07 — Fact-Check

**Purpose:** Verify every checkable claim against primary sources, and rewrite or remove what cannot be verified.

**Inputs:** [SCRIPT_V2], the [CLAIM-nn] list from P-LONG-04, [NICHE]. Use an assistant with web search enabled if you can; availability and free limits vary and change: VERIFY BEFORE RELYING on its own help page.

```
Fact-check this script for a YouTube video in [NICHE]: [SCRIPT_V2]
For every sentence tagged [CLAIM-nn] and for every number, date, price, legal or health statement, comparison ("best", "cheapest", "fastest"), and named person or organization, output a table:
ID | Claim in one line | Type (number, date, price, rule, health, legal, finance, comparison, quote, other) | Verified? (YES with source / PARTLY / NO / CANNOT VERIFY) | Source (publisher, page title, URL, date accessed) | Safe rewrite.
Rules: use only sources you actually retrieved in this chat. If you have no web access, mark every row CANNOT VERIFY and say so on the first line; do not answer from memory. Never invent a URL, study, or statistic. Prefer primary sources (official pages, standards, original studies) over blogs. Mark anything that changes over time with the date it was checked. Rewrite unverifiable claims so they are true without the unverified detail, or recommend deleting them. Flag any health, finance, or legal statement that gives advice, and recommend adding sourced context and a recommendation to consult a qualified professional (see 05-originality-layer/03-sensitive-topics-and-personas.md).
Finish with the corrected script with all rewrites applied, and a list of claims the owner must still confirm manually.
```

**Expected output:** The claim table, a corrected script, and the manual-confirm list. Save as `07-factcheck.md`. Open at least the three most important sources yourself.

**Check:** For each source the assistant lists, click the URL. Delete any claim whose link does not exist or does not say what the table says.

**If the output is weak:** Reply: "List only the claims you could not verify, and why, with no guesses." Then verify those by hand.

### P-LONG-08 — Originality and Similarity Check

**Purpose:** Prove the script does not copy the modelled video and is not a reskin of your own previous scripts.

**Inputs:** [SCRIPT_V3] (script v2 after fact-check), [DNA_REPORT] (the report on the modelled video), [PREVIOUS_OUTLINES] (outlines of your last 3 videos, or "none"), [OWNER_ASSETS]. Also run the local overlap script below before using the prompt.

First, run the local overlap check (Python 3, free). Save as `overlap.py`:

```
import re, sys
def words(path):
    t = open(path, encoding="utf-8").read().lower()
    t = re.sub(r"\d{1,2}:\d{2}(:\d{2})?", " ", t)
    return re.findall(r"[a-z0-9']+", t)
a, b = words(sys.argv[1]), words(sys.argv[2])
n = int(sys.argv[3]) if len(sys.argv) > 3 else 6
grams = lambda w: {tuple(w[i:i+n]) for i in range(len(w) - n + 1)}
shared = sorted(grams(a) & grams(b))
print(len(shared), "shared", n, "word sequences")
for g in shared[:50]:
    print(" ".join(g))
```

Run: `python overlap.py videos/<slug>/06-script-v2.md transcripts-private/<video-id>.txt 6`. Any shared 6-word sequence is rewritten unless it is a common phrase or a proper noun.

```
You are an originality reviewer. Compare my script with the analysis of the video I modelled and with my previous outlines.
My script: [SCRIPT_V3]
Analysis of the modelled video (mechanics, do-not-copy list): [DNA_REPORT]
My previous video outlines: [PREVIOUS_OUTLINES]
My real assets: [OWNER_ASSETS]

OUTPUT
1. SHARED EXPRESSION: any phrase, joke, catchphrase, named segment, or example in my script that matches the do-not-copy list. Quote my line (not theirs) and give a rewrite.
2. STRUCTURE PARITY: map my beats to the modelled video's beats. Count how many correspond one-to-one in order and function. Mechanics may be shared; a beat-for-beat clone with changed nouns may not. Verdict: LOW / MEDIUM / HIGH parity, and which beats to restructure.
3. ORIGINAL VALUE AUDIT: list every original-value item (experience, test, real example, opinion, original visual) with timestamp. Is each backed by my assets? Count them against the rule of 1 per 2 minutes, minimum 5.
4. TEMPLATE RISK: compare the structure, opening pattern, and example types against my previous outlines. If three or more videos share nearly identical structure, topic phrasing, or visuals with little variation, say so and recommend two concrete variations.
5. VERDICT: PASS, REWRITE, or STOP, with a numbered list of required changes. STOP means the script is too close to another creator's expression or has no original value.
Do not be polite for politeness' sake; be specific.
```

**Expected output:** Five sections ending in a verdict. Save as `08-originality.md`.

**Check:** Apply all required changes, then run the overlap script again. For the formal score, run P-ORIG-01 from [the scoring rubric](../05-originality-layer/02-scoring-rubric.md).

**If the output is weak:** Paste only the five highest-risk beats and ask for a stricter parity review of just those.

## Done when

- [ ] `01-owner-assets.md` through `08-originality.md` exist in the video's folder.
- [ ] Script v2 meets the word budget within 10 percent and has the required original-value items, all true.
- [ ] Every [OWNER TO ADD] is filled or the sentence is deleted.
- [ ] Every claim is verified at a source you opened, or rewritten.
- [ ] The overlap script shows no shared 6-word sequence except common phrases and names.
- [ ] P-LONG-08 verdict is PASS.

## Next

Continue to [03-voice-and-audio.md](03-voice-and-audio.md).
