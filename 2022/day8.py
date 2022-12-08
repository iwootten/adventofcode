def get_data(filename):
    with open(filename) as input_file:
        return [[int(a) for a in l.strip()] for l in input_file.readlines()]


def get_part1_answer(data):
    count = (4 * len(data)) - 4
    for x in range(1, len(data) - 1):
        for y in range(1, len(data[x]) - 1):
            height = data[x][y]
            visible = False
            # print(f"{x}, {y}: {data[x][y]}")
            left = data[x][:y]
            visible |= height > max(left)
            # print(f"Left: {left}")
            right = data[x][y+1:]
            visible |= height > max(right)
            # print(f"Right: {right}")
            up = [data[i][y] for i in range(0, x)]
            visible |= height > max(up)
            # print(f"Up: {up}")
            down = [data[i][y] for i in range(x + 1, len(data[x]))]
            visible |= height > max(down)
            # print(f"Down: {down}")
            count += 1 if visible else 0
    return count

def get_distance(trees, height):
    view = [i + 1 for i, v in enumerate(trees) if v >= height]
    return len(trees) if len(view) == 0 else view[0]

def get_part2_answer(data):
    best_scenic_score = 0
    for x in range(1, len(data) - 1):
        for y in range(1, len(data[x]) - 1):
            height = data[x][y]

            left = data[x][:y][::-1]
            right = data[x][y+1:]
            up = [data[i][y] for i in range(0, x)][::-1]
            down = [data[i][y] for i in range(x + 1, len(data[x]))]

            down_index = get_distance(down, height)
            up_index = get_distance(up, height)
            left_index = get_distance(left, height)
            right_index = get_distance(right, height)

            scenic_score = left_index * right_index * up_index * down_index
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score

    return best_scenic_score


if __name__ == "__main__":
    data = get_data("./data/day8_input.txt")
    print(f"Part 1: {get_part1_answer(data)}")
    print(f"Part 2: {get_part2_answer(data)}")
