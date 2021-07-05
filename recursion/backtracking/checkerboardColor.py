COLORS = ['RED','BLUE']
matrix = [
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]
         ]
NUM_ROWS = len(matrix)
NUM_COLS = len(matrix[0])


def nextRowAndColumn(row, col):
    if col + 1 < NUM_COLS:
        return (row, col + 1)
    if row + 1 < NUM_ROWS:
        return (row + 1, 0)
    return (3, 0)

def okToColor(row, col, color):
    if row - 1 >= 0 and color == matrix[row - 1][col]:
        return False
    if row + 1 < NUM_ROWS and color == matrix[row + 1][col]:
        return False
    if col - 1 >= 0 and color == matrix[row][col - 1]:
        return False
    if col + 1 < NUM_COLS and color == matrix[row][col + 1]:
        return False
    return True

def explore2(row, col, color):
    if row >= NUM_ROWS:
        return True
    if okToColor(row, col, color):
        matrix[row][col] = color
        for nextColor in COLORS:
            nextRow, nextCol = nextRowAndColumn(row, col)
            if explore2(nextRow, nextCol, nextColor):
                return True
    return False

def colorMap():

    explore2(0,0,'RED')
    print(matrix)

colorMap()





# def explore1(row, col, color):
    
#     if row >= NUM_ROWS:
#         return mapIsOK();

#     map[row][column] = color

#     for nextColor in COLORS:
#         nextRow, nextCol = nextRowAndColumn(row, col);
#         if explore1(nextRow, nextCol, nextColor):
#             return True

#     return False

# def mapIsOK():
#     pass