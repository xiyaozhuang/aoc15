"--- Day 1: Not Quite Lisp ---"


def part1(data):
    string = data[0]
    floor = 0

    for character in string:
        if character == "(":
            floor += 1

        elif character == ")":
            floor -= 1

    return floor


def part2(data):
    string = data[0]
    floor = 0

    for i in range(len(string)):
        if string[i] == "(":
            floor += 1

        else:
            floor -= 1

        if floor == -1:
            return i + 1
