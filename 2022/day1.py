def get_data(filename):
    with open(filename) as input_file:
        return [int(a) if a != "\n" else 0 for a in input_file.readlines()]


def get_part1_answer(data):
    heaviest = 0
    total = 0

    for index, amount in enumerate(data):
        total += amount
        if amount == 0 or index == len(data) - 1:
            if total > heaviest:
                heaviest = total
            total = 0
    return heaviest


def get_part2_answer(data):
    heaviest = [0, 0, 0]
    total = 0

    for index, amount in enumerate(data):
        total += amount
        if amount == 0 or index == len(data) - 1:
            if total > heaviest[0]:
                heaviest = sorted(heaviest[1:] + [total])
            total = 0
    return sum(heaviest)


if __name__ == "__main__":
    input_data = data = get_data("./data/day1_input.txt")
    print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")
