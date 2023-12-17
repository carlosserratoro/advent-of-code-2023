# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import os
from collections import deque
from aoc.common import get_lines
from aoc.day_03.regex import REGEX_NUMBER, REGEX_CHAR_IS_SYMBOL


def get_adjacent_numbers(sliding_window, pos):
    """Get list of adjacent numbers surrounding a given position."""
    adjacent_numbers = []
    for row_no, row in enumerate(sliding_window):
        match_numbers = REGEX_NUMBER.finditer(row)
        for match, start, end in [
            (m.group(), m.start() - 1, m.end()) for m in match_numbers
        ]:
            if start <= pos <= end:
                adjacent_numbers.append(int(match))
    return adjacent_numbers


def find_gear_ratios(sliding_window):
    """Find all the gear ratios in the sliding window."""
    gear_ratios = []
    middle_row = sliding_window[1]
    for match in REGEX_CHAR_IS_SYMBOL.finditer(middle_row):
        adjacent_numbers = get_adjacent_numbers(sliding_window, match.start())
        if len(adjacent_numbers) == 2:
            # A gear consists of exactly two adjacent numbers.
            gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])
    return gear_ratios


def get_sum_gear_ratios(lines):
    """Get the sum of all the gear ratios found."""
    sum_gear_ratios = 0

    sliding_window = deque()
    last_line = None
    for line_no, line in enumerate(lines):
        last_line = line
        if line_no == 0:
            sliding_window.append("." * len(last_line))
            sliding_window.append("." * len(last_line))
            sliding_window.append(last_line)
        else:
            sliding_window.popleft()
            sliding_window.append(last_line)
            sum_gear_ratios += sum(find_gear_ratios(sliding_window))
    if last_line:
        sliding_window.popleft()
        sliding_window.append("." * len(last_line))
        sum_gear_ratios += sum(find_gear_ratios(sliding_window))

    return sum_gear_ratios


if __name__ == "__main__":
    script_path = os.path.abspath(os.path.dirname(__file__))
    input_path = os.path.join(script_path, "inputs/parts_1_2.txt")
    print("Day 03, Part 2:", get_sum_gear_ratios(get_lines(input_path)))
