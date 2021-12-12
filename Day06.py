def part1(data):
    for j in range(80):
        # new fish created so that loop isnt affected
        new = []
        for i in range(len(data)):
            # changing each one
            data[i] -= 1
            # looping adding 1 new 8 fish
            if data[i] == -1:
                data[i] = 6
                new.append(8)
        # combine lists
        data += new
    return len(data)


def part2(data):
    dic = {}
    # dictionaty creation
    for n in data:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
    for i in range(256):
        # changing keys
        dic1 = {(k-1): v for k, v in dic.items()}
        # if we need to make new fish
        if -1 in dic1:
            x = dic1[-1]
            # spawned
            dic1[8] = x
            # fish looped but not spawned
            if 6 in dic1:
                dic1[6] += x
            else:
                dic1[6] = x
            # removing negative fish
            del dic1[-1]
        # changing main dictionary
        dic = dic1
    # summing values
    return sum(dic.values())

with open("Day6.txt") as file:
    data = file.read().split(",")
    data = list(map(int, data))
    print(f"Part1 solution = {part1(data.copy())}")
    print(f"Part2 solution = {part2(data.copy())}")
