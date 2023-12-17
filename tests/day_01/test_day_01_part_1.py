# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_01.part_1 import get_calibration_value


def test_get_calibration_value():
    assert 12 == get_calibration_value("12")
    assert 12 == get_calibration_value("1a2")
    assert 12 == get_calibration_value("a1b2c")
