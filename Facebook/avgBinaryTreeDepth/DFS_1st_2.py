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

data = {0: [4], 1: [7, 9], 2: [10, 2, 6], 3: [6], 4: [2]}

'''

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def collectData(node, data, level = 0):

    if node is None:
        return
    
    if level not in data:
        data[level] = [node.value]
    else:
        data[level].append(node.value)
    
    collectData(node.left, data, level + 1)
    collectData(node.right, data, level + 1)

def avgPerLevel(data):
    result = []
    for level in data:
        avg = sum(data[level]) // len(data[level])
        result.append(avg)
    return result

n4 = Node(4)
n7 = Node(7)
n9 = Node(9)
n10 = Node(10)
n2 = Node(2)
n6 = Node(6)
n6_2 = Node(6)
n2_2 = Node(2)

n4.left, n4.right = n7, n9
n7.left, n7.right = n10, n2
n2.right = n6
n6.left = n2_2
n9.right = n6_2

d = {}
collectData(n4, d)
print(d)
print(avgPerLevel(d))