import itertools
import collections
import copy
def part1(data):
    c = 0
    stack = [(0, 0, 0)]
    costs = {}
    while True:
        cost, x, y = stack[0]
        if x == len(data) - 1 and y == len(data[0]) - 1:
            return cost
        stack = stack[1:]
        for xp,yp in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if xp in range(0, len(data[0])) and yp in range(0, len(data)):
                c += 1
                newcost = cost + data[xp][yp]
                if (xp, yp) in costs and costs[(xp, yp)] <= newcost:
                    continue
                costs[(xp,yp)] = newcost
                stack.append((newcost,xp,yp))
        stack = sorted(stack)   

def part2(data):
    # creating 500x500
    expanded = [[0 for x in range(5 * len(data[0]))] for y in range(5 * len(data))]
    for x in range(len(expanded)):
        for y in range(len(expanded[0])):
            dist = x // len(data) + y // len(data[0])
            newval = data[x % len(data)][y % len(data[0])]
            for i in range(dist):
                newval += 1
                if newval == 10:
                    newval = 1
            expanded[x][y] = newval
    c = 0
    stack = [(0, 0, 0)]
    costs = {}
    while True:
        cost, x, y = stack[0]
        if x == len(expanded) - 1 and y == len(expanded[0]) - 1:
            return cost
        stack=stack[1:]
        for xp,yp in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if xp in range(0, len(expanded[0])) and yp in range(0, len(expanded)):
                newcost = cost + expanded[xp][yp]
                if (xp, yp) in costs and costs[(xp,yp)] <= newcost:
                    continue
                costs[(xp, yp)] = newcost
                stack.append((newcost,xp,yp))
        stack = sorted(stack)


with open("Day15.txt") as file:
    data = file.read().split("\n")
    data = [[int(data[j][i]) for i in range(len(data[0]))] for j in range(len(data))]
    print(f"Part1 solution = {part1(copy.deepcopy(data))}")
    print(f"Part2 solution = {part2(copy.deepcopy(data))}")