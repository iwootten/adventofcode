def get_data(filename):
    with open(filename) as input_file:
        return [[[int(c) for c in group.split("-")] for group in a.strip().split(",")] for a in input_file.readlines()]

def get_part1_answer(data):
    total = 0

    for elf_group in data:
        elf_a = elf_group[0]
        elf_b = elf_group[1]
        a_min = elf_a[0]
        a_max = elf_a[1]
        b_min = elf_b[0]
        b_max = elf_b[1]

        total += (b_min >= a_min and b_max <= a_max) or (a_min >= b_min and a_max <= b_max)
    return total

def get_part2_answer(data):
    total = 0

    for elf_group in data:
        elf_a = set(list(range(elf_group[0][0], elf_group[0][1] + 1)))
        elf_b = set(list(range(elf_group[1][0], elf_group[1][1] + 1)))

        total += len(elf_a & elf_b) > 0
    return total

if __name__ == "__main__":
    data = get_data("./data/day4_input.txt")
    print(f"Part 1: {get_part1_answer(data)}")
    print(f"Part 2: {get_part2_answer(data)}")