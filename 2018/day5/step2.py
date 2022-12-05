import string

def get_list():
    rows = []

    f = open('./input.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows

def remove_letter(row, to_remove):
    return row.replace(to_remove.lower(), '').replace(to_remove.upper(), '')

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

alphabet = string.ascii_lowercase
min_length = 9999999
min_letter = None
min_code = None

for letter in alphabet:
    scanned_row = scan_row(remove_letter(row, letter))
    if len(scanned_row) < min_length:
        min_length = len(scanned_row)
        min_letter = letter
        min_code = scanned_row

print(min_letter, min_length)