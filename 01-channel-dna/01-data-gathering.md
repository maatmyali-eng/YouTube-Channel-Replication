# Data Gathering: ToS-Safe Collection for [CHANNEL_URL]

> **Purpose:** Collect the public facts about one channel that the analysis prompts need.
> **Use when:** Starting a new channel model, before running anything in 02-channel-analysis.md.
> **Time needed:** 2 to 3 hours by hand for 15 videos; about 20 minutes extra for the optional API workflow.
> **Needs:** A browser, a Google account, Google Sheets, a private folder for notes.
> **Cost:** $0

## Inputs

- [CHANNEL_URL], [CHANNEL_NAME], [NICHE], [LANGUAGE] from 00-start-here/01-setup-card.md.
- [WEEKLY_HOURS] to decide how many videos to sample (see Step 2).

## Steps

### Step 1. Know what is allowed

YouTube's Terms of Service prohibit accessing the service by automated means such as robots, botnets, or scrapers, with narrow exceptions (verified 2026-10-20). The YouTube API Services Developer Policies separately prohibit scraping YouTube data and using any technology other than YouTube API Services to access YouTube audiovisual content (verified 2026-10-20, via a published summary of the policies; VERIFY BEFORE RELYING at https://developers.google.com/youtube/terms/developer-policies). This repo therefore uses only what a person can see in a browser plus the official API.

| Activity | Status | Compliant alternative or condition |
|---|---|---|
| Watching videos on the public watch page in a normal browser | Permitted | None needed |
| Reading the visible title, description, chapters, upload date, view count, like count, comment count | Permitted | Type the numbers into the sheet by hand |
| Opening the on-page "Show transcript" panel and copying text by hand | Permitted for private analysis | Keep transcripts in a private folder. Never publish them, never reuse their wording in your scripts. Sample only the videos you need |
| Reading comments on the watch page and noting themes | Permitted | Record themes and short paraphrases. Do not store usernames |
| Official YouTube Data API reads (channels.list, playlistItems.list, videos.list, commentThreads.list) | Permitted within the API terms | Stay inside the quota. Refresh or delete stored API data as the developer policies require (VERIFY BEFORE RELYING on the policy page above) |
| Your own channel's data in YouTube Studio | Permitted | None needed |
| Downloading videos or audio (yt-dlp, "video downloader" sites, screen-ripping) | Not permitted | Watch in the browser and write observations in the Watch Notes tab |
| Scripts, bots, or headless browsers that load YouTube pages | Not permitted | Manual workflow below, or the official API |
| Bulk transcript harvesting, including libraries that call undocumented caption endpoints | Not permitted | Copy from the on-page panel for your 15 sampled videos only |
| Bulk comment harvesting, proxies, or getting around rate limits | Not permitted | commentThreads.list through the API, one video at a time |
| Reusing another creator's thumbnails, footage, voiceover, music, or script wording in your output | Not permitted | Extract the pattern (composition, color, structure), then create new assets |
| Browser extensions that overlay stats on YouTube pages (vidIQ, TubeBuddy and similar) | Gray area | They read page data automatically. If you use one, treat it as a viewer aid, read the numbers by eye, and type them into your sheet. Check the extension's own terms |
| Free web tools that fetch transcripts from a pasted URL | Gray area, likely against the ToS | Use the on-page transcript panel by hand |
| Pasting a YouTube link into Google's own AI products so they summarize the video | Gray area, lower risk because it is Google's first-party feature | Free limits and terms change. VERIFY BEFORE RELYING at https://ai.google.dev/gemini-api/docs/video-understanding. If unsure, use the Watch Notes tab instead |
| Screenshots of a few thumbnails for private analysis | Gray area | Do not edit or republish them. Prefer the text description fields in the sheet (composition, colors, text, face) |
| Third-party estimated-earnings sites | Gray area for accuracy, not for ToS | Treat revenue estimates as guesses. Never put them in a plan as facts |

### Step 2. Decide the sample size

- If [WEEKLY_HOURS] is 5 or less: sample 10 long videos and 5 Shorts.
- If [WEEKLY_HOURS] is more than 5: sample 15 long videos and 10 Shorts.
- Skip the Shorts rows if you only plan to make long-form, and the reverse. Long-form and Shorts are analyzed separately because their baselines differ.

### Step 3. Build the spreadsheet

1. Go to https://sheets.google.com and click Blank spreadsheet. Name it `[CHANNEL_NAME] data`.
2. Rename the first tab `Videos`. Add tabs named `Comments`, `Cadence`, `Settings`, `Picks`, `Watch Notes`.
3. In `Videos`, paste this header row into cell A1 (it splits into columns on paste if you use Data > Split text to columns with Tab as the separator):

```
video_id	type	publish_date	title	length_min	views	likes_shown	comments_shown	pillar	hook_type	title_formula	thumb_notes	age_days	views_per_day	outlier_ratio	sample_group	transcript_saved	notes	gap_days
```

4. Column meanings: `type` is Long or Short. `pillar` is the content category you assign. `hook_type` and `title_formula` are your labels (for example Question, Number list). `thumb_notes` is one sentence on composition, colors, text, and face. `sample_group` is BEST, WORST, or MID. `gap_days` is days since the previous upload.
5. Formulas (row 2, then fill down to row 61):
   - M2 `=TODAY()-C2`
   - N2 `=IF(M2>0,F2/M2,"")`
   - O2 `=IF(M2<28,"",F2/IF(B2="Long",Settings!$B$1,Settings!$B$2))`
   - S2 `=IF(C3="","",C2-C3)` (requires rows sorted newest first)
6. In `Settings`, put the label `long baseline` in A1 and this formula in B1: `=MEDIAN(FILTER(Videos!F2:F61,Videos!M2:M61>=28,Videos!B2:B61="Long"))`. Put `short baseline` in A2 and in B2: `=MEDIAN(FILTER(Videos!F2:F61,Videos!M2:M61>=28,Videos!B2:B61="Short"))`.
7. In `Picks`, cell A1 for the top long videos: `=SORT(FILTER(Videos!A2:S61,Videos!M2:M61>=28,Videos!B2:B61="Long"),15,FALSE)`. In cell A30 for the bottom: `=SORT(FILTER(Videos!A2:S61,Videos!M2:M61>=28,Videos!B2:B61="Long"),15,TRUE)`. Copy both blocks to cells further down with `"Short"` for Shorts.
8. In `Comments`, headers: `video_id	comment_text	likes	theme_tag	sentiment	is_question_or_request`.
9. In `Cadence`: A1 `median gap days`, B1 `=MEDIAN(Videos!S2:S61)`. A2 `long uploads last 90 days`, B2 `=COUNTIFS(Videos!C2:C61,">="&TODAY()-90,Videos!B2:B61,"Long")`. A3 `Shorts last 90 days`, B3 `=COUNTIFS(Videos!C2:C61,">="&TODAY()-90,Videos!B2:B61,"Short")`. A4 `most common weekday (1=Mon)`, B4 `=MODE(ARRAYFORMULA(WEEKDAY(Videos!C2:C61,2)))`.
10. Public pages do not show upload time of day. Record only the date.

### Step 4. Manual collection (no code)

1. Open [CHANNEL_URL] in your browser. Click the Videos tab. Click Latest. Scroll until about 60 videos load.
2. For each video, type the title, publish date, length, and view count into `Videos`. Mark type as Long. Do the same on the Shorts tab with type Short.
3. Sort rows newest first by publish date.
4. Open a video's watch page. Click `...more` under the video. Copy the full description into your private notes. Note any chapters (timestamped lines or the segments on the progress bar).
5. Check the Videos tab chip `Popular` to see which videos the channel's audience rewarded most. Use it only as a cross-check of the sheet ranking.
6. Pick your sample using Step 5, then for each sampled video: click `...more`, scroll to the bottom of the description, click `Show transcript`. In the panel, click the three-dot menu and choose `Toggle timestamps` as you need. Select the text with the mouse and press Ctrl+C. Save it as `transcripts-private/[video_id].txt`. The button label or position can change; if you cannot find it, VERIFY BEFORE RELYING on the current layout at https://support.google.com/youtube.
7. Add `transcripts-private/` to your `.gitignore` if the repo is on GitHub.
8. For comments, on 5 sampled videos scroll to the comment section, set Sort by to Top comments, and read 30 top-level comments each. Paste shortened text into `Comments` without usernames. Tag a theme and mark questions or requests.
9. In `Watch Notes` write one row per sampled video: cuts counted in a 60-second stretch, music present (Y/N) and loudness relative to voice (lower/similar/higher), sound effects (Y/N), on-screen text frequency, three dominant colors, font style described in words, face on screen (Y/N), thumbnail text word count. These notes compensate for text-only AI models (see 02-channel-analysis.md).

### Step 5. Pick the 10 best and 5 worst

Rules, applied to videos at least 28 days old so views have mostly settled (a working heuristic, not a YouTube rule):

1. BEST (10): highest `outlier_ratio` in `Picks`, but include at least 3 different pillars and, if the channel mixes lengths, at least 2 length bands. If one pillar fills the top 10, take its best 4 and fill the rest from the next pillars.
2. WORST (5): lowest `outlier_ratio`, but exclude live streams, premieres, announcements, and one-off off-topic uploads, because their low numbers say nothing about style. Keep videos that sit squarely in a main pillar.
3. Mark the rest MID. Pull transcripts only for BEST and WORST.
4. Caveats: views can come from promotion, collaborations, or external links, so one outlier is a lead, not a rule. A title or thumbnail may have been changed after upload; record what you see now.
5. Run P-CDNA-03 to check your picks.

### Step 6. Optional: official Data API workflow

This uses the official API through Google Apps Script. It reads public metadata only.

1. In your sheet click Extensions > Apps Script. Click the + next to Services, choose `YouTube Data API v3`, click Add.
2. Replace the editor content with the script below. Set `CHANNEL_HANDLE` to the channel's handle including `@`.
3. Click Run on `pullChannelMetadata`, approve the permissions, then check the `Videos` tab.
4. Quota (verified 2026-10-20): the default project quota is 10,000 units per day; channels.list, playlistItems.list, videos.list, and commentThreads.list cost 1 unit per call; one call returns up to 50 items (100 comments for commentThreads); the quota resets at midnight Pacific Time. The official page lists search.list and videos.insert in their own buckets of 100 calls per day at 1 unit each, while other sources describe search.list as costing 100 units from the shared pool; this workflow avoids search.list, so the difference does not affect you. Check usage at the Quotas page in the Google Cloud console.
5. The API has no reliable flag that marks a video as a Short (VERIFY BEFORE RELYING at https://developers.google.com/youtube/v3/docs/videos). Fill the `type` column by checking the channel's Shorts tab by hand.

```javascript
const CHANNEL_HANDLE = '@REPLACE_WITH_HANDLE';
const MAX_VIDEOS = 60;

function isoToMinutes(d) {
  const m = d.match(/PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?/);
  const h = +(m[1] || 0), mi = +(m[2] || 0), s = +(m[3] || 0);
  return Math.round((h * 60 + mi + s / 60) * 100) / 100;
}

function pullChannelMetadata() {
  const sheet = SpreadsheetApp.getActive().getSheetByName('Videos');
  const ch = YouTube.Channels.list('contentDetails,snippet,statistics', { forHandle: CHANNEL_HANDLE });
  if (!ch.items || ch.items.length === 0) throw new Error('Channel not found: ' + CHANNEL_HANDLE);
  const uploads = ch.items[0].contentDetails.relatedPlaylists.uploads;
  let ids = [];
  let token = null;
  do {
    const page = YouTube.PlaylistItems.list('contentDetails', { playlistId: uploads, maxResults: 50, pageToken: token });
    page.items.forEach(function (i) { ids.push(i.contentDetails.videoId); });
    token = page.nextPageToken;
  } while (token && ids.length < MAX_VIDEOS);
  ids = ids.slice(0, MAX_VIDEOS);
  const rows = [];
  for (let i = 0; i < ids.length; i += 50) {
    const batch = YouTube.Videos.list('snippet,contentDetails,statistics', { id: ids.slice(i, i + 50).join(',') });
    batch.items.forEach(function (v) {
      const st = v.statistics || {};
      rows.push([
        v.id, '', new Date(v.snippet.publishedAt), v.snippet.title,
        isoToMinutes(v.contentDetails.duration),
        Number(st.viewCount || 0),
        st.likeCount === undefined ? '' : Number(st.likeCount),
        st.commentCount === undefined ? '' : Number(st.commentCount)
      ]);
    });
  }
  sheet.getRange(2, 1, rows.length, 8).setValues(rows);
}

function pullTopComments() {
  const VIDEO_ID = 'REPLACE_WITH_VIDEO_ID';
  const sheet = SpreadsheetApp.getActive().getSheetByName('Comments');
  try {
    const res = YouTube.CommentThreads.list('snippet', { videoId: VIDEO_ID, maxResults: 100, order: 'relevance', textFormat: 'plainText' });
    const rows = res.items.map(function (t) {
      const c = t.snippet.topLevelComment.snippet;
      return [VIDEO_ID, String(c.textDisplay).slice(0, 300), c.likeCount];
    });
    if (rows.length) sheet.getRange(sheet.getLastRow() + 1, 1, rows.length, 3).setValues(rows);
  } catch (e) {
    Logger.log('Comments unavailable for ' + VIDEO_ID + ': ' + e.message);
  }
}
```

## Prompts

### P-CDNA-03 — Outlier Pick Check

Purpose: Confirm your 10 best and 5 worst picks are fair and varied before you spend time on transcripts.
Inputs: [CHANNEL_NAME], [NICHE], [PICKS_TABLE] (the Picks tab pasted as text, top 20 and bottom 10 rows), [BASELINES] (the two numbers from Settings).

```
You are a YouTube analytics reviewer. I am studying the style of the channel [CHANNEL_NAME] in the niche [NICHE]. Below are its videos at least 28 days old, ranked by outlier_ratio (views divided by the channel median for that format).

[BASELINES]
[PICKS_TABLE]

Tasks:
1. Select the 10 best videos to study. Rules: at least 3 different pillars, and at least 2 length bands if lengths vary. Explain each pick in one line.
2. Select the 5 worst videos to study. Exclude live streams, premieres, announcements, and one-off off-topic uploads. Explain each pick in one line.
3. List confounders that could make a ranking misleading (promotion, collaboration, trend timing, title or thumbnail change, series effects). Name which picks they affect.
4. Report any pillar that is over-represented in the best 10 and say whether that reflects the audience or the channel's upload mix.
5. State what you cannot know from this table, such as impressions, click-through rate, and retention.
Use only the data given. If a field is blank, say so instead of guessing.
```

Expected output: Two numbered lists of picks with one-line reasons, a confounder list, and an unknowns list.
If the output is weak: Paste fewer rows, add the pillar column, and tell it "do not infer any number that is not in the table."

### P-CDNA-04 — Comment Theme Clustering

Purpose: Turn shortened comments into audience needs, objections, and requests.
Inputs: [CHANNEL_NAME], [NICHE], [COMMENTS_TEXT] (comments pasted without usernames), [VIDEO_TITLES] (titles of the videos the comments came from).

```
You are an audience researcher. Below are top-level comments from public videos on [CHANNEL_NAME] ([NICHE]), with usernames removed.

Videos: [VIDEO_TITLES]
Comments: [COMMENTS_TEXT]

Produce:
1. Between 5 and 8 themes. For each: a name, a count of comments in it, the underlying viewer need, and a 6-word-or-fewer paraphrase (not a copy) of one typical comment.
2. Every explicit question or request, grouped by topic. These are candidate future video topics.
3. Complaints or criticisms of the channel itself, grouped.
4. Words and phrases the audience uses for the topic, written as single terms, so I can match their vocabulary.
5. A caution list: themes that look like a few repeated commenters, bot-like comments, or jokes, so I do not over-weight them.
Do not identify or guess anything about individual commenters. Do not claim demographics unless a comment states it.
```

Expected output: Theme table, request list, complaint list, vocabulary list, caution list.
If the output is weak: Reduce to 60 comments from one video at a time and merge the results with a second run that asks it to combine two theme lists.

## Done when

- The `Videos` tab holds at least 40 rows for the channel with publish dates and views.
- The `Settings` baselines show numbers, not errors.
- You have 10 BEST and 5 WORST rows marked in `sample_group`, passing the checks in P-CDNA-03.
- Transcripts for those videos sit in `transcripts-private/` and are not in any public repo.
- `Watch Notes` has a row for every sampled video.
- `Comments` has themes tagged for at least 5 videos.

## Next

Continue to [02-channel-analysis.md](02-channel-analysis.md).
