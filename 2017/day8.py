from __future__ import print_function
import re


def get_data():
    operations = []
    registers = {}

    with open('day8/input.txt', 'r') as content_file:
        pattern = re.compile(r"""(?P<name>.*)\s(?P<operator>(inc|dec))\s(?P<increment_value>\-?[0-9]+)\sif\s(?P<condition_name>.*)\s(?P<comparator>[<=>!]+)\s(?P<comparator_value>\-?[0-9]+)""", re.VERBOSE)

        for row in content_file.readlines():
            match = pattern.match(row)

            registers[match.group('name')] = 0

            operations.append({
                'name': match.group("name"),
                'operator': match.group("operator"),
                'increment_value': int(match.group("increment_value")),
                'condition_name': match.group("condition_name"),
                'comparator': match.group("comparator"),
                'comparator_value': int(match.group("comparator_value"))
            })

    return registers, operations


def process_condition(register_value, comparator, comparator_value):
    comparator_map = {
        ">": register_value > comparator_value,
        "<": register_value < comparator_value,
        ">=": register_value >= comparator_value,
        "<=": register_value <= comparator_value,
        "==": register_value == comparator_value,
        "!=": register_value != comparator_value,
    }

    return comparator_map[comparator]


def process_operations(input_registers, input_operations):
    max_value = -9999

    for operation in input_operations:
        print("{} {} {} if {} {} {}".format(operation['name'], operation['operator'], operation['increment_value'],
                                      operation['condition_name'], operation['comparator'], operation['comparator_value']))

        modify_value = -operation['increment_value'] if operation['operator'] == 'dec' else operation['increment_value']
        register_value = input_registers[operation['condition_name']]
        condition_result = process_condition(register_value, operation['comparator'],  operation['comparator_value'])

        print("Condition result: {}, {} {} by {}".format(condition_result, "Modifying" if condition_result else "Not modifying",
                                                         operation['name'], modify_value))

        if condition_result:
            input_registers[operation['name']] += modify_value
            max_value = input_registers[operation['name']] if max_value < input_registers[operation['name']]  else max_value

    return input_registers, max_value


registers, operations = get_data()

print("{} Registers, {} Steps\n".format(len(registers.keys()), len(operations)))
final_registers, max_value = process_operations(registers, operations)

print("\nHighest ever value was: {}".format(max_value))
print("Final Max value is: {}".format(max(final_registers.values())))
