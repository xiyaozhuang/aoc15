import aoc15
from aoc15 import day1, utils


def test_list_attributes():
    output = utils.list_attributes(aoc15, "utils")
    expected = [utils]

    assert output == expected


def test_get_solvers():
    output = utils.get_solvers(r"^day1$")
    expected = {"day1": [day1.part1, day1.part2]}

    assert output == expected


def test_read_data():
    output = utils.read_data("data/tests/test.txt")
    expected = ["test\n"]

    assert output == expected


def test_solve():
    output = utils.solve("data/tests", r"day1")
    expected = {"day1": {"part1": -1, "part2": 1}}

    assert output == expected
