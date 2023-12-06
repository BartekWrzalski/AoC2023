import re

with open("day6/day6.txt", "r", encoding="utf-8") as file:
    input = file.readlines()


def one():
    times = [int(time) for time in input[0].split()[1:]]
    records = [int(record) for record in input[1].split()[1:]]

    result = 1
    for time, record in zip(times, records):
        charge_time = time // 2

        while (time - charge_time) * charge_time > record:
            charge_time -= 1

        result *= time - 2 * charge_time - 1
    print(result)


def two():
    time = int("".join(re.findall(r"\d+", input[0])))
    record = int("".join(re.findall(r"\d+", input[1])))

    charge_time = time // 2
    l = 0
    r = charge_time

    while r - l > 1:
        distance = (time - charge_time) * charge_time
        # print(charge_time, distance)
        if distance > record:
            r = charge_time
            charge_time -= (r - l) // 2
        else:
            l = charge_time
            charge_time += (r - l) // 2

    print(time - 2 * l - 1)


one()
two()
