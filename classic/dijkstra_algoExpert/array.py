'''
Dijkstra
https://www.algoexpert.io/questions/Dijkstra's%20Algorithm
Return an array of shortest distance between a node and all possible nodes

  __________2________
 |                   |
(0) --2-- (2) --1-- (4)
 |      /  |      /  |
 3    2    4    1    |
 |  /      |  /      |
(1) --7-- (3)        |
 |_______________8___|

Input
    Node start: 4
    Edges:
            [
            [ [1,3],[2,2]        ],
            [ [3,7]              ],
            [ [1,2],[3,4],[4,1]  ],
            [ []                 ],
            [ [0,2][1,8],[3,1]   ]
            ]

Testing:
Node 4 Distance 0 Visited: {4}             [2, 8, inf, 1, 0]
Node 3 Distance 1 Visited: {3, 4}          [2, 8, inf, 1, 0]
Node 0 Distance 2 Visited: {0, 3, 4}       [2, 5,   4, 1, 0]
Node 2 Distance 4 Visited: {0, 2, 3, 4}    [2, 5,   4, 1, 0]
Node 1 Distance 5 Visited: {0, 1, 2, 3, 4} [2, 5,   4, 1, 0]
'''

def dijkstrasAlgorithm(start, edges):
    numOfNodes = len(edges)
    minDistances = [float('inf') for _ in range(numOfNodes)]
    minDistances[start] = 0   # At start position the min distance is always zero 
    visited = set()

    while len(visited) != numOfNodes:
        nodeIdx, currentNodeMinDistance = getUnvisitedNodeWithMinDistance(minDistances, visited)
        print('Node', nodeIdx, 'Distance', currentNodeMinDistance)
        if currentNodeMinDistance == float('inf'):
            break

        visited.add(nodeIdx)

        print('Visited:', visited)

        for edge in edges[nodeIdx]:
            edgeNode, edgeDistance = edge

            if edgeNode in visited:
                continue
            
            minDistances[edgeNode] = min(currentNodeMinDistance + edgeDistance, minDistances[edgeNode])

        print(minDistances)
            
    return list(map(lambda x: -1 if x == float('inf') else x, minDistances))

def getUnvisitedNodeWithMinDistance(minDistances, visited):
    currentMinDistance = float('inf')
    nodeIdx = -1
    
    for idx, distance in enumerate(minDistances):
        if idx in visited:
            continue
        if distance <= currentMinDistance:
            nodeIdx = idx
            currentMinDistance = distance
    
    return nodeIdx, currentMinDistance


start =  4
edges = [
    [[1, 3], [2, 2]],
    [[3, 7]],
    [[1, 2], [3, 4], [4, 1]],
    [],
    [[0, 2], [1, 8], [3, 1]]
  ]
print(dijkstrasAlgorithm(start, edges))