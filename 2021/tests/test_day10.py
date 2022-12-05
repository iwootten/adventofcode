from day10 import (
    get_data,
    get_part1_answer,
    get_part2_answer,
    get_illegal_chars,
    get_valid_lines,
    get_autocomplete,
)


def test_day10_part1():
    initial_data = get_data("./data/day10_example1.txt")

    chars = get_illegal_chars(initial_data)
    answer = get_part1_answer(initial_data)

    assert chars == [1197, 3, 57, 3, 25137]
    assert answer == 26397


def test_day10_valid_lines():
    initial_data = get_data("./data/day10_example1.txt")

    lines = get_valid_lines(initial_data)

    assert lines == [0, 1, 3, 6, 9]


def test_day10_autocomplete():
    initial_data = get_data("./data/day10_example1.txt")

    autocomplete = get_autocomplete(initial_data[0])

    assert "".join(autocomplete) == "}}]])})]"


def test_day10_part2():
    initial_data = get_data("./data/day10_example1.txt")

    answer = get_part2_answer(initial_data)

    assert answer == 288957
