from day3 import get_data, get_epsilon, get_oxygen_generator, get_co2_scrubber


def test_day2_part1():
    data = get_data("./data/day3_example1.txt")
    gamma, epsilon = get_epsilon(data)
    assert gamma, epsilon == ("10110", "01001")

    assert (int(gamma, 2), int(epsilon, 2)) == (22, 9)
    assert (int(gamma, 2) * int(epsilon, 2)) == 198


def test_day3_part2():
    data = get_data("./data/day3_example1.txt")
    oxygen_generator = get_oxygen_generator(data)
    co2_scrubber = get_co2_scrubber(data)
    assert oxygen_generator, co2_scrubber == ("10111", "01010")

    assert (int(oxygen_generator, 2), int(co2_scrubber, 2)) == (23, 10)
    assert (int(oxygen_generator, 2) * int(co2_scrubber, 2)) == 230
