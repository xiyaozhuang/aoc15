from aoc15 import day4

with open("data/tests/day4.txt") as file:
    data = file.readlines()


def test_part1():
    assert day4.part1(data) == 609043


def test_part2():
    assert day4.part2(data) == 6742839
