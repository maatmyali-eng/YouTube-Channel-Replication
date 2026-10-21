# Shorts DNA Analysis

> **Purpose:** Turn any channel's Shorts into measurable style rules (hook, pacing, on-screen text, captions, sound, loop) without copying a word.  
> **Use when:** Before you write the first Short for [CHANNEL_NAME], and again whenever the modelled channel changes its Shorts format.  
> **Time needed:** 90 to 120 minutes for 8 Shorts.  
> **Needs:** A browser, Google Sheets, and any free AI chat assistant.  
> **Cost:** $0  

Shorts are a separate system from long-form. A long video earns attention across minutes and is judged mostly by click and watch time. A Short is shown to a viewer who is already swiping, so the first second, the loop, and the length decide almost everything. Do not reuse your long-form analysis here. Run this one.

## Inputs

- [CHANNEL_URL] is the channel you are modelling. [CHANNEL_NAME] is your own channel.
- [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE] from `00-start-here/01-setup-card.md`.
- [STYLE_BIBLE] if you finished `01-channel-dna/03-style-bible-template.md`. It is optional here. The Shorts analysis adds a layer on top of it.
- A sample of 8 Shorts from [CHANNEL_URL] (Step 3).
- Prompt-specific placeholders, defined in P-SHORT-01: [RUN_MODE], [SHORTS_BATCH], [CARDS_SO_FAR].

## Steps

1. **Read the current platform facts once.** They shape every planning choice below.

| Fact | Current statement | Status |
|---|---|---|
| What counts as a Short | A square or vertical video of 3 minutes or less, uploaded on or after 15 October 2024, is classified as a Short. A vertical video over 3:00 is a regular video. | (verified 2026-10-20) from several 2026 guides that cite YouTube Help. Confirm on the YouTube Help page "YouTube Shorts". |
| Minimum length | No practical minimum. Sources disagree (1 second, 15 seconds). | VERIFY BEFORE RELYING. This repo plans every Short at 15 seconds or longer so the question never matters. |
| View counting | Since 31 March 2025 a Shorts view is counted each time the Short starts or replays, with no minimum watch time. The older measure is now called "engaged views" and sits in YouTube Analytics, Advanced mode. YouTube said earnings and Partner Program eligibility stay tied to engaged views. | (verified 2026-10-20) TechCrunch, 26 March 2025. |
| Claimed music in long Shorts | A Short longer than 1 minute that contains claimed content is blocked and is not eligible for monetization. | (verified 2026-10-20) YouTube "Shorts monetization policies" text. |
| Where Shorts money comes from | Shorts ad revenue comes from the Shorts feed and is separate from long-form watch-page revenue. Only partners who accepted the Shorts Monetization Module earn it. | (verified 2026-10-20) same YouTube page. |
| Reused and inauthentic content | Reused content (clips, compilations, reactions without real added value) and inauthentic content (mass-produced, repetitive) are both monetization policies and apply to the channel as a whole. | (verified 2026-10-20) YouTube channel monetization policies page and the 16 July 2026 clarification in `appendices/research-snapshot.md`. |

2. **Create the working files.** In your repo folder create `transcripts-private/` (it already exists if you did long-form), `reports/`, and a Google Sheet named `shorts-watch-log`. Paste this header into cell A1 using Edit > Paste special > Paste values only, then use Data > Split text to columns > Comma:

```csv
short_id,url,date_shown,views_shown,likes_shown,comments_shown,length_s,hook_code,structure_code,loop_code,cuts_total,spoken_words,on_screen_text_words,caption_style,music_present,voice_type,original_value_element,notes
```

3. **Pick 8 Shorts.** Open [CHANNEL_URL], click the Shorts tab, and use the sort chips (Latest, Popular, Oldest; chip names can change, VERIFY BEFORE RELYING). Choose 4 from Popular, 2 from the newest, and 2 from the newest that have the fewest views. The low performers matter because they show which patterns the channel itself abandoned. Log each Short's ID, date, views, likes, and comments exactly as shown on the page.

4. **Learn the codes.** P-SHORT-01 and the later Shorts files use these codes.

| Hook codes | Meaning |
|---|---|
| H1 | Result first: the finished outcome is shown or stated in the first second |
| H2 | Open question the viewer wants answered |
| H3 | Bold or contrarian claim |
| H4 | Mid-action cold open, no introduction |
| H5 | Number or list promise ("three things") |
| H6 | Mistake or warning |
| H7 | Visual oddity or pattern break |
| H8 | Direct address to a specific viewer ("if you cook for one") |
| H9 | Story already in progress |
| H10 | Challenge or constraint |

| Structure codes | Meaning |
|---|---|
| S1 | Single tip |
| S2 | Countdown or list |
| S3 | Before and after reveal |
| S4 | Myth versus fact |
| S5 | Mini story |
| S6 | Step-by-step demo |
| S7 | A versus B comparison |
| S8 | Question and answer |
| S9 | Rapid fire |
| S10 | Case study or teardown |

| Loop codes | Meaning |
|---|---|
| L1 | Visual match: the last frame matches the first frame |
| L2 | Sentence wrap: the last words grammatically lead into the first words |
| L3 | Callback: the last line reframes the opening line |
| L4 | Question ending: the last line asks what the first line answers |
| L5 | Hard end: no loop design |

5. **Watch each Short three times.** Do not download, rip, or record any video or audio. Use only the public Short in your browser and take written notes.
   - Pass 1, picture only: mute the player. Count cuts and note what is on screen in each second.
   - Pass 2, sound only: look away from the screen. Note voice, music, sound effects, silence, and where the sound changes.
   - Pass 3, slow: on desktop, change `youtube.com/shorts/ID` in the address bar to `youtube.com/watch?v=ID`. The standard player has speed control (gear icon > Playback speed) and, when paused, the `,` and `.` keys step one frame back and forward (VERIFY BEFORE RELYING). Use this for the first 3 seconds and for the last second.

6. **Fill the log row for each Short.** Count `cuts_total` (every visible change of shot or camera angle). Count `spoken_words` and `on_screen_text_words`. Set `caption_style` to one of: none, phrase, word-by-word, highlighted-word. Set `voice_type` to one of: human, synthetic, none. Write the single thing in the Short that only that creator could have supplied in `original_value_element` (their demo, data, experience, or joke). That field tells you what you must replace with your own material.

7. **Get the words legally.** Open the Short's watch page and check the description area for "Show transcript" (VERIFY BEFORE RELYING, it appears only when captions exist). If it is missing, type the spoken words by hand. A Short of 60 seconds or less takes about 5 minutes. Save each as `transcripts-private/<short-id>.txt`. These files are private study notes. Never publish them and never paste them into your scripts.

8. **Run P-SHORT-01 in CARDS mode** on batches of up to 4 Shorts (two runs for 8). Then run it once in SYNTHESIS mode with all cards pasted. Save the result as `reports/shorts-dna-<yyyy-mm-dd>.md`.

9. **Make the planning decisions** using the length table. These are this repo's planning rules, not YouTube numbers, because YouTube publishes no per-second retention rule.

| Length band | Best for | Planning notes |
|---|---|---|
| 15 to 25 seconds | One tip, one reveal, loop-first designs | Highest chance the viewer reaches the end and the replay. Needs a very tight script. |
| 26 to 45 seconds | The default band for a Short with a hook, one proof, and a payoff | Matches most single-idea Shorts. |
| 46 to 60 seconds | Step-by-step demos, mini stories | Every sentence must earn its place. Stay at 60 seconds or less when you use any non-library music. |
| 61 to 180 seconds | Mini-documentary style, rare for a new channel | Any claimed content blocks the Short, so use only music and sound you own or that is cleared. Treat it as a short long-form video and ask whether it should be a regular upload. |

10. **Write down the feed effect in one sentence for your channel.** Replays count as views, so a well-built loop raises total views. Eligibility and earnings follow engaged views, so a loop that only inflates replays without holding attention does nothing for you. Plan for the viewer who stays, not the viewer who scrolls.

## Prompts

### P-SHORT-01 — Shorts DNA Analysis

**Purpose:** Convert your watch notes into per-Short cards and then into a set of style rules you can reuse.
**Inputs:** [CHANNEL_URL], [NICHE], [AUDIENCE], [LANGUAGE], [RUN_MODE] (write CARDS or SYNTHESIS), [SHORTS_BATCH] (for CARDS: your log rows, pass notes, and transcripts for up to 4 Shorts, separated by a line of `===`), [CARDS_SO_FAR] (for SYNTHESIS: every card from earlier runs), [STYLE_BIBLE] (optional).

```
You are a short-form video analyst. I want to learn the STYLE MECHANICS of the YouTube Shorts on [CHANNEL_URL] in the niche [NICHE] for the audience [AUDIENCE], so I can make completely new, original Shorts in the same style family in [LANGUAGE]. Never reproduce another creator's words, footage, voice, music, characters, or likeness. When you must refer to a spoken line, describe it as a formula with blanks, for example "I tested ___ so you don't have to", and quote no more than 6 consecutive words of the original, only when needed to show a mechanic.

RUN_MODE: [RUN_MODE]

CODES
Hook: H1 result first, H2 open question, H3 bold or contrarian claim, H4 mid-action cold open, H5 number or list promise, H6 mistake or warning, H7 visual oddity or pattern break, H8 direct address to a specific viewer, H9 story already in progress, H10 challenge or constraint.
Structure: S1 single tip, S2 countdown or list, S3 before and after reveal, S4 myth versus fact, S5 mini story, S6 step-by-step demo, S7 A versus B comparison, S8 question and answer, S9 rapid fire, S10 case study or teardown.
Loop: L1 visual match, L2 sentence wrap, L3 callback, L4 question ending, L5 hard end.

IF RUN_MODE IS CARDS:
For every Short in the input below, produce one card with exactly these parts.
1. Header: short_id, length in seconds, views shown, age shown, views per day if age is known (show the arithmetic).
2. Hook (seconds 0 to 1): what is on screen, what is heard, what text appears. Assign one primary hook code and at most one secondary. Write the hook as a formula with blanks.
3. Promise (seconds 1 to 3): what the viewer is led to expect, and whether the Short pays it off.
4. Structure code and a one-line description of the beat order.
5. Per-second table. Rows for seconds 0 to 5 at one second each, then one row per beat until the end. Columns: Time | Picture | Voice or sound | On-screen text | Job (hook, promise, proof, new information, pattern break, payoff, loop). Use only what my notes support. Write "not in notes" where unknown. Do not guess.
6. Pacing numbers: cuts per 10 seconds, spoken words per second, on-screen text words per 10 seconds, and the longest stretch with no visual change.
7. On-screen text spec: position (top, middle, bottom), size (small, medium, large), style, how it enters (cut, pop, typed), and how many words appear at once.
8. Caption style and whether the captions repeat the voice or add new information.
9. Sound: voice type, music presence and mood, sound effects used as punctuation, silence used on purpose, and what the audio does in the last second.
10. Loop: loop code, and exactly how the last second connects to the first second.
11. Original-value element: what the creator supplied that cannot be copied. State what I must replace with my own material.
12. Risk note: anything in this Short I must not reproduce (a catchphrase, a character, a recognizable edit signature, a music cue).

IF RUN_MODE IS SYNTHESIS:
Using every card in CARDS_SO_FAR, produce the following.
A. Frequency table: hook codes, structure codes, and loop codes, with counts, and which codes appear in the top performers versus the weakest.
B. Typical numbers with min, median, max: length, cuts per 10 seconds, spoken words per second, on-screen text words per 10 seconds, time to first new information.
C. Rules for each of: hook, promise, pacing, on-screen text, captions, sound, loop, series structure (recurring formats or titles), and posting rhythm if my notes show dates. Each rule is one sentence and testable by someone who has not seen the channel.
D. What the weakest Shorts did differently from the strongest, stated as observations, not as causes.
E. A "SHORTS_DNA" block of no more than 450 words that I can paste into any later prompt as [SHORTS_DNA]. It must contain the rules, the length band to use, the allowed hook codes, structure codes and loop codes in rank order, and a "Never copy" list.
F. A "Differentiation list" of 8 specific ways my channel can use the same style while being visibly different (subject angle, format twist, visual identity, voice, original demo, data, location, point of view).
G. Three planning implications from this fact set: a Short is square or vertical and up to 3 minutes; views count at start or replay while earnings and Partner Program eligibility follow engaged views; music claims block Shorts longer than 1 minute.

If a [STYLE_BIBLE] is provided, keep the SHORTS_DNA consistent with it and flag any conflict.

[STYLE_BIBLE]
[SHORTS_BATCH]
[CARDS_SO_FAR]
```

**Expected output:** CARDS mode returns one structured card per Short. SYNTHESIS mode returns sections A to G, ending with the SHORTS_DNA block.
**If the output is weak:** If the cards contain invented details, reply: "Remove every detail that is not in my notes and mark it 'not in notes'." If the synthesis is generic, paste the three cards of the strongest Shorts again and say: "Redo section C using only patterns that appear in at least 3 cards."

## Done when

- `shorts-watch-log` has 8 filled rows and every code cell uses an H, S, or L code from Step 4.
- You wrote notes only. You saved no video or audio file from [CHANNEL_URL].
- `reports/shorts-dna-<date>.md` exists with sections A to G.
- The SHORTS_DNA block is 450 words or fewer and contains a "Never copy" list.
- You picked one length band and wrote it at the top of the report.

## Next

Continue to [02-script-prompt-chain.md](02-script-prompt-chain.md).
