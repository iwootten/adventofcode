import re

def get_data(filename):
    with open(filename) as input_file:
        return [a.strip() for a in input_file.readlines()]


def get_part1_answer(data):
    numbers = [''.join(b for b in a if b.isdigit()) for a in data]
    answer = [int(a[0] + a[-1]) for a in numbers]

    return sum(answer)


def get_part2_answer(data):
    num_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    numbers = []
    for l in data:
        positions = [i for i, c in enumerate(l.strip()) if c.isdigit()]

        earliest_position = min(positions) if positions else len(l)
        latest_position = max(positions) if positions else -1

        earliest_word = len(l)
        earliest_value = 0
        latest_word = -1
        latest_value = 0

        for k in num_map.keys():
            if k in l and earliest_word > l.find(k):
                earliest_word = l.find(k)
                earliest_value = num_map[k]

        for k in num_map.keys():
            if k in l and latest_word < l.rfind(k):
                latest_word = l.rfind(k)
                latest_value = num_map[k]
        
        earliest = l[earliest_position] if earliest_position < earliest_word else int(earliest_value)
        latest = l[latest_position] if latest_position > latest_word else int(latest_value)

        numbers.append([int(earliest), int(latest)])

    answer = [int(str(a[0]) + str(a[-1])) for a in numbers]

    return sum(answer)




if __name__ == "__main__":
    input_data = get_data("./data/day1_input.txt")
    # print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")
