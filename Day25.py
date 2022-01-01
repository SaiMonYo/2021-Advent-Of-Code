from copy import deepcopy

with open("Day25.txt") as file:
    rows = file.read().split("\n")
    
t = 0
while True:
    t += 1
    old = deepcopy(rows)
    for i in range(len(rows)):
        # need to check before any moves
        first, last = rows[i][0] == ".", rows[i][-1] == ">"
        # moving fish to east first
        rows[i] = rows[i].replace(">.", ".>")
        # if there was fish at end and it could move to start
        if last and first:
            rows[i] = ">" + rows[i][1:-1] + "."
    changes = []
    # need to move all southern at same time
    for j in range(len(rows)):
        for i in range(len(rows[j])):
            # loops back around
            if rows[j][i] == "v" and rows[(j + 1 ) % len(rows)][i] == ".":
                changes.append((j, (j + 1 ) % len(rows), i))
    # moving all the southern at once
    for y1, y2, x in changes:
        rows[y1] = rows[y1][:x] + "." + rows[y1][x+1:]
        rows[y2] = rows[y2][:x] + "v" + rows[y2][x+1:]
    # board is repeated
    if rows == old:
        print(f"Part 1 Solution - {t}")
        break