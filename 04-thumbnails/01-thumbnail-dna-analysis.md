# Thumbnail DNA Analysis

> **Purpose:** Turn the thumbnails of [CHANNEL_URL] into a written rule set you can reuse without copying any single image.  
> **Use when:** Before you design any thumbnail for [CHANNEL_NAME].  
> **Time needed:** 45 to 60 minutes for 20 thumbnails.  
> **Needs:** A browser, a spreadsheet (Google Sheets), any free chat AI.  
> **Cost:** $0

## Inputs

- [CHANNEL_URL], [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE]
- [STYLE_BIBLE] from 01-channel-dna/03-style-bible-template.md (optional but useful; the thumbnail must match the channel's tone)
- [THUMB_DESCRIPTIONS]: your written description of 20 thumbnails, built in Steps 1 to 4 below. Defined in P-THUMB-01.

## Steps

1. Open [CHANNEL_URL] in a browser and click the **Videos** tab. Look only at the public page. Do not download video files or use scrapers.
2. Click **Popular** (sort chip). Note the first 10 videos. Then click **Latest** and note the first 10. Ten popular plus ten recent shows what works and what the channel does now.
3. Create a Google Sheet named `thumb-watch-log` with these columns, one row per video: `ID, Video title, Views, Age, Layout, Focal subject, Face (Y/N), Expression, Text words, Text position, Text style, Colors (3 named), Contrast, Background, Emotion trigger, Curiosity gap type, Payoff in video (Y/N), Notes`.
4. For each of the 20 thumbnails, fill the row by looking at the thumbnail at small size. Open the channel page, zoom the browser out to 50 percent, and describe what you can still read. That is how a phone viewer sees it. Use these fixed vocabularies so rows can be compared:
   - **Layout:** single subject centered, subject left plus text right, subject right plus text left, split before/after, grid of items, object with arrow or circle, text-dominant, scene wide shot.
   - **Focal subject:** face, hands holding object, single object, finished result, process step, text only.
   - **Expression** (if a face): neutral, surprise, delight, concern, skepticism, concentration.
   - **Text words:** the number of words. Count them. Zero is allowed.
   - **Text style:** bold sans, condensed sans, handwritten, outlined, boxed label, none.
   - **Contrast:** high (subject separates instantly from background), medium, low.
   - **Emotion trigger:** curiosity, desire, surprise, relief, fear of loss, pride, humor.
   - **Curiosity gap type:** result hidden, number or price, before/after, mistake reveal, comparison, question, none.
5. Do not paste or upload the actual thumbnail images into an image generator at any point. You may paste a screenshot into a chat AI only to have it describe the image for private analysis, and only if you delete that description of any real person's face before you reuse it. The safer route is to write the description yourself.
6. Export the sheet as CSV (`File > Download > Comma-separated values`). Paste the rows into [THUMB_DESCRIPTIONS] in the prompt below.
7. Run P-THUMB-01. Save the answer as `thumbnails/thumb-dna-[CHANNEL_NAME].md`.
8. Read the result against the **Copy boundary** table below. Delete any line in the DNA that points to one specific image, person, logo, or character.

### Copy boundary

| Copy (pattern level) | Never copy (artifact level) |
|---|---|
| Layout family: subject left, text right | The same photo, crop, or pose of a real person |
| Text length: 2 to 4 words, bold, high contrast | The same words in the same font as one particular thumbnail |
| Color temperature: warm subject on dark teal background | An identical hex palette plus identical layout plus identical props together |
| Emotion: relief at a cheap result | A recognizable face, mascot, logo, character, or watermark |
| Curiosity gap: price reveal | A signature prop that identifies the creator (a named mug, a branded apron) |
| Focal ratio: subject fills about 40 percent of the frame | Reused image elements cut from their thumbnails |

## Prompts

### P-THUMB-01 — Thumbnail DNA analysis

Purpose: Find the repeatable decisions behind the thumbnails of one channel and write them as a reusable rule block called [THUMB_DNA].

Inputs: [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [THUMB_DESCRIPTIONS] (the 20 rows of your thumb-watch-log, pasted as CSV or a table), [STYLE_BIBLE] (optional).

```
You are a thumbnail analyst who has reviewed thousands of YouTube thumbnails. Work only from the text I give you. Do not invent thumbnails I did not describe.

Channel: [CHANNEL_NAME]
Niche: [NICHE]
Audience: [AUDIENCE]
Language of any on-image text: [LANGUAGE]
Style Bible (may be empty): [STYLE_BIBLE]

Here are 20 thumbnails described row by row. The first 10 are top performers, the last 10 are recent.
[THUMB_DESCRIPTIONS]

Do the following, in this order, and use the exact headings.

1. DATA CHECK
List any row with a missing field. Do not guess the missing value; write "missing" and continue.

2. PATTERN TABLE
For each dimension below, give the dominant choice, the share of the 20 thumbnails that use it (for example 14 of 20), and one exception.
Dimensions: composition (layout and focal ratio), text (word count, position, style), color (3 dominant hues, warm or cool, background type), emotion (trigger and expression), contrast (high, medium, low and how it is achieved), face or object focus, curiosity gap (type and how clearly it is stated).

3. TOP-10 VERSUS RECENT-10
Name every dimension where the top 10 differ from the recent 10. Say what that suggests, and label it "hypothesis" because ten items are not proof.

4. CURIOSITY GAP AUDIT
For each gap type found, state what the viewer is promised. Mark each as "paid off in the video" or "not paid off" using the Payoff column. Flag any thumbnail where the promise is larger than the video could deliver. We will not reproduce that pattern.

5. THUMB_DNA BLOCK
Write a block of at most 350 words, headed [THUMB_DNA], that a designer who has never seen the channel could follow. It must contain:
- LAYOUT RULES (3 to 5 rules, with focal ratio in percent of frame)
- TEXT RULES (max words, position, style, size relative to frame height)
- COLOR RULES (named colors, warm or cool, background treatment)
- EMOTION AND FACE RULES (when to use a face, which expressions, when to use an object instead)
- CURIOSITY RULES (which gap types, how to state them honestly)
- FREEDOM LIST: 6 things that are allowed to vary in every new thumbnail so no two look the same
- DO-NOT-COPY LIST: faces, logos, mascots, characters, exact phrases, exact props, watermarks, and any image element taken from the channel
Describe patterns only. Do not name or describe any one creator's face or any single thumbnail's unique artwork.

6. SIMILARITY RISK NOTES
Name the 3 elements in this channel's thumbnails that are most distinctive and would make a copy easy to recognize. Tell me to change each of them.

Keep the output plain. No praise, no filler.
```

Expected output: Six labeled sections ending with a [THUMB_DNA] block under 350 words, a pattern table with counts out of 20, and three named distinctive elements to change.

If the output is weak: (1) If counts are vague, say "give counts as X of 20 for every row of the table and recompute from my rows." (2) If the block is generic ("use bright colors"), say "rewrite the [THUMB_DNA] block with numbers: word count, focal percentage, and 3 named colors." (3) If the AI describes a thumbnail you did not give it, say "use only my rows; delete anything that is not in them."

### Worked example (neutral niche: home cooking on a budget)

Ten sample rows summarised, so you can see what a finished log looks like:

| ID | Layout | Focal | Text words | Colors | Gap |
|---|---|---|---|---|---|
| 1 | Subject right, text left | Finished bowl of lentil soup | 3 ("UNDER $2") | Orange, charcoal, cream | Number or price |
| 2 | Split before/after | Empty fridge vs full plate | 2 ("FRIDGE EMPTY?") | Teal, yellow, white | Result hidden |
| 3 | Single subject centered | Hands holding a pan | 0 | Red, black | Mistake reveal |

A [THUMB_DNA] block built from the full 20 rows might read: "Layout: finished dish fills 40 percent of the frame, right of center; text sits on the left third. Text: 2 to 4 words, bold condensed sans, white with a dark outline, cap height at least 90 px on the 720 px canvas. Color: warm food against a cool charcoal or teal background. Emotion: relief and desire. Curiosity: price number or hidden result, always paid off in the first 90 seconds. Freedom list: dish type, background color pair, text position (left or top), prop, camera angle, accent shape." Every item is a rule, none points to one image.

## Done when

- `thumb-watch-log` has 20 complete rows with no empty cells.
- `thumb-dna-[CHANNEL_NAME].md` contains a [THUMB_DNA] block of 350 words or fewer.
- Every dimension in the pattern table has a count out of 20.
- The DNA contains no face, logo, mascot, character, or exact phrase from the channel.
- You have a list of 3 distinctive elements you will change.

## Next

Continue to [02-original-generation.md](02-original-generation.md).
