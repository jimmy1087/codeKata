# o(nlogn) time || o(n)
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Steps:
    def __init__(self, counter):
        self.counter = counter

def reconstructBst(preOrderTraversalValues):
    print('len(array):', len(preOrderTraversalValues))
    steps = Steps(1)
    root = BST(preOrderTraversalValues[0])
    for i in range(1, len(preOrderTraversalValues)):
        node = BST(preOrderTraversalValues[i])
        reconstructBstHelper(root, node, steps)
    print('Total steps:', steps.counter)
    return root
	
def reconstructBstHelper(root, node, steps):
    steps.counter += 1
    if node.value < root.value:
        if root.left is None:
            root.left = node
        else:
            reconstructBstHelper(root.left, node, steps)
    else:
        if root.right is None:
            root.right = node
        else:
            reconstructBstHelper(root.right, node, steps)
    return
		
#--------------------------------

def printBTSinPreOrder(node):
    if node is None:
        return
    print(node.value)
    printBTSinPreOrder(node.left)
    printBTSinPreOrder(node.right)

a = [10, 4, 2, 1, 5, 12, 11, 14, 13, 19, 18]
r = reconstructBst(a)
printBTSinPreOrder(r)