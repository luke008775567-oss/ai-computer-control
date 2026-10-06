"""Safe macOS computer-control MCP server."""
from __future__ import annotations
import os, subprocess, time, webbrowser
from pathlib import Path
import pyautogui
from mcp.server import MCPServer

mcp = MCPServer("AI Computer Control")
CONTROL_ENABLED = os.getenv("AI_COMPUTER_CONTROL_ENABLED", "false").lower() == "true"
CONFIRM_ENABLED = os.getenv("AI_COMPUTER_CONTROL_CONFIRM", "false").lower() == "true"
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.08

def require_control(action: str, sensitive: bool = False):
    if not CONTROL_ENABLED:
        raise PermissionError(f"{action} is disabled. Set AI_COMPUTER_CONTROL_ENABLED=true.")
    if sensitive and not CONFIRM_ENABLED:
        raise PermissionError(f"{action} requires AI_COMPUTER_CONTROL_CONFIRM=true.")

@mcp.tool()
def control_status() -> dict:
    """Return current safety settings."""
    return {"control_enabled": CONTROL_ENABLED, "confirmation_enabled": CONFIRM_ENABLED, "pyautogui_failsafe": bool(pyautogui.FAILSAFE)}

@mcp.tool()
def screenshot() -> str:
    """Capture the screen to a temporary PNG file."""
    path = Path("/tmp/ai-computer-control-screen.png")
    pyautogui.screenshot().save(path)
    return str(path)

@mcp.tool()
def move_mouse(x: int, y: int) -> str:
    """Move mouse to screen coordinates."""
    require_control("move_mouse"); pyautogui.moveTo(x, y, duration=.2); return f"Moved to ({x}, {y})."

@mcp.tool()
def click(x: int, y: int, button: str = "left") -> str:
    """Click at coordinates."""
    require_control("click")
    if button not in {"left","right","middle"}: raise ValueError("Invalid mouse button")
    pyautogui.click(x=x, y=y, button=button); return f"Clicked {button} at ({x}, {y})."

@mcp.tool()
def double_click(x: int, y: int) -> str:
    """Double-click at coordinates."""
    require_control("double_click"); pyautogui.doubleClick(x=x,y=y); return f"Double-clicked at ({x}, {y})."

@mcp.tool()
def scroll(amount: int) -> str:
    """Scroll vertically."""
    require_control("scroll"); pyautogui.scroll(amount); return f"Scrolled {amount}."

@mcp.tool()
def type_text(text: str) -> str:
    """Type text into the focused application."""
    require_control("type_text", True)
    if len(text)>5000: raise ValueError("Text is limited to 5000 characters")
    pyautogui.write(text, interval=.01); return f"Typed {len(text)} characters."

@mcp.tool()
def press_key(key: str) -> str:
    """Press an allowlisted keyboard key."""
    require_control("press_key", True)
    allowed={"enter","esc","escape","tab","space","backspace","delete","up","down","left","right","home","end","pageup","pagedown","shift","ctrl","alt","command","cmd"}
    k=key.lower()
    if k not in allowed and not (len(k)==1 and k.isprintable()): raise ValueError("Unsupported key")
    pyautogui.press(k); return f"Pressed {key}."

@mcp.tool()
def open_app(app_name: str) -> str:
    """Open a named macOS application without a shell."""
    require_control("open_app", True)
    if not app_name.strip() or len(app_name)>200: raise ValueError("Invalid app name")
    subprocess.run(["open","-a",app_name], check=True, timeout=10)
    return f"Opened {app_name}."

@mcp.tool()
def open_url(url: str) -> str:
    """Open an HTTP(S) URL in the default browser."""
    require_control("open_url", True)
    if not (url.startswith("https://") or url.startswith("http://")): raise ValueError("Only HTTP(S) URLs are allowed")
    webbrowser.open(url); return f"Opened {url}."

@mcp.tool()
def wait(seconds: float) -> str:
    """Wait up to 30 seconds."""
    if not 0 <= seconds <= 30: raise ValueError("seconds must be between 0 and 30")
    time.sleep(seconds); return f"Waited {seconds:g} seconds."

if __name__ == "__main__":
    mcp.run()
