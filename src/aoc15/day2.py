"--- Day 2: I Was Told There Would Be No Math ---"


def part1(data):
    paper = 0

    for string in data:
        length, width, height = (int(character) for character in string.split("x"))
        areas = (length * width, width * height, height * length)

        surface_area = 2 * sum(areas)
        slack = min(areas)

        paper += surface_area + slack

    return paper


def part2(data):
    ribbon = 0

    for string in data:
        length, width, height = (int(character) for character in string.split("x"))
        perimeters = (length + width, width + height, height + length)

        perimeter = 2 * min(perimeters)
        bow = length * width * height

        ribbon += perimeter + bow

    return ribbon
