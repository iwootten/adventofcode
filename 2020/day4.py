import re


def get_data(filename):
    with open(filename) as input_file:
        return [
            [field.split(":") for field in line.replace("\n", " ").split(" ")]
            for line in input_file.read().split("\n\n")
        ]


def get_part1_answer(data):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0
    for line_fields in data:
        valid += all(
            [
                required in [field[0] for field in line_fields]
                for required in required_fields
            ]
        )
    return valid


def check_field(field_name, value):
    field_map = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hgt": lambda x: 150 <= int(x[0:-2]) <= 193
        if x[-2:] in ["cm", "in"] and x[-2:] == "cm"
        else 59 <= int(x[0:-2]) <= 76
        if x[0:-2]
        else False,
        "hcl": lambda x: re.compile("^#([0-9]|[a-f]){6}$").match(x) is not None,
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda x: re.compile("^[0-9]{9}$").match(x) is not None,
    }
    return field_map[field_name](value)


def get_part2_answer(data):
    count = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for line_fields in data:
        valid = all(
            [
                required in [field[0] for field in line_fields]
                for required in required_fields
            ]
        )
        for field in line_fields:
            valid &= True if field[0] == "cid" else check_field(field[0], field[1])
        count += valid

    return count


if __name__ == "__main__":
    input_data = get_data("./data/day4_input1.txt")
    part1_answer = get_part1_answer(input_data)
    part2_answer = get_part2_answer(input_data)

    print(f"Part1: {part1_answer}")
    print(f"Part2: {part2_answer}")
