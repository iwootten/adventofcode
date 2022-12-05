def get_data(filename):
    with open(filename) as input_file:
        return [[int(i) for i in list(line.strip())] for line in input_file.readlines()]


def get_part1_answer(input_data, iterations=1):
    processed_data = input_data.copy()
    directions = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
    flash_count = 0

    for i in range(iterations):
        flash_stack, processed_stack = [], []
        for x in range(len(processed_data)):
            for y in range(len(processed_data[0])):
                processed_data[x][y] += 1
                if processed_data[x][y] > 9:
                    flash_stack.append((x, y))
                    processed_stack.append((x, y))

        while flash_stack:
            x, y = flash_stack.pop()
            neighbours = [
                (x + dx, y + dy)
                for dx, dy in directions
                if ((x + dx) >= 0)
                and ((x + dx) < len(processed_data))
                and ((y + dy) >= 0)
                and ((y + dy) < len(processed_data[0]))
            ]
            for nx, ny in neighbours:
                processed_data[nx][ny] += 1
                if processed_data[nx][ny] > 9 and (nx, ny) not in processed_stack:
                    flash_stack.append((nx, ny))
                    processed_stack.append((nx, ny))

        for x, y in processed_stack:
            processed_data[x][y] = 0
            flash_count += 1

    return processed_data, flash_count


def get_part2_answer(input_data):
    processed_data = input_data.copy()
    directions = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
    flash_count = 0
    synced = False
    k = 0

    while not synced:
        flash_stack, processed_stack = [], []
        k += 1
        for x in range(len(processed_data)):
            for y in range(len(processed_data[0])):
                processed_data[x][y] += 1
                if processed_data[x][y] > 9:
                    flash_stack.append((x, y))
                    processed_stack.append((x, y))

        while flash_stack:
            x, y = flash_stack.pop()
            neighbours = [
                (x + dx, y + dy)
                for dx, dy in directions
                if ((x + dx) >= 0)
                and ((x + dx) < len(processed_data))
                and ((y + dy) >= 0)
                and ((y + dy) < len(processed_data[0]))
            ]
            for nx, ny in neighbours:
                processed_data[nx][ny] += 1
                if processed_data[nx][ny] > 9 and (nx, ny) not in processed_stack:
                    flash_stack.append((nx, ny))
                    processed_stack.append((nx, ny))

        for x, y in processed_stack:
            processed_data[x][y] = 0
            flash_count += 1

        synced = sum([sum(processed_data[x]) for x in range(len(processed_data))]) == 0

    return k


if __name__ == "__main__":
    input_data = get_data("./data/day11_input1.txt")

    # _, part1 = get_part1_answer(input_data, 10)
    part2 = get_part2_answer(input_data)

    # print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
