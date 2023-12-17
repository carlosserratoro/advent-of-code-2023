# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import os
from aoc.common import get_lines
from aoc.day_04.common import parse_card
from collections import defaultdict


def get_num_scratchcards(lines):
    scratch_cards_copies = defaultdict(lambda: 1)
    for line in lines:
        card_number, winning_numbers, our_numbers = parse_card(line)
        num_wins = len(winning_numbers & our_numbers)
        copies_to_add = scratch_cards_copies[card_number]
        for new_card_number in range(card_number + 1, card_number + 1 + num_wins):
            scratch_cards_copies[new_card_number] += copies_to_add
    return sum(scratch_cards_copies.values())


if __name__ == "__main__":
    script_path = os.path.abspath(os.path.dirname(__file__))
    input_path = os.path.join(script_path, "inputs/parts_1_2.txt")
    print("Day 04, Part 2:", get_num_scratchcards(get_lines(input_path)))
