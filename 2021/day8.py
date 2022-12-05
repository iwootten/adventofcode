def get_data(filename):
    with open(filename) as input_file:
        return [
            (line.split("|")[0].split(), line.split("|")[1].split())
            for line in input_file.readlines()
        ]


DIGIT_LENGTHS = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}


def get_part1_answer(input_data):
    return sum(
        [1 for _, output in input_data for item in output if len(item) in DIGIT_LENGTHS]
    )


def get_signal_map(signal):
    digits = {}

    for item in signal:
        if len(item) in DIGIT_LENGTHS:
            digits[DIGIT_LENGTHS[len(item)]] = item

    for item in signal:
        if len(item) == 5:
            if len(set(item) & set(digits[4])) == 2:
                digits[2] = item
            elif len(set(item) & set(digits[4]) & set(digits[1])) == 2:
                digits[3] = item
            elif len(set(item) & set(digits[4]) & set(digits[1])) == 1:
                digits[5] = item

        if len(item) == 6:
            if len(set(item) & set(digits[4])) == 4:
                digits[9] = item
            elif len(set(item) & set(digits[4]) & set(digits[1])) == 2:
                digits[0] = item
            elif len(set(item) & set(digits[4]) & set(digits[1])) == 1:
                digits[6] = item
    return digits


def get_part2_answer(input_data):
    # fives = [2, 3, 5]
    # sixes = [0, 6, 9]
    total = 0

    for signal, output in input_data:
        digits = get_signal_map(signal)

        final_value = ""

        for item in output:
            for k, v in digits.items():
                if len(item) == len(v) and (len(set(v) & set(item)) == len(item)):
                    final_value += str(k)
        total += int(final_value)
    return total


if __name__ == "__main__":
    input_data = get_data("./data/day8_input1.txt")

    part2 = get_part2_answer(input_data)

    print(part2)
