# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import os
from collections import deque
from aoc.common import get_lines
from aoc.day_03.regex import REGEX_NUMBER, REGEX_CHAR_IS_SYMBOL


def has_adjacent_symbol(sliding_window, start, end):
    """Whether there is an adjacent symbol surrounding start and end of number."""
    for row in (0, 1, 2):
        scan_positions = range(start - 1, end + 1) if row != 1 else (start - 1, end)
        for pos in scan_positions:
            if 0 <= pos < len(sliding_window[row]):
                if REGEX_CHAR_IS_SYMBOL.match(sliding_window[row][pos]):
                    return True
    return False


def find_part_numbers(sliding_window):
    """Find all the part numbers in the middle row of the sliding window."""
    part_numbers = []
    middle_row = sliding_window[1]
    for match in REGEX_NUMBER.finditer(middle_row):
        if has_adjacent_symbol(sliding_window, match.start(), match.end()):
            part_numbers.append(int(match.group()))
    return part_numbers


def get_sum_part_numbers(lines):
    """Get the sum of all the part numbers found."""
    sum_part_numbers = 0

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
            sum_part_numbers += sum(find_part_numbers(sliding_window))
    if last_line:
        sliding_window.popleft()
        sliding_window.append("." * len(last_line))
        sum_part_numbers += sum(find_part_numbers(sliding_window))

    return sum_part_numbers


if __name__ == "__main__":
    script_path = os.path.abspath(os.path.dirname(__file__))
    input_path = os.path.join(script_path, "inputs/parts_1_2.txt")
    print("Day 03, Part 1:", get_sum_part_numbers(get_lines(input_path)))
