# Setup Card: Fill This Once Per Channel

> **Purpose:** Capture every variable the rest of the repo uses, so any prompt can be pasted with no guessing.  
> **Use when:** Before you touch any other file, and again whenever you start modeling a new channel.  
> **Time needed:** 20 minutes for the card, 5 minutes to save it.  
> **Needs:** A browser, a text editor or notes app, and the channel you want to study open in a tab.  
> **Cost:** $0

## Inputs

Nothing from earlier files. This is the first file. You need to have chosen one reference channel to model (the channel whose style you study) and know roughly how many hours a week you can work.

How the card is used: every prompt in this repo contains placeholders in square brackets, such as [NICHE]. Before pasting a prompt into an AI chat, replace each bracketed placeholder with the value from your filled card. A prompt that still contains an unfilled bracket will produce vague output, so search the prompt for "[" before you send it.

## Steps

1. Copy the blank card below into a new plain-text or Markdown file. Name it `setup-card-<short-channel-name>.md`. Use one file per channel you model.
2. Fill each line using the guidance beside it. Do not leave a line empty. If you do not know a value yet, write your best current guess and mark it `(guess)`.
3. Compare your answers with the worked example further down (a fictional channel in the demonstration niche "home cooking on a budget").
4. Run prompt P-START-01 below to check the card for gaps and risk flags.
5. Save the card using the "How to save and reuse the filled card" section.
6. Follow the 10-step routine at the bottom of this file.

### The blank card

```text
SETUP CARD
[CHANNEL_URL]        =
[CHANNEL_NAME]       =
[NICHE]              =
[AUDIENCE]           =
[LANGUAGE]           =
[COUNTRY]            =
[HARDWARE]           =
[WEEKLY_HOURS]       =
[FACE_OR_FACELESS]   =
[VOICE_MODE]         =
[VIDEO_TOPIC]        =
[VIDEO_LENGTH]       =
[TRANSCRIPT]         =
[STYLE_BIBLE]        =
Own channel working title (notes only, never used in prompts) =
```

### Guidance for every variable

| Variable | What to write | Guidance |
|---|---|---|
| [CHANNEL_URL] | The full URL of the reference channel you are modeling | Open the channel page in a browser and copy the address bar, for example `https://www.youtube.com/@handle`. This is a public page. You study it by watching it; no downloading. |
| [CHANNEL_NAME] | The display name of that reference channel | Used only to label your analysis files. It never appears in content you publish. |
| [NICHE] | Your own channel's subject area, in one short phrase | Be narrower than a whole category. "Budget home cooking for one or two people" beats "food". |
| [AUDIENCE] | Who watches: age band, situation, and what they want | One sentence. Include the problem they have, not only demographics. |
| [LANGUAGE] | The language your videos are spoken and written in | One language per channel. Name the regional variant if it matters (for example British English). |
| [COUNTRY] | The country where you live and will receive payments | It affects payment, tax forms, and which monetization features are offered. VERIFY BEFORE RELYING on the YouTube Help page "YouTube Partner Program overview & eligibility" for your country. |
| [HARDWARE] | Your device and its limits | Write phone model or PC RAM, CPU, and GPU model or "no GPU". Folder 04-free-tool-stack.md picks tools from this line. |
| [WEEKLY_HOURS] | Hours per week you will actually work | Be honest. This sets how many videos per week the plan in 08-monetization assumes. |
| [FACE_OR_FACELESS] | One of: on-camera face, hands-only or object-only camera, screen recording, animation you draw yourself, voice with stock or generated visuals | Faceless is allowed, but the highest-risk version is stock footage plus text-to-speech with no original value. Choose a format that includes something only you make. |
| [VOICE_MODE] | One of: own recorded voice, free text-to-speech with disclosure review, hired voice actor with written license | Never a clone of a real person's voice. See 02-long-form/03-voice-and-audio.md later for the rules. |
| [VIDEO_TOPIC] | The topic of the single video you are working on now | Changes every video. Phrase it as a viewer problem or question. |
| [VIDEO_LENGTH] | Target length of the single video | For long form write minutes, for example "8 minutes". For Shorts write seconds, for example "40 seconds". |
| [TRANSCRIPT] | The text of one reference video's transcript | Open the video's watch page, click "...more" under the description, choose "Show transcript", and copy the text. Use it only as analysis input to extract structure. Never publish it or paraphrase it closely. |
| [STYLE_BIBLE] | Your finished Style Bible document | Leave blank now. You create it in 01-channel-dna and paste the whole text here afterward. |

### Worked example (fictional channel, demonstration niche)

The channel below is invented for demonstration. Replace every value with your own.

```text
SETUP CARD
[CHANNEL_URL]        = https://www.youtube.com/@ExampleBudgetKitchen   (fictional)
[CHANNEL_NAME]       = Example Budget Kitchen
[NICHE]              = Home cooking on a budget: dinners for one or two people under a fixed grocery cost
[AUDIENCE]           = Adults 22 to 40 living alone or with a partner, short on money and cooking time, who want dinners that cost little and need few dishes
[LANGUAGE]           = English (US)
[COUNTRY]            = Canada
[HARDWARE]           = Windows laptop, 8 GB RAM, Intel integrated graphics, no dedicated GPU; Android phone with a decent camera
[WEEKLY_HOURS]       = 10
[FACE_OR_FACELESS]   = Hands-only overhead kitchen camera filmed on my own phone, no face
[VOICE_MODE]         = Own recorded voice on the phone, cleaned up in free editing software
[VIDEO_TOPIC]        = Five dinners from one bag of rice and a can of chickpeas
[VIDEO_LENGTH]       = 8 minutes
[TRANSCRIPT]         = (pasted from one reference video's on-page transcript panel, 1,400 words)
[STYLE_BIBLE]        = (blank until folder 01-channel-dna is finished)
Own channel working title (notes only, never used in prompts) = Two Plates Cheap
```

What this example does right: the niche is narrow, the audience has a stated problem, the hardware line lets later files pick tools, and the format (hands-only camera, own voice) contains original footage and original narration, which keeps the channel away from the templated, stock-footage-plus-text-to-speech pattern that YouTube treats as high risk (verified 2026-10-20).

## How to save and reuse the filled card

1. Save the file as `setup-card-<short-channel-name>.md`. Keep it outside the shared part of the repo if you publish the repo anywhere, since it contains your hardware and country.
2. Keep a second copy in a cloud notes tool you already use (a Google Doc or the notes app on your phone) so you can paste from a phone.
3. At the start of every new AI chat session, paste the whole card as the first message, preceded by this single line: `Here is my setup card. Use these values for every bracketed placeholder in prompts I paste later.`
4. After finishing 01-channel-dna, paste the full Style Bible text into the [STYLE_BIBLE] line and save the card again. Add a date in the filename when you change it, for example `setup-card-budgetkitchen-2026-11-02.md`, and keep the older one.
5. If a chat tool loses context, repeat step 3. Never rely on the chat remembering the card.

## Prompts

### P-START-01 — Setup Card Gap and Risk Check

**Purpose:** Find empty, vague, or risky lines in your filled card before you build on it.

**Inputs:** Your filled setup card (all fourteen variables).

```text
You are a YouTube channel strategist reviewing a setup card before production starts. Review the card below line by line.

SETUP CARD:
[PASTE YOUR FILLED CARD HERE]

Do the following and print the results in this order:

1. TABLE: one row per variable, with columns Variable, Status (Complete / Vague / Missing), and a one-sentence fix if the status is not Complete. [STYLE_BIBLE] and [TRANSCRIPT] may be blank at this stage; mark them "Expected blank" if so.
2. RISK FLAGS: list every line that raises a YouTube monetization or compliance risk, using these checks only:
   a. The format combines stock footage or generated visuals with text-to-speech and contains no original footage, commentary, or teaching.
   b. The niche involves health, medical, legal, or financial advice delivered by an AI-generated persona.
   c. The plan implies publishing many near-identical videos from one template.
   d. The voice mode involves imitating a real person.
   For each flag, quote the line, name the risk in one sentence, and propose a safer alternative that costs $0.
3. FEASIBILITY: using [WEEKLY_HOURS] and [HARDWARE], state in numbers how many finished long videos and how many Shorts per week are realistic, and show the arithmetic in two or three lines.
4. NICHE SHARPENING: rewrite [NICHE] and [AUDIENCE] each in one sentence so they are narrower and name a viewer problem.

Do not give income predictions. Do not invent YouTube policy wording; if a policy question comes up, say VERIFY BEFORE RELYING and name the official YouTube Help page to check.
```

**Expected output:** A 14-row table, a short list of risk flags with free alternatives, a feasibility calculation, and two rewritten sentences.

**If the output is weak:** Paste only the lines that came back Vague, add one sentence of real context for each (for example what equipment you own), and rerun with the instruction "Review only these lines."

## The 10-step routine for every new channel

Run these in order. Each step names the folder and the first file to open. Steps 2 to 9 each end by saving their output into your notes under the folder name.

1. **Fill and check the card.** Finish this file, run P-START-01, then read [02-principles-and-copy-line.md](02-principles-and-copy-line.md), [03-compliance-master-checklist.md](03-compliance-master-checklist.md), and [04-free-tool-stack.md](04-free-tool-stack.md).
2. **Channel DNA.** Gather public data and build the Style Bible. Start at [../01-channel-dna/01-data-gathering.md](../01-channel-dna/01-data-gathering.md). Paste the finished Style Bible into [STYLE_BIBLE] on your card.
3. **Long-form system.** Analyze one reference video, then script, voice, visuals, and metadata for your own new long video. Start at [../02-long-form/01-video-dna-analysis.md](../02-long-form/01-video-dna-analysis.md).
4. **Shorts system.** Same method for vertical videos, with separate prompts. Start at [../03-shorts/01-shorts-dna-analysis.md](../03-shorts/01-shorts-dna-analysis.md).
5. **Thumbnails.** Extract composition patterns and generate original thumbnails. Start at [../04-thumbnails/01-thumbnail-dna-analysis.md](../04-thumbnails/01-thumbnail-dna-analysis.md).
6. **Originality layer.** Score every script, thumbnail, and title for distance from the reference and for original value before publishing. Start at [../05-originality-layer/01-differentiation-method.md](../05-originality-layer/01-differentiation-method.md). In practice you return here after each draft in steps 3 to 5.
7. **Automation.** Only after you have made at least three videos by hand, design the repeating parts of the pipeline with human checkpoints. Start at [../06-automation/01-pipeline-architecture.md](../06-automation/01-pipeline-architecture.md).
8. **Build-your-own ideas.** Pick optional tools and small software projects that remove your slowest manual step. Start at [../07-build-your-own/01-ideas-research-and-ideation.md](../07-build-your-own/01-ideas-research-and-ideation.md).
9. **Monetization plan.** Read the reality and timeline math first, then follow the 30-day plan. Start at [../08-monetization/01-reality-and-timeline-math.md](../08-monetization/01-reality-and-timeline-math.md).
10. **Operate and repeat.** Use the quick start, the troubleshooting FAQ, and the tracking sheet each week. Start at [../09-operations/01-quick-start.md](../09-operations/01-quick-start.md). To model another channel, copy a fresh blank card and return to step 1.

## Done when

- All fourteen variable lines are filled, or marked `(guess)` or "blank until folder 01 is finished" where the guidance allows it.
- P-START-01 returned no line with status Missing and every risk flag has a chosen alternative.
- The card is saved in two places with a dated filename.
- You can name, without looking, the folder you will open for step 2.

## Next

[02-principles-and-copy-line.md](02-principles-and-copy-line.md)
