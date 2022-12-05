def get_data(filename):
    with open(filename) as input_file:
        return [[int(c) for c in line.strip()] for line in input_file.readlines()]


def get_epsilon(data):
    row_count = len(data)
    gamma = ""
    epsilon = ""

    for j in range(0, len(data[0])):
        common = (
            1 if sum([data[i][j] for i in range(0, row_count)]) > row_count / 2 else 0
        )
        gamma += str(common)
        epsilon += str(0 if common else 1)
    return gamma, epsilon


def get_oxygen_generator(data):
    row_count = len(data)
    col_count = len(data[0])

    filtered_rows = [a for a in range(0, len(data))]

    for j in range(0, len(data[0])):
        bit_criteria = (
            1
            if sum([data[row][j] for row in filtered_rows]) >= len(filtered_rows) / 2
            else 0
        )
        new_filter = []

        if len(filtered_rows) > 1:
            for i in range(0, len(filtered_rows)):
                if data[filtered_rows[i]][j] == bit_criteria:
                    new_filter.append(filtered_rows[i])
            filtered_rows = new_filter

    return "".join([str(a) for a in data[filtered_rows[0]]])


def get_co2_scrubber(data):
    row_count = len(data)
    col_count = len(data[0])

    filtered_rows = [a for a in range(0, len(data))]

    for j in range(0, len(data[0])):
        bit_criteria = (
            0
            if sum([data[row][j] for row in filtered_rows]) >= len(filtered_rows) / 2
            else 1
        )
        new_filter = []

        if len(filtered_rows) > 1:
            for i in range(0, len(filtered_rows)):
                if data[filtered_rows[i]][j] == bit_criteria:
                    new_filter.append(filtered_rows[i])
            filtered_rows = new_filter

    return "".join([str(a) for a in data[filtered_rows[0]]])


if __name__ == "__main__":
    input_data = get_data("./data/day3_input1.txt")
    gamma, epsilon = get_epsilon(input_data)

    print(gamma, epsilon)
    print(int(gamma, 2), int(epsilon, 2))
    print(int(gamma, 2) * int(epsilon, 2))

    oxygen = get_oxygen_generator(input_data)
    co2 = get_co2_scrubber(input_data)
    print(oxygen, co2)
    print(int(oxygen, 2), int(co2, 2))
    print(int(oxygen, 2) * int(co2, 2))
