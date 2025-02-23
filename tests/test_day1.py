from aoc15 import day1

with open("data/tests/day1.txt") as file:
    data = file.readlines()


def test_part1():
    assert day1.part1(data) == -1


def test_part2():
    assert day1.part2(data) == 1
