def get_data(filename):
    with open(filename) as input_file:
        data = []
        for a in input_file.readlines():
            _, games_str = a.strip().split(':')
    
            games = [{c.strip().split(' ')[1]: int(c.strip().split(' ')[0]) for c in b.strip().split(',')} for b in games_str.split(';')]

            data.append(games)
        return data


def get_part1_answer(data):
    test_data = {'red': 12, 'green':13, 'blue': 14}
    successful = []
    for i, games in enumerate(data):
        games_success = True
        print(games)
        for game in games:
            game_success = [v >= game[k] for k, v in test_data.items() if k in game]
            games_success &= all(game_success)
            print(games_success)

        if games_success:
            successful.append(i+1)
    
    for i in successful:
        print(f"Game {i+1} is a {'success' if games_success else 'failure'}")
    return sum(successful)


def get_part2_answer(data):
    powers = []
    for i, games in enumerate(data):
        max_values = {}
        for game in games:
            for k, v in game.items():
                if v > max_values.get(k, 0):
                    max_values[k] = v

        values = list(max_values.values())

        power = 1
        for v in values:
            power *= v
        powers.append(power)
            
    return sum(powers)




if __name__ == "__main__":
    input_data = get_data("./data/day2_input.txt")
    print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")
