# scoring and lookup dictionaries
lookup = {")": 3, "]": 57, "}" : 1197, ">": 25137}
lookup2 = {"(": 1, "[": 2, "{" : 3, "<": 4}

# open matched with closed
equivs = {"(": ")", "{": "}", "[": "]", "<": ">"}
# closed matched with open
equivs2 = {v: k for k, v in equivs.items()}
# opens and closes
openers = list(equivs.keys())
closers = list(equivs.values())

def part1(data):
    t = 0
    for i in range(len(data)):
        line = data[i]
        lasts = []
        for c in line:
            # opening a new chunk add to the top of "stack"
            if c in openers:
                lasts = [c] + lasts
            # a closing
            else:
                # the top != the matching opening bracket
                if lasts[0] != equivs2[c]:
                    # add score and break
                    t += lookup[c]
                    break
                else:
                    # found a match remove that match
                    lasts = lasts[1:]
    return t


def part2(data):
    scores = []
    for i in range(len(data)):
        line = data[i]
        lasts = []
        # incomplete line
        incomplete = True
        for c in line:
            if c in openers:
                lasts = [c] + lasts
            else:
                if lasts[0] != equivs2[c]:
                    # just a bad line
                    incomplete = False
                    break
                else:
                    lasts = lasts[1:]
        # calculating score
        if incomplete:
            s = 0
            for ch in lasts:
                s = s * 5 + lookup2[ch]
            scores.append(s)
    # median score
    return sorted(scores)[len(scores)//2]


with open("Day10.txt") as file:
    data = file.read().split("\n")
    #data = list(map(int, data))
    print(f"Part1 solution = {part1(data.copy())}")
    print(f"Part2 solution = {part2(data.copy())}")