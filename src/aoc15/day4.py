"--- Day 4: The Ideal Stocking Stuffer ---"

import hashlib


def find_decimal(data, starts_with):
    key = data[0].strip()
    i = 1

    while True:
        string_to_bytes = (key + str(i)).encode()
        md5 = hashlib.md5(string_to_bytes)
        hexadecimal = md5.hexdigest()

        if hexadecimal.startswith(starts_with):
            return i

        i += 1


def part1(data):
    return find_decimal(data, "0" * 5)


def part2(data):
    return find_decimal(data, "0" * 6)
