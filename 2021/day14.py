from collections import defaultdict


def get_data(filename):
    with open(filename) as input_file:
        lines = input_file.readlines()

        polymer = lines[0].strip()

        pairs = {l.split("->")[0].strip(): l.split("->")[1].strip() for l in lines[2:]}

        return polymer, pairs


def get_min_max_diff(polymer_in, pairs, step_count=1):
    pair_count = defaultdict(int)
    char_count = defaultdict(int)

    for c in polymer_in:
        char_count[c] += 1

    for i in range(len(polymer_in) - 1):
        pair_count[polymer_in[i : i + 2]] += 1

    for _ in range(step_count):
        for p, count in list(pair_count.items()):
            # print(f"Current pair: {p}, count {count}")
            new_char = pairs[p]

            pair_count[p] -= count
            pair_count[p[0] + new_char] += count
            pair_count[new_char + p[1]] += count

            char_count[new_char] += count

    return max(char_count.values()) - min(char_count.values())


def get_polymer(polymer_in, pairs, step_count=1):
    polymer_out = str(polymer_in)

    for _ in range(step_count):
        insertion_offset = 0
        for j in range(len(polymer_out) - 1):
            pair = polymer_out[j + insertion_offset : j + 2 + insertion_offset]
            if pair in pairs:
                polymer_out = (
                    polymer_out[: j + 1 + insertion_offset]
                    + pairs[pair]
                    + polymer_out[j + 1 + insertion_offset :]
                )
                insertion_offset += len(pairs[pair])
    return polymer_out


def get_part1_answer(polymer_in, pairs):
    polymer = get_polymer(polymer_in, pairs, step_count=10)

    freq = [polymer.count(c) for c in set(polymer)]

    return max(freq) - min(freq)


def get_part2_answer(polymer_in, pairs):
    polymer = get_polymer(polymer_in, pairs, step_count=40)

    freq = [polymer.count(c) for c in set(polymer)]

    return max(freq) - min(freq)


if __name__ == "__main__":
    polymer, pairs = get_data("./data/day14_input1.txt")

    print(get_min_max_diff(polymer, pairs, step_count=40))
