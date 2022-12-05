def get_data(filename):
    with open(filename) as input_file:
        return [
            [
                (int(c.split(",")[0]), int(c.split(",")[1]))
                for c in line.strip().split("->")
            ]
            for line in input_file.readlines()
        ]


def empty_matrix(input_data):
    max_x = max(d[0] for row in input_data for d in row)
    max_y = max(d[1] for row in input_data for d in row)

    matrix = [[0 for x in range(0, max_x + 2)] for y in range(0, max_y + 2)]

    return matrix


def process_data(input_data, matrix, diagonals=False):
    for start, end in input_data:
        print(f"Processing {start, end}")
        min_x, max_x = min(start[0], end[0]), max(start[0], end[0])
        min_y, max_y = min(start[1], end[1]), max(start[1], end[1])
        if start[1] == end[1]:
            print(f"Range for x is {range(min_x, max_x + 1)}")
            for x in range(min_x, max_x + 1):
                matrix[x][start[1]] += 1
        elif start[0] == end[0]:
            print(f"Range for y is {range(min_y, max_y + 1)}")
            for y in range(min_y, max_y + 1):
                matrix[start[0]][y] += 1
        elif diagonals:
            x_step = -1 if end[0] < start[0] else 1
            y_step = -1 if end[1] < start[1] else 1

            print(
                f"Range for x, y is {range(start[0], end[0] + x_step, x_step), range(start[1], end[1] + y_step, y_step)}"
            )
            for x, y in zip(
                range(start[0], end[0] + x_step, x_step),
                range(start[1], end[1] + y_step, y_step),
            ):
                matrix[x][y] += 1
        else:
            print(f"Skipped {start, end}")
    return matrix


def intersect_count(matrix, overlap_threshold):
    count = 0

    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            if matrix[x][y] >= overlap_threshold:
                count += 1
    return count


if __name__ == "__main__":
    input_data = get_data("./data/day5_input1.txt")
    empty = empty_matrix(input_data)
    print(len(empty), len(empty[0]))
    complete_matrix = process_data(input_data, empty, True)
    # print(input_data)
    print(intersect_count(complete_matrix, 2))
