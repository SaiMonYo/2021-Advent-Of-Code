def fold(board, l, i):
    # line x=?
    if l == "x":
        for y in range(0, len(board)):
            for x in range(i, len(board[0])):
                # if theres a point
                if board[y][x] == 1:
                    # working out new index and removing old
                    board[y][i-(x-i)] = 1
                    board[y][x] = 0
    else:
        for y in range(i, len(board)):
            for x in range(0, len(board[0])):
                if board[y][x] == 1:
                    # working out new index and removing old
                    board[i-(y-i)][x] = 1
                    board[y][x] = 0


def part1(data):
    # parsing the raw data
    points, folds = data
    points = points.split("\n")
    folds = folds.split("\n")
    board = [[0 for i in range(1500)] for j in range(1500)]
    # putting points on the paper
    for p in points:
        x,y = list(map(int, p.split(",")))
        board[y][x] = 1
    f = folds[0]
    # ("x" or "y"), position of line
    l, i = f.split(" ")[-1].split("=")
    i = int(i)
    # folding paper
    fold(board, l, i)
    # counting points
    c = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 1:
                c += 1
    part2(board, folds)
    return c

def part2(board, folds):
    # already done first fold
    for f in folds[1:]:
        # ("x" or "y"), position of line
        l, i = f.split(" ")[-1].split("=")
        i = int(i)
        fold(board, l, i)
    # output
    print("Part 2 solution: ")
    for j in range(8):
        print(''.join("#" if c else " " for c in board[j][:50]))


with open("Day13.txt") as file:
    data = file.read().split("\n\n")
    print(f"Part1 solution = {part1(data)}")