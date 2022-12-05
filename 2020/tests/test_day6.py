import day6


def test_part1_examples():
    data = day6.get_data("./data/day6_example1.txt")
    assert day6.get_part1_answer(data) == 11


def test_part2_examples():
    data = day6.get_data("./data/day6_example1.txt")

    assert day6.line_count("abc") == 3
    assert day6.line_count("a\nb\nc") == 0
    assert day6.line_count("ab\nbc") == 1
    assert day6.line_count("a\na\na\na") == 1
    assert day6.line_count("b") == 1

    assert day6.get_part2_answer(data) == 6
