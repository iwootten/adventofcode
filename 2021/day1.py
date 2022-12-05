def get_data(filename):
    with open(filename) as input_file:
        return [int(a) for a in input_file.readlines()]


def get_part1_answer(data):
    count = 0
    for i in range(1, len(data)):
        prev_value = int(data[i - 1])
        value = int(data[i])
        if value > prev_value:
            count += 1
        increased = value > prev_value
        print(f"{value}: {increased}")
    return count


def get_part2_answer(data):
    count = 0
    for i in range(1, len(data) - 2):
        this_window = data[i - 1 : i + 2]
        next_window = data[i : i + 3]

        print(this_window)
        print(next_window)
        count += sum(next_window) > sum(this_window)
    return count


if __name__ == "__main__":
    input_data = get_data("./data/day1_input1.txt")
    print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")
