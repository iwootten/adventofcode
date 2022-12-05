from __future__ import print_function
from datetime import datetime


def print_buffer(buffer, current_index):
    for index, b in enumerate(buffer):
        if current_index == index:
            print("({})\t".format(b), end="")
        else:
            print("{}\t".format(b), end="")
    print()


def find_spin_lock(step_size=3, no_of_steps=3):
    buffer = [0]
    current_position = 0

    for current_val in range(1, no_of_steps + 1):
        start = datetime.now()
        current_position = (current_position + step_size) % len(buffer) + 1
        buffer.insert(current_position, current_val)


        # print("Current Position: {}".format(current_position))
        # print("Current Val: {}".format(current_val))

        # print_buffer(buffer, current_position)
        if current_val % 100000 == 0:
            duration = datetime.now() - start
            print(". - {}".format(duration.total_seconds()))
            start = datetime.now()

    print(buffer[current_position - 3: current_position + 3])


def reduced_spin_lock(step_size=3, no_of_steps=3):
    current_position = 0
    after_zero = 0

    for current_val in range(1, no_of_steps + 1):
        current_position = (current_position + step_size) % current_val + 1

        if current_position == 1:
            after_zero = current_val

    print(after_zero)


def part1():
    find_spin_lock(382)


def part2():
    reduced_spin_lock(382, 50000000)

part2()
