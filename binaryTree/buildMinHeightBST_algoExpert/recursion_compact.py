class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildMinHeightBST(a):
    return buildMinHeightBSTHelper(a, left = 0, right = len(a)-1)

def buildMinHeightBSTHelper(a, left, right):
    if left > right:
        return None
    mid = (right + left) // 2
    n = Node(a[mid])
    n.left = buildMinHeightBSTHelper(a, left, mid - 1)
    n.right = buildMinHeightBSTHelper(a, mid + 1, right)
    return n

def printInOrder(node):
    if node is None:
        return 
    printInOrder(node.left)
    print(' ' + str(node.value))
    printInOrder(node.right)

a = [1,2,5,7,10,13,14,15,22]

n = buildMinHeightBST(a)
printInOrder(n)

'''
a = [1,2,5,7,10,13,14,15,22]
     0 1 2 3 4  5  6  7  8
l = 0, r = 8
mid = 4   n = Node(10)
n.l
    a = [1,2,5,7]
         0 1 2 3 
    l = 0, r = 3
    mid = 2   n = Node(5)
    n.l
        a = [1,2]
             0 1
             l = 0, r = 1
             mid = 1  n = Node(2)
             n.l
                a = [1]
                     0
                     l = 0  r = 0
                     mid = 0  n = Node(1)
                     n.l
                        a = []
                        l = 0   r = -1
                        return None
                     n.r
                        a = []
                        l = 1   r = 0
                        return None
            n.r
                a = [5]
                     2
                     l = 2  r = 1
                     return None
    n.r
        a = [5,7]
             2 3
             l = 2  r = 3
             mid = 



'''

