'''
Given a binary tree, get the average value at each level of the tree

Input:
    
    4
   / \
  7   9
 / \   \
10  2   6
     \
      8
     /
    1

Each tuple stores (Node, NumItems, LevelOfTree)

queue   = [(4,1,0)]
current = (4,1,0)  // queue = []
data    = { 0: (4,1,0) }
queue   = [(7,1,1), (9,1,1)]

current = (7,1,1)  // queue = [(9,1,1)]
data    = { 0: (4,1,0), 1:(7,1,1) }
queue   = [(9,1,1), (10,1,2), (2,1,2)]

current = (9,1,1) // queue = [(10,1,2), (2,1,2)]
data    = { 0: (4,1,0), 1:(16,2,1) }
queue   = [(10,1,2), (2,1,2), (6,1,2)]

current = (10,1,2) // queue = [(2,1,2), (6,1,2), (8,1,3)]
data    = { 0: (4,1,0), 1:(16,2,1), 2: (10,1,2)}
queue   = [(2,1,2), (6,1,2)]

current = (2,1,2)  // queue = [(6,1,2), (8,1,3)]
data    = { 0: (4,1,0), 1:(16,2,1), 2: (12,2,2)}
queue   = [(6,1,2), (8,1,3)]

current = (6,1,2)  // queue = [(8,1,3)]
data    = { 0: (4,1,0), 1:(16,2,1), 2: (18,3,2)}
queue   = [(8,1,3)]

current = (8,1,3)  // queue = []
data    = { 0: (4,1,0), 1:(16,2,1), 2: (18,3,2), 3: (8,1,3)}
queue   = [(2,1,4)]

current = (1,1,4)  // queue = []
data    = { 0: (4,1,0), 1:(16,2,1), 2: (18,3,2), 3: (8,1,3), 4: (1,1,4)}
queue   = []
'''

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def collectData(node, data, lvl = 0):
    queue = [(node, 1, lvl)]
    while queue:
        n, items, lvl = queue.pop(0)

        if lvl not in data:
            data[lvl] = (n.value, 1, lvl)
        else:
            sumItems, numItems, x = data[lvl]
            data[lvl] = (sumItems + n.value, numItems + 1, lvl)

        print(data)
        
        if n.left is not None:
            queue.append((n.left, 1, lvl+1))
        if n.right is not None:
            queue.append((n.right, 1, lvl+1))

def avgValues(data):
    r = []
    for lvl in data:
        sumItems, numItems, lvl = data[lvl]
        r.append(sumItems//numItems)
    return r

'''
    4
   / \
  7   9
 / \   \
10  2   6
     \
      8
     /
    1
'''

# Data for test
n1, n2, n7, n9, n10, n6, n8, n4 = Node(1), Node(2), Node(7), Node(9), Node(10), Node(6), Node(8), Node(4)
n4.left, n4.right = n7, n9
n7.left, n7.right = n10, n2
n9.right = n6
n2.right = n8
n8.left = n1

# Test
dataPerRow = {}
collectData(n4, dataPerRow)
print("DataPerRow: ", dataPerRow)
response = avgValues(dataPerRow)
print(response)