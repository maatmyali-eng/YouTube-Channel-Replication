# Workflow A: No-Code Pipeline (Sheets, Forms, Free Automation Tier, Free LLM)

> **Purpose:** Build a working script-drafting and metadata-drafting pipeline with no code, using Google Forms, Google Sheets, a free automation tier, and a free LLM tier.  
> **Use when:** You have never automated anything, or you want a pipeline you can rebuild in under two hours.  
> **Time needed:** 90 to 120 minutes for setup, then about 10 minutes per week to run.  
> **Needs:** A Google account, a free Make account, a free Google AI Studio API key.  
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [VIDEO_LENGTH]
- [STYLE_BIBLE] (the saved output of P-CDNA-02)
- The stage cards and file names from `01-pipeline-architecture.md`

## What this workflow is, and what it is not

Workflow A has three layers. Build them in order.

1. **Layer 1, Sheets and Forms only.** A Google Form feeds a Google Sheet. Every prompt is pasted by hand into a free chat tool. This layer always works and never breaks.
2. **Layer 2, one free automation scenario per task.** A Make scenario reads rows from the sheet, sends a prompt to the Gemini API, and writes the draft back. A person reviews every draft.
3. **Upgrade, not part of this file.** Google Apps Script is code, so it is not no-code. If you outgrow the free limits below, the upgrade path is `05-low-code-workflow.md`.

This workflow ends at a draft in a cell. It never uploads, never schedules, and never changes a status past the point where a human gate in `04-human-checkpoints.md` applies. Fully automated publishing of unreviewed videos is the main demonetization risk, and this workflow is built so that it cannot happen.

## Free-tier limits (verified 2026-10-20)

| Tool | Free limits | Trap | Free fallback |
|---|---|---|---|
| Make Free | 1,000 credits per month, 2 active scenarios, 15-minute minimum interval, 5-minute execution limit, 5 MB files, 7-day logs | Every module that runs uses credits, and retries use credits. Scenarios stop until the next cycle when credits run out. Credit counting details: VERIFY BEFORE RELYING at make.com/pricing | Layer 1: paste prompts by hand |
| Zapier Free | 100 tasks per month, two-step Zaps, 15-minute polling. Webhooks, premium apps and AI Fields are paid. "AI by Zapier" is not available on Free | Two steps means one trigger and one action. Reading a row, calling an LLM and writing back needs three steps, so it cannot run on Free | Use Make, or Layer 1 |
| Gemini API free tier through Google AI Studio | A free API key with no billing needed. Per-model limits are not published in the docs. They are shown per project at aistudio.google.com/rate-limit. Preview models are limited more tightly | Google's pricing page says free-tier requests may be used to improve Google products. Do not send private or unreleased material you must keep confidential. Free-tier availability by model: VERIFY BEFORE RELYING at ai.google.dev/gemini-api/docs/pricing | The free Gemini app at gemini.google.com (compute-based limits that reset on a schedule), pasted by hand |
| Google Sheets `=AI()` function | Requires an eligible Google Workspace plan or a Google AI plan | Not $0 on a personal account | Do not use it. Use the Make module instead |
| Google Sheets and Forms | Free with a Google account. Spreadsheet size and cell character limits: VERIFY BEFORE RELYING at support.google.com/docs | A very long script in one cell can hit the cell character limit | Store the script as a Google Doc link and keep only the link in the cell |

Why Make and not Zapier: Zapier Free allows two-step Zaps only. The drafting job needs three steps (find the row, generate, write back), so Make Free is the only one of the two that can do it at $0. Zapier Free can still send you a notification when a row changes status, which is a two-step job.

## Steps

### Part 1. Build the intake form

1. Go to forms.google.com and select **Blank form**. Title it `[CHANNEL_NAME] Idea Intake`.
2. Add these questions, in this order. Set questions 1 and 4 to **Required**.
   1. `Topic idea` (Short answer)
   2. `Format` (Multiple choice: Long, Short)
   3. `Audience question this answers` (Short answer)
   4. `First-hand angle: what have you personally tested, made, measured, or lived that the video will show?` (Paragraph)
   5. `Source links you will check` (Paragraph)
3. Open the **Responses** tab and select **Link to Sheets**. Choose **Create a new spreadsheet**. Name it `[CHANNEL_NAME] Pipeline`.
4. Open the new spreadsheet. Rename the tab `Form Responses 1` to `Intake`.

### Part 2. Build the Pipeline sheet

5. Add a tab named `Pipeline`. Type these headers in row 1, in this exact order, and never rename or reorder them later. Add new columns only at the far right.

| Col | Header | Filled by |
|---|---|---|
| A | slug | You |
| B | format | You (Long or Short) |
| C | status | Dropdown |
| D | topic | You or P-AUTO-02 |
| E | audience_question | You |
| F | first_hand_angle | You |
| G | value_stack_layers | You (from P-ORIG-02) |
| H | outline | Make or you |
| I | script_draft | Make |
| J | script_final_link | You (link to your edited Google Doc) |
| K | factcheck_notes | You (from P-LONG-07) |
| L | voice_file | You |
| M | thumb_text | You |
| N | title | Make or you |
| O | description | Make or you |
| P | disclosure_decision | You |
| Q | orig_score | You (from P-ORIG-01) |
| R | reviewer_initials | You |
| S | scheduled_date | You |
| T | publish_url | You |
| U | notes | You |
| V | last_updated | Make |

6. Select column C. Open **Data > Data validation > Add rule**. Under Criteria choose **Dropdown** and enter these values, one per option: IDEA, APPROVED, SCRIPTED, SCRIPT_OK, VOICED, VISUALS_DONE, EDITED, THUMB_DONE, META_DONE, REVIEW_PASSED, SCHEDULED, PUBLISHED, ANALYSED, HOLD, KILLED. Menu labels can change, so if you cannot find them, press Alt+/ and search for "Data validation".
7. Add a tab named `Config`. In cell A1 type `channel_name`, B1 your [CHANNEL_NAME]. In A2 type `style_bible`, and paste the full [STYLE_BIBLE] into B2. In A3 type `video_length`, B3 your [VIDEO_LENGTH]. In A4 type `language`, B4 your [LANGUAGE].
8. Add a tab named `Log` with headers `timestamp`, `scenario`, `slug`, `result`.
9. In `Pipeline`, copy each approved idea from `Intake` into a new row by hand. Fill A to G. Do not change status to APPROVED until you have passed gate C1: column F and column G must both be filled.

### Part 3. Create the API key

10. Go to aistudio.google.com and sign in. Select **Get API key**, then **Create API key**. Copy it once.
11. Do not paste the key into the sheet, a document, or a chat. It goes only into the Make connection in the next part.

### Part 4. Scenario 1: draft scripts

12. Go to make.com and create a free account. Select **Create a new scenario**.
13. Add module 1: **Google Sheets > Search Rows**. Connect your Google account. Choose the `[CHANNEL_NAME] Pipeline` spreadsheet and the `Pipeline` sheet. Set filters: column C equals `APPROVED`, and column F is not empty, and column G is not empty. Set **Maximum number of returned rows** to 3.
14. Add module 2: **Google Gemini AI > Generate a Response**. When asked, create a connection and paste the API key from step 10. Choose a Flash-class model that is not a preview model and that the pricing page lists as free (VERIFY BEFORE RELYING: model availability changes). Paste P-AUTO-03 into the prompt field. For each square-bracket token in the prompt, delete the token and pick the matching column from the mapping panel: [TOPIC] is column D, [AUDIENCE_QUESTION] is E, [FIRST_HAND_ANGLE] is F, [VALUE_STACK_LAYERS] is G, [FORMAT] is B. Map [STYLE_BIBLE], [CHANNEL_NAME], [VIDEO_LENGTH] and [LANGUAGE] from the `Config` tab with a second **Google Sheets > Get a Cell** module placed before module 2, or type the values directly if you prefer.
15. Add module 3: **Google Sheets > Update a Row**. Use the row number from module 1. Set column I (script_draft) to the Gemini text, column C to `SCRIPTED`, and column V to the function `now`.
16. Set the schedule. Select the clock on module 1 and choose **On demand**. You will press **Run once** yourself. Do not set 15-minute polling, because each poll costs credits.
17. Select **Save**, then **Run once**. Check the sheet. Column I should hold a draft and column C should read `SCRIPTED`.

Credit estimate (VERIFY BEFORE RELYING at make.com/pricing): a run that finds 3 rows uses about 1 credit for the search plus 2 for each row, which is 7 credits. Running it twice a week stays far below 1,000 credits per month.

### Part 5. Scenario 2: draft metadata

18. Create a second scenario. Module 1: **Google Sheets > Search Rows** with column C equal to `THUMB_DONE`, column N empty, maximum 3 rows. Module 2: Gemini **Generate a Response** with P-AUTO-04. Module 3: **Update a Row** with column N set to the title block, column O set to the description, column C unchanged. Set it to **On demand**. This uses your second and last free scenario slot.
19. Keep status at `THUMB_DONE` after Make writes. Only you move it to `META_DONE`, after gates C6 and C7.

### Part 6. Weekly run

20. Fill the `Intake` form from your phone during the week. On batch day, copy the best ideas into `Pipeline`, set them to `APPROVED`, and press **Run once** on Scenario 1.
21. For every drafted row, open the draft, edit it into a Google Doc, and paste the link into column J. Run P-LONG-07 and P-ORIG-01 in a chat tool, paste results into K and Q, then set the status to `SCRIPT_OK`.

## Prompts

### P-AUTO-02 — Batch Idea Rows

Purpose: Generate candidate rows for the `Pipeline` tab that you can paste straight into the sheet.
Inputs: [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [STYLE_BIBLE], [PUBLISHED_TITLES] (the titles already in column N or on the channel), [FIRST_HAND_ASSETS] (what you can personally test, make, measure, or show).

```
You are an editorial planner for [CHANNEL_NAME], a channel about [NICHE] for [AUDIENCE], written in [LANGUAGE].
Style Bible: [STYLE_BIBLE]
Already published or queued titles (do not repeat or paraphrase): [PUBLISHED_TITLES]
What the owner can personally test, make, measure, or show: [FIRST_HAND_ASSETS]

Write 15 candidate videos: 10 Long and 5 Short. Output as tab-separated rows with no header and no extra text, in this order:
format | topic | audience_question | first_hand_angle | value_stack_layers

Rules:
1. Every row must be grounded in something listed in the owner's first-hand assets. If a topic needs something the owner does not have, leave it out.
2. value_stack_layers names at least 3 of these 5 layers: first-hand evidence, original analysis, original visuals or demonstration, a clear point of view, practical utility. At least one must be first-hand evidence.
3. Topics must not repeat any listed title and must not copy another creator's video concept, wording, or structure. Use the style, not the content.
4. No health, finance, or legal advice topics unless the owner's assets show real qualification. If a topic touches those areas, prefix the topic with "SENSITIVE:".
5. No claims you cannot support. No clickbait the video cannot deliver.
```

Expected output: 15 tab-separated lines you paste into columns B, D, E, F, G.
If the output is weak: Add three real examples of your best past topics to [FIRST_HAND_ASSETS], and ask for 15 new rows that avoid the weak ones you name.

### P-AUTO-03 — Script Draft From One Row

Purpose: The prompt Scenario 1 sends for each `APPROVED` row. It produces a first draft with clear gaps for you to fill.
Inputs: [CHANNEL_NAME], [LANGUAGE], [STYLE_BIBLE], [VIDEO_LENGTH], [FORMAT], [TOPIC], [AUDIENCE_QUESTION], [FIRST_HAND_ANGLE], [VALUE_STACK_LAYERS].

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

Expected output: A script with visible gaps and a GAPS list.
If the output is weak: If the draft is generic, add two sentences of real detail to the row's first_hand_angle column and run the row again. If the tone is off, paste three short passages of your own writing into the prompt before the Style Bible.

### P-AUTO-04 — Metadata Draft From One Row

Purpose: The prompt Scenario 2 sends for each `THUMB_DONE` row.
Inputs: [CHANNEL_NAME], [LANGUAGE], [TOPIC], [AUDIENCE_QUESTION], [SCRIPT_FINAL], [THUMB_TEXT].

```
You write YouTube metadata for [CHANNEL_NAME] in [LANGUAGE].
Topic: [TOPIC]. Viewer question: [AUDIENCE_QUESTION]. Thumbnail text: [THUMB_TEXT].
Final script: [SCRIPT_FINAL]

Output exactly:
TITLES: 5 options, each under 60 characters, each accurate to the script, none that overpromise.
DESCRIPTION: 2 sentences that state what the viewer will learn, then a chapter list with timestamps only for chapters that exist in the script, then one line naming sources used.
KEYWORDS: 8 plain phrases a viewer would type.
MISMATCH CHECK: list any title or thumbnail claim the script does not support.

Rules: No deceptive wording, no fake urgency, no claims of results the video does not show, no other creator's names or brands used to attract search traffic.
```

Expected output: Five titles, a description, keywords, and a mismatch list.
If the output is weak: If the mismatch list is empty but titles overpromise, ask for five new titles that quote a specific fact from the script.

### P-AUTO-05 — Workflow Failure Diagnosis

Purpose: Find the cause when a scenario fails or writes nothing.
Inputs: [ERROR_TEXT] (the message from the Make history tab), [SCENARIO_MODULES] (the list of modules and their settings in plain text), [SHEET_HEADERS] (row 1 of `Pipeline`).

```
I run a no-code Make scenario on the free plan with Google Sheets and the Gemini API.
Error text: [ERROR_TEXT]
Modules and settings: [SCENARIO_MODULES]
Sheet headers: [SHEET_HEADERS]

List the 3 most likely causes in order of probability. For each cause give: how to confirm it in under 2 minutes, the exact fix, and whether the fix can use extra credits. Do not suggest paid plans, code, or any step that publishes content. If a cause depends on a limit you cannot confirm, write VERIFY BEFORE RELYING and name the official page.
```

Expected output: Three ranked causes with checks and fixes.
If the output is weak: Add a screenshot description of the failing module's output bundle and rerun.

## Failure points and fixes

| Failure | Cause | Fix |
|---|---|---|
| Scenario stops mid-month | Credits used up, including retries | Check usage in the Make dashboard, lower the row limit to 2, run less often, or fall back to Layer 1 |
| Error 429 or "quota" from Gemini | Free-tier rate limit | Wait, run fewer rows, check aistudio.google.com/rate-limit, or paste prompts by hand into the free Gemini app |
| Same row processed twice | Update Row module did not run, so status stayed APPROVED | Confirm module 3 uses the row number from module 1 and writes column C |
| Draft lands in the wrong row | A column was inserted or reordered | Never insert columns in the middle. Re-map modules to the headers |
| Script cut off | Cell character limit or model output limit | Store the script in a Google Doc, keep a link in the cell, and ask for the script in two parts |
| Every draft sounds alike | Weak first_hand_angle, or generic Style Bible | Fill column F with real detail before approving. This is also your inauthentic-content defense |
| Form answers missing | Link to Sheets broke | Reopen the form, **Responses > Link to Sheets**, choose the existing sheet |
| API key exposed | Key pasted into a shared file | Delete the key in AI Studio, create a new one, update the Make connection |

## Done when

- [ ] The form feeds the `Intake` tab and the `Pipeline` tab has all 22 headers.
- [ ] The status dropdown works and `Config` holds the [STYLE_BIBLE].
- [ ] Scenario 1 turns one APPROVED row into a script draft with a GAPS list.
- [ ] Scenario 2 writes titles and a description for one THUMB_DONE row.
- [ ] Both scenarios are set to On demand and use no polling.
- [ ] You edited at least one draft by hand and logged the gate results.
- [ ] No scenario can change a status to SCHEDULED, PUBLISHED, or ANALYSED.

## Next

[03-bulk-systems.md](03-bulk-systems.md)
