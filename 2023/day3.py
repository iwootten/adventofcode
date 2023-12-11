def get_data(filename):
    with open(filename) as input_file:
        return input_file.readlines()

def parse_data(data):
    symbols = []
    numbers = []
    for y, line in enumerate(data):
        for x, value in enumerate(line.strip()):
            if value.isdigit():
                if x > 0 and line[x - 1].isdigit():
                    numbers[-1].append((x, y))
                else:
                    numbers.append([(x, y)])
            elif value != '.':
                symbols.append((x, y))
    return numbers, symbols


def get_part1_answer(data):
    numbers, symbols = parse_data(data)
    invalid_numbers = []

    tests = []
    for x, y in symbols:
        tests.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1),
         (x + 1, y + 1)])

    for number_group in numbers:
        hit = any([test in number_group for test in tests])
        if not hit:
            invalid_numbers.append(number_group)

    valid_numbers = numbers.copy()

    for n in invalid_numbers:
        valid_numbers.remove(n)
    
    results = []
    for group in valid_numbers:
        group_values = []
        for x, y in group:
            group_values.append(data[y][x])
        results.append(int("".join(group_values)))

    return sum(results)  


def get_part2_answer(data):
    possible_gears = []
    numbers, _ = parse_data(data)

    for y, line in enumerate(data):
        for x, value in enumerate(line.strip()):
            if value == "*":
                possible_gears.append((x, y))
    print(possible_gears)
    
    gear_groups = []
    for possible_gear in possible_gears:
        x, y = possible_gear
        found = []
        possible_positions = [
            (x - 1, y), 
            (x + 1, y), 
            (x, y - 1), 
            (x, y + 1), 
            (x - 1, y - 1), 
            (x - 1, y + 1), 
            (x + 1, y - 1), 
            (x + 1, y + 1)
        ]
        for number_group in numbers:
            for possible_position in possible_positions:
                if possible_position in number_group:
                    found.append(number_group)
                    break
    
        if len(found) == 2:
            gear_groups.append(found)
            print(f"Found a gear group at {possible_gear}, {found}")

    print(gear_groups)

    results = []
    for group in gear_groups:
        ratio = 1
        for group_row in group:
            group_values = []
            for x, y in group_row:
                group_values.append(data[y][x])
            print(int("".join(group_values)))
            ratio *= int("".join(group_values))
        results.append(ratio)
    
    return sum(results)



if __name__ == "__main__":
    input_data = get_data("./data/day3_input.txt")
    print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")
