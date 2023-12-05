import re

with open("day1/day1.txt", "r", encoding="utf-8") as file:
    input = file.readlines()

def one(source):
    numbers = [
        re.findall(r'[0-9]', line) for line in source
    ]

    result = sum(10 * int(x[0]) + int(x[-1]) for x in numbers)

    print(result)

def two(source):
    pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")
    
    def to_int(v):
        if v.isdecimal():
            return int(v)

        return {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }[v]

    filtered = [re.findall(pattern, line) for line in source]
    numbers = [list(map(to_int, line)) for line in filtered]
    
    sums = [10 * x[0] + x[-1] for x in numbers]

    # for a, b, c in zip(filtered, numbers, sums):
    #     print(a, b, c)
    print(sum(sums))


one(input)
two(input)