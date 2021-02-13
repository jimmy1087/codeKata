def getRiverSizes(matrix):

    sizes = []
    riversVisited = [[False for value in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            if riversVisited[row][col]:
                continue
            if matrix[row][col] != 1:
                continue

            traverseRiver(row, col, matrix, riversVisited, sizes)

    return sizes

def traverseRiver(startRow, startCol, matrix, riversVisited, sizes):
    riverSize = 0
    queue = [(startRow, startCol)]

    while queue:
        row, col = queue.pop(0)

        if riversVisited[row][col]:
            continue
        
        riversVisited[row][col] = True
        riverSize += 1

        neighbors = getNeighbors(row, col, matrix)
        for neighbor in neighbors:
            row, col = neighbor
            if matrix[row][col] != 1:
                continue
            queue.append((row, col))
    
    if riverSize > 0:
        sizes.append(riverSize)

def getNeighbors(row, col, matrix):
    neighbors = []
    numRows = len(matrix)
    numCols = len(matrix[0])

    if row - 1 >= 0: #TOP
        neighbors.append((row - 1, col))
    if row + 1 < numRows: #DOWN
        neighbors.append((row + 1, col))
    if col - 1 >= 0: #LEFT
        neighbors.append((row, col - 1))
    if col + 1 < numCols: #RIGHT
        neighbors.append((row, col + 1))
    
    return neighbors

import pytest

def test_matrix_1():

    m = [[0,0,1,0,0],
         [0,0,1,0,1],
         [0,0,1,0,0]]
         
    assert [3, 1] == getRiverSizes(m)

def test_matrix_2():

    m = [[1,1,1,0,1],
         [0,1,1,0,1],
         [1,0,1,0,1]]
         
    assert [6, 3, 1] == getRiverSizes(m)