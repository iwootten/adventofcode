from day2 import get_data, get_part1_answer, get_part2_answer


def test_day2_part1():
    data = get_data("./data/day2_example1.txt")
    answer = get_part1_answer(data)
    assert answer == (15, 10)


def test_day2_part2():
    data = get_data("./data/day2_example1.txt")
    answer = get_part2_answer(data)
    assert answer == (15, 60)
