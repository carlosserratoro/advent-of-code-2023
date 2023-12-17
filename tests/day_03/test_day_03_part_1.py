# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_03.part_1 import find_part_numbers


def test_find_part_numbers_no_found():
    assert [] == find_part_numbers(["...", ".1.", "..."])


def test_find_part_numbers_single_digit_found():
    assert [1] == find_part_numbers(["*..", ".1.", "..."])
    assert [1] == find_part_numbers([".*.", ".1.", "..."])
    assert [1] == find_part_numbers(["..*", ".1.", "..."])
    assert [1] == find_part_numbers(["...", ".1.", "*.."])
    assert [1] == find_part_numbers(["...", ".1.", ".*."])
    assert [1] == find_part_numbers(["...", ".1.", "..*"])
    assert [1] == find_part_numbers(["...", "*1.", "..*"])
    assert [1] == find_part_numbers(["...", ".1*", "..."])


def test_find_part_numbers_double_digit_found():
    assert [12] == find_part_numbers(["*...", ".12.", "...."])
    assert [12] == find_part_numbers([".*..", ".12.", "...."])
    assert [12] == find_part_numbers(["..*.", ".12.", "...."])
    assert [12] == find_part_numbers(["...*", ".12.", "...."])
    assert [12] == find_part_numbers(["....", ".12.", "*..."])
    assert [12] == find_part_numbers(["....", ".12.", ".*.."])
    assert [12] == find_part_numbers(["....", ".12.", "..*."])
    assert [12] == find_part_numbers(["....", ".12.", "...*"])
    assert [12] == find_part_numbers(["....", "*12.", "...."])
    assert [12] == find_part_numbers(["....", ".12*", "...."])


def test_find_part_numbers_several_numbers_found():
    assert [1, 23, 4] == find_part_numbers(
        [
            ".....*...",
            "?1.23..4.",
            ".......?.",
        ]
    )
