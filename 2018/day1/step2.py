def get_list():
    rows = []

    f = open('./input1.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows

if __name__ == "__main__":
    index = 0
    frequency = 0
    previous_frequencies = [0] * 500000
    previous_frequencies[0] += 1
    frequency_changes = get_list()
    found = False

    while not found:
        row = frequency_changes[index % len(frequency_changes)]

        frequency += int(row[1:]) * -1 if '-' == row[0] else int(row[1:])

        previous_frequencies[frequency] += 1

        if previous_frequencies[frequency] == 2:
            found = True
        index += 1
    print frequency