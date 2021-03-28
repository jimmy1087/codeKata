
def validBST(node):
    return validBSTHelper(node, float('-inf'), float('inf'))

def validBSTHelper(node, minVal, maxVal):
    if node is None:
        return True

    print(str(minVal)+':'+str(node.val)+':'+str(maxVal))

    if node.val < minVal or node.val > maxVal:
        return False
    
    return validBSTHelper(node.left, minVal, node.val) and validBSTHelper(node.right, node.val, maxVal)
'''
Valid BST
         10
       /    \
      5     15
     / \   /  \
    2   5 13  22
   /        \
  1         14

10)    v(10, -inf, inf)                                              -inf:10:inf
5|15)    v(5, -inf, 10) && v(15, 10, inf)                     -inf:5:10           10:15:inf
2|5)       v(2, -inf, 5) && v(5, 5, 10)                    -inf:2:5  5:5:10   10:13:15     15:22:inf
1)           v(1, -inf, 2)                               -inf:1:2                13:14:15
1)             return True
2)           return True
5)         return True && v(5, 5, 10)
_|5)         return True
5)         return True && True

'''
class N:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

n10, n5, n15, n2, n5_2, n1, n13, n22, n14 = N(10), N(5), N(15), N(2), N(5), N(1), N(13), N(22), N(14)
n10.left, n10.right = n5, n15
n5.left, n5.right = n2, n5_2
n2.left = n1
n15.left, n15.right = n13, n22
n13.right = n14
print('TEST VALID BST')
print(validBST(n10))
print('TEST RETURN INVALID BST')
'''
Invalid BST
         10
       /    \
      5     15
     / \   /  \
    2   4 13  22
   /        \
  1         14
'''

n10, n5, n15, n2, n4, n1, n13, n22, n14 = N(10), N(5), N(15), N(2), N(4), N(1), N(13), N(22), N(14)
n10.left, n10.right = n5, n15
n5.left, n5.right = n2, n4
n2.left = n1
n15.left, n15.right = n13, n22
n13.right = n14

print(validBST(n10))

print('TEST LESS THAN OR EQUAL TO THE RIGHT')
'''
Invalid BST
         5
       /    \
      5     15
     / \   /  \
    2   5 13  22
   /        \
  1         14
'''

n5_0, n5, n15, n2, n5_2, n1, n13, n22, n14 = N(5), N(5), N(15), N(2), N(5), N(1), N(13), N(22), N(14)
n5_0.left, n5_0.right = n5, n15
n5.left, n5.right = n2, n5_2
n2.left = n1
n15.left, n15.right = n13, n22
n13.right = n14

print(validBST(n5_0))