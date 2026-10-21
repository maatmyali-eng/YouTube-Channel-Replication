# Thumbnail Design Workflow and Templates

> **Purpose:** Build finished thumbnails with free editors, using 5 reusable layouts, a font and color method, and a weekly batch routine.  
> **Use when:** You have image prompts or owned photos from 02-original-generation.md and need finished 1280 x 720 files.  
> **Time needed:** 25 minutes per thumbnail the first week; about 10 minutes after templates exist.  
> **Needs:** A browser. Canva free or Photopea or GIMP.  
> **Cost:** $0

## Inputs

- [THUMB_DNA], [VIDEO_TOPIC], [CHANNEL_NAME], [LANGUAGE], [FACE_OR_FACELESS], [HARDWARE]
- Images that passed the source check in 02-original-generation.md (listed in `thumbnails/asset-log.csv` with `commercial_ok` = Y)
- TEXT: 0 to 4 words from your chosen concept

## Steps

### A. Pick one editor

| Editor | Free status (verify at the tool's site) | Watermark / license trap | Best for |
|---|---|---|---|
| Canva free (canva.com) | Free plan exists. Some premium elements are marked with a crown and need a paid plan. | Using a crown element in a free design either blocks export or adds a watermark. Magic Media AI limits and commercial terms conflict between sources: VERIFY BEFORE RELYING on canva.com/policies. | Fastest templates, beginners |
| Photopea (photopea.com) | Free, runs in the browser, shows ads. A paid plan removes ads, you do not need it. | None for files you make. Photopea opens .psd files; font and image licenses are still yours to check. | Photoshop-style layers without installing |
| GIMP (gimp.org) | Free, open source, runs on Windows, macOS, Linux. | None. Needs a desktop install and a reasonable [HARDWARE]. | Offline, no account |

If you have no account and no install permission, use Photopea.

### B. Create the canvas (exact steps)

Canvas size: 1280 x 720 px, 16:9. Menu names can shift between app versions; VERIFY on screen.

- Canva: **Create a design > Custom size**, width 1280, height 720, unit px, **Create new design**.
- Photopea: **File > New**, width 1280, height 720, units Pixels, resolution 72, **Create**.
- GIMP: **File > New**, width 1280, height 720, **OK**.

### C. Export (exact steps)

Target: JPG or PNG, 1280 x 720 px, under 2 MB (verified 2026-10-20). If the file is over 2 MB, export JPG at lower quality.

- Canva: **Share > Download**, File type JPG, set quality slider to about 80 percent if offered, **Download**. Do not tick Pro-only options.
- Photopea: **File > Export as > JPG**, set quality to 80, check the size shown in the dialog, **Save**.
- GIMP: **File > Export As**, name `thumb-A.jpg`, **Export**, set quality 85, **Export**.

Name files `thumbnails/<slug>/thumb-A.jpg`, `thumb-B.jpg`, `thumb-C.jpg`, where `<slug>` is the video slug used elsewhere in this repo.

### D. Make the 5 layout templates once

Build each as a saved design called `T1` to `T5`. All use a 1280 x 720 canvas, a 40 px margin on every side (this repo's safe area), and a reserved bottom-right block at x 1060 to 1280, y 620 to 720 for the timestamp (VERIFY on a phone preview). Coordinates are x, y from the top-left corner.

**T1 Right Hero.** Subject box x 640 to 1240, y 40 to 680 (about 47 percent of frame width). Text box x 40 to 620, y 120 to 560, left aligned, two lines max. Background: solid or gradient in color 1. Use for a finished dish, product, or face.

**T2 Split Compare.** Two panels, each 636 px wide: left x 0 to 636, right x 644 to 1280, with an 8 px divider in color 3. Label strips 70 px tall at y 40 to 110 on each panel, 2 words each. Keep each subject inside x 60 to 600 and x 704 to 1240, y 130 to 680. Use for before and after, cheap versus expensive, mistake versus fix.

**T3 Center Object and Pointer.** Object centered, box x 400 to 880, y 90 to 640. One pointer shape (arrow or circle) in color 3 at about 120 px, placed so it touches the object edge. Text 2 words, top band x 40 to 1240, y 40 to 170. Use for a single surprising detail.

**T4 Text Dominant.** Text fills x 60 to 1220 and y 120 to 520, two lines, cap height 150 to 200 px. One small object or icon at x 60 to 360, y 540 to 680, nothing in the reserved block. Use when the number or claim is the hook.

**T5 Wide Scene and Label.** Full-bleed scene photo, darkened 25 percent for contrast. Label box x 40 to 600, y 500 to 660, filled with color 1, text 2 to 4 words in color 2. Use for process shots and wide kitchen or location scenes.

Rotation rule (this repo's rule): never use the same template on more than 2 uploads in a row, and change the color pair every 3 uploads. This keeps the channel recognizable without looking mass-produced.

### E. Font and color pairing method

1. **Fonts.** Use one display font plus, at most, one supporting font. Pick from Google Fonts (fonts.google.com), which lists the license on each font page; most are under the SIL Open Font License, but VERIFY each font's license line before use. Starting pairs:
   - Anton (display) with Montserrat (support)
   - Bebas Neue (display) with Open Sans (support)
   - Oswald (display) with Roboto (support)
   Photopea and GIMP need the font installed or available; Canva includes many. In Canva, a few fonts are Pro-only; if you see a crown, choose another.
2. **Colors, 60-30-10.** 60 percent background color (color 1), 30 percent subject and shapes (color 2), 10 percent accent such as arrow, outline, or highlight (color 3). Choose colors from [THUMB_DNA]: copy the warm or cool character, never the identical palette plus layout.
3. **Check contrast.** Put the text color against its background in a free contrast checker (WebAIM Contrast Checker, webaim.org/resources/contrastchecker; VERIFY it is still free). Require at least 4.5:1.
4. **Check at small size.** Zoom the preview to 13 percent (about 168 x 94 px). You must still read the text and see the subject.

Starter palettes for the neutral demo niche (home cooking on a budget):

| Name | Color 1 | Color 2 | Color 3 |
|---|---|---|---|
| Warm pantry | #1F2A30 | #F4A940 | #FFFFFF |
| Fresh herb | #0E3B2E | #F7F3E8 | #FFD23F |
| Tomato night | #14171A | #E4572E | #F5F5F5 |
| Cool steel | #1B2430 | #79C7E3 | #FFE066 |
| Oat cream | #F4EBDD | #3A2E27 | #D1495B |

### F. Weekly batch routine (90 minutes for 4 videos)

This saves time only. Every thumbnail must still pass P-THUMB-03 in 02-original-generation.md, so the output is never a copy-and-swap of one template.

1. (10 min) For the week's 4 videos, run P-THUMB-02 once each and keep concepts A, B, C.
2. (20 min) Source images: your own shots first; generator images second; log each in `asset-log.csv`.
3. (40 min) Build A, B, C for each video in the editor. Different template and color pair per variant.
4. (10 min) Run the size check script below on `thumbnails/`.
5. (10 min) Run P-THUMB-03 on each A variant and P-THUMB-05 (in 04-ab-testing-and-safety.md) on each final.

Size check script (Python 3 with Pillow; install with `pip install pillow`):

```python
import sys
from pathlib import Path
from PIL import Image

root = Path(sys.argv[1] if len(sys.argv) > 1 else "thumbnails")
bad = 0
for p in sorted(root.rglob("*")):
    if p.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        continue
    size_mb = p.stat().st_size / (1024 * 1024)
    with Image.open(p) as im:
        w, h = im.size
    problems = []
    if (w, h) != (1280, 720):
        problems.append(f"size {w}x{h} (need 1280x720)")
    if size_mb >= 2:
        problems.append(f"{size_mb:.2f} MB (need under 2 MB)")
    if problems:
        bad += 1
        print(f"FAIL {p}: " + "; ".join(problems))
    else:
        print(f"OK   {p}: {w}x{h}, {size_mb:.2f} MB")
print("Files with problems:", bad)
sys.exit(1 if bad else 0)
```

## Prompts

### P-THUMB-04 — Layout and text picker

Purpose: Choose a template (T1 to T5), a text line, and a color palette for one video before you open the editor.

Inputs: [VIDEO_TOPIC], [THUMB_DNA], [FACE_OR_FACELESS], [LANGUAGE], [LAST_TEMPLATES] (the template codes of your last 2 uploads), [LAST_PALETTES] (palette names of your last 3 uploads).

```
You are a thumbnail layout planner. Use the five templates below and nothing else.
T1 Right Hero: subject on the right 47 percent, text on the left.
T2 Split Compare: two panels with a divider, 2-word label on each.
T3 Center Object and Pointer: one object centered, pointer shape, 2-word top text.
T4 Text Dominant: 2 lines of large text, one small object lower left.
T5 Wide Scene and Label: full-bleed scene, label box lower left.

Video topic: [VIDEO_TOPIC]
On screen: [FACE_OR_FACELESS]
Language of text: [LANGUAGE]
Family style: [THUMB_DNA]
My last two uploads used templates: [LAST_TEMPLATES]
My last three uploads used palettes: [LAST_PALETTES]

Rules: do not choose a template that would be used on 3 uploads in a row; do not reuse the palette of the last upload; text is 0 to 4 words, true of the video, and does not repeat the title.

Give 3 options in a table with columns: Template, Text (exactly as it would appear), Palette (name plus 3 hex codes with 60/30/10 roles), Subject to photograph or generate, Why it suits the topic (one sentence). Then name which option to try first. Do not invent facts about the video.
```

Expected output: A 3-row table and one recommendation.

If the output is weak: Say "use only T1 to T5 and avoid the templates and palettes I listed as recent."

## Done when

- `T1` to `T5` exist as saved designs in your editor.
- Each thumbnail file is 1280 x 720 px, under 2 MB, and named `thumb-A/B/C.jpg`.
- The size check script prints 0 files with problems.
- Text is 4 words or fewer, readable at 13 percent zoom, with 4.5:1 contrast.
- The last two uploads did not use the same template.

## Next

Continue to [04-ab-testing-and-safety.md](04-ab-testing-and-safety.md).
