from day5 import get_data, get_part1_answer, get_part2_answer


def test_day5_part1():
    data = get_data("./data/day5_example.txt")
    answer = get_part1_answer(data)
    assert answer == "CMZ"


def test_day5_part2():
    data = get_data("./data/day5_example.txt")
    answer = get_part2_answer(data)
    assert answer == "MCD"
