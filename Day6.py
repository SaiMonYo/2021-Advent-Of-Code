def part1(data):
    for j in range(20):
        new = []
        for i in range(len(data)):
            data[i] -= 1
            if data[i] == -1:
                data[i] = 6
                new.append(8)
        data += new
    return len(data)
        


def part2(data):
    dic = {}
    for n in data:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
    for i in range(256):
        dic1 = {(k-1): v for k, v in dic.items()}
        if -1 in dic1:
            x = dic1[-1]
            dic1[8] = x
            if 6 in dic1:
                dic1[6] += x
            else:
                dic1[6] = x
            del dic1[-1]
        dic = dic1
    return sum(dic.values())

def test(data):
    dic = {1: 6206821033, 2: 5617089148, 3: 5217223242, 4: 4726100874, 5: 4368232009, 6: 3989468462}
    c = 0
    for n in data:
        c += dic[n]
    return c

with open("Day6.txt") as file:
    data = file.read().split(",")
    data = list(map(int, data))
    print(f"Part1 solution = {part1(data.copy())}")
    print(f"Part2 solution = {part2(data.copy())}")
    print(f"Part1 solution = {test(data.copy())}")