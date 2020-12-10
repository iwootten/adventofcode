def get_coordinates():
    rows = []

    f = open('./input.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows

# Calculate the manhattan matrix...

# Do two passes of different sized areas
# determine which do not change in size

def get_positions(coordinates, matrix_size):
    coordinate_list = []
    for coordinate in coordinates:
        x, y = coordinate.split(',')
        coordinate_list.append((int(x), int(y)))
    return coordinate_list

def manhattan(pos_a, pos_b):
    return abs(pos_b[0] - pos_a[0]) + abs(pos_b[1] - pos_a[1])

def sum_manhattan(matrix_size, limit):
    matrix = [['.' for x in range(matrix_size)] for x in range(matrix_size)]
    coordinates = get_positions(get_coordinates(), matrix_size)

    for j in range(matrix_size):
        for i in range(matrix_size):
            distances = []
            for (x, y) in coordinates:
                distances.append(manhattan((i, j), (x, y)))

            total_distance = sum(distances)

            if total_distance < limit:
                matrix[i][j] = '#'
    return matrix

def clear_non_contiguous(matrix):
    for j in range(len(matrix)):
        sum_neighbours = 0
        for i in range(len(matrix[j])):
            if matrix[i][j] != '#':
                continue
            neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for x, y in neighbours:
                if x + i > 0 and y + j > 0 and x + i < len(matrix) and y + j < len(matrix[i]) and matrix[x + i][y + j]:
                    sum_neighbours += 1
            if sum_neighbours == 0:
                matrix[i][j] = '.'
    return matrix

def print_matrix(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            print(matrix[i][j], end="")
        print()

def sum_matrix(matrix):
    total = 0
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if matrix[i][j] == '#':
                total += 1
    return total

def print_coordinates(coordinates, matrix_size):
    index = 0
    for j in range(matrix_size):
        for i in range(matrix_size):
            print(index if (i, j) in coordinates else '.', end='')
            if (i, j) in coordinates:
                index += 1
        print()

matrix_size = 500
summed = sum_manhattan(matrix_size, 10000)
cleared = clear_non_contiguous(summed)

print_matrix(summed)
print_matrix(cleared)
print(sum_matrix(summed))
