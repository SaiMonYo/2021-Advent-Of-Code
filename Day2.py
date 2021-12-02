def part1(data):
    x = 0
    y = 0
    # defualt iterator 
    for i, d in enumerate(data):
        # direction, amount
        di, c = d.split(" ")
        c = int(c)
        # couldve used match case, or just looked at first letter
        if di == "forward":
            x += c
        elif di == "down":
            y += c
        elif di == "up":
            y -= c
        # couldve used else for up as there is no back command
        else:
            x -= c
    return x * y


def part2(data):
    a = 0
    x = 0
    y = 0
    # default iterator
    for i, d in enumerate(data):
        # direction, amount
        di, c = d.split(" ")
        c = int(c)
        if di == "forward":
            x += c
            y += a * c
        elif di == "down":
            a += c
        elif di == "up":
            a -= c
        # couldve used else for up as there is no back command
        else:
            x -= c
    return x * y


with open("Day2.txt") as file:
    data = file.read().split("\n")
    #data = list(map(int, data))
    print(f"Part1 solution = {part1(data)}")
    print(f"Part2 solution = {part2(data)}")

