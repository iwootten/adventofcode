import math


def get_data(filename):
    with open(filename) as input_file:
        return [l.strip() for l in input_file.readlines()]


class Monkey:
    worry_stack = []
    operation = ""
    amount = ""
    divisible_by = 0
    monkey_true = 0
    monkey_false = 0
    count = 0

    def __repr__(self) -> str:
        return ",".join([str(c) for c in self.worry_stack])

    def next(self):
        if len(self.worry_stack) == 0:
            return None
        item = self.worry_stack[0]
        self.worry_stack = self.worry_stack[1:]
        return item

    def inspect(self, value):
        self.count += 1
        amount = self.amount

        if self.amount == "old":
            amount = value
        if self.operation == "*":
            return value * int(amount)
        if self.operation == "+":
            return value + int(amount)

    def relief(self, value):
        return int(value / 3)

    def test(self, value):
        # print(f"Checking if {value} divisible by {self.divisible_by}")
        # print(f"{self.monkey_true}, {self.monkey_false}")
        return self.monkey_true if value % self.divisible_by == 0 else self.monkey_false

def get_inspection_counts(data, relief=True, iterations=20):

    monkeys = []

    for index in range(0, len(data), 7):
        m = Monkey()
        m.worry_stack = [int(a) for a in data[index + 1].split(":")[-1].split(",")]
        m.operation, m.amount = data[index + 2].split()[-2:]

        m.divisible_by = int(data[index + 3].split()[-1])
        m.monkey_true = int(data[index + 4][-1])
        m.monkey_false = int(data[index + 5][-1])

        monkeys.append(m)

    common = math.prod([m.divisible_by for m in monkeys])

    for j in range(iterations):
        for i, m in enumerate(monkeys):
            # print(f"Monkey: {i}")

            while item := m.next():
                # print(f"Start {item}")
                item = m.inspect(item)
                # print(f"Inspect {item}")
                if relief:
                    item = m.relief(item)
                # print(f"Relief {item}")
                target = m.test(item)
                # print(f"Target {target}")
                monkeys[target].worry_stack.append(item % common)
                # print(monkeys[target].worry_stack)
                # print()
    return [m.count for m in monkeys]


def get_part1_answer(data):
    inspection_counts = get_inspection_counts(data)

    sorted_counts = sorted(inspection_counts, reverse=True)

    return sorted_counts[0] * sorted_counts[1]


def get_part2_answer(data):
    inspection_counts = get_inspection_counts(data, relief=False, iterations=10000)

    sorted_counts = sorted(inspection_counts, reverse=True)

    return sorted_counts[0] * sorted_counts[1]


if __name__ == "__main__":
    data = get_data("./data/day11_input.txt")
    print(f"Part 1: {get_part1_answer(data)}")
    print(f"Part 2: {get_part2_answer(data)}")
