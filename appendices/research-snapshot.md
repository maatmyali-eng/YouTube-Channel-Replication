# Research Snapshot (Dated Facts, Sources, and How to Re-Verify)

> **Purpose:** One place that lists every time-sensitive fact this repo relies on, where it came from, when it was checked, and how to check it again.  
> **Use when:** Before you apply for YPP, before you buy or rely on any tool, and whenever a policy announcement appears.  
> **Time needed:** 15 minutes to re-verify one row; about 2 hours for the full table.  
> **Needs:** A browser and a web-enabled AI chat tool or search engine.  
> **Cost:** $0

## Inputs

- The repo snapshot dated 2026-10-20 (given in the project pack).
- Web re-verification performed on 2026-10-21 by search. Rows say which.
- Prompt-specific placeholders, defined in P-OPS-06: [ROW_NUMBERS], [PAGE_TEXT].

## Steps

1. Read the "Disagreements" and "Facts most likely to change next" sections first.
2. For any row you will act on, run its "How to re-verify" step. Open the official page, not a blog.
3. Update the "Date verified" cell and, if the fact changed, the file that uses it (search the repo for the old number).
4. Where a row says VERIFY BEFORE RELYING, do not act on it until you have read the named official page yourself.
5. Optionally run P-OPS-06 to compare a pasted page against a row.

Date format: YYYY-MM-DD. "Official page" means YouTube Help, YouTube Blog, Google AdSense Help, Google Developers documentation, or the tool's own license file. The expression "secondary source" means a third-party article. I could not open YouTube Help pages directly in my sessions, so rows built on secondary sources say so, and the confidence column tells you how much to trust them.

## Table 1: YouTube Partner Program

| # | Fact | Source URL | Date verified | How to re-verify | Confidence |
|---|---|---|---|---|---|
| 1 | Tier 1 (fan funding, Shopping): 500 subscribers, 3 public uploads in 90 days, and either 3,000 qualified public watch hours in 12 months or 3 million qualified public Shorts views in 90 days. | https://vidiq.com/blog/post/monetize-youtube-guide/ ; https://www.tella.com/blog/how-to-join-youtube-partner-program | 2026-10-21 | Open YouTube Studio → Earn and read the thresholds shown for your country; then open the YouTube Help "YouTube Partner Program overview and eligibility" page and compare. | Medium (secondary sources agree; Studio is final) |
| 2 | Tier 2 (ads and Premium share): 1,000 subscribers and either 4,000 qualified watch hours in 12 months or 10 million qualified Shorts views in 90 days. | https://vidiq.com/blog/post/monetize-youtube-guide/ ; https://air.io/en/monetization/youtube-partner-program-requirements-2026-the-complete-guide | 2026-10-21 | Same as row 1. | Medium |
| 3 | From 1 Feb 2027, new Tier 2 applicants need 8,000 qualified watch hours or 20 million qualified Shorts views; announced 10 Aug 2026. Applying before that date uses the lower thresholds. | https://air.io/en/youtube-glossary/what-is-the-youtube-partner-program-ypp-requirements-benefits ; https://vidiq.com/pt/blog/post/new-ypp-terms-monetization | 2026-10-21 | Search the YouTube Blog and Creator Insider for "Partner Program 2027 thresholds". Read the announcement date and effective date in the primary post. | Medium |
| 4 | Subscriber requirement after 1 Feb 2027 stays at 1,000 (two secondary sources say unchanged; one lists no figure). | https://vidiq.com/pt/blog/post/new-ypp-terms-monetization ; https://air.io/en/youtube-glossary/what-is-the-youtube-partner-program-ypp-requirements-benefits | 2026-10-21 | VERIFY BEFORE RELYING: read the primary announcement and the YouTube Help eligibility page. | Low |
| 5 | Qualified watch hours come only from public long-form videos (including podcasts) and archived livestreams. They exclude private, unlisted, deleted, ad-viewed videos, Shorts watch time, and non-archived live streams. | https://blog.youtube/news-and-events/youtube-monetization-qualified-watch-hours-shorts-views/ | 2026-10-21 | Open the YouTube Blog post (dated 12 Aug 2026) and compare the list. | High (official blog) |
| 6 | Qualified Shorts views must be public and engaged (viewer stayed past the initial seconds; loops do not count). Excluded: private, unlisted, deleted, ad-viewed Shorts, long-form views, and image posts in the Shorts feed. | https://blog.youtube/news-and-events/youtube-monetization-qualified-watch-hours-shorts-views/ | 2026-10-21 | Same post; then check "engaged views" in Studio → Analytics. | High |
| 7 | Shorts views and long-form watch hours never combine. | https://air.io/en/monetization/youtube-partner-program-requirements-2026-the-complete-guide | 2026-10-21 | Studio → Earn shows two separate progress paths; confirm there. | High |
| 8 | From 1 Feb 2027, keeping Shorts revenue requires 10 million qualified Shorts views per rolling 90 days. | https://air.io/en/youtube-glossary/what-is-the-youtube-partner-program-ypp-requirements-benefits | 2026-10-21 | VERIFY BEFORE RELYING: read the primary announcement; the wording ("for members") may be narrower than secondary summaries. | Low |
| 9 | Apply in Studio → Earn after linking AdSense and enabling 2-step verification. | https://vidiq.com/pt/blog/post/youtube-partner-program-guide | 2026-10-21 | Follow the application path in Studio; menu labels change. | Medium |
| 10 | Where the expanded program (Tier 1) is available depends on country. A 2023 report listed the U.S., U.K., Canada, Taiwan, and South Korea at launch; current coverage is not confirmed here. | https://techcrunch.com/?p=2556997 | 2026-10-21 | VERIFY BEFORE RELYING: open the YouTube Help page listing countries where expanded YPP is available. Check your [COUNTRY]. | Low |

## Table 2: Content policy and disclosure

| # | Fact | Source URL | Date verified | How to re-verify | Confidence |
|---|---|---|---|---|---|
| 11 | "Inauthentic content" (clarified 16 July 2026; renamed from "repetitious content") has three non-monetizable categories: generic, repetitive, or template-based content with little variation; off-putting or distressing content; AI personas discussing sensitive topics such as health and finance. | https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/ | 2026-10-21 | Open YouTube Help "Monetization policies" → "Inauthentic content". Compare the three categories word by word. | Medium (news report of an official video) |
| 12 | Enforcement works at channel level based on patterns across recent uploads. | https://hackernoon.com/youtubes-ai-slop-crackdown-cant-tell-a-directed-ai-film-from-a-bot-farm | 2026-10-21 | VERIFY BEFORE RELYING: single opinion piece; look for the same statement on YouTube Help or Creator Insider. | Low |
| 13 | AI voiceover can qualify when the video has original commentary, education, or entertainment value. The policy targets mass production, not AI itself. | https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/ ; https://medium.com/no-time/youtubes-new-monetization-warning-has-creators-panicking-but-here-s-what-the-update-actually-f52313a33fe5 | 2026-10-21 | Same as row 11. | Medium |
| 14 | The separate reused-content policy did not change. | https://invideo.io/blog/youtube-kills-ai-faceless-channels/ | 2026-10-21 | YouTube Help "Reused content" page; check the "last updated" note. | Medium |
| 15 | Realistic altered or synthetic content must be disclosed in Studio ("Altered or synthetic content"); unrealistic, animated, and minor edits do not need it. YouTube can add the label itself (since May 2026, snapshot). | https://blog.youtube/inside-youtube/our-approach-to-responsible-ai-innovation/ ; https://air.io/en/youtube-hacks/youtube-ai-disclosure-in-2026-label-it-yourself-or-youtube-will | 2026-10-21 | Open YouTube Help "Disclosing use of altered or synthetic content" and compare the examples list. | Medium |
| 16 | Whether AI voiceover and AI music need the label: sources disagree. One secondary source says AI music needs a label and a generic voice does not. The repo rule: when unsure, disclose. | https://air.io/en/youtube-hacks/youtube-ai-disclosure-in-2026-label-it-yourself-or-youtube-will | 2026-10-21 | VERIFY BEFORE RELYING: quote the current YouTube Help wording into your notes. | Low |
| 17 | Undisclosed branded content can be auto-labeled by YouTube, per announcements of 3 Sep 2026. | Pack snapshot (no new source opened in this session) | 2026-10-20 | Search YouTube Help "paid product placements, sponsorships and endorsements" and the Creator Insider update. | Low-Medium |
| 18 | YouTube accepts privacy requests for synthetic content simulating an identifiable person's face or voice. | https://blog.youtube/inside-youtube/our-approach-to-responsible-ai-innovation/ | 2026-10-21 | YouTube Help "Privacy guidelines"; confirm the request form. | Medium |

## Table 3: Strikes and claims

| # | Fact | Source URL | Date verified | How to re-verify | Confidence |
|---|---|---|---|---|---|
| 19 | A Content ID claim is not a strike and does not count toward termination. | https://vidiq.com/tr/blog/post/youtube-copyright-claim-copyright-strike ; https://www.soundstripe.com/blogs/how-to-avoid-copyright-strikes-on-youtube | 2026-10-21 | YouTube Help "Understand copyright strikes" and "Content ID claims". | Medium |
| 20 | Three active copyright strikes within 90 days can lead to termination; a strike expires 90 days after it is issued if Copyright School is completed and fewer than three are active. | https://air.io/en/youtube-glossary/what-is-a-youtube-copyright-strike ; https://www.trademarkengine.com/blog/youtube-copyright-claims-vs-copyright-strikes-creators-need-to-know/ | 2026-10-21 | Same as row 19; check Studio → Content → Copyright for your own strike dates. | Medium |
| 21 | A Content ID claim on a Short over one minute can block it. | https://vidiq.com/tr/blog/post/youtube-copyright-claim-copyright-strike | 2026-10-21 | VERIFY BEFORE RELYING: this has changed with Shorts length rules; check YouTube Help "Shorts and Content ID". | Low |
| 22 | Community Guidelines strike rules and appeal windows. One source gives a 90-day figure that conflicts with other sources. | Not confirmed | not verified | VERIFY BEFORE RELYING: read YouTube Help "Community Guidelines strike basics". | Low |

## Table 4: YouTube Data API

| # | Fact | Source URL | Date verified | How to re-verify | Confidence |
|---|---|---|---|---|---|
| 23 | Videos uploaded through videos.insert from unverified API projects created after 28 July 2020 are restricted to private until the project passes a compliance audit. | https://www.upload-post.com/youtube-api/ ; https://singhamandeep.com/?p=1570 | 2026-10-21 | Open Google's videos.insert reference on developers.google.com and read the note at the top. | High (multiple sources quote the official line) |
| 24 | Uploads have their own bucket: 100 videos.insert calls per day at 1 unit each since 1 June 2026; other endpoints share 10,000 units per day; resets at midnight Pacific. Older sources say 1,600 units per upload. | https://postproxy.dev/blog/automate-youtube-uploads/ ; https://www.upload-post.com/youtube-api/ ; https://ppc.land/youtube-data-api/ | 2026-10-21 | Google Cloud Console → APIs & Services → YouTube Data API v3 → Quotas. Read the numbers for your project. | Medium |
| 25 | Developers must not keep most API data longer than 30 days without refreshing or deleting it. | https://ppc.land/youtube-data-api/ | 2026-10-21 | VERIFY BEFORE RELYING: read the Developer Policies page. | Low |
| 26 | The Analytics API only serves channels you own or manage. | https://ppc.land/youtube-data-api/ | 2026-10-21 | YouTube Analytics API documentation overview. | Medium |
| 27 | Data gathering uses the public watch page, the on-page transcript panel, public metadata, and the official Data API; no downloading or scraping at scale. | Pack snapshot; ppc.land notes scraping is outside the terms | 2026-10-20 | Read YouTube Terms of Service ("Permissions and Restrictions") and the API Services Terms. | Medium |

## Table 5: Free tools

| # | Fact | Source URL | Date verified | How to re-verify | Confidence |
|---|---|---|---|---|---|
| 28 | Kokoro-82M is Apache 2.0. | https://www.promptquorum.com/power-local-llm/piper-vs-kokoro-tts | 2026-10-21 | Open the model card at hexgrad/Kokoro-82M on Hugging Face and read the license field. | Medium |
| 29 | Piper's maintained repository (OHF-Voice/piper1-gpl) is GPL-3.0-or-later and embeds eSpeak NG; the older rhasspy/piper repository (MIT) was archived 6 Oct 2025. Voice files carry their own licenses. | https://www.promptquorum.com/power-local-llm/piper-tts-review ; https://reelmind.ai/blogs/text-to-speech-open-source-for-commercial-video-and-voice-licensing | 2026-10-21 | Open the GitHub repository's LICENSE file and the license listed for each voice you download. Narration output is generally yours, but check the voice license. | Medium |
| 30 | LTX-2 Community License (dated 5 Jan 2026): royalty-free, but entities with annual revenue of US$10 million or more need a paid commercial license; use-based restrictions apply. LTX 2.5 (released 11 Aug 2026) is reported under the LTX-2.x Community License. | https://huggingface.co/Lightricks/LTX-2.3/blob/main/LICENSE ; https://zsky.ai/blog/is-ltx-2-5-free | 2026-10-21 | Read the LICENSE file shipped with the exact model version you download. | Medium-High |
| 31 | Wan 2.2 is Apache 2.0 and needs a heavy GPU. | Pack snapshot | 2026-10-20 | Open the model's repository LICENSE and README. | Medium |
| 32 | Whisper (transcription), ComfyUI, DaVinci Resolve free, CapCut free, Canva free, n8n self-hosted, GitHub Actions free minutes, Google Sheets plus Apps Script: free to start, but each tool's limits, license, and commercial-use terms change. | Pack snapshot | 2026-10-20 | VERIFY BEFORE RELYING: open each tool's own pricing, license, and terms pages. Write down the date you checked in your tool log. | Low |
| 33 | Free video-generator tiers mostly add watermarks or limit commercial use. One site claims commercial use on every plan including free, which you must confirm on its terms page before use. | https://zsky.ai/blog/is-ltx-2-5-free (vendor claim) | 2026-10-21 | Read the terms page of the specific generator. Treat vendor marketing as unverified. | Low |

## Disagreements between sources

1. **Subscriber count after 1 Feb 2027:** two secondary sources say 1,000; one lists no figure (rows 3 and 4).
2. **AI voice and AI music labels:** secondary sources split (row 16).
3. **Upload quota per call:** older guides say 1,600 units; newer guides say 1 unit within a 100-call bucket (row 24). Your Cloud Console is the final authority.
4. **Date of the inauthentic content announcement:** reports give 14, 15, and 16 July 2026; this repo uses the 16 July clarification date from the TechCrunch report.
5. **Strike appeal windows:** secondary sources differ (row 22).

## Facts most likely to change next

1. **1 Feb 2027 YPP thresholds and the subscriber requirement.** The date is close; details may be clarified or revised. Check YouTube's blog and Studio → Earn monthly before applying.
2. **Shorts revenue rule (10 million qualified Shorts views per rolling 90 days).** It is new and described differently by different sources.
3. **Inauthentic content enforcement.** The policy was clarified in July 2026 and enforcement examples keep appearing. Re-read YouTube Help each month.
4. **AI disclosure wording for voice and music.** Sources already disagree; YouTube may change the Studio question.
5. **Branded content auto-labeling.** Announced 3 Sep 2026; rollout scope may change.
6. **YouTube Data API upload bucket and audit process.** The per-call cost changed in June 2026; the audit form and timelines can change.
7. **Free tool terms.** Licenses and free tiers shift: LTX has a revenue threshold, Piper changed license, and free video-generator tiers change watermark rules without notice.
8. **Expanded YPP country availability and AdSense requirements** (verification, tax forms, payment rules) differ by [COUNTRY].
9. **Shorts length and Content ID handling for Shorts** (row 21).

## Prompts

### P-OPS-06 — Compare a pasted page to a snapshot row

**Purpose:** Check whether an official page still matches what this file says.

**Inputs:** [ROW_NUMBERS] (the row numbers from this file, for example "3, 4, 8"), [PAGE_TEXT] (text you copied from the official page), [COUNTRY].

```
You are a fact checker. Compare the pasted official page text with the repo rows I name.

Rows to check (copy each row's fact from the repo): [ROW_NUMBERS]
Country: [COUNTRY]

Official page text:
[PAGE_TEXT]

For each row, return: Row number | What the repo says | What the page says (quote at most 15 words) | Match, Partial match, Conflict, or Not covered | Exact edit I should make to the repo row if it is a Partial match or Conflict.

Rules: Use only the pasted text. If the page does not mention the fact, answer "Not covered" and do not guess. Do not use your memory for thresholds, dates, or policy wording. End with a list of repo files that probably contain the changed fact and the search term to find it.
```

**Expected output:** One line per row, with edits for any conflict.

**If the output is weak:** Paste the complete page rather than an excerpt and ask for only the rows you named.

## Done when

- [ ] Each row you act on has a date verified within the last 30 days.
- [ ] Every VERIFY BEFORE RELYING row you depend on has been read on an official page by you.
- [ ] The file that uses any changed fact has been edited.

## Next

[Glossary](glossary.md)
