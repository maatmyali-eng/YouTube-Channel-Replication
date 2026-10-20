# Repurposing Long-Form Into Shorts Without Reuse

> **Purpose:** Turn your own long videos into new Shorts that pass a difference test, so they are not treated as reused, repetitious, or templated content.
> **Use when:** You have published or finished a long video for [CHANNEL_NAME] and want Shorts from the same research, footage, or ideas.
> **Time needed:** 30 to 45 minutes per Short, plus the difference test.
> **Needs:** The transcript and visuals list of your own long video, a free AI chat assistant, Python (optional, for the overlap check).
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [WORDS_PER_MINUTE], [SHORTS_DNA], [OWNER_ASSETS], [PAST_HOOKS] as in earlier files.
- [TRANSCRIPT]: the transcript of YOUR OWN long video, saved as `transcripts-private/<your-video-id>.txt`. Never the transcript of the channel you model at [CHANNEL_URL]. Cutting Shorts from another creator's video is reuse by definition, and nothing in this file makes it acceptable.
- [LONG_VIDEO_TITLE]: the title of your long video.
- [LONG_VIDEO_VISUALS]: a short list of the shots and graphics the long video used, so the Short can use new ones.
- [SHORT_COUNT]: how many Shorts to extract (1 to 3, see the cap in Step 4).
- Prompt-specific placeholders: [SHORT_SCRIPT_TABLE], [SHORT_VISUAL_PLAN], [OVERLAP_RESULT].

## Steps

1. **Know the policies you are working under.** Facts, each checked on 2026-10-20:

| Policy fact | Source and status |
|---|---|
| Reused content means repurposing content already on YouTube or another online source without significant original commentary, substantive modifications, or educational or entertainment value. The policy applies to the channel as a whole, and reused content is allowed if viewers can tell there is a meaningful difference between the original and your video. | YouTube Help, channel monetization policies (verified 2026-10-20). |
| Inauthentic content covers repetitive or mass-produced content. The July 2025 update renamed "repetitious content" to "inauthentic content" and left the reused content policy unchanged. The 16 July 2026 clarification names generic, repetitive, or template-based content as a category. | YouTube Help and `appendices/research-snapshot.md` (verified 2026-10-20). |
| Shorts views are ineligible for Shorts ad revenue when the Short is non-original, such as unedited clips from others' movies or TV, re-uploads of other creators' content, or compilations with no original content added. | YouTube Help, Shorts monetization policies (verified 2026-10-20). |
| YouTube's recommendation system was reported to favor original work over re-uploads of other creators' clips. Coverage says it does not spell out what happens to Shorts that a creator makes from their own long videos, so treat that case as unconfirmed, not exempt. | tbreak.com report, date not confirmed. VERIFY BEFORE RELYING on YouTube's own announcement. |

   The practical reading: a Short cut straight from your long video is the same video in a smaller frame. Viewers cannot tell a meaningful difference, so it carries risk. A new Short that uses your research and your skills but is written, shot, and edited fresh is a different video.

2. **Pick moments by the ledger.** Open the original-value ledger you made for the long video (see [../02-long-form/02-script-prompt-chain.md](../02-long-form/02-script-prompt-chain.md); it lists the demos, data, and experiences only you supplied). Each ledger item is a candidate Short. Choose items that stand alone: one claim and one payoff that make sense to someone who never saw the long video.

3. **Do not use auto-clipping tools to make the final Short.** Tools that cut a long video into captioned vertical clips produce straight crops. A straight crop fails difference points D2 and D3 below by design. Use such tools only to find candidate moments, never to export the Short. Their free tiers usually add watermarks or limit exports (VERIFY BEFORE RELYING on each tool's current terms).

4. **Apply the repo caps** (this repo's rules, not YouTube numbers):
   - At most 3 Shorts from one long video, each with a different claim and a different hook code.
   - Publish them on different days, at least 2 days apart.
   - Never publish a Short on a subject you have already covered in another Short on the same channel with the same claim.

5. **Run P-SHORT-04** with your inputs. It returns, per Short, a new hook, a new script, a new visual plan with every shot marked NEW or REFRAMED, and a self-test.

6. **Produce the Short from the visual plan** using `04-vertical-visuals-and-editing.md`. Film the NEW shots fresh. For any REFRAMED shot (footage reused from the long video), re-crop to vertical, change the angle or speed, and cut it to the Short's own rhythm.

7. **Run the overlap check.** Save the Short's spoken script as `shorts/<slug>/voiceover.txt` and save this as `overlap_check.py`:

```python
import re, sys

def words(t):
    return re.findall(r"[a-z0-9']+", t.lower())

def grams(w, n=5):
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}

long_t = open(sys.argv[1], encoding="utf-8").read()
short_t = open(sys.argv[2], encoding="utf-8").read()
sg = grams(words(short_t))
lg = grams(words(long_t))
if not sg:
    print("Short is too short for the 5-word check")
    sys.exit()
shared = sg & lg
pct = 100 * len(shared) / len(sg)
print(f"Short 5-word sequences: {len(sg)}")
print(f"Shared with the long video: {len(shared)} ({pct:.1f}%)")
for g in sorted(shared)[:20]:
    print(" ".join(g))
print("PASS" if pct <= 25 else "FAIL: rewrite the lines above")
```

   Run it in a terminal: `python overlap_check.py transcripts-private/<your-video-id>.txt shorts/<slug>/voiceover.txt`. Paste the printout into [OVERLAP_RESULT].

8. **Run P-SHORT-10** (the difference test audit). It must return PASS on all five points. Then continue to the gate in `06-prepublish-gate.md`.

**What must change.** Every item in the left column must be true of the Short. This is the whole policy of this file.

| Element | Long video | The Short must be |
|---|---|---|
| Opening | Long video's intro | A new hook with its own first frame and its own first sentence |
| Words | Long video's script | Newly written; no more than 25 percent of the Short's 5-word sequences appear in the long transcript |
| Pictures | Long video's footage | At least half of the seconds are new footage, new angle, or new graphics |
| Value | Part of a larger story | Complete alone: one claim, one payoff |
| Packaging | Long title, thumbnail, description | New title, new on-screen text, new description, its own loop |

**The five-point difference test.** All five must pass.

| Point | Test | Pass condition |
|---|---|---|
| D1 New hook | Put the Short's first second next to the long video's opening. | Different first frame, different first sentence, different hook code from the long video's hook |
| D2 New script | Run `overlap_check.py`. | 25 percent or less of 5-word sequences shared, and no more than 2 consecutive sentences carried over unchanged |
| D3 New picture | Count seconds by source in the beat table. | At least 50 percent NEW footage or graphics; every REFRAMED shot re-cut at the Short's own rhythm; no straight crop of the long video |
| D4 Stand-alone value | Show the Short to someone who never saw the long video. | They can state the claim and the payoff in one sentence each. The Short is not a trailer and does not end on "watch the full video" |
| D5 New packaging | Compare titles, descriptions, and on-screen text. | Different title wording, a different description, different caption template or text, and a different loop pair |

**Examples of safe versus risky** (neutral niche: home cooking on a budget). The long video is "I cooked for $5 a day for a week".

| Short | Verdict | Why |
|---|---|---|
| A fresh 30-second demo of the one trick that saved the most money, filmed again from a new angle, new script, new hook | Safe | Passes D1 to D5; the long video is the research, the Short is a new piece |
| A calculation Short: you show your receipts on screen and add up what one ingredient cost across the week | Safe | New visuals (your receipts), new script, one claim |
| A Short about the mistake you made while filming the long video, told as a mini story | Safe | New content that exists only in the Short |
| An answer to a viewer comment from the long video, filmed new | Safe | New footage, new script; the long video is the context, not the content |
| A 60-second automatic crop of the best moment from the long video with captions added | Risky | Fails D1, D2, D3 and D4; viewers see the same video smaller |
| The same script read faster over new stock footage | Risky | Fails D2; the words are the same |
| Ten Shorts from one long video, all in the same caption template and all ending "full video in the description" | Risky | Violates the cap of 3, fails D4 and D5, and reads as a template |
| Highlight compilation of five old videos with no new commentary | Risky | A compilation with no original content added is listed as non-original in Shorts monetization policies |
| Any clip, audio, or script from the modelled channel at [CHANNEL_URL] | Stop | Another creator's expression; never allowed |

## Prompts

### P-SHORT-04 — Repurpose Long-Form Into Original Shorts

**Purpose:** Extract up to 3 stand-alone, new Shorts from your own long video, each built to pass the difference test.
**Inputs:** [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [WORDS_PER_MINUTE], [SHORTS_DNA], [OWNER_ASSETS], [PAST_HOOKS], [LONG_VIDEO_TITLE], [TRANSCRIPT], [LONG_VIDEO_VISUALS], [SHORT_COUNT].

```
You are a short-form editor and scriptwriter for the YouTube channel [CHANNEL_NAME] in the niche [NICHE]. Audience: [AUDIENCE]. Language: [LANGUAGE]. The channel is [FACE_OR_FACELESS]; voice mode: [VOICE_MODE]. Speaking speed: [WORDS_PER_MINUTE] words per minute.

I will give you the transcript of MY OWN long video titled "[LONG_VIDEO_TITLE]". Create [SHORT_COUNT] new Shorts (maximum 3) from its ideas. Each must be a NEW video, not an excerpt, not a summary, and not a trailer. The goal is that a viewer can tell a meaningful difference between the Short and the long video.

Style rules for Shorts on this channel (style family only): [SHORTS_DNA]
What I can film or show myself: [OWNER_ASSETS]
Visuals already used in the long video: [LONG_VIDEO_VISUALS]
Hooks I used recently: [PAST_HOOKS]

TRANSCRIPT OF MY LONG VIDEO:
[TRANSCRIPT]

HARD RULES
1. Each Short stands alone: one claim and one payoff that make sense to someone who never saw the long video. No "in my last video", no "full video in the description" as the ending.
2. Write all words fresh. Never repeat 5 or more consecutive words from the transcript. Never carry over a sentence.
3. Use a different hook code from the long video's opening and from each other Short in this set (codes H1 result first, H2 open question, H3 bold claim, H4 mid-action cold open, H5 number promise, H6 mistake warning, H7 visual oddity, H8 direct address, H9 story in progress, H10 challenge). Use a different structure code for each Short (S1 single tip, S2 list, S3 before and after, S4 myth versus fact, S5 mini story, S6 step-by-step demo, S7 comparison, S8 question and answer, S9 rapid fire, S10 case study).
4. At least 50 percent of the seconds must be NEW footage, a new angle, or new graphics I can make from my assets. Mark every beat NEW, REFRAMED (long-video footage re-cropped and re-cut), or TEXT CARD. Do not propose any footage from another creator, a film, a TV show, or a real person's likeness.
5. Length 15 to 60 seconds. Word budget = length / 60 x [WORDS_PER_MINUTE] x 0.9, rounded down. Never exceed it.
6. Every number, safety claim, health claim, price, or money claim is marked [CHECK]. Never invent facts that are not in my transcript or common knowledge, and say so when a fact comes from my transcript.
7. Include one loop (L1 visual match, L2 sentence wrap, L3 callback, or L4 question ending) that makes the Short feel complete without the loop. No bait that is not paid off.

OUTPUT for each Short
A. Source moment: describe in your own words which idea of the long video this comes from. Do not quote it.
B. Stand-alone claim and payoff (one sentence each).
C. Hook: spoken line, first-frame picture, on-screen text (6 words or fewer), hook code.
D. Structure code and length in seconds.
E. Full voiceover with its word count and the budget.
F. Beat table covering every second: Time | Picture | Voice | On-screen text | Sound | Source (NEW, REFRAMED, or TEXT CARD).
G. Loop: last line, first line, the sentence they form together.
H. Title of 60 characters or fewer that does not repeat the long video's title, and a new 2-sentence description.
I. Difference self-test with evidence for each: D1 new hook, D2 new script (list any sentence that might overlap the transcript), D3 new picture (share of NEW seconds as a percentage with the arithmetic), D4 stand-alone value, D5 new packaging.
J. Disclosure flags for any realistic synthetic element (DISCLOSE or NOT NEEDED).

After all Shorts print a cross-check: confirm the hook codes and structure codes are all different, the claims are all different, and no Short depends on another.
```

**Expected output:** For each Short a complete package (A to J) and a cross-check.
**If the output is weak:** If a script echoes the transcript, reply: "Rewrite Short __ from scratch using only the claim and the proof idea, not the transcript wording." If more than half the beats are REFRAMED, reply: "Replace REFRAMED beats with NEW shots I can film from my assets until NEW is at least 50 percent of the seconds."

### P-SHORT-10 — Difference Test Audit

**Purpose:** Score a finished Short script and plan against the five-point difference test before you produce or publish it.
**Inputs:** [TRANSCRIPT] (your own long video), [SHORT_SCRIPT_TABLE], [SHORT_VISUAL_PLAN], [OVERLAP_RESULT] (printout of `overlap_check.py`).

```
You are a strict policy-minded reviewer. Compare a new YouTube Short to the creator's own long video and decide whether a viewer can tell a meaningful difference. Use only the material below.

LONG VIDEO TRANSCRIPT: [TRANSCRIPT]
SHORT SCRIPT AND BEAT TABLE: [SHORT_SCRIPT_TABLE]
SHORT VISUAL PLAN (each shot with source NEW, REFRAMED, or TEXT CARD): [SHORT_VISUAL_PLAN]
OVERLAP CHECK PRINTOUT: [OVERLAP_RESULT]

Score each point PASS or FAIL with evidence:
D1 New hook: first frame and first sentence differ from the long video's opening, and the hook code differs.
D2 New script: overlap at or below 25 percent of 5-word sequences, and no more than 2 consecutive sentences carried over unchanged.
D3 New picture: at least 50 percent of seconds are NEW or TEXT CARD material; no straight crop; REFRAMED shots are re-cut at the Short's own rhythm. Show the arithmetic in seconds.
D4 Stand-alone value: a viewer who never saw the long video can state the claim and payoff; the Short is not a trailer and does not end on a pointer to the long video.
D5 New packaging: title, description, on-screen text, and loop differ from the long video's.

Then list every sentence or shot you would change, with a one-line fix. End with one verdict word: PASS (all five pass), FIX (one or two points fail and the fix is small), or STOP (three or more fail, or the Short is a straight crop of the long video). Do not praise.
```

**Expected output:** Five scored points, a change list, and a verdict.
**If the output is weak:** If it passes D3 without arithmetic, reply: "Show the seconds per source and compute the NEW share."

## Done when

- Every Short comes from your own long video, never from the modelled channel.
- You made 3 Shorts or fewer from this long video, with different claims, hook codes, and structures, scheduled at least 2 days apart.
- `overlap_check.py` printed PASS (25 percent or less shared) for each Short.
- P-SHORT-10 returned PASS for each Short.
- At least half of each Short's seconds are new footage, a new angle, or new graphics, and no Short is a straight crop.
- Each Short is complete on its own and does not end on a pointer to the long video.

## Next

Continue to [06-prepublish-gate.md](06-prepublish-gate.md).
