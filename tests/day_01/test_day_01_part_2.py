# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_01.part_2 import get_calibration_value
from aoc.day_01.part_2 import DIGITS_NUMBERS, DIGITS_WORDS, DIGITS_WORDS_REVERSED
from aoc.day_01.trie import Trie


def test_get_calibration_value_left():
    trie_left = Trie()
    for key, value in {**DIGITS_NUMBERS, **DIGITS_WORDS}.items():
        trie_left[key] = value

    assert 2 == get_calibration_value(trie_left, "two1nine", ">")
    assert 8 == get_calibration_value(trie_left, "eightwothree", ">")
    assert 1 == get_calibration_value(trie_left, "abcone2threexyz", ">")
    assert 2 == get_calibration_value(trie_left, "xtwone3four", ">")
    assert 4 == get_calibration_value(trie_left, "4nineeightseven2", ">")
    assert 1 == get_calibration_value(trie_left, "zoneight234", ">")
    assert 7 == get_calibration_value(trie_left, "7pqrstsixteen", ">")


def test_get_calibration_value_right():
    trie_right = Trie()
    for key, value in {**DIGITS_NUMBERS, **DIGITS_WORDS_REVERSED}.items():
        trie_right[key] = value

    assert 9 == get_calibration_value(trie_right, "two1nine", "<")
    assert 3 == get_calibration_value(trie_right, "eightwothree", "<")
    assert 3 == get_calibration_value(trie_right, "abcone2threexyz", "<")
    assert 4 == get_calibration_value(trie_right, "xtwone3four", "<")
    assert 2 == get_calibration_value(trie_right, "4nineeightseven2", "<")
    assert 4 == get_calibration_value(trie_right, "zoneight234", "<")
    assert 6 == get_calibration_value(trie_right, "pqrstsixteen", "<")
