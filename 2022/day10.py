def get_data(filename):
    with open(filename) as input_file:
        return [l.strip() for l in input_file.readlines()]


def get_part1_answer(data):
    register = 1
    cycle_count = 0
    cycle_to_consider = 20
    strength = 0

    for line in data:
        duration = 2 if line != "noop" else 1

        if cycle_count + duration >= cycle_to_consider:
            # print(f"Signal strength: {cycle_to_consider * register}")
            strength += cycle_to_consider * register
            cycle_to_consider += 40

        cycle_count += duration

        if line != "noop":
            register += int(line.split()[1])

    return strength


def get_part2_answer(data):
    register = 1
    cycle_count = 0
    complete = False
    changes = {}
    sprite = 1

    for line in data:
        duration = 2 if line != "noop" else 1

        cycle_count += duration

        if line != "noop":
            register += int(line.split()[1])
            changes[cycle_count] = register

    # print(changes)

    image = ""

    for i in range(240):
        col = i % 40
        row = int(i / 40)

        if i in changes:
            sprite = changes[i]

        if col in range(sprite - 1, sprite + 2):
            image += "#"
        else:
            image += "."

        if col == 39:
            image += "\n"
    return image


if __name__ == "__main__":
    data = get_data("./data/day10_input.txt")
    print(f"Part 1: {get_part1_answer(data)}")
    print("Part 2:\n")
    print(get_part2_answer(data))
