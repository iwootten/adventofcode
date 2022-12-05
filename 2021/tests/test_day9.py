from day9 import get_data, get_part1_answer, get_part2_answer


def test_day9_part1():
    initial_data = get_data("./data/day9_example1.txt")

    answer = get_part1_answer(initial_data)

    assert answer == [2, 1, 6, 6]


def test_day9_part2():
    initial_data = get_data("./data/day9_example1.txt")

    answer = get_part2_answer(initial_data)

    assert answer == 1134
