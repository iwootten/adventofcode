def get_data(filename):
    with open(filename) as input_file:
        return [a.strip().split() for a in input_file.readlines()]

RULES = {
    "RS": 0,
    "SP": 0,
    "PR": 0,
    "SR": 1,
    "PS": 1,
    "RP": 1,
}
their_map = {
    "A": "R",
    "B": "P",
    "C": "S"
}
my_map = {
    "X": "R",
    "Y": "P",
    "Z": "S"
}

def get_part1_answer(data):
    total = 0
    for their_move, my_move in data:
        total += list(my_map.keys()).index(my_move) + 1

        if their_map[their_move] != my_map[my_move]:
            winner = RULES[f"{their_map[their_move]}{my_map[my_move]}"]
            # print(f"Outcome: {winner}")
            if winner == 1:
                total += 6
        else:
            # print("Outcome: Draw")
            total += 3
    return total

def get_part2_answer(data):
    total = 0
    for their_move, outcome in data:
        if outcome == "X":
            my_move = [r[1] for r in list(RULES.keys())[0:3] if r[0] == their_map[their_move]][0]
        if outcome == "Y":
            my_move = their_map[their_move]
        if outcome == "Z":
            my_move = [r[1] for r in list(RULES.keys())[3:6] if r[0] == their_map[their_move]][0]

        print(f"My Move {my_move}")
        total += list(my_map.values()).index(my_move) + 1

        if their_map[their_move] != my_move:
            winner = RULES[f"{their_map[their_move]}{my_move}"]
            # print(f"Outcome: {winner}")
            if winner == 1:
                total += 6
        else:
            # print("Outcome: Draw")
            total += 3
    return total
if __name__ == "__main__":
    data = get_data("./data/day2_input.txt")
    print(f"Part2: {get_part2_answer(data)}")