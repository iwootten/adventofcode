from day3 import get_data, get_part1_answer, get_part2_answer


def test_day2_part1():
    data = get_data("./data/day3_example.txt")
    answer = get_part1_answer(data)
    assert answer == 4361


def test_day2_part2():
    data = get_data("./data/day3_example.txt")
    answer = get_part2_answer(data)

    assert answer == 467835