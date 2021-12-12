def part1(data):
    c = 0
    for j in range(len(data)):
        line = data[j]
        for i in range(len(line)):
            n = int(line[i])
            # couldve used what i used in part 2
            # if i >= 0 and i <= len(data)-1 and j >= 0 and j <= len(data)-1
            if j - 1 >= 0:
                if n >= int(data[j-1][i]):
                    continue
            if j + 1 < len(data):
                if int(data[j+1][i]) <= n:
                    continue
            if i + 1 < len(line):
                if int(data[j][i+1]) <= n:
                    continue
            if i - 1 >= 0:
                if int(data[j][i-1]) <= n:
                    continue
            # all neighbours are higher
            c += n + 1
    return c


def part2(data):
    basins = []
    for j in range(len(data)):
        line = data[j]
        for i in range(len(line)):
            n = int(line[i])
            # if i >= 0 and i <= len(data)-1 and j >= 0 and j <= len(data)-1
            if j - 1 >= 0:
                if n >= int(data[j-1][i]):
                    continue
            if j + 1 < len(data):
                if int(data[j+1][i]) <= n:
                    continue
            if i + 1 < len(line):
                if int(data[j][i+1]) <= n:
                    continue
            if i - 1 >= 0:
                if int(data[j][i-1]) <= n:
                    continue
            # locations i need to check
            checking = [(i, j)]
            # prevent infinite loops
            seen = set({(i, j)})
            # local basin
            basin = set({(i, j)})
            # flood filling
            while len(checking):
                # remove first one we need to check
                x, y = checking.pop()
                # neighbours
                for x1, y1 in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x1 = x + x1
                    y1 = y + y1
                    # not out of list
                    if x1 >= 0 and x1 <= len(data)-1 and y1 >= 0 and y1 <= len(data)-1:
                        # havent seen before
                        if (x1, y1) not in seen:
                            seen.add((x1, y1))
                            if int(data[y1][x1]) != 9:
                                basin.add((x1, y1))
                                # need to check this new value
                                checking.append((x1, y1))
            basins.append(len(basin))
    # biggest 3
    basins = sorted(basins)[::-1]
    return basins[0] * basins[1] * basins[2]


with open("Day9.txt") as file:
    data = file.read().split("\n")
    #data = list(map(int, data))
    print(f"Part1 solution = {part1(data)}")
    print(f"Part2 solution = {part2(data)}")
