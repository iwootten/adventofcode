from __future__ import print_function

import math
import sys


direction_map = {
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0)
}


def move(current_x, current_y):
    x_up, y_up = current_direction

    return current_x + x_up, current_y + y_up


def should_turn(pos, direction, limit):
    x, y = pos
    direction_x, direction_y = direction
    return math.fabs(x + direction_x) > limit or math.fabs(y + direction_y) > limit


def grid_size(value):
    grid_size = int(math.ceil(math.sqrt(value)))

    return grid_size + 1 if grid_size % 2 == 0 else grid_size


def neighbours(pos):
    current_x, current_y = pos
    neighbours = []
    border = int(round(math.ceil(n / 2)))

    for x in range(current_x - 1, current_x + 2):
        for y in range(current_y - 1, current_y + 2):
            if pos != (x, y) and abs(x) <= border and abs(y) <= border:
                neighbours.append((x, y))

    return neighbours


if __name__ == "__main__":
    position = 0, 0
    current_direction = 1, 0
    target = int(sys.argv[1])

    gs = grid_size(target)
    border = int(round(math.ceil(gs / 2)))

    grid = [[0] * gs for i in range(-border, border + 1)]
    grid[0][0] = 1

    for i in range(2, target + 1):
        n = grid_size(i)
        border = int(round(math.ceil(n / 2)))

        if i > 1:
            if should_turn(position, current_direction, border):
                current_direction = direction_map[current_direction]

            new_x = position[0] + current_direction[0]
            new_y = position[1] + current_direction[1]

            position = new_x, new_y
            total = sum(grid[p[0]][p[1]] for p in neighbours(position))
            grid[position[0]][position[1]] = total

        if i == target:
            # import pdb; pdb.set_trace()
            print("Value: {}".format(i))
            print("\tGrid size: {}".format(n))
            print("\tBorder: {}".format(border))
            print("\tDirection: {}".format(current_direction))
            print("\tPos: {}".format(position))
            print("\tDistance: {}".format(abs(position[0]) + abs(position[1])))

    print("\n")

    for y in range(-border, border + 1)[::-1]:
        for x in range(-border, border + 1):
            print("{}\t".format(grid[x][y]), end='')
        print("\n")
