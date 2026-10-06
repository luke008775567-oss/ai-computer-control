"""Additional safe agent utilities.

These helpers are deliberately read-only or bounded. They form the foundation for
the next expansion without granting the agent unrestricted shell execution.
"""

from __future__ import annotations

import json
import os
import platform
import subprocess
from pathlib import Path
from typing import Any


def system_info() -> dict[str, Any]:
    """Return basic non-sensitive local system information."""
    return {
        "platform": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "python": platform.python_version(),
        "home": str(Path.home()),
    }


def list_processes(limit: int = 100) -> list[dict[str, str]]:
    """List processes without exposing command-line arguments or environment secrets."""
    limit = max(1, min(limit, 1000))
    if platform.system() != "Darwin":
        return []
    result = subprocess.run(
        ["ps", "-axo", "pid=,comm="],
        capture_output=True,
        text=True,
        check=True,
        timeout=5,
    )
    rows = []
    for line in result.stdout.splitlines()[:limit]:
        parts = line.strip().split(None, 1)
        if len(parts) == 2:
            rows.append({"pid": parts[0], "name": parts[1]})
    return rows


def safe_path(path: str, roots: list[str] | None = None) -> Path:
    """Resolve a path and optionally enforce allowed root directories."""
    p = Path(path).expanduser().resolve()
    if roots:
        allowed = [Path(r).expanduser().resolve() for r in roots]
        if not any(p == root or root in p.parents for root in allowed):
            raise PermissionError("Path is outside the configured allowed roots")
    return p


def json_result(value: Any) -> str:
    """Serialize tool results consistently."""
    return json.dumps(value, ensure_ascii=False, indent=2, default=str)
