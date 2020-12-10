import re

def get_data():
    rows = []

    f = open('./input.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows


def get_instruction(row):
    matches = re.findall(r".*([A-Z]).*([A-Z])", row)

    return matches[0][0], matches[0][1]

def get_dependency_map(data):
    transitions = {}

    for row in data:
        transition = get_instruction(row)
        if transition[0] not in transitions:
            transitions[transition[0]] = []
        if transition[1] not in transitions:
            transitions[transition[1]] = []
        transitions[transition[1]] += [transition[0]]
    return transitions

def get_choice(dep_map):
    possible_choices = []
    for start, deps in dep_map.items():
        if len(deps) == 0:
            possible_choices.append(start)
    return sorted(possible_choices)[0]

def remove_choice(dep_map, choice):
    dep_map.pop(choice, None)

    for start, deps in dep_map.items():
        if choice in deps:
            deps.remove(choice)
    return dep_map

data = get_data()
dep_map = get_dependency_map(data)

while len(dep_map):
    choice = get_choice(dep_map)
    dep_map = remove_choice(dep_map, choice)
    print(choice, end="")