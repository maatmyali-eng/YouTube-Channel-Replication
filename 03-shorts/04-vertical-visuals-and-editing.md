# Vertical Visuals and Editing in Free Tools

> **Purpose:** Film, edit, caption, mix, and export a Short in 1080 x 1920 using only free tools, with safe zones, caption templates, a music decision, and a batch routine.
> **Use when:** You have an approved script table from `02-script-prompt-chain.md` or `03-batch-scripts.md`.
> **Time needed:** 60 to 120 minutes per Short at first, less once the template project exists.
> **Needs:** A phone with a camera, a computer, DaVinci Resolve (free), Python with Pillow (optional), a free AI chat assistant.
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [FACE_OR_FACELESS], [VOICE_MODE], [HARDWARE], [WEEKLY_HOURS], [STYLE_BIBLE], [SHORTS_DNA] from earlier files.
- The script table for each Short (`shorts/<slug>/script.md`).
- [OWNER_ASSETS] for the proof shots.
- Prompt-specific placeholders: [SCRIPT_TABLE], [SAFE_ZONE_RULE] (the rule in Step 4), [CAPTION_TEMPLATE] (T1, T2, or T3 from Step 7).

## Steps

1. **Create the folders.** For each Short: `shorts/<slug>/footage/`, `audio/`, `captions/`, `exports/`, `proof/`. In the repo root keep `visuals-log.csv` and `music-log.csv`, the same files used by long-form. If they do not exist, create them with these headers (if your existing files use other columns, keep yours and record the same information):

```csv
asset_id,short_slug,what_it_is,source,maker_or_url,license_or_terms,date_checked,commercial_ok,own_or_free_or_ai
```

```csv
track_id,short_slug,title,source,url,license_or_terms,attribution_text,date_checked,safe_for_over_60s
```

2. **Choose your editor.** All free, all checked for the four things you need to know.

| Tool | Free limits | Watermark and commercial status | Paid trap | Free fallback |
|---|---|---|---|---|
| DaVinci Resolve (free) | Full editor, no time limit. Some Studio-only effects and AI features are missing (VERIFY BEFORE RELYING for auto-subtitles on the Blackmagic Design site). | No watermark. Your own exports are yours. | Resolve Studio is a paid upgrade you do not need for this repo. | Kdenlive or Shotcut |
| YouTube app Shorts camera and editor | Free, basic trimming, text, and the Sound picker. | No watermark. Sounds from the Shorts picker are licensed for use in Shorts (verified 2026-10-20) and cannot be exported. | None. | Resolve |
| CapCut (free) | Sources in October 2026 disagree on watermarks, the export cap (1080p), and caption limits. | VERIFY BEFORE RELYING on CapCut's own pricing and terms pages. Read the content license in its terms before you upload footage you cannot share. | Pro and Standard subscriptions auto-renew. | Resolve |
| Canva (free) | Free video editor with limits on premium elements. VERIFY BEFORE RELYING. | Elements marked premium cannot be exported cleanly on the free plan. Check each asset's license. | Canva Pro subscription. | Resolve |
| Kdenlive, Shotcut | Open-source editors, no watermark, no limits. | Free software licenses (check each project's site). | None. | Resolve |

   This repo uses Resolve in the steps below. If you use another editor, keep the same numbers (1080 x 1920, 30 fps, margins, caption specs).

3. **Set up the vertical project in Resolve.**
   - Open Resolve > Project Manager > New Project > name it `shorts-template`.
   - Click the gear icon (Project Settings) at the lower right > Master Settings > Timeline resolution: choose Custom, set 1080 x 1920 (tick "Use vertical resolution" if your version shows it). Timeline frame rate 30. Playback frame rate 30.
   - Same window > Image Scaling > Mismatched resolution files: Scale full frame with crop. Click Save.
   - Menu names change between Resolve versions. If one is missing, VERIFY BEFORE RELYING on the Resolve manual for your version.

4. **Apply the safe-zone rule.** YouTube's Shorts interface covers part of the frame (title, subscribe button, action column, description). The vendors who measure it disagree: top margin 241 to 288 px, bottom margin from about 300 to 672 px, right margin from 48 to 201 px on a 1080 x 1920 frame (checked 2026-10-20 across five tool vendors, none is an official YouTube spec for organic Shorts, so VERIFY BEFORE RELYING by previewing on your own phone). This repo uses the safe overlap of all of them:

   **[SAFE_ZONE_RULE]: keep every face, caption, text, and key object inside x from 60 to 880 and y from 290 to 1440. Keep the most important caption line above y = 1248.**

   Make an overlay so you can see this while editing. Save this file as `safezone-overlay.py`, run `pip install pillow` once, then run `python safezone-overlay.py`:

```python
from PIL import Image, ImageDraw
W, H = 1080, 1920
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
red = (255, 0, 0, 90)
d.rectangle([0, 0, W, 290], fill=red)
d.rectangle([0, 1440, W, H], fill=red)
d.rectangle([0, 0, 60, H], fill=red)
d.rectangle([880, 0, W, H], fill=red)
d.rectangle([0, 1248, W, 1440], fill=(255, 160, 0, 70))
img.save("safezone-overlay.png")
```

   In Resolve, Media page > Import Media > pick `safezone-overlay.png`. On the Edit page drag it to track V3 above everything and stretch it to the full length. Before exporting, click it and press `D` to disable it. If you do not use Python, set Resolve's View > Safe Area overlay as a rough guide and verify on your phone in Step 12.

5. **Film vertical.** Hold the phone vertical. Set the camera to 1080p at 30 fps (iPhone: Settings > Camera > Record Video; Android: camera app > video settings). Film every proof shot from the plan. Record 1 extra second before and after each action. Record 10 seconds of silence in your room for noise reference. If [HARDWARE] has no tripod, rest the phone against a stack of books. Never film a screen showing someone else's video.

6. **Match visuals to formats.** This repo rule is that at least 50 percent of the seconds in every Short show something you filmed, recorded, drew, or built yourself. The rest may be your own text cards or licensed free assets (logged in `visuals-log.csv`).

| Format | How to produce it for free |
|---|---|
| Overhead hands | Phone on a stack of books or a tripod, light from a window |
| Macro close-up | Phone 10 to 15 cm from the subject; tap to focus; good light |
| Screen recording | Windows: Xbox Game Bar (Win + G). Mac: Shift + Command + 5. Your own screen only |
| Split screen | In Resolve, place two clips on V1 and V2, use Inspector > Cropping and Position to give each half the frame |
| Text card plus footage | Resolve Effects > Titles > Text+ over your own footage |
| Own drawings | Draw on paper, photograph it, import it |
| AI-generated visuals | Allowed for abstract, clearly unrealistic imagery only. Never realistic fake people, places, or events. Follow [../02-long-form/04-visual-production.md](../02-long-form/04-visual-production.md) for tools, limits, and licenses, and read the disclosure table in [../02-long-form/03-voice-and-audio.md](../02-long-form/03-voice-and-audio.md) |

7. **Edit to the table.** Import the footage. Cut to the beat timings in `script.md`. Rules: the first frame is the hook frame, so start on the action with no black or logo; stay inside the cut-rhythm range given in your [SHORTS_DNA] block; put one change of picture, angle, or zoom at every new information beat; trim silence at the head and tail of the final audio to zero so the loop has no gap. For a punch-in, select the clip on the Edit page, open Inspector > Transform, keyframe Zoom from 1.00 to 1.12 over the beat.

   **Caption templates.** Use one per Short and rotate across a batch (rule R7 spirit). Fonts below are free for commercial use under the SIL Open Font License on Google Fonts (VERIFY BEFORE RELYING on each font page).

| Template | Use for | Words on screen | Font and size | Colors | Position | Motion |
|---|---|---|---|---|---|---|
| T1 Phrase | Most explainers | 3 to 6 words, 2 lines maximum | Montserrat Bold, 66 px | Text #FFFFFF, outline #000000 6 px | Centered, bottom edge of the block at y = 1240 | Hard cut on and off |
| T2 Highlight | Fast demos | One short phrase, the spoken word highlighted | Poppins ExtraBold, 72 px | Text #FFFFFF, highlight #FFD400, outline #000000 6 px | Same as T1 | Highlight moves word by word |
| T3 Keyword | Calm or sparse styles | 1 to 3 words at key beats only | Inter Bold, 84 px | Text #FFFFFF, shadow black 50 percent | Block centered at y = 1000 | 0.15 second scale from 90 to 100 percent |

   Create captions in Resolve: write your SRT (P-SHORT-07 below makes one), then File > Import > Subtitle, drop it on a subtitle track on the Edit page, select the track, and style it in the Inspector (font, size, position). To burn them in, use Deliver page > Subtitle Settings > Export Subtitle, Format: Burn into video (menu names VERIFY BEFORE RELYING). Without SRT import, build captions with Effects > Titles > Text+ per phrase. Captions repeat the voice or add a new fact. They never contradict it.

8. **Handle the audio.** Record the voice at 15 cm from a phone microphone in a carpeted, quiet room, or generate it with the free options in [../02-long-form/03-voice-and-audio.md](../02-long-form/03-voice-and-audio.md). Cut breaths that distract, keep natural pauses of 0.2 seconds. Targets: voice around -14 LUFS with peaks below -1 dBTP (a widely used convention, YouTube publishes no official number, VERIFY BEFORE RELYING). Without a meter, set the voice so peaks sit near -6 dB on Resolve's mixer. Put music 15 to 20 dB below the voice (practitioner guideline) and lower it further under every spoken line. Use sound effects only as punctuation at a cut.

9. **Decide the music.** This repo's rule: music is never required.

| Option | Rule | Safe for Shorts over 60 s? |
|---|---|---|
| A. No music | Own voice plus natural sound plus effects you recorded | Yes |
| B. YouTube Audio Library | In YouTube Studio open Audio Library. YouTube states that only music and sound effects from this library are known to it to be copyright-safe (verified 2026-10-20). Some tracks need attribution in the description. Log each in `music-log.csv`. | Yes |
| C. Sound picker in the YouTube app | Add the sound in the app after you upload. YouTube Shorts licensing covers sounds chosen through its own tools and they are not portable into Resolve (verified 2026-10-20). | VERIFY BEFORE RELYING on the Help page "Shorts monetization policies" and its music eligibility link. |
| D. Music you made or own | Keep proof (project files, stems). | Yes |
| E. Other royalty-free libraries | A "no copyright" label does not mean YouTube treats it as cleared. VERIFY BEFORE RELYING on each library's license and Content ID statement. | No. Treat as risky. |

   Never use popular songs, TikTok sounds, audio ripped from any video, or the Remix feature to build original-style Shorts. A Short longer than 1 minute that contains claimed content is blocked and not eligible for monetization (verified 2026-10-20, YouTube "Shorts monetization policies"). Under 60 seconds a claim may still hurt monetization or reach depending on the rights holder (VERIFY BEFORE RELYING). Every music choice goes into `music-log.csv`.

10. **Export.** Deliver page > Format MP4 > Codec H.264 > Resolution 1080 x 1920 > Frame rate 30 > Quality: Restrict to 10000 Kb/s (YouTube's published 1080p guidance is about 8 Mbps, VERIFY BEFORE RELYING) > Audio codec AAC. Choose a file name and location (`shorts/<slug>/exports/<slug>.mp4`) > Add to Render Queue > Render All. Confirm in the file's properties that it is vertical and 3 minutes or less so YouTube treats it as a Short.

11. **Run the batch routine** when you have several scripts. Sequence matters because each setup takes time once:
   1. Film all proof shots for the whole batch grouped by setting (all stove shots, all fridge shots).
   2. Record all voiceovers in one session, then trim each file.
   3. In Resolve right-click the `shorts-template` timeline > Duplicate Timeline for each Short. The template holds only technical settings and the caption styles. Each Short still gets its own visual format, rhythm, and wording from the plan.
   4. Edit all Shorts to the table, then add captions, then mix.
   5. Export with Add to Render Queue for all, then Render All.
   6. Watch every export on your phone before you upload it.
   Estimate capacity from [WEEKLY_HOURS] divided by your measured hours per Short. Start with 2 hours per Short as an assumption and replace it with your real time after the first batch.

12. **Check on a phone.** Upload the export as Unlisted from YouTube Studio > Create > Upload videos (menu names VERIFY BEFORE RELYING). Open it in the YouTube app on a phone. Expand the description. If any caption or key object is covered, fix the safe-zone margin and re-export.

13. **Log the assets.** Fill `visuals-log.csv` and `music-log.csv` for every non-owned asset. Check disclosure and sensitive-topic rules as in `02-script-prompt-chain.md` Step 9.

## Prompts

### P-SHORT-07 — Vertical Shot List, Caption File, and Asset Log

**Purpose:** Turn a script table into a filming list, a ready-to-import SRT caption file, and log rows.
**Inputs:** [SCRIPT_TABLE], [FACE_OR_FACELESS], [HARDWARE], [OWNER_ASSETS], [SHORTS_DNA], [SAFE_ZONE_RULE] (paste the bold rule from Step 4), [CAPTION_TEMPLATE] (T1, T2, or T3).

```
You are a short-form video producer. Work from the script table below for one YouTube Short. The channel is [FACE_OR_FACELESS]. Equipment: [HARDWARE]. Things I can film or show: [OWNER_ASSETS]. Style rules: [SHORTS_DNA].

SCRIPT TABLE:
[SCRIPT_TABLE]

Frame size is 1080 x 1920 at 30 fps. Safe-zone rule: [SAFE_ZONE_RULE]. Caption template: [CAPTION_TEMPLATE].

Produce these four items.

1. SHOT LIST: one row per beat with columns Beat | Time | What to film or record | Camera position and framing (vertical, distance from subject) | Light | Movement | How it stays inside the safe zone | Source (own footage, own screen, own drawing, free asset, AI-generated abstract). Mark each row FILM, RECORD, DRAW, or SOURCE. Never propose footage from another creator, a film or TV show, or a real person's likeness. Never propose a realistic AI-generated person, place, or event.

2. CAPTION FILE: valid SRT text for the whole Short. Format each block as: block number, a line with start --> end in the form 00:00:00,000 --> 00:00:01,800, then the caption line, then a blank line. Follow the chosen caption template's words-per-screen limit. Match the times to the beats in the table. Add a final line "ADJUST TIMES AFTER YOU RECORD YOUR VOICE" below the SRT.

3. KEY TEXT LIST: the on-screen keywords with the beat each appears on, at most 6 words each.

4. LOG ROWS: for every non-owned asset in the shot list, one CSV row for visuals-log.csv with the columns asset_id,short_slug,what_it_is,source,maker_or_url,license_or_terms,date_checked,commercial_ok,own_or_free_or_ai. Fill unknown fields with VERIFY BEFORE RELYING. If no non-owned assets are needed, write "no non-owned assets".

Do not add a music track. If the table calls for sound, list only silence, natural sound, or an effect I record myself.
```

**Expected output:** A shot list, an SRT block set, a keyword list, and log rows.
**If the output is weak:** If the SRT times drift from the table, reply: "Recompute every caption time from the table's beat times and keep every caption inside its beat."

## Done when

- The exported file is 1080 x 1920, 30 fps, MP4, 3 minutes or less, with no watermark.
- No caption, face, or key object touches the red margins of the safe-zone overlay, and the important caption line sits above y = 1248.
- At least 50 percent of the seconds show your own filmed, recorded, or drawn material.
- The music choice is A, B, C (added in the app), or D, and it is logged in `music-log.csv`.
- Voice peaks are below -1 dBTP or about -6 dB on the mixer, and music sits 15 to 20 dB under the voice.
- You watched the Unlisted upload on a phone with the description expanded and nothing was covered.

## Next

Continue to [05-repurposing-without-reuse.md](05-repurposing-without-reuse.md).
