# DeckDiff

Tiny quick script to diff _Magic: The Gathering_ decks. No runtime dependencies, just read, diff, print.

Tested with Python 3.11 to 3.14.

## Setup

No runtime deps, script just needs Python. For dev (tests etc.), use [uv](https://docs.astral.sh/uv/):

```
uv sync
```

## Usage

- Export the decks you want to diff to text files.
- Each line needs to have the format `<amount> <name>`, so e.g. `1 Path to Exile` or `5 Island`.
- Run the script with Python: `python deckdiff.py A.txt B.txt`
- Output is printed to standard out

## Tests

Tests use `pytest` + `hypothesis` (property-based), dev deps in `pyproject.toml`.

```
uv sync
uv run pytest
```

To test against a specific Python version (e.g. 3.11):

```
uv run --group dev --isolated --python=3.11 python -m pytest tests/
```
