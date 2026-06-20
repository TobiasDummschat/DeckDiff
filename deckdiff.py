from argparse import Namespace, ArgumentParser
from collections import Counter
from pathlib import Path


def to_counter(text: str) -> Counter:
    lines = text.split("\n")
    count_and_names = [
        line.strip().split(" ", maxsplit=1) for line in lines if line.strip()
    ]
    return Counter({name: int(count) for count, name in count_and_names})


def to_text(counter: Counter) -> str:
    return "\n".join([f"{count} {card}" for card, count in counter.items()])


def print_counter(title: str, counter: Counter) -> None:
    text = to_text(counter)
    title_spaces = 2
    title_hashes = 3
    bar_length = len(title) + 2 * (title_spaces + title_hashes)
    bar = "#" * bar_length
    title_line = (
        "#" * title_hashes
        + " " * title_spaces
        + title
        + " " * title_spaces
        + "#" * title_hashes
    )
    print(f"{bar}\n{title_line}\n{bar}\n\n{text}\n")


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("deck_a", type=Path)
    parser.add_argument("deck_b", type=Path)
    return parser.parse_args()


def main():
    args = parse_args()

    text_a = args.deck_a.read_text()
    text_b = args.deck_b.read_text()

    counter_a = to_counter(text_a)
    counter_b = to_counter(text_b)

    a_not_b = counter_a - counter_b
    b_not_a = counter_b - counter_a
    intersection = counter_a & counter_b

    print_counter("Intersection", intersection)
    print_counter("In A but not B", a_not_b)
    print_counter("In B but not A", b_not_a)


if __name__ == "__main__":
    main()
