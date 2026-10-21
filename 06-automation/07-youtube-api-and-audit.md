# YouTube Data API Track, Private Upload Script, and Compliance Audit

> **Purpose:** Set up the YouTube Data API for private uploads from your pipeline, explain the private-upload lock and quota buckets, show how the compliance audit works, and give a safe fallback that needs no API at all.  
> **Use when:** Your pipeline already produces reviewed files and you want them to land in YouTube Studio as private drafts without hand uploading. This track is optional. You do not need it to monetize.  
> **Time needed:** About 90 minutes for the API setup and a first private upload. The audit application is a separate project of several hours plus waiting time with no guaranteed outcome.  
> **Needs:** A Google account that owns the channel, Python 3.11, finished videos that have passed gates C1 to C8, `04-human-checkpoints.md` read.  
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [CHANNEL_URL], [LANGUAGE], [COUNTRY]
- A video folder from `03-bulk-systems.md` containing `final.mp4`, `review-log.md` with every gate filled, `disclosure.md`, and `captions.srt`
- The chosen thumbnail in `thumbnails/<slug>/`

## Decide first: API or Studio?

| Question | If yes |
|---|---|
| Do you publish fewer than about 10 videos a week? | Use the manual Studio route in Part 7. It takes about 10 minutes per video (my estimate) and needs no setup |
| Do you want videos to land in Studio without hand uploading, and you accept they stay private until you act? | The API track below, up to Part 5, with no audit |
| Do you need API-uploaded videos to be able to go public? | You need the compliance audit in Part 6, and approval is not guaranteed |
| Do you want the API to publish on its own? | No. This repo forbids it. Publishing is a human decision |

Most owners should stay on the manual route. Building and auditing an upload pipeline costs hours that do not raise watch time, retention or originality, and those are what monetization depends on.

## Facts as of 2026-10-20

All of the following were checked by web search on 2026-10-20. Where sources disagreed I say so.

1. **The private-upload lock (verified 2026-10-20).** The `videos.insert` reference states that videos uploaded from unverified API projects created after 28 July 2020 are restricted to private viewing mode, and that lifting the restriction requires the project to pass an audit. Setting `privacyStatus` to public does not change this, and the call does not fail. A secondary source quoting YouTube Help says individually locked videos cannot be appealed, and that the project can apply for an audit instead. The rule keys off the Cloud project and its creation date, not your channel. Any project you create now is in this category.
2. **Quota buckets (verified 2026-10-20).** Google's revision history, as reported by several sources, records two changes: on 4 December 2025 the cost of `videos.insert` fell from about 1,600 units to about 100, and on 1 June 2026 `videos.insert` and `search.list` moved into their own daily buckets. Current default per project per day: 100 `videos.insert` calls at 1 unit each, 100 `search.list` calls, and 10,000 units shared by every other method. Quota resets at midnight Pacific Time. Related costs from the 10,000-unit pool, as reported: `thumbnails.set` 50 units, `videos.update` 50 units, `captions.insert` 400 units per track. The older `videos.insert` reference text still quotes 100 units per call, and many articles still say "six uploads per day". VERIFY BEFORE RELYING in Cloud Console under **APIs & Services > Enabled APIs & services > YouTube Data API v3 > Quotas & System Limits**, and on the page developers.google.com/youtube/v3/determine_quota_cost.
3. **OAuth consent screen in Testing status (verified 2026-10-20).** Google's help page says projects in Testing are limited to 100 test users and that a test user's authorization expires seven days after consent. Several sources add that the `youtube.upload` scope is classed as sensitive, and that projects In production must complete verification for sensitive scopes. For a one-person tool, staying in Testing and signing in again each week is the $0 path.
4. **Disclosure property (verified 2026-10-20).** The revision history says the API can mark videos that contain realistic altered or synthetic content, settable in `videos.insert` or `videos.update`. The exact property name and whether it is live for your project: VERIFY BEFORE RELYING on the Videos resource reference page. The upload script below treats it as optional.
5. **The audit form (verified 2026-10-20).** The form is called the YouTube Data API Services Audit and Quota Extension Form, at support.google.com/youtube/contact/yt_api_form. It offers two reasons: a compliance audit to request additional quota, or a re-audit to keep current quota. It asks for organization and contact details, a publicly accessible `https://` privacy policy URL, an optional terms URL, and demo account details with access instructions for the reviewer. There is a separate appeals form for projects marked non-compliant.
6. **Undisclosed paid promotion (from the research snapshot, verified 2026-10-20).** YouTube can auto-label undisclosed branded content since announcements of 3 September 2026. This applies to API uploads too: declare paid promotion yourself.

## Steps

### Part 1. Create the Cloud project and enable the API

1. Go to console.cloud.google.com and sign in with the Google account that owns the channel.
2. Select the project picker at the top, then **New Project**. Name it `yt-private-uploads`. Leave the organization as it is. Select **Create**.
3. Open **APIs & Services > Library**, search for **YouTube Data API v3**, and select **Enable**.
4. Write down the project number (Dashboard, **Project info**). You will need it if you ever apply for an audit, and you must audit this project and no other.

Billing does not need to be enabled for these steps (VERIFY BEFORE RELYING: Google may ask for billing details in some regions. If it does, do not continue unless a $0 option is offered).

### Part 2. Configure the consent screen

5. Open **APIs & Services > OAuth consent screen**. In newer consoles the same pages sit under **Google Auth Platform** with tabs named Branding, Audience and Data Access (VERIFY BEFORE RELYING: menu names change).
6. Choose user type **External**. Enter app name `[CHANNEL_NAME] private uploader`, a support email and a developer contact email.
7. Under data access or scopes, add exactly one scope: `https://www.googleapis.com/auth/youtube.upload`. It is the narrowest scope that allows `videos.insert`. Add no other scope.
8. Under **Audience** or **Test users**, select **Add users** and enter the Google account that owns the channel. Keep the publishing status as **Testing**.

### Part 3. Create the OAuth client

9. Open **APIs & Services > Credentials > Create credentials > OAuth client ID**.
10. Choose application type **Desktop app**. Name it `uploader-desktop`. Select **Create**, then **Download JSON**.
11. Save the file in your `yt-pipeline/` folder as `client_secret.json`. It is a secret. The `.gitignore` from `05-low-code-workflow.md` already ignores every `*.json` file, so it will not be committed. Never run this upload script on GitHub Actions or any shared machine.

### Part 4. Prepare and run the private upload

12. Install the extra packages inside your existing virtual environment: `pip install -r requirements-upload.txt`
13. Create the folder `tools/` and the two scripts below.
14. In the video folder create `upload.json` (example below). You make every decision in it yourself: `made_for_kids` must be `true` or `false`, and `synthetic_media` must be `true`, `false` or `null` according to `disclosure.md`. This file is kept out of git by the `*.json` rule, which is fine.
15. Fill the eight gate lines in `review-log.md` with the word `pass` after `pass/fail`, and put the rubric score number after `rubric score` on the C8 line. For example: `C8 Final watch: date 2026-10-20  pass/fail pass  minutes watched 14  rubric score 84`.
16. Run: `python tools/upload_private.py --slug L012-lentil-stew-under-3-dollars --confirm-reviewed`
17. A browser window opens. Sign in with the channel's account. Google will warn that the app has not been verified, because it is your own Testing app. Select **Advanced** and continue to your app (VERIFY BEFORE RELYING: current wording of the warning). Grant the upload permission.
18. The script prints the video ID and a Studio link. The video is private. Open the link, run the checks in Studio, decide the disclosure settings, and only then decide whether to publish or schedule.

### Part 5. Check your quota

19. In Cloud Console open **APIs & Services > Enabled APIs & services > YouTube Data API v3 > Quotas & System Limits**. Record the `videos.insert` daily limit and your usage.
20. The tools here make one `videos.insert` call per video, plus 50 units if you also use `--thumbnail`. You will never approach the limits at the volumes this repo recommends. Do not create extra Cloud projects to get more quota: splitting use across projects to evade limits is against YouTube's API policies (VERIFY BEFORE RELYING at developers.google.com/youtube/terms/developer-policies).

### Part 6. The compliance audit (optional, advanced)

21. **What the audit is.** It is a review of your API client against the YouTube API Services Terms of Service and Developer Policies. It is not a code-quality test. The form also exists to grant quota above the default. Passing it is what lifts the private lock for that project.
22. **Is it realistic for you?** The form is built for API clients with an organization, a product page, a privacy policy and a demo account. A one-person private script is an unusual applicant, and I could not confirm whether Google approves such cases. No source I found gives a reliable timeline or approval rate. Reports of "a few weeks" are unconfirmed. Do not apply unless you can answer every question truthfully. The form requires a statement that the facts are true, and false facts can lead to loss of access.
23. **What Google reviews, as reported by secondary sources** (VERIFY BEFORE RELYING each point against developers.google.com/youtube/terms/api-services-terms-of-service and the Required Minimum Functionality page):
    - Your described use of YouTube data and whether the privacy policy matches it. The policy should name YouTube API Services, link the Google Privacy Policy, and explain how a user revokes access and has stored data deleted.
    - Whether each scope you request maps to a real feature you can demonstrate.
    - Whether the upload screen lets the person choose visibility (a privacy selector), and follows the rules for metadata fields.
    - A consistent story across privacy policy, terms and interface.
    - Screenshots and a demo account with sample data and full feature access.
    - The terms' requirement not to violate others' copyright or privacy rights.
24. **Prepare before you apply:** a public `https://` privacy policy page (use P-AUTO-24 to draft it, then publish it on a free static page you control), a short written description of the tool, screenshots of the interface that uploads, a list of scopes with the feature each one serves, and a test Google account with a channel for the reviewer (the form's demo-account section states that Google is not bound by any terms that apply to that account, so use a throwaway account holding no private data).
25. **Apply.** Open the form, choose the compliance audit option, and answer from facts only. Use P-AUTO-23 to draft answers and a gap list. Audit the same project number you wrote down in step 4. Auditing the wrong project is a reported cause of "approved but still locked".
26. **If marked non-compliant,** use the appeals form, fix the named gaps, and wait for a decision. If a re-audit is requested later, you must complete it to keep access. If your tool's data use changes, you must resubmit.
27. **After approval,** nothing in the script changes. It still uploads as private, and you still publish by hand. Do not add a `publishAt` field or a public option. Do not pay anyone who promises guaranteed approval, and do not borrow another developer's audited credentials.

### Part 7. The safe fallback: manual upload with the pipeline preparing everything

28. Run the kit builder: `python tools/make_upload_kit.py --slug L012-lentil-stew-under-3-dollars --thumb A`. It copies `final.mp4`, `captions.srt` and the chosen thumbnail into `upload-kit/` inside the video folder, and writes `upload-card.md` with every field in the order YouTube Studio asks for it.
29. Go to studio.youtube.com and select **Create > Upload videos**. Choose `upload-kit/final.mp4`.
30. On the **Details** page paste the title and description from the card. Upload `thumbnail.jpg` (1280 x 720, under 2 MB, JPG or PNG, verified 2026-10-20; a verified channel is needed for custom thumbnails). Choose the audience answer from the card. Leave age restriction on its default unless your content needs it.
31. Select **Show more**. Tick **Paid promotion** if the video includes a sponsorship or paid placement. Set **Altered content** according to `disclosure.md`. Paste the tags, set the video language and the category. Studio labels change often (VERIFY BEFORE RELYING: current names).
32. On **Video elements** upload `captions.srt` under subtitles, with timing. Add end screens or cards only if they help the viewer.
33. On **Checks**, wait for the copyright and ads-suitability checks to finish, and read the results. Do not publish with an unresolved claim you do not understand.
34. On **Visibility**, choose **Schedule**, set the date, time and time zone, then select **Schedule**. To keep it hidden for now, choose **Private** instead.
35. Update the sheet: status `SCHEDULED` with the date, and after release `PUBLISHED` with the URL.

## Code

### requirements-upload.txt

```
# Lower bounds. Run "pip freeze" after your first successful upload to record exact versions.
google-api-python-client>=2.100
google-auth-oauthlib>=1.2
google-auth-httplib2>=0.2
google-auth>=2.30
```

### Example `upload.json`

```json
{
  "title": "Lentil Stew Under 3 Dollars: What I Actually Spent",
  "description": "I cooked this stew three times and kept every receipt.\n\nChapters\n0:00 The budget\n1:10 The shopping list\n3:40 The cooking\n7:15 The real cost per serving",
  "tags": ["lentil stew", "budget cooking", "cheap dinner"],
  "category_id": "26",
  "language": "en",
  "made_for_kids": false,
  "synthetic_media": false
}
```

Category IDs differ by region and change (VERIFY BEFORE RELYING: list them with the `videoCategories.list` method or in Studio). Set `synthetic_media` to `null` if you prefer to set the label in Studio.

### tools/upload_private.py

```python
"""Upload ONE finished video to YouTube as PRIVATE.

This script cannot make a video public and cannot schedule one. Publishing is a
human decision made in YouTube Studio. It also refuses to run unless all eight
human checkpoints (C1 to C8) are marked "pass" in review-log.md.

Usage:
  python tools/upload_private.py --slug L012-lentil-stew-under-3-dollars --confirm-reviewed
  (optional) --thumbnail workspace/thumbnails/L012-lentil-stew-under-3-dollars/thumb-A.jpg
"""
import argparse
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# The narrowest scope that allows videos.insert. Do not add more scopes.
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT / "workspace"
CLIENT_SECRET = ROOT / "client_secret.json"
TOKEN_FILE = ROOT / "token.json"

SLUG_PATTERN = re.compile(r"^[LS]\d{3}-[a-z0-9]+(-[a-z0-9]+)*$")
GATE_CODES = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]
REQUIRED_KEYS = ["title", "description", "tags", "category_id", "language", "made_for_kids", "synthetic_media"]
RETRY_STATUS = {500, 502, 503, 504}   # temporary server errors: wait and try again


def check_gates(folder: Path) -> list:
    """Return a list of problems. An empty list means every gate is marked pass."""
    log = folder / "review-log.md"
    if not log.exists():
        return ["review-log.md not found"]
    lines = log.read_text(encoding="utf-8").splitlines()
    problems = []
    for code in GATE_CODES:
        line = next((l for l in lines if l.strip().startswith(code + " ")), None)
        if line is None:
            problems.append(f"{code}: line missing")
            continue
        found = re.search(r"pass/fail\s+(pass|fail)\b", line, re.IGNORECASE)
        if not found or found.group(1).lower() != "pass":
            problems.append(f"{code}: not marked pass")
            continue
        if code == "C8":
            score = re.search(r"rubric score\s+(\d+)", line, re.IGNORECASE)
            if not score or int(score.group(1)) < 80:
                problems.append("C8: rubric score must be 80 or more")
    return problems


def load_metadata(folder: Path) -> dict:
    """Read upload.json and check the basics. Limits below: VERIFY BEFORE RELYING."""
    path = folder / "upload.json"
    if not path.exists():
        raise SystemExit("upload.json not found in the video folder.")
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED_KEYS if key not in data]
    if missing:
        raise SystemExit(f"upload.json is missing: {missing}")
    if not isinstance(data["made_for_kids"], bool):
        raise SystemExit("made_for_kids must be true or false. It is your decision, not a default.")
    if data["synthetic_media"] not in (True, False, None):
        raise SystemExit("synthetic_media must be true, false or null (see disclosure.md).")
    if not isinstance(data["tags"], list):
        raise SystemExit("tags must be a list of text values.")
    title = data["title"]
    if not title.strip() or len(title) > 100 or "<" in title or ">" in title:
        raise SystemExit("Title must be 1 to 100 characters and must not contain < or >.")
    if len(data["description"].encode("utf-8")) > 5000:
        raise SystemExit("Description is over 5,000 bytes.")
    if sum(len(tag) for tag in data["tags"]) > 500:
        raise SystemExit("Tags total more than 500 characters.")
    return data


def get_credentials() -> Credentials:
    """Log in. Re-uses the saved login, and signs in again when it has expired."""
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            TOKEN_FILE.write_text(creds.to_json())
            return creds
        except RefreshError:
            # In Testing status, Google ends logins after 7 days. This is normal.
            print("Saved login expired (normal every 7 days in Testing status). Signing in again.")
            TOKEN_FILE.unlink(missing_ok=True)
    if not CLIENT_SECRET.exists():
        raise SystemExit("client_secret.json not found. Download it from the Cloud Console (Part 3).")
    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
    creds = flow.run_local_server(port=0)
    TOKEN_FILE.write_text(creds.to_json())
    return creds


def main():
    parser = argparse.ArgumentParser(description="Upload one video as PRIVATE.")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--confirm-reviewed", action="store_true",
                        help="You confirm a person has reviewed this video (gates C1 to C8).")
    parser.add_argument("--thumbnail", help="Optional path to a thumbnail (costs extra quota units).")
    args = parser.parse_args()

    if not args.confirm_reviewed:
        raise SystemExit("Refused: add --confirm-reviewed only after a person has passed every gate.")
    if not SLUG_PATTERN.match(args.slug):
        raise SystemExit("Invalid slug. Example: L012-lentil-stew-under-3-dollars")

    folder = WORKSPACE / "videos" / args.slug
    video_path = folder / "final.mp4"
    done_marker = folder / "uploaded.json"
    if not video_path.exists():
        raise SystemExit("final.mp4 not found in the video folder.")
    if done_marker.exists():
        raise SystemExit("uploaded.json exists, so this video was already uploaded. Delete it only to upload again.")

    problems = check_gates(folder)
    if problems:
        raise SystemExit("Refused. Fix these gate lines in review-log.md:\n  " + "\n  ".join(problems))
    data = load_metadata(folder)

    body = {
        "snippet": {
            "title": data["title"],
            "description": data["description"],
            "tags": data["tags"],
            "categoryId": data["category_id"],
            "defaultLanguage": data["language"],
        },
        # privacyStatus is fixed to "private". There is no option to change it here.
        "status": {
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": data["made_for_kids"],
        },
    }
    if data["synthetic_media"] is not None:
        # Property name: VERIFY BEFORE RELYING on the Videos resource reference.
        # If the API answers 400 for it, set synthetic_media to null and set the label in Studio.
        body["status"]["containsSyntheticMedia"] = data["synthetic_media"]

    youtube = build("youtube", "v3", credentials=get_credentials())
    media = MediaFileUpload(str(video_path), chunksize=8 * 1024 * 1024, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media, notifySubscribers=False)

    response, retries = None, 0
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                print(f"Uploaded {int(status.progress() * 100)}%")
        except HttpError as error:
            if error.resp.status in RETRY_STATUS and retries < 5:
                retries += 1
                wait = 2 ** retries
                print(f"Temporary error {error.resp.status}. Waiting {wait} seconds (try {retries} of 5).")
                time.sleep(wait)
                continue
            raise

    video_id = response["id"]
    actual = response.get("status", {}).get("privacyStatus", "unknown")

    if args.thumbnail:
        try:
            youtube.thumbnails().set(videoId=video_id, media_body=MediaFileUpload(args.thumbnail)).execute()
            print("Thumbnail set.")
        except HttpError as error:
            # Custom thumbnails need a verified channel. Set it by hand in Studio instead.
            print(f"Thumbnail was not set ({error.resp.status}). Set it in YouTube Studio.")

    done_marker.write_text(json.dumps({
        "video_id": video_id,
        "privacy_status": actual,
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
    }, indent=2), encoding="utf-8")

    print("\nUPLOAD FINISHED")
    print(f"  Video ID: {video_id}")
    print(f"  Privacy:  {actual}")
    print(f"  Studio:   https://studio.youtube.com/video/{video_id}/edit")
    print("\nREMINDER: This video is PRIVATE. Open it in Studio, wait for the checks, confirm the")
    print("disclosure settings from disclosure.md, then decide yourself whether to publish or schedule.")


if __name__ == "__main__":
    main()
```

### tools/make_upload_kit.py

```python
"""Prepare everything for a MANUAL upload in YouTube Studio.

Copies the final files into upload-kit/ and writes upload-card.md with every
field in the order Studio asks for it. Publishing stays your decision.

Usage:
  python tools/make_upload_kit.py --slug L012-lentil-stew-under-3-dollars --thumb A
"""
import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT / "workspace"
SLUG_PATTERN = re.compile(r"^[LS]\d{3}-[a-z0-9]+(-[a-z0-9]+)*$")


def main():
    parser = argparse.ArgumentParser(description="Build a manual upload kit.")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--thumb", choices=["A", "B", "C"], default="A")
    args = parser.parse_args()
    if not SLUG_PATTERN.match(args.slug):
        raise SystemExit("Invalid slug. Example: L012-lentil-stew-under-3-dollars")

    folder = WORKSPACE / "videos" / args.slug
    data = json.loads((folder / "upload.json").read_text(encoding="utf-8"))
    kit = folder / "upload-kit"
    kit.mkdir(exist_ok=True)
    notes = []

    for name in ("final.mp4", "captions.srt"):
        source = folder / name
        if source.exists():
            shutil.copy2(source, kit / name)
        else:
            notes.append(f"MISSING: {name}")

    thumb_source = WORKSPACE / "thumbnails" / args.slug / f"thumb-{args.thumb}.jpg"
    if thumb_source.exists():
        shutil.copy2(thumb_source, kit / "thumbnail.jpg")
        if thumb_source.stat().st_size > 2 * 1024 * 1024:
            notes.append("WARNING: thumbnail is over 2 MB. Re-export it smaller.")
    else:
        notes.append(f"MISSING: thumbnails/{args.slug}/thumb-{args.thumb}.jpg")

    altered = {True: "Yes. Set 'Altered content' to Yes.",
               False: "No. Leave 'Altered content' at No.",
               None: "Not decided here. Read disclosure.md and decide in Studio."}[data.get("synthetic_media")]
    kids = "Yes, it is made for kids" if data.get("made_for_kids") else "No, it is not made for kids"

    card = f"""# Upload card: {args.slug}

Open studio.youtube.com, select Create, then Upload videos, and choose upload-kit/final.mp4.

## 1. Details
Title:
{data['title']}

Description (copy everything below this line up to the next heading):
{data['description']}

Thumbnail: upload upload-kit/thumbnail.jpg
Audience: {kids}

## 2. Show more
Paid promotion: tick it if this video includes a sponsorship or paid placement.
Altered or synthetic content: {altered}
Tags: {', '.join(data['tags'])}
Language: {data['language']}
Category ID in your notes: {data['category_id']} (choose the matching category name)

## 3. Video elements
Subtitles: upload upload-kit/captions.srt with timing.

## 4. Checks
Wait for the copyright and ads-suitability checks to finish. Read the results.

## 5. Visibility
Choose Schedule and set the date, time and time zone, or choose Private. You decide.

## Notes from this script
{chr(10).join(notes) if notes else 'None. All files were found.'}
"""
    (kit / "upload-card.md").write_text(card, encoding="utf-8")
    print(f"Kit ready in {kit}")
    for note in notes:
        print(note)


if __name__ == "__main__":
    main()
```

## Prompts

### P-AUTO-23 — Audit Readiness Checklist and Draft Answers

Purpose: Turn the facts about your tool into draft answers for the audit form and a list of gaps, without inventing anything.
Inputs: [APP_DESCRIPTION] (what the tool does, in plain words), [SCOPES_USED] (for example only `youtube.upload`), [DATA_STORED] (what is saved, where, for how long), [PRIVACY_POLICY_URL], [FORM_QUESTIONS] (paste the questions from the current form), [WHO_USES_IT] (just you, or others).

```
You help a solo developer prepare a YouTube API Services compliance audit submission. Use only the facts below. Do not invent features, users, data practices, or screenshots.

Tool description: [APP_DESCRIPTION]
Scopes requested: [SCOPES_USED]
Data stored: [DATA_STORED]
Privacy policy URL: [PRIVACY_POLICY_URL]
Who uses the tool: [WHO_USES_IT]
Form questions: [FORM_QUESTIONS]

Produce:
1. A draft answer for each form question, using only the facts above. Where a fact is missing, write MISSING FACT and say what I must provide. Never fill a gap with a guess.
2. A table mapping each scope to the exact feature that needs it. If a scope has no feature, say it must be removed.
3. A gap list against these checks, each marked MET, NOT MET or UNKNOWN: privacy policy is public and names YouTube API Services; it links the Google Privacy Policy; it explains how to revoke access and delete stored data; the upload screen lets the user choose visibility; the privacy policy, terms and interface describe the same behavior; a demo account with sample data exists; screenshots are ready.
4. A list of screenshots to capture, each with the screen name and what it must show.
5. A final line: "Approval is decided by Google and is not guaranteed." Do not estimate approval odds or timelines.
Mark anything about current Google requirements that I should confirm as VERIFY BEFORE RELYING and name the official page.
```

Expected output: Draft answers, a scope table, a gap list and a screenshot list.
If the output is weak: Add the exact current wording of each form question and a one-paragraph description of what happens, step by step, from clicking the upload command to the video appearing in Studio.

### P-AUTO-24 — Privacy Policy Draft for the Tool

Purpose: Draft a plain-language privacy policy page for the audit form. This is a draft, not legal advice.
Inputs: [OWNER_NAME_OR_BRAND], [CONTACT_EMAIL], [DATA_STORED], [WHERE_STORED] (for example "only on the owner's computer"), [COUNTRY].

```
Write a plain-language privacy policy for a small tool named "[OWNER_NAME_OR_BRAND] private uploader". Contact: [CONTACT_EMAIL]. Country of the owner: [COUNTRY].
Facts: The tool uses the YouTube API Services with the youtube.upload permission to upload videos to the signed-in user's own channel as private videos. Data it stores: [DATA_STORED]. Where it is stored: [WHERE_STORED].

Include these sections, with short honest sentences and no claims beyond the facts above:
1. What the tool is and what permission it asks for.
2. What information it accesses, stores, and where.
3. What it does not do: it does not sell data, does not share data with other parties, and does not publish videos by itself.
4. A statement that the tool uses YouTube API Services and that by using it the person agrees to be bound by the YouTube Terms of Service, with the link https://www.youtube.com/t/terms.
5. A link to the Google Privacy Policy: https://policies.google.com/privacy.
6. How to revoke the tool's access: through the Google Account permissions page at https://myaccount.google.com/permissions.
7. How the person can ask for stored data to be deleted, and how quickly the owner will respond (use a period the owner can really keep, and leave a bracket [DAYS] for the owner to fill in).
8. Contact details and the date of the last update.
End with this note on its own line: "This is a draft and not legal advice. Have a qualified person review it if other people will use the tool." Mark every legal or Google requirement I should confirm as VERIFY BEFORE RELYING.
```

Expected output: A ready-to-publish policy draft with one bracket for you to fill in.
If the output is weak: Add the exact list of data your tool keeps (for example `token.json` on your disk) and ask for each sentence to match it.

## Failure points and fixes

| Failure | Cause | Fix |
|---|---|---|
| Sign-in blocked, "access blocked" or "not verified" | Your account is not in the Test users list | Add it under the consent screen's Audience or Test users |
| `invalid_grant` or login asked again after a week | Testing status ends authorizations after 7 days | Run the script again. It deletes `token.json` and signs in. Publishing the consent screen to production brings verification duties |
| `redirect_uri_mismatch` | OAuth client was not created as Desktop app | Create a new Desktop app client and download its JSON |
| `403 quotaExceeded` | The day's bucket is used up | Check Quotas & System Limits. The daily quota resets at midnight Pacific Time |
| `403 uploadLimitExceeded` | A YouTube-side upload limit for the channel (VERIFY BEFORE RELYING: exact rule) | Wait and try again later, or use Studio |
| Video is private even though you wanted it public | The private-upload lock for unaudited projects, and this script never makes videos public | Publish from Studio, or pass the audit. Locked videos cannot be appealed one by one |
| `insufficientPermissions` | Wrong or missing scope in the saved login | Delete `token.json`, run again, and grant the upload permission |
| 400 on `containsSyntheticMedia` | Property name or availability differs | Set `synthetic_media` to `null` and set the label in Studio. VERIFY BEFORE RELYING on the Videos resource page |
| 400 invalid title or description | Length or characters | Shorten, remove `<` and `>`, and check the byte count of the description |
| Thumbnail not set | Channel not verified, or the scope does not cover it | Set it in Studio. Custom thumbnails need a verified channel |
| Upload stalls | Network drop | Run again. Check Studio first for a partial duplicate, and delete it |
| "Refused" gate message | Gate lines not filled with `pass` | Fill `review-log.md` as in step 15, then rerun |
| Approved, but videos still locked | The audit covered another project | Compare the project number in `client_secret.json` with the one in the audit approval |

## Done when

- [ ] You decided in writing whether to use the API route, the manual route, or both.
- [ ] If you used the API: one video uploaded as private, the Studio link opened, and you published or scheduled it yourself.
- [ ] `client_secret.json` and `token.json` are not in any repository and not on any shared machine.
- [ ] You recorded your real `videos.insert` quota from Cloud Console.
- [ ] If you applied for the audit: you answered truthfully, audited the correct project number, and kept a copy of the submission.
- [ ] The manual upload kit produced a complete `upload-card.md` for one video, and you finished that upload in Studio.
- [ ] No script or schedule in your setup can publish a video.

## Next

[../07-build-your-own/01-ideas-research-and-ideation.md](../07-build-your-own/01-ideas-research-and-ideation.md)
