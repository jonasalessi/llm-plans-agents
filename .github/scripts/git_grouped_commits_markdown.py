#!/usr/bin/env python3
"""
Outputs commit messages between a given tag and a target branch, grouped by
conventional commit-like prefixes, as Markdown.

WHY: Provide a predictable, easily parsed changelog snapshot for releases.

Usage:
  python .github/scripts/git_grouped_commits_markdown.py <tag> [<targetBranch>]

Examples:
  python .github/scripts/git_grouped_commits_markdown.py v1.2.3
  python .github/scripts/git_grouped_commits_markdown.py v1.2.3 develop
  DEFAULT_BRANCH=release python .github/scripts/git_grouped_commits_markdown.py v1.2.3
"""
import argparse
import os
import re
import subprocess
import sys
from typing import Callable, Dict, List, Tuple


# Constants for configuration and formatting
PREFIXES: List[str] = [
    'feat', 'fix', 'chore', 'refactor', 'docs', 'test', 'style', 'perf', 'ci', 'build', 'revert'
]
DEFAULT_BRANCH: str = os.getenv('DEFAULT_BRANCH', 'main')
TITLE: str = 'Commit Messages Grouped by Prefix'
COMMIT_PREFIX_RE = re.compile(r'^(\w+)(\([^)]+\))?:')


def getCommitMessages(tag: str, targetBranch: str, runCmd: Callable = subprocess.run) -> List[str]:
    """Return commit subjects between tag and targetBranch.

    External command execution is inverted through runCmd for testability.
    """
    try:
        result = runCmd(
            ['git', 'log', f'{tag}..{targetBranch}', '--pretty=format:%s'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        err = e.stderr.strip() if e.stderr else str(e)
        raise RuntimeError(f'git log failed: {err}') from e

    raw = result.stdout.strip() if result.stdout else ''
    if not raw:
        return []

    messages = [line.strip() for line in raw.split('\n') if line.strip()]
    return messages


def groupByPrefix(messages: List[str], prefixes: List[str] = PREFIXES) -> Tuple[Dict[str, List[str]], List[str]]:
    """Group messages by known prefixes and collect the rest as otherMessages."""
    if not messages:
        return ({p: [] for p in prefixes}, [])

    grouped: Dict[str, List[str]] = {p: [] for p in prefixes}
    otherMessages: List[str] = []

    for message in messages:
        match = COMMIT_PREFIX_RE.match(message)
        if not match:
            otherMessages.append(message)
            continue

        prefix = match.group(1)
        if prefix in grouped:
            grouped[prefix].append(message)
            continue

        otherMessages.append(message)

    return grouped, otherMessages


def renderMarkdown(grouped: Dict[str, List[str]], otherMessages: List[str], ctx: Dict[str, str]) -> str:
    """Render the grouped messages as Markdown and return the content."""
    lines: List[str] = []
    lines.append(f'# {TITLE}')
    lines.append('')
    lines.append(f'- **From tag:** `{ctx["tag"]}`')
    lines.append(f'- **To branch:** `{ctx["targetBranch"]}`')
    lines.append('')

    for prefix in PREFIXES:
        msgs = grouped.get(prefix, [])
        if not msgs:
            continue
        lines.append(f'## {prefix}')
        for msg in msgs:
            lines.append(f'- {msg}')
        lines.append('')

    if otherMessages:
        lines.append('## Other')
        for msg in otherMessages:
            lines.append(f'- {msg}')
        lines.append('')

    return '\n'.join(lines)


def parseArgs(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Output commit messages between a tag and branch grouped by prefix as Markdown.'
    )
    parser.add_argument('tag', help='Starting tag (exclusive). Example: v1.0.0')
    parser.add_argument(
        'targetBranch', nargs='?', default=DEFAULT_BRANCH,
        help=f'Target branch (default: {DEFAULT_BRANCH}).'
    )
    return parser.parse_args(argv)


def run(argv: List[str]) -> int:
    args = parseArgs(argv)
    ctx = {'tag': args.tag, 'targetBranch': args.targetBranch}

    try:
        messages = getCommitMessages(args.tag, args.targetBranch)
    except RuntimeError as e:
        print(str(e), file=sys.stderr)
        return 1

    grouped, otherMessages = groupByPrefix(messages)
    markdown = renderMarkdown(grouped, otherMessages, ctx)
    print(markdown)
    return 0


if __name__ == '__main__':
    sys.exit(run(sys.argv[1:]))
