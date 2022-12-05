def get_data(filename):
    with open(filename) as input_file:
        lines = input_file.readlines()
        folds = []

        coordinates = [
            (int(l.split(",")[0]), int(l.split(",")[1])) for l in lines if "," in l
        ]
        for l in lines:
            if "fold" in l:
                direction, value = l.strip("fold along ").strip().split("=")
                folds.append((direction, int(value)))
        return coordinates, folds


def get_matrix(positions):
    max_x, max_y = 0, 0
    for x, y in positions:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    matrix = [["." for i in range(max_y + 1)] for j in range(max_x + 1)]

    for x, y in positions:
        matrix[x][y] = "#"
    return matrix


def fold_matrix(matrix, direction, value):
    a, b = [], []

    if direction == "x":
        a = matrix[0:value]
        b = matrix[len(matrix) : value : -1]
    if direction == "y":
        a = [matrix[x][0:value] for x in range(len(matrix))]
        b = [
            [matrix[x][y] for y in range(len(matrix[0]) - 1, value, -1)]
            for x in range(len(matrix))
        ]

    return [
        ["#" if a[x][y] == "#" or b[x][y] == "#" else "." for y in range(len(a[0]))]
        for x in range(len(a))
    ]


def print_matrix(matrix):
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            print(matrix[x][y], end="")
        print("")


def get_part1_answer(positions, fold):
    matrix = get_matrix(positions)

    folded = fold_matrix(matrix, fold[0], fold[1])

    return sum([line.count("#") for line in folded])


def get_part2_answer(positions, folds):
    matrix = get_matrix(positions)
    folded = matrix.copy()
    for fold in folds:
        folded = fold_matrix(folded, fold[0], fold[1])

    return folded


if __name__ == "__main__":
    positions, folds = get_data("./data/day13_input1.txt")

    print(get_part1_answer(positions, folds[0]))
    print_matrix(get_part2_answer(positions, folds))
