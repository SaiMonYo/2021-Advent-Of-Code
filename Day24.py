import functools
from time import perf_counter

with open("Day24.txt") as file:
	# parsing
	chunks = [chunk.split("\n") for chunk in file.read().replace("inp", "\ninp").lstrip().split("\n\n")]
	digits = []
	for chunk in chunks:
		up = chunk[4].endswith('1')
		sub = int(chunk[5].split(' ')[-1])
		val = int(chunk[-3].split()[-1])
		digits.append((up, sub, val))


# memoization
@functools.cache
def solve(vars, rev, z):
	# reached the end and we found a good number
	if len(vars) == 0 and z == 0:
		return " "
	up, sub, val = vars[0]
	if up:
		# if were looking for minimum value we will start at 1, otherwise 9
		for i in list(range(1,10))[::rev]:
			# z = 26z + w + value 3 above inp
			result = solve(vars[1:], rev, val + i + 26 * z)
			if result:
				return str(i) + result
	else:
		# needs to decrease
		digit = (z % 26) + sub
		# if were looking for minimum value we will start at 1, otherwise 9
		if digit in list(range(1, 10))[::-1]:
			result = solve(vars[1:], rev, z // 26)
			# is not None, weve got a good result
			if result:
				return str(digit) + result
	# not needed as if it reached here it wouldn't return anything "None"
	# helps with clarity though
	return None

# tuple so it can be hashed
# only need to try 9^7 possibilities
# as we can work out what the other values need to be
# and this can be reduced further by going digit by digit
# only around 500k calls to solve function
# runs in 0.4 seconds no memoization, 0.02 with
digits = tuple(digits)
t = perf_counter()
print(f"Part 1 Solution - {solve(digits,-1, 0)}")
print(f"Part 2 Solution - {solve(digits, 1, 0)}")
print((perf_counter() - t) * 1000)