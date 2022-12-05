from day5 import locate, get_seat_id


def test_part1_examples():
    seat_token = "FBFBBFFRLR"

    assert locate(seat_token[:-3]) == 44
    assert locate(seat_token[-3:], upper=7, upper_char="L", lower_char="R") == 5

    assert get_seat_id(seat_token) == 357

    assert get_seat_id("BFFFBBFRRR") == 567
    assert get_seat_id("FFFBBBFRRR") == 119
    assert get_seat_id("BBFFBBFRLL") == 820
