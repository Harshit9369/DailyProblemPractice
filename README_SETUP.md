# LeetCode → GitHub Helper (Java)

This mini-tool lets you type one command and it will:
- Fetch a LeetCode problem description
- Create a folder named `####-Problem-Name/`
- Add a `README.md` with the statement and placeholders for your notes
- Add a `Solution.java` stub
- Commit and push to your GitHub repo automatically

## Quick Start

1) Copy the four files into the root of your **Git repository**:
   - `add_problem.py`
   - `requirements.txt`
   - `.env.example`
   - `leetcode_add.sh`

2) Make the shell script executable:
```bash
chmod +x leetcode_add.sh
```

3) (First time only) let the wrapper create a virtualenv and install deps.

4) Use it:
```bash
# from your repo root
./leetcode_add.sh two-sum
# or:
./leetcode_add.sh 1
# or paste a URL:
./leetcode_add.sh https://leetcode.com/problems/two-sum/
```

The script will:
- Create a folder like `0001-Two-Sum/` with `README.md` and `Solution.java`
- `git add`, `git commit`, and `git push` to your current branch

## Private/Paid problems (optional)

If a problem is paid-only or your network blocks anonymous calls, add cookies:

1) Copy `.env.example` → `.env`
2) Fill in `LEETCODE_SESSION` and `LEETCODE_CSRF_TOKEN` from your browser (while logged into LeetCode).
   - DevTools → Application → Cookies → `leetcode.com`
3) Run the script again.

## Notes

- The problem description is converted from HTML to Markdown.
- The commit message looks like `Add: 1. Two Sum`.
- If push fails, make sure your repo has `origin` remote and authenticated git (SSH or HTTPS).

Happy grinding!
