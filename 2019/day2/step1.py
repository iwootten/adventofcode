def get_list():
    f = open('./input.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows


def process_code(number_list):
    instruction_pointer = 0

    while instruction_pointer < len(number_list):
        opcode = number_list[instruction_pointer]
        position_1 = number_list[instruction_pointer + 1]
        position_2 = number_list[instruction_pointer + 2]
        output_position = number_list[instruction_pointer + 3]

        if opcode == 99:
            break
        elif opcode == 1:
            number_list[output_position] = number_list[position_1] + number_list[position_2]
        elif opcode == 2:
            number_list[output_position] = number_list[position_1] * number_list[position_2]

        instruction_pointer += 4

    return number_list


def test_opcodes():
    assert process_code("1,0,0,0,99") == "2,0,0,0,99"
    assert process_code("2,3,0,3,99") == "2,3,0,6,99"
    assert process_code("2,4,4,5,99,0") == "2,4,4,5,99,9801"
    assert process_code("1,1,1,4,99,5,6,0,99") == "30,1,1,4,2,5,6,0,99"
    assert process_code("1,9,10,3,2,3,11,0,99,30,40,50") == "3500,9,10,70,2,3,11,0,99,30,40,50"


def try_noun_verb(number_list, noun, verb):
    number_list[1] = noun
    number_list[2] = verb
    new_list = process_code(number_list)
    return ",".join([str(n) for n in new_list])


number_row = get_list()[0]
number_list_a = [int(n) for n in number_row.split(',')]

print(try_noun_verb(number_list_a, 12, 2))
print(try_noun_verb(number_list_a, 10, 3))

