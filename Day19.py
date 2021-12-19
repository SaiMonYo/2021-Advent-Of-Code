def orientate(point, orientation):
    # get the 24 permutations of rotations etc.
    x, y, z = point
    return [
        (+x,+y,+z),(+y,+z,+x),(+z,+x,+y),(+z,+y,-x),(+y,+x,-z),(+x,+z,-y), 
        (+x,-y,-z),(+y,-z,-x),(+z,-x,-y),(+z,-y,+x),(+y,-x,+z),(+x,-z,+y), 
        (-x,+y,-z),(-y,+z,-x),(-z,+x,-y),(-z,+y,+x),(-y,+x,+z),(-x,+z,+y), 
        (-x,-y,+z),(-y,-z,+x),(-z,-x,+y),(-z,-y,-x),(-y,-x,-z),(-x,-z,-y) 
    ][orientation]


# scanner class
class Scanner:
    '''holds the coordinates and the all the orientations'''
    def __init__(self, chunk):
        # no need to keep name
        self.coords = [tuple(map(int, line.split(","))) for line in chunk.split("\n")[1:]]
        # get all orienations
        self.all_orientated = [self.remap(i) for i in range(24)]

    def remap(self, i):
        return [orientate(point, i) for point in self.coords]
        
# reading file
with open("input.txt") as file:
    scanners = [Scanner(chunk) for chunk in file.read().split("\n\n")]

# having the values be from scanner 0
good = set(point for point in scanners[0].coords)
bad = scanners[1:]
locations = [(0,0,0)]

# still have values not aligned
while bad:
    # getting the alignment from one
    # point in good to one in the bad
    for a in list(good):
        for b in list(bad):
            # all points in each permutation
            for orient in b.all_orientated:
                for c in orient:
                    dx = c[0] - a[0]
                    dy = c[1] - a[1]
                    dz = c[2] - a[2]
                    aligned = {(x-dx, y-dy, z-dz) for x,y,z in orient}
                    overlap = len(aligned.intersection(good))
                    # each one shares atleast 12 in the right orientation
                    if overlap >= 12:
                        locations.append((dx, dy, dz))
                        good |= aligned
                        bad.remove(b)
                        break
# part 1 - 
print(f"Part 1 Solution - {len(good)}")
# part 2 - max manhatten distances
best = max([max([abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) for a in locations]) for b in locations])
print(f"Part 2 Solution - {best}")
