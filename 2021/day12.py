from os import path


def get_data(filename):
    with open(filename) as input_file:
        return [line.strip().split("-") for line in input_file.readlines()]


def get_route_graph(input_data):
    routes = {}
    for start, end in input_data:
        # print(f"{start}, {end}")
        if start not in routes:
            routes[start] = set()
        if end not in routes:
            routes[end] = set()

        routes[start] |= {end}
        routes[end] |= {start}
    return routes


def find_paths(cave_graph, current_cave="start", end_cave="end", path=[]):
    path = path + [current_cave]

    if current_cave == end_cave:
        return [path]
    if current_cave not in cave_graph:
        return []

    paths = []

    for possible_cave in cave_graph[current_cave]:
        if possible_cave not in path or possible_cave.isupper():
            paths += find_paths(cave_graph, possible_cave, end_cave, path)

    return paths


def find_paths_multiple(cave_graph, current_cave="start", end_cave="end", path=[]):
    path = path + [current_cave]

    if current_cave == end_cave:
        return [path]
    if current_cave not in cave_graph:
        return []

    paths = []

    for possible_cave in cave_graph[current_cave]:
        if possible_cave.islower() and possible_cave != "start":
            this_cave_count = path.count(possible_cave)
            if this_cave_count < 2:
                small_caves = [c for c in path if not c.isupper()]
                other_small_caves = [
                    small_caves.count(c) for c in small_caves if c != possible_cave
                ] or [0]
                if max(other_small_caves) == 2 and this_cave_count == 0:
                    paths += find_paths_multiple(
                        cave_graph, possible_cave, end_cave, path
                    )
                elif max(other_small_caves) == 1 and this_cave_count <= 1:
                    paths += find_paths_multiple(
                        cave_graph, possible_cave, end_cave, path
                    )
        elif possible_cave.isupper():
            paths += find_paths_multiple(cave_graph, possible_cave, end_cave, path)

    return paths


def get_part1_answer(input_data):
    route_graph = get_route_graph(input_data)
    return len(find_paths(route_graph))


def get_part2_answer(input_data):
    route_graph = get_route_graph(input_data)
    paths = find_paths_multiple(route_graph)
    return len(paths)


if __name__ == "__main__":
    input_data = get_data("./data/day12_input1.txt")

    part2 = get_part2_answer(input_data)

    print(part2)
