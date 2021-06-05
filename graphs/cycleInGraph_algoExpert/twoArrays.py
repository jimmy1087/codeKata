def cycleInGrahp(edges):
    numNodes = len(edges)
    visited = [False for _ in range(numNodes)]  # Track nodes visited
    inStack = [False for _ in range(numNodes)]  # Track at each DFS level, which nodes are in stack (Nodes previously processed)

    for node in range(numNodes):
        if visited[node]:
            continue

        isCycle = isNodeInCycle(node, edges, visited, inStack)
        if isCycle:
            print('Cycle found traversing node:', node, 'Visited:', inStack)
            return True
        
    return False

def isNodeInCycle(node, edges, visited, inStack):
    print('Visiting Node:', node, 'Visited:', visited)
    visited[node] = True
    inStack[node] = True

    neighbors = edges[node]
    for neighbor in neighbors:

        if not visited[neighbor]:
            isCycle = isNodeInCycle(neighbor, edges, visited, inStack)
            if isCycle:
                return True
        elif inStack[neighbor]:
            return True

    inStack[node] = False
    return False


edges = [[8], [0, 2], [0, 3], [0, 4], [0, 5], [0], [7], [8], [6]]
cycleInGrahp(edges)

import pytest

def test_edges1():
    edges = [[8], [0, 2], [0, 3], [0, 4], [0, 5], [0], [7], [8], [6]]
    assert True == cycleInGrahp(edges)