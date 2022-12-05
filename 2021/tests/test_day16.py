import day16


def test_day16_get_data():
    data = day16.get_data("./data/day16_example1.txt")

    assert data == "110100101111111000101000"


def test_day16_parse_header():
    assert day16.parse_header("110100") == (6, 4)
    assert day16.parse_header("001110") == (1, 6)
    assert day16.parse_header("111011") == (7, 3)


def test_parse_literal():
    assert day16.get_part1_answer("110100101111111000101000") == 6


def test_parse_literal_2():
    assert day16.parse_literal("101111111000101") == 2021


def test_parse_sum_literal():
    assert day16.get_part1_answer("11010001010") == 6


def test_parse_operator():
    assert (
        day16.get_part1_answer(
            "00111000000000000110111101000101001010010001001000000000"
        )
        == 1 + 6 + 2
    )


def test_parse_operator_2():
    assert (
        day16.get_part1_answer(
            "11101110000000001101010000001100100000100011000001100000"
        )
        == 7 + 2 + 4 + 1
    )


def test_day16_part1():
    bit_string = day16.get_binary("8A004A801A8002F478")

    assert (
        bit_string
        == "100010100000000001001010100000000001101010000000000000101111010001111000"
    )
    assert day16.get_part1_answer(bit_string) == 16


def test_day16_part1_example_2():
    assert day16.get_part1_answer(day16.get_binary("620080001611562C8802118E34")) == 12


def test_day16_part1_example_3():
    assert (
        day16.get_part1_answer(day16.get_binary("C0015000016115A2E0802F182340")) == 23
    )


def test_day16_part1_example_4():
    assert (
        day16.get_part1_answer(day16.get_binary("A0016C880162017C3686B18A3D4780")) == 31
    )


def test_day16_part2():
    assert day16.get_part2_answer(day16.get_binary("C200B40A82")) == 3
    assert day16.get_part2_answer(day16.get_binary("04005AC33890")) == 54
    assert day16.get_part2_answer(day16.get_binary("880086C3E88112")) == 7
    assert day16.get_part2_answer(day16.get_binary("CE00C43D881120")) == 9
    assert day16.get_part2_answer(day16.get_binary("D8005AC2A8F0")) == 1
    assert day16.get_part2_answer(day16.get_binary("F600BC2D8F")) == 0
    assert day16.get_part2_answer(day16.get_binary("9C005AC2F8F0")) == 0
    assert day16.get_part2_answer(day16.get_binary("9C0141080250320F1802104A08")) == 1
