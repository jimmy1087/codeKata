# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reconstructBst(preOrderTraversalValues):
	root = reconstructBstHelper(preOrderTraversalValues, 0, float('-inf'), float('inf'))
	
def reconstructBstHelper(a, i, minRef, maxRef):
    
    if len(a) == i+1:
        return BST(a[i+1])

    node = BST(a[i])
    nextNode = BST(a[i+1])
    
    print('i: ', i, ' node: ', node.value, ' nextN: ', nextNode.value, ' min', minRef, 'max', maxRef)

    if nextNode.value < node.value and a[i+1] > minRef:
        node.left = reconstructBstHelper(a, i+1, minRef, node.value)
    
    print('22222:  i: ', i, ' node: ', node.value, ' nextN: ', nextNode.value, ' min', minRef, 'max', maxRef)
    
    if nextNode.value > node.value and a[i+1] < maxRef:
        node.right = reconstructBstHelper(a, i+1, node.value, maxRef)

a = [10, 4, 2, 1, 5, 17, 19, 18]
reconstructBst(a)