class AncestralTree:
	def __init__(self, name):
		self.name = name
		self.ancestor = None

# o(d) | o(1)  d: longest depth of any of the descendants
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDepth(descendantOne)
	depthTwo = getDepth(descendantTwo)

	if depthOne > depthTwo:
		return backTrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return backTrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getDepth(node):
	depth = 0
	while node.ancestor is not None:
		node = node.ancestor
		depth += 1
	return depth

def backTrackAncestralTree(lowNode, highNode, depth):
	while depth > 0:
		lowNode = lowNode.ancestor
		depth -= 1
	while lowNode != highNode:
		lowNode = lowNode.ancestor
		highNode = highNode.ancestor
	return lowNode.name

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

A, B, C = AncestralTree('A'), AncestralTree('B'), AncestralTree('C')
D, E, F = AncestralTree('D'), AncestralTree('E'), AncestralTree('F')
G, H, I = AncestralTree('G'), AncestralTree('H'), AncestralTree('I')
A.ancestor = None
B.ancestor, C.ancestor = A, A
D.ancestor, E.ancestor = B, B
H.ancestor, I.ancestor = D, D
F.ancestor, G.ancestor = C, C

print(getYoungestCommonAncestor(A, E, I)) # --> B