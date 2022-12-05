from day11 import get_data, get_part1_answer, get_part2_answer


def test_day11_part1():
    initial_data = get_data("./data/day11_example1.txt")

    answer, count = get_part1_answer(initial_data)

    assert answer == [
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3],
    ]
    assert count == 9


def test_day11_part1_2():
    initial_data = get_data("./data/day11_example2.txt")
    lines, count = get_part1_answer(initial_data, iterations=10)

    answer = ["".join([str(c) for c in line]) for line in lines]

    assert answer == [
        "0481112976",
        "0031112009",
        "0041112504",
        "0081111406",
        "0099111306",
        "0093511233",
        "0442361130",
        "5532252350",
        "0532250600",
        "0032240000",
    ]
    assert count == 204


def test_day11_part1_3():
    initial_data = get_data("./data/day11_example2.txt")
    _, count = get_part1_answer(initial_data, iterations=100)

    assert count == 1656


def test_day11_part2():
    initial_data = get_data("./data/day11_example2.txt")
    answer = get_part2_answer(initial_data)

    assert answer == 195
