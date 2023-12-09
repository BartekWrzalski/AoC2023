import re
import math

with open("day8/day8.txt", "r", encoding="utf-8") as file:
    input = file.readlines()

steps = input[0][:-1]
cycle_len = len(steps)
nodes = {
    start: {"L": left, "R": right}
    for start, left, right in [re.findall("\w+", move) for move in input[2:]]
}


def one():
    current = "AAA"
    step_count = 0

    while current != "ZZZ":
        direction = steps[step_count % cycle_len]
        current = nodes[current][direction]
        step_count += 1

    print(step_count)


def two():
    currents = [start for start in nodes if start[-1] == "A"]
    steps_each_path = []
    step_count = 0

    for current in currents:
        while current[-1] != "Z":
            direction = steps[step_count % cycle_len]
            current = nodes[current][direction]
            step_count += 1

        steps_each_path.append(step_count)
        step_count = 0

    print(
        math.lcm(
            *steps_each_path,
        )
    )


one()
two()
