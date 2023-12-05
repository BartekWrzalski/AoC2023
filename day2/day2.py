import re
from copy import copy
import math

with open("day2/day2.txt", "r", encoding="utf-8") as file:
    input = file.readlines()


def one(source):
    limit = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    result = 0
    for game in source:
        cubes = re.split(r";|,", game.split(": ")[1])
        for draw in cubes:
            num, color = draw.split()

            if int(num) > limit[color]:
                break
        else:
            result += int(game.split()[1][:-1])

    print(result)

def two(source):
    needed = {
        "red": 0,
        "green": 0,
        "blue": 0 
    }
    result = []

    for game in source:
        need_in_game = copy(needed)
        
        cubes = re.split(r";|,", game.split(": ")[1])
        for draw in cubes:
            num, color = draw.split()

            if int(num) > need_in_game[color]:
                need_in_game[color] = int(num)

        result.append(math.prod(need_in_game.values()))
    
    print(sum(result))

one(input)
two(input)