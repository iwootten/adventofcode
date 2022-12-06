from collections import deque

def get_data(filename):
    with open(filename) as input_file:
        return [a.strip() for a in input_file.readline()]


def get_part1_answer(data):
    characters = deque([], maxlen=4)
    found = None
    for index, c in enumerate(data):
        characters.append(c)
        if len(characters) == 4 and len(set(characters)) == 4:
            found = index + 1
            break
    return found


def get_part2_answer(data):
    characters = deque([], maxlen=14)
    found = None
    for index, c in enumerate(data):
        characters.append(c)
        if len(characters) == 14 and len(set(characters)) == 14:
            found = index + 1
            break
    return found


if __name__ == "__main__":
    data = get_data("./data/day6_input.txt")
    # print(data)
    print(f"Part 1: {get_part1_answer(data)}")
    print(f"Part 2: {get_part2_answer(data)}")
