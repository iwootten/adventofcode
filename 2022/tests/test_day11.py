from day11 import get_data, get_inspection_counts, get_part1_answer, get_part2_answer


def test_day11_inspection_counts():
    data = get_data("./data/day11_example.txt")
    answer = get_inspection_counts(data)
    assert answer == [101, 95, 7, 105]


def test_day11_part1():
    data = get_data("./data/day11_example.txt")
    answer = get_part1_answer(data)
    assert answer == 10605


def test_day11_part2():
    data = get_data("./data/day11_example.txt")
    answer = get_part2_answer(data)
    assert answer == 2713310158
