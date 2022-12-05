import re


def get_data(filename):
    with open(filename) as input_file:
        return input_file.read().splitlines()


def get_bag_map(data):
    bag_map = {}
    for line in data:
        source, target_description = line.rstrip(".").split("bags contain")
        source = source.rstrip(" ").replace(" ", "_")
        targets = [
            target.lstrip(" ").rstrip("bags").rstrip(" ").replace(" ", "_")
            for target in target_description.split(",")
        ]
        if targets:
            bag_map[source] = []
            for target in targets:
                match = re.search("^[0-9]+", target)
                if match:
                    bag_map[source].append(
                        (int(target[: match.end()]), target[match.end() + 1 :])
                    )

    return bag_map


def find_possible_bags(bag_map, search_key):
    appears_in = [
        key
        for key, values in bag_map.items()
        if search_key in [value[1] for value in values]
    ]
    for key in appears_in:
        parents = find_possible_bags(bag_map, key)
        appears_in += parents if parents else []

    return appears_in


def count_bags(bag_map, bag_to_count):
    if not bag_map[bag_to_count]:
        return 1
    return 1 + sum(
        [
            child_bag_count * count_bags(bag_map, child_bag_values)
            for child_bag_count, child_bag_values in bag_map[bag_to_count]
        ]
    )


if __name__ == "__main__":
    input_data = get_data("./data/day7_input1.txt")
    data_map = get_bag_map(input_data)

    part_1 = len(set(find_possible_bags(data_map, "shiny_gold")))
    part_2 = count_bags(data_map, "shiny_gold") - 1

    print(f"Part1: {part_1}")
    print(f"Part2: {part_2}")
