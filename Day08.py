import itertools

def part1(data):
    c = 0
    for i in range(len(data)):
        line = data[i]
        # first part not needed
        _, w = line.split(" | ")
        for b in w.split(" "):
            # they have specific amounts of segments
            if len(b) in [2, 3, 4, 7]:
                c += 1
    return c


# letters of the segments
letters = 'abcdefg'

# frozensets as normal sets cant be hashed
# all segments needed to light up the digit
dic = {frozenset('abcefg'): 0,
    frozenset('cf'): 1,
    frozenset('acdeg'): 2,
    frozenset('acdfg'): 3,
    frozenset('bcdf'): 4,
    frozenset('abdfg'): 5,
    frozenset('abdefg'): 6,
    frozenset('acf'): 7,
    frozenset('abcdefg'): 8,
    frozenset('abcdfg'): 9}


def allowed(perm, line):
    results = []
    for word in line:
        # lining up the correct config with the permutation
        lights = frozenset(perm[letters.index(letter)] for letter in word)
        # needs to be in the dictionary of allowed "words"
        if lights not in dic:
            return False
        # digit corresponding to the segments
        results.append(dic[lights])
    # last 4, 4 after the | symbol
    return results[-4:]

def part2(data):
    t = 0
    for i in range(len(data)):
        line = data[i].replace("| ", "").split(" ")
        # all permutaions of the segments configuration
        for perm in itertools.permutations(letters):
            # correct permutation
            if allowed(perm, line):
                # decoding the line
                t += int(''.join(str(digit) for digit in allowed(perm, line)))
                # weve decoding so we stop searching through the perms
                break
    return t


with open("Day8.txt") as file:
    data = file.read().split("\n")
    #data = list(map(int, data))
    print(f"Part1 solution = {part1(data.copy())}")
    print(f"Part2 solution = {part2(data.copy())}")
