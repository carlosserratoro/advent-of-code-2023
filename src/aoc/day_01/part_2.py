# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import os
from aoc.common import get_lines
from aoc.day_01.trie import Trie


DIGITS_NUMBERS = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}
DIGITS_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
DIGITS_WORDS_REVERSED = {
    word[::-1]: word_value for (word, word_value) in DIGITS_WORDS.items()
}


def get_calibration_value(trie, line, direction):
    """Given a calibration string, return its number.

    We may start scanning the line from the left to the right,
    i.e. direction `>`, or from the right to the left, i.e. `<`.
    """
    assert direction in (">", "<")

    value = 0
    trie.starve()

    starting_index = 0 if direction == ">" else len(line) - 1
    ending_index = len(line) - 1 if direction == ">" else 0
    sign = +1 if direction == ">" else -1

    c_idx = starting_index
    while not value and c_idx < len(line):
        feed_success = trie.feed(line[c_idx])
        if feed_success and c_idx == ending_index:
            value = trie.last_value
        elif trie.last_value and not feed_success:
            value = trie.last_value

        # Keep advancing. If we failed, rollback so that we discard
        # all but the first character from the last time we started
        # searching.
        c_idx += sign * 1
        if not feed_success:
            c_idx -= sign * (trie.len_feed - 1)
            trie.starve()

    return value


def get_sum_calibration_values(calibration_lines):
    trie_left = Trie()
    for key, value in {**DIGITS_NUMBERS, **DIGITS_WORDS}.items():
        trie_left[key] = value

    trie_right = Trie()
    for key, value in {**DIGITS_NUMBERS, **DIGITS_WORDS_REVERSED}.items():
        trie_right[key] = value

    sum_calibrations = 0
    for line in calibration_lines:
        num_left = get_calibration_value(trie_left, line, direction=">")
        num_right = get_calibration_value(trie_right, line, direction="<")
        sum_calibrations += 10 * num_left + num_right
    return sum_calibrations


if __name__ == "__main__":
    script_path = os.path.abspath(os.path.dirname(__file__))
    input_path = os.path.join(script_path, "inputs/parts_1_2.txt")
    print("Day 01, Part 2:", get_sum_calibration_values(get_lines(input_path)))
