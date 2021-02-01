'''
Print vertical nodes, Vertical nodes have the same column index. Print from left to right, top to bottom

          6
       /     \
      4       3
     /  \   /  \
    7    2 10   -1
        /   \
       0     9

colIdx:  value
-2: 7
-1: 4, 0
 0: 6, 2, 10
+1: 3, 9
+2: -1 

Print order
7, 4, 0, 6, 2, 10, 3, 9, -1
--------------------------------------

queue: [(0, -1), (9, +1)]

node: 0 
colIdx: -1

data: { 0: [(6, 0), (2, 0), (10, 0)], -1: [(4, -1), (0, -1)], +1: [(3, +1), (9, +1)], -2: [(7, -2)], +2: (-1, +2) }

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def collectData(node, data, colIdx = 0):
    queue = [(node, colIdx)]
    while queue:
        node, colIdx = queue.pop(0)

        if colIdx not in data:
            data[colIdx] = [(node.value, colIdx)]
        else:
            data[colIdx].append((node.value, colIdx))

        if node.left is not None:
            queue.append((node.left, colIdx - 1))
        if node.right is not None:
            queue.append((node.right, colIdx + 1))

def printVertical(data):
    r = []
    for colIdx in sorted(data):
        for items in data[colIdx]:
            r.append(items[0])
    return r

    #return [[ item for (item, i) in data[colIdx] ] for colIdx in sorted(data) ]   -- It does not works, cause item is an array.


n6 = Node(6)
n4 = Node(4)
n3 = Node(3)
n7 = Node(7)
n2 = Node(2)
n0 = Node(0)
n3 = Node(3)
n10 = Node(10)
n9 = Node(9)
nn1 = Node(-1)

n6.left, n6.right = n4, n3
n4.left, n4.right = n7, n2
n3.left, n3.right = n10, nn1
n2.left = n0
n10.right = n9

d = {}
collectData(n6, d)
print(printVertical(d))
