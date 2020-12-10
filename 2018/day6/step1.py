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

def find_closest(matrix_size):
    matrix = [[None for x in range(matrix_size)] for x in range(matrix_size)]
    coordinates = get_positions(get_coordinates(), matrix_size)
    min_index = None
    for j in range(matrix_size):
        for i in range(matrix_size):
            distances = []
            for c_index, (x, y) in enumerate(coordinates):
                distance = manhattan((i, j), (x, y))

                distances.append({
                    'distance': distance,
                    'index': c_index
                })
            min_item = min(distances, key=lambda x: x['distance'])
            min_count = sum([1 for item in distances if item['distance'] == min_item['distance']])
            matrix[i][j] = min_item['index'] if min_count == 1 else -1
    return matrix

def print_matrix(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            print(matrix[i][j], end="")
        print()

def print_coordinates(coordinates, matrix_size):
    index = 0
    for j in range(matrix_size):
        for i in range(matrix_size):
            print(index if (i, j) in coordinates else '.', end='')
            if (i, j) in coordinates:
                index += 1
        print()

def find_infinite(matrix):
    infinite = []
    for i in range(matrix_size):
        if matrix[0][i] not in infinite:
            infinite.append(matrix[0][i])
        if matrix[len(matrix) - 1][i] not in infinite:
            infinite.append(matrix[len(matrix) - 1][i])
        if matrix[i][0] not in infinite:
            infinite.append(matrix[i][0])
        if matrix[i][len(matrix) - 1] not in infinite:
            infinite.append(matrix[i][len(matrix) - 1])
    return list(set(infinite))

matrix_size = 500
closest = find_closest(matrix_size)

print_coordinates(get_positions(get_coordinates(), matrix_size), matrix_size)
print_matrix(closest)

infinite = find_infinite(closest)

area_count = [0] * matrix_size

for j in range(matrix_size):
    for i in range(matrix_size):
        if closest[i][j] != -1 and closest[i][j] not in infinite:
            area_count[closest[i][j]] += 1

max_index = 0

for i, count in enumerate(area_count):
    if count > area_count[max_index]:
        max_index = i

print("Largest area: {}".format(max(area_count)))
print("Row with largest area: {}".format(max_index))
