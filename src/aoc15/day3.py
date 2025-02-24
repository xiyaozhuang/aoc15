"--- Day 3: Perfectly Spherical Houses in a Vacuum ---"


class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.history = {(0, 0)}

    def deliver(self, direction):
        if direction == ">":
            self.x += 1

        elif direction == "^":
            self.y += 1

        elif direction == "<":
            self.x -= 1

        elif direction == "v":
            self.y -= 1

        self.history.add((self.x, self.y))


def part1(data):
    directions = data[0]
    santa = Santa()

    for direction in directions:
        santa.deliver(direction)

    deliveries = len(santa.history)

    return deliveries


def part2(data):
    directions = data[0]
    santa = Santa()
    robot = Santa()

    for i in range(len(directions)):
        if i % 2 == 0:
            santa.deliver(directions[i])

        else:
            robot.deliver(directions[i])

    history = santa.history.union(robot.history)
    deliveries = len(history)

    return deliveries
