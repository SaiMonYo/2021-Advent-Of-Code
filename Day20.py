def run(points, even, algo):
    # on even turns there will be a finite amount of on lights
    # on an odd turn there will be a finite number of off lights
    # so we keep track of only the finite points on the board
    npoints = set()
    rows, columns = [], []
    for x, y in points:
        rows.append(y)
        columns.append(x)
    # only need to look at the maximas and minumas +- 2
    # everything else will # on even steps, . on odds
    for y in range(min(rows)-2, max(rows) + 2):
        for x in range(min(columns)-2, max(columns)+2):
            # working out 9 bit number
            byte = ""
            # neighbours
            for oy in range(-1, 2):
                for ox in range(-1, 2):
                    if ((x + ox, y + oy) in points) == even:
                        byte += "1"
                    else:
                        byte += "0"
            if (algo[int(byte, 2)] == "#") != even:
                npoints.add((x, y))
    return npoints


# data handing
with open("Day20.txt") as file:
    algo, board = file.read().split("\n\n")
    board = board.split("\n")
    points = set()
    for j in range(len(board)):
        for i in range(len(board[j])):
            if board[j][i] == "#":
                points.add((i, j))

# looping 50 times
for s in range(50):
    if s == 2:
        print(f"Part 1 Solution - {len(points)}")
    points = run(points, s % 2 == 0, algo)
print(f"Part 2 Solution - {len(points)}")
