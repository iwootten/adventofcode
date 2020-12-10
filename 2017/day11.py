import math

directions = {
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0),
    "n": (0, 1, -1),
}


def get_data():
    with open('day11/input.txt', 'r') as content_file:
        content = content_file.read()

    return content


def magnitude(x, y, z):
    return (abs(0 - x) + abs(0 - y) + abs(0 - z)) / 2


def process_route(route_moves):
    x, y, z, max_mag = 0, 0, 0, 0

    for move in route_moves:
        move_x, move_y, move_z = directions[move]

        x += move_x
        y += move_y
        z += move_z

        mag = magnitude(x, y, z)
        if mag > max_mag:
            max_mag = mag

    return x, y, z, max_mag


def test():
    moves = "ne,ne,ne".split(",")

    x, y, z, _ = process_route(moves)
    mag = magnitude(x, y, z)

    print "Final Position {},{},{}".format(x, y, z)
    print "Magnitude: {}".format(mag)

    assert mag == 3

    moves = "ne,ne,sw,sw".split(",")

    x, y, z, _ = process_route(moves)
    mag = magnitude(x, y, z)

    print "Final Position {},{},{}".format(x, y, z)
    print "Magnitude: {}".format(mag)

    assert mag == 0

    moves = "ne,ne,s,s".split(",")

    x, y, z, _ = process_route(moves)
    mag = magnitude(x, y, z)

    print "Final Position {},{},{}".format(x, y, z)
    print "Magnitude: {}".format(mag)

    assert mag == 2

    moves = "se,sw,se,sw,sw".split(",")

    x, y, z, _ = process_route(moves)
    mag = magnitude(x, y, z)

    print "Final Position {},{},{}".format(x, y, z)
    print "Magnitude: {}".format(mag)

    assert mag == 3


def part1():
    moves = get_data().split(",")

    x, y, z, max_mag = process_route(moves)
    mag = magnitude(x, y, z)

    print "Final Position {},{},{}".format(x, y, z)
    print "Magnitude: {}".format(mag)
    print "Max Ever Magnitude: {}".format(max_mag)


part1()

