import day7


def test_part1_example():
    data = day7.get_data("./data/day7_example1.txt")
    bag_map = day7.get_bag_map(data)
    assert len(set(day7.find_possible_bags(bag_map, "shiny_gold"))) == 4


def test_part2_example():
    data = day7.get_data("./data/day7_example1.txt")
    bag_map = day7.get_bag_map(data)
    assert day7.count_bags(bag_map, "shiny_gold") - 1 == 32

    data = day7.get_data("./data/day7_example2.txt")
    bag_map = day7.get_bag_map(data)
    assert day7.count_bags(bag_map, "shiny_gold") - 1 == 126
