from aoc15 import day3

with open("data/tests/day3.txt") as file:
    data = file.readlines()


def test_part1():
    assert day3.part1(data) == 2


def test_part2():
    assert day3.part2(data) == 3
