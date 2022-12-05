from day5 import get_data, empty_matrix, process_data, intersect_count


def test_day5_part1():
    vectors = get_data("./data/day5_example1.txt")

    empty = empty_matrix(vectors)
    complete_matrix = process_data(vectors, empty)
    answer = intersect_count(complete_matrix, 2)
    assert answer == 5


def test_day5_part2():
    vectors = get_data("./data/day5_example1.txt")

    empty = empty_matrix(vectors)
    complete_matrix = process_data(vectors, empty, diagonals=True)
    answer = intersect_count(complete_matrix, 2)
    print(complete_matrix)
    assert answer == 12
