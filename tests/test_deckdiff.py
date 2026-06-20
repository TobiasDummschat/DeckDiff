from collections import Counter

from hypothesis import given
from hypothesis import strategies as st

from deckdiff import diff_decks, print_counter, to_counter, to_text

card_names = st.text(min_size=1).map(str.strip).filter(lambda s: s and "\n" not in s)
counts = st.integers(min_value=1, max_value=99)
decks = st.dictionaries(card_names, counts, max_size=15).map(Counter)


def test_to_counter_parses_amount_and_name():
    assert to_counter("1 Sol Ring") == Counter({"Sol Ring": 1})


def test_to_counter_skips_blank_lines():
    assert to_counter("1 Sol Ring\n\n\n4 Island\n") == Counter(
        {"Sol Ring": 1, "Island": 4},
    )


def test_to_counter_keeps_full_multiword_name():
    assert to_counter("1 Kynaios and Tiro of Meletis") == Counter(
        {"Kynaios and Tiro of Meletis": 1},
    )


def test_to_counter_to_text_roundtrip():
    original = Counter({"Sol Ring": 1, "Island": 4})
    assert to_counter(to_text(original)) == original


def test_print_counter_wraps_title_in_hash_bar_and_lists_cards(capsys):
    print_counter("Foo", Counter({"Sol Ring": 1}))
    out = capsys.readouterr().out
    assert out == "#############\n###  Foo  ###\n#############\n\n1 Sol Ring\n\n"


@given(decks)
def test_to_counter_to_text_is_idempotent(deck):
    once = to_counter(to_text(deck))
    twice = to_counter(to_text(once))
    assert once == twice == deck


@given(decks, decks)
def test_diff_and_intersection_recombine_into_original_decks(deck_a, deck_b):
    a_not_b, b_not_a, intersection = diff_decks(deck_a, deck_b)
    assert a_not_b + intersection == deck_a
    assert b_not_a + intersection == deck_b


@given(decks, decks)
def test_a_not_b_and_b_not_a_share_no_cards(deck_a, deck_b):
    a_not_b, b_not_a, _ = diff_decks(deck_a, deck_b)
    assert not (set(a_not_b) & set(b_not_a))
