class N:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def nodeDepths(tree):
    a = []
    nodeDepthsHelper(tree, a, 0)
    return sum(a)

def nodeDepthsHelper(node, a, curSum):
    if node is None:
        return 0

    nodeDepthsHelper(node.left, a, curSum + 1)
    nodeDepthsHelper(node.right, a, curSum + 1)
    
    a.append(curSum)

'''
            1                       
         /     \                      
        2       3                 
      /  \     /  \         
     4    5   6    7               
    / \    \    
   8   9   10 

    dfs(2, 1)
        dfs(4, 2)
            dfs(8, 3)
                dfs(None, 4) ... ret 0
                dfs(None, 4) ... ret 0
                a[3]
            dfs(9, 2)
                dfs(None, 4) ... ret 0
                dfs(None, 4) ... ret 0
                a[3,3]
            a[3,3,2]
        dfs(5, 2)
            dfs(None, 3) ... ret 0
            dfs(10, 3)   
                dfs(None, 4) ... ret 0
                dfs(None, 4) ... ret 0
                a[3, 3, 2, 3]
            a[3, 3, 2, 3, 2]
        a[3, 3, 2, 3, 2, 1]
    dfs(3, 1)
        dfs(6, 2)
            dfs(None, 3) ... ret 0
            dfs(None, 3) ... ret 0
            a[3, 3, 2, 3, 2, 1, 2]
        dfs(7, 2)
            dfs(None, 3) ... ret 0
            dfs(None, 3) ... ret 0
            a[3, 3, 2, 3, 2, 1, 2, 2]
        a[3, 3, 2, 3, 2, 1, 2, 2, 1]
      
sum([3, 3, 2, 3, 2, 1, 2, 2, 1]) = 19

'''




n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = N(1), N(2), N(3), N(4), N(5), N(6), N(7), N(8), N(9), N(10)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7
n4.left, n4.right = n8, n9
n5.left = n10


print(nodeDepths(n1))