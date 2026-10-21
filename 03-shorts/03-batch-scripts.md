# Batch Short Scripts With Enforced Variety

> **Purpose:** Draft 10 to 30 Short scripts in one planning run so that hook types, structures, topics, lengths and loops rotate and no upload looks templated.  
> **Use when:** You have a [SHORTS_DNA] block and at least 4 topic pillars for the channel.  
> **Time needed:** 60 to 90 minutes for a batch of 10, about 2 hours for 30.  
> **Needs:** Any free AI chat assistant, Google Sheets, the report `reports/shorts-dna-<date>.md`.  
> **Cost:** $0

A batch is a drafting convenience. It does not make mass production acceptable. YouTube's inauthentic content policy covers generic, repetitive, or template-based content with little variation between videos (verified 2026-10-20, `appendices/research-snapshot.md`), and the monetization policy defines repetitious content as a channel where viewers have trouble spotting the difference between videos. Two defenses work together here: the variety rules in this file, and a different proof asset of your own in every Short. Do not generate 30 scripts and publish 30 Shorts in one day. Publishing cadence is set in [../08-monetization/02-30-day-plan.md](../08-monetization/02-30-day-plan.md).

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [WORDS_PER_MINUTE], [STYLE_BIBLE], [SHORTS_DNA], [OWNER_ASSETS], [PAST_HOOKS] (same meaning as in `02-script-prompt-chain.md`).
- [BATCH_SIZE]: a whole number from 10 to 30.
- [TOPIC_PILLARS]: 4 to 8 recurring subtopics of [NICHE], each one line. Example: "rice and grains; pantry staples; leftovers; kitchen tools on a budget; meal planning; food safety and storage".
- [TOPIC_BANK]: optional list of ideas you already have, or the word "none".
- Prompt-specific placeholders: [PHASE] (PLAN or SCRIPTS), [WAVE] (for example "1 to 10"), [PLAN_TABLE] (the approved plan), [BATCH_TO_CHECK].

## Steps

1. **List your pillars and assets.** Write 4 to 8 pillars. Write [OWNER_ASSETS] as concrete things you can film, record, or calculate (your stove, your grocery receipts, your screen). A Short whose proof you cannot produce is not planned, it is wishful.
2. **Make the sheet.** In Google Sheets create a file named `shorts-batch-plan` with four tabs named exactly `Plan`, `Scripts`, `Variety-Check`, and `Publish-Log`. In `Plan` cell A1 paste this header, then use Data > Split text to columns > Comma:

```csv
id,pillar,topic,claim,hook_code,structure_code,loop_code,length_s,delivery,visual_format,proof_asset,status
```

   In `Scripts` A1 paste: `id,hook_line,voiceover,word_count,word_budget,title,description,disclosure_flags,asset_list,status`. In `Publish-Log` A1 paste: `id,short_url,publish_date,hook_code,structure_code,loop_code,length_s,views_total,engaged_views,viewed_vs_swiped_pct,subs_gained,notes`. (Rename `viewed_vs_swiped_pct` to whatever your Studio Analytics Shorts view calls it, VERIFY BEFORE RELYING.)
3. **Run P-SHORT-03 with [PHASE] = PLAN.** Paste the plan table it returns into the `Plan` tab columns A to L (Edit > Paste special > Paste values only, then split on the pipe or tab if needed).
4. **Add the helper formulas to `Plan`.** In N2 paste `=IF(A2="","",IF(H2<=25,"A",IF(H2<=45,"B","C")))` and fill down to row 31. In M3 paste `=IF(A3="","",IF(OR(E3=E2,F3=F2,G3=G2,B3=B2,I3=I2,J3=J2),"REPEAT","ok"))` and fill down to row 31. In O4 paste `=IF(A4="","",IF(AND(N2=N3,N3=N4),"3 IN A ROW","ok"))` and fill down to row 31. Any "REPEAT" or "3 IN A ROW" is a rule break.
5. **Build the `Variety-Check` tab.** In B1 enter `=COUNTA(Plan!A2:A31)` (this is N). Then build these blocks. Type the codes in column A and the formulas in B and C, and fill down.

| Block | Codes in column A | Column B (count) | Column C (verdict) |
|---|---|---|---|
| Hooks, rows 3 to 12 | H1 to H10 | `=COUNTIF(Plan!$E$2:$E$31,A3)` | `=IF(B3>ROUNDUP($B$1/5,0),"TOO MANY","ok")` |
| Hook variety, row 13 | "distinct" | `=SUMPRODUCT(--(B3:B12>0))` | `=IF(B13>=MIN(8,$B$1),"ok","TOO FEW")` |
| Structures, rows 16 to 25 | S1 to S10 | `=COUNTIF(Plan!$F$2:$F$31,A16)` | `=IF(B16>ROUNDUP($B$1/4,0),"TOO MANY","ok")` |
| Structure variety, row 26 | "distinct" | `=SUMPRODUCT(--(B16:B25>0))` | `=IF(B26>=MIN(6,$B$1),"ok","TOO FEW")` |
| Loops, rows 29 to 33 | L1 to L5 | `=COUNTIF(Plan!$G$2:$G$31,A29)` | rows 29 to 32: `=IF(B29>ROUNDUP($B$1/3,0),"TOO MANY","ok")`; row 33 (L5): `=IF(B33>ROUNDUP($B$1/6,0),"TOO MANY","ok")` |
| Loop variety, row 34 | "distinct" | `=SUMPRODUCT(--(B29:B33>0))` | `=IF(B34>=MIN(3,$B$1),"ok","TOO FEW")` |
| Length bands, rows 37 to 39 | A, B, C | `=COUNTIF(Plan!$N$2:$N$31,A37)` | `=IF(B37/$B$1>0.5,"BAND TOO COMMON","ok")` |

6. **Fix the plan** until every verdict reads "ok". Then run P-SHORT-05 on the plan as a second opinion (it catches things the formulas cannot, such as near-identical hook skeletons).
7. **Run P-SHORT-03 with [PHASE] = SCRIPTS** for waves of 10 (for example [WAVE] = "1 to 10", then "11 to 20"). Paste the approved plan as [PLAN_TABLE]. Keep waves at 10 so the chat stays inside its limit and quality does not decay.
8. **Paste results** into the `Scripts` tab. Mark each row `draft`.
9. **Run P-SHORT-05 on the scripts** (paste the full scripts as [BATCH_TO_CHECK]). Apply the fixes it lists.
10. **Run P-SHORT-09 from `02-script-prompt-chain.md` on every script** before you film it. P-SHORT-09 is the fact and safety check and the batch prompt does not replace it. Sensitive topics (health, money, law, children) go through [../05-originality-layer/03-sensitive-topics-and-personas.md](../05-originality-layer/03-sensitive-topics-and-personas.md) first.
11. **Produce each Short individually** following `04-vertical-visuals-and-editing.md`. A batch of scripts becomes a batch of Shorts only after each one has its own filmed proof.

**The 12 variety rules** (this repo's rules, not YouTube numbers; N is the batch size):

| Rule | Requirement |
|---|---|
| R1 Hook codes | Each of H1 to H10 used at most ROUNDUP(N/5) times; never the same code twice in a row; at least MIN(8, N) distinct codes |
| R2 Structures | Each of S1 to S10 at most ROUNDUP(N/4) times; never twice in a row; at least MIN(6, N) distinct |
| R3 Loops | Each loop code at most ROUNDUP(N/3) times; L5 at most ROUNDUP(N/6) times; at least MIN(3, N) distinct; never the same code twice in a row |
| R4 Lengths | Between 15 and 60 seconds; bands A (15 to 25), B (26 to 45), C (46 to 60) all appear when N is 6 or more; no band above 50 percent; no three in a row from one band |
| R5 Pillars | Each Short in exactly one pillar; at least MIN(4, number of pillars) used; none used more than ROUNDUP(N/3) times; never the same pillar twice in a row |
| R6 Spoken hooks | The first word differs within every window of 5 consecutive Shorts; no two hooks share a skeleton ("I tested ___ so you don't have to") |
| R7 Visual format | At least 3 formats; never the same format twice in a row |
| R8 Delivery | Rotate among calm, brisk, deadpan, curious, urgent, warm; never the same twice in a row |
| R9 Proof | Every Short has one claim, one payoff, and one proof asset; no two Shorts reuse the same filmed proof shot |
| R10 Endings | The last-line pattern differs across the batch; a call to action appears in at most one Short in three, and the wording never repeats |
| R11 Titles | No title pattern twice in a row |
| R12 Sensitive | Any health, money, legal, or safety topic is tagged SENSITIVE and uses general, verifiable claims only |

**Worked example** (neutral niche: home cooking on a budget; faceless; N = 10). Pillars: P1 rice and grains, P2 pantry staples, P3 leftovers, P4 kitchen tools on a budget, P5 meal planning, P6 food safety and storage. This plan passes all twelve rules.

| # | Pillar | Topic | Hook | Str | Loop | Sec | Visual format |
|---|---|---|---|---|---|---|---|
| 1 | P1 | Day-old rice fries better than fresh rice | H3 | S4 | L4 | 30 | Overhead hands |
| 2 | P2 | Vegetable-scrap stock, start to finish | H1 | S6 | L2 | 22 | Macro close-up |
| 3 | P6 | Three freezer mistakes that ruin leftovers | H6 | S2 | L1 | 45 | Text card plus footage |
| 4 | P2 | Dried versus canned beans, cost per serving | H2 | S7 | L3 | 55 | Screen recording of calculator |
| 5 | P5 | Cooking for one: freeze single portions | H8 | S1 | L4 | 28 | Fridge point of view |
| 6 | P4 | One pan doing three jobs | H5 | S6 | L2 | 18 | Split screen |
| 7 | P3 | Can stale bread be dinner? | H10 | S3 | L5 | 40 | Overhead hands |
| 8 | P5 | A weekly meal plan, question and answer | H4 | S8 | L1 | 50 | Text card plus footage |
| 9 | P1 | Why rinsing rice matters (my mistake) | H7 | S5 | L3 | 35 | Macro close-up |
| 10 | P6 | Is this leftover still safe? (SENSITIVE) | H9 | S4 | L2 | 24 | Fridge point of view |

Check: hooks all distinct; structures S4 and S6 twice, others once, 8 distinct; loops L2 three times (limit 4); band A has 3, band B has 5 (50 percent, allowed), band C has 2; six pillars used, none more than two.

## Prompts

### P-SHORT-03 — Batch Short Scripts

**Purpose:** First produce a rule-compliant variety plan, then write the scripts in waves.
**Inputs:** [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [WORDS_PER_MINUTE], [BATCH_SIZE], [TOPIC_PILLARS], [TOPIC_BANK], [STYLE_BIBLE], [SHORTS_DNA], [OWNER_ASSETS], [PAST_HOOKS], [PHASE], [WAVE], [PLAN_TABLE].

```
You are a short-form scriptwriter and content planner for the YouTube channel [CHANNEL_NAME] in the niche [NICHE]. Audience: [AUDIENCE]. Language: [LANGUAGE]. The channel is [FACE_OR_FACELESS]; voice mode is [VOICE_MODE]. Speaking speed: [WORDS_PER_MINUTE] words per minute.

Batch size N = [BATCH_SIZE]. Topic pillars: [TOPIC_PILLARS]. Existing ideas: [TOPIC_BANK].
Style rules (style family only, never any real creator's words): [SHORTS_DNA]
Brand context: [STYLE_BIBLE]
What I can film or show myself: [OWNER_ASSETS]
Hooks used recently (avoid their patterns): [PAST_HOOKS]

CODES
Hook: H1 result first, H2 open question, H3 bold or contrarian claim, H4 mid-action cold open, H5 number or list promise, H6 mistake or warning, H7 visual oddity or pattern break, H8 direct address to a specific viewer, H9 story already in progress, H10 challenge or constraint.
Structure: S1 single tip, S2 countdown or list, S3 before and after reveal, S4 myth versus fact, S5 mini story, S6 step-by-step demo, S7 A versus B comparison, S8 question and answer, S9 rapid fire, S10 case study or teardown.
Loop: L1 visual match, L2 sentence wrap, L3 callback, L4 question ending, L5 hard end.
Length bands: A 15 to 25 seconds, B 26 to 45, C 46 to 60.

VARIETY RULES (all mandatory)
R1 Each hook code used at most ROUNDUP(N/5) times, never the same code twice in a row, at least MIN(8,N) distinct codes.
R2 Each structure at most ROUNDUP(N/4) times, never twice in a row, at least MIN(6,N) distinct.
R3 Each loop code at most ROUNDUP(N/3) times, L5 at most ROUNDUP(N/6), at least MIN(3,N) distinct, never the same twice in a row.
R4 Lengths between 15 and 60 seconds; if N is 6 or more all three bands appear; no band above 50 percent; no three in a row from one band.
R5 Each Short in exactly one pillar; at least MIN(4, number of pillars) pillars used; no pillar more than ROUNDUP(N/3) times; never the same pillar twice in a row.
R6 The first spoken word differs within every window of 5 consecutive Shorts; no two hooks share a skeleton.
R7 At least 3 visual formats, never the same twice in a row.
R8 Delivery rotates among calm, brisk, deadpan, curious, urgent, warm, never the same twice in a row.
R9 Each Short has one claim, one payoff, and one proof asset I can create from my assets. No two Shorts use the same filmed proof shot.
R10 Last-line patterns differ across the batch. At most one Short in three has a call to action and no wording repeats.
R11 No title pattern twice in a row.
R12 Health, money, legal, and safety topics are tagged SENSITIVE and use general, verifiable claims only.
Also: everything is original. Never reproduce any real creator's phrases, catchphrases, characters, or structures. Never invent statistics, sources, quotes, or quantities; mark any number or safety claim [CHECK]. No bait that is not paid off. No sponsor, affiliate, or product claims.

PHASE: [PHASE]

IF PHASE IS PLAN:
Output one table with N rows and the columns: id | pillar | topic | claim (one sentence) | hook_code | structure_code | loop_code | length_s | delivery | visual_format | proof_asset | status (write "planned"). Fill the table in this order: choose topics first, then assign codes so all rules hold. After the table, print a RULE AUDIT: for each of R1 to R12 write PASS or FAIL with the counts used. If any rule fails, fix the table and print it again before you stop. Do not write scripts in this phase.

IF PHASE IS SCRIPTS:
Write scripts only for Shorts [WAVE] of this approved plan, keeping every code, length, delivery, visual format, and proof asset exactly as planned:
[PLAN_TABLE]
For each Short output: 
1. Header: id | pillar | hook_code | structure_code | loop_code | length_s | delivery | visual_format.
2. Word budget = length_s / 60 x [WORDS_PER_MINUTE] x 0.9, rounded down. Never exceed it.
3. Hook line (spoken), first-frame picture, on-screen text (6 words or fewer).
4. Full voiceover with its word count.
5. Beat table with columns Time | Picture | Voice | On-screen text | Sound. Rows must cover every second from 0 to length_s with no gaps; first beats are one second each, later beats 2 to 5 seconds.
6. Loop: exact last line, exact first line, and the sentence they form together. The Short must feel complete without the loop.
7. One title of 60 characters or fewer and a 2-sentence description.
8. Disclosure flags: DISCLOSE for any realistic synthetic person, voice, or scene; NOT NEEDED otherwise.
9. Asset list and the proof shot.
After the last script print a WAVE AUDIT that re-checks R1 to R12 for the whole plan and for this wave, and list every sentence that is longer than 22 words.
Stop after the wave. Wait for me to say "continue".
```

**Expected output:** PLAN returns one table and a rule audit. SCRIPTS returns up to 10 complete scripts with beat tables and a wave audit.
**If the output is weak:** If the plan fails rules, reply: "Your audit shows FAIL on R__. Fix only the rows that cause it, keep the others unchanged, and reprint the table." If scripts sound alike, reply: "Rewrite scripts __ and __ with a different first picture, a different opening word, and a different sentence rhythm, keeping every code unchanged."

### P-SHORT-05 — Variety Checker

**Purpose:** Independently audit a plan or a set of scripts for template smell.
**Inputs:** [BATCH_TO_CHECK] (the plan table or the full scripts), [BATCH_SIZE], [SHORTS_DNA].

```
You are a strict reviewer who protects a YouTube channel from looking templated or mass-produced. Review the batch below. Batch size N = [BATCH_SIZE]. The channel's style rules are: [SHORTS_DNA]

BATCH:
[BATCH_TO_CHECK]

Run these checks and report each as PASS or FAIL with evidence (ids and counts):
1. Hook codes: each at most ROUNDUP(N/5), never consecutive repeats, at least MIN(8,N) distinct.
2. Structures: each at most ROUNDUP(N/4), never consecutive repeats, at least MIN(6,N) distinct.
3. Loops: each at most ROUNDUP(N/3), L5 at most ROUNDUP(N/6), at least MIN(3,N) distinct, no consecutive repeats.
4. Lengths and bands (A 15 to 25, B 26 to 45, C 46 to 60): all bands present when N is 6 or more, none above 50 percent, no three in a row from one band.
5. Pillars: at least MIN(4, pillars available) used, none above ROUNDUP(N/3), no consecutive repeats.
6. First spoken words: no repeated first word inside any window of 5 consecutive Shorts.
7. Hook skeletons: replace the topic nouns in every hook with blanks and list any two hooks that now read the same.
8. Swap test: pick 3 Shorts at random and swap their topics; would a viewer notice the Short changed? If not, list them as TEMPLATE.
9. Endings: list the last line of each Short and flag duplicates in pattern or wording. Flag more than one call to action in three.
10. Proof: list each Short's proof asset and flag any two that reuse the same filmed shot.
11. Claims: list every number, safety, health, money, or legal claim and mark [CHECK] where missing.
12. Bait: flag any Short whose ending does not deliver what its opening promised.

Then output: (a) a table of FAIL items with the exact fix for each, (b) the ids that need a rewrite, with a one-line instruction per id, (c) one verdict word GO, FIX, or STOP, where GO means no FAIL, FIX means 1 to 3 FAILs that can be repaired without changing more than 3 Shorts, and STOP means anything else.
Do not praise. Do not rewrite the whole batch.
```

**Expected output:** Twelve PASS or FAIL lines, a fix table, a rewrite list, and a verdict.
**If the output is weak:** If every check says PASS without evidence, reply: "Show the counts and ids behind each PASS."

## Done when

- `Variety-Check` shows "ok" for every hook, structure, loop and band row, and `Plan` has no "REPEAT" or "3 IN A ROW".
- P-SHORT-05 returned GO on the plan and again on the scripts.
- Every script has a word count at or under its budget and a beat table with no time gaps.
- P-SHORT-09 returned GO for each Short you intend to film.
- Every Short names a proof asset you can really produce, and no two share a filmed shot.
- You have a written publishing cadence from the 30-day plan, and it is not "all at once".

## Next

Continue to [04-vertical-visuals-and-editing.md](04-vertical-visuals-and-editing.md).
