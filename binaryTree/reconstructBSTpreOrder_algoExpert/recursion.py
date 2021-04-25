# O(n) time || O(n) space
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx

def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstHelper(preOrderTraversalValues, treeInfo, float('-inf'), float('inf'))

def reconstructBstHelper(a, treeInfo, lowerBoundary, upperBoundary):
    
    if treeInfo.rootIdx == len(a):
        return None
    
    currentValue = a[treeInfo.rootIdx]
    if currentValue < lowerBoundary or currentValue >= upperBoundary:
        return None
    
    treeInfo.rootIdx += 1
    leftSubTree = reconstructBstHelper(a, treeInfo, lowerBoundary, currentValue)
    rightSubTree = reconstructBstHelper(a, treeInfo, currentValue, upperBoundary)

    return BST(currentValue, leftSubTree, rightSubTree)

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