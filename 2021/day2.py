def get_data(filename):
    with open(filename) as input_file:
        return [a.strip().split() for a in input_file.readlines()]


def get_part1_answer(data):
    x, y = 0, 0

    for command, value in data:
        value = int(value)
        if command == "forward":
            x += value
        if command == "down":
            y += value
        if command == "up":
            y -= value
    return x, y


def get_part2_answer(data):
    horizontal, depth, aim = 0, 0, 0

    for command, value in data:
        value = int(value)
        if command == "forward":
            horizontal += value
            depth += aim * value
        if command == "down":
            aim += value
        if command == "up":
            aim -= value
    return horizontal, depth


if __name__ == "__main__":
    input_data = get_data("./data/day2_input1.txt")
    print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")
