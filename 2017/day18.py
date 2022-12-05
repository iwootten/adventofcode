def get_data(filename):
    commands = []

    with open('day18/{}'.format(filename), 'r') as content_file:
        for command in content_file.readlines():
            args = command.strip("\n").split(" ")

            if len(args) == 3:
                try:
                    args[2] = int(args[2])
                except ValueError:
                    pass

            commands.append({'action': args[0], 'args': args[1:]})

    return commands


def run_set(registers, x, y):
    registers[x] = y if type(y) == int else registers[y]
    return registers


def add(registers, x, y):
    registers[x] +=y if type(y) == int else registers[y]
    return registers


def mul(registers, x, y):
    registers[x] *= y if type(y) == int else registers[y]
    return registers


def mod(registers, x, y):
    registers[x] %= y if type(y) == int else registers[y]
    return registers


def process_actions(commands):
    current_command_index = 0
    last_sound = 0
    names = list(set([c['args'][0] for c in commands]))
    registers = {n: 0 for n in names}

    while current_command_index < len(commands):
        offset = False
        action = commands[current_command_index]['action']
        args = commands[current_command_index]['args']
        #
        print action, args

        if action == 'snd':
            last_sound = registers[args[0]]
        elif action == 'rcv':
            if registers[args[0]] != 0:
                print last_sound
                import pdb; pdb.set_trace()
        elif action == 'set':
            registers = run_set(registers, args[0], args[1])
        elif action == 'add':
            registers = add(registers, args[0], args[1])
        elif action == 'mul':
            registers = mul(registers, args[0], args[1])
        elif action == 'mod':
            registers = mod(registers, args[0], args[1])
        elif action == 'jgz':
            args[1] = args[1] if type(args[1]) == int else registers[args[1]]
            if registers[args[0]] > 0:
                current_command_index += args[1]
                offset = True

        print registers
        if not offset:
            current_command_index += 1


def other_program(current_program):
    return current_program = 1 if current_program == 0 else 0

def process_threads(commands):
    current_command_index = [0, 0]
    names = list(set([c['args'][0] for c in commands]))

    current_program = 0

    a_registers = {n: 0 for n in names}
    b_registers = {n: 0 if n != 'p' else 1 for n in names}

    registers = [a_registers, b_registers]

    program_queue = [[], []]

    while current_command_index[current_program] < len(commands):
        offset = False
        action = commands[current_command_index[current_program]]['action']
        args = commands[current_command_index[current_program]]['args']
        #
        print action, args

        if action == 'snd':
            program_queue[current_program].append(registers[current_program][args[0]])
        elif action == 'rcv':
            if registers[current_program][args[0]] != 0:
                registers[current_program][args[0]]
        elif action == 'set':
            registers[current_program] = run_set(registers[current_program], args[0], args[1])
        elif action == 'add':
            registers[current_program] = add(registers[current_program], args[0], args[1])
        elif action == 'mul':
            registers[current_program] = mul(registers[current_program], args[0], args[1])
        elif action == 'mod':
            registers[current_program] = mod(registers[current_program], args[0], args[1])
        elif action == 'jgz':
            args[1] = args[1] if type(args[1]) == int else registers[current_program][args[1]]
            if registers[args[0]] > 0:
                current_command_index += args[1]
                offset = True

        print registers
        if not offset:
            current_command_index[current_program] += 1

        current_program = other_program(current_program)


def example1():
    commands = get_data("train.txt")
    process_actions(commands)


def part1():
    commands = get_data("input.txt")
    process_actions(commands)


def example2():
    commands = get_data("train.txt")
    process_threads(commands)

part1()
