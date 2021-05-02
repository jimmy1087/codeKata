class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def rangeSumBST(root: Node, low: int, high: int) -> int:
    r = []
    dfs(root, low, high, r)
    return sum(r)

def dfs(node: Node, low: int, high: int, r: []):
    if node is None:
        return
    
    if low <= node.val <= high:
        r.append(node.val)
    
    if node.val > low:
        dfs(node.left, low, high, r)
    if node.val < high:
        dfs(node.right, low, high, r)
    
'---------------------------------------------------------'

n10, n5, n7, n3, n15, n18 = Node(10), Node(5), Node(7), Node(3), Node(15), Node(18)
n10.left, n10.right = n5, n15
n5.left, n5.right = n3, n7
n15.right = n18

print(rangeSumBST(n10, 7, 15))