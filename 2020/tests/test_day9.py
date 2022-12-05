import day9


def test_part1_example():
    data = day9.get_data("./data/day9_example1.txt")

    assert day9.find_rule_breaker(data, 5) == 127


def test_part2_example():
    data = day9.get_data("./data/day9_example1.txt")

    assert day9.find_weakness(data, 127) == 62
