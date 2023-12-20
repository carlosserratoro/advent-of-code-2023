# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_07.hand import Hand
from aoc.day_07.hand_types import HandTypes
from aoc.day_07.card_strenghts import CARD_STRENGTHS


def test_hand_type():
    assert Hand("AAAAA").hand_type == HandTypes.FIVE_OF_A_KIND
    assert Hand("AA8AA").hand_type == HandTypes.FOUR_OF_A_KIND
    assert Hand("23332").hand_type == HandTypes.FULL_HOUSE
    assert Hand("TTT98").hand_type == HandTypes.THREE_OF_A_KIND
    assert Hand("23432").hand_type == HandTypes.TWO_PAIR
    assert Hand("A23A4").hand_type == HandTypes.ONE_PAIR
    assert Hand("23456").hand_type == HandTypes.HIGH_CARD

    hand = Hand("AKQJT")
    expected_hand_type = HandTypes.HIGH_CARD
    assert hand.hand_type == expected_hand_type

    # Repeat, because we cache the value.
    assert hand.hand_type == expected_hand_type


def test_hand_type_with_jokers():
    assert Hand("2345J", use_jokers=True).hand_type == HandTypes.ONE_PAIR
    assert Hand("234JJ", use_jokers=True).hand_type == HandTypes.THREE_OF_A_KIND
    assert Hand("23JJJ", use_jokers=True).hand_type == HandTypes.FOUR_OF_A_KIND
    assert Hand("2JJJJ", use_jokers=True).hand_type == HandTypes.FIVE_OF_A_KIND

    hand = Hand("KTJJT", use_jokers=True)
    expected_hand_type = HandTypes.FOUR_OF_A_KIND
    assert hand.hand_type == expected_hand_type

    # Repeat, because we cache the value.
    assert hand.hand_type == expected_hand_type


def test_strength():
    base = len(CARD_STRENGTHS)
    hand = Hand("AKQJT")
    expected_strength = (
        base**0 * CARD_STRENGTHS["T"]
        + base**1 * CARD_STRENGTHS["J"]
        + base**2 * CARD_STRENGTHS["Q"]
        + base**3 * CARD_STRENGTHS["K"]
        + base**4 * CARD_STRENGTHS["A"]
    )
    assert hand.strength == expected_strength

    # Repeat, because we cache the value.
    assert hand.strength == expected_strength


def test_lt():
    # Different types
    assert Hand("AA8AA") < Hand("AAAAA")
    assert Hand("23332") < Hand("AA8AA")
    assert Hand("TTT98") < Hand("23332")
    assert Hand("23432") < Hand("TTT98")
    assert Hand("A23A4") < Hand("23432")
    assert Hand("23456") < Hand("A23A4")

    # Same type, different strength
    assert Hand("23332") < Hand("33322")
