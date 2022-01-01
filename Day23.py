from copy import deepcopy

# constants
columns = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
good = [0, 1, 3, 5, 7, 9, 10]

class State:
    def __init__(self, rooms, hall):
        self.rooms = rooms
        self.hall = hall

    def extend(self):
        # for part 2
        self.rooms["A"] = self.rooms["A"][:1] + ["D", "D"] + self.rooms["A"][-1:]
        self.rooms["B"] = self.rooms["B"][:1] + ["C", "B"] + self.rooms["B"][-1:]
        self.rooms["C"] = self.rooms["C"][:1] + ["B", "A"] + self.rooms["C"][-1:]
        self.rooms["D"] = self.rooms["D"][:1] + ["A", "C"] + self.rooms["D"][-1:]

    def get_items(self):
        return self.rooms, self.hall

    def done(self):
        # all rooms have to be full with the pod of the type
        for pod, room in self.rooms.items():
            for occup in room:
                if occup != pod:
                    return False
        return True

    def able_move(self, pod):
        # all are the same pod
        for test in self.rooms[pod]:
            if pod != test and test != ".":
                return False
        return True

    def able_from_pos(self, pod):
        # able to move from given position
        for test in self.rooms[pod]:
            if test != pod and test != ".":
                return True
        return False

    def get_final_pos(self, pod):
        # get the position that the pod will go to
        # enumerate before revserse to keep order
        for i, test in list(enumerate(self.rooms[pod]))[::-1]:
            if test == ".":
                return i

    def get_from_top_of_room(self, pod):
        # get the pod that is at top of a given room
        for i, c in enumerate(self.rooms[pod]):
            if c != ".":
                return i

    def is_blocking(self, c, pod, i):
        return c in range(columns[pod]+1, i) or c in range(i+1, columns[pod])

    def throughroute(self, pod, i):
        # a through route to home
        for j in range(11):
            if self.is_blocking(j, pod, i) and self.hall[j] != ".":
                return False
        return True

    def get_key(self):
        # used for hashing in the dictionary for memoization
        return hash(''.join(self.hall) + ''.join(''.join(room) for room in self.rooms.values()))

    def __hash__(self):
        # hash function for caching - not used
        return hash(''.join(self.hall) + ''.join(''.join(room) for room in self.rooms.values()))


# memoization (faster than functools cache)
cache = {}
def solve(state: State):
    if state.done():
        return 0
    key = state.get_key()
    if key in cache:
        return cache[key]
    # try moving all in hall
    for i, c in enumerate(state.hall):
        # if it is a pod and can move to its home we do that
        # priotise this, as is always best move
        if c != "." and state.able_move(c):
            if state.throughroute(c, i):
                # calculating cost of that move
                dist = state.get_final_pos(c) + 1 + abs(columns[c] - i)
                cost = costs[c] * dist
                # moving the pod into its home
                state.hall[i] = "."
                state.rooms[c][state.get_final_pos(c)] = c
                # recursion
                return cost + solve(State(*state.get_items()))

    rooms, hall = state.get_items()
    # any path will be better
    best = float("inf")
    for pod, home in rooms.items():
        if state.able_from_pos(pod):
            # get index and pod at top of a room
            j = state.get_from_top_of_room(pod)
            c = home[j]
            for i in good:
                if hall[i] == "." and state.throughroute(pod, i):
                    dist = j + 1 + abs(i - columns[pod])
                    # deepcopy the 2D array, instead of passing old array by reference
                    rooms2 = deepcopy(rooms)
                    rooms2[pod][j] = "."
                    # hall isnt passed by reference as were construction a new array by slicing in the call
                    best = min(best, costs[c] * dist + solve(State(rooms2, hall[:i] + [c] + hall[i+1:])))
    # memoization
    cache[key] = best
    return best


with open("Day23.txt") as file:
    # parsing
    raw = file.read().split("\n")
    A = [raw[2][3], raw[3][3]]
    B = [raw[2][5], raw[3][5]]
    C = [raw[2][7], raw[3][7]]
    D = [raw[2][9], raw[3][9]]

# solving
start = State({'A': A, 'B': B, 'C': C, 'D': D}, ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'])
print(f"Part 1 Solution - {solve(start)}")
start.extend()
print(f"Part 2 Solution - {solve(start)}")