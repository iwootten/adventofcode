from day3 import get_data, get_part1_answer


def test_day3_part1():
    data = get_data("./data/day3_example.txt")
    answer = get_part1_answer(data, col_diff=3, row_diff=1)
    assert answer == 7


def test_day3_part2():
    data = get_data("./data/day3_example.txt")

    assert get_part1_answer(data, col_diff=1, row_diff=1) == 2
    assert get_part1_answer(data, col_diff=3, row_diff=1) == 7
    assert get_part1_answer(data, col_diff=5, row_diff=1) == 3
    assert get_part1_answer(data, col_diff=7, row_diff=1) == 4
    assert get_part1_answer(data, col_diff=1, row_diff=2) == 2
