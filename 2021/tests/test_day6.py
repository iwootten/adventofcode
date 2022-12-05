from day6 import get_data, get_part1_answer, get_part2_answer


def test_day6_part1():
    initial_data = get_data("./data/day6_example1.txt")

    answer = get_part1_answer(initial_data, 18)

    assert answer == [
        int(a) for a in "6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8".split(",")
    ]

    answer = len(get_part1_answer(initial_data, 80))

    assert answer == 5934


def test_day6_part2():
    initial_data = get_data("./data/day6_example1.txt")

    answer = get_part2_answer(initial_data, 256)

    assert answer == 26984457539
