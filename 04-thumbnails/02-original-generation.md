# Original Thumbnail Generation

> Purpose: Produce brand-new thumbnail images in the family style of [THUMB_DNA] using free generators, with a built-in method to stay clearly different from the source thumbnails.
> Use when: You have a [THUMB_DNA] block and a [VIDEO_TOPIC].
> Time needed: 20 to 30 minutes per video (3 variants).
> Needs: One free image generator or none (fallbacks below), a free editor from 03-design-workflow-and-templates.md.
> Cost: $0

## Inputs

- [THUMB_DNA] from 01-thumbnail-dna-analysis.md
- [VIDEO_TOPIC], [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [HARDWARE]
- [SOURCE_DESCRIPTION]: the written description of the 1 to 3 source thumbnails closest to your topic (used only for the difference check)
- [OWNER_ASSETS]: photos, footage frames, or drawings you made yourself (used as the main subject whenever possible)

## Steps

### 1. Choose the image source

Free image tools change their terms often. The sources I checked on 2026-10-20 disagree with each other on commercial rights for several of them. Treat every row as VERIFY BEFORE RELYING and read the tool's own terms page before you publish an image from it on a monetized channel.

| Source | Free limit reported (verify) | Commercial status | Trap | Fallback |
|---|---|---|---|---|
| Your own photos and screenshots | Unlimited | You own them | None | This is the best option for [FACE_OR_FACELESS] = FACE or for food, product, or process shots |
| Stable Diffusion 3.5 (local, ComfyUI) | Unlimited on your GPU | Community License allows free commercial use under US$1M annual revenue (reported 2026-10-20; read the license) | Needs a capable GPU; check [HARDWARE] | Online free host |
| FLUX.1 schnell (local) | Unlimited on your GPU | Reported as Apache 2.0; VERIFY on the model card | GPU needed; other FLUX variants have different licenses | Any other row |
| Leonardo.ai free | Reported about 150 tokens per day | Sources say royalty-free but images are public on the free plan | Public gallery; limits change | Own photos |
| Adobe Firefly free | Reported 25 credits per month in one source and 4 per day in another | Marketed as commercially safe; VERIFY the free-plan terms | Credit limits; watermark on some outputs | Own photos |
| Bing Image Creator / Copilot | Reported 15 fast boosts then slower unlimited | Sources conflict: one says personal use only, another says commercial allowed | Terms may bar commercial use | Do not use it for a monetized channel until you read the current Microsoft terms |
| Canva free (Magic Media) | Reported 50 credits per month | Conflicting; reported watermark on free AI images | Watermark; credits | Canva's non-AI free photos and shapes, if the license permits your use; read Canva's license page |
| Ideogram free | Reported 10 per day | A third-party source claims commercial use allowed; VERIFY | Public images on free plans | Add text in your editor instead |
| Google Gemini image generation | Reported to have a free allowance | VERIFY Google's current terms | Allowance changes | Own photos |

Rules for every source:
1. Keep a record: the tool, the date, the prompt, and a link to the terms page. Put it in `thumbnails/asset-log.csv` with columns `file, tool, date, prompt, terms_url, commercial_ok (Y/N/CHECK)`.
2. If `commercial_ok` is CHECK, do not publish that image.
3. If the free tool adds a watermark, do not crop it out; use another source.

### 2. Generate the image without text

Image generators still misspell text often. Generate only the subject and background, then add the words in your editor (03-design-workflow-and-templates.md). This also keeps text sharp at small sizes.

### 3. Settings

Ask for 16:9 or generate square or any ratio and extend the canvas. Export or resize to 1280 x 720 px, 16:9, JPG or PNG, under 2 MB (verified 2026-10-20 from several guides). Custom thumbnails require a verified channel (phone verification). One source reports a 50 MB desktop limit; ignore it and stay under 2 MB.

### 4. Text-overlay rules

These are this repo's design rules, not YouTube rules.

1. Maximum 4 words. Three is better. Zero is fine if the image carries the idea.
2. Cap height at least 90 px on the 720 px canvas, so it is readable at about 168 x 94 px (small feed size). Test by zooming out to 25 percent.
3. Contrast between text and its immediate background of at least 4.5:1 (the common accessibility ratio). Use a dark outline or a solid box, not a drop shadow alone.
4. Text must not repeat the title word for word. It adds the number, the question, or the reveal.
5. The text must be true of the video. If the thumbnail says "UNDER $2", a dish under $2 must be shown and costed in the video.
6. Keep text out of the bottom-right corner, where the video length stamp sits. This repo reserves x 1060 to 1280 and y 620 to 720 (VERIFY with your own phone preview).
7. One font family, two weights at most.

### 5. Negative-prompt list

Use the generator's negative prompt field if it has one. If not, add "Avoid:" and the list at the end of the prompt.

```
Negative: text, letters, words, captions, watermark, signature, logo, brand name, trademark, copyright symbol, real person, celebrity, recognizable face, known character, mascot, cartoon character, film still, brand packaging, label, extra fingers, deformed hands, extra limbs, blurry, low resolution, jpeg artifacts, cluttered background, busy pattern, duplicated objects, cropped subject, oversaturated skin, uncanny face
```

### 6. The difference method (change at least 4 of 8)

Before you generate, compare your plan with the source thumbnail description and change at least 4 of these 8 attributes. The 4-of-8 threshold is this repo's rule.

1. Layout family (subject left becomes subject right, or split becomes single).
2. Focal subject (a face becomes a finished dish, a hand becomes an object).
3. Color pair (swap warm dominant to cool dominant, or change both hues).
4. Background type (solid, gradient, scene, texture).
5. Text content, position, and style.
6. Camera angle and framing (overhead, eye level, close-up).
7. Props and objects (nothing signature, nothing branded).
8. Emotion and expression.

Also keep these three hard rules: no face of a real person you have no permission to depict, no logo or watermark, no element lifted from a source image. Then run P-THUMB-03 to audit.

## Prompts

### P-THUMB-02 — Original thumbnail concepts and image prompts

Purpose: Produce three major-difference thumbnail concepts for one video, each with a ready image prompt, a text overlay, and a difference note against the source.

Inputs: [THUMB_DNA], [VIDEO_TOPIC], [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [SOURCE_DESCRIPTION], [OWNER_ASSETS].

```
You are a thumbnail art director. Create original thumbnail concepts. Do not describe or imitate any specific existing thumbnail's artwork.

Channel: [CHANNEL_NAME] | Niche: [NICHE] | Audience: [AUDIENCE] | Text language: [LANGUAGE]
Video topic: [VIDEO_TOPIC]
Presence on screen: [FACE_OR_FACELESS]
Assets I own and can use: [OWNER_ASSETS]
Style rules to follow (the family style): [THUMB_DNA]
Source thumbnails closest to this topic, described in words (we must stay clearly different): [SOURCE_DESCRIPTION]

Produce 3 concepts. Test and Compare works best when variants differ in a major way, so make them differ in layout and text, not only in color.

For each concept give:
A. NAME (3 words)
B. LAYOUT in one sentence with percentages of the 1280 x 720 frame
C. SUBJECT and ACTION (what is in the frame, what it is doing)
D. TEXT OVERLAY (0 to 4 words, in [LANGUAGE], must be true of the video; also say where it goes and the style)
E. COLORS (3 named colors and the background type)
F. EMOTION and CURIOSITY GAP (one sentence; say what the video pays off)
G. IMAGE PROMPT for a free image generator (no text in the image; one paragraph; include subject, setting, lighting, camera angle, lens feel, color palette, and 16:9). Use only my owned assets or generic objects. No real person, no brand, no logo, no character.
H. NEGATIVE PROMPT (copy this exactly and add anything specific): text, letters, words, watermark, logo, brand name, real person, celebrity, recognizable face, known character, mascot, brand packaging, extra fingers, deformed hands, blurry, cluttered background
I. DIFFERENCE TABLE: for the 8 attributes (layout, focal subject, color pair, background, text, camera angle, props, emotion), write "same" or "changed" against the source description. At least 4 must be "changed". If fewer, rewrite the concept.
J. HONESTY CHECK: yes or no. Does the thumbnail promise exactly what the video delivers?

After the 3 concepts, write a TEST PLAN: which concept goes first, and what single difference each variant is meant to test.
Do not invent facts about the video. Plain language only.
```

Expected output: Three numbered concepts with sections A to J, a difference table with at least 4 "changed" per concept, and a test plan.

If the output is weak: (1) If concepts look alike, say "make concept 2 a split layout and concept 3 text-dominant, with different color pairs." (2) If the image prompt includes text or a brand, say "remove all words and brands from the prompt and add the negative list." (3) If fewer than 4 attributes changed, say "rewrite the concept until at least 4 of 8 are changed."

### P-THUMB-03 — Resemblance audit

Purpose: Check one finished thumbnail against the source thumbnails before you upload it.

Inputs: [SOURCE_DESCRIPTION], [FINAL_DESCRIPTION] (your own written description of the finished thumbnail: layout, subject, colors, background, exact text, angle, props, emotion).

```
You are a strict reviewer. Compare two written thumbnail descriptions. Judge only what is written.

SOURCE thumbnail(s): [SOURCE_DESCRIPTION]
MY thumbnail: [FINAL_DESCRIPTION]

1. Score each of these 8 attributes as SAME or CHANGED: layout, focal subject, color pair, background, text wording and style, camera angle and framing, props and objects, emotion and expression.
2. Count CHANGED. If fewer than 4, verdict FAIL and list the 2 cheapest changes that would bring it to 4.
3. Check these hard rules and answer YES or NO to each: contains a face of a real person without permission; contains a logo, watermark, or brand; contains an element taken from a source image; uses a character or mascot that belongs to someone else; text copies the source's words; the thumbnail promises something the video does not show (I will tell you the video's content: [VIDEO_TOPIC]).
4. Verdict: PASS only if 4 or more attributes are CHANGED and every hard rule is NO. Otherwise FAIL with a fix list.
Output a table and the verdict. No commentary.
```

Expected output: An 8-row table, a hard-rule list, and PASS or FAIL.

If the output is weak: If it says PASS with only 3 changes, say "count again; PASS needs 4 or more CHANGED."

## Done when

- You have 3 concepts per video, each with an image prompt, text overlay, and difference table.
- Every image used appears in `asset-log.csv` with `commercial_ok` equal to Y.
- Every final thumbnail is 1280 x 720 px, under 2 MB, with 4 words or fewer.
- P-THUMB-03 returned PASS for all three variants.

## Next

Continue to [03-design-workflow-and-templates.md](03-design-workflow-and-templates.md).
