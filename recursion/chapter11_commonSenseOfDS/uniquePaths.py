def uniquePaths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return uniquePaths(rows-1,cols) + uniquePaths(rows, cols-1)

print(uniquePaths(3,4))