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

queue = [10, 2, 6]
level_size = 3
level = 2
data = { 0: (4,1), 1: (16,2), 2: (18,3), 3: (6,1), 4: (2,1)}

result = [4, 8, 6, 6, 2]
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def collectDataPerLevel(node, data, level = 0):
    queue = [node]
    while len(queue):
        level_size = len(queue)
        while (level_size):
            level_size -= 1
            currentNode = queue.pop(0)
            
            if level not in data:
                data[level] = (currentNode.value, 1)
            else:
                sumVal, count = data[level]
                sumVal += currentNode.value
                count  += 1
                data[level] = (sumVal, count)

            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

        level += 1
    
def avgPerLevel(data):
    result = []
    for level in data:
        sumVal, count = data[level]
        avg = sumVal // count
        result.append(avg)
    return result

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