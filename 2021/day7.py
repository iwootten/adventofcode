def get_data(filename):
    with open(filename) as input_file:
        return [int(a) for a in input_file.readline().split(",")]


def get_part1_answer(input_data):
    crab_map = {i: 0 for i in range(0, max(input_data))}

    for p in crab_map.keys():
        for item in input_data:
            crab_map[p] += abs(item - p)

    min_index = min(crab_map, key=crab_map.get)

    return min_index, crab_map[min_index]


def get_part2_answer(input_data):
    crab_map = {i: 0 for i in range(0, max(input_data))}

    for p in crab_map.keys():
        for item in input_data:
            crab_map[p] += sum([i for i in range(1, abs(item - p) + 1)])

    min_index = min(crab_map, key=crab_map.get)

    return min_index, crab_map[min_index]


if __name__ == "__main__":
    input_data = get_data("./data/day7_input1.txt")

    # part1_fuel = get_part1_answer(input_data)
    part2_fuel = get_part2_answer(input_data)

    # print(part1_fuel)
    print(part2_fuel)
