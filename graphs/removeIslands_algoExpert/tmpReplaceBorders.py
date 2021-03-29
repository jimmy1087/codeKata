def removeIslands(matrix):

    visited = [[False for col in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            if visited[row][col]:
                continue
            if matrix[row][col] != 1:
                continue

            if isBorder(row, col, matrix):
                traverseNodes(row, col, matrix, visited)
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
            if matrix[row][col] == 2:
                matrix[row][col] = 1

    for row in range(len(matrix)):
        r = []
        for col in range(len(matrix[row])):
            r += [matrix[row][col]]
        print(r)
            
def isBorder(row, col, matrix):
    numRows = len(matrix)-1
    numCols = len(matrix[0])-1
    return row == 0 or row == numRows or col == 0 or col == numCols

def traverseNodes(startRow, startCol, matrix, visited):
    
    queue = [(startRow, startCol)]
    while queue:
        
        row, col = queue.pop(0)
        if visited[row][col]:
            continue
        if matrix[row][col] != 1:
            continue

        visited[row][col] = True
        matrix[row][col] = 2

        neighbors = getNeighbors(row, col, matrix)
        for neighbor in neighbors:
            row, col = neighbor
            if visited[row][col]:
                continue
            queue.append((row, col))

def getNeighbors(row, col, matrix):
    neighbors = []
    numRows = len(matrix)-1
    numCols = len(matrix[0])-1

    if row - 1 >= 0: #TOP
        neighbors += [(row - 1, col)]
    if row + 1 < numRows: #DOWN
        neighbors += [(row + 1, col)]
    if col - 1 >= 0: #LEFT
        neighbors += [(row, col - 1)]
    if col + 1 < numCols: #RIGHT
        neighbors += [(row, col + 1)]
    
    return neighbors


m = [
    [0,1,1,0,0],
    [0,0,0,0,0],
    [1,0,1,1,0],
    [1,1,0,0,0]
    ]

removeIslands(m)