class N:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeInfo:
    def __init__(self, isBalance, maxHeight):
        self.isBalance = isBalance
        self.maxHeight = maxHeight

def isBalance(node):
    tree = isTreeHeightBalance(node)
    return tree.isBalance

def isTreeHeightBalance(node):

    if node is None:
        return TreeInfo(True, -1)

    leftNode = isTreeHeightBalance(node.left)
    rightNode = isTreeHeightBalance(node.right)

    isBalance = (
        leftNode.isBalance and
        rightNode.isBalance and
        abs(leftNode.maxHeight - rightNode.maxHeight) <= 1
    )
    height = max(leftNode.maxHeight, rightNode.maxHeight) + 1
    return TreeInfo(isBalance, height)


'''
         1
       /   \
      2     3
     / \     \
    4   5     6
       / \
      7   8
'''

n1, n2, n3, n4, n5, n6, n7, n8 = N(1), N(2), N(3), N(4), N(5), N(6), N(7), N(8)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n5.left, n5.right = n7, n8
n3.right = n6

print(isTreeHeightBalance(n1))