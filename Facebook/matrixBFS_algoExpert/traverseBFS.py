def traverseBFS(matrix):
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited)
    #print('Visited: ', visited)    
    
def traverseNode(i, j, matrix, visited):
    counter = 1
    nodesToExplore = [[0,0]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i, j = currentNode[0], currentNode[1]
        if visited[i][j]:
            continue
        print("VisitingNode: " + str(counter), currentNode)
        counter += 1
        visited[i][j] = True
        unvisitedNodes = getUnvisitedNodes(i, j, matrix, visited)
        for neighbor in unvisitedNodes:
            nodesToExplore.append(neighbor)
        #print("Queue", nodesToExplore)
        
def getUnvisitedNodes(i, j, matrix, visited):
    unvisited = []
    # Top
    if i > 0 and not visited[i-1][j]:
        unvisited.append([i-1,j])
    # Down
    if i < len(matrix)-1 and not visited[i+1][j]:
        unvisited.append([i+1,j])
    # Left
    if j > 0 and not visited[i][j-1]: 
        unvisited.append([i,j-1])
    # Right
    if j < len(matrix[0])-1 and not visited[i][j+1]:
        unvisited.append([i,j+1])

    return unvisited

a = [
    [1,1,0],
    [1,0,0],
    [1,0,0]
]
traverseBFS(a)

