import day8


def test_part1_example():
    data = day8.get_data("./data/day8_example1.txt")

    assert day8.get_accumulator_total(data)[0] == 5


def test_part2_example():
    data = day8.get_data("./data/day8_example1.txt")

    assert day8.replace_instructions(data) == 8
