from collections import defaultdict
import math


def get_data(filename):
    with open(filename) as input_file:
        data = []
        for l in input_file.readlines():
            start, ours = l.strip().split("|")
            _, winning = start.strip().split(":")

            data.append(({int(w) for w in winning.strip().split()}, {int(o) for o in ours.strip().split()}))

        return data



def get_part1_answer(data):
    matches = [len(winning.intersection(ours)) for winning, ours in data]
    
    points = [math.pow(2, m-1) if m >= 1 else 1 if m==1 else 0 for m in matches]

    return sum(points)


def get_part2_answer(data):
    matches = [winning.intersection(ours) for winning, ours in data]

    copies = defaultdict(int)

    for i, match in enumerate(matches):
        total_instances = copies[i] + 1

        for j in range(i+1, i+len(match)+1):
            copies[j] += total_instances
    
    return sum([copies[i] + 1 for i, _ in enumerate(matches)])

if __name__ == "__main__":
    input_data = get_data("./data/day4_input.txt")
    print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")
