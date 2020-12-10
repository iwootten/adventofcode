import re
import datetime

def get_list():
    rows = []

    f = open('./input.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows

def get_instruction(row):
    matches = re.findall(r"\[(\d+-\d+-\d+\s\d+:\d+)\]\s(.+)", row)

    return datetime.datetime.strptime(matches[0][0], "%Y-%m-%d %H:%M").timestamp(), matches[0][0], int(matches[0][0][-2:]), matches[0][1]

rows = get_list()
stamped = []
sleep_activity = [[0 for x in range(60)] for x in range(4000)]

for row in rows:
    stamped.append(get_instruction(row))

sorted_stamped = sorted(stamped, key=lambda x:x[0])

current_guard = None
sleep_start = None
sleep_end = None

for timestamp, activity_datetime, activity_min, observation in sorted_stamped:
    if observation.startswith('Guard'):
        matches = re.findall(r"Guard #(\d+) begins shift", observation)
        current_guard = int(matches[0])
    elif observation == 'falls asleep':
        sleep_start = activity_min
    elif observation == 'wakes up':
        sleep_end = activity_min
        for i in range(sleep_start, sleep_end):
            sleep_activity[current_guard][i] += 1

max_index = 0
max_minute = 0

for current_guard in range(4000):
    for minute in range(60):
        if sleep_activity[current_guard][minute] > sleep_activity[max_index][max_minute]:
            max_index = current_guard
            max_minute = minute

print("Guard {} asleep longest in minute {}".format(max_index, max_minute))
print("Total {}".format(max_index * max_minute))