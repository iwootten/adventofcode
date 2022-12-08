def get_data(filename):
    with open(filename) as input_file:
        return [a.strip("\n") for a in input_file.readlines()]


def get_part1_answer(data):
    header = []
    line_break = None

    for index, line in enumerate(data):
        if line == "":
            line_break = index
            break

    header, instructions = data[: line_break - 1], data[line_break + 1 :]

    no_of_stacks = int(data[line_break - 1].strip()[-1])

    stacks = []

    for index in range(no_of_stacks):
        line_index = index * 3 + (index + 1)
        stack = []
        for line in header:
            if line[line_index].strip():
                stack.append(line[line_index])
        stack.reverse()
        stacks.append(stack)

    for instruction in instructions:
        amount, move = instruction.strip("move ").split("from")
        from_move, to_move = move.split("to")
        for i in range(int(amount)):
            letter_to_move = stacks[int(from_move) - 1].pop()
            stacks[int(to_move) - 1].append(letter_to_move)

    code = ""
    for stack in stacks:
        code += stack[-1]
    return code


def get_part2_answer(data):
    header = []
    line_break = None

    for index, line in enumerate(data):
        if line == "":
            line_break = index
            break

    header, instructions = data[: line_break - 1], data[line_break + 1 :]

    no_of_stacks = int(data[line_break - 1].strip()[-1])

    stacks = []

    for index in range(no_of_stacks):
        line_index = index * 3 + (index + 1)
        stack = []
        for line in header:
            if line[line_index].strip():
                stack.append(line[line_index])
        stack.reverse()
        stacks.append(stack)

    for instruction in instructions:
        amount, move = instruction.strip("move ").split("from")
        from_move, to_move = move.split("to")
        from_move, to_move, amount = int(from_move) - 1, int(to_move) - 1, int(amount)
        items_to_move = stacks[from_move][-amount:]

        stacks[from_move] = stacks[from_move][:-amount]
        stacks[to_move] = stacks[to_move] + items_to_move

    code = ""
    for stack in stacks:
        code += stack[-1]
    return code


if __name__ == "__main__":
    data = get_data("./data/day5_input.txt")
    # print(data)
    print(f"Part 1: {get_part1_answer(data)}")
    print(f"Part 2: {get_part2_answer(data)}")
