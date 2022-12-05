def get_list():
    rows = []

    f = open('./input.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows

def get_differing_rows(rows):
    difference = None

    for index, row in enumerate(rows):
        for i in range(index + 1, len(rows)):
            diff = 0
            comparison_row = rows[i]

            for char_pos, c in enumerate(row.strip()):
                if c != comparison_row[char_pos]:
                    diff += 1
            if diff == 1:
                difference = (index, i)
    return difference

def common_letters(row_a, row_b):
    row_a = row_a.strip()
    for char_pos, c in enumerate(row_a):
        if c != row_b[char_pos]:
            return row_a[0:char_pos] + row_a[char_pos + 1:]

row_list = get_list()
row_a_index, row_b_index = get_differing_rows(row_list)

print(row_a_index, row_b_index)
print(common_letters(row_list[row_a_index], row_list[row_b_index]))
