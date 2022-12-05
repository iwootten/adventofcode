from day8 import get_data, get_part1_answer, get_part2_answer


def test_day8_part1():
    initial_data = get_data("./data/day8_example2.txt")

    answer = get_part1_answer(initial_data)

    assert answer == 26


def test_day8_part2():
    initial_data = get_data("./data/day8_example1.txt")

    answer = get_part2_answer(initial_data)

    assert answer == 5353


def test_day8_part2_total():
    initial_data = get_data("./data/day8_example2.txt")

    answer = get_part2_answer(initial_data)

    assert answer == 61229
