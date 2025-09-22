# About

A simple terminal-based client for ollama on ubuntu linux (or similar).
Automatically handles installing ollama and models.

automatically logs all conversations to the `logs/` folder for retrieval.

# Author

William Jackson (william@wxj.me)

# Setup
this project uses uv as its package and virtual environment manager.
see the install instructions here: https://docs.astral.sh/uv/getting-started/installation/


# Usage
run the project:
```bash
uv run main.py
```

## Navigation
press Ctrl+C to go back or close the program.
In the future, I want to make conversations continuable, but for now, they're lost once closed.

the multiline input isn't super robust (once you go to a new line, it can't be edited again, and arrow key navigation doesn't work), so I recommend drafting your responses in another app and pasting them in.
