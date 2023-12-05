with open("day3/day3.txt", "r", encoding="utf-8") as file:
    input = file.readlines()

line_len = len(input[0])

def look_bw(i, j):
    k = j - 1
    while k >= 0 and input[i][k].isnumeric():
        k -= 1
    return int(input[i][k+1:j])

def look_fw(i, j):
    k = j + 1
    while k + 1 < line_len and input[i][k].isnumeric():
        k += 1
    return int(input[i][j+1:k])

def look_both(i, j):
    l = j - 1
    r = j + 1
    while l >= 0 and input[i][l].isnumeric():
        l -= 1
    while r + 1 < line_len and input[i][r].isnumeric():
        r += 1
    return int(input[i][l+1:r])


def one(source):
    result = 0

    for i, line in enumerate(source):
        for j, char in enumerate(line):
            if char.isnumeric() or char == "." or char == "\n":
                continue

            if j - 1 >= 0 and source[i][j - 1].isnumeric():
                result += look_bw(i, j)
            
            if j + 1 < line_len and source[i][j + 1].isnumeric():
                result += look_fw(i, j )
            
            if i - 1 >= 0:
                if source[i - 1][j].isnumeric():
                    result += look_both(i - 1, j)

                else:
                    if j - 1 >= 0 and source[i - 1][j - 1].isnumeric():
                        result += look_bw(i - 1, j)
                
                    if j + 1 < line_len and source[i - 1][j + 1].isnumeric():
                        result += look_fw(i - 1, j)
            
            if i + 1 < line_len:
                if source[i + 1][j].isnumeric():
                    result += look_both(i + 1, j)

                else:
                    if j - 1 >= 0 and source[i + 1][j - 1].isnumeric():
                        result += look_bw(i + 1, j)
                
                    if j + 1 < line_len and source[i + 1][j + 1].isnumeric():
                        result += look_fw(i + 1, j)
    print(result)

def two(source):
    result = 0

    for i, line in enumerate(source):
        for j, char in enumerate(line):
            if not char == "*":
                continue
            gears = []
            if j - 1 >= 0 and source[i][j - 1].isnumeric():
                gears.append(look_bw(i, j))
            
            if j + 1 < line_len and source[i][j + 1].isnumeric():
                gears.append(look_fw(i, j))
            
            if i - 1 >= 0:
                if source[i - 1][j].isnumeric():
                    gears.append(look_both(i - 1, j))

                else:
                    if j - 1 >= 0 and source[i - 1][j - 1].isnumeric():
                        gears.append(look_bw(i - 1, j))
                
                    if j + 1 < line_len and source[i - 1][j + 1].isnumeric():
                        gears.append(look_fw(i - 1, j))
            
            if i + 1 < line_len:
                if source[i + 1][j].isnumeric():
                    gears.append(look_both(i + 1, j))

                else:
                    if j - 1 >= 0 and source[i + 1][j - 1].isnumeric():
                        gears.append(look_bw(i + 1, j))
                
                    if j + 1 < line_len and source[i + 1][j + 1].isnumeric():
                        gears.append(look_fw(i + 1, j))
            
            if len(gears) == 2:
                result += gears[0] * gears[1]
    print(result)

one(input)
two(input)
