class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def rangeSumBST(node: Node, low: int, high: int) -> int:
    r = 0
    stack = [node]
    while stack:
        node = stack.pop(0)

        if node is None:
            continue

        if low <= node.val <= high:
            r += node.val

        if node.val > low:
            stack.append(node.left)
        if node.val < high:
            stack.append(node.right)

    return r
    
'---------------------------------------------------------'

n10, n5, n7, n3, n15, n18 = Node(10), Node(5), Node(7), Node(3), Node(15), Node(18)
n10.left, n10.right = n5, n15
n5.left, n5.right = n3, n7
n15.right = n18

print(rangeSumBST(n10, 7, 15))