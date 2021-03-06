class N:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def nodeDepths(tree, depth = 0):
    if tree is None:
        return 0
    return depth + nodeDepths(tree.left, depth+1) + nodeDepths(tree.right, depth+1)

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = N(1), N(2), N(3), N(4), N(5), N(6), N(7), N(8), N(9), N(10)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7
n4.left, n4.right = n8, n9
n5.left = n10


print(nodeDepths(n1))

'''

dfs(lf, dp + 1) + dfs(rt + dp + 1) + depth

1:            1                       dp  +  dfs(l, dp+1)  +  dfs(r, dp+1) 
           /     \                      
2:        2       3                  + 0         14                5         = 19
        /  \     /  \         
3:     4    5   6    7               + 1          8                5         = 14 (left node 2 childs)
      / \    \   \    \         
4:   8   9   10   N    N             + 2          3                3         = 8  (left node 4 childs)
    / \ / \    \         
5: N  N N  N    N                    + 3          0                0         = 3  (RET current node at each leaf) 


1: dfs(1, 0)
2:   0 + dfs(2, 1) + dfs(3, 1)
3:   1 + dfs(4, 2) + dfs(5, 2)              
4:      2 + dfs(8, 3) + dfs(9, 3)           
5:         3 + dfs(None, 4) + dfs(None, 4)    3 RET
5:         3 + dfs(None, 4) + dfs(None, 4)    3 RET
4:      2 + 3 + 3 = 8 RET                     8 RET
3:   1 + 8 + dfs(5,2)
4:      2 + dfs(10, 3)
5:         3 + dfs(None, 4)
4:      2 + 3 = 5 RET                         5 RET
3:   1 + 8 + 5 = 14 RET
2:   0 + 14 + dfs(3, 1)
3:   1 + dfs(6, 2) + dfs(7, 2)
4:     2 + dfs(None, 3) + dfs(None, 3)        2 RET
4:     2 + dfs(None, 3) + dfs(None, 3)        2 RET
3:   1 + 2 + 2 = 5 RET                        5 RET
2:   0 + 14 + 5 = 19 RET                     19 RET

'''
