def get_data(filename):
    with open(filename) as input_file:
        return [list(line.strip()) for line in input_file.readlines()]


ILLEGAL_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTO_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
MATCHING = {"(": ")", "{": "}", "[": "]", "<": ">"}


def get_illegal_chars(input_data):
    illegals = []
    for line in input_data:
        chunks = []
        for c in line:
            if c in ["(", "[", "{", "<"]:
                chunks.append(c)
            else:
                opening = chunks.pop()

                if c != MATCHING[opening]:
                    illegals.append(ILLEGAL_SCORES[c])
    return illegals


def get_part1_answer(input_data):
    return sum(get_illegal_chars(input_data))


def get_valid_lines(input_data):
    valid_lines = [i for i in range(len(input_data))]

    for i in range(len(input_data)):
        chunks = []
        for c in input_data[i]:
            if c in ["(", "[", "{", "<"]:
                chunks.append(c)
            else:
                if c != MATCHING[chunks.pop()]:
                    valid_lines.remove(i)
    return valid_lines


def get_autocomplete(line):
    chunks = []
    to_complete = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            chunks.append(c)
        else:
            chunks.pop()
    while chunks:
        to_complete.append(MATCHING[chunks.pop()])
    return to_complete


def get_part2_answer(input_data):
    valid_lines = [input_data[i] for i in get_valid_lines(input_data)]
    totals = []

    for line in valid_lines:
        total = 0
        for c in get_autocomplete(line):
            total = total * 5 + AUTO_SCORES[c]
        totals.append(total)
    totals.sort()

    return totals[int(len(totals) / 2)]


if __name__ == "__main__":
    input_data = get_data("./data/day10_input1.txt")

    part1 = get_part1_answer(input_data)
    part2 = get_part2_answer(input_data)

    print(part1)
    print(part2)
