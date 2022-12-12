from day10 import get_data, get_part1_answer, get_part2_answer


def test_day10_part1():
    data = get_data("./data/day10_example2.txt")
    answer = get_part1_answer(data)
    assert answer == 13140


def test_day10_part2():
    data = get_data("./data/day10_example2.txt")
    answer = get_part2_answer(data)
    assert answer == "##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######.....\n"
