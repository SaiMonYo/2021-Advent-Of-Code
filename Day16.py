class Packet:
    def __init__(self, v, i, lit, subs):
        self.v = v
        self.i = i
        self.lit = lit
        self.subs = subs

    def part2(self):
        match self.i:
            case 0:
                # summing all the packets/subpackets (recursive)
                return sum(p.part2() for p in self.subs)
            case 1:
                # product of all packets/subpackets (recursive)
                a = 1
                for p in self.subs:
                    a *= p.part2()
                return a
            case 2:
                # minimum in packets/subpackets (recursive)
                return min(p.part2() for p in self.subs)
            case 3:
                # maximum of packets/subpackets (recursive)
                return max(p.part2() for p in self.subs)
            case 4:
                # literal case
                return self.lit
            case 5:
                # subpacket 2 is bigger 1st or 2nd (recursive)
                return self.subs[0].part2() > self.subs[1].part2()
            case 6:
                # subpacket 1 is smaller (recursive)
                return self.subs[0].part2() < self.subs[1].part2()
            case 7:
                return self.subs[0].part2() == self.subs[1].part2()  


# returns the decimal conversion from binary
def fbin(string):
    return int(string, 2)

# returns start and remaining bits
def eat(string, pos, initial = 0):
    return string[initial:pos], string[pos:]


def parse():
    # we need to modify string in place
    global bits
    # version, id, bits, literal number
    v = fbin(bits[0:3])
    bid = fbin(bits[3:6])
    bits = bits[6:]
    lit = ""
    subs = []
    if bid == 4:
        # has a significant bit
        while bits[0] != "0":
            # eat in 4s
            c, bits = eat(bits, 5, 1)
            # add eaten bits to literal
            lit += c
        # need one more
        c, bits = eat(bits, 5, 1)
        # decimal
        lit = fbin(lit + c)
        return Packet(v, bid, lit, subs)
    # lead 0
    if bits[0] == "0":
        # remove non needed 0
        bits = bits[1:]
        # 15 bits
        l, bits = eat(bits, 15)
        # bits is changing in place
        current_l = len(bits)
        while current_l - len(bits) < fbin(l):
            # adding recursive subpackets to main outer packet
            subs.append(parse())
    else:
        bits = bits[1:]
        # 11 bits
        ran, bits = eat(bits, 11)
        for _ in range(fbin(ran)):
            subs.append(parse())
    return Packet(v, bid, lit, subs)
        
def part1(outer):
    if outer.subs == []:
        return outer.v
    return outer.v + sum(part1(p) for p in outer.subs)

conv = {"0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"}


with open("Day16.txt") as file:
    raw = file.read().split("\n")[0]
    # hex to bits
    bits = ""
    for d in raw:
        bits += conv[d]
# output
outer = parse()
print(f"Part 1 solution = {part1(outer)}")
print(f"part 2 solution = {outer.part2()}")