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

queue = [6]
level_size = 1
level = 2
data = { 0: (4, 1), 1: (16, 2), 2: (18, 3), }

result = [4, 8, 6, 6, 2]
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def collectDataInBFS(node, data, level = 0):
    queue = [node]
    while queue:
        itemsPerLevel = len(queue)
        while itemsPerLevel:  
            itemsPerLevel -= 1
            node = queue.pop(0)

            if level not in data:
                data[level] = (node.value, 1)
            else:
                itemsSum, itemsCounter = data[level]
                data[level] = (itemsSum + node.value, itemsCounter + 1)
            
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        level += 1

def avgPerLevel(data):
    result = []
    for level in data:
        rowSum, items = data[level]
        avgItem = rowSum // items
        result.append(avgItem)
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
collectDataInBFS(n4, d)
print(d)
print(avgPerLevel(d))
