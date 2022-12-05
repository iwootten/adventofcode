with open('./input1.txt', 'r') as content_file:
    total = 0
    negative = 0
    for row in content_file.readlines():
        total += int(row[1:]) * -1 if '-' == row[0] else int(row[1:])
        negative += 1 if '-' == row[0] else 0
    print total, negative