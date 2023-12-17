# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_03.part_2 import find_gear_ratios


def test_find_gear_ratios_no_found():
    assert [] == find_gear_ratios([".....", "..*..", "....."])
    assert [] == find_gear_ratios(["1....", "..*..", "....1"])
    assert [] == find_gear_ratios(["..1..", "..*..", "....."])


def test_find_gear_ratios_single_digit_found():
    assert [3 * 7] == find_gear_ratios(["3..", ".*.", "7.."])
    assert [3 * 7] == find_gear_ratios(["3..", ".*.", ".7."])
    assert [3 * 7] == find_gear_ratios(["3..", ".*.", "..7"])

    assert [3 * 7] == find_gear_ratios([".3.", ".*.", "7.."])
    assert [3 * 7] == find_gear_ratios([".3.", ".*.", ".7."])
    assert [3 * 7] == find_gear_ratios([".3.", ".*.", "..7"])

    assert [3 * 7] == find_gear_ratios(["..3", ".*.", "7.."])
    assert [3 * 7] == find_gear_ratios(["..3", ".*.", ".7."])
    assert [3 * 7] == find_gear_ratios(["..3", ".*.", "..7"])


def test_find_gear_ratios_double_digit_found():
    assert [11 * 13] == find_gear_ratios(["11...", "..*..", "13..."])
    assert [11 * 13] == find_gear_ratios(["11...", "..*..", ".13.."])
    assert [11 * 13] == find_gear_ratios(["11...", "..*..", "..13."])
    assert [11 * 13] == find_gear_ratios(["11...", "..*..", "...13"])

    assert [11 * 13] == find_gear_ratios([".11..", "..*..", "13..."])
    assert [11 * 13] == find_gear_ratios([".11..", "..*..", ".13.."])
    assert [11 * 13] == find_gear_ratios([".11..", "..*..", "..13."])
    assert [11 * 13] == find_gear_ratios([".11..", "..*..", "...13"])

    assert [11 * 13] == find_gear_ratios(["..11.", "..*..", "13..."])
    assert [11 * 13] == find_gear_ratios(["..11.", "..*..", ".13.."])
    assert [11 * 13] == find_gear_ratios(["..11.", "..*..", "..13."])
    assert [11 * 13] == find_gear_ratios(["..11.", "..*..", "...13"])

    assert [11 * 13] == find_gear_ratios(["...11", "..*..", "13..."])
    assert [11 * 13] == find_gear_ratios(["...11", "..*..", ".13.."])
    assert [11 * 13] == find_gear_ratios(["...11", "..*..", "..13."])
    assert [11 * 13] == find_gear_ratios(["...11", "..*..", "...13"])


def test_find_gear_ratios_several_numbers_found():
    assert [2 * 7, 9 * 11] == find_gear_ratios(
        [
            ".3....2..9.",
            "..*...?..*.",
            ".1.13..7.11",
        ]
    )
