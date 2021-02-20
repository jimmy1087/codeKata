'''

Given a binary tree, get the averare value at each level of the tree

Input:
    
    4
   / \
  7   9
 / \   \
10  2   6
     \
      6
     /
    2
    
Output:

[4, 8, 6, 6, 2]

    lv: 0  data: { 0: (4, 1) }
v.l lv: 1  data: { 0: (4, 1), 1: (7, 1) }
v.l lv: 2  data: { 0: (4, 1), 1: (7, 1), 2: (10, 1) }
^
v.r lv: 2  data: { 0: (4, 1), 1: (7, 1), 2: (12, 2) }
v.r lv: 3  data: { 0: (4, 1), 1: (7, 1), 2: (12, 2), 3: (6, 1) }
v.l lv: 4  data: { 0: (4, 1), 1: (7, 1), 2: (12, 2), 3: (6, 1), 4: (2, 1) }
^ * 4
v.r lv: 1  data: { 0: (4, 1), 1: (16, 2), 2: (12, 2), 3: (6, 1), 4: (2, 1) }
v.r lv: 2  data: { 0: (4, 1), 1: (16, 2), 2: (18, 3), 3: (6, 1), 4: (2, 1) }
^ * 2

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def collectDataPerLevel(node, data, level = 0):
    if node is None:
        return
    
    if level in data:
        sumItems, cntItems = data[level]
        data[level] = (sumItems + node.value, cntItems + 1)
    else:
        data[level] = (node.value, 1)
    
    collectDataPerLevel(node.left, data, level + 1)
    collectDataPerLevel(node.right, data, level + 1)
    
def avgPerLevel(data):
    r = []
    for lv in data:
        sumItems, cntItems = data[lv]
        avg = sumItems // cntItems
        r.append(avg)
    return r

# o(n) time | o(n) space

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