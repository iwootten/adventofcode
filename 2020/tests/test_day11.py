import day11

def test_get_part1_answer():
    data = day11.get_data("./data/day11_example1.txt")

    assert day11.get_part1_answer(data) == 37

def test_get_part2_answer():
    data = day11.get_data("./data/day11_example1.txt")

    assert day11.get_part2_answer(data) == 26