# Workflow B: Low-Code Pipeline (Python, GitHub Actions, Free LLM Tier, Kokoro, Whisper, FFmpeg)

> **Purpose:** Run script drafting on a weekly schedule, then render voice, captions and a rough cut with open-source tools, all driven by the Google Sheets queue from Workflow A.  
> **Use when:** Workflow A works, you can copy and paste commands into a terminal, and you want the sheet to drive the work instead of your clicks.  
> **Time needed:** About 3 hours for setup, then 15 minutes per week plus rendering time.  
> **Needs:** A Google account, a free GitHub account, a computer with Python 3.11, FFmpeg and espeak-ng installed, the `Pipeline` sheet from `02-no-code-workflow.md`.  
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [LANGUAGE], [VIDEO_LENGTH], [STYLE_BIBLE], [VOICE_MODE], [HARDWARE]
- The `Pipeline` and `Config` tabs from `02-no-code-workflow.md`, with the headers unchanged
- The workspace layout from `03-bulk-systems.md`

## What this workflow does, and where it stops

| Stage | What the code does | Status it writes | What you do |
|---|---|---|---|
| Draft | Reads `APPROVED` rows, asks a free LLM API for a script, saves `script-v1.md`, writes the draft to the sheet | `SCRIPTED` (the only status code is allowed to write) | Edit into `script.md`, fact-check, set `SCRIPT_OK` yourself (gate C2) |
| Voice | Reads `script.md` for `SCRIPT_OK` rows, refuses if any `[OWNER TO ADD]`, `[CHECK]` or `[STOP` marker remains, renders `voice.wav` with Kokoro | none, adds a note | Listen to all of it, set `VOICED` yourself (gate C3) |
| Captions | Transcribes `voice.wav` with Whisper into `captions.srt` | none, adds a note | Correct names and terms |
| Assemble | Joins the files in `clips/` and `voice.wav` into `rough-cut.mp4` | none, adds a note | Edit in DaVinci Resolve or CapCut. A rough cut is not a finished video |

The code cannot upload, schedule or publish. The code also cannot write any status that carries a gate in `04-human-checkpoints.md`. This is deliberate: fully automated publishing of unreviewed videos is the main demonetization risk, and a faceless script, voice and stock-clip pipeline with no human work added is the pattern YouTube's July 2026 inauthentic content clarification describes as non-monetizable (verified 2026-10-20). Rendering is allowed to be automatic. Judgment and first-hand content are not.

## Free limits and licences (verified 2026-10-20)

| Item | Limit or licence | Trap | Free fallback |
|---|---|---|---|
| GitHub Actions, public repo | Free on standard GitHub-hosted runners | Your scripts and drafts would be public | Use a private repo |
| GitHub Actions, private repo on the Free plan | 2,000 minutes per month and 500 MB of storage, Linux minutes at 1x | Minutes stop when used up. Artifacts count toward the 500 MB | Run the same commands on your own computer |
| Gemini API free tier | Free key from Google AI Studio, no billing. Per-model limits are shown only at aistudio.google.com/rate-limit. Preview models are limited more tightly. Free-tier requests may be used to improve Google products | Do not send anything confidential. Model names change | The free Gemini app, pasted by hand |
| Kokoro-82M TTS | Apache 2.0 weights, `pip install kokoro>=0.9.4`, needs espeak-ng installed | Voice quality varies by language. Not a cloned voice, which this repo never uses | Piper (VERIFY BEFORE RELYING: licence and voice-model terms on the Piper project page) or your own recording |
| Whisper through `faster-whisper` | Runs on CPU | VERIFY BEFORE RELYING: licence on the Whisper and faster-whisper project pages. Model files download on first use | Type captions in DaVinci Resolve or upload an SRT you wrote |
| FFmpeg | Free software | VERIFY BEFORE RELYING: licence of the build you install (LGPL or GPL) | CapCut or DaVinci Resolve for assembly |
| Google Sheets API | VERIFY BEFORE RELYING: free quota on the Google Sheets API page in Cloud Console | A per-minute read limit stops fast loops | The scripts make few calls |

## Folder layout

```
yt-pipeline/
  .env.example
  .gitignore
  requirements.txt
  requirements-draft.txt
  prompts/
    script_prompt.txt
  pipeline/
    __init__.py
    config.py
    sheets_queue.py
    gen_script.py
    make_voice.py
    make_captions.py
    assemble_video.py
    run.py
  workspace/                  (a copy of [CHANNEL_NAME]-workspace/ from 03-bulk-systems.md)
    videos/
      L012-lentil-stew-under-3-dollars/
        script-v1.md          (machine draft)
        script.md             (your approved script)
        voice.wav
        captions.srt
        clips/
        rough-cut.mp4
  .github/
    workflows/
      draft-scripts.yml
      render-media.yml
```

## Steps

### Part 1. Install the tools on your computer

1. Install Python 3.11 from python.org. On Windows, tick **Add python.exe to PATH**.
2. Install espeak-ng and FFmpeg.
   - Ubuntu or Debian: `sudo apt-get update && sudo apt-get install -y espeak-ng ffmpeg`
   - macOS with Homebrew: `brew install espeak-ng ffmpeg`
   - Windows: install the espeak-ng `.msi` from the espeak-ng releases page and FFmpeg from ffmpeg.org, then add both folders to PATH (VERIFY BEFORE RELYING: current download pages).
3. Make the project folder and files. Create `yt-pipeline/` and every file in the layout above. Paste the code from the sections below into each file.
4. Open a terminal inside `yt-pipeline/` and run:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
cp .env.example .env               # Windows: copy .env.example .env
```

The CPU build of PyTorch goes first so that Kokoro does not pull in a very large GPU build.

### Part 2. Let code read the sheet

5. Go to console.cloud.google.com and create a project named `yt-pipeline`. Billing is not required for these steps (VERIFY BEFORE RELYING: the Cloud Console may ask for billing in some regions).
6. Open **APIs & Services > Library**, search **Google Sheets API**, and select **Enable**.
7. Open **IAM & Admin > Service Accounts > Create service account**. Name it `pipeline-bot`. Skip the optional role steps.
8. Open the new service account, then **Keys > Add key > Create new key > JSON**. A file downloads. Move it to `yt-pipeline/` and rename it `service-account.json`. This file is a password. Never commit or share it.
9. Open the file and copy the value of `client_email`. In your `[CHANNEL_NAME] Pipeline` sheet select **Share**, paste that email, and give it **Editor** access.
10. Copy the sheet ID from its address: the long text between `/d/` and `/edit`.
11. Fill `.env` using `.env.example` below. Put the model name in `GEMINI_MODEL` by copying a free Flash-class, non-preview model name from aistudio.google.com or the Gemini API pricing page (VERIFY BEFORE RELYING: model names change).
12. Run `python -m pipeline.run check`. It must print `OK: all required headers found` and a count of rows per status.

### Part 3. Run each stage by hand first

13. Set one row to `APPROVED` with columns F and G filled. Run `python -m pipeline.run draft`.
14. Open `workspace/videos/<slug>/script-v1.md`. Edit it into your final script, resolve every marker, and save it as `script.md` in the same folder. Pass gate C2 and set the status to `SCRIPT_OK` yourself.
15. Run `python -m pipeline.run voice <slug>`, then `python -m pipeline.run captions <slug>`.
16. Listen to the whole of `voice.wav`. Pass gate C3. If your [VOICE_MODE] is your own voice, skip step 15's voice command, save your recording as `voice.wav` and run only the captions command.
17. After gate C4, put images and clips in `clips/`, named `01-...`, `02-...` so they sort in order. Run `python -m pipeline.run assemble <slug>`.

### Part 4. Put drafting on a schedule

18. Create a **private** repository on github.com named `yt-pipeline`. Push the project. Check that `.env` and `service-account.json` do not appear in the repository.
19. Open **Settings > Secrets and variables > Actions**. Under **Secrets** add `GEMINI_API_KEY`, `SHEET_ID`, and `GOOGLE_SERVICE_ACCOUNT_JSON` (paste the whole content of the JSON file). Under **Variables** add `GEMINI_MODEL`.
20. Open **Settings > Actions > General > Workflow permissions** and choose **Read and write permissions**. Save.
21. Open the **Actions** tab, choose **Draft scripts (weekly)**, and select **Run workflow** to test it once. Check the sheet and the new `script-v1.md`.

## Code

### requirements.txt

```
# Lower bounds. After your first successful run, execute "pip freeze > requirements.lock.txt"
# and install from that file if you want exactly repeatable builds.
python-dotenv>=1.0
gspread>=6.0
google-genai>=1.0
kokoro>=0.9.4
soundfile>=0.12
numpy>=1.26
faster-whisper>=1.0
```

### requirements-draft.txt

```
# The weekly drafting job needs only these three, so it installs fast.
python-dotenv>=1.0
gspread>=6.0
google-genai>=1.0
```

### .env.example

```
# Copy this file to ".env" and fill in the values. Never commit ".env".

# Google Sheets queue
SHEET_ID=paste-the-long-id-from-the-sheet-address
SHEET_TAB=Pipeline
CONFIG_TAB=Config
GOOGLE_SERVICE_ACCOUNT_FILE=service-account.json

# Free Gemini API key from aistudio.google.com
GEMINI_API_KEY=paste-your-key
# Copy a free, non-preview Flash-class model name from the AI Studio model list.
GEMINI_MODEL=
MAX_ROWS_PER_RUN=3
GEMINI_SLEEP_SECONDS=20

# Where your workspace folder lives, relative to this project
WORKSPACE_DIR=workspace

# Kokoro voice. "a" is American English, "b" is British English.
# Other language codes and voice names are in the Kokoro VOICES list (VERIFY BEFORE RELYING).
KOKORO_LANG=a
KOKORO_VOICE=af_heart
KOKORO_SPEED=1.0

# Whisper. Models: tiny, base, small, medium. Leave WHISPER_LANG empty to auto-detect, or use a code like en.
WHISPER_MODEL=small
WHISPER_LANG=

# Seconds each still image stays on screen in the rough cut
STILL_SECONDS=6
```

### .gitignore

```
.env
service-account.json
*.json
.venv/
__pycache__/
workspace/videos/**/*.wav
workspace/videos/**/*.mp4
workspace/videos/**/_work/
workspace/videos/**/clips/
```

### prompts/script_prompt.txt

```
You are a scriptwriter for [CHANNEL_NAME]. Write in [LANGUAGE].
Follow this Style Bible for tone, structure, hook mechanics, pacing and vocabulary level: [STYLE_BIBLE]

Format: [FORMAT]. Target length: [VIDEO_LENGTH].
Topic: [TOPIC]
The viewer's question: [AUDIENCE_QUESTION]
The owner's first-hand material: [FIRST_HAND_ANGLE]
Value layers the video must deliver: [VALUE_STACK_LAYERS]

Write a script in this layout:
HOOK (first 15 seconds, or first 3 seconds for a Short)
OPEN LOOP (one question the video answers later)
BODY (numbered beats; for each beat write: spoken text, then a line starting "SHOW:" describing what the viewer sees)
PAYOFF (answers the open loop)
CLOSE (one specific next-step for the viewer, no generic "like and subscribe" filler)

Rules:
1. Use only the first-hand material provided. Where the script needs a number, a result, a quote, or a personal experience that was not provided, write [OWNER TO ADD: what is needed] and do not invent it.
2. Mark every factual claim that needs a source with [CHECK].
3. Do not reproduce or closely paraphrase any other creator's script. Match the style, never the content.
4. Do not give medical, financial, or legal advice. If the topic requires it, write [STOP: sensitive topic, owner review required] and nothing else.
5. End with a list titled GAPS that lists every [OWNER TO ADD] and [CHECK] item.
```

### pipeline/__init__.py

```python
# This file is intentionally empty. It tells Python that "pipeline" is a package.
```

### pipeline/config.py

```python
"""Settings loader.

Reads values from the .env file on your computer, or from environment
variables on GitHub Actions. Beginners: you never need to edit this file.
"""
import os
import re
from pathlib import Path

from dotenv import load_dotenv

# Load .env if it exists. On GitHub Actions there is no .env file, and that is fine.
load_dotenv()

# ROOT is the yt-pipeline folder (the parent of the "pipeline" folder).
ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = (ROOT / os.getenv("WORKSPACE_DIR", "workspace")).resolve()

# A slug looks like L012-lentil-stew-under-3-dollars or S031-three-pantry-swaps.
SLUG_PATTERN = re.compile(r"^[LS]\d{3}-[a-z0-9]+(-[a-z0-9]+)*$")


def need(name: str) -> str:
    """Return a setting or stop with a clear message if it is missing."""
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing setting {name}. Add it to your .env file (see .env.example).")
    return value


def video_dir(slug: str) -> Path:
    """Return the folder for one video, creating it if needed."""
    if not SLUG_PATTERN.match(slug or ""):
        raise SystemExit(f"'{slug}' is not a valid slug. Example: L012-lentil-stew-under-3-dollars")
    path = WORKSPACE / "videos" / slug
    path.mkdir(parents=True, exist_ok=True)
    return path
```

### pipeline/sheets_queue.py

```python
"""Reads and writes the Google Sheet that acts as the queue.

The code is only allowed to write the status SCRIPTED. Every other status
carries a human checkpoint (see 04-human-checkpoints.md), so a person sets it.
"""
import json
import os
from datetime import datetime, timezone

import gspread

from .config import need

REQUIRED_HEADERS = [
    "slug", "format", "status", "topic", "audience_question", "first_hand_angle",
    "value_stack_layers", "script_draft", "notes", "last_updated",
]

# The only status this program may write. Do not add more.
STATUSES_CODE_MAY_WRITE = {"SCRIPTED"}

# Google Sheets cells have a character limit (VERIFY BEFORE RELYING: current limit).
# We stay safely under it. The full text is always saved in the file as well.
CELL_LIMIT = 45000


def now_text() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


class Queue:
    def __init__(self):
        # Two ways to log in: a JSON text (GitHub Actions) or a JSON file (your computer).
        raw_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()
        if raw_json:
            client = gspread.service_account_from_dict(json.loads(raw_json))
        else:
            client = gspread.service_account(filename=need("GOOGLE_SERVICE_ACCOUNT_FILE"))
        book = client.open_by_key(need("SHEET_ID"))
        self.sheet = book.worksheet(os.getenv("SHEET_TAB", "Pipeline"))
        self.config_sheet = book.worksheet(os.getenv("CONFIG_TAB", "Config"))
        self.headers = self.sheet.row_values(1)

    def missing_headers(self):
        return [h for h in REQUIRED_HEADERS if h not in self.headers]

    def rows(self):
        """Return every data row as a dict. "_row" holds the sheet row number."""
        values = self.sheet.get_all_values()
        result = []
        for number, cells in enumerate(values[1:], start=2):
            padded = cells + [""] * (len(self.headers) - len(cells))
            record = dict(zip(self.headers, padded))
            record["_row"] = number
            result.append(record)
        return result

    def find(self, slug: str):
        for record in self.rows():
            if record.get("slug", "").strip() == slug:
                return record
        return None

    def config(self) -> dict:
        """Read the Config tab: column A is the name, column B is the value."""
        pairs = {}
        for cells in self.config_sheet.get_all_values():
            if len(cells) >= 2 and cells[0].strip():
                pairs[cells[0].strip()] = cells[1]
        return pairs

    def set_cell(self, row: int, column_name: str, value: str):
        column = self.headers.index(column_name) + 1
        self.sheet.update_cell(row, column, value[:CELL_LIMIT])

    def set_status(self, row: int, new_status: str):
        if new_status not in STATUSES_CODE_MAY_WRITE:
            raise SystemExit(f"Refused: code may not write status {new_status}. A person sets it.")
        self.set_cell(row, "status", new_status)
        self.set_cell(row, "last_updated", now_text())

    def add_note(self, row: int, text: str):
        current = self.sheet.cell(row, self.headers.index("notes") + 1).value or ""
        joined = (current + "\n" if current else "") + f"[{now_text()}] {text}"
        self.set_cell(row, "notes", joined)
        self.set_cell(row, "last_updated", now_text())
```

### pipeline/gen_script.py

```python
"""Stage: draft scripts for rows with status APPROVED."""
import os
import re
import time

from google import genai

from .config import ROOT, need, video_dir
from .sheets_queue import Queue

PROMPT_FILE = ROOT / "prompts" / "script_prompt.txt"


def fill_prompt(template: str, row: dict, cfg: dict) -> str:
    """Swap every [TOKEN] in the template for real text, in a single pass."""
    values = {
        "[CHANNEL_NAME]": cfg.get("channel_name", ""),
        "[LANGUAGE]": cfg.get("language", ""),
        "[STYLE_BIBLE]": cfg.get("style_bible", ""),
        "[VIDEO_LENGTH]": cfg.get("video_length", ""),
        "[FORMAT]": row.get("format", ""),
        "[TOPIC]": row.get("topic", ""),
        "[AUDIENCE_QUESTION]": row.get("audience_question", ""),
        "[FIRST_HAND_ANGLE]": row.get("first_hand_angle", ""),
        "[VALUE_STACK_LAYERS]": row.get("value_stack_layers", ""),
    }
    return re.sub(r"\[[A-Z_]+\]", lambda m: values.get(m.group(0), m.group(0)), template)


def call_model(client, model: str, prompt: str) -> str:
    """Ask the model. If the free tier says "slow down", wait and try again."""
    for attempt in range(1, 5):
        try:
            response = client.models.generate_content(model=model, contents=prompt)
            return response.text or ""
        except Exception as error:  # the SDK raises several error types
            message = str(error)
            busy = any(code in message for code in ("429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE"))
            if busy:
                wait = 30 * attempt
                print(f"Model is busy or rate limited. Waiting {wait} seconds (try {attempt} of 4).")
                time.sleep(wait)
                continue
            raise
    raise SystemExit("Gave up after 4 tries. Check aistudio.google.com/rate-limit and run again later.")


def run_draft():
    queue = Queue()
    config = queue.config()
    client = genai.Client(api_key=need("GEMINI_API_KEY"))
    model = need("GEMINI_MODEL")
    template = PROMPT_FILE.read_text(encoding="utf-8")
    limit = int(os.getenv("MAX_ROWS_PER_RUN", "3"))
    pause = float(os.getenv("GEMINI_SLEEP_SECONDS", "20"))

    done = 0
    for row in queue.rows():
        if done >= limit:
            break
        if row.get("status") != "APPROVED":
            continue
        slug = row.get("slug", "").strip()
        # Gate C1 reminder: no first-hand angle or value layers means no draft.
        if not slug or not row.get("first_hand_angle", "").strip() or not row.get("value_stack_layers", "").strip():
            print(f"Skipping row {row['_row']}: slug, first_hand_angle and value_stack_layers must all be filled.")
            continue

        print(f"Drafting {slug} ...")
        text = call_model(client, model, fill_prompt(template, row, config))
        if not text.strip():
            queue.add_note(row["_row"], "Draft failed: the model returned no text. Rewrite the first-hand angle and try again.")
            continue

        (video_dir(slug) / "script-v1.md").write_text(text, encoding="utf-8")
        queue.set_cell(row["_row"], "script_draft", text)
        queue.set_status(row["_row"], "SCRIPTED")
        queue.add_note(row["_row"], "Machine draft saved as script-v1.md. Edit, fact-check, then save as script.md (gate C2).")
        done += 1
        time.sleep(pause)

    print(f"Finished. Drafted {done} script(s).")
```

### pipeline/make_voice.py

```python
"""Stage: turn the approved script.md into voice.wav with Kokoro TTS."""
import os
import re

import numpy as np
import soundfile as sf

from .config import video_dir
from .sheets_queue import Queue

# If any of these remain, a person has not finished the script. Refuse to render.
BLOCKING_MARKERS = ["[OWNER TO ADD", "[CHECK]", "[STOP"]

SECTION_LABEL = re.compile(r"^(HOOK|OPEN LOOP|BODY|PAYOFF|CLOSE)\b")


def spoken_text(markdown: str) -> str:
    """Keep only the words that should be spoken."""
    kept = []
    for line in markdown.splitlines():
        text = line.strip()
        if not text:
            continue
        if text.upper().startswith("GAPS"):
            break                                   # the GAPS list is for you, not for the voice
        if text.upper().startswith("SHOW:"):
            continue                                # visual directions are not spoken
        if text.startswith("#"):
            continue                                # markdown headings
        if SECTION_LABEL.match(text) and len(text) < 90:
            continue                                # labels such as HOOK or OPEN LOOP
        text = re.sub(r"\[[^\]]*\]", "", text)      # leftover bracket notes
        text = re.sub(r"[*_`>]", "", text)          # markdown marks
        text = re.sub(r"^\d+[.)]\s*", "", text)     # list numbers
        if text.strip():
            kept.append(text.strip())
    return "\n".join(kept)


def render_voice(slug: str):
    queue = Queue()
    row = queue.find(slug)
    if row is None:
        raise SystemExit(f"No row with slug {slug} in the sheet.")
    if row.get("status") not in ("SCRIPT_OK", "VOICED"):
        raise SystemExit("Refused: status must be SCRIPT_OK (you must pass gate C2 first).")

    script_path = video_dir(slug) / "script.md"
    if not script_path.exists():
        raise SystemExit("script.md not found. Save your edited, approved script as script.md.")
    raw = script_path.read_text(encoding="utf-8")
    for marker in BLOCKING_MARKERS:
        if marker in raw:
            raise SystemExit(f"Refused: script.md still contains {marker}. Resolve every gap first.")

    text = spoken_text(raw)
    if len(text) < 50:
        raise SystemExit("There is almost no spoken text in script.md. Check the file.")

    # Imported here so the weekly drafting job does not need Kokoro installed.
    from kokoro import KPipeline

    pipeline = KPipeline(lang_code=os.getenv("KOKORO_LANG", "a"))
    voice = os.getenv("KOKORO_VOICE", "af_heart")
    speed = float(os.getenv("KOKORO_SPEED", "1.0"))
    sample_rate = 24000  # Kokoro's native rate

    pieces = []
    for result in pipeline(text, voice=voice, speed=speed, split_pattern=r"\n+"):
        # Newer versions return an object with .audio, older versions return a tuple.
        audio = result.audio if hasattr(result, "audio") else result[2]
        if audio is None:
            continue
        if hasattr(audio, "detach"):
            audio = audio.detach().cpu().numpy()
        pieces.append(np.asarray(audio, dtype="float32").reshape(-1))
        pieces.append(np.zeros(int(sample_rate * 0.25), dtype="float32"))  # quarter-second pause

    if not pieces:
        raise SystemExit("Kokoro produced no audio. Check that espeak-ng is installed.")

    out_path = video_dir(slug) / "voice.wav"
    sf.write(str(out_path), np.concatenate(pieces), sample_rate)
    queue.add_note(row["_row"], "voice.wav rendered with Kokoro. Listen to all of it (gate C3). Decide the synthetic-voice disclosure.")
    print(f"Saved {out_path}")
```

### pipeline/make_captions.py

```python
"""Stage: make captions.srt from voice.wav with Whisper (faster-whisper)."""
import os
import textwrap

from .config import video_dir
from .sheets_queue import Queue


def srt_time(seconds: float) -> str:
    total_ms = int(round(seconds * 1000))
    hours, rest = divmod(total_ms, 3_600_000)
    minutes, rest = divmod(rest, 60_000)
    secs, ms = divmod(rest, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{ms:03}"


def make_captions(slug: str):
    queue = Queue()
    row = queue.find(slug)
    if row is None:
        raise SystemExit(f"No row with slug {slug} in the sheet.")
    if row.get("status") not in ("SCRIPT_OK", "VOICED", "VISUALS_DONE", "EDITED"):
        raise SystemExit("Refused: the script must have passed gate C2 first (status SCRIPT_OK or later).")

    wav_path = video_dir(slug) / "voice.wav"
    if not wav_path.exists():
        raise SystemExit("voice.wav not found. Render it, or save your own recording as voice.wav.")

    # Imported here so the weekly drafting job does not need Whisper installed.
    from faster_whisper import WhisperModel

    model = WhisperModel(os.getenv("WHISPER_MODEL", "small"), device="cpu", compute_type="int8")
    language = os.getenv("WHISPER_LANG") or None
    segments, _info = model.transcribe(str(wav_path), language=language, vad_filter=True)

    out_path = video_dir(slug) / "captions.srt"
    count = 0
    with open(out_path, "w", encoding="utf-8") as handle:
        for segment in segments:
            text = segment.text.strip()
            if not text:
                continue
            count += 1
            wrapped = "\n".join(textwrap.wrap(text, 42))  # two short lines read easily
            handle.write(f"{count}\n{srt_time(segment.start)} --> {srt_time(segment.end)}\n{wrapped}\n\n")

    queue.add_note(row["_row"], f"captions.srt written ({count} captions). Correct names and terms by hand.")
    print(f"Saved {out_path}")
```

### pipeline/assemble_video.py

```python
"""Stage: join clips/ and voice.wav into rough-cut.mp4 with FFmpeg.

The result is a ROUGH CUT for you to edit. It is not a finished video.
"""
import os
import subprocess

from .config import video_dir
from .sheets_queue import Queue

IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".webp"}
VIDEO_TYPES = {".mp4", ".mov", ".mkv", ".webm"}

# Make every clip the same size and speed so they can be joined.
FILTER = ("scale=1920:1080:force_original_aspect_ratio=decrease,"
          "pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p,setsar=1")


def run(command):
    print("RUN:", " ".join(command))
    subprocess.run(command, check=True)


def duration(path) -> float:
    """Length of a media file in seconds, using ffprobe (installed with FFmpeg)."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True)
    return float(result.stdout.strip())


def assemble(slug: str):
    queue = Queue()
    row = queue.find(slug)
    if row is None:
        raise SystemExit(f"No row with slug {slug} in the sheet.")
    if row.get("status") not in ("VISUALS_DONE", "EDITED"):
        raise SystemExit("Refused: status must be VISUALS_DONE (you must pass gate C4 first).")

    folder = video_dir(slug)
    voice = folder / "voice.wav"
    clips_dir = folder / "clips"
    if not voice.exists() or not clips_dir.exists():
        raise SystemExit("Need voice.wav and a clips/ folder with images or video clips.")
    clips = sorted(p for p in clips_dir.iterdir() if p.suffix.lower() in IMAGE_TYPES | VIDEO_TYPES)
    if not clips:
        raise SystemExit("The clips/ folder is empty.")

    work = folder / "_work"
    work.mkdir(exist_ok=True)
    still_seconds = os.getenv("STILL_SECONDS", "6")

    names = []
    for index, clip in enumerate(clips):
        part = work / f"part{index:03}.mp4"
        if clip.suffix.lower() in IMAGE_TYPES:
            command = ["ffmpeg", "-y", "-loop", "1", "-t", still_seconds, "-i", str(clip)]
        else:
            command = ["ffmpeg", "-y", "-i", str(clip)]
        command += ["-vf", FILTER, "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "20", str(part)]
        run(command)
        names.append(part.name)

    # The concat list uses names relative to the list file's own folder.
    list_file = work / "list.txt"
    list_file.write_text("".join(f"file '{name}'\n" for name in names), encoding="utf-8")
    silent = work / "silent.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_file), "-c", "copy", str(silent)])

    video_len, audio_len = duration(silent), duration(voice)
    if video_len < audio_len:
        print(f"WARNING: pictures last {video_len:.0f}s but the voice lasts {audio_len:.0f}s. "
              "The rough cut will stop early. Add clips or raise STILL_SECONDS.")

    rough = folder / "rough-cut.mp4"
    run(["ffmpeg", "-y", "-i", str(silent), "-i", str(voice), "-map", "0:v:0", "-map", "1:a:0",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(rough)])

    queue.add_note(row["_row"], "rough-cut.mp4 built. Edit it for pacing and original commentary before it counts as a video.")
    print(f"Saved {rough}")
```

### pipeline/run.py

```python
"""Command line entry point.

Examples:
  python -m pipeline.run check
  python -m pipeline.run draft
  python -m pipeline.run voice L012-lentil-stew-under-3-dollars
  python -m pipeline.run captions L012-lentil-stew-under-3-dollars
  python -m pipeline.run assemble L012-lentil-stew-under-3-dollars
"""
import argparse
from collections import Counter


def main():
    parser = argparse.ArgumentParser(description="Low-code YouTube production pipeline")
    parser.add_argument("stage", choices=["check", "draft", "voice", "captions", "assemble"])
    parser.add_argument("slug", nargs="?", help="Video slug, needed for voice, captions and assemble")
    args = parser.parse_args()

    if args.stage in ("voice", "captions", "assemble") and not args.slug:
        raise SystemExit("This stage needs a slug, for example L012-lentil-stew-under-3-dollars")

    # Stages are imported only when used, so each GitHub job installs only what it needs.
    if args.stage == "check":
        from .sheets_queue import Queue
        queue = Queue()
        missing = queue.missing_headers()
        if missing:
            raise SystemExit(f"Missing headers in row 1 of the sheet: {missing}")
        print("OK: all required headers found")
        counts = Counter(row.get("status", "") or "(blank)" for row in queue.rows())
        for status, count in sorted(counts.items()):
            print(f"  {status}: {count}")
    elif args.stage == "draft":
        from .gen_script import run_draft
        run_draft()
    elif args.stage == "voice":
        from .make_voice import render_voice
        render_voice(args.slug)
    elif args.stage == "captions":
        from .make_captions import make_captions
        make_captions(args.slug)
    elif args.stage == "assemble":
        from .assemble_video import assemble
        assemble(args.slug)


if __name__ == "__main__":
    main()
```

### .github/workflows/draft-scripts.yml

```yaml
# Runs every Monday at 03:00 UTC and can also be started by hand.
# It drafts scripts for APPROVED rows and saves them as text files.
# It never uploads, schedules, or publishes anything.
name: Draft scripts (weekly)

on:
  schedule:
    - cron: "0 3 * * 1"
  workflow_dispatch:

permissions:
  contents: write        # needed to save the draft files back to the repository

concurrency:
  group: draft-scripts
  cancel-in-progress: false

jobs:
  draft:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - name: Get the code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip
          cache-dependency-path: requirements-draft.txt

      - name: Install light dependencies
        run: pip install -r requirements-draft.txt

      - name: Draft scripts for APPROVED rows
        run: python -m pipeline.run draft
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          GEMINI_MODEL: ${{ vars.GEMINI_MODEL }}
          SHEET_ID: ${{ secrets.SHEET_ID }}
          GOOGLE_SERVICE_ACCOUNT_JSON: ${{ secrets.GOOGLE_SERVICE_ACCOUNT_JSON }}
          MAX_ROWS_PER_RUN: "3"
          GEMINI_SLEEP_SECONDS: "20"

      - name: Save new draft files
        run: |
          git config user.name "pipeline-bot"
          git config user.email "pipeline-bot@users.noreply.github.com"
          git add workspace/videos
          if git diff --cached --quiet; then
            echo "No new drafts to save."
          else
            git commit -m "Add script drafts"
            git push
          fi
```

### .github/workflows/render-media.yml

```yaml
# Started by hand only. Renders voice.wav and captions.srt for one approved video.
# Files are kept as a download for 3 days so they do not fill the free storage.
name: Render voice and captions (manual)

on:
  workflow_dispatch:
    inputs:
      slug:
        description: "Video slug, for example L012-lentil-stew-under-3-dollars"
        required: true

jobs:
  render:
    runs-on: ubuntu-latest
    timeout-minutes: 90
    steps:
      - name: Get the code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install system tools
        run: sudo apt-get update && sudo apt-get install -y espeak-ng ffmpeg

      - name: Remember downloaded models between runs
        uses: actions/cache@v4
        with:
          path: ~/.cache/huggingface
          key: models-${{ runner.os }}-v1

      - name: Install Python packages (CPU build of PyTorch first)
        run: |
          pip install torch --index-url https://download.pytorch.org/whl/cpu
          pip install -r requirements.txt

      - name: Render voice
        run: python -m pipeline.run voice "$SLUG"
        env:
          SLUG: ${{ inputs.slug }}
          SHEET_ID: ${{ secrets.SHEET_ID }}
          GOOGLE_SERVICE_ACCOUNT_JSON: ${{ secrets.GOOGLE_SERVICE_ACCOUNT_JSON }}
          KOKORO_LANG: "a"
          KOKORO_VOICE: "af_heart"

      - name: Make captions
        run: python -m pipeline.run captions "$SLUG"
        env:
          SLUG: ${{ inputs.slug }}
          SHEET_ID: ${{ secrets.SHEET_ID }}
          GOOGLE_SERVICE_ACCOUNT_JSON: ${{ secrets.GOOGLE_SERVICE_ACCOUNT_JSON }}
          WHISPER_MODEL: "small"

      - name: Keep the results for 3 days
        uses: actions/upload-artifact@v4
        with:
          name: media-${{ inputs.slug }}
          path: |
            workspace/videos/${{ inputs.slug }}/voice.wav
            workspace/videos/${{ inputs.slug }}/captions.srt
          retention-days: 3
```

Action versions (`checkout@v4`, `setup-python@v5`, `cache@v4`, `upload-artifact@v4`): VERIFY BEFORE RELYING on each action's releases page. Set `KOKORO_LANG` and `KOKORO_VOICE` in the file to match your [LANGUAGE].

## Exact FFmpeg commands (the manual version of assemble)

Run these inside a video folder if you prefer to assemble by hand or the script fails.

```bash
# 1. Make one image into a 6-second clip with the standard size and speed
ffmpeg -y -loop 1 -t 6 -i clips/01-intro.png \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p,setsar=1" \
  -an -c:v libx264 -preset medium -crf 20 part000.mp4

# 2. Make a video clip the same size and speed
ffmpeg -y -i clips/02-demo.mp4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p,setsar=1" \
  -an -c:v libx264 -preset medium -crf 20 part001.mp4

# 3. Write list.txt with one line per part:   file 'part000.mp4'   then join them
ffmpeg -y -f concat -safe 0 -i list.txt -c copy silent.mp4

# 4. Add the voice
ffmpeg -y -i silent.mp4 -i voice.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -shortest rough-cut.mp4

# 5. Optional: burn captions into the picture (run inside the folder that holds captions.srt)
ffmpeg -y -i rough-cut.mp4 -vf "subtitles=captions.srt" -c:a copy rough-cut-captioned.mp4

# 6. Check a file's length
ffprobe -v error -show_entries format=duration -of csv=p=0 voice.wav
```

Upload `captions.srt` as a caption file in YouTube Studio instead of burning captions in when you want viewers to be able to turn them off.

## Prompts

### P-AUTO-12 — Adapt the Code to My Setup

Purpose: Have a chat LLM change the scripts for your language, voice, sheet headers, or computer without breaking the gate rules.
Inputs: [LANGUAGE], [VOICE_MODE], [HARDWARE], [CHANGE_REQUEST] (what you want changed), [FILE_TEXT] (paste the full file or files to change).

```
You are a careful Python developer helping a beginner. The project is a low-code YouTube production pipeline. Language of the channel: [LANGUAGE]. Voice mode: [VOICE_MODE]. Hardware: [HARDWARE].

Change request: [CHANGE_REQUEST]
Current file or files: [FILE_TEXT]

Return the complete changed file or files, ready to paste, with comments written for a beginner on every new or changed line.

Hard rules:
1. Do not add any code that uploads, schedules, or publishes a video.
2. Do not let the code write any sheet status other than SCRIPTED.
3. Do not remove the refusal checks for [OWNER TO ADD], [CHECK], and [STOP markers.
4. Use only free libraries and free tiers. If a change needs a paid service, say so and offer a free alternative.
5. Do not guess model names, library names, or licence terms. If unsure, write VERIFY BEFORE RELYING and name the official page.
After the code, give the exact terminal commands to test the change and the output I should see.
```

Expected output: Complete files plus test commands.
If the output is weak: Paste the exact error text and the line number, and ask for only the corrected function.

### P-AUTO-13 — Debug a Failed Run

Purpose: Diagnose a failed local run or GitHub Actions run.
Inputs: [LOG_TEXT] (the last 80 lines of the log, with all keys and secrets deleted), [STAGE] (draft, voice, captions, assemble), [WHAT_CHANGED] (what you changed since it last worked).

```
My low-code YouTube pipeline stage "[STAGE]" failed.
Log: [LOG_TEXT]
What changed since it last worked: [WHAT_CHANGED]

Give the 3 most likely causes in order. For each: how to confirm in under 2 minutes, the exact fix, and whether the fix costs anything. Never suggest a paid plan, never suggest removing the human-gate checks, and never suggest publishing automatically. If the cause is a free-tier limit, name the official page where I can read the current limit. If I pasted a secret by mistake, tell me first to delete and recreate that secret.
```

Expected output: Three ranked causes with checks and fixes.
If the output is weak: Add the Python version, operating system, and the output of `pip list`.

## Failure points and fixes

| Failure | Cause | Fix |
|---|---|---|
| `Missing setting ...` | `.env` not filled, or a secret not added on GitHub | Fill `.env`, or add the secret under Settings > Secrets and variables > Actions |
| `PermissionError` or 403 from Sheets | The sheet was not shared with the service account | Share the sheet with the `client_email` as Editor |
| 403 "API has not been used" | Google Sheets API not enabled | Enable it in APIs & Services > Library |
| `WorksheetNotFound` | Tab name differs | Set `SHEET_TAB` and `CONFIG_TAB` to the exact tab names |
| Missing headers from `check` | A header was renamed | Restore the header names from `02-no-code-workflow.md` |
| 429 or `RESOURCE_EXHAUSTED` | Free Gemini limit reached | Lower `MAX_ROWS_PER_RUN`, raise `GEMINI_SLEEP_SECONDS`, read your limits at aistudio.google.com/rate-limit, or draft by hand |
| 404 model not found | `GEMINI_MODEL` is wrong or retired | Copy a current free model name from AI Studio |
| Draft is empty | Request blocked or too thin | Add real detail to `first_hand_angle` and rerun |
| `Refused: ... gate C2` | Status is not `SCRIPT_OK` | Edit the script, pass the gate, set the status yourself |
| `Refused: script.md still contains ...` | Unresolved markers | Fix every `[OWNER TO ADD]`, `[CHECK]`, `[STOP` |
| Kokoro error about espeak | espeak-ng missing | Install espeak-ng and reopen the terminal |
| Huge PyTorch download | GPU build pulled in | Install the CPU build first, as in Part 1 |
| Odd pronunciations | Names, numbers, abbreviations | Respell phonetically in `script.md`, use shorter sentences, listen again (gate C3) |
| Whisper is slow or the download stalls | First-run model download, slow CPU | Use `WHISPER_MODEL=base`, keep the cache step in the workflow |
| Wrong words in captions | Names and terms | Edit `captions.srt` by hand |
| `ffmpeg` not found | Not installed or not on PATH | Install it and reopen the terminal |
| Rough cut ends before the voice | Pictures shorter than audio | Add clips, raise `STILL_SECONDS` |
| Schedule did not run | GitHub can delay scheduled runs and may pause schedules in inactive repositories (VERIFY BEFORE RELYING: current rule at docs.github.com) | Use **Run workflow** by hand |
| Push fails with 403 | Workflow permissions are read-only | Set **Read and write permissions** |
| Minutes or storage used up | Private Free plan has 2,000 minutes and 500 MB | Check usage in Settings > Billing, shorten retention, render locally |
| Key shown in a log | A command printed environment values | Delete the key, create a new one, never print environment values |

## Done when

- [ ] `python -m pipeline.run check` prints OK and the status counts.
- [ ] One APPROVED row became a `script-v1.md` draft and the status SCRIPTED.
- [ ] You edited it into `script.md`, set SCRIPT_OK yourself, and the voice command rendered `voice.wav`.
- [ ] The voice command refused when you left an `[OWNER TO ADD]` marker in the file.
- [ ] `captions.srt` exists and you corrected at least the names.
- [ ] `rough-cut.mp4` plays, and you edited it in an editor before treating it as a video.
- [ ] The scheduled workflow ran once in a private repository, with no secrets in the repository files.
- [ ] Nothing in the project can upload or publish.

## Next

[06-custom-software.md](06-custom-software.md)
