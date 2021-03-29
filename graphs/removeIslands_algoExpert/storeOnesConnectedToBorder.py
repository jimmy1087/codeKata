def removeIslands(matrix):

    for row in range(len(matrix)):
        r = []
        for col in range(len(matrix[row])):
            r += [matrix[row][col]]
        print(r)

    onesConnectedToBorder = [[False for col in row]for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            isRowBorder = row == 0 or row == len(matrix) - 1
            isColBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = isRowBorder or isColBorder
            
            if not isBorder:
                continue
            if onesConnectedToBorder[row][col]:
                continue
            if matrix[row][col] != 1:
                continue

            traverseNodes(row, col, matrix, onesConnectedToBorder)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if onesConnectedToBorder[row][col]:
                continue
            matrix[row][col] = 0
    
    for row in range(len(matrix)):
        r = []
        for col in range(len(matrix[row])):
            r += [matrix[row][col]]
        print(r)

def traverseNodes(row, col, matrix, onesConnectedToBorder):
    queue = [(row, col)]
    while queue:
        row, col = queue.pop(0)
        if onesConnectedToBorder[row][col]:
            continue
        onesConnectedToBorder[row][col] = True
        neighbors = getNeighbors(row, col, matrix)
        for neighbor in neighbors:
            if onesConnectedToBorder[row][col]:
                continue
            queue += [(row,col)]

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