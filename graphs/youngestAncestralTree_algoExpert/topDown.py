#Incorrect approach to actual problem. !!!READ careful.
#Anyway.... having a complete tree starting from the root this solution would work.

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	commonAncestor = dfs(topAncestor, descendantOne, descendantTwo)
	return commonAncestor[1]

# o(n) time | o(1)
def dfs(node, dOne, dTwo):
	if node is None:
		return (False, None)
		
	if node.name is dOne.name or node.name is dTwo.name:
		return (True, None)  # Found descendant
		
	findLeft = dfs(node.left, dOne, dTwo)
	if findLeft[1] is not None:  # Common ancestor has been found on leftSubTree.  Return
		return findLeft
		
	findRight = dfs(node.right, dOne, dTwo)
	if findRight[1] is not None: # Common ancestor has been found on rightSubTree. Return
		return findRight
	
	commonNode = None
	if findLeft[0] and findRight[0]:  # Preorder traversal: evaluate if both branches have descendants
		commonNode = node.name        # Ancestor found.
		
	return ((findLeft[0] or findRight[0]), commonNode)
	
'''
PSEUDO
dfs(node, dOne, dTwo):

	if node is None:
		return (False, None)
		
	if node is dOne or node is dTwo:
		return (True, None)
		
	findLeft = dfs(node.left, dOne, dTwo)
	if findLeft[1] is not None:
		return findLeft
		
	findRight = dfs(node.right, dOne, dTwo)
	if findRight[1] is not None:
		return findRight
	
	commonNode = None
	if findLeft[0] and findRight[0]:
		commonNode = node.name
		
	return ((findLeft[0] or findRight[0]), commonNode)
'''
'''
Tests:
        A
      /   \
     B     C
    / \   / \
   D   E F   G
  / \
 H   I

descendantOne = E
descendantTwo = I
'''

A, B, C = Node('A'), Node('B'), Node('C')
D, E, F = Node('D'), Node('E'), Node('F')
G, H, I = Node('G'), Node('H'), Node('I')
A.left, A.right = B, C
B.left, B.right = D, E
D.left, D.right = H, I
C.left, C.right = F, G

print(getYoungestCommonAncestor(A, E, I)) # --> B