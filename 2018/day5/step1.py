def get_list():
    rows = []

    f = open('./train.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows

def scan_row(row):
    i = 0

    while i < len(row) - 1:
        letter_a = row[i]
        letter_b = row[i+1]

        if letter_a != letter_b and letter_a.upper() == letter_b.upper():
            row = row[:i] + row[i+2:]
            i = -1
        i += 1
    return row

rows = get_list()
row = rows[0].strip()

print(len(scan_row(row)))