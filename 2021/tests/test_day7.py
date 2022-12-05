from day7 import get_data, get_part1_answer, get_part2_answer


def test_day6_part1():
    initial_data = get_data("./data/day7_example1.txt")

    answer = get_part1_answer(initial_data)

    assert answer == (2, 37)


def test_day6_part2():
    initial_data = get_data("./data/day7_example1.txt")

    answer = get_part2_answer(initial_data)

    assert answer == (5, 168)
