from day4 import get_data, get_part1_answer, get_part2_answer


def test_day4_part1():
    numbers, boards = get_data("./data/day4_example1.txt")
    answer = get_part1_answer(numbers, boards)
    assert answer == (24, 188)


def test_day4_part2():
    numbers, boards = get_data("./data/day4_example1.txt")
    answer = get_part2_answer(numbers, boards)
    assert answer == (13, 148)
