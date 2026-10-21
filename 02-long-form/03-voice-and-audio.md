# Voice and Audio (Long-Form)

> **Purpose:** Produce clean, correctly mixed, correctly licensed narration and sound for a long-form video using only free tools.  
> **Use when:** Script v2 has passed P-LONG-07 and P-LONG-08 and you are ready to record or synthesize the voice.  
> **Time needed:** 1.5 to 3 hours for a 10-minute video the first time; 45 minutes once set up.  
> **Needs:** Script from `02-script-prompt-chain.md`, a phone or PC, Audacity (free), FFmpeg (free), optionally Python 3.  
> **Cost:** $0  

## Inputs

- [VOICE_MODE] from the setup card. This file reads it as one of: own voice, free TTS (text-to-speech), or mixed. If your card uses other words, map them to these three.
- [LANGUAGE], [HARDWARE], [WEEKLY_HOURS], [FACE_OR_FACELESS].
- The final script (`videos/<slug>/06-script-v2.md` after fact-check fixes).
- Defined here: [TTS_ENGINE] (Kokoro or Piper), [PRONUNCIATIONS] (a list you build in Step 9), [SCRIPT_V3] (the script after fact-check), [WORDS_PER_MINUTE].

## Steps

### A. Pick the path

1. **Own voice** is the strongest option for originality and removes the synthetic-voice questions entirely. Use it if you can talk for 10 minutes without distress. **Free TTS** is acceptable when the video has real original commentary, teaching, or testing; YouTube's July 2026 clarification says AI voiceover can qualify for monetization when the video carries original value, and that the policy targets mass-produced templated output rather than AI itself (verified 2026-10-20). **Mixed** means your voice for the hook and key opinions and TTS for the rest; cut it so the change is not jarring.

### B. Recording your own voice (phone or PC)

2. **Choose the room.** Record in the smallest soft room you have: a walk-in closet with clothes, or a bed with a duvet pulled over you and the phone. Avoid kitchens, bathrooms, and rooms with bare walls. Turn off fans, air conditioners, and fridges for the take. Close windows facing traffic.
3. **Place the microphone.** Phone: bottom edge about 15 to 20 cm from your mouth, slightly off to the side so breath does not hit it. Wired earbuds with an inline mic are better than a laptop mic when you have nothing else. Keep the distance the same for the whole session.
4. **Set the recording format.** Best: record directly into Audacity on a PC. In Audacity open **Edit > Preferences > Audio Settings**, set **Recording Channels** to **1 (Mono)**, and **Project Rate** to **48000 Hz**. Phone alternative: use the built-in voice recorder at its highest quality setting (on iPhone, **Settings > Voice Memos > Audio Quality > Lossless**; VERIFY BEFORE RELYING because menu names change by version). Do not use a recorder that applies automatic noise suppression or auto-gain if you can turn it off.
5. **Record 10 seconds of silence first** at the start of every session. Audacity needs it as a noise sample.
6. **Record in short takes**, one paragraph per take. Clap once at the start of each take to give yourself a sync point. If you stumble, pause for 2 seconds and repeat the sentence; you will cut the bad take later.
7. **Clean the voice in Audacity** (menu names are from Audacity 3.x; VERIFY BEFORE RELYING if your version differs). Apply in this order:
   1. Select the 10 seconds of silence. **Effect > Noise Removal and Repair > Noise Reduction > Get Noise Profile**.
   2. Select all (Ctrl+A). Same menu again. Noise reduction 6 to 12 dB, Sensitivity 6.00, Frequency smoothing 3 bands. Preview. If the voice sounds watery, lower the dB value.
   3. **Effect > EQ and Filters > High-Pass Filter**, frequency 80 Hz, roll-off 12 dB per octave. This removes rumble.
   4. **Effect > Volume and Compression > Compressor**: Threshold -18 dB, Noise floor -40 dB, Ratio 2:1, Attack 10 ms, Release 200 ms, Make-up gain on. Light compression only.
   5. **Effect > Volume and Compression > Loudness Normalization**: normalize perceived loudness to **-16 LUFS** (voice only; the final mix target is set in Step 14).
8. **Export** the voice with **File > Export > Export as WAV**, 48000 Hz, 24-bit PCM, named `voice.wav` in the video's folder.

### C. Free text-to-speech

9. **Prepare the text.** Run P-LONG-10 below to turn the script's spoken lines into numbered TTS chunks with pause and pronunciation notes. Keep the [PRONUNCIATIONS] table; you will reuse it for every video.
10. **Choose the engine.** Both engines below have no voice cloning, only fixed voices, and that is the point: this repo never clones a real person's voice.

| Engine | License (verified 2026-10-20) | Needs | Trap | Free fallback |
|---|---|---|---|---|
| Kokoro (82M parameters, Python) | Apache-2.0 for the code and model | Python 3, `pip install kokoro soundfile`, espeak-ng for some languages; runs on CPU, faster on GPU | Language coverage is smaller than cloud engines; check that your [LANGUAGE] has a Kokoro voice | Piper |
| Piper (OHF-Voice/piper1-gpl) | The current maintained repo is GPL-3.0-or-later. The original rhasspy/piper repo was MIT and was archived in October 2025 | `pip install piper-tts`, a downloaded voice file | **Each voice model has its own license.** Open the voice's model card and confirm it allows commercial use before publishing; VERIFY BEFORE RELYING | Kokoro, or record your own voice |

    If neither covers your [LANGUAGE], check the free tier of a cloud TTS service on its official pricing page and read its commercial-use and attribution terms. Do not use a free tier whose terms say "non-commercial" for a channel you intend to monetize.
11. **Install and test Kokoro.** In a terminal: `python -m venv tts-env`, activate it (`tts-env\Scripts\activate` on Windows, `source tts-env/bin/activate` on macOS or Linux), then `pip install kokoro soundfile`. Install espeak-ng from your package manager or its releases page if the first run complains. Save the following as `make_voice.py` next to your `tts_lines.txt`. If a function name has changed in your installed version, check the Kokoro model card on Hugging Face (hexgrad/Kokoro-82M): VERIFY BEFORE RELYING.

```
import re
import numpy as np
import soundfile as sf
from kokoro import KPipeline

SR = 24000
pipe = KPipeline(lang_code="a")   # a = American English, b = British English
VOICE = "af_heart"                # change voice here
SPEED = 0.95

chunks = []
for line in open("tts_lines.txt", encoding="utf-8"):
    m = re.match(r"(\d+)\|(.*)", line.strip())
    if not m:
        continue
    text = m.group(2).strip()
    pause = 0.45
    p = re.search(r"\[PAUSE ([0-9.]+)\]\s*$", text)
    if p:
        pause = float(p.group(1))
        text = text[:p.start()].strip()
    for _, _, audio in pipe(text, voice=VOICE, speed=SPEED):
        chunks.append(np.asarray(audio, dtype="float32"))
    chunks.append(np.zeros(int(SR * pause), dtype="float32"))

sf.write("voice_raw.wav", np.concatenate(chunks), SR)
print("done")
```

    Run `python make_voice.py`. Listen to the first 30 seconds before running the whole script.
12. **Piper instead:** follow the README at the OHF-Voice/piper1-gpl repository for the exact download and run commands for your version (VERIFY BEFORE RELYING); the shape is: download a voice, then pass text in and get a WAV out. Generate one WAV per chunk and join them with silences using Audacity (**Tracks > Add New > Mono Track**, then **Generate > Silence**).
13. **Make it sound human.**
    - Generate by sentence group, not as one block, so each chunk has its own intonation.
    - Write commas where a speaker would breathe. Break any sentence over 25 words.
    - Use pauses of 0.3 s after commas inside a chunk (by splitting), 0.45 to 0.6 s between sentences, 0.8 to 1.0 s before a key reveal.
    - Try speeds 0.92 to 1.0. Faster than 1.05 sounds mechanical.
    - Vary the voice only if the Style Bible has two speakers; otherwise keep one voice for the whole channel.
    - Fix mispronunciations by respelling the word in the text (for example write the name as it sounds), or use the engine's phoneme syntax if the model card documents it. Record every fix in [PRONUNCIATIONS].
    - Add a quiet room-tone bed (a free 20-second ambience loop from a licensed source, logged in the music log below) at about -45 dB under the voice, so silence does not sound digital.
    - Cut audible glitches out by hand; re-generate only that chunk.
    - Run the same cleanup as own voice from Step 7.3 to 7.5 (skip noise reduction).

### D. Mixing and loudness

14. **Targets.** Aim for integrated loudness of **-14 LUFS** (acceptable range -15 to -13) with true peak at or below **-1 dBTP** for the final mix. This is the widely used convention for YouTube; YouTube Help does not publish an official number, so this is a practical target, not a rule (verified 2026-10-20; VERIFY BEFORE RELYING by searching "YouTube loudness" on YouTube Help). Louder files are turned down by YouTube's playback normalization, so pushing past -14 buys nothing and costs dynamics.
15. **Level the tracks** in your editor (see `04-visual-production.md`). Starting values: voice peaks around -6 dBFS; music bed about 18 to 22 dB under the voice while speaking, rising to about 10 to 12 dB under the voice during silent beats; sound effects around the voice level or slightly below. Adjust by ear on headphones and on a phone speaker. Use ducking or keyframes so music dips by about 6 dB before each sentence begins and returns after it ends.
16. **Measure instead of trusting your ears.** Export the final audio or the whole video and run:

```
ffmpeg -i final.mp4 -af ebur128=peak=true -f null -
```

    Read the summary at the end: **I** is integrated loudness in LUFS, **True peak** is in dBFS. Target I between -15 and -13, true peak no higher than -1.0. Free alternatives: the Youlean Loudness Meter's free edition (check its page for the current free limits; VERIFY BEFORE RELYING), or DaVinci Resolve's loudness meter on the Fairlight page.
17. **Fix loudness.** If I is too low or too high, apply the gain difference on the master, then check true peak again. For a precise automatic fix, FFmpeg's two-pass loudnorm filter works: first `ffmpeg -i voice_mix.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null -`, then use the printed measured values in a second command with `loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=...:measured_TP=...:measured_LRA=...:measured_thresh=...:offset=...`. Re-measure with the command in Step 16.
18. **Listen on three devices:** headphones, laptop speakers, and a phone speaker. If the voice is hard to follow on the phone, raise the voice or lower the music by 2 dB.

### E. Music and sound effects: sources and proof

19. **Where to get music and sound effects at $0** (check each license page at download time; VERIFY BEFORE RELYING on anything not marked verified):

| Source | What it gives | License notes | Trap |
|---|---|---|---|
| YouTube Audio Library (YouTube Studio > **Audio Library**) | Music and sound effects | Tracks can be filtered by attribution requirement. Tracks marked "YouTube Audio Library License" need no credit. Creative Commons "attribution" tracks require you to paste the provided credit text into your description. YouTube says YPP creators can monetize videos using Audio Library tracks (verified 2026-10-20) | Many creators use the same tracks, so the sound is not distinctive. Never edit the attribution text. Do not confuse with **Creator Music**, which licenses popular songs for a fee or revenue share: not $0 |
| Pixabay music and sound effects | Music, SFX | Pixabay's own content license; read the current terms | Individual uploads can be re-uploaded elsewhere under other terms. Download only from Pixabay itself |
| Free Music Archive | Music | License differs per track | Some tracks are non-commercial; filter for commercial use |
| Freesound | Sound effects | License differs per sound | Only use CC0, or CC-BY with attribution; avoid "NonCommercial" |
| Your own sounds | Foley, kitchen noises, room tone | You own them | None |
| Free AI music generators | Generated tracks | Free tiers often restrict commercial use or leave the rights with the service | Do not use free-tier output in a monetized video unless the terms you read on the day of use say so in plain words |

20. **Keep proof for every track and effect.** Create `music-log.csv` in the video folder with the columns below and fill one row per file used. Take a screenshot of the license page the day you download, and save it in `proof/` with the file name in the log.

```
file_name,title,artist_or_creator,source_site,source_url,license_name,license_url,attribution_text_required,attribution_text,date_downloaded,screenshot_file,used_in_video_slug
```

21. **If a Content ID claim appears** on a track with a valid license, open YouTube Studio > **Content**, find the video, open the claim under **Copyright**, and dispute it using the license URL and screenshot. If you cannot prove the license, replace the track and re-upload rather than argue.
22. **Never** use a popular song, a clip from a movie or show, or a track "from the channel I am modelling," even for a few seconds. Do not use AI music tools that are marketed as imitating a named artist's voice.

### F. The AI-voice disclosure decision

23. In YouTube Studio, during upload, open **Details** and find **Altered content** (YouTube Help calls it the "altered content" setting). YouTube requires disclosure of meaningfully altered or synthetic content when it seems realistic. Its Help page lists voice cloning someone else's voice for voiceover as requiring disclosure, and lists synthetic music (including Creator Music) and unrealistic content as not requiring it. It also says disclosure does not limit a video's audience or affect monetization eligibility (verified 2026-10-20). YouTube may add the label on its own if it decides content is realistic and undisclosed. Sources disagree on whether a generic AI narrator needs the label, so use this table and quote the current Help wording yourself: VERIFY BEFORE RELYING at YouTube Help, "Disclosing use of altered or synthetic content".

| Situation | Choose "Yes"? | Reason |
|---|---|---|
| Your own recorded voice, with ordinary cleanup | No | Not synthetic; noise reduction is a minor edit |
| Generic TTS narrator reading your own script, obviously an artificial narrator, no real person imitated | In doubt: **Yes** | The Help text does not list this case; sources disagree; disclosing costs nothing in reach or monetization |
| TTS voice presented as a real, identifiable person, or reading invented statements as if that person said them | Yes, and do not publish it | Impersonation; against this repo's rules |
| Any clone of a real person's voice | Not allowed | Hard rule of this repo; it also requires disclosure |
| AI voice for an obviously animated or fictional character | No | Unrealistic |
| Realistic AI-generated footage of events, places, or people | Yes | Realistic synthetic visuals |
| AI-generated music | No for the label | Listed as not requiring disclosure; still check the generator's license |

24. **When you answer Yes**, also add one plain sentence to the description such as "Narration uses a synthetic voice." Do this even when you answered No for borderline cases. Add the same line to your `per-video-checklist` in `../templates/per-video-checklist.md`.

## Prompts

### P-LONG-10 — TTS Script Preparation

**Purpose:** Convert the final script into numbered chunks a TTS engine reads well, plus a pronunciation table.

**Inputs:** [SCRIPT_V3] (VOICE lines only), [LANGUAGE], [TTS_ENGINE], [WORDS_PER_MINUTE], [PRONUNCIATIONS] (existing table, or "none").

```
Prepare this script for text-to-speech with [TTS_ENGINE] in [LANGUAGE]. Use only the VOICE lines; ignore SCREEN and SOUND lines.
Script: [SCRIPT_V3]
Existing pronunciation fixes: [PRONUNCIATIONS]

OUTPUT 1: TTS LINES. One chunk per line, in this exact format: three-digit number, a vertical bar, the text. Example shape: 001|Text of the first chunk.
Rules: each chunk is one to three sentences and under 250 characters; never split inside a sentence; expand numbers, symbols, abbreviations, units, and dates into words as they are said; replace special characters the engine may read aloud; if a pause is needed after a chunk, end the line with [PAUSE x] where x is seconds (0.3 to 1.0); use 0.8 to 1.0 only before reveals; do not change the meaning or the wording except to make it speakable, and mark each such change in OUTPUT 3.

OUTPUT 2: PRONUNCIATION TABLE. Columns: Word | Why risky | Respelling to use in the text | Chunk numbers. Include names, brands, foreign words, acronyms, and homographs (words spelled the same but said differently).

OUTPUT 3: CHANGE LOG. Each place where you changed wording for speech, with chunk number and the old and new text.

OUTPUT 4: ESTIMATE. Total words, estimated duration at [WORDS_PER_MINUTE], total pause seconds, and the estimated final length.
Do not add content. Do not remove any [CLAIM-nn] tags from the change log.
```

**Expected output:** A block of numbered lines to paste into `tts_lines.txt`, a pronunciation table, a change log, and a duration estimate.

**If the output is weak:** If chunks are too long, reply: "Resplit every chunk over 200 characters at a sentence boundary and renumber." If the assistant paraphrases, reply: "Restore the original wording in all chunks except where OUTPUT 3 lists a speech-only change."

### P-LONG-11 — Audio Cue Sheet and Search Brief

**Purpose:** Turn the script into a music and sound-effect plan with search terms for licensed sources, so you do not browse aimlessly.

**Inputs:** [SCRIPT_V3], [STYLE_BIBLE] (audio section), [DNA_REPORT] (sections 7 and 8), [VIDEO_LENGTH].

```
Create an audio cue sheet for this video. Script: [SCRIPT_V3]. Length: [VIDEO_LENGTH].
Style Bible audio rules: [STYLE_BIBLE]
Modelled channel's sound mechanics (timing and loudness patterns only): [DNA_REPORT]

OUTPUT A: MUSIC PLAN. A table: Time range | Role (bed, tension, payoff, outro) | Mood and tempo in plain words | Instruments to prefer or avoid | Energy change at start and end | Search terms to type into the YouTube Audio Library and Pixabay music (give 3 terms per row).
OUTPUT B: SOUND-EFFECT LIST. A table: Time | Moment in script | Effect type | Length in seconds | Search terms for Freesound (CC0) and the YouTube Audio Library. Use effects only where they help comprehension or rhythm; keep the count within the modelled channel's average.
OUTPUT C: SILENCE POINTS. Where the music drops out on purpose.
OUTPUT D: MIX NOTES. Music level under voice in dB for each role, ducking points, and the final loudness target (-14 LUFS integrated, true peak at or below -1 dBTP).
OUTPUT E: LICENSE TASKS. A checklist for the music log: one row per track to fill, and a reminder to screenshot each license page.
Do not name specific copyrighted songs or artists as references. Describe sounds in words only.
```

**Expected output:** Five tables and lists that you can work through while browsing the sources in Step 19.

**If the output is weak:** Reply: "Give me search terms that are specific to instruments and tempo, not just 'upbeat'."

## Done when

- [ ] `voice.wav` (or `voice_raw.wav` plus cleanup) exists, 48 kHz, free of clicks and background noise.
- [ ] You measured the final mix: integrated loudness between -15 and -13 LUFS, true peak at or below -1 dBTP.
- [ ] `music-log.csv` has one row per music or sound file, each with a license URL and a screenshot in `proof/`.
- [ ] Any attribution text is saved for the description.
- [ ] Your Altered content answer is decided with the table and recorded in the per-video checklist.
- [ ] No cloned voice, no copyrighted song, and no non-commercial track is in the project.

## Next

Continue to [04-visual-production.md](04-visual-production.md).
