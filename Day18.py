# representation of snail number
#
# [[1, 2], [3, [4, 5]]] ==
#             /\
#            /  \
#           /    \
#          / \ /  \
#         1  2 3 / \  
#                4  5


class Node:
    # only has value if left or/and right == None
    def __init__(self, val=None, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def parse(fish_num):
    # parsing to tree structure
    # if it is an integer, type(fish_num) == int: is slower
    if isinstance(fish_num, int):
        return Node(fish_num)
    # recursive parsing/branching
    root = Node(None, parse(fish_num[0]), parse(fish_num[1]))
    root.left.parent = root
    root.right.parent = root
    # needs to be in simpliest terms
    reduce(root)
    return root


def add(a, b):
    # create new pair with a and b as branches
    root = Node(None, a, b)
    root.left.parent = root
    root.right.parent = root
    reduce(root)
    return root


def magnitude(root):
    # is a leaf, half of a pair
    if isinstance(root.val, int):
        return root.val
    # recursive call
    return 3 * magnitude(root.left) + 2 * magnitude(root.right)


def reduce(root):
    # Depth First Search (DFS) on the number
    # assume already simpliest
    # this gets changed throughout the code
    done = True
    # Handling explosions
    stack = [(root, 0)]
    while len(stack) > 0:
        node, depth = stack.pop()
        if not node:
            continue
        # condition for explosion
        if depth >= 4 and node.val == None and (not (node.left and node.right) or (node.left.val != None and node.right.val != None)):
            # go up the tree to add to
            prev_node = node.left
            cur_node = node
            # moving up
            while cur_node and (cur_node.left == prev_node or cur_node.left == None):
                prev_node = cur_node
                cur_node = cur_node.parent
            # if there is a left branch
            # otherwise we just discard the left side 
            if cur_node != None:
                # there is a left child now
                cur_node = cur_node.left
                while cur_node.val == None:
                    if cur_node.right != None:
                        cur_node = cur_node.right
                    else:
                        cur_node = cur_node.left
                # adding to the left value
                cur_node.val += node.left.val
            # moving up the tree for first right value
            prev_node = node.right
            cur_node = node
            while cur_node and (cur_node.right == prev_node or cur_node.right == None):
                prev_node = cur_node
                cur_node = cur_node.parent
            # needs a right node otherwise discard like before
            if cur_node != None:
                cur_node = cur_node.right
                while cur_node.val == None:
                    if cur_node.left != None:
                        cur_node = cur_node.left
                    else:
                        cur_node = cur_node.right
                cur_node.val += node.right.val
            # exploded so we remove those left and right nodes
            # we found an explosion so we set done to false aswell
            node.val, node.left, node.right, done = 0, None, None, False
            break
        # add to the stack
        stack.append((node.right, depth + 1))
        stack.append((node.left, depth + 1))
    if not done:
        # all explosions before splits
        reduce(root)
        return

    # handling splits after the explosions
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node == None:
            continue
        if node.val != None and node.val >= 10:
            # creating a new pair below
            node.left = Node(node.val//2, parent = node)
            node.right = Node(node.val - (node.val//2), parent = node)
            node.val = None
            done = False
            break
        # add to the stack
        stack += [node.right, node.left]
    if not done:
        reduce(root)


with open("Day18.txt") as file:
    # eval runs the code, can be bad, so turns the line to a literal list
    # can use ast.literal_eval which only runs if data structure which is safer
    data = [eval(line) for line in file.read().split("\n")]
    # adding all lines together
    root = parse(data[0])
    for line in data:
        root = add(root, parse(line))
    print(f"Part 1 Solution - {magnitude(root)}")


# all permutations of numbers added
# keep track of best
best = 0
for i in range(len(data)):
    for j in range(len(data)):
        # need to be different
        if i == j:
            continue
        a, b = parse(data[i]), parse(data[j])
        best = max(magnitude(add(a, b)), best)
print(f"Part 2 Solution - {best}")
