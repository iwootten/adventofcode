def get_data(filename):
    with open(filename) as input_file:
        return [int(line) for line in input_file.read().splitlines()]


def find_rule_breaker(data, preamble_length):
    for index in range(preamble_length, len(data)):
        preamble = data[index - 25 : index]
        valid = [
            preamble[x] + preamble[y]
            for y in range(0, len(preamble))
            for x in range(0, len(preamble))
            if x != y
        ]

        if data[index] not in valid:
            return data[index]


def find_weakness(data, sum_total):
    for index in range(0, len(data)):
        current_length = 0
        current_sum = 0
        while current_sum < sum_total and index + current_length < len(data):
            current_set = data[index : index + current_length]
            if sum(current_set) == sum_total:
                return min(current_set) + max(current_set)
            current_length += 1


if __name__ == "__main__":
    input_data = get_data("./data/day9_input1.txt")
    rule_breaker = find_rule_breaker(input_data, 25)

    print(f"Part1: {rule_breaker}")
    print(f"Part2: {find_weakness(input_data, rule_breaker)}")
