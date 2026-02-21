# Profile-Viewer
A terminal-based launcher that lets you quickly open websites or apps from an interactive menu.

## Requirements

- Python 3.10+

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Profile-Viewer.git
   cd Profile-Viewer
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install pick
   ```

## Usage

```bash
python app.py
```

Use the arrow keys to navigate the menu and press **Enter** to open your selection. Press **Ctrl+C** to exit.

> **Note:** Run this in a native terminal (e.g. macOS Terminal or iTerm2), not inside an IDE's embedded terminal, as the interactive menu requires full TTY support.