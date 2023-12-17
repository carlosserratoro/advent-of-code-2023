# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_04.part_1 import parse_card


def test_parse_card():
    card_number, winning_numbers, our_numbers = parse_card(
        "Card 99: 41 48 83 86 17 | 83 86 6 31 17 9 48 53"
    )
    assert 99 == card_number
    assert {41, 48, 83, 86, 17} == winning_numbers
    assert {83, 86, 6, 31, 17, 9, 48, 53} == our_numbers
