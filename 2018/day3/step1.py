import re

def get_list():
    rows = []

    f = open('./input.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows

def get_layout(row):
    matches = re.findall(r"#\d+\s@\s(\d+),(\d+):\s(\d+)+x(\d+)+", row)
    return (int(matches[0][0]), int(matches[0][1])), (int(matches[0][2]), int(matches[0][3]))

rows = get_list()
fabric = [[0 for x in xrange(1000)] for x in xrange(1000)]

for i, row in enumerate(rows):
    pos, size = get_layout(row)

    for y in range(pos[0], pos[0] + size[0]):
        for x in range(pos[1], pos[1] + size[1]):
            fabric[x][y] += 1

count = 0

for x in range(0, len(fabric)):
    for y in range(0, len(fabric[x])):
        if fabric[x][y] > 1:
            count += 1

print count