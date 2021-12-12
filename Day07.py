# was able to get this done with good code
# as i slept through 3 alarms and wasnt rushing

def part1(data):
    # using middle value to get distances to all other crabs
    middle = sorted(data)[len(data)//2]
    return sum(abs(crab - middle) for crab in data)


def part2(data):
    cost = 999999999999
    for i in range(min(data), max(data) + 1):
        # summing
        ccost = sum((abs(crab - i) * (abs(crab - i) + 1)) >> 1 for crab in data)
        # updating cost
        cost = min(cost, ccost)
    return cost


with open("Day7.txt") as file:
    data = file.read().split(",")
    data = list(map(int, data))
    print(f"Part1 solution = {part1(data.copy())}")
    print(f"Part2 solution = {part2(data.copy())}")
