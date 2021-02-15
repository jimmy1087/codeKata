'''
Return the closest value to a target value in a BST

Target: 12

         10
       /    \
      5     15
     / \    / \
    2   5  13  22
   /        \
  1         14

  Return: 13

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def closestValue(node, target):

    currentNode = node
    closest = float('inf')
    while currentNode is not None:

        if abs(target-currentNode.value) < abs(target-closest):
            closest = currentNode.value
        
        if target < currentNode.value:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

    return closest

'''
Target: 12

           10           [10] close: abs(12-10) = 2  or abs(12-inf) = inf    ... closeNode: 10
         /    \
        5     15        [15] close: abs(12-15) = 3  or abs(12-10)  = 2      ... closeNode: 10
       / \    / \
      2   5  13  22     [13] close: abs(12-13) = 1  or abs(12-10)  = 2      ... closeNode: 13
     /         \      
    1           14      [14] close: abs(12-14) = 2  or abs(12-13)  = 1      ... closeNode: 13

Return: 13
'''

n1, n2, n5, n5_2 = Node(1), Node(2), Node(5), Node(5)
n10, n15, n13, n14, n22 = Node(10), Node(15), Node(13), Node(14), Node(22)

n10.left, n10.right = n5, n15

n5.left, n5.right = n2, n5_2
n2.left = n1

n15.left, n15.right = n13, n22
n13.right = n14

print('Target: 12', 'Out:', closestValue(n10, 12))