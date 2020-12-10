def get_data(filename):
    with open('day16/{}'.format(filename), 'r') as content_file:
        commands = content_file.read().split(",")

    return commands


def spin(l, n):
    return l[-n:] + l[:-n]


def exchange(l, a, b):
    l = list(l)
    program_a = l[a]
    program_b = l[b]

    l[b] = program_a
    l[a] = program_b

    return "".join(l)


def partner(l, a, b):
    pos_a = l.index(a)
    pos_b = l.index(b)

    return exchange(l, pos_a, pos_b)


def process_actions(input_string, commands):
    for command in commands:
        action = command[0]

        args = command[1:].split("/")

        # print "Processing: {} - args: {}".format(command, args)

        if action == 's':
            input_string = spin(input_string, int(args[0]))
        elif action == 'x':
            input_string = exchange(input_string, int(args[0]), int(args[1]))
        elif action == 'p':
            input_string = partner(input_string, args[0], args[1])

        # print "New string: {}".format(input_string)

    return input_string

def get_position_map(string_a, string_b):
    a = list(string_a)
    b = list(string_b)
    pos_map = [None] * len(a)

    for index, c in enumerate(a):
        pos_map[b.index(c)] = index

    return pos_map

def calculate_duplication(original_order, commands):
    """
    Determine the number of iterations necessary to create the original input
    """
    program_order = str(original_order)
    count = 0
    position_map = []

    while position_map != range(len(original_order)):
        program_order = process_actions(program_order, commands)
        position_map = get_position_map(original_order, program_order)
        count += 1

    return count

def example1():
    program_order = "abcde"
    commands = get_data("train.txt")
    print process_actions(program_order, commands)

def example2():
    program_order = "abcde"
    commands = get_data("train.txt")

    count = calculate_duplication(program_order, commands)

    print count


def part1():
    start = "abcdefghijklmnop"

    commands = get_data("input.txt")

    print process_actions(start, commands)


def part2():
    program_order = "abcdefghijklmnop"
    commands = get_data("input.txt")

    count = calculate_duplication(program_order, commands)

    number_of_iterations = 1000000000

    for i in range(number_of_iterations % count):
        program_order = process_actions(program_order, commands)

    print program_order

part2()
