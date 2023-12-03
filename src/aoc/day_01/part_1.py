# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import os
from aoc.common import get_lines


def get_calibration_value(line):
    """Given a calibration string, return its number."""

    # Search for the first digit.
    idx = 0
    while not line[idx].isdigit():
        idx += 1
    value = int(line[idx]) * 10

    # Search for the last digit.
    idx = len(line) - 1
    while not line[idx].isdigit():
        idx -= 1
    value += int(line[idx])

    return value


def get_sum_calibration_values(calibration_lines):
    sum_calibrations = 0
    for line in calibration_lines:
        num = get_calibration_value(line)
        sum_calibrations += num
    return sum_calibrations


if __name__ == "__main__":
    script_path = os.path.abspath(os.path.dirname(__file__))
    input_path = os.path.join(script_path, "inputs/parts_1_2.txt")
    print("Day 01, Part 1:", get_sum_calibration_values(get_lines(input_path)))
