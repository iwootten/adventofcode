from collections import defaultdict

def get_data(filename):
    with open(filename) as input_file:
        return [a.strip() for a in input_file.readlines()]

def get_directory_map(data):
    path = "/"

    totals = defaultdict(int)

    for i, line in enumerate(data[1:]):
        args = line.split()

        if args[0] == "$":
            if args[1] == "cd" and args[2] == "..":
                elements = [e for e in path.split("/")[:-1] if e]
                path = "/" + "/".join(elements)
            elif args[1] == "cd":
                path = path + "/" + args[2] if path != "/" else "/" + args[2]
        elif args[0] != "dir":
            totals[path] += int(args[0])

            parent_path_bits = path.split("/")[:-1]
            for path_bit_index in range(0, len(parent_path_bits)):
                parent_path = "/" + "/".join(parent_path_bits[:path_bit_index + 1]).lstrip("/")
                if parent_path != path:
                    totals[parent_path] += int(args[0])
    return totals

def get_part1_answer(data):
    total = 0
    dir_map = get_directory_map(data)
    for _, dir_size in dir_map.items():
        if dir_size <= 100000:
            total += dir_size
    return total


def get_part2_answer(data):
    dir_map = get_directory_map(data)
    
    limit = 30000000 - (70000000 - dir_map['/'])
    for path, value in sorted(dir_map.items(), key=lambda item: item[1]):
        if value > limit:
            return value


if __name__ == "__main__":
    data = get_data("./data/day7_input.txt")
    # print(data)
    print(f"Part 1: {get_part1_answer(data)}")
    print(f"Part 2: {get_part2_answer(data)}")
