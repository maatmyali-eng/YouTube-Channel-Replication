# Free Tool Stack

> **Purpose:** List the free tools for every production step with their real limits, watermark and commercial-use status, free fallback, and paid traps.  
> **Use when:** Choosing tools for a new channel, or before relying on any tool's free tier.  
> **Time needed:** 30 minutes to pick a stack; 5 minutes per tool to re-verify.  
> **Needs:** [HARDWARE] and [WEEKLY_HOURS] from your setup card ([01-setup-card.md](01-setup-card.md)), and a browser.  
> **Cost:** $0

## Inputs

- [HARDWARE] and [WEEKLY_HOURS].
- [FACE_OR_FACELESS] and [VOICE_MODE], since they decide which categories you need.

## Steps

1. Read "How to read the tables" below. It explains the Verified column honestly.
2. Find your hardware in "Best $0 starter stack by [HARDWARE]" and write down the tools it names.
3. For each tool you will use, open the page named in the table and run the 5-minute routine at the end. Write the result in your license log (see [03-compliance-master-checklist.md](03-compliance-master-checklist.md), items C-29 and C-30).
4. Install or sign up for one tool at a time. Test one export before adding the next.
5. Any tool that fails the commercial-use or watermark check is replaced by its free fallback.

## How to read the tables

I could not open live pricing or terms pages while writing this file. Free tiers change often, so the tables give you what each tool is for, the kind of limit to expect, and the page to check, and they do not state quotas or prices I cannot confirm. The Verified column means:

- **2026-10-20 (snapshot)**: the specific fact named was in the research snapshot dated that day. Even then, re-check before relying.
- **Not verified**: the entry comes from general knowledge of the tool. VERIFY BEFORE RELYING on the page named.

"PAID TRAP" marks a place where free use ends in a way people miss: a watermark, a commercial-use ban, a locked export option, a credit system that expires, or a trial that bills automatically. "Commercial use" means using the tool's output in a monetized YouTube video.

Never download, rip, or scrape others' videos. Use the public watch page, the on-page transcript panel, public metadata, and the official YouTube Data API only. Folder [../01-channel-dna/01-data-gathering.md](../01-channel-dna/01-data-gathering.md) gives the exact steps.

## Tables by category

### 1. Research

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| YouTube watch page and channel page (browser) | Studying titles, thumbnails, upload cadence, video structure by watching | No limit beyond your time | None | Studying is allowed; copying expression is not (see [02-principles-and-copy-line.md](02-principles-and-copy-line.md)) | A notebook | 0 min | Not verified |
| YouTube Data API v3 | Reading public metadata (titles, stats, dates) via a script or sheet | Quota is 10,000 units per day for non-upload endpoints (shared pool) | None | Subject to YouTube API Services Terms; VERIFY BEFORE RELYING on developers.google.com/youtube/terms | Manual reading of public pages | 20 min | 2026-10-20 (snapshot, quota only) |
| Google Trends | Comparing search interest by region and time | Free; no account needed | None | Information source only | YouTube search autocomplete | 2 min | Not verified |
| YouTube search autocomplete | Finding phrases viewers type | Free | None | Information source only | Google autocomplete | 0 min | Not verified |
| YouTube Studio Research tab (own channel) | Seeing what viewers search for | Free with a YouTube channel; availability varies by channel and region | None | Information source only | Trends | 5 min | Not verified; check support.google.com/youtube |
| Google Sheets | Logging research and analysis | Free with a Google account; storage shared with Drive (15 GB shared pool) | None | Your data | LibreOffice Calc (free, local) | 2 min | Not verified |

### 2. Transcripts

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| YouTube on-page transcript panel | Reading a public video's transcript as analysis input only | Only where the creator or YouTube provides one | None | Analysis only; never publish or closely paraphrase | Watch and take notes | 1 min | 2026-10-20 (snapshot, method) |
| Whisper (OpenAI, open source) | Transcribing YOUR OWN recordings locally | Free; speed depends on [HARDWARE] | None | Open license (MIT as of my knowledge); VERIFY BEFORE RELYING on github.com/openai/whisper | YouTube Studio auto captions on your own uploads | 30 min | 2026-10-20 (snapshot, tool name only) |
| whisper.cpp | Faster Whisper on CPU-only PCs | Free; slower on low-end PCs | None | Open license; VERIFY BEFORE RELYING on its GitHub page | Whisper via Google Colab | 30 min | Not verified |
| YouTube Studio caption editor | Fixing auto captions on your uploads | Free | None | Your content | Subtitle Edit (open source, Windows) | 5 min | Not verified |

Do not use Whisper or any tool to transcribe other creators' downloaded video files. Use only the on-page panel for reference videos.

### 3. LLMs (script, analysis, prompts)

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| ChatGPT free | Prompts in this repo | Message caps and model access change; VERIFY BEFORE RELYING on chatgpt.com/pricing | None | OpenAI terms generally assign output to the user; VERIFY BEFORE RELYING | Gemini or Claude free | 2 min | Not verified |
| Google Gemini / AI Studio | Long inputs such as a full transcript | Daily caps; AI Studio free-tier data may be used to improve products. PAID TRAP: paid API tier changes the data terms. VERIFY BEFORE RELYING on ai.google.dev | None | Check Google terms; VERIFY BEFORE RELYING | Mistral Le Chat free | 5 min | Not verified |
| Claude free | Careful analysis and rewriting | Usage caps reset on a schedule; VERIFY BEFORE RELYING on claude.ai pricing page | None | Check Anthropic consumer terms; VERIFY BEFORE RELYING | Gemini | 2 min | Not verified |
| Mistral Le Chat | Backup chat model | Free tier with caps; VERIFY BEFORE RELYING | None | Check terms | Ollama local | 2 min | Not verified |
| Ollama with an open model | Offline drafts, privacy, bulk jobs on [HARDWARE] with enough RAM | Free; speed bound by hardware. Each model has its own license. PAID TRAP: none for the tool, but some models carry usage restrictions | None | Per model; read the model card for "commercial" | Free chat tiers above | 30 min | Not verified |

Never paste a competitor's transcript into a prompt and ask the model to rewrite it. Prompts in this repo ask for structure only.

### 4. Speech and voice

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| Your own voice + phone recorder | Highest-originality narration | Free | None | Yours | Phone voice memo app | 0 min | Not verified |
| Audacity | Noise removal, EQ, normalization of your recordings | Free, open source | None | Your output is yours | Free editor noise reduction | 10 min | Not verified |
| Kokoro TTS | Free text-to-speech, local | Free; needs a computer; Apache 2.0 license (verified 2026-10-20). Check the license of each voice pack | None | Apache 2.0 allows commercial use; disclosure rules still apply (see C-13) | Piper | 30 min | 2026-10-20 (snapshot, license) |
| Piper TTS | Lightweight TTS on low-end PCs | Free; each voice model has its own license. PAID TRAP: none, but a voice's license may forbid commercial use | None | Per voice; VERIFY BEFORE RELYING on each voice's model card | Device built-in TTS | 30 min | 2026-10-20 (snapshot, tool name only) |
| Android and Windows built-in TTS | Emergency fallback voice | Free | None | Terms vary; VERIFY BEFORE RELYING | Kokoro | 0 min | Not verified |
| ElevenLabs free tier | Hosted TTS | Free tier has monthly character limits. PAID TRAP: free-tier terms have historically required attribution or limited commercial use. VERIFY BEFORE RELYING on elevenlabs.io/pricing | Audio only; check terms | Not assumed allowed | Kokoro | 5 min | Not verified |
| Voice cloning tools | Cloning any real voice | Do not use. Cloning real people's voices violates this repo's rules (C-27) | n/a | n/a | Your own voice or Kokoro | n/a | n/a |

### 5. Image generation

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| ComfyUI + open image model | Local image generation | Free; needs a GPU for speed. PAID TRAP: some model licenses restrict commercial use or cap company revenue; read each model's license | None | Per model; read the model card | Free web generators below | 2 hours | 2026-10-20 (snapshot, ComfyUI listed) |
| Microsoft Copilot / Bing Image Creator | Quick web images | Daily boost or credit limits; VERIFY BEFORE RELYING on Microsoft's terms | Possible content credentials | VERIFY BEFORE RELYING | Gemini images | 5 min | Not verified |
| Google Gemini image generation | Web images in chat | Daily limits; VERIFY BEFORE RELYING | May embed a provenance mark | VERIFY BEFORE RELYING | Canva free | 5 min | Not verified |
| Canva free (Magic Media) | Images inside a design tool | Free plan caps AI use. PAID TRAP: "Pro" elements and some features need payment; Pro-only assets in a free export can trigger prompts or block download | Possible on Pro-only assets | Check Canva's content license; VERIFY BEFORE RELYING | Photopea + free stock | 5 min | Not verified |

Any image that looks like a real photo and shows something that did not happen needs disclosure (see C-12).

### 6. Video generation

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| Wan 2.2 (local) | Short generated clips | Free; Apache 2.0 (verified 2026-10-20); heavy GPU needed, not for low-end PCs | None | Apache 2.0 allows commercial use; disclosure rules still apply | Free web tiers below, or film your own | 3 hours | 2026-10-20 (snapshot) |
| LTX video models (local) | Short generated clips | Free to run; newer versions carry a revenue-based community license. PAID TRAP: revenue threshold can end free commercial use. VERIFY BEFORE RELYING on each model's license | None | Check the exact model version's license | Wan 2.2 | 3 hours | 2026-10-20 (snapshot, license caution) |
| Free web video generators (Kling, Luma, Runway, Pika class) | Few-second clips | Tiny credit pools, queue times; free tiers mostly add watermarks or limit commercial use (verified 2026-10-20) | Usually yes on free | Often restricted on free plans | Your own phone footage | 5 min | 2026-10-20 (snapshot, general pattern) |

Mass-generated clips stitched under text-to-speech is the high-risk pattern in Group A of the checklist. Use generated clips sparingly, as part of an original video.

### 7. Editing

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| DaVinci Resolve (free) | Full PC editor, color, audio | Free version lacks some Studio-only effects. PAID TRAP: "Studio" upgrade prompts; some AI tools are Studio-only | No watermark | Allowed for your own videos; VERIFY BEFORE RELYING on blackmagicdesign.com | Kdenlive | 1 hour | 2026-10-20 (snapshot, tool name only) |
| CapCut free | Phone and PC editing, captions, templates | PAID TRAP: some effects, templates, fonts, and export options are Pro-only. Its music library can have commercial-use limits. VERIFY BEFORE RELYING on capcut.com terms | Possible on some templates and effects | Per asset; read the label | DaVinci Resolve or Kdenlive | 10 min | 2026-10-20 (snapshot, tool name only) |
| Kdenlive | Open-source PC editor | Free | None | Allowed | Shotcut | 20 min | Not verified |
| Shotcut | Light open-source PC editor | Free | None | Allowed | OpenShot | 15 min | Not verified |
| Clipchamp free | Simple Windows editor | Export resolution and stock may be limited; VERIFY BEFORE RELYING | Check | Check | Shotcut | 10 min | Not verified |

### 8. Captions

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| YouTube Studio auto captions + editor | Captions on your own uploads | Free | None | Yours | Subtitle Edit | 5 min | Not verified |
| CapCut auto captions | Burned-in word-by-word captions | Auto-caption allowance can change. PAID TRAP: some caption styles are Pro | Possible | Per asset | Whisper plus Subtitle Edit | 5 min | Not verified |
| Whisper + Subtitle Edit | Local captions for your own recording | Free | None | Open licenses | YouTube Studio | 40 min | Not verified |

### 9. Thumbnails

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| Canva free | Layout and text | PAID TRAP: Pro elements, background remover, and brand kits are paid | On Pro-only assets if exported | Check Canva's content license | Photopea | 10 min | 2026-10-20 (snapshot, tool name only) |
| Photopea (browser) | Photoshop-style editing | Free with ads; VERIFY BEFORE RELYING | None | Your output is yours; assets are your responsibility | GIMP | 5 min | Not verified |
| GIMP | Local image editor | Free, open source | None | Allowed | Krita | 20 min | Not verified |
| Krita | Drawing and painting | Free, open source | None | Allowed | GIMP | 20 min | Not verified |
| Figma free | Layout, shared templates | Free plan has file and editor caps; VERIFY BEFORE RELYING | None | Your design | Canva | 15 min | Not verified |

### 10. Music and sound effects

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| YouTube Audio Library (in Studio) | Tracks and SFX for YouTube | Free; some tracks require attribution; read each track's label | None | Intended for YouTube videos; VERIFY BEFORE RELYING on its terms | Pixabay Music | 5 min | Not verified |
| Pixabay Music and Sound Effects | Tracks and SFX | Free; read the current Pixabay license. Tracks may still be registered by third parties. PAID TRAP: none | None | Generally allowed under its license; VERIFY BEFORE RELYING | Free Music Archive (per track) | 5 min | Not verified |
| Free Music Archive | Tracks with Creative Commons licenses | Per-track license. PAID TRAP: "NC" tracks are non-commercial and fail C-09 | None | Only CC licenses that allow commercial use | YouTube Audio Library | 10 min | Not verified |
| Incompetech | Royalty-free music with attribution | Free with credit; paid license removes the credit requirement | None | Allowed with attribution; VERIFY BEFORE RELYING | Pixabay | 5 min | Not verified |
| Freesound | Sound effects | Per-file CC license. PAID TRAP: some files are CC BY-NC | None | Only files whose license allows commercial use | Pixabay SFX | 10 min | Not verified |
| AI music generators (free tiers) | Generating tracks | Often non-commercial on free plans. VERIFY BEFORE RELYING on each service's terms | Possible | Often not allowed | YouTube Audio Library | 5 min | Not verified |

### 11. Stock footage and images

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| Pexels | Photos and video | Free | None | Pexels license generally allows commercial use with restrictions (for example on identifiable people and on selling unaltered files); VERIFY BEFORE RELYING | Pixabay | 5 min | Not verified |
| Pixabay | Photos and video | Free | None | Pixabay license generally allows commercial use; VERIFY BEFORE RELYING | Pexels | 5 min | Not verified |
| Coverr and Mixkit | Short video clips | Free | None | Check each site's license | Pexels | 5 min | Not verified |
| Wikimedia Commons | Images and some video | Free; license varies per file. PAID TRAP: share-alike files can require your video to carry the same license | None | Per file; check the file page | Pexels | 10 min | Not verified |
| Your own filming | Original footage | Free | None | Yours | Phone camera | 0 min | Not verified |

Stock-only videos with text-to-speech fall into the high-risk pattern. Use stock as support for your own material, not as the whole video.

### 12. Scheduling

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| YouTube Studio scheduling | Setting publish date and time | Free, built in | None | n/a | Manual publish | 2 min | 2026-10-20 (snapshot; design ends in Studio publishing) |
| Google Calendar | Production schedule | Free | None | n/a | Phone calendar | 2 min | Not verified |
| Trello or Notion free | Task boards | Free plans have caps; VERIFY BEFORE RELYING | None | n/a | Google Sheets | 10 min | Not verified |

### 13. Analytics

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| YouTube Studio Analytics | Retention, CTR, traffic sources of your own videos | Free | None | n/a | Google Sheets log | 5 min | Not verified |
| YouTube Analytics API | Pulling your own stats into a sheet | Within the API quota (see Research); VERIFY BEFORE RELYING | None | Subject to API Terms | Manual export | 30 min | 2026-10-20 (snapshot, quota) |
| Looker Studio | Dashboards from Sheets | Free | None | n/a | Sheets charts | 20 min | Not verified |

### 14. Automation

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| n8n (self-hosted) | Workflows linking sheets, LLMs, files | Free to self-host; needs a computer or server that stays on. PAID TRAP: n8n Cloud is paid; the license is source-available, not open-source; VERIFY BEFORE RELYING on n8n's license page | None | Check license for your use | Google Apps Script | 2 hours | 2026-10-20 (snapshot) |
| GitHub Actions | Scheduled scripts | Free minutes allowance for repositories; limits differ for private repositories; VERIFY BEFORE RELYING on GitHub Docs "Billing" | None | Terms apply | Local cron job | 1 hour | 2026-10-20 (snapshot, free minutes) |
| Google Sheets + Apps Script | Sheet-based automation | Daily quotas apply; VERIFY BEFORE RELYING on Apps Script quotas page | None | Google terms | n8n | 1 hour | 2026-10-20 (snapshot) |
| Zapier or Make free plans | Simple no-code flows | Small task allowances. PAID TRAP: auto-upgrade prompts and multi-step flows may need paid plans; VERIFY BEFORE RELYING | None | Terms apply | n8n | 20 min | Not verified |

Auto-publishing through the YouTube Data API is limited: videos.insert from an unaudited API project created after 28 July 2020 is locked private until the project passes a compliance audit, and the default bucket is about 100 videos.insert calls per day (verified 2026-10-20). This repo ends automation in human review plus manual or Studio-scheduled publishing. See [../06-automation/07-youtube-api-and-audit.md](../06-automation/07-youtube-api-and-audit.md).

### 15. Hosting and compute

| Tool | What for | Real free limits | Watermark | Commercial-use status | Free fallback | Setup time | Verified |
|---|---|---|---|---|---|---|---|
| GitHub (private or public repo) | Storing this repo, scripts, templates | Free plan limits apply; VERIFY BEFORE RELYING | None | n/a | Local folder plus Drive | 10 min | Not verified |
| Google Drive | Storing files | 15 GB shared with Gmail and Photos (as of my knowledge; VERIFY BEFORE RELYING) | None | n/a | Local disk | 2 min | Not verified |
| Google Colab free | Running Whisper or small models without a local GPU | GPU not guaranteed; sessions time out; usage caps change. VERIFY BEFORE RELYING on Colab's FAQ | None | Check Colab terms for your workload | Local CPU runs | 15 min | Not verified |
| Cloudflare Pages / Workers free | Hosting small web tools or APIs | Free plan limits apply; VERIFY BEFORE RELYING | None | Check terms | GitHub Pages | 30 min | Not verified |
| Hugging Face Spaces (free CPU) | Hosting small demos | Free hardware is limited and sleeps; VERIFY BEFORE RELYING | None | Check terms and each model's license | Local run | 30 min | Not verified |

## Best $0 starter stack by [HARDWARE]

### Phone only

- Research: YouTube app and browser, Google Sheets on phone.
- LLM: one free chat app (ChatGPT, Gemini, or Claude).
- Voice: your own voice, recorded with the phone voice memo app in a quiet room (closet with clothes works).
- Visuals: your own phone footage plus Pexels or Pixabay as support.
- Editing and captions: CapCut free, avoiding Pro-only items.
- Thumbnails: Canva free or Photopea in the phone browser.
- Music: YouTube Audio Library or Pixabay.
- Publishing: YouTube Studio app.
- Skip: local Whisper, Kokoro, Wan, ComfyUI.

### Low-end PC (8 GB RAM, no dedicated GPU)

- Research: browser, Google Sheets, Google Trends.
- LLM: free chat tiers; Ollama only with a small model and patience.
- Voice: your own voice with Audacity; Kokoro or Piper if you must use TTS. Check C-13.
- Visuals: your own footage plus stock; Canva or Photopea.
- Editing: DaVinci Resolve free if the machine runs it smoothly; otherwise Kdenlive or Shotcut.
- Captions: YouTube Studio auto captions plus editor, or whisper.cpp for your own audio.
- Automation: Google Sheets with Apps Script first; n8n only if the PC can stay on.
- Skip: Wan 2.2, LTX, ComfyUI image models. They need a strong GPU.

### Strong GPU

- Everything above, plus ComfyUI with an open image model whose license allows commercial use.
- Wan 2.2 for short generated clips; check LTX versions' license (revenue threshold).
- Local Whisper for your recordings; Ollama for private bulk drafting.
- Keep human footage or analysis at the center (C-01, C-03). A GPU lets you generate more, and the originality gate still applies.

## How to re-verify a tool's free tier in 5 minutes

1. **Open the pricing page (1 minute).** Note what the free plan includes and excludes. Copy the exact line about commercial use if there is one.
2. **Open the terms page (2 minutes).** Use your browser's find function (Ctrl+F) on the page and search for: `commercial`, `watermark`, `attribution`, `non-commercial`, `revenue`, `training`. Read each hit.
3. **Test one export (1 minute).** Make a 5-second test file with the free plan. Look at all four corners for a watermark and check the file format and resolution.
4. **Log it (1 minute).** Add a row to the license log: tool, plan, date, license wording copied, screenshot saved.
5. **Decide.** Pass if commercial use is allowed, there is no watermark, and no paid trap applies to your use. Otherwise switch to the fallback column.

Repeat every 90 days and whenever the tool sends a terms-change email.

## Prompts

### P-START-04 — Free-Tier Re-Verification Worksheet

**Purpose:** Produce a verification checklist for the tools in your stack, then fill it from official pages.

**Inputs:** [HARDWARE], [VOICE_MODE], [FACE_OR_FACELESS], and [TOOL_LIST] (the tools you plan to use, one per line). Use a chat tool that has web search turned on.

```text
You are helping me verify free tiers before I rely on tools for monetized YouTube videos. My hardware: [HARDWARE]. Format: [FACE_OR_FACELESS]. Voice mode: [VOICE_MODE].

Tools to verify:
[TOOL_LIST]

For each tool, search the tool's official pricing page and official terms page (not blogs or review sites). Then output a table with columns: Tool, Official pricing URL, Official terms URL, Free limits (exact numbers as written on the page, or "not stated"), Watermark on free exports (Yes / No / Not stated), Commercial use of output allowed on the free plan (Yes / No / Not stated, with the exact sentence in quotation marks, under 20 words), Attribution required, Paid trap (one sentence), Date you checked, Confidence (High if both official pages were read, Low otherwise).

Rules: Do not guess. If a page cannot be opened or a fact is not stated, write VERIFY BEFORE RELYING and name the exact page I should open. Do not use numbers from memory. After the table, list any tool whose commercial-use answer is No or Not stated and name its free fallback from my list.
```

**Expected output:** A table with URLs, exact free limits, watermark and commercial-use status, trap notes, dates, and confidence.

**If the output is weak:** Run one tool per message and add "Open the pricing page first and quote the first paragraph about the free plan." If search is not available, do the manual 5-minute routine above.

## Done when

- You have chosen one starter stack and written the tool names in your notes.
- Each tool you will use has a row in your license log with commercial-use wording, a screenshot, and a date.
- You produced one test export from each editing and thumbnail tool and confirmed no watermark.
- Every tool with a paid trap has a named free fallback.

## Next

[../01-channel-dna/01-data-gathering.md](../01-channel-dna/01-data-gathering.md)
