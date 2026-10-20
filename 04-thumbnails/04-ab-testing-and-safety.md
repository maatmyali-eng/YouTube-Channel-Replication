# A/B Testing and Thumbnail Safety

> Purpose: Test thumbnails for free, read the results without fooling yourself, and clear every thumbnail for copyright, likeness, logo, and policy risk.
> Use when: Every upload, before publishing, and again 7 to 14 days after.
> Time needed: 10 minutes before publishing; 10 minutes per test result.
> Needs: YouTube Studio on desktop, `thumb-test-log` Google Sheet.
> Cost: $0

## Inputs

- Three finished variants `thumb-A.jpg`, `thumb-B.jpg`, `thumb-C.jpg` from 03-design-workflow-and-templates.md
- [CHANNEL_NAME], [VIDEO_TOPIC], [NICHE], [FACE_OR_FACELESS]
- `thumbnails/asset-log.csv` from 02-original-generation.md

## Steps

### Part 1. Thumbnail safety gate (do this first)

1. Open `asset-log.csv`. Every image in the thumbnail must have `commercial_ok` = Y. If not, stop.
2. Walk through the checklist below with the thumbnail open at full size.
3. Run P-THUMB-05 with your written description of the finished thumbnail. Fix every FAIL.
4. Only then upload.

#### Checklist: no recognizable IP or real faces without permission

Tick every line. One unticked line blocks the upload.

- [ ] No real person's face appears unless it is mine, or I hold written permission (a message or release naming the use).
- [ ] No AI-generated face is made to look like a real, named, or recognizable person, living or dead.
- [ ] No celebrity, politician, athlete, creator, or public figure, real or imitated.
- [ ] No cartoon, game, film, anime, or TV character, and no look-alike of one.
- [ ] No brand logo, product packaging, label, store sign, or trademark is visible or implied. Blur or remove incidental logos on pans, boxes, and clothing.
- [ ] No screenshot, still, or frame from another creator's video, a film, a game, or a stream.
- [ ] No stock image, icon, or font used outside its license; every one is in `asset-log.csv`.
- [ ] No watermark from a free tool, and none cropped out of someone else's image.
- [ ] No text copied from a source thumbnail, and P-THUMB-03 returned PASS.
- [ ] No other person's artwork, meme template, or fan art.
- [ ] No fake interface of YouTube, a news channel, a bank, or another platform presented as real.
- [ ] No photoreal AI image showing a real event, disaster, arrest, or public figure doing something that did not happen.
- [ ] No fake play button, fake award, fake "verified" badge, fake subscriber or view numbers.
- [ ] No nudity, sexual suggestion, graphic violence, or dangerous act shown for shock.
- [ ] No children identifiable in the image unless they are mine and I accept publishing them.
- [ ] The text and image promise only what the video delivers.

#### What YouTube prohibits on thumbnails (verified 2026-10-20 from creator-policy summaries; read the official Help page before relying)

Thumbnails with nudity or sexually provocative content, hate speech, violence, or harmful and dangerous content can be rejected and can bring a strike. Misleading thumbnails, meaning images that make viewers expect something the video does not contain, also violate policy. Repeated violations can cost you custom-thumbnail privileges. Three strikes in 90 days can end in channel termination. Official source to check: YouTube Help, search "Thumbnails" and "Spam, deceptive practices, and scams policies". VERIFY BEFORE RELYING on the exact penalty durations quoted in secondary articles.

#### AI-image disclosure

The "Altered or synthetic content" label in YouTube Studio applies to realistic content in the video. For thumbnails, the safe rule is simpler: do not publish photorealistic AI images of real people or real events. Stylized or clearly illustrated images are low risk. If you use a realistic synthetic image anyway, open the 02-long-form/03-voice-and-audio.md disclosure table and quote the current YouTube Help wording; VERIFY BEFORE RELYING on Studio's current rules.

### Part 2. Free A/B testing

#### Method 1: YouTube Test & Compare (preferred when you have it)

Facts (verified 2026-10-20 from several creator-news and guide sources):
- You upload up to 3 thumbnail variants for one video. YouTube shows them evenly to viewers and reports which earned the most watch time share.
- Results take a few days to two weeks, depending on impressions. If there is no clear winner, the first thumbnail is selected, and you can still change it manually.
- It runs in YouTube Studio on desktop. It is not available for private videos, mature-rated content, or videos made for kids.
- Access: sources agree you need Advanced Features (identity verification by phone or ID). One source says the tool is limited to channels in the YouTube Partner Program; others say all channels with Advanced Features. VERIFY BEFORE RELYING at YouTube Help, search "Test & Compare".
- One source says it also tests titles. VERIFY in Studio whether a title field shows the option.

Steps:
1. Go to YouTube Studio on a computer. Verify your channel under **Settings > Channel > Feature eligibility** and switch on **Advanced features** (VERIFY the menu names).
2. Open **Content**, click the video, and in the **Thumbnail** area look for **Test & Compare**. If you cannot see it, use Method 2.
3. Upload thumb-A, thumb-B, thumb-C. Make them differ in layout, text, and color, not just a shade.
4. Publish. Do not touch the title, description, or thumbnails for the test window.
5. When Studio reports results, copy them to `thumb-test-log`.

#### Method 2: manual rotation (when Test & Compare is not available)

This is weaker because videos change over time. Use it only to avoid obviously bad thumbnails.

1. Publish with thumb-A. Leave it for 7 days or until 1,000 impressions, whichever is later. These thresholds are this repo's rules.
2. Record in the log: impressions, click-through rate (CTR), average view duration, views. Find them under **Analytics > Reach** for the video (VERIFY the tab name).
3. Swap to thumb-B on the same weekday. Wait the same time. Record the same numbers.
4. Compare. If you have a third variant, repeat with thumb-C.
5. Keep the better one. Do not swap more than once every 7 days.

#### What to measure

| Metric | Where | Why |
|---|---|---|
| Watch time share (Test & Compare) | Test results panel | YouTube's own winner measure, which rewards the thumbnail that brings viewers who stay |
| Impressions click-through rate | Analytics > Reach | Click appeal. Check against your own channel's average. A claimed benchmark of 4 to 5 percent as "strong" appears in guides; it varies by niche, so VERIFY with your own channel's median |
| Average view duration and percentage viewed | Analytics > Engagement | Detects clickbait: high CTR with low retention means the thumbnail over-promises |
| Impressions | Analytics > Reach | Needs enough volume before you trust CTR |

Decision rules (this repo's rules):
- Treat any CTR difference under 10 percent relative (for example 5.0 percent versus 5.4 percent) as a tie. Keep the more honest one.
- If a variant has higher CTR but lower average view duration by 15 percent or more, drop it. It is bringing the wrong viewers.
- Record one lesson per test, stated as a hypothesis, for example "price number beat question".
- Test one big difference at a time across uploads so the lesson is readable.

`thumb-test-log` columns: `video slug, test method, variants, template codes, impressions, CTR A, CTR B, CTR C, watch time share, avg view duration, winner, lesson, date`.

## Prompts

### P-THUMB-05 — Thumbnail safety review

Purpose: Check a finished thumbnail description against copyright, likeness, logo, and policy risks.

Inputs: [FINAL_DESCRIPTION] (written description of the thumbnail with exact text), [VIDEO_TOPIC], [ASSET_LOG_ROWS] (rows from asset-log.csv for the images used), [CHANNEL_NAME].

```
You are a compliance reviewer for YouTube thumbnails. Judge only the description and the asset log I give you. Do not guess about things I did not describe; list them as UNKNOWN.

Thumbnail description: [FINAL_DESCRIPTION]
Video content: [VIDEO_TOPIC]
Asset log rows: [ASSET_LOG_ROWS]

Answer each item with PASS, FAIL, or UNKNOWN and one reason:
1. Real person's face without permission, or an AI face imitating a real or recognizable person.
2. Celebrity, politician, public figure, or imitation of one.
3. Third-party character, mascot, or look-alike.
4. Visible logo, brand packaging, label, or trademark.
5. Frame, screenshot, or artwork taken from another creator, film, game, or stream.
6. Asset licensing: every image has commercial_ok = Y and a terms URL.
7. Watermark or cropped watermark.
8. Text copied from another thumbnail or title.
9. Fake interface, fake badge, fake numbers, fake play button.
10. Photorealistic synthetic depiction of a real event or real person.
11. Nudity, sexual suggestion, graphic violence, dangerous act.
12. Misleading: promise in image or text not delivered by the video content.
13. Sensitive topic risk (health, finance, legal, news, tragedy) that needs a safer treatment.

Then give: overall verdict (BLOCK if any FAIL, HOLD if any UNKNOWN, CLEAR otherwise), the shortest fix for each FAIL, and the exact question I must answer for each UNKNOWN. No commentary.
```

Expected output: A 13-line table, a verdict, and fixes or questions.

If the output is weak: Say "answer all 13 items and use only PASS, FAIL, or UNKNOWN."

### P-THUMB-06 — Test result reader

Purpose: Turn Test & Compare or manual rotation numbers into one decision and one lesson without over-reading small samples.

Inputs: [TEST_NUMBERS] (the row from `thumb-test-log`), [VARIANT_DESCRIPTIONS] (what differed between A, B, C).

```
You are a careful analyst. Use only the numbers I give you.

Variants described: [VARIANT_DESCRIPTIONS]
Test numbers: [TEST_NUMBERS]

1. State which variant has the best result on each metric I provided.
2. Apply these rules: a relative CTR difference under 10 percent is a tie; a variant with 15 percent or lower average view duration than the others is rejected even if its CTR is higher; fewer than 1,000 impressions per variant means "not enough data".
3. Give one decision: keep A, B, or C, or "no decision, keep the most accurate thumbnail".
4. Write one lesson as a hypothesis, naming the single difference that most likely caused the result.
5. List what I should do differently in the next test (one change at a time).
Do not claim statistical significance. Do not invent numbers.
```

Expected output: Decision, one lesson, and one change for the next test.

If the output is weak: Say "apply the 10 percent and 15 percent rules literally and show the arithmetic."

## Done when

- Every thumbnail passed the 16-line checklist and P-THUMB-05 returned CLEAR.
- Each upload has either a Test & Compare run or a logged manual rotation with at least 1,000 impressions per variant.
- `thumb-test-log` holds one lesson per video.
- No thumbnail was published with a PASS missing from P-THUMB-03.

## Next

Continue to [../05-originality-layer/01-differentiation-method.md](../05-originality-layer/01-differentiation-method.md).
