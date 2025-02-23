import re

import aoc15
from aoc15 import *


def list_attributes(obj: object, pattern: str) -> list:
    """
    Lists the attributes of an object that match the given pattern.
    """

    attributes = []

    for attribute in dir(obj):
        if re.match(pattern, attribute):
            attributes.append(getattr(obj, attribute))

    return attributes


def get_solvers(pattern: str) -> dict:
    """
    Gets the functions which solve the problems for each day.
    """

    solvers = {}

    for module in list_attributes(aoc15, pattern):
        name = module.__name__.split(".")[1]
        solvers[name] = list_attributes(module, r"part\d")

    return solvers


def read_data(path: str) -> list:
    """
    Reads a text file from a path as a list of lines.
    """

    with open(path) as file:
        return file.readlines()


def solve(
    directory_path: str, pattern: str = r"day", print_summary: bool = False
) -> dict:
    """
    Solves the parts for each day by using all the files in the directory path as input.
    """

    if not directory_path.endswith("/"):
        directory_path += "/"

    solvers = get_solvers(pattern)
    solutions = {}

    for day, parts in solvers.items():
        path = directory_path + day + ".txt"
        data = read_data(path)

        solutions[day] = {"part1": parts[0](data), "part2": parts[1](data)}

    if print_summary:
        for key, value in solutions.items():
            print(key, value)

    return solutions
