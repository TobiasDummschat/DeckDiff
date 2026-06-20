# DeckDiff

Tiny quick script to diff _Magic: The Gathering_ decks. No dependencies, no tests, just read, diff, print.

Only tested with Python 3.14.

## Usage

1. Export the decks you want to diff to text files. Each line needs to have the format "\<amount> \<name>", so e.g. "1 Counterspell" or "5 Island".
1. Run the script with Python: `python deckdiff.py A.txt B.txt`
1. Output is printed to standard out
