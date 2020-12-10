from __future__ import print_function


def process_length(elements, length, position):
    offset_list = elements[position:] + elements[:position]
    sub_list = offset_list[:length]
    reverse_sub_list = sub_list[::-1]

    replaced = reverse_sub_list + offset_list[length:]
    # import pdb; pdb.set_trace()
    return replaced[len(elements) - position:] + replaced[:len(elements) - position]


def print_list(elements, position, length):
    offset_position = circular_index(position, len(elements))
    offset_end = circular_index(position + length - 1, len(elements))

    for index, element in enumerate(elements):
        if offset_position == index:
            print("(", end='')
        if offset_position == index:
            print("[", end='')
        print("{}".format(element), end='')
        if offset_position == index:
            print("]", end='')
        if offset_end == index:
            print(")", end='')
    print("\t\tP: {}, L: {}".format(offset_position, length))


def circular_index(index, limit):
    return index % limit


def twist_hash(elements, lengths, current_position=0, skip_size=0):
    for length in lengths:
        # print("Before: ")
        # print_list(elements, current_position, length)
        elements = process_length(elements, length, current_position)
        # print("After:")
        # print_list(elements, current_position, length)
        # print("Skip: {}".format(skip_size))
        # print("Length + Skip: {}".format(length + skip_size))
        current_position = circular_index(current_position + length + skip_size, len(elements))
        skip_size += 1
    return elements, skip_size, current_position


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def sparse_hash(start_elements, start_lengths):
    suffix_lengths = [17, 31, 73, 47, 23]

    # # Round One
    # output_elements, round_one_skip, round_one_position = twist_hash(start_elements, start_lengths)

    input_lengths = start_lengths + suffix_lengths
    elements = start_elements

    # print([ord(val) for val in input_elements] + append_string)

    skip = 0
    position = 0

    # Round 2 - 64
    for i in range(1, 65):
        elements, skip, position = twist_hash(elements, input_lengths, current_position=position, skip_size=skip)

    return elements


def dense_hash(l):
    chunked = chunks(l, 16)
    hash = []

    for chunk in chunked:
        val = None
        for n in chunk:
            if val is None:
                val = n
            else:
                val ^= n
        hash.append(val)
    return hash


def knot_hash(input_string):
    input_elements = range(0, 256)
    input_lengths = [ord(c) for c in input_string]

    sparse = sparse_hash(input_elements, input_lengths)
    dense = dense_hash(sparse)
    final_hash = "".join([format(c, '02x') for c in dense])

    return final_hash


def part1():
    input_elements2 = range(0, 256)
    input_lengths2 = [165, 1, 255, 31, 87, 52, 24, 113, 0, 91, 148, 254, 158, 2, 73, 153]
    #
    input_elements = [0, 1, 2, 3, 4]
    input_lengths = [3, 4, 1, 5]

    output_elements, final_skip, final_position = twist_hash(input_elements2, input_lengths2)

    print(output_elements)
    print("Final skip: {}".format(final_skip))
    print("Current position: {}".format(final_position))


def tests():
    assert knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert knot_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert knot_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert knot_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

def part2():
    print(knot_hash("165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153"))
