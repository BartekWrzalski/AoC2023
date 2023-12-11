from copy import deepcopy

with open("day11/day11.txt", "r", encoding="utf-8") as file:
    input = file.readlines()


def expand():
    expanded = deepcopy(input)
    empty_rows_ix = []
    empty_cols_ix = []

    for i, line in enumerate(expanded):
        if len(set(line[:-1])) == 1:
            empty_rows_ix.append(i)

    for j in range(len(expanded[0])):
        if all(expanded[i][j] == "." for i in range(len(expanded))):
            empty_cols_ix.append(j)

    empty_row = ["." * (len(expanded[0]) - 1) + "\n"]
    for row in empty_rows_ix[::-1]:
        expanded = expanded[:row] + empty_row + expanded[row:]

    for col in empty_cols_ix[::-1]:
        for i in range(len(expanded)):
            expanded[i] = expanded[i][:col] + "." + expanded[i][col:]

    return expanded


def one():
    expanded = expand()
    result = 0

    galaxies = []
    for i in range(len(expanded)):
        for j in range(len(expanded[i])):
            if expanded[i][j] == "#":
                galaxies.append((i, j))

    for i, galaxy in enumerate(galaxies):
        for next in galaxies[i + 1 :]:
            result += abs(galaxy[0] - next[0]) + abs(galaxy[1] - next[1])

    print(result)


def two():
    expand_len = 1_000_000
    result = 0

    empty_rows_ix = []
    empty_cols_ix = []

    for i, line in enumerate(input):
        if len(set(line[:-1])) == 1:
            empty_rows_ix.append(i)

    for j in range(len(input[0])):
        if all(input[i][j] == "." for i in range(len(input))):
            empty_cols_ix.append(j)

    galaxies = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "#":
                galaxies.append((i, j))

    for i, galaxy in enumerate(galaxies):
        for next in galaxies[i + 1 :]:
            expand_width = sum(
                [
                    min(galaxy[1], next[1]) < ex < max(galaxy[1], next[1])
                    for ex in empty_cols_ix
                ]
            )
            expand_height = sum(
                [
                    min(galaxy[0], next[0]) < ex < max(galaxy[0], next[0])
                    for ex in empty_rows_ix
                ]
            )

            result += (
                abs(galaxy[0] - next[0])
                + abs(galaxy[1] - next[1])
                + (expand_len - 1) * (expand_height + expand_width)
            )

    print(result)


one()
two()
