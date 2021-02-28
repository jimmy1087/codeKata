class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
def preOrderTraverse(node, array):
    if node is None:
        return
    array.append(node.value)
    preOrderTraverse(node.left, array)
    preOrderTraverse(node.right, array)
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

print(preOrderTraverse(n10, []))


'''
         A
       /   \
      B     C
     / \   / \
    D   E F   G
'''

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')

a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

print(preOrderTraverse(a, []))