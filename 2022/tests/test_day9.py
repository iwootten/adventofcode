from day9 import get_data, get_part1_answer, get_part2_answer


def test_day9_part1():
    data = get_data("./data/day9_example.txt")
    answer = get_part1_answer(data)
    assert answer == 13


def test_day9_part2():
    data = get_data("./data/day9_example.txt")
    answer = get_part2_answer(data)
    assert answer == 1


def test_day9_part2_ex2():
    data = get_data("./data/day9_example2.txt")
    answer = get_part2_answer(data)
    assert answer == 36
