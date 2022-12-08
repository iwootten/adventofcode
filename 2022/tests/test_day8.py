from day8 import get_data, get_part1_answer, get_part2_answer


def test_day8_part1():
    data = get_data("./data/day8_example.txt")
    answer = get_part1_answer(data)
    assert answer == 21


def test_day8_part2():
    data = get_data("./data/day8_example.txt")
    answer = get_part2_answer(data)
    assert answer == 8
