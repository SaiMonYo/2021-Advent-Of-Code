import itertools
import functools

def Die():
    # generator, handles die for part 1
    while True:
        yield from range(1, 101)

score1, score2, pos1, pos2, n, die = 0, 0, 6, 1, 0, Die()
# looping until either wins
while score1 < 1000 and score2 < 1000:
    # player 1's turn
    pos1 += next(die) + next(die) + next(die)
    pos1 = (pos1 - 1) % 10 + 1
    score1 += pos1
    n += 3
    # player 1 can win mid loop
    if score1 >= 1000:
        break
    # player 2's turn
    pos2 += next(die) + next(die) + next(die)
    pos2 = (pos2 - 1) % 10 + 1
    score2 += pos2
    n += 3
print(f"Part 1 solution - {min(score1, score2) * n}")


# caching args against return (memoization)
# was using a dictionary but using all args as a key
# so caching is easier and faster
@functools.lru_cache(maxsize = None)
def winner(current_pos, next_pos, current_score, next_score):
    # only need to check this value as other score was checked last call
    if next_score > 20:
        return 0, 1
    out = [0, 0]
    # 1, 1, 1  1, 1, 2 ... same as a nested nested for loop of ranges 1-4
    for x, y, z in itertools.product([1, 2, 3], repeat = 3):
        # adding to the pos and cycling
        next_current_pos = current_pos + x + y + z
        next_current_pos = (next_current_pos - 1) % 10 + 1
        next_current_score = current_score + next_current_pos
        # recursive call
        a, b = winner(next_pos, next_current_pos, next_score, next_current_score)
        out = [out[0] + b, out[1] + a]
    return out
print(f"Part 2 Solution - {max(winner(6, 1, 0, 0))}")
