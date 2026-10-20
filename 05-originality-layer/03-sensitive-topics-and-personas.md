# Sensitive Topics, AI Personas, and Synthetic Media

> Purpose: Keep a channel monetizable while covering topics near health, finance, legal, and news, and while using AI voices, avatars, or images.
> Use when: Before choosing a topic, before scripting, and before publishing any video that touches a sensitive subject or uses synthetic media.
> Time needed: 10 minutes per video; 30 minutes to set up the channel's rules once.
> Needs: The video topic, the script or outline, your asset log, a free chat AI.
> Cost: $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [COUNTRY], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [VIDEO_TOPIC], [VIDEO_LENGTH]
- [SCRIPT_OR_SUMMARY] (from 02-scoring-rubric.md)
- [ASSET_LOG] (from 02-long-form/04-visual-production.md and 04-thumbnails/02-original-generation.md)
- [CREDENTIALS]: any real qualification you hold on the topic, stated as a fact (for example "none", "home cook for 12 years", "licensed accountant"). Defined in P-ORIG-03.

## What the rules say (verified 2026-10-20)

1. **Inauthentic content, clarified in mid-July 2026** (reports date it 14 to 16 July): three categories are not monetizable. (a) Generic, repetitive, or template-based content with little variation between videos. (b) Off-putting or distressing content. (c) AI personas discussing sensitive topics such as health and finance. YouTube describes the change as a clarification of existing policy aimed at mass production, not at AI itself. AI voiceover can qualify when the video has original commentary, education, or entertainment value. The reused-content policy did not change.
2. **Altered or synthetic content disclosure.** Realistic content that a viewer could easily mistake for a real person, place, scene, or event, made with altered or synthetic media including generative AI, must be disclosed in YouTube Studio. Examples YouTube lists include a realistic synthetic version of a real person's voice or face, altered footage of real events or places, and realistic generated scenes of fictional major events. Clearly unrealistic, animated, special-effects, or production-assistance uses (script help, ideas, automatic captions) do not need it. Since May 2026 YouTube describes a single, more prominent label for photorealistic and meaningfully altered content, and YouTube may add the label itself. For sensitive topics such as health, news, elections, and finance, the label is shown more prominently on the video. YouTube also offers a privacy process to request removal of synthetic content that simulates an identifiable person's face or voice.
3. **Branded content.** Undisclosed paid promotion can be auto-labeled since announcements of 3 September 2026.

VERIFY BEFORE RELYING: the exact current wording on YouTube Help, search "Inauthentic content", "Disclosing use of altered or synthetic content", "Medical misinformation policy", "Misinformation policies", and "Advertiser-friendly content guidelines". Secondary sources disagree on whether a generic AI voiceover and AI-generated music need the label, so use the decision table in Step 5 and then read the Help page.

## Steps

1. **Classify the topic with the zone table.** Write the zone in your `videos/<slug>/value-stack.md` file.

| Zone | What it covers | What you do |
|---|---|---|
| GREEN | Your own experience, tests, and opinions on non-sensitive subjects; general information from named primary sources, clearly framed | Proceed. Normal rubric scoring |
| AMBER | Health, nutrition, money, legal, safety, news, or elections adjacent subjects, made by a real human creator who frames it as experience or education | Proceed only with the AMBER rules below, and run P-ORIG-03 |
| RED | An AI persona giving advice in these areas; treatment, dosage, diagnosis claims; investment picks or return promises; legal outcomes; synthetic news presented as real; realistic synthetic media of real people or events; distressing or exploitative content | Do not publish. Use the safe alternatives table |

2. **Apply the AI persona rules (all are repo rules built from the July 2026 clarification).**
   1. A synthetic host, avatar, or character may not present as a doctor, nurse, therapist, financial adviser, lawyer, journalist, or any other expert.
   2. A synthetic host may not discuss health, finance, legal, or news topics in a way that guides a viewer's decision. This applies even with a disclaimer; a disclaimer does not turn a prohibited persona into a permitted one.
   3. A synthetic voice must never narrate invented first-person experience ("I lost 10 kg in a month", "I made $5,000 trading"). If the experience is real, it must be yours, and you must be able to show proof.
   4. A synthetic voice reading your own script over footage you made, with no invented identity or credentials, is a narration tool, not a persona. It still needs original commentary and your own footage. This boundary is a gray area; VERIFY on YouTube Help and prefer your real voice or your face on sensitive-adjacent videos.
   5. No cloned voice or likeness of any real person without their documented permission. This includes voices of public figures, creators, and deceased people.
   6. Give every persona a plain name that makes clear it is a character, never a fake "Dr." or "Professor".
3. **Apply the AMBER rules (health, finance, legal, news).** Every item must hold; if one does not, move to RED.
   1. A real human presents it: face, real voice, or your own first-person narration.
   2. It is framed as your experience or general education, never as an instruction for an individual ("what I spent", not "what you must do").
   3. Every factual claim names its primary source and date on screen: a government health page, a regulator, a statute, a named study. Run the fact-check prompt P-LONG-07 in 02-long-form/02-script-prompt-chain.md.
   4. No outcome promises: no cure, no weight-loss result, no profit, no guaranteed approval, no "legal in your country" claim. [COUNTRY] changes the answer, so state which country the information covers.
   5. No dosage, treatment, supplement, trading signal, or legal strategy recommendations.
   6. Say plainly what you are not: "I am a home cook, not a dietitian", with a pointer to a qualified professional or official service for the viewer's own situation. This helps viewers; it does not protect an otherwise prohibited video.
   7. Title and thumbnail contain no fear hook, miracle claim, or "doctors hate this" phrasing.
   8. Expect ad limits on some sensitive topics even when the video is compliant. VERIFY at "Advertiser-friendly content guidelines".
4. **Apply the off-putting and distressing content rules.** Do not publish: graphic injury or violence made for shock; fake emergencies or fake disasters; synthetic content built to upset, frighten, or manipulate; exploitation of real tragedies or victims; unsettling content aimed at children; endless rage or panic bait; harassment of a named person. YouTube's Vice President of Trust and Safety described inauthentic content as including content that is "off-putting" and emotionally manipulative (reported 2026). If your hook depends on distress, rewrite the hook around the useful or interesting idea.
5. **Decide the disclosure.** Use this table, then check the live Studio wording before ticking the box. When in doubt for realistic synthetic content, disclose; over-disclosing costs little.

| Your content | Label in Studio? | Reason |
|---|---|---|
| Your own real footage and your own real voice | No | Not synthetic |
| AI used only for ideas, outlines, script drafts, captions | No | Production assistance, per YouTube's own examples |
| Clearly animated or illustrated visuals | No | Unrealistic |
| A realistic AI image or video that could be mistaken for a real place, scene, or event | Yes | Realistic synthetic media |
| Altered footage of a real event or place | Yes | YouTube lists it |
| A synthetic voice imitating a real or recognizable person | Do not make it. If it exists with permission, Yes | Likeness rule |
| A cloned version of your own voice | VERIFY; one source says no label | Your own likeness; check current text |
| A generic synthetic voice that imitates no one, over true footage | VERIFY; sources disagree | If a viewer could think it is a real person speaking, disclose |
| AI-generated music | VERIFY; sources disagree | If unsure, disclose |
| Paid promotion, sponsored gift, affiliate-like arrangement | Declare paid promotion | Undisclosed branded content can be auto-labeled since 3 Sep 2026 |

6. **Use the safe alternatives table when a plan lands in RED.**

| RED plan | Safe, monetizable version |
|---|---|
| AI avatar doctor explains why a food "reverses" a condition | You, on camera, show what you cooked and bought for a week, state what you ate, read a printed nutrition label aloud, point to an official health body for diet questions |
| AI voice gives stock picks or return projections | A budgeting video built on your own real receipts and a spreadsheet you share; no picks, no returns; link to your country's consumer finance regulator for investing questions |
| AI newsreader narrates breaking events over stock clips | A commentary video where you analyze one development, cite two primary sources on screen, and make clear what is confirmed and what is not |
| Legal explainer voiced by a lawyer character | A first-person account of a process you went through (renting, returning an item), with the official government page shown on screen and a note that rules vary by [COUNTRY] |
| Realistic AI clip of a disaster for views | An animated or illustrated explainer, labelled as an illustration, on how people prepare, drawn from a named public authority's guidance |
| Cloned celebrity voice narrating your script | Your own voice, or a generic voice that imitates no one, plus your own commentary |
| Shock-value "disturbing facts" compilation | A story built around one real question, with context and a clear lesson, and no graphic imagery |
| Dozens of near-identical videos from one prompt | One video per week with a new Value Stack, scored in 02-scoring-rubric.md |

Worked example in the neutral niche (home cooking on a budget): "Eat this to cure high blood pressure" is RED (health outcome claim). "I ate on $1.62 a meal for a week and here are the receipts" is GREEN. "What the sodium numbers on my pantry labels were, and where to read official guidance" is AMBER: you show the labels as printed, state you are not a dietitian, cite the national health authority page of [COUNTRY], and make no outcome claim.

## Prompts

### P-ORIG-03 — Sensitive-topic and persona review

Purpose: Classify one video plan as GREEN, AMBER, or RED, list violations, and produce a safe rewrite, required on-screen text, and a disclosure decision.

Inputs: [CHANNEL_NAME], [NICHE], [AUDIENCE], [COUNTRY], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [VIDEO_TOPIC], [CREDENTIALS], [SCRIPT_OR_SUMMARY], [ASSET_LOG].

```
You are a YouTube policy-aware editor. You are not a lawyer, a doctor, or a financial adviser, and you must not give health, finance, legal, or news advice. Your job is to review a video plan for compliance risk and to propose a safer version. Use only the materials below. If something is missing, ask.

Channel: [CHANNEL_NAME] | Niche: [NICHE] | Audience: [AUDIENCE] | Country the content covers: [COUNTRY] | Language: [LANGUAGE]
Presenter: [FACE_OR_FACELESS] | Voice: [VOICE_MODE]
My real credentials on this topic: [CREDENTIALS]
Video topic: [VIDEO_TOPIC]
Script or timestamped summary: [SCRIPT_OR_SUMMARY]
Asset log: [ASSET_LOG]

Facts to apply (YouTube, clarified mid-July 2026): three categories are not monetizable: generic, repetitive, or template-based content; off-putting or distressing content; AI personas discussing sensitive topics such as health and finance. AI voiceover can qualify when the video has original commentary, education, or entertainment value. Realistic altered or synthetic content must be disclosed in YouTube Studio.

Do these, with these headings:
1. ZONE: GREEN, AMBER, or RED, with the reason in two sentences.
2. PERSONA CHECK: Is any synthetic host, avatar, character, or voice presenting as an expert or discussing health, finance, legal, or news in a way that guides decisions? Does any synthetic voice narrate invented first-person experience? Does anything clone or imitate a real person? Answer each YES or NO with the line or scene that triggers it.
3. AMBER RULES CHECK (only if AMBER): For each of the 8 rules (human presenter, framed as experience or education, named primary sources with dates, no outcome promises, no dosage or treatment or trading signal or legal strategy, honest statement of what I am not, no fear or miracle title, ad-limit risk noted) answer MET or NOT MET and quote 12 words or fewer as evidence.
4. DISTRESS CHECK: Does anything depend on shock, fear, or emotional manipulation? List scenes.
5. SYNTHETIC MEDIA AND DISCLOSURE: List every item in the asset log or script that is synthetic. For each, say whether a viewer could easily mistake it for a real person, place, or event, and give the disclosure decision: DISCLOSE, NO LABEL, or CHECK YOUTUBE HELP. Never tell me a label is not needed when the item imitates a real person.
6. VERDICT: PROCEED, REVISE, or STOP. STOP if the zone is RED or any persona check is YES.
7. SAFE REWRITE: a revised video angle that keeps the audience's interest, uses my real experience or evidence, and keeps me on the right side of the rules. Give a new working title with no miracle or fear claims and three on-screen text lines I must show (source names, "not a substitute for professional advice" wording suited to this topic, country scope).
8. SOURCES TO CHECK: the types of official sources (name the kind of body, not invented URLs) I must read before publishing.
Do not invent facts, studies, statistics, or URLs. Be blunt.
```

Expected output: Eight labeled sections, a zone, a persona check, a disclosure decision per synthetic item, a verdict, and a safe rewrite.

If the output is weak: (1) If it states medical or financial facts, say "do not state any health or finance facts; only review my plan and name the type of official source". (2) If it skips items in the asset log, say "go through every row of the asset log". (3) If it marks everything PROCEED, say "review as a reviewer who wants to remove this channel from monetization".

## Done when

- Every upload has a zone (GREEN, AMBER, or RED) recorded in its value-stack file.
- No RED video is published.
- Every AMBER video passed all 8 AMBER rules and the fact check.
- No synthetic host presents as an expert, and no synthetic voice narrates invented first-person experience.
- Every synthetic realistic item has a disclosure decision, and the Studio box is ticked where required.
- Any sponsorship or gifted item is declared as paid promotion.
- Criterion 9 and gate G3 in 02-scoring-rubric.md are scored from this file's outputs.

## Next

Continue to [../06-automation/01-pipeline-architecture.md](../06-automation/01-pipeline-architecture.md).
