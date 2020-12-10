from __future__ import print_function
import math

# Determine when collisions occur for packets and the firewall


def construct_firewall():
    layer_list = []

    with open('day13/input.txt', 'r') as content_file:
        for row in content_file.readlines():
            layer, depth = row.split(":")

            layer = int(layer.strip())
            depth = int(depth.strip())

            layer_list.append((layer, depth))

        last_layer = layer_list[-1][0]

    content = [[]] * (last_layer + 1)

    for layer, depth in layer_list:
        content[layer] = [None] * depth

    return content


def scanner_position(depth, step):
    index = step % (depth - 1)
    direction = 1 if int(math.floor(step / (depth - 1))) % 2 == 0 or step == 0 else -1

    return index if direction == 1 else depth - index - 1, direction


def print_firewall(firewall, step=0, packet_pos=None):
    max_depth = 0

    for i, layer in enumerate(firewall):
        print("{}\t".format(i), end="")
        max_depth = len(layer) if len(layer) > max_depth else max_depth
    print()

    for current_depth in range(max_depth):
        for i, layer in enumerate(firewall):
            if packet_pos == i and current_depth == 0:
                print("(", end="")

            if len(layer) > current_depth:
                current_scanner_pos, _ = scanner_position(len(layer), step)
                character = "S" if current_scanner_pos == current_depth else " "
                print("{}\t".format("[{}]".format(character) if layer[current_depth] is None else ""), end="")
            else:
                print("...\t", end="")

            if packet_pos == i and current_depth == 0:
                print(")", end="")
        print()


def take_trip(firewall, delay=0):
    current_packet_pos = 0
    i = 0
    collisions = []

    while current_packet_pos < len(firewall) - 1:
        step = i + delay
        # print("\n\nPicosecond: {}".format(step))
        # print("Packet Position: {}".format(current_packet_pos))
        # print("delay: {}".format(delay))
        # print("i: {}".format(i))
        current_scanner_pos = None

        if len(firewall[current_packet_pos]):
            if current_scanner_pos != 0 and current_packet_pos != i:
                current_packet_pos += 1
        else:
            current_packet_pos += 1

        if len(firewall[current_packet_pos]):
            current_scanner_pos, _ = scanner_position(len(firewall[current_packet_pos]), step)

        if current_scanner_pos == 0:
            collisions.append((current_packet_pos, len(firewall[i])))

        # print("New Packet Position: {}\n".format(current_packet_pos))

        # print_firewall(firewall, step=step, packet_pos=current_packet_pos)
        i += 1
    return collisions


def part1():
    firewall = construct_firewall()
    collisions = take_trip(firewall)
    print("Collisions found at {}".format(collisions))
    print("Trip severity: {}".format(sum([collision[0] * collision[1] for collision in collisions])))


def part2():
    firewall = construct_firewall()
    delay = 0
    collisions = take_trip(firewall, delay)

    while len(collisions) > 0:
        delay += 1
        collisions = take_trip(firewall, delay)

        # print("Collisions found at {}".format(collisions))
        # print("Trip severity: {}".format(sum([collision[0] * collision[1] for collision in collisions])))

    print("\nDelay Ended at: {}".format(delay))


part2()

