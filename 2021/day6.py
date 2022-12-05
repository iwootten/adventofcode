def get_data(filename):
    with open(filename) as input_file:
        return [int(a) for a in input_file.readline().split(",")]


def get_part1_answer(input_data, duration_in_days):
    fish_stack = input_data[:]
    for day_number in range(duration_in_days):
        print(day_number)
        for i in range(0, len(fish_stack)):
            if fish_stack[i] != 0:
                fish_stack[i] -= 1
            else:
                fish_stack[i] = 6
                fish_stack.append(8)
    return fish_stack


def print_fish_map(fish_map):
    for i in range(0, 9):
        if fish_map[i]:
            print(",".join([str(i) for j in range(0, fish_map[i])]), end=",")
    print("")


def get_part2_answer(input_data, duration_in_days):
    fish_map = {i: 0 for i in range(0, 9)}

    for item in input_data:
        fish_map[item] += 1

    for day_number in range(duration_in_days):
        new_fish = fish_map[0]
        for i in range(0, 8):
            fish_map[i] = fish_map[i + 1]
        fish_map[6] += new_fish
        fish_map[8] = new_fish
        print(day_number + 1)

    total = 0

    for i in range(0, 9):
        total += fish_map[i]

    return total


if __name__ == "__main__":
    initial_data = get_data("./data/day6_input1.txt")

    final = get_part2_answer(initial_data, 256)

    print(final)
