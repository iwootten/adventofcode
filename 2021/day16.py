def get_data(filename):
    with open(filename) as input_file:
        return get_binary(input_file.readline())


def get_binary(input_string):
    binary_map = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    return "".join([binary_map[c] for c in input_string.strip()])


def parse_header(binary_string):
    version, type = bin_to_dec(binary_string[0:3]), bin_to_dec(binary_string[3:6])

    return version, type


def parse_literal(literal_string):
    chunks = [literal_string[i : i + 5] for i in range(0, len(literal_string), 5)]
    values = []

    print(chunks)
    for c in chunks:
        values.append(c[1:])

        if c[0] == "0":
            break

    return bin_to_dec("".join(values))


def bin_to_dec(binary_string):
    return int(binary_string, 2)


def product(values):
    value = values[0]
    for i in range(len(values) - 1):
        value *= values[i + 1]
    return value


class Parser:

    version_count = 0
    data = ""
    index = 0
    binary_string = ""
    packet_values = []
    operator_stack = []
    operator_map = {
        0: sum,
        1: product,
        2: min,
        3: max,
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1])
    }

    def __init__(self, binary_string):
        self.binary_string = binary_string

    def process_literal(self):
        literal_string = self.binary_string[self.index:]
        print(f"Literal {literal_string}")

        chunks = [literal_string[i: i + 5] for i in range(0, len(literal_string), 5)]
        print(f"Chunks: {chunks}")

        final_chunk_finish = next(
            (
                i + 5
                for i in range(0, len(literal_string), 5)
                if literal_string[i: i + 5][0] == "0"
            )
        )
        value = "".join([literal_string[i + 1: i + 5] for i in range(0, final_chunk_finish, 5)])
        dec_value = bin_to_dec(value)
        print(f"Literal value {bin_to_dec(value)}")
        self.index += final_chunk_finish

        print(f"Index: {self.index}, Length: {len(self.binary_string)}")

        return dec_value

    def process_operator(self, string_type):
        operator_string = self.binary_string[self.index:]
        print(f"Operator {operator_string}")

        length_type = operator_string[0]
        no_of_sub_packets = 0
        packet_values = []

        if length_type == "0":
            # 15-bit number representing number of bits
            no_of_bits = bin_to_dec(operator_string[1:16])
            print(f"15 bit - Sub packet length {no_of_bits}")
            self.index += 16
            final_index = self.index + no_of_bits
            while self.index < final_index:
                no_of_sub_packets += 1
                packet_values.append(self.process_packet())
        else:
            # 11-bit number representing no of sub packets
            no_of_sub_packets = bin_to_dec(operator_string[1:12])
            print(f"11 bit - no of sub-packets {no_of_sub_packets}")

            self.index += 12

            for i in range(no_of_sub_packets):
                packet_values.append(self.process_packet())

        operation = self.operator_map[string_type]
        value = operation(packet_values)
        print(f"Operation ")
        print(f"Operation Value {value}")
        return value

    def process_packet(self):
        print(f"Binary string: {self.binary_string[self.index:]}")
        if int(self.binary_string[self.index:]):
            version, string_type = parse_header(self.binary_string[self.index:])
            self.index += 6
            print(f"Version: {version}, Type {string_type}")

            self.version_count += version

            if string_type == 4:
                return self.process_literal()
            else:
                return self.process_operator(string_type)
        else:
            self.index += len(self.binary_string[self.index:])


def get_part1_answer(data):
    parser = Parser(data)
    parser.process_packet()
    return parser.version_count


def get_part2_answer(data):
    parser = Parser(data)

    return parser.process_packet()


if __name__ == "__main__":
    # part1 = get_part1_answer(get_data("./data/day16_input1.txt"))
    #
    # print(f"Total: {part1}")
    part2 = get_part2_answer(get_data("./data/day16_input1.txt"))

    print(part2)
