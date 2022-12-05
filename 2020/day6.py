def get_data(filename):
    with open(filename) as input_file:
        return input_file.read().split("\n\n")


def get_part1_answer(data):
    return sum([len(set(group.replace("\n", ""))) for group in data])


def line_count(group):
    questions = set(group.replace("\n", ""))

    return sum(
        [
            all(question in group for group in group.splitlines())
            for question in questions
        ]
    )


def get_part2_answer(data):
    count = 0
    for group in data:
        count += line_count(group)
    return count


if __name__ == "__main__":
    input_data = get_data("./data/day6_input1.txt")

    print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")
