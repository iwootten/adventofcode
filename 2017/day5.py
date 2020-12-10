from __future__ import print_function


def get_jump_list():
    jump_elements = []

    with open('day5/input.txt', 'r') as content_file:
        for row in content_file.readlines():
            jump_elements.append(int(row))

    return jump_elements


def print_jump_list(input_list, offset):
    for index, item in enumerate(input_list):
        if index == offset:
            print("({})\t".format(item), end='')
        else:
            print("{}\t".format(item), end='')


def first():
    jump_list = get_jump_list()

    i = 1
    index = 0
    offset = jump_list[0]
    last_index = jump_list[0]

    print_jump_list(jump_list, offset)
    print("\n")

    while index < len(jump_list):
        offset = jump_list[index]
        index += offset

        jump_list[last_index] += 1

        # print_jump_list(jump_list, index)

        print("Jump: {} Index: {}".format(i, index))

        i += 1
        last_index = index


def second():
    jump_list = get_jump_list()

    i = 1
    index = 0
    offset = jump_list[0]
    last_index = jump_list[0]

    print_jump_list(jump_list, offset)
    print("\n")

    while index < len(jump_list):
        offset = jump_list[index]
        index += offset

        jump_list[last_index] += -1 if offset >= 3 else 1

        # print_jump_list(jump_list, index)

        print("Jump: {} Index: {}".format(i, index))

        i += 1
        last_index = index

first()
