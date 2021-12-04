class Board:
    def __init__(self, board):
        # complicated list comprehension
        # splitting into rows, rows split by spaces
        # inting those numbers and removing "" if there are any
        self.board = [list(map(int, filter(lambda x: x != "", row.split(" ")))) for row in board.split("\n")]
        # summing entire board
        self.score = sum(sum(row) for row in self.board)


def part1(data):
    # first part
    numbers = map(int, data[0].split(","))
    data = data[1:]
    boards = []
    # creating boards
    for i, line in enumerate(data):
        b = Board(line)
        boards.append(b)

    for n in numbers:
        for b in boards:
            # was using if they had multiple of same numbers
            found = False
            for j in range(len(b.board)):
                for i in range(len(b.board[j])):
                    if b.board[j][i] == n:
                        b.score -= n
                        # marking a number as -1
                        # used 0 but that made collisions
                        b.board[j][i] = -1
                        if isWinner(b.board):
                            return b.score * n
                        found = True
                        break
                if found:
                    break


def part2(data):
    numbers = map(int, data[0].split(","))
    data = data[1:]
    boards = []
    for i, line in enumerate(data):
        b = Board(line)
        boards.append(b)
    # called numbers
    for n in numbers:
        # list that we remove at the end
        # remove at end so it doesnt affect loop
        rem = []
        for b in boards:
            found = False
            for j in range(len(b.board)):
                for i in range(len(b.board[j])):
                    if b.board[j][i] == n:
                        b.score -= n
                        b.board[j][i] = -1
                        if isWinner(b.board) and len(boards)!= 1:
                            rem.append(b)
                        # last one
                        elif isWinner(b.board):
                            return b.score * n
        # removing
        for b in rem:
            boards.remove(b)



def isWinner(board):
    for row in board:
        if all(c == -1 for c in row):
            return True
    for i in range(len(board)):
        if all(board[j][i] == -1 for j in range(len(board[-1]))):
            return True
    # diagonals but they werent needed so wasted time
    # making and debugging errrors
    '''
    if all(board[i][i] == -1 for i in range(len(board))):
        return True

    if all(board[i][len(board)-i-1] == -1 for i in range(len(board))):
        return True'''
    return False

with open("Day4.txt") as file:
    data = file.read().split("\n\n")
    #data = list(map(int, data))
    print(f"Part1 solution = {part1(data.copy())}")
    print(f"Part2 solution = {part2(data.copy())}")

