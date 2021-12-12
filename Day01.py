def part1(data):
    t = 0
    c = 0
    # start on 1
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            c += 1
    return c

def part2(data):
    c = 0
    old = 0
    # sweeping window 
    for i in range(2, len(data)):
        if sum(data[i-2:i+1]) > old:
            c += 1
        old = sum(data[i-2:i+1])
    # minus 1 for the first window as it is always > 0
    # and we dont count the first window
    # this cost me leaderboard position on part 2
    return c - 1



with open("Day1.txt") as file:
    data = file.read().split("\n")
    if data[-1] == "" or data[-1] == "\n":
        data = data[:-1]
    # designed code yesterday try except not needed
    try:
        data = list(map(int, data))
    except:
        pass
    print(f"Part1 solution = {part1(data)}")
    print(f"Part2 solution = {part2(data)}")
