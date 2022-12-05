import day15


def test_day15_part1():
    data = day15.get_data("./data/day15_example1.txt")

    assert day15.get_part1_answer(data) == 40


def test_day15_part2():
    data = day15.get_data_2("./data/day15_example1.txt")

    assert day15.get_part2_answer(data) == 315
