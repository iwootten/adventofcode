import heapq
from collections import defaultdict


def get_data(filename):
    with open(filename) as input_file:
        lines = [[int(i) for i in line.strip()] for line in input_file.readlines()]

        return [[lines[i][j] for i in range(len(lines[0]))] for j in range(len(lines))]


def get_data_2(filename):
    # Get data in matrix 5 times larger, with values increasing between 1-9, offset by a value of 1
    data = get_data(filename)
    return [
        [
            (
                (
                    data[x % len(data)][y % len(data[0])]
                    + int(x / len(data))
                    + int(y / len(data[0]))
                    - 1
                )
            )
            % 9
            + 1
            for y in range(0, 5 * len(data))
        ]
        for x in range(0, 5 * len(data[0]))
    ]


def get_path(source, data):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distances = {}

    queue = []
    visited = defaultdict(bool)

    # Use dijkstra to work out path from source to dest
    for x in range(len(data)):
        for y in range(len(data[0])):
            distances[(x, y)] = 2147483647

    heapq.heappush(queue, (0, source))

    distances[source] = 0

    while queue:
        _, u = heapq.heappop(queue)
        visited[u] = True

        x, y = u

        neighbours = [
            (x + dx, y + dy)
            for dx, dy in directions
            if ((x + dx) >= 0)
            and ((x + dx) < len(data))
            and ((y + dy) >= 0)
            and ((y + dy) < len(data[0]))
        ]

        for v in neighbours:
            if not visited[v]:
                distance = distances[u] + data[v[0]][v[1]]

                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(queue, (distance, v))

    return distances


def print_matrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            print(matrix[x][y], end="")
        print("")


def get_part1_answer(data):
    distances = get_path((0, 0), data)

    return distances[(len(data) - 1, len(data[0]) - 1)]


def get_part2_answer(data):
    distances = get_path((0, 0), data)

    return distances[(len(data) - 1, len(data[0]) - 1)]


if __name__ == "__main__":
    # data = get_data("./data/day15_example1.txt")
    data = get_data_2("./data/day15_input1.txt")
    part2 = get_part2_answer(data)
    # print_matrix(data)
    # print()
    # print_matrix(data_b)

    # data = [[8]]
    # for y in range(len(data) * 5):
    #     for x in range(len(data[0]) * 5):
    #         print(
    #             (
    #                 data[x % len(data)][y % len(data[0])]
    #                 + int(x / len(data))
    #                 + int(y / len(data[0]))
    #                 - 1
    #             )
    #             % 9
    #             + 1,
    #             end="",
    #         )
    #     print()
    print(part2)
