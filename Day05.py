def part1(data):
    lines = []
    # maxes 
    mx = 0
    my = 0
    for i in range(len(data)):
        # parsing
        line = data[i]
        p, p1 = line.split(" -> ")
        x, y = list(map(int, p.split(",")))
        x1, y1 = list(map(int, p1.split(",")))
        x, y = int(x), int(y)
        x1, y1 = int(x1), int(y1)
        # for board
        mx = max([x, x1, mx])
        my = max([y, y1, my])
        # horizontal and verticals only
        if x1 == x or y1 == y:
            lines.append((x, y, x1, y1))
    # creating board
    board = [[0 for _ in range(mx+1)] for __ in range(my+1)]
    # adding lines
    for line in lines:
        x, y, x1, y1 = line
        if x == x1:
            y, y1 = sorted([y, y1])
            for yi in range(y, y1+1):
                board[yi][x] += 1
        else:
            x, x1 = sorted([x, x1])
            for xi in range(x, x1+1):
                board[y][xi] += 1
    # summing board
    return sum(sum(0 if p <= 1 else 1 for p in row) for row in board)


def part2(data):
    lines = []
    mx = 0
    my = 0
    for i in range(len(data)):
        # parsing
        line = data[i]
        p, p1 = line.split(" -> ")
        x, y = list(map(int, p.split(",")))
        x1, y1 = list(map(int, p1.split(",")))
        mx = max([x, x1, mx])
        my = max([y, y1, my])
        lines.append((x, y, x1, y1))
    board = [[0 for _ in range(mx+1)] for __ in range(my+1)]
    for line in lines:
        # tuple unpacking
        x, y, x1, y1 = line
        # horizontal
        if x == x1:
            y, y1 = sorted([y, y1])
            for yi in range(y, y1+1):
                board[yi][x] += 1
        # vertical
        elif y == y1:
            x, x1 = sorted([x, x1])
            for xi in range(x, x1+1):
                board[y][xi] += 1
        else:
            # diagonals
            dy = y1 - y
            dx = x1 - x
            # gradient
            m = int(dy / dx)
            if m == 1:
                x, x1 = sorted([x, x1])
                y, y1 = sorted([y, y1])
                xp = x
                yp = y
                board[yp][xp] += 1
                while xp != x1:
                    yp += 1
                    xp += 1
                    board[yp][xp] += 1
            else:
                x, x1 = sorted([x, x1])
                y1, y = sorted([y, y1])
                yp = y
                xp = x
                board[yp][xp] += 1
                while yp != y1:
                    yp -= 1
                    xp += 1
                    board[yp][xp] += 1
    # debugging
    #for row in board:
        #print(''.join(str(c) if c > 0 else "." for c in row))

    # summing board
    return sum(sum(0 if p <= 1 else 1 for p in row) for row in board)


with open("Day5.txt") as file:
    data = file.read().split("\n")
    #data = list(map(int, data))
    print(f"Part1 solution = {part1(data.copy())}")
    print(f"Part2 solution = {part2(data.copy())}")
