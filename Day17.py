# only need y velocity for part 1
def runy(vy, ty1, ty2, zero = False):
    y = 0
    while not y < ty2:
        y += vy
        vy -= 1
        # maxima at velocity = 0
        if zero and vy == 0:
            return y
        if ty1 <= y <= ty2:
            return True
    return False


def simulate(vx, vy, tx1, tx2, ty1, ty2):
    x, y = 0, 0
    while True:
        x, y = x + vx, y + vy
        vx, vy = max(vx-1, 0), vy - 1
        # in the given area
        if tx1 <= x <= tx2 and ty1 <= y <= ty2:
            return True
        if x > tx2 or y < ty1:
            return False
        if vx == 0 and not tx1 <= x <= tx2:
            return False

# getting data
data = open("Day17.txt").read().strip()
parts = data.split(" ")
tx1 = parts[2]
ty1 = parts[-1]
tx1, tx2 = tx1.split("..")
ty1, ty2 = ty1.split("..")
# inting everything
tx1, tx2, ty1, ty2 = list(map(int, [tx1[2:], tx2[:-1], ty1[2:], ty2]))

out = False
vy = 0
last = 0
# multiple values skip so we have this to get maximum value
c = 0
while not out:
    vy += 1
    if runy(vy, ty1, ty2):
        last = vy
        vy += 1
    else:
        c += 1
    if c == 100:
        print("Part 1 Solution -", runy(last, ty1, ty2, True))
        break
c = 0
# all velocities
for vy in range(ty1, last+1):
    for vx in range(tx2+1):
        if simulate(vx, vy, tx1, tx2, ty1, ty2):
            c += 1
print("Part 2 Solution -", c)
