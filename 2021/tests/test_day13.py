from day13 import get_data, get_part1_answer, get_matrix, fold_matrix


def test_day13_part1():
    positions, folds = get_data("./data/day13_example1.txt")

    matrix = get_matrix(positions)

    answer = get_part1_answer(positions, folds[0])

    assert answer == 17
