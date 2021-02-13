class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
def inOrderTraverse(node, array):
    if node is None:
        return
    inOrderTraverse(node.left, array)
    array.append(node.value)
    inOrderTraverse(node.right, array)
    return array
'''
     10
    /  \
   4    9
  /    / \
 2    7   12
       \
        8
'''
n10 = Node(10)
n4 = Node(4)
n9 = Node(9)
n2 = Node(2)
n7 = Node(7)
n8 = Node(8)
n12 = Node(12)

n10.left, n10.right = n4, n9
n4.left = n2
n9.left, n9.right = n7, n12
n7.right = n8

print(inOrderTraverse(n10, []))