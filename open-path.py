#!/usr/bin/env python3
"""Open a Herdr clicked local path using the Ubuntu default application."""

import os
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


def local_path(value: str, cwd: str | None = None) -> Path | None:
    if not value or any(ord(char) < 32 for char in value):
        return None
    if value.startswith("file://"):
        uri = urlsplit(value)
        if uri.scheme != "file" or uri.netloc not in ("", "localhost"):
            return None
        path = Path(unquote(uri.path))
    else:
        if "://" in value:
            return None
        path = Path(os.path.expanduser(value))

    if not path.is_absolute():
        if not cwd or not Path(cwd).is_absolute():
            return None
        path = Path(cwd) / path

    if not path.exists():
        path = Path(re.sub(r":\d+(?::\d+)?$", "", str(path)))

    path = path.resolve()
    return path if path.exists() else None


def main() -> int:
    value = os.environ.get("HERDR_PLUGIN_CLICKED_URL", "")
    try:
        context = json.loads(os.environ.get("HERDR_PLUGIN_CONTEXT_JSON", "{}"))
        path = local_path(value, context.get("focused_pane_cwd"))
    except (ValueError, OSError, RuntimeError):
        return 1
    if path is None:
        return 1

    try:
        return subprocess.run(["xdg-open", str(path)], check=False).returncode
    except OSError:
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
