def get_data(filename):
    with open(filename) as input_file:
        lines = input_file.readlines()
        numbers_drawn = [int(a) for a in lines[0].split(",")]
        board_section = lines[2:]
        boards = [
            [[int(b) for b in a.strip().split()] for a in board_section[i : i + 5]]
            for i in range(0, len(board_section), 6)
        ]

        return numbers_drawn, boards


def get_board_sum(board):
    return sum(
        [
            board[x][y] if board[x][y] != "x" else 0
            for x in range(0, len(board))
            for y in range(0, len(board[x]))
        ]
    )


def get_part1_answer(numbers_drawn, boards):
    for number in numbers_drawn:
        for index, board in enumerate(boards):
            for x in range(0, len(board)):
                for y in range(0, len(board[x])):
                    if board[x][y] == number:
                        board[x][y] = "x"

                    complete_row = all([a == "x" for a in board[x]])
                    complete_col = all(
                        [board[a][y] == "x" for a in range(0, len(board))]
                    )

                    if complete_col or complete_row:
                        return number, get_board_sum(board)


def get_part2_answer(numbers_drawn, boards):
    board_stack = []
    result_stack = []

    for number in numbers_drawn:
        for index, board in enumerate(boards):
            for x in range(0, len(board)):
                for y in range(0, len(board[x])):
                    if board[x][y] == number:
                        board[x][y] = "x"

                    complete_row = all([a == "x" for a in board[x]])
                    complete_col = all(
                        [board[a][y] == "x" for a in range(0, len(board))]
                    )

                    if (complete_col or complete_row) and (index not in board_stack):
                        board_stack.append(index)
                        result_stack.append((number, get_board_sum(board)))
    return result_stack.pop()


if __name__ == "__main__":
    numbers_drawn, boards = get_data("./data/day4_input1.txt")

    number, board_sum = get_part1_answer(numbers_drawn, boards)

    print(number, board_sum)
    print(number * board_sum)

    number, board_sum = get_part2_answer(numbers_drawn, boards)

    print(number, board_sum)
    print(number * board_sum)
