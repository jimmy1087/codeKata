class AncestralTree:
	def __init__(self, name):
		self.name = name
		self.ancestor = None

# o(d) | o(d)  d: longest depth of any of the descendants
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	
	# Edge cases; one of the descendant is the root
	if descendantOne.ancestor is None:
		return descendantOne
	if descendantTwo.ancestor is None:
		return descendantTwo
	
	ancestors = []
	
	# 1. Store all ancestors from one descendant in an array
	while descendantOne.ancestor is not topAncestor:
		descendantOne = descendantOne.ancestor
		ancestors.append(descendantOne.name)
	
	# 2. Edge case; the ancestor is the root
	if descendantOne.ancestor is topAncestor:
		ancestors.append(topAncestor.name)
	
	# 3. Traverse ancestors from second descendant and check which one is common
	while descendantTwo.name not in ancestors:
		descendantTwo = descendantTwo.ancestor
		
	return descendantTwo.name

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