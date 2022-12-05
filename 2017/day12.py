import re


def get_data():
    content = []

    with open('day12/input.txt', 'r') as content_file:
        pattern = re.compile(r"""(?P<source>.*)\s(\<\-\>)\s(?P<targets>.*)""", re.VERBOSE)

        for row in content_file.readlines():
            match = pattern.match(row)

            source = match.group("source")

            if match.group("targets"):
                input_targets = match.group("targets").split(",")

                targets = []

                for target in input_targets:
                    targets.append(int(target.strip()))

                content.append(targets)

    return content


def get_route_map(data, program_id):
    length = len(data)
    data_map = [None] * length

    start_total = 0
    end_total = 1

    while start_total != end_total:
        start_total = sum(r if r else 0 for r in data_map)
        for index, pipes in enumerate(data):
            if program_id in pipes or any(data_map[p] for p in pipes):
                data_map[index] = True
            else:
                data_map[index] = False
        end_total = sum(data_map)

    return data_map


def part1():
    data = get_data()
    route_map = get_route_map(data, 0)

    for index, can_reach_root in enumerate(route_map):
        print "{} : {}".format(index, can_reach_root)

    print "\n{} programs can reach program 0".format(sum(route_map))


def part2():
    data = get_data()
    current_program = 0
    more_groups = True
    group_map = [None] * len(data)

    while more_groups:
        route_map = get_route_map(data, current_program)

        for index, item in enumerate(route_map):
            if item:
                group_map[index] = current_program

        current_program = next((i for i, g in enumerate(group_map) if g is None), None)
        more_groups = current_program is not None

    print "Total groups: {}".format(len(set(group_map)))

part2()
