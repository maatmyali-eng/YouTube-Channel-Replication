#!/usr/bin/env python3
"""
check_repo.py - integrity checker and prompt-library generator for YouTube-Channel-Replication.

Standard library only. Needs Python 3.8 or newer.

USAGE
    python3 scripts/check_repo.py                 # run from the repo root
    python3 scripts/check_repo.py --root PATH     # check a repo somewhere else
    python3 scripts/check_repo.py --strict        # warnings also cause FAIL
    python3 scripts/check_repo.py --no-write      # do not rewrite prompt-library.md

WHAT IT DOES (in this order)
    1. Scans every .md file (except prompt-library.md) for headings that match
           ^### (P-[A-Z]+-\\d{2}) - (.+)$      (the dash is an em dash)
       outside code fences, and writes prompt-library.md as a table of
       ID, name, file, folder, sorted by folder and then ID.
       This runs first so that prompt-library.md exists before the file check.
    2. Warns on duplicate prompt IDs, and on headings that start with "### P-"
       but do not match the required form.
    3. Verifies that every file in the repo tree exists.
    4. Verifies that every relative Markdown link in every .md file resolves,
       with exact letter case (GitHub is case sensitive). Links inside code
       fences and inline code are ignored. http(s), mailto and #anchor-only
       links are ignored.
    5. Warns when a file contains the unfinished-work markers (to-do, to-be-decided)
       or the abbreviation for "and so on".
    6. Prints a final PASS or FAIL summary.

EXIT CODES
    0  PASS (warnings allowed unless --strict)
    1  FAIL (missing files, broken links, or warnings under --strict)
    2  bad arguments or unreadable root folder
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

LIBRARY_NAME = "prompt-library.md"

REPO_TREE = [
    "README.md",
    "prompt-library.md",
    "00-start-here/01-setup-card.md",
    "00-start-here/02-principles-and-copy-line.md",
    "00-start-here/03-compliance-master-checklist.md",
    "00-start-here/04-free-tool-stack.md",
    "01-channel-dna/01-data-gathering.md",
    "01-channel-dna/02-channel-analysis.md",
    "01-channel-dna/03-style-bible-template.md",
    "01-channel-dna/04-style-bible-worked-example.md",
    "02-long-form/01-video-dna-analysis.md",
    "02-long-form/02-script-prompt-chain.md",
    "02-long-form/03-voice-and-audio.md",
    "02-long-form/04-visual-production.md",
    "02-long-form/05-metadata-and-seo.md",
    "02-long-form/06-prepublish-gate.md",
    "03-shorts/01-shorts-dna-analysis.md",
    "03-shorts/02-script-prompt-chain.md",
    "03-shorts/03-batch-scripts.md",
    "03-shorts/04-vertical-visuals-and-editing.md",
    "03-shorts/05-repurposing-without-reuse.md",
    "03-shorts/06-prepublish-gate.md",
    "04-thumbnails/01-thumbnail-dna-analysis.md",
    "04-thumbnails/02-original-generation.md",
    "04-thumbnails/03-design-workflow-and-templates.md",
    "04-thumbnails/04-ab-testing-and-safety.md",
    "05-originality-layer/01-differentiation-method.md",
    "05-originality-layer/02-scoring-rubric.md",
    "05-originality-layer/03-sensitive-topics-and-personas.md",
    "06-automation/01-pipeline-architecture.md",
    "06-automation/02-no-code-workflow.md",
    "06-automation/03-bulk-systems.md",
    "06-automation/04-human-checkpoints.md",
    "06-automation/05-low-code-workflow.md",
    "06-automation/06-custom-software.md",
    "06-automation/07-youtube-api-and-audit.md",
    "07-build-your-own/01-ideas-research-and-ideation.md",
    "07-build-your-own/02-ideas-script-and-voice.md",
    "07-build-your-own/03-ideas-visuals-and-editing.md",
    "07-build-your-own/04-ideas-publishing-and-analytics.md",
    "07-build-your-own/05-channel-style-analyzer-starter.md",
    "08-monetization/01-reality-and-timeline-math.md",
    "08-monetization/02-30-day-plan.md",
    "08-monetization/03-parallel-routes.md",
    "08-monetization/04-growth-levers-and-kpis.md",
    "08-monetization/05-income-scenarios.md",
    "08-monetization/06-mistakes-to-avoid.md",
    "09-operations/01-quick-start.md",
    "09-operations/02-troubleshooting-faq.md",
    "09-operations/03-tracking-sheet.md",
    "templates/content-calendar.md",
    "templates/per-video-checklist.md",
    "appendices/research-snapshot.md",
    "appendices/glossary.md",
    "scripts/check_repo.py",
]

SKIP_DIRS = {".git", ".github", "node_modules", ".venv", "venv", "__pycache__"}

# Heading format required by the pack: "### P-CODE-NN — Name" (em dash).
PROMPT_RE = re.compile(r"^### (P-[A-Z]+-\d{2}) \u2014 (.+)$")
NEAR_MISS_RE = re.compile(r"^###\s+P-")

# Markdown link or image: [text](target "optional title")
LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)"
)
INLINE_CODE_RE = re.compile(r"`+[^`]*`+")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

# Fence opener or closer: three or more backticks or tildes, up to 3 spaces indent.
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")

# TODO and TBD are case sensitive; "etc." is case insensitive.
WORD_RE = re.compile(r"(?:\b(?:TODO|TBD)\b)|(?i:\betc\.)")


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return handle.read()


def find_markdown(root):
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            if name.lower().endswith(".md"):
                found.append(Path(dirpath) / name)
    return found


def rel(path, root):
    return path.relative_to(root).as_posix()


def iter_lines(text):
    """Yield (line_number, line, in_fence). Fence delimiter lines count as in_fence."""
    fence_char = None
    fence_len = 0
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE_RE.match(line)
        if fence_char is None:
            if match:
                fence_char = match.group(1)[0]
                fence_len = len(match.group(1))
                yield number, line, True
                continue
            yield number, line, False
        else:
            if (
                match
                and match.group(1)[0] == fence_char
                and len(match.group(1)) >= fence_len
                and not match.group(2).strip()
            ):
                fence_char = None
            yield number, line, True


def exists_exact(dest, root):
    """True if dest exists with exact letter case. None if dest is outside root."""
    try:
        relative = dest.relative_to(root)
    except ValueError:
        return None
    current = root
    for part in relative.parts:
        try:
            names = os.listdir(current)
        except OSError:
            return False
        if part not in names:
            return False
        current = current / part
    return True


def scan_prompts(files, root):
    """Return (prompts, warnings). prompts is a list of dicts."""
    prompts = []
    warnings = []
    for path in files:
        relpath = rel(path, root)
        folder = relpath.split("/")[0] if "/" in relpath else "(root)"
        for number, line, in_fence in iter_lines(read_text(path)):
            if in_fence:
                continue
            match = PROMPT_RE.match(line)
            if match:
                prompts.append(
                    {
                        "id": match.group(1),
                        "name": match.group(2).strip(),
                        "file": relpath,
                        "folder": folder,
                        "line": number,
                    }
                )
            elif NEAR_MISS_RE.match(line):
                warnings.append(
                    f"{relpath}:{number}: heading starts with '### P-' but does not match "
                    f"'### P-CODE-NN \u2014 Name': {line.strip()}"
                )
    return prompts, warnings


def find_duplicates(prompts):
    seen = defaultdict(list)
    for prompt in prompts:
        seen[prompt["id"]].append(prompt)
    warnings = []
    for prompt_id in sorted(seen):
        entries = seen[prompt_id]
        if len(entries) > 1:
            places = ", ".join(f"{e['file']}:{e['line']}" for e in entries)
            warnings.append(f"duplicate prompt ID {prompt_id} appears {len(entries)} times: {places}")
    return warnings


def write_library(prompts, root):
    ordered = sorted(prompts, key=lambda p: (p["folder"], p["id"], p["file"], p["line"]))
    lines = [
        "# Prompt Library",
        "",
        "> Generated by scripts/check_repo.py. Do not edit by hand; run the script again to refresh it.",
        "",
        f"Total prompts: {len(ordered)}",
        "",
        "| ID | Name | File | Folder |",
        "|---|---|---|---|",
    ]
    for p in ordered:
        name = p["name"].replace("|", "\\|")
        lines.append(f"| {p['id']} | {name} | [{p['file']}]({p['file']}) | {p['folder']} |")
    lines.append("")
    target = root / LIBRARY_NAME
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))
    return len(ordered)


def check_tree(root):
    return [name for name in REPO_TREE if not exists_exact(root / name, root)]


def check_links(files, root):
    errors = []
    checked = 0
    for path in files:
        relpath = rel(path, root)
        for number, line, in_fence in iter_lines(read_text(path)):
            if in_fence:
                continue
            cleaned = INLINE_CODE_RE.sub("", line)
            for match in LINK_RE.finditer(cleaned):
                raw = match.group(1)
                if raw.startswith("#") or SCHEME_RE.match(raw):
                    continue
                target = unquote(raw.split("#", 1)[0].split("?", 1)[0])
                if not target:
                    continue
                checked += 1
                base = root if target.startswith("/") else path.parent
                dest = (base / target.lstrip("/")).resolve()
                result = exists_exact(dest, root)
                if result is None:
                    errors.append(f"{relpath}:{number}: link leaves the repo: {raw}")
                elif not result:
                    errors.append(f"{relpath}:{number}: broken link (missing or wrong letter case): {raw}")
    return errors, checked


def check_words(files, root):
    warnings = []
    for path in files:
        relpath = rel(path, root)
        for number, line, _in_fence in iter_lines(read_text(path)):
            for match in WORD_RE.finditer(line):
                warnings.append(f"{relpath}:{number}: contains '{match.group(0)}'")
    return warnings


def section(title):
    print("")
    print(f"== {title}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check the YouTube-Channel-Replication repo.")
    parser.add_argument("--root", help="repo root (default: parent of the scripts folder)")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    parser.add_argument("--no-write", action="store_true", help="do not rewrite prompt-library.md")
    args = parser.parse_args(argv)

    if args.root:
        root = Path(args.root).resolve()
    else:
        root = Path(__file__).resolve().parent.parent
    if not root.is_dir():
        print(f"error: root folder not found: {root}", file=sys.stderr)
        return 2

    errors = []
    warnings = []

    md_files = find_markdown(root)
    scan_files = [p for p in md_files if rel(p, root) != LIBRARY_NAME]

    # 1 and 2: prompt scan, library, duplicate and near-miss warnings.
    section("Prompt scan")
    prompts, near_miss = scan_prompts(scan_files, root)
    warnings.extend(near_miss)
    warnings.extend(find_duplicates(prompts))
    if args.no_write:
        print(f"Found {len(prompts)} prompts. {LIBRARY_NAME} not rewritten (--no-write).")
    else:
        count = write_library(prompts, root)
        print(f"Wrote {LIBRARY_NAME} with {count} prompts.")

    # 3: repo tree.
    section("Repo tree")
    missing = check_tree(root)
    for name in missing:
        errors.append(f"missing file: {name}")
    print(f"{len(REPO_TREE) - len(missing)} of {len(REPO_TREE)} expected files present.")

    # 4: links (re-list so a freshly written prompt-library.md is included).
    section("Links")
    md_files = find_markdown(root)
    link_errors, checked = check_links(md_files, root)
    errors.extend(link_errors)
    print(f"Checked {checked} relative links in {len(md_files)} Markdown files; "
          f"{len(link_errors)} broken.")

    # 5: unfinished-work words.
    section("Unfinished-work words")
    word_warnings = check_words(scan_files, root)
    warnings.extend(word_warnings)
    print(f"{len(word_warnings)} occurrences.")

    # Details.
    if errors:
        section("Errors")
        for message in errors:
            print(f"ERROR: {message}")
    if warnings:
        section("Warnings")
        for message in warnings:
            print(f"WARN: {message}")

    # 6: summary.
    section("Summary")
    print(f"Errors: {len(errors)}   Warnings: {len(warnings)}   Prompts: {len(prompts)}")
    failed = bool(errors) or (args.strict and bool(warnings))
    if failed:
        print("FAIL")
        return 1
    if warnings:
        print("PASS (with warnings)")
    else:
        print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
