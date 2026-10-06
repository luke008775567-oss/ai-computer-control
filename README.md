# AI Computer Control

A macOS-focused MCP server for safe, allowlisted computer control.

## Features
- Screenshots
- Mouse control
- Keyboard control
- Open macOS apps
- Open HTTP(S) URLs
- Wait/delay
- Safety gates and PyAutoGUI failsafe

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Enable computer-changing actions only after testing:

```bash
export AI_COMPUTER_CONTROL_ENABLED=true
export AI_COMPUTER_CONTROL_CONFIRM=true
python server.py
```

macOS may require Accessibility and Screen Recording permissions for the app running the server.

The server intentionally does not expose arbitrary shell execution.
