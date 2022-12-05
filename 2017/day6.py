from __future__ import print_function


def increment_index(bank_length, current_index, increment):
    return current_index + increment if current_index < bank_length - 1 else 0


def cycle(memory_banks):
    block_to_reallocate = max(memory_banks)
    largest_index = memory_banks.index(block_to_reallocate)

    memory_banks[largest_index] = 0

    current_index = increment_index(len(memory_banks), largest_index, 1)

    while 0 < block_to_reallocate:
        memory_banks[current_index] += 1

        current_index = increment_index(len(memory_banks), current_index, 1)
        block_to_reallocate -= 1
    return memory_banks


def print_memory_banks(memory_banks):
    for item in memory_banks:
        print("{}\t".format(item), end='')
    print("")


puzzle_input = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
cycle_log = ["0,2,7,0"]
banks = [0, 2, 7, 0]
i = 1
cycle_result = ""

while cycle_result not in cycle_log:
    if i != 1:
        cycle_log.append(cycle_result)

    print("{}:".format(i))
    print_memory_banks(puzzle_input)
    cycle_result = ",".join([str(n) for n in cycle(puzzle_input)])
    i += 1

initial_cycle_loop = cycle_log.index(cycle_result) + 1

print("{} seen at {} and again at {}, making the loop size {}".format(cycle_result, initial_cycle_loop, i, i - initial_cycle_loop))