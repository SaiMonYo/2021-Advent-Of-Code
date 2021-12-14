import itertools
import collections
import copy


def solve(data, n):
    # similar to lantern fish, need to find optimal code
    # instead of constructing long string, we need to look at letter pairs
    # polymer and instructions of the insertions
    poly, instr = data
    instr = instr.split("\n")
    # creating insertion lookup
    dic = {}
    for line in instr:
        a, b = line.split(" -> ")
        dic[a] = b
    
    # creating the pairs
    occur = {}
    for i in range(len(poly)-1):
        s = poly[i] + poly[i+1]
        if s in occur:
            occur[s] += 1
        else:
            occur[s] = 1
    # looping n times
    for r in range(n):
        # doing insertions
        temp = {}
        for key, value in occur.items():
            # CH -> CB BC
            f = key[0] + dic[key]
            l = dic[key] + key[1]
            # adding to the temp dictionary
            if f in temp:
                temp[f] += value
            else:
                temp[f] = value
            if l in temp:
                temp[l] += value
            else:
                temp[l] = value
        # swapping over
        occur = temp 

    count = collections.Counter()
    for key in occur:
        count[key[0]] += occur[key]
    # adding last letter as it wasnt included in pairs
    count[poly[-1]] += 1
    # maximum - minimum
    return max(count.values())-min(count.values())
        

with open("Day14.txt") as file:
    data = file.read().split("\n\n")
    #data = list(map(int, data))
    print(f"Part1 solution = {solve(copy.deepcopy(data), 10)}")
    print(f"Part2 solution = {solve(copy.deepcopy(data), 40)}")