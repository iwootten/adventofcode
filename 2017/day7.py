from __future__ import print_function
import re


def get_maps():
    tower_map = {}
    weight_map = {}
    child_map = {}

    with open('day7/input.txt', 'r') as content_file:
        pattern = re.compile(r"""(?P<name>.*)\s\((?P<weight>.*)\)(\s\-\>\s(?P<children>.*))?""", re.VERBOSE)

        for row in content_file.readlines():
            match = pattern.match(row)

            name = match.group("name")
            weight = int(match.group("weight"))
            weight_map[name] = weight

            if match.group("children"):
                children = match.group("children").split(",")

                for child in children:
                    tower_map[child.strip()] = name
                child_map[name] = [child.strip() for child in children]

    return tower_map, weight_map, child_map


def find_root(tower_map):
    search_key = tower_map.keys()[0]

    while search_key in tower_map.keys():
        search_key = tower_map[search_key]

    return search_key


def get_tower_programs(search_node, child_map):
    contents = []

    if search_node in child_map:
        for child in child_map[search_node]:
            contents.extend(get_tower_programs(child, child_map))

    contents.append(search_node)

    return contents


def calculate_weight(programs, weight_map):
    total = 0

    for program in programs:
        total += weight_map[program]

    return total


def get_odd_item(child_weight_map):
    child_weight_values = child_weight_map.values()
    odd_item_value = next(item for item in child_weight_values if child_weight_values.count(item) == 1)

    for key, item in child_weight_map.iteritems():
        if item == odd_item_value:
            return key, item


def find_mismatch(child_map, weight_map):
    for key, child_list in child_map.iteritems():
        child_weight_map = {}

        for child in child_list:
            child_programs = get_tower_programs(child, child_map)
            child_weight = calculate_weight(child_programs, weight_map)

            child_weight_map[child] = child_weight

        if len(set(child_weight_map.values())) != 1:
            child_weight_values = child_weight_map.values()
            odd_key, odd_value = get_odd_item(child_weight_map)
            correct_value = next(item for item in child_weight_values if child_weight_values.count(item) != 1)
            print("Mismatch found for child key '{}' in children '{}'".format(odd_key, ", ".join(child_list)))
            print("\tTower Value is {} - should be {}".format(odd_value, correct_value))
            print("\tNeeds adjusting by {}".format(correct_value - odd_value))
            print("\tOriginal needs adjusting to {}".format(weight_map[odd_key] + (correct_value - odd_value)))


class Program(object):
    weight = 0
    name = ""
    children = []

    def __init__(self, name, weight, children):
        self.weight = weight
        self.name = name
        self.children = children

    def __repr__(self):
        if len(self.children):
            return "{} ({}) -> {}".format(self.name, self.weight, ",".join(self.children))
        return "{} ({})".format(self.name, self.weight)


tower, weights, children = get_maps()
root_program = find_root(tower)

programs = get_tower_programs(root_program, children)
weight = calculate_weight(programs, weights)

print("Root program: {}".format(root_program))
print("Weight: {}".format(weight))

find_mismatch(children, weights)
