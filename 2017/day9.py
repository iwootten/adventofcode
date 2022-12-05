def get_data():
    with open('day9/input.txt', 'r') as content_file:
        content = content_file.read()

    return content


def remove_cancelled(input_data):
    i = 0
    number_cancelled = 0
    data = input_data[:]
    while i < len(data):
        if data[i] == "!" and i + 1 != len(data) - 1:
            number_cancelled += 1
            del data[i + 1]
        i += 1

    return data, number_cancelled


def remove_waste(input_data):
    i = 0
    data = input_data[:]
    characters_removed = 0

    while i < len(data):
        if data[i] == '<':
            j = i + 1
            found = False
            while not found and j < len(data):
                found = data[j] == '>'
                j += 1
            if found:
                characters_removed += (j - 1) - (i + 1)
                del data[i+1:j-1]
        i += 1

    return data, characters_removed


def count_groups(data):
    current_group_number = 0
    current_total = 0

    for char in data:
        if char == '{':
            current_group_number += 1
        if char == '}':
            current_total += current_group_number
            current_group_number -= 1

    return current_total


def step1():
    input_data = list(get_data())
    cancelled_removed, number_cancelled = remove_cancelled(input_data)
    parsed_string, total_removed = remove_waste(cancelled_removed)
    no_of_groups = count_groups(parsed_string)
    print "{}: {}".format(parsed_string, no_of_groups)


def step2():
    input_data = list(get_data())
    cancelled_removed, number_cancelled = remove_cancelled(input_data)
    garbage_removed, total_removed = remove_waste(cancelled_removed)

    print "Original Length: {}".format(len(input_data))
    print "Number Cancelled: {}".format(number_cancelled)
    print "Non cancelled characters removed: {}".format(total_removed - number_cancelled)


step2()
