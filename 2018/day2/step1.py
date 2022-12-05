def get_list():
    rows = []

    f = open('./input.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows

box_map = []
two_code_count = 0
three_code_count = 0

for row in get_list():
    contains_two = False
    contains_three = False
    row_map = [0] * 200

    for c in row:
        row_map[ord(c)] += 1

    for item in row_map:
        if item == 2:
            contains_two = True
        if item == 3:
            contains_three = True

    two_code_count += 1 if contains_two else 0
    three_code_count += 1 if contains_three else 0

print(two_code_count, three_code_count, two_code_count * three_code_count)
