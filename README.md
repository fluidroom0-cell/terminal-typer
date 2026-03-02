# TypingCLI ⌨️

A terminal-based typing practice app built with Python and `curses`.

## What it does

Displays a quote on screen and tracks your keystrokes in real time — correct input shows in green, mistakes in red. Errors are counted and displayed as you type. Once you complete a quote, a new one loads automatically.

## Current Features

- Real-time keystroke feedback (green / red)
- Error counter
- Auto-loads new quotes on completion
- Adapts to terminal size

## Roadmap

This is just the foundation. Planned additions:

- **Stats tracking** — WPM, accuracy, personal bests
- **Leaderboard** — compete against others
- **Quote categories** — code snippets, literature, custom sets
- **Difficulty modes** — punctuation-heavy, long-form, timed challenges
- **Progress history** — track improvement over time
- **Config file** — custom themes, keybindings, quote sources

## Run

```bash
python main.py
```

Requires Python 3 (no extra dependencies — uses stdlib `curses`).

