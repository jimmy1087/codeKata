'''
Return the closest value to a target value in a BST

         10
       /    \
      5     15
     / \    / \
    2   5  13  22
   /        \
  1         14

  Target: 12
  Return: 13

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def closestValue(node, target):
    return closestValueHelper(node, target, float('inf'))

# o(log(n)) Time | o(log(n)) space b/for each level a recursion call is stored in the stack
def closestValueHelper(node, target, closest):
    # base case
    if node is None:
        return closest  # Important to Bubble up value, cause otherwise the closest will not change at each level of the tree!

    # main operation
    if abs(target-node.value) < abs(target-closest):
        closest = node.value

    #DFS
    if target > node.value:
        return closestValueHelper(node.right, target, closest)
    else:
        return closestValueHelper(node.left, target, closest)

'''
Target: 12

           10           [10] close: abs(12-10) = 2  or abs(12-inf) = inf    ... closeNode: 10
         /    \
        5     15        [15] close: abs(12-15) = 3  or abs(12-10)  = 2      ... closeNode: 10
       / \    / \
      2   5  13  22     [13] close: abs(12-13) = 1  or abs(12-10)  = 2      ... closeNode: 13
     /         \      
    1           14      [14] close: abs(12-14) = 2  or abs(12-13)  = 1      ... closeNode: 13 // Actually, this will not evaluate, cause the left node of 13 is None.

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