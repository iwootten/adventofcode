def get_data(filename):
    with open(filename) as input_file:
        return [[int(b) for b in list(a.strip())] for a in input_file.readlines()]


def get_low_points(input_data):
    low_points = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x in range(len(input_data)):
        for y in range(len(input_data[0])):
            min_neighbour = min(
                [
                    input_data[x + dx][y + dy]
                    for dx, dy in directions
                    if ((x + dx) >= 0)
                    and ((x + dx) < len(input_data))
                    and ((y + dy) >= 0)
                    and ((y + dy) < len(input_data[0]))
                ]
            )

            if min_neighbour > input_data[x][y]:
                low_points.append((x, y))
    return low_points


def get_part1_answer(input_data):
    return [input_data[p[0]][p[1]] + 1 for p in get_low_points(input_data)]


def get_basins(input_data):
    groups = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for gx, gy in get_low_points(input_data):
        group_stack = [(gx, gy)]
        group = [(gx, gy)]
        while len(group_stack) > 0:
            lx, ly = group_stack.pop()
            for dx, dy in directions:
                for mag in range(len(input_data)):
                    if (
                        ((lx + dx * mag) >= 0)
                        and ((lx + dx * mag) < len(input_data))
                        and ((ly + dy * mag) >= 0)
                        and ((ly + dy * mag) < len(input_data[0]))
                    ):
                        current = input_data[lx + dx * mag][ly + dy * mag]

                        if current == 9:
                            break
                        if (
                            current > input_data[lx][ly]
                            and (lx + dx * mag, ly + dy * mag) not in group
                        ):
                            group.append((lx + dx * mag, ly + dy * mag))
                            group_stack.append((lx + dx * mag, ly + dy * mag))
        groups.append([input_data[x][y] for x, y in group])
    return groups


def get_part2_answer(input_data):
    basin_lengths = [len(b) for b in get_basins(input_data)]

    basin_lengths.sort(reverse=True)

    return basin_lengths[0] * basin_lengths[1] * basin_lengths[2]


if __name__ == "__main__":
    input_data = get_data("./data/day9_input1.txt")

    part2 = get_part2_answer(input_data)

    print(part2)
