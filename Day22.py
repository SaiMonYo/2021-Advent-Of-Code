import numpy as np

with open("Day22.txt") as file:
    data = file.read().split("\n")

def parse(coord):
    a, b = coord.split("..")
    return int(a[2:]), int(b)

# parsing the input
cubes = []
for line in data:
    x, y, z = line.split(" ")[1].split(",")
    cubes.append(["on" in line, *parse(x), *parse(y), *parse(z)])

# part 1
space = np.zeros((101,101,101), dtype=int)
for cube in cubes:
    # if all points are within the -50 to 50 constraint
    if all(-50 <= coord <= 50 for coord in cube[1:]):
        # shifting all points up 50 to make in the array 0-100
        x1, x2, y1, y2, z1, z2 = map(lambda x: x + 50, cube[1:])
        space[x1:x2+1, y1:y2+1, z1:z2+1] = int(cube[0])
# adding the list
print(f"Part 1 Solution - {np.sum(space)}")

# returns the bounds of the 1D intersection
def get_low_high(a1, a2, low, high):
    return min(max(a1, low), high), min(max(a2, low), high)

def non_overlapping(coords, rest):
    x1, x2, y1, y2, z1, z2 = coords[1:]
    # total volume of the cube
    volume = abs(x2+1 - x1) * abs(y2+1 - y1) * abs(z2+1 - z1)
    intersects = []
    for cube in rest:
        # cant be intersecting
        if cube[1] > x2 or cube[2] < x1 or cube[3] > y2 or cube[4] < y1 or cube[5] > z2 or cube[6] < z1:
            continue
        # must be intersecting so add the intersection cuboid
        intersects.append([cube[0], *get_low_high(cube[1], cube[2], x1, x2), *get_low_high(cube[3], cube[4], y1, y2), *get_low_high(cube[5], cube[6], z1, z2)])
    # find the non conflicting volume
    for i, cube in enumerate(intersects):
        volume -= non_overlapping(cube, intersects[i+1:])
    return volume

n = 0
for i, cube in enumerate(cubes):
    if cube[0]:
        n += non_overlapping(cube, cubes[i+1:])
print(f"Part 2 Solution - {n}")