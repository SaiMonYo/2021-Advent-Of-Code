import copy
import heapq

def part1(data):
    # 0 cost at 0, 0
    stack = [(0, 0, 0)]
    # creating a heap/priority queue which places items in order 
    # which we need for our dijkstra
    heapq.heapify(stack)
    costs = {}
    while True:
        # get the smallest element
        cost, x, y = heapq.heappop(stack)
        # if we've reached bottom right we know its best path
        if x == len(data) - 1 and y == len(data[0]) - 1:
            return cost
        # 4 cartesian neighbours
        for xp, yp in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            # not outside the grid
            if xp in range(0, len(data[0])) and yp in range(0, len(data)):
                # cost to enter that square
                newcost = cost + data[xp][yp]
                # we've already found a route cheaper
                if (xp, yp) in costs and costs[(xp, yp)] <= newcost:
                    continue
                # set this positions cost to the newcost
                costs[(xp,yp)] = newcost
                # need to check its neighbours
                heapq.heappush(stack, (newcost,xp,yp)) 


def part2(data):
    # creating 500x500
    expanded = [[0 for _ in range(5 * len(data[0]))] for __ in range(5 * len(data))]
    for x in range(len(expanded)):
        for y in range(len(expanded[0])):
            dist = x // len(data) + y // len(data[0])
            newval = data[x % len(data)][y % len(data[0])]
            for _ in range(dist):
                newval += 1
                if newval == 10:
                    newval = 1
            expanded[x][y] = newval
    # priority queue/stack 
    stack = [(0, 0, 0)]
    heapq.heapify(stack)
    costs = {}
    while True:
        # getting first item
        cost, x, y = heapq.heappop(stack)
        # first time we visit a node/square is the shortest route
        if x == len(expanded) - 1 and y == len(expanded[0]) - 1:
            return cost
        # adjacents
        for xp, yp in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if xp in range(0, len(expanded[0])) and yp in range(0, len(expanded)):
                newcost = cost + expanded[xp][yp]
                # already found a shorter route
                if (xp, yp) in costs and costs[(xp, yp)] <= newcost:
                    continue
                # adding to priority queue
                costs[(xp, yp)] = newcost
                heapq.heappush(stack, (newcost,xp,yp)) 


with open("Day15.txt") as file:
    data = file.read().split("\n")
    data = [[int(data[j][i]) for i in range(len(data[0]))] for j in range(len(data))]
    print(f"Part1 solution = {part1(copy.deepcopy(data))}")
    print(f"Part2 solution = {part2(copy.deepcopy(data))}")
