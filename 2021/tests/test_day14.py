import day14


def test_day13_get_polymer():
    polymer, pairs = day14.get_data("./data/day14_example1.txt")

    assert day14.get_polymer(polymer, pairs) == "NCNBCHB"
    assert day14.get_polymer(polymer, pairs, step_count=2) == "NBCCNBBBCBHCB"
    assert (
        day14.get_polymer(polymer, pairs, step_count=3) == "NBBBCNCCNBBNBNBBCHBHHBCHB"
    )
    assert (
        day14.get_polymer(polymer, pairs, step_count=4)
        == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    )


def test_day14_get_part1_answer():
    polymer, pairs = day14.get_data("./data/day14_example1.txt")

    assert day14.get_part1_answer(polymer, pairs) == 1588


def test_day14_get_part2_answer():
    polymer, pairs = day14.get_data("./data/day14_example1.txt")

    assert day14.get_min_max_diff(polymer, pairs, step_count=40) == 2188189693529
