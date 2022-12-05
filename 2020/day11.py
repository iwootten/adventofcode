def get_data(filename):
    with open(filename) as input_file:
        return [[c for c in a.strip()] for a in input_file.readlines()]

EMPTY = "L"
OCCUPIED = "#"

def get_populated_seat_count(seat_plan):
    seat_count = 0
    for row in seat_plan:
        seat_count += row.count("#")
    return seat_count

def print_matrix(seat_plan):
    for row in seat_plan:
        print("".join([str(x) for x in row]))
    print("")

def get_part1_answer(input_data):
    seat_plan = input_data.copy()
    seats_to_empty, seats_to_occupy = [], []
    max_value = (0,0)
    changes_count = 1

    while changes_count > 0:
        changes_count = 0
        seats_to_empty, seats_to_occupy = [], []
        seat_count = [[0 for x in range(len(seat_plan[0]))] for y in range(len(seat_plan))]

        for x in range(0, len(seat_plan)):
            for y in range(0, len(seat_plan[0])):
                neighbours = [
                    (x-1, y-1), 
                    (x-1, y), 
                    (x-1, y+1),
                    (x, y+1), 
                    (x, y-1), 
                    (x+1, y), 
                    (x+1, y-1), 
                    (x+1, y+1)
                ]
                neighbour_list = filter(lambda n: n[0] >= 0 and n[0] < len(seat_plan) and n[1] >= 0 and n[1] < len(seat_plan[0]), neighbours)
                seat_count[x][y] += sum([1 for n_x, n_y in neighbour_list if seat_plan[n_x][n_y] == OCCUPIED])

                if seat_count[x][y] >= 4 and seat_plan[x][y] == OCCUPIED:
                    seats_to_empty.append((x,y))
                if seat_count[x][y] == 0 and seat_plan[x][y] == EMPTY:
                    seats_to_occupy.append((x, y))

        for x, y in seats_to_empty:
            seat_plan[x][y] = EMPTY
            changes_count += 1
        for x, y in seats_to_occupy:
            seat_plan[x][y] = OCCUPIED
            changes_count += 1

    return get_populated_seat_count(seat_plan)

def get_part2_answer(input_data):
    seat_plan = input_data.copy()
    seats_to_empty, seats_to_occupy = [], []
    max_value = (0,0)
    changes_count = 1

    while changes_count > 0:
        changes_count = 0
        seats_to_empty, seats_to_occupy = [], []
        seat_count = [[0 for x in range(len(seat_plan[0]))] for y in range(len(seat_plan))]

        for x in range(0, len(seat_plan)):
            for y in range(0, len(seat_plan[0])):
                directions = [
                    (-1, -1), 
                    (-1, 0), 
                    (-1, 1),
                    (0, 1), 
                    (0, -1), 
                    (1, 0), 
                    (1, -1), 
                    (1, 1)
                ]
                neighbour_list = []
                
                for dx, dy in directions:
                    magnitude = 1
                    found = False
                    while not found and ((x + dx * magnitude) >= 0) and ((x + dx * magnitude) < len(seat_plan)) and ((y + dy * magnitude) >= 0) and ((y + dy * magnitude) < len(seat_plan[0])):
                        if seat_plan[x + dx * magnitude][y + dy * magnitude] != '.':
                            found = True
                            neighbour_list.append((x + dx * magnitude, y + dy * magnitude))
                        else:
                            magnitude += 1

                seat_count[x][y] += sum([1 for n_x, n_y in neighbour_list if seat_plan[n_x][n_y] == OCCUPIED])

                if seat_count[x][y] >= 5 and seat_plan[x][y] == OCCUPIED:
                    seats_to_empty.append((x,y))
                if seat_count[x][y] == 0 and seat_plan[x][y] == EMPTY:
                    seats_to_occupy.append((x, y))

        for x, y in seats_to_empty:
            seat_plan[x][y] = EMPTY
            changes_count += 1
        for x, y in seats_to_occupy:
            seat_plan[x][y] = OCCUPIED
            changes_count += 1

    return get_populated_seat_count(seat_plan)

if __name__ == "__main__":
    input_data = get_data("./data/day11_input1.txt")
    populated_seat_count = get_part2_answer(input_data)

    print(populated_seat_count)