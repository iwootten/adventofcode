import string

def get_data(filename):
    with open(filename) as input_file:
        return [a.strip() for a in input_file.readlines()]

letters = {v: k for k, v in enumerate(string.ascii_lowercase, start=1)}
letters.update({v: k for k, v in enumerate(string.ascii_uppercase, start=27)})

def get_part1_answer(data):
    input = [list(set(a[0:int(len(a)/2)])&set(a[int(len(a)/2):]))[0] for a in data]

    total = 0
    for item in input:
        total += letters[item]
    return total

def get_part2_answer(data):
    groups = [data[i: i + 3] for i in range(0, len(data), 3)]
    unique = [list(set(group[0]) & set(group[1]) & set(group[2]))[0] for group in groups]

    total = 0
    for item in unique:
        total += letters[item]
    return total

if __name__ == "__main__":
    data = get_data("./data/day3_input.txt")
    print(f"Part 1: {get_part1_answer(data)}")
    print(f"Part 2: {get_part2_answer(data)}")