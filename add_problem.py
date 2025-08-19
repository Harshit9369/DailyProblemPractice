#!/usr/bin/env python3
"""
LeetCode → GitHub helper
---------------------------------
Usage:
  python add_problem.py <slug_or_number_or_url> [--repo .] [--no-push]

Examples:
  python add_problem.py two-sum
  python add_problem.py 1
  python add_problem.py https://leetcode.com/problems/two-sum/

What it does:
  • Fetches problem metadata & description from LeetCode
  • Creates folder: "0001-Two-Sum/" (number + kebab-case title)
  • Writes README.md with the problem statement + placeholders for your notes
  • Adds a Solution.java stub
  • git add/commit/push to your repo (unless --no-push)
Dependencies:
  pip install requests markdownify python-dotenv
Optional (private/paid problems):
  Put your LeetCode cookies into a .env file (see .env.example) or export them in shell.
"""

import argparse
import os
import re
import sys
import json
import subprocess
from pathlib import Path

import requests
from markdownify import markdownify as md
from dotenv import load_dotenv

LC_GRAPHQL = "https://leetcode.com/graphql"
LC_ALL_API = "https://leetcode.com/api/problems/all/"

def run(cmd, cwd=None, check=True):
    print("$", " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, check=check)

def guess_repo_root(start: Path) -> Path:
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             cwd=start, capture_output=True, text=True, check=True)
        return Path(out.stdout.strip())
    except subprocess.CalledProcessError:
        return start

def normalize_input(s: str) -> str:
    s = s.strip()
    # If URL, extract slug
    m = re.search(r"/problems/([^/]+)/", s)
    if m:
        return m.group(1)
    # If number
    if s.isdigit():
        return s
    # Probably a slug-like or title; convert spaces to dashes
    return re.sub(r"\s+", "-", s.lower())

def get_slug_from_number(frontend_id: str, headers: dict) -> str:
    print("Resolving number → slug via LeetCode public API...")
    r = requests.get(LC_ALL_API, headers=headers, timeout=30)
    r.raise_for_status()
    data = r.json()
    for pair in data.get("stat_status_pairs", []):
        stat = pair.get("stat", {})
        if str(stat.get("frontend_question_id")) == str(frontend_id):
            return stat.get("question__title_slug")
    raise ValueError(f"Could not find slug for problem number {frontend_id}.")

def fetch_problem(slug: str, headers: dict) -> dict:
    print(f"Fetching problem data for slug '{slug}' ...")
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        titleSlug
        content
        difficulty
        topicTags { name slug }
        isPaidOnly
      }
    }
    """
    payload = {"query": query, "variables": {"titleSlug": slug}}
    r = requests.post(LC_GRAPHQL, json=payload, headers=headers, timeout=60)
    if r.status_code != 200:
        raise RuntimeError(f"GraphQL request failed with status {r.status_code}: {r.text[:200]}")
    data = r.json()
    q = data.get("data", {}).get("question")
    if not q:
        raise RuntimeError(f"Could not fetch question data for slug '{slug}'. Response: {data}")
    return q

def to_folder_name(frontend_id: str, title: str) -> str:
    def sanitize(t: str) -> str:
        t = re.sub(r"[^\w\s-]", "", t)  # remove punctuation
        t = re.sub(r"\s+", "-", t.strip())
        return t
    return f"{int(frontend_id):04d}-{sanitize(title)}"

def ensure_java_stub(folder: Path, class_name: str = "Solution"):
    java_path = folder / "Solution.java"
    if java_path.exists():
        return
    java_code = f"""\
public class {class_name} {{
    // Paste your final solution here.
    // You can write a main() to test locally; LeetCode ignores it.
    public static void main(String[] args) {{
        // quick local check
        System.out.println("Ready to code: {class_name}");
    }}
}}
"""
    java_path.write_text(java_code, encoding="utf-8")

def write_readme(folder: Path, q: dict):
    readme = folder / "README.md"
    tags = ", ".join(t["name"] for t in q.get("topicTags", [])) or "—"
    link = f"https://leetcode.com/problems/{q['titleSlug']}/"
    paid_note = " (Paid Only)" if q.get("isPaidOnly") else ""
    # Convert HTML to Markdown
    content_md = md(q.get("content") or "", heading_style="ATX", strip=["span"])
    template = f"""# {q['questionFrontendId']}. {q['title']}

**Difficulty:** {q.get('difficulty', '—')}{paid_note}  
**Tags:** {tags}  
**Link:** {link}

---

## Problem
{content_md}

---

## My Approach
(Write your thought process, observations, invariants, edge cases, patterns.)

## Complexity
- Time: O(?)
- Space: O(?)

## Alternate Approaches
(Outline other viable solutions and when to prefer them.)

## Notes
(Add proofs, pitfalls, and follow-ups.)
"""
    readme.write_text(template, encoding="utf-8")

def load_headers_from_env() -> dict:
    """
    Returns headers for LeetCode requests.
    If you provide LEETCODE_SESSION and CSRFTOKEN in environment/.env,
    we attach them — useful for paid/private problems.
    """
    load_dotenv()
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com",
        "Origin": "https://leetcode.com",
        "Content-Type": "application/json",
    }
    leet_session = os.getenv("LEETCODE_SESSION")
    csrf = os.getenv("LEETCODE_CSRF_TOKEN") or os.getenv("CSRFTOKEN") or os.getenv("CSRF_TOKEN")
    cookie = []
    if leet_session:
        cookie.append(f"LEETCODE_SESSION={leet_session}")
    if csrf:
        cookie.append(f"csrftoken={csrf}")
        headers["x-csrftoken"] = csrf
    if cookie:
        headers["Cookie"] = "; ".join(cookie)
    return headers

def main():
    parser = argparse.ArgumentParser(description="Create problem folder from LeetCode and commit to GitHub.")
    parser.add_argument("problem", help="LeetCode slug, number, or URL")
    parser.add_argument("--repo", default=".", help="Path to your Git repo (default: current directory)")
    parser.add_argument("--no-push", action="store_true", help="Skip git push")
    args = parser.parse_args()

    headers = load_headers_from_env()

    inp = normalize_input(args.problem)
    if inp.isdigit():
        slug = get_slug_from_number(inp, headers=headers)
    else:
        slug = inp

    q = fetch_problem(slug, headers=headers)
    folder_name = to_folder_name(q["questionFrontendId"], q["title"])
    repo_root = guess_repo_root(Path(args.repo).resolve())
    target = repo_root / folder_name
    target.mkdir(exist_ok=True)

    write_readme(target, q)
    ensure_java_stub(target)

    # Git add/commit/push
    # Detect branch
    try:
        out = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                             cwd=repo_root, capture_output=True, text=True, check=True)
        branch = out.stdout.strip()
    except subprocess.CalledProcessError:
        branch = "main"

    run(["git", "add", str(target)], cwd=repo_root)
    msg = f"Add: {q['questionFrontendId']}. {q['title']}"
    try:
        run(["git", "commit", "-m", msg], cwd=repo_root)
    except subprocess.CalledProcessError:
        print("Nothing to commit (maybe files unchanged).")

    if not args.no_push:
        try:
            run(["git", "push", "origin", branch], cwd=repo_root)
        except subprocess.CalledProcessError:
            print("Push failed. Ensure your repo has a remote named 'origin' and you are authenticated.")

    print(f"Done. Created {target}")
    print("Happy coding!")

if __name__ == "__main__":
    main()
