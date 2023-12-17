# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import os
from aoc.common import get_lines
from aoc.day_04.common import parse_card


def get_sum_points(lines):
    sum_points = 0
    for line in lines:
        _, winning_numbers, our_numbers = parse_card(line)
        num_wins = len(winning_numbers & our_numbers)
        if num_wins:
            points = 2 ** (num_wins - 1)
            sum_points += points
    return sum_points


if __name__ == "__main__":
    script_path = os.path.abspath(os.path.dirname(__file__))
    input_path = os.path.join(script_path, "inputs/parts_1_2.txt")
    print("Day 04, Part 1:", get_sum_points(get_lines(input_path)))
