def get_data(filename):
    with open(filename) as input_file:
        return input_file.readlines()


def get_part1_answer(data):
    return next(
        iter(
            [
                int(number) * int(other_number)
                for number in data
                for other_number in data
                if int(number) + int(other_number) == 2020
            ]
        )
    )


def get_part2_answer(data):
    return next(
        iter(
            [
                int(number) * int(other_number) * int(another_number)
                for number in data
                for other_number in data
                for another_number in data
                if int(number) + int(other_number) + int(another_number) == 2020
            ]
        )
    )


if __name__ == "__main__":
    input_data = get_data("./data/day1_input1.txt")
    print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")
