class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minHeightBST(a):
    return minHeightBSTHelper(a, None, 0, len(a)-1)

def minHeightBSTHelper(a, bst, left, right):
    if right < left:
        return
    mid = (left + right) // 2
    newNode = BST(a[mid])
    if bst is None:
        bst = newNode
    else:
        if newNode.value < bst.value:
            bst.left = newNode
            bst = bst.left
        else:
            bst.right = newNode
            bst = bst.right
    minHeightBSTHelper(a, bst, left, mid - 1)
    minHeightBSTHelper(a, bst, mid + 1, right)
    return bst


def printInOrder(node):
    if node is None:
        return 
    printInOrder(node.left)
    print(' ' + str(node.value))
    printInOrder(node.right)

a = [1,2,5,7,10,13,14,15,22]

n = minHeightBST(a)
printInOrder(n)


