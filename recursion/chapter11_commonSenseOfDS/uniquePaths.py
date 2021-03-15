def uniquePaths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return uniquePaths(rows-1,cols) + uniquePaths(rows, cols-1)

print(uniquePaths(3,4))


def uniquePaths_dp(rows, cols, memo):
    if rows == 1 or cols == 1:
        return 1
    if memo.get((rows, cols)) is None:
        memo[(rows, cols)] = uniquePaths(rows-1, cols) + uniquePaths(rows, cols-1)
    return memo[(rows, cols)]

print(uniquePaths(3,4))