'''
            1                       
         /     \                      1 + 1 = 2
        2       3                 
      /  \     /  \                   2 + 2 + 2 + 2 = 8
     4    5   6    7               
    / \    \                          3 + 3 + 3 = 9
   8   9   10
                                      Total = 2 + 8 + 9
'''
class N:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def nodeDepths(node):
    
    a = []
    nodeDepthsHelper(node, a, 0)
    print(a)
    return sum(a)

def nodeDepthsHelper(node, a, lvl):
    if node is None:
        return
    a.append(lvl)

    nodeDepthsHelper(node.left, a, lvl+1)
    nodeDepthsHelper(node.right, a, lvl+1)


n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = N(1), N(2), N(3), N(4), N(5), N(6), N(7), N(8), N(9), N(10)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7
n4.left, n4.right = n8, n9
n5.left = n10


print(nodeDepths(n1))