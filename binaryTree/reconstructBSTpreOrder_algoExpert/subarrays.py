
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reconstructBst(preOrderTraversalValues):
	if len(preOrderTraversalValues) == 0:
		return None
	
	currentValue = preOrderTraversalValues[0]
	rightIdx = len(preOrderTraversalValues)
	
	for idx in range(1, len(preOrderTraversalValues)):
		value = preOrderTraversalValues[idx]
		if value >= currentValue:
			rightIdx = idx
			break
	
	leftSubtree = reconstructBst(preOrderTraversalValues[1:rightIdx])
	rightSubTree = reconstructBst(preOrderTraversalValues[rightIdx:])
	return BST(currentValue, leftSubtree, rightSubTree)

#--------------------------------

def printBTSinPreOrder(node):
    if node is None:
        return
    print(node.value)
    printBTSinPreOrder(node.left)
    printBTSinPreOrder(node.right)

a = [10, 4, 2, 1, 5, 17, 19, 18]
r = reconstructBst(a)
printBTSinPreOrder(r)