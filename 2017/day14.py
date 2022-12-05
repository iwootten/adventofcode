from day10 import knot_hash


def setup_grid(string_to_hash):
    grid = [[] for i in range(128)]
    total = 0

    for k in range(len(grid)):
        current_row = "{}-{}".format(string_to_hash, k)
        hashed_value = knot_hash(current_row)

        for c in hashed_value:
            binary_value = bin(int(c, 16))[2:].zfill(4)
            for v in binary_value:
                grid[k].append(v)
        total += sum([int(v) for v in grid[k]])

    return grid, total


def find_neighbour_indices(m, i, j, dist=1):
    neighbours = []

    irange = range(max(0, i - dist), min(len(m), i + dist + 1))
    jrange = range(max(0, j - dist), min(len(m[0]), j + dist + 1)) if len(m) > 0 else []

    for icheck in irange:
        for jcheck in jrange:
            if ((icheck != i and jcheck==j) or (jcheck != j and icheck==i)) and m[icheck][jcheck] == "#":
                neighbours.append((icheck, jcheck))

    return neighbours


def label_regions(grid):
    current_label = 1
    queue = []

    for j in range(len(grid)):
        for k in range(len(grid[j])):
            if grid[j][k] == "#":
                grid[j][k] = str(current_label)
                queue.append((j, k))

                while len(queue) > 0:
                    x, y = queue.pop()

                    neighbours = find_neighbour_indices(grid, x, y, dist=1)

                    for element in neighbours:
                        grid[element[0]][element[1]] = str(current_label)

                    if neighbours:
                        queue.extend(neighbours)

                current_label += 1
    return grid, current_label


def part1():
    grid, total = setup_grid("ffayrhll")
    print "Total: {}".format(total)

    # print knot_hash("flqrgnkx-0")
    # print "".join([bin(int(c, 16))[2:].zfill(4) for c in knot_hash("flqrgnkx-0")])

    assert "".join(grid[0][0:8]) == "11010100"
    assert "".join(grid[1][0:8]) == "01010101"
    assert "".join(grid[2][0:8]) == "00001010"
    assert "".join(grid[3][0:8]) == "10101101"
    assert "".join(grid[4][0:8]) == "01101000"
    assert "".join(grid[5][0:8]) == "11001001"
    assert "".join(grid[6][0:8]) == "01000100"
    assert "".join(grid[7][0:8]) == "11010110"


def print_region(grid, size=8):
    for j in range(size):
        print "".join(grid[j][0:size])


def part2():
    grid, total = setup_grid("ffayrhll")

    for j in range(len(grid)):
        for k in range(len(grid[j])):
            grid[j][k] = "#" if grid[j][k] == "1" else "."

    print_region(grid)

    print "\nLabelling Regions....\n"

    grid, current_label = label_regions(grid)

    print_region(grid, 8)

    print current_label - 1


part2()
