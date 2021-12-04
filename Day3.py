def part1(data):
    # counting bit occurences
    # realised i could do it bit by bit
    # not byte by byte on second challenge
    array1 = [0 for i in range(len(data[0]))]
    array2 = [0 for i in range(len(data[0]))]
    for i, d in enumerate(data):
         for j in range(len(d)):
            if d[j] == "0":
                array1[j] +=1
            else:
                array2[j] += 1
    # creating gamma
    gamma = ["0" if (array1[i] > array2[i] and array1[i] != array2[i]) else "1" for i in range(len(array1))]
    gamma = int(''.join(gamma), 2)
    # full 1's 
    y = int(len(data[0])*"1", 2)
    return gamma * (y-gamma)



def part2(data):
    # copying since were going to be removing elements
    data = data.copy()
    datacopy = data.copy()
    # bit by bit not byte by byte
    for i in range(len(data[0])):
        a = 0
        b = 0
        for line in data:
            if line[i] == "0":
                a += 1
            else:
                b += 1
        if a > b:
            # removing
            data = [c for c in data if c[i] == "0"]
        else:
            # removing
            data = [c for c in data if c[i] == "1"]
        if len(data) == 1:
            break
    # convert from base 2
    oxy = int(data[0], 2)

    # copying data across
    data = datacopy
    # same as above just flip the bits
    for i in range(len(data[0])):
        a = 0
        b = 0
        for line in data:
            if line[i] == "0":
                a += 1
            else:
                b += 1
        if a > b:
            data = [c for c in data if c[i] == "1"]
        else:
            data = [c for c in data if c[i] == "0"]
        if len(data) == 1:
            break
    
    co2 = int(data[0], 2)
    return oxy * co2


with open("Day3.txt") as file:
    data = file.read().split("\n")
    #data = list(map(int, data))
    print(f"Part1 solution = {part1(data)}")
    print(f"Part2 solution = {part2(data)}")
