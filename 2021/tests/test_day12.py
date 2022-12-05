from day12 import get_data, get_part1_answer, get_part2_answer


def test_day10_part1():
    initial_data = get_data("./data/day12_example1.txt")

    answer = get_part1_answer(initial_data)

    assert answer == 10


def test_day10_part1_2():
    initial_data = get_data("./data/day12_example2.txt")

    answer = get_part1_answer(initial_data)

    assert answer == 19


def test_day10_part1_3():
    initial_data = get_data("./data/day12_example3.txt")

    answer = get_part1_answer(initial_data)

    assert answer == 226


def test_day10_part2():
    initial_data = get_data("./data/day12_example1.txt")

    answer = get_part2_answer(initial_data)

    assert answer == 36


def test_day10_part2():
    initial_data = get_data("./data/day12_example2.txt")

    answer = get_part2_answer(initial_data)

    assert answer == 103


def test_day10_part3():
    initial_data = get_data("./data/day12_example3.txt")

    answer = get_part2_answer(initial_data)

    assert answer == 3509
