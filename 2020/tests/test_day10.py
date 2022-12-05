import day10


def test_part1_example():
    data = day10.get_data("./data/day10_example1.txt")

    assert day10.find_differences(data) == (7, 5)


def test_part1_example_2():
    data = day10.get_data("./data/day10_example2.txt")

    assert day10.find_differences(data) == (22, 10)


def test_part2():
    data = day10.get_data("./data/day10_example1.txt")

    assert day10.search_data(data) == 8


def test_part2_example2():
    data = day10.get_data("./data/day10_example2.txt")
    data.append(0)
    data.append(max(data) + 3)
    data.sort()

    assert day10.search_data(data) == 19208
