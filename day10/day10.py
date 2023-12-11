import re

with open("day10/day10.txt", "r", encoding="utf-8") as file:
    input = file.readlines()

for i, line in enumerate(input):
    if "S" in line:
        s_i, s_j = i, line.index("S")


def get_move_vector(i, j, prev: (int, int)) -> (int, int):
    if input[i][j] == "-":
        return 0, prev[1]

    elif input[i][j] == "|":
        return prev[0], 0

    elif input[i][j] == "L":  # prev = (-1, 0) or (0, -1)
        return -prev[1], -prev[0]

    elif input[i][j] == "J":  # prev = (-1, 0) or (0, 1)
        return prev[1], prev[0]

    elif input[i][j] == "7":  # prev = (1, 0) or (0, 1)
        return -prev[1], -prev[0]

    elif input[i][j] == "F":  # prev = (1, 0) or (0, -1)
        return prev[1], prev[0]


def one():
    c_i, c_j = s_i, s_j
    if input[s_i][s_j + 1] in "-J7":
        c_j += 1
        vec = (0, 1)
    elif input[s_i][s_j - 1] in "-FL":
        c_j -= 1
        vec = (0, -1)
    elif input[s_i + 1][s_j] in "|JL":
        c_i += 1
        vec = (-1, 0)
    elif input[s_i - 1][s_j] in "|F7":
        c_i -= 1
        vec = (1, 0)

    steps = 1
    while input[c_i][c_j] != "S":
        vec = get_move_vector(c_i, c_j, vec)
        c_i -= vec[0]
        c_j += vec[1]
        steps += 1

    print(steps // 2)


def write_inside(line: list[str]) -> list[str]:
    inside = False
    borders = []

    for i in range(len(line)):
        if line[i] == ".":
            if borders > 0:
                line[i] = "1"
            continue

        if line[i] == "|":
            ...
        elif line[i] == "F":
            ...
        elif line[i] == "7":
            ...
        elif line[i] == "L":
            ...
        elif line[i] == "J":
            ...


def s_pipe(s_i, s_j) -> str:
    neighbours = []
    if input[s_i][s_j + 1] in "-J7":
        neighbours.append(set("-FL"))
    if input[s_i][s_j - 1] in "-FL":
        neighbours.append(set("-J7"))
    if input[s_i + 1][s_j] in "|JL":
        neighbours.append(set("|F7"))
    if input[s_i - 1][s_j] in "|F7":
        neighbours.append(set("|JL"))

    return "".join(neighbours[0] & neighbours[1])


def two():
    clean_map = [["." for _ in range(len(input[0]))] for _ in range(len(input))]

    on_s = s_pipe(s_i, s_j)
    clean_map[s_i][s_j] = on_s

    c_i, c_j = s_i, s_j
    if on_s in "-LF":
        c_j += 1
        vec = (0, 1)
    elif on_s in "J7":
        c_j -= 1
        vec = (0, -1)
    else:
        c_i += 1
        vec = (-1, 0)

    while clean_map[c_i][c_j] == ".":
        clean_map[c_i][c_j] = input[c_i][c_j]
        vec = get_move_vector(c_i, c_j, vec)
        c_i -= vec[0]
        c_j += vec[1]

    for line in clean_map:
        write_inside(line)

    with open("day10/day10_2.txt", "w", encoding="utf-8") as file:
        for line in clean_map:
            file.write("".join(line) + "\n")

    # for i in range(len(input)):
    #     print(input[i])


one()
two()
