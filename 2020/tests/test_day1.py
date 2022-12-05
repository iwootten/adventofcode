from day1 import get_data, get_part1_answer, get_part2_answer


def test_day1_part1():
    data = get_data("./data/day1_example1.txt")
    answer = get_part1_answer(data)
    assert answer == 514579


def test_day1_part2():
    data = get_data("./data/day1_example1.txt")
    answer = get_part2_answer(data)
    assert answer == 241861950
