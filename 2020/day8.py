def get_data(filename):
    with open(filename) as input_file:
        return input_file.read().splitlines()


def get_accumulator_total(data):
    index, accumulator = 0, 0
    visited_instructions = []

    while index not in visited_instructions and index < len(data):
        visited_instructions.append(index)

        instruction, offset = data[index].split(" ")
        offset = int(offset)

        if instruction == "acc":
            accumulator += offset

        index += offset if instruction == "jmp" else 1
    return accumulator, index >= len(data)


def replace_instructions(data):
    index = 0

    while index < len(data):
        test_data = data.copy()
        if "jmp" in data[index]:
            test_data[index] = test_data[index].replace("jmp", "nop")
        elif "nop" in data[index]:
            test_data[index] = test_data[index].replace("nop", "jmp")

        accumulator, found = get_accumulator_total(test_data)

        if found:
            return accumulator

        index += 1


if __name__ == "__main__":
    input_data = get_data("./data/day8_input1.txt")

    print(f"Part1: {get_accumulator_total(input_data)[0]}")
    print(f"Part2: {replace_instructions(input_data)}")
