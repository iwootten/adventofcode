def generator(last_value, factor):
    return (last_value * factor) % 2147483647

def picky_generator(last_value, factor, multiple):
    current_value = generator(last_value, factor)

    while current_value % multiple != 0:
        current_value = generator(current_value, factor)

    return current_value

def part1():
    count = 0
    current_value_a = 618
    current_value_b = 814

    for i in range(40000000):
        current_value_a = generator(current_value_a, 16807)
        current_value_b = generator(current_value_b, 48271)

        # print "{} : {}".format(current_value_a, current_value_b)

        binary_val_a = str(bin(current_value_a)[2:].zfill(32))
        binary_val_b = str(bin(current_value_b)[2:].zfill(32))

        # print binary_val_a
        # print binary_val_b

        count += 1 if binary_val_a[-16:] == binary_val_b[-16:] else 0

    print "Total: {}".format(count)

def part2():
    count = 0
    current_value_a = 618
    current_value_b = 814

    for i in range(5000000):
        current_value_a = picky_generator(current_value_a, 16807, 4)
        current_value_b = picky_generator(current_value_b, 48271, 8)

        # print "{} : {}".format(current_value_a, current_value_b)

        binary_val_a = str(bin(current_value_a)[2:].zfill(32))
        binary_val_b = str(bin(current_value_b)[2:].zfill(32))

        # print binary_val_a
        # print binary_val_b

        count += 1 if binary_val_a[-16:] == binary_val_b[-16:] else 0

    print "Total: {}".format(count)

part2()

