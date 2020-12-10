import re
import string

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

def get_choice(dep_map, assigned):
    possible_choices = [k for k, deps in dep_map.items() if len(deps) == 0]
    filtered = [k for k in possible_choices if k not in assigned]
    if len(filtered) == 0:
        return
    return sorted(filtered)[0]

def remove_choice(dep_map, choice):
    dep_map.pop(choice, None)

    for start, deps in dep_map.items():
        if choice in deps:
            deps.remove(choice)
    return dep_map

def being_worked_on(worker_pool, task):
    return task in [w['working_on'] for w in worker_pool]

def next_free(worker_pool):
    return next(iter([i for i, w in enumerate(worker_pool) if w['working_on'] == False]), False)

def working_on(worker):
    return worker['working_on'] if worker['working_on'] else '.'

data = get_data()
dep_map = get_dependency_map(data)
worker_pool = [{
    'working_on': False,
    'ends': -1
} for x in range(5)]
step_duration = 60
choice_string = ''
done = ''
clock = 0
assigned = []

while len(dep_map):
    for worker_index, worker in enumerate(worker_pool):
        # End workers finishing now
        if worker['ends'] <= clock and worker['ends'] > 0:
            to_remove = worker_pool[worker_index]['working_on']
            worker_pool[worker_index] = {
                'working_on': False,
                'ends': -1
            }
            dep_map = remove_choice(dep_map, to_remove)
            done += to_remove
            assigned.remove(to_remove)

    for worker_index, worker in enumerate(worker_pool):
        choice = get_choice(dep_map, assigned)
        # import pdb; pdb.set_trace()
        if choice:
            choice_duration = string.ascii_uppercase.index(choice) + step_duration + 1
            if not worker['working_on'] and not being_worked_on(worker_pool, choice):
                choice_string += choice

                worker_pool[worker_index]['working_on'] = choice
                worker_pool[worker_index]['ends'] = clock + choice_duration

                assigned.append(choice)
    print("{}\t".format(clock), end="")
    for i in range(len(worker_pool)):
        print("\t{}".format(working_on(worker_pool[i])), end="")
    print("\t{}".format(done))
    clock += 1

correct ='CABFDE'
print(done == correct)
print("Correct: {}".format(correct))
print("Actual: {}".format(done))
print(clock - 1)

