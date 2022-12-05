from day4 import get_part1_answer, check_field, get_data, get_part2_answer


def test_day4_part1():
    data = get_data("./data/day4_example.txt")
    answer = get_part1_answer(data)
    assert answer == 2


def test_day4_part2():
    data = get_data("./data/day4_example2.txt")
    answer = get_part2_answer(data)
    assert answer == 0


def test_day4_field_map():
    assert check_field("byr", "2002")
    assert not check_field("byr", "2003")

    assert check_field("hgt", "60in")
    assert check_field("hgt", "190cm")
    assert not check_field("hgt", "190in")
    assert not check_field("hgt", "190")

    assert check_field("hcl", "#123abc")
    assert not check_field("hcl", "#123abz")
    assert not check_field("hcl", "123abc")

    assert check_field("ecl", "brn")
    assert not check_field("ecl", "wat")

    assert check_field("pid", "000000001")
    assert not check_field("pid", "0123456789")


def test_day4_part2_2():
    data = get_data("./data/day4_example3.txt")
    answer = get_part2_answer(data)
    assert answer == 4
