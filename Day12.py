def recursive_help(pos, visited, neighbours):
    # end case
    if pos == "end":
        return 1
    # not a valid path
    if pos.islower() and pos in visited:
        return 0
    visited.add(pos)
    ret = 0
    # getting neighbours
    for name in neighbours[pos]:
        ret += recursive_help(name, visited.copy(), neighbours)
    return ret


def part1(data):
    return recursive_help("start", set(), data)


def recursive_help2(pos, visited, visited2, neighbours):
    # end case
    if pos == "end":
        return 1
    if pos.islower() and pos in visited:
        # not valid paths
        if pos == "start":
            return 0
        if visited2 != "":
            return 0
        # allow this to be the the small cave we visit twice
        else:
            visited2 = pos
    visited.add(pos)
    ret = 0
    # getting neighbours
    for name in neighbours[pos]:
        # need copy, as set is passed by reference
        ret += recursive_help2(name, visited.copy(), visited2, neighbours)
    return ret


def part2(data):
    return recursive_help2("start", set(), "", data)


with open("Day12.txt") as file:
    data = file.read().split("\n")
    # adjacency list
    # contains the cave and all neighbouring caves
    neighbours = {}
    for line in data:
        if line == "":
            continue
        a, b = line.split("-")
        if a in neighbours:
            neighbours[a].append(b)
        else:
            neighbours[a] = [b]
        if b in neighbours:
            neighbours[b].append(a)
        else:
            neighbours[b] = [a]
    print(f"Part1 solution = {part1(neighbours.copy())}")
    print(f"Part2 solution = {part2(neighbours.copy())}")