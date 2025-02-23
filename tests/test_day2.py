from aoc15 import day2

with open("data/tests/day2.txt") as file:
    data = file.readlines()


def test_part1():
    assert day2.part1(data) == 58 + 43


def test_part2():
    assert day2.part2(data) == 34 + 14
