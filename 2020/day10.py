def get_data(filename):
    with open(filename) as input_file:
        data = [int(line) for line in input_file.read().splitlines()]

        data.append(0)
        data.append(max(data) + 3)
        data.sort()

        return data


def find_differences(sorted_data):
    joltage, ones, threes = 0, 0, 0

    for item in sorted_data:
        diff = item - joltage
        ones += diff == 1
        threes += diff == 3

        joltage = item
    return ones, threes


def search_data(sorted_data):
    paths = [0] * (max(sorted_data) + 1)
    paths[0] = 1

    for index in range(1, max(sorted_data) + 1):
        for diff in range(1, 4):
            if index - diff in sorted_data:
                paths[index] += paths[index - diff]

    return paths[-1]


if __name__ == "__main__":
    input_data = get_data("./data/day10_input1.txt")
    ones, threes = find_differences(input_data)

    print(f"Part1: {ones * threes}")
    print(f"Part2: {search_data(input_data)}")
