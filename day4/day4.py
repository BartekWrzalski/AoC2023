with open("day4/day4.txt", "r", encoding="utf-8") as file:
    input = file.readlines()

def one(source):
    result = 0
    for line in source:
        win, card = line.split(":")[1].split("|")

        n = sum([num in card.split() for num in win.split()])
        
        result += 2**(n-1) if n > 0 else 0
    
    print(result)

def two(source):
    result = [0] * len(source)
    for i, line in enumerate(source):
        win, card = line.split(":")[1].split("|")

        n = sum([num in card.split() for num in win.split()])
        
        result[i] += 1
        for k in range(1, n + 1):
            result[i + k] += result[i]
    
    print(sum(result))

one(input)
two(input)