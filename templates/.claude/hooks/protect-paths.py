#!/usr/bin/env python3
import json
import pathlib
import subprocess
import sys


def block(reason):
    print(f"Protected path: {reason}", file=sys.stderr)
    raise SystemExit(2)


try:
    event = json.load(sys.stdin)
    if event.get("tool_name") not in ("Edit", "Write"):
        raise SystemExit(0)
    path = event.get("tool_input", {}).get("file_path")
    if not isinstance(path, str) or not path:
        block("missing file_path")
    root = pathlib.Path(subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip()).resolve()
    target = pathlib.Path(path).resolve()
    try:
        relative = target.relative_to(root).as_posix()
    except ValueError:
        block("target outside repository")
    pieces = relative.split("/")
    if any(pieces[i:i+2] == ["src", "generated"] for i in range(len(pieces) - 1)):
        block("generated code: use the generator")
    if "migrations" in pieces:
        tracked = subprocess.run(
            ["git", "ls-files", "--error-unmatch", "--", relative],
            cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            check=False,
        ).returncode == 0
        if tracked:
            block("tracked migration: create a new one and confirm applied state")
except SystemExit:
    raise
except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
    block(f"cannot validate path or hook input ({type(exc).__name__})")
