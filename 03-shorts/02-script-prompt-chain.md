# Shorts Script Prompt Chain

> **Purpose:** Write one original 15 to 60 second Short with a second-by-second table and a designed loop ending.
> **Use when:** You have a [SHORTS_DNA] block and one idea for one Short.
> **Time needed:** 25 to 40 minutes per Short.
> **Needs:** Any free AI chat assistant, a stopwatch (phone clock), the file `reports/shorts-dna-<date>.md`.
> **Cost:** $0

This chain writes one Short at a time. For 10 to 30 Shorts in one run use `03-batch-scripts.md`. A Short carries one claim and one payoff. If you need two claims, you have two Shorts.

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [HARDWARE] from the setup card.
- [VIDEO_TOPIC]: one sentence naming the single idea of this Short.
- [VIDEO_LENGTH]: the target length in seconds, from 15 to 60 (for a Short, this variable is always seconds).
- [STYLE_BIBLE] and [SHORTS_DNA] (the 450 word block from P-SHORT-01).
- [WORDS_PER_MINUTE]: your measured speaking speed. Read 100 words of any text aloud with a stopwatch. Words per minute = 6000 divided by your seconds. If you use free text-to-speech, time its output once and use that number.
- [OWNER_ASSETS]: what you can show or demonstrate yourself (your kitchen, your screen, your data, your drawings).
- [PAST_HOOKS]: the first lines of your last 10 Shorts, or "none yet".
- Prompt-specific placeholders: [WORD_BUDGET], [CHOSEN_HOOK], [SCRIPT_TABLE], [LOOP_TYPE_REQUEST], [SCRIPT_TO_CHECK].

## Steps

1. **Compute the word budget.** This is a repo rule, not a YouTube number: `[WORD_BUDGET] = [VIDEO_LENGTH] / 60 x [WORDS_PER_MINUTE] x 0.9`. Example: 30 seconds at 160 words per minute gives 30 / 60 x 160 x 0.9 = 72 words. The 0.9 leaves room for pauses and sound effects.
2. **Write the idea card yourself in 3 lines** before you use AI: the claim, the proof you can show with [OWNER_ASSETS], and the payoff. If you cannot name the proof, change the topic. A Short with no proof of your own is the pattern YouTube's inauthentic-content policy targets (generic, repetitive, template-based content with little variation between videos; (verified 2026-10-20)).
3. **Run P-SHORT-02.** Paste your inputs. Read the table top to bottom.
4. **Run P-SHORT-08** to get 5 hook variants and 3 loop endings. Choose one hook and one ending, then paste the chosen pair back into P-SHORT-02 with the instruction "regenerate the table with this hook and this ending". Do not mix lines from different variants by hand without re-running the timing.
5. **Run P-SHORT-09** on the final table. Fix every item marked "Fix".
6. **Do the stopwatch read.** Read the voiceover aloud, once, at natural speed. If it runs over [VIDEO_LENGTH], cut words, not speed. If you use TTS, generate it and compare the audio length with the table.
7. **Check the loop.** Play the finished Short on repeat three times (after production). If you can hear or see the seam as a jolt, rewrite the last line using the loop method below.
8. **Save** the final table as `shorts/<slug>/script.md`. Use a different slug for each Short (for example `2026-10-20-day-old-rice`).
9. **Check disclosure and topic risk.** If your Short uses a synthetic voice, a realistic generated scene, or a cloned or lookalike voice or face, read the disclosure decision table in [../02-long-form/03-voice-and-audio.md](../02-long-form/03-voice-and-audio.md) before publishing. Never clone a real person's voice or likeness. If the topic is health, money, law, or another sensitive area, read [../05-originality-layer/03-sensitive-topics-and-personas.md](../05-originality-layer/03-sensitive-topics-and-personas.md) first.

**The loop-ending method.** A loop makes the Short end into its own beginning so that a replay feels natural. A loop must never be a trick. The last second must deliver what the Short promised. Do these four things in order:

1. Write the first spoken line (the hook) first and keep it fixed.
2. Choose the loop code. L2 sentence wrap: the last words make a grammatical lead-in to the first words ("...and that is exactly why" then "fresh rice ruins fried rice"). L4 question ending: the last line asks the question that the first line answers. L1 visual match: the final shot matches the first shot in framing and position. L3 callback: the last line reframes the hook.
3. Write the last line so the Short already feels complete without the loop. Remove any "watch again" request.
4. Test: say the last line and the first line back to back. If it sounds like one continuous thought, the loop works. If it needs a pause to make sense, rewrite it.

**Worked example** (neutral niche: home cooking on a budget; faceless, own voice, 30 seconds, [WORD_BUDGET] about 72 words). Idea card: claim, day-old rice fries better than fresh rice; proof, own footage of the same pan with both rice types; payoff, the technique.

| Time | Picture | Voice | On-screen text | Sound | Job | Source |
|---|---|---|---|---|---|---|
| 0 to 2 | Overhead pan, spatula pushes a clump of fresh rice | "Fresh rice ruins fried rice." | FRESH RICE = MUSH | Pan sizzle from first frame | Hook (H3) | Own footage |
| 2 to 6 | Close-up of steam rising from wet clumped grains | "Hot grains are full of water, so they clump and steam in the pan." | Water makes it steam, not fry | Sizzle continues | Promise and proof | Own footage |
| 6 to 12 | Hands spread rice on a tray, then a bowl in the fridge | "Cook the rice a day early, spread it out, cool it quickly, and get it in the fridge." | Cook it a day early | Light tap sound as the tray lands | New information | Own footage |
| 12 to 20 | Cold loose grains hit hot oil and brown | "Cold rice loses surface moisture, so each grain separates and browns." | Dry grains brown | Sizzle rises | Proof | Own footage |
| 20 to 26 | Hands break up a clump over the pan | "Break up any clumps with your hands before the rice touches the oil." | Break the clumps first | Sizzle, one soft whoosh at the cut | New information and payoff | Own footage |
| 26 to 30 | Finished fried rice in the pan, slow push-in | "So what turns fried rice into mush?" | (none) | Sound fades into the opening sizzle | Loop (L4) | Own footage |

Word count of the voice column: 61, under the 72-word budget. The last line asks the question that the first line answers, so the replay reads as one thought.

## Prompts

### P-SHORT-02 — Single Short Script and Second-by-Second Table

**Purpose:** Produce a complete script table for one Short of 15 to 60 seconds.
**Inputs:** [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [VIDEO_TOPIC], [VIDEO_LENGTH], [WORD_BUDGET], [STYLE_BIBLE], [SHORTS_DNA], [OWNER_ASSETS], [PAST_HOOKS], [LOOP_TYPE_REQUEST] (optional: L1, L2, L3, or L4).

```
You are a short-form scriptwriter for the YouTube channel [CHANNEL_NAME] in the niche [NICHE]. The audience is [AUDIENCE]. Write in [LANGUAGE]. The channel is [FACE_OR_FACELESS] and the voice mode is [VOICE_MODE].

Write ONE original Short about: [VIDEO_TOPIC]
Target length: [VIDEO_LENGTH] seconds. Voiceover word budget: [WORD_BUDGET] words maximum (never exceed it).

Style rules to follow (the style family, never the words of any real creator):
[SHORTS_DNA]
Longer brand style context:
[STYLE_BIBLE]

What I can show or demonstrate myself:
[OWNER_ASSETS]
Hooks I have used recently (do not repeat their pattern or wording):
[PAST_HOOKS]
Requested loop type (if blank, choose the best): [LOOP_TYPE_REQUEST]

HARD RULES
1. Everything must be original. Do not reuse any phrase, structure, catchphrase, character, or joke from any real creator or show. Use only visuals I can create or show with my own assets, or free assets that I will log with license details.
2. Exactly one claim and one payoff. No second topic.
3. The first second must carry the hook in picture and in sound or text at the same time. The first 3 seconds must make the promise clear.
4. Include one original-value element: something only I can supply from my own assets (demo, data, comparison, calculation, location, experience). State it.
5. Every statement of fact must be one I can verify. Mark any number, quantity, health or safety claim, or price with [CHECK]. Never invent statistics, sources, quotes, or quantities.
6. No deceptive claims, no cliffhanger that is not paid off, no "wait for the end" bait. The last second must deliver what the first seconds promised.
7. No health, finance, or legal advice stated as certain. If the topic touches those areas, say so at the top and keep claims general.
8. No text on screen that reads as an advertisement unless I said it is sponsored.

OUTPUT, in this exact order
1. IDEA CARD: claim, proof, payoff, original-value element (4 lines).
2. HOOK: the spoken hook line, the first-frame picture, the on-screen text, and the hook code (H1 to H10).
3. FULL VOICEOVER: the continuous text, with a word count and an estimated read time at [WORD_BUDGET] words for [VIDEO_LENGTH] seconds.
4. SECOND-BY-SECOND TABLE: columns Time | Picture | Voice | On-screen text (max 6 words per screen) | Sound | Job | Source (own footage, own screen, free asset, AI-generated). Cover every second from 0 to [VIDEO_LENGTH] with no gaps. Seconds 0 to 5 use one row per second or per beat. After that, one row per beat of 2 to 5 seconds. Follow the cut rhythm in the style rules; if they give a range, stay inside it.
5. LOOP: the loop code, the exact last line, the exact first line, and the sentence they form when read back to back. Confirm the Short feels complete without the loop.
6. TITLE AND DESCRIPTION: 3 title options of 60 characters or fewer that use words from the Short's own claim and no misleading promise, and a 2-sentence description in my voice.
7. DISCLOSURE FLAGS: list each AI-made or synthetic element (voice, visuals, music) and whether it is realistic. Write "DISCLOSE" for any realistic synthetic person, voice, or scene, and "NOT NEEDED" otherwise. Add "VERIFY on YouTube Help: Altered or synthetic content" under the list.
8. ASSET LIST: every picture, sound, and music item I must create or source, with where to log its license.
9. SELF-CHECK: confirm word count, claim count (must be 1), and that the last line matches the loop.
```

**Expected output:** An idea card, hook, full voiceover with word count, the second-by-second table covering every second, a loop pair, three titles, disclosure flags, an asset list, and a self-check.
**If the output is weak:** If the voiceover is over budget, reply: "Cut the voiceover to [WORD_BUDGET] words by removing the weakest sentence, keep the hook and loop, and regenerate the table." If the hook feels generic, run P-SHORT-08 and paste the chosen hook back.

### P-SHORT-08 — Hook Variants and Loop Endings

**Purpose:** Get five different hooks and three loop endings for one Short so you choose rather than accept the first draft.
**Inputs:** [VIDEO_TOPIC], [AUDIENCE], [LANGUAGE], [SHORTS_DNA], [PAST_HOOKS], [SCRIPT_TABLE] (the P-SHORT-02 output).

```
You are a short-form hook specialist. Language: [LANGUAGE]. Audience: [AUDIENCE]. Topic of the Short: [VIDEO_TOPIC].

Style rules for this channel:
[SHORTS_DNA]
Hooks used recently (avoid their pattern and wording): [PAST_HOOKS]
Current script and table: [SCRIPT_TABLE]

Task 1: Write 5 hook variants, each using a DIFFERENT hook code from this list: H1 result first, H2 open question, H3 bold or contrarian claim, H4 mid-action cold open, H5 number or list promise, H6 mistake or warning, H7 visual oddity or pattern break, H8 direct address to a specific viewer, H9 story already in progress, H10 challenge or constraint.
For each variant give: hook code, spoken line (12 words or fewer), first-frame picture I can shoot myself, on-screen text (6 words or fewer), and one sentence on why it fits this audience.
Every hook must be true to the Short's content. No bait that the Short does not pay off.

Task 2: Write 3 loop endings for the current script, one each of L2 sentence wrap, L4 question ending, and L3 callback. For each, give the exact last line, then the exact sentence it forms with the chosen hook, and one sentence on whether the Short still feels complete without the loop.

Task 3: Rank the 5 hooks by likely stop-scrolling power for this audience. Give one reason each. State clearly that this is a judgment, not a measurement.
```

**Expected output:** Five hooks with distinct codes, three loop endings, and a ranked list.
**If the output is weak:** If two hooks sound alike, reply: "Replace variants 2 and 4 with hooks that open with a different first word and a different first picture."

### P-SHORT-09 — Fact and Risk Check for One Short

**Purpose:** Catch false claims, unsafe advice, copied phrasing, and policy risks before you produce the Short.
**Inputs:** [SCRIPT_TO_CHECK] (the final table and voiceover), [NICHE], [LANGUAGE].

```
You are a careful fact-checker and YouTube policy reviewer. Review the Short script below. Language: [LANGUAGE]. Niche: [NICHE].

[SCRIPT_TO_CHECK]

Produce a table with one row per issue and the columns: Line | Problem type | Why it matters | Fix.
Problem types: UNVERIFIED FACT, NUMBER TO VERIFY, SAFETY (food, health, money, legal), POSSIBLE COPIED PHRASE OR CATCHPHRASE, DECEPTIVE OR BAIT PHRASING, UNDISCLOSED SPONSOR OR AFFILIATE CUE, SYNTHETIC MEDIA RISK, GENERIC OR TEMPLATE-LIKE PHRASING.
Then answer: (a) Which single sentence is the weakest and why. (b) Does the Short deliver exactly one claim and one payoff? (c) Is the last line a real payoff, not a tease? (d) What would I need to look up before I publish, and in which kind of source (official site, standards body, manufacturer, textbook)? Do not invent sources or links. If a fact cannot be confirmed from general knowledge, write VERIFY BEFORE RELYING.
End with one verdict word: GO, FIX, or STOP, and one sentence of reason.
```

**Expected output:** An issue table, answers (a) to (d), and a verdict.
**If the output is weak:** If it reports no issues on a script that contains numbers or health claims, reply: "List every number, quantity, and safety claim in the script and say what source type would confirm each."

## Done when

- The table covers every second from 0 to [VIDEO_LENGTH] with no gap, and the voiceover is at or under [WORD_BUDGET] words.
- The Short has one claim, one payoff, and one stated original-value element.
- You chose a hook from at least 3 variants and a loop ending from 3 candidates.
- P-SHORT-09 returned GO, or every "Fix" item is resolved.
- Every number and safety claim marked [CHECK] has been verified in an official or authoritative source and you wrote down where.
- The loop sentence (last line plus first line) reads as one thought.
- The file is saved as `shorts/<slug>/script.md`.

## Next

Continue to [03-batch-scripts.md](03-batch-scripts.md).
