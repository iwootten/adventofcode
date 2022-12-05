def get_data(filename):
    with open(filename) as input_file:
        return input_file.readlines()


def get_part1_answer(data):
    valid = 0

    for policy in data:
        rule, string = policy.split(":")
        frequency, letter = rule.split(" ")
        min, max = frequency.split("-")

        count = string.count(letter)
        if int(min) <= count <= int(max):
            valid += 1
    return valid


def get_part2_answer(data):
    valid = 0

    for policy in data:
        rule, string = policy.split(":")
        positions, letter = rule.split(" ")
        position_a, position_b = positions.split("-")

        string = string.rstrip("\n").lstrip(" ")

        if (string[int(position_a) - 1] == letter) ^ (
            string[int(position_b) - 1] == letter
        ):
            valid += 1
    return valid


if __name__ == "__main__":
    input_data = get_data("./data/day2_input1.txt")
    print(f"Part1: {get_part2_answer(input_data)}")
