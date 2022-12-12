from collections import namedtuple


def get_data(filename):
    with open(filename) as input_file:
        return [
            (l.strip().split()[0], int(l.strip().split()[1]))
            for l in input_file.readlines()
        ]


class Point:
    x = 0
    y = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.x, self.y}"

    def __eq__(self, a: object) -> bool:
        return a.x == self.x and a.y == self.y

    def should_move_straight(self, a):
        return ((a.x == self.x) and (abs(self.y - a.y) == 2)) or (
            (a.y == self.y) and (abs(self.x - a.x) == 2)
        )

    def diff_x(self, a):
        return self.x - a.x

    def diff_y(self, a):
        return self.y - a.y

    def should_move_diagonally(self, a):
        return (
            not self.should_move_straight(a)
            and abs(self.diff_x(a)) > 1
            or abs(self.diff_y(a)) > 1
        )


directions = {
    "L": (-1, 0),
    "R": (1, 0),
    "D": (0, -1),
    "U": (0, 1),
}


def print_rope(head, knots, size, origin=(0, 0)):
    for y in range(origin[1] + size, origin[1] - 1, -1):
        for x in range(origin[0], origin[0] + size):
            if Point(x, y) == head:
                print("H", end="")
            elif Point(x, y) in knots:
                print(knots.index(Point(x, y)) + 1, end="")
            else:
                print(".", end="")
        print("")
    print()


def get_part1_answer(data):
    head, tail = Point(0, 0), Point(0, 0)
    tail_list = []
    for direction, times in data:
        for i in range(times):
            head.x += directions[direction][0]
            head.y += directions[direction][1]

            if tail.should_move_straight(head):
                tail.x += directions[direction][0]
                tail.y += directions[direction][1]
            if tail.should_move_diagonally(head):
                x_diff = -1 if tail.diff_x(head) > 0 else 1
                y_diff = -1 if tail.diff_y(head) > 0 else 1
                tail.x += x_diff
                tail.y += y_diff
            if (tail.x, tail.y) not in tail_list:
                tail_list.append((tail.x, tail.y))
    return len(tail_list)


def get_part2_answer(data):
    head = Point(0, 0)
    knots = [Point(0, 0) for _ in range(9)]

    tail_list = []
    for direction, times in data:
        for i in range(times):
            head.x += directions[direction][0]
            head.y += directions[direction][1]

            last_knot = head

            for j, knot in enumerate(knots):
                if knot.should_move_straight(last_knot):
                    # Should be direction between knots, not head
                    if knot.x == last_knot.x:
                        knot.y += -1 if knot.diff_y(last_knot) > 0 else 1
                    elif knot.y == last_knot.y:
                        knot.x += -1 if knot.diff_x(last_knot) > 0 else 1
                elif knot.should_move_diagonally(last_knot):
                    x_diff = -1 if knot.diff_x(last_knot) > 0 else 1
                    y_diff = -1 if knot.diff_y(last_knot) > 0 else 1
                    knot.x += x_diff
                    knot.y += y_diff

                if j == len(knots) - 1 and (knot.x, knot.y) not in tail_list:
                    tail_list.append((knot.x, knot.y))
                last_knot = knot

    return len(tail_list)


if __name__ == "__main__":
    data = get_data("./data/day9_input.txt")
    print(f"Part 1: {get_part1_answer(data)}")
    print(f"Part 2: {get_part2_answer(data)}")
