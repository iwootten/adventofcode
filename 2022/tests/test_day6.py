from day6 import get_data, get_part1_answer, get_part2_answer


def test_day6_part1():
    answer = get_part1_answer("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    assert answer == 7
    answer = get_part1_answer("bvwbjplbgvbhsrlpgdmjqwftvncz")
    assert answer == 5
    answer = get_part1_answer("nppdvjthqldpwncqszvftbrmjlhg")
    assert answer == 6
    answer = get_part1_answer("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    assert answer == 10
    answer = get_part1_answer("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    assert answer == 11


def test_day6_part2():
    answer = get_part2_answer("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    assert answer == 19
    answer = get_part2_answer("bvwbjplbgvbhsrlpgdmjqwftvncz")
    assert answer == 23
    answer = get_part2_answer("nppdvjthqldpwncqszvftbrmjlhg")
    assert answer == 23
    answer = get_part2_answer("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    assert answer == 29
    answer = get_part2_answer("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    assert answer == 26
