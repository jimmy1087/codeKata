'''

Given a binary tree, get the averare value at each level of the tree

Input:
        4        lv = 0   data[0] = [4]
       / \
      7   9      lv = 1   data[1] = [7]
     / \   \
    10  2   6    lv = 2   data[2] = [10]  .. data[10,2]
         \
          6      lv = 3   data[3] = [6]
         /
        2        lv = 4   data[4] = [2]
    
Output:

[4, 8, 6, 6, 2]

Node(4)  lv: 0 data = { 0: [4]}
Node(7)  lv: 1 data = { 0: [4], 1: [7]}
Node(10) lv: 2 data = { 0: [4], 1: [7], 2: [10]}
up.r
Node(2)  lv: 2 data = { 0: [4], 1: [7], 2: [10, 2]}
Node(6)  lv: 3 data = { 0: [4], 1: [7], 2: [10, 2], 3: [6]}
Node(2)  lv: 4 data = { 0: [4], 1: [7], 2: [10, 2], 3: [6], 4:[2]}
up.r
Node(9)  lv: 1 data = { 0: [4], 1: [7,9], 2: [10, 2], 3: [6], 4:[2]}
Node(6)  lv: 2 data = { 0: [4], 1: [7,9], 2: [10, 2, 6], 3: [6], 4:[2]}

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# o(n) time | o(n) space
def collectDataPerLevel(node, data, level = 0):
    if node is None:
        return
    
    if level not in data:
        data[level] = [node.value]
    else:
        data[level].append(node.value)
    
    collectDataPerLevel(node.left, data, level + 1)
    collectDataPerLevel(node.right, data, level + 1)
    
def avgPerLevel(data):
    result = []
    for level in data:
        nums = data[level]
        avg = sum(nums) // len(nums)
        result.append(avg)
    return result

# Data for test
n1 = Node(4)
n1.left = Node(7)

n2l = n1.left 
n2l.left  = Node(10)
n2l.right = Node(2)

n3r = n2l.right
n3r.right = Node(6)

n4l = n3r.right
n4l.left = Node(2)

n1.right = Node(9)
n2r = n1.right 
n2r.right = Node(6)

# Test
dataPerRow = {}
collectDataPerLevel(n1, dataPerRow)
print("DataPerRow: ", dataPerRow)
response = avgPerLevel(dataPerRow)
print(response)