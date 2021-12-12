def flash(i, j, data, f):
    # all 8 directions, no self (0, 0)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    f += 1
    # marking the flashing octo as -1 so we dont flash again
    data[j][i] = -1
    for x, y in directions:
        # new indexes
        x1, y1 = i + x, j + y
        # indexes within the list and the octo at that index hasnt flashed
        if x1 in range(10) and y1 in range(10) and data[y1][x1] != -1:
            # increment
            data[y1][x1] += 1
            # check if flashed
            if data[y1][x1] > 9:
                # flash that octo
                f = flash(x1, y1, data, f)
    return f


def part1(data):
    f = 0
    data = [[int(c) for c in row] for row in data]
    # 100 iterations
    for _ in range(100):
        # adding one to each octopus
        for j in range(10):
            for i in range(10):
                data[j][i] += 1
        # seeing if they flashed
        for j in range(10):
            for i in range(10):
                if data[j][i] > 9:
                    f = flash(i, j, data, f)
        # returning all flashed octopuses back to 0
        for j in range(10):
            for i in range(10):
                if data[j][i] == -1:
                    data[j][i] += 1
    return f           


def part2(data):
    c = 0
    data = [[int(c) for c in row] for row in data]
    # looping until return
    while True:
        # number of iterations
        c += 1
        # incrementing octopuses
        for j in range(10):
            for i in range(10):
                data[j][i] += 1
        # if the octo needs to be flashed
        for j in range(10):
            for i in range(10):
                if data[j][i] > 9:
                    # dont care about number of flashes
                    flash(i, j, data, 0)
        # if they all flashed
        if all(all(d == -1 for d in row) for row in data):
            return c
        # resetting flashed octos back to 0
        for j in range(10):
            for i in range(10):
                if data[j][i] == -1:
                    data[j][i] += 1


with open("Day11.txt") as file:
    data = file.read().split("\n")
    print(f"Part1 solution = {part1(data.copy())}")
    print(f"Part2 solution = {part2(data.copy())}")