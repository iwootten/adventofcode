from day7 import get_data, get_part1_answer, get_part2_answer


def test_day6_part1():
    data = get_data("./data/day7_example.txt")

    answer = get_part1_answer(data)

    assert answer == 95437


def test_day6_part2():
    data = get_data("./data/day7_example.txt")
    answer = get_part2_answer(data)

    assert answer == 24933642
