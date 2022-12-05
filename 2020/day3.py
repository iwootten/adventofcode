def get_data(filename):
    matrix = []
    with open(filename) as input_file:
        for line in input_file.readlines():
            matrix.append(list(line.rstrip("\n")))
    return matrix


def get_part1_answer(forest_matrix, col_diff, row_diff):
    row, col, count = 0, 0, 0
    columns_per_row = len(forest_matrix[0])

    while row < len(forest_matrix):
        count += 1 if forest_matrix[row][col % columns_per_row] == "#" else 0
        col += col_diff
        row += row_diff

    return count


if __name__ == "__main__":
    input_data = get_data("./data/day3_input1.txt")
    a = get_part1_answer(input_data, 3, 1)

    b = get_part1_answer(input_data, col_diff=1, row_diff=1)
    c = get_part1_answer(input_data, col_diff=5, row_diff=1)
    d = get_part1_answer(input_data, col_diff=7, row_diff=1)
    e = get_part1_answer(input_data, col_diff=1, row_diff=2)

    print(f"Part1: {a}")
    print(f"Part2: {a * b * c * d * e}")
