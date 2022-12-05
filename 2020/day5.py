def get_data(filename):
    with open(filename) as input_file:
        for line in input_file.readlines():
            yield line.rstrip("\n")


def locate(specifier, lower=0, upper=127, upper_char="F", lower_char="B"):
    for c in list(specifier):
        diff = round((upper - lower + 1) / 2)
        lower = lower + diff if c == lower_char else lower
        upper = upper - diff if c == upper_char else upper

    return lower if lower == upper else None


def get_seat_id(seat_token):
    row, col = locate(seat_token[:-3]), locate(
        seat_token[-3:], upper=7, upper_char="L", lower_char="R"
    )

    return row * 8 + col


def find_missing_id(seats):
    return [seat for seat in range(min(seats), max(seats)) if seat not in seats][0]


if __name__ == "__main__":
    input_data = get_data("./data/day5_input1.txt")

    seat_ids = [get_seat_id(token) for token in input_data]

    print(f"Part1: {max(seat_ids)}")

    missing = find_missing_id(seat_ids)

    print(f"Part2: {missing}")
