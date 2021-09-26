class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preOrder(tree):
    if tree is None:
        return    
    print(tree.value)
    preOrder(tree.left)
    preOrder(tree.right)

def inOrder(tree):
    if tree is None:
        return
    inOrder(tree.right)
    print(tree.value)
    inOrder(tree.left)

def posOrder(tree):
    if tree is None:
        return
    posOrder(tree.left)
    posOrder(tree.right)
    print(tree.value)


t10, t6, t13, t4, t6_2, t11, t14, t5, t7 = Node(10), Node(6), Node(13), Node(4), Node(6), Node(11), Node(14), Node(5), Node(7)
t10.left, t10.right = t6, t13
t6.left, t6.right = t4, t6_2
t4.right = t5
t6_2.right = t7
t13.left, t13.right = t11, t14

inOrder(t10)