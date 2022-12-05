def diff_checksum(row):
    checksum = 0

    code_digits = [int(n) for n in row.split()]

    minimum = min(code_digits)
    maximum = max(code_digits)

    checksum += maximum - minimum

    return checksum


def divide_checksum(row):
    code_digits = [int(n) for n in row.split()]

    for index_a, a in enumerate(code_digits):
        for index_b, b in enumerate(code_digits):
            if index_a != index_b and a % b == 0 :
                print "Found a: {} b: {}".format(a, b)
                return a / b if a > b else b / a


with open('day2/input.txt', 'r') as content_file:
    total = 0
    for row in content_file.readlines():
        total += divide_checksum(row)
    print total
