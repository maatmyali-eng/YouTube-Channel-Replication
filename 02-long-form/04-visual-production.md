# Visual Production (Long-Form)

> **Purpose:** Build the shot list, source or make the visuals, edit in a free editor, add captions, and avoid the "slideshow with TTS" pattern.
> **Use when:** You have the final voice track and the script.
> **Time needed:** 3 to 6 hours for a 10-minute video at first; 1.5 to 3 hours with practice.
> **Needs:** `voice.wav`, final script, DaVinci Resolve (free) or CapCut (free), a phone camera or screen recorder.
> **Cost:** $0

## Inputs

- [FACE_OR_FACELESS], [HARDWARE], [WEEKLY_HOURS], [VIDEO_LENGTH], [LANGUAGE], [STYLE_BIBLE] (visual and editing sections).
- The final script ([SCRIPT_V3] from `03-voice-and-audio.md`) and the visual-logic section of the DNA report (section 6 of P-LONG-01).
- [OWNER_ASSETS] from `02-script-prompt-chain.md`.
- Defined here: [DNA_VISUALS] (section 6 of your video DNA report) and [SHOT_LIST] (the output of P-LONG-12).

## Steps

1. **Run P-LONG-12** to get a shot list. Read the column "Source" first. At least 40 percent of runtime should come from visuals you captured or made yourself (your screen, your camera, your own graphics, your own animation). This is this repo's own threshold, not a YouTube figure. It exists because the three non-monetizable categories in YouTube's July 2026 clarification include generic, repetitive, template-based content, and faceless stock-plus-TTS formats are the highest-risk pattern (verified 2026-10-20).
2. **Choose sourcing by [FACE_OR_FACELESS].**

   **Face (on camera).** Use a phone on a tripod or a stack of books at eye level, 1080p, 30 fps (or 24 fps, but keep one setting per channel). Face a window for soft light; never put the window behind you. Record voice with the method in `03-voice-and-audio.md` instead of the camera microphone when possible, and sync with your clap. Cut to your own screen, hands, or objects for every demonstration.

   **Faceless.** Your original value must come through demonstration. Plan for three visual layers: (a) your own screen capture or your own hands and objects, (b) original graphics (charts, diagrams, lists you draw), (c) limited licensed stock or AI visuals only to bridge gaps. Never build a video entirely from layer (c).
3. **Know your free sources.** Check each license at the time of use and log it in `visuals-log.csv` with the same columns as the music log (replace "music" with "visual").

| Source | Free limits | Commercial use / watermark | Trap | Free fallback |
|---|---|---|---|---|
| Your own phone camera or screen recording | None | Yours | Showing other people's faces, private data, or trademarks without need | Re-record |
| OBS Studio (screen capture) | None | Open source, no watermark | Capturing DRM streams or windows with private info | Resolve screen-record alternative: your OS's built-in recorder |
| Pexels and Pixabay video and photos | Free downloads | Own license pages; typically no attribution, but terms exclude implying endorsement and some uses; read each current license | Clips with recognizable people, logos, or artwork may carry extra restrictions; the same clip appears in thousands of videos | Shoot your own B-roll |
| Wikimedia Commons | Free | License differs per file (public domain, CC BY, CC BY-SA) | Missing attribution; ShareAlike conditions | Use public domain or CC0 only |
| Canva free | Free plan | Check Canva's current license terms for free elements; some elements are Pro-only | Pro-only elements added to a design block export or add a watermark | Inkscape or Krita (free) for your own graphics |
| Blender or Fusion (inside Resolve) | None | No watermark | Learning curve | Simple moves and text animation in the editor |
| AI image or video generators (free tiers) | Tight daily credits | Often watermarked or limited commercial use; terms change | Realistic output needs the **Altered content** label if it could be mistaken for real | Draw your own diagram |

   Terms in this table that are not marked as verified: VERIFY BEFORE RELYING on each service's current license page.
4. **Use your own screen as the default visual.** Install OBS Studio (free). Add a **Display Capture** or **Window Capture** source, set **Settings > Output > Recording Quality** to **High Quality, Medium File Size**, **Recording Format** to **mkv** (safer if it crashes), then in **File > Remux Recordings** convert to mp4. Hide notifications and personal tabs first.
5. **Set up the editor. DaVinci Resolve (recommended).** The free edition has no watermark and no time limit and exports up to UHD 4K at 60 fps; its AI features (Magic Mask, Voice Isolation, Speed Warp, text-based editing and others) are Studio-only, so do not plan around them (verified 2026-10-20). Steps:
   1. **File > New Project**, name it after the video slug.
   2. **File > Project Settings > Master Settings**: Timeline resolution **1920 x 1080 HD**, timeline frame rate to match your footage (24 or 30), **Playback frame rate** the same.
   3. **Media** page > **File > Import Media**: voice, footage, graphics, music.
   4. **Edit** page: drag `voice.wav` to Audio 1 first. This is the master timeline; every visual follows the voice.
   5. Lay in visuals one sentence at a time using the shot list. Use **Blade** (B key) to cut and **Ripple Delete** to close gaps.
   6. Add music to Audio 3 and sound effects to Audio 4. Keyframe music level to duck under speech.
   7. Fairlight page (audio) for the loudness check; see `03-voice-and-audio.md`.

   **CapCut (alternative).** Free-plan limits changed in the 2026 plan restructure and sources disagree: some report no watermark on standard exports with a watermark only on Pro-tagged templates and effects, others report a 1080p export cap, others a watermark on all free exports, and auto-caption limits per video. Before you spend a day on CapCut, export a 10-second test with the effects you plan to use and check the result. VERIFY BEFORE RELYING at CapCut's official pricing page. Desktop path: **New project > Import**, drag clips to the timeline, **Text > Auto captions > Generate** (if offered on your plan), **Export** (top right): set resolution, frame rate, format MP4.
6. **Pacing rules.** Use the average shot length and cut frequency from your DNA report (section 6) as the target. If you have no report, use these starting values for talking-explainer videos: a new visual or a visible change at least every 4 to 8 seconds; no static image held longer than 10 seconds unless the viewer is reading or watching something happen on it; one visual change tied to each new idea, not to the clock.
7. **B-roll rules.**
   - Every B-roll clip must show what the sentence says or prove it. If a clip is only decoration, delete it.
   - Show process as it happens (hands doing it, screen showing it) rather than a stock image of the topic.
   - Do not use other creators' clips, thumbnails, screenshots of their videos, TV, film, or game footage unless you hold a licence or the permission is written down.
   - Blur or crop private details, license plates, and unrelated people.
   - Use the same grade (color correction) and the same lower-third and text style on all clips so the video looks like one piece.
8. **Captions.**
   1. Export the voice to WAV. Free local option: Whisper (open-source, MIT license). In a terminal: `pip install openai-whisper`, then `whisper voice.wav --model small --language en --output_format srt` (change the language code to match [LANGUAGE]; model names and options change, so VERIFY BEFORE RELYING by running `whisper --help`). Resolve's own **Timeline > Create Subtitles from Audio** may or may not be in the free edition on your version: VERIFY BEFORE RELYING.
   2. Open the SRT in a text editor and correct names, numbers, and technical terms. Your script is the source of truth; paste corrections from it.
   3. Upload as a separate caption file: **YouTube Studio > Subtitles > Add language > Add under Subtitles > Upload file > With timing**. YouTube's own auto-captions are free as a fallback; review and fix them under the same menu.
   4. Burned-in text only for emphasis words and key numbers, large enough to read on a phone, inside the safe margin (keep all text inside the inner 90 percent of the frame).
9. **Avoid the slideshow-with-TTS pattern.** Run the **Slideshow Test** on your rough cut:
   1. **Mute test.** Watch two minutes with the sound off. Does the picture alone show something happening (steps, results, a person, a process)? If it only shows a series of still images, fail.
   2. **Sameness test.** Count how many different visual types appear (own capture, own footage, diagram, text card, animation, stock). Fewer than three in a 10-minute video, fail.
   3. **Support test.** Pick 10 random seconds. Does the visual prove or explain the sentence being spoken? Fail if it only relates by mood.
   4. **Template test.** Place this video's first two minutes beside your last video's first two minutes. If layout, pacing, transitions, and the structure of the first 30 seconds look the same, vary them.
   5. **Value test.** List the original-value items from the outline (see `02-script-prompt-chain.md`). Is each one visible on screen, with your own visuals? Fail if any exists only in narration and could be shown.
   Run P-LONG-13 for a written audit.
10. **Export.** Resolve: **Deliver** page. In **Render Settings**, choose the **YouTube** preset and the **1080p** variant if listed, or set Format **MP4**, Codec **H.264**, resolution 1920 x 1080, frame rate equal to your timeline. Audio: Codec **AAC**, Bitrate **320 kbps** (or the highest offered). Set **File Name** and **Location**, click **Add to Render Queue**, then **Render All**. YouTube lists recommended upload bitrates on its Help page "Recommended upload encoding settings"; VERIFY BEFORE RELYING and match them. Reopen the exported file and watch the first minute, the middle, and the last 20 seconds before moving on.
11. **Plan the last 20 seconds** with an end screen in mind: YouTube end screens can be added to the last 5 to 20 seconds, and the video must be at least 25 seconds long (verified 2026-10-20). Leave the end area visually clean.

## Prompts

### P-LONG-12 — Shot List

**Purpose:** Produce a shot-by-shot plan with source, instructions, and licence needs, matched to how you actually produce.

**Inputs:** [SCRIPT_V3], [STYLE_BIBLE], [FACE_OR_FACELESS], [HARDWARE], [WEEKLY_HOURS], [OWNER_ASSETS], [DNA_VISUALS], [VIDEO_LENGTH].

```
You are a video producer planning visuals for one YouTube video. Script: [SCRIPT_V3]
Length: [VIDEO_LENGTH]. Presentation: [FACE_OR_FACELESS]. My equipment: [HARDWARE]. Production time available per week: [WEEKLY_HOURS] hours.
Style Bible visual rules: [STYLE_BIBLE]
Visual logic observed in the modelled channel (mechanics only; do not copy its content): [DNA_VISUALS]
What I can truly show on camera or screen: [OWNER_ASSETS]

OUTPUT A: SHOT LIST TABLE, one row per shot, covering the whole runtime with no gaps. Columns: Shot # | Timecode | The narration line (first 8 words) | Shot type | Source (OWN SCREEN, OWN FOOTAGE, ORIGINAL GRAPHIC, ANIMATION, LICENSED STOCK, AI-GENERATED) | Exact instruction to create it or exact search words to find it | Duration in seconds | Licence proof needed (yes/no and what) | Production minutes estimated.
Rules: no shot longer than 10 seconds without a stated reason; every visual must show or prove what is said; each shot's source must be something I can actually make with the equipment and assets I listed; never propose using another creator's footage, music, thumbnails, or characters; any AI-generated shot that looks realistic must be marked "DISCLOSE: Altered content = Yes".
OUTPUT B: SOURCE MIX. Percent of runtime for each source type. OWN SCREEN + OWN FOOTAGE + ORIGINAL GRAPHIC + ANIMATION must total at least 40 percent. If your plan falls short, revise the list until it does, and say what you changed.
OUTPUT C: PRODUCTION ORDER. The order in which to capture or make things efficiently (batch all screen recordings together, then graphics, then stock search), with total estimated hours versus my weekly hours.
OUTPUT D: RISK FLAGS. Shots with licence, privacy, trademark, or realism concerns, each with a safer alternative.
OUTPUT E: GRAPHICS LIST. Each original graphic to be made, with its text content and dimensions (1920 x 1080 unless a different size is needed).
```

**Expected output:** A full shot table, a source mix summary, a batching order, risk flags, and a graphics list.

**If the output is weak:** Reply: "Rewrite the shot list so every shot's source is one I can produce with the equipment I listed, and recompute the source mix." If it names unrealistic AI shots, reply: "Replace each AI-generated shot with an own-screen or original-graphic shot."

### P-LONG-13 — Slideshow and Template Risk Audit

**Purpose:** Judge a rough cut against the repetition and low-effort patterns that put monetization at risk.

**Inputs:** [ROUGH_CUT_NOTES] (a minute-by-minute description of what is on screen; or [SHOT_LIST]), [SCRIPT_V3], [PREVIOUS_VIDEO_NOTES] (the same description for your last two videos, or "none"), [OWNER_ASSETS].

```
Audit this video plan for the pattern YouTube treats as generic, repetitive, or template-based content, and for "slideshow with narration" structure.
What is on screen, minute by minute: [ROUGH_CUT_NOTES]
Script: [SCRIPT_V3]
My previous videos' structure and visuals: [PREVIOUS_VIDEO_NOTES]
What is genuinely mine: [OWNER_ASSETS]

OUTPUT
1. A table with the five tests: Mute test, Sameness test, Support test, Template test, Value test. For each: PASS or FAIL, evidence from my notes, and one specific fix.
2. A list of every segment longer than 10 seconds that shows only a still image or generic stock, with a replacement visual I could make myself.
3. A comparison with my previous videos: which structural and visual elements repeat exactly, and two variations that keep the Style Bible's identity while changing the pattern.
4. Realistic-content check: which visuals could a viewer mistake for real footage of real events or people; mark each "Altered content: Yes".
5. VERDICT: GO, FIX, or STOP, with the minimum list of changes to reach GO.
Be specific and critical. Do not praise. Do not suggest hiding AI use or evading detection.
```

**Expected output:** Five tests, a list of weak segments, a variation plan, a realism check, and a verdict.

**If the output is weak:** Add more detail to [ROUGH_CUT_NOTES] (one line per 10 to 15 seconds) and rerun.

## Done when

- [ ] Shot list exists and the own-visuals share is 40 percent or more.
- [ ] `visuals-log.csv` lists every stock, graphic, or AI visual with a licence URL and screenshot.
- [ ] The rough cut passes all five tests in Step 9.
- [ ] Captions are corrected against the script and uploaded as an SRT, or reviewed auto-captions are published.
- [ ] The exported video plays correctly from start to end, and the last 20 seconds are clear for an end screen.
- [ ] Realistic AI visuals, if any, are marked for the Altered content setting.

## Next

Continue to [05-metadata-and-seo.md](05-metadata-and-seo.md).
