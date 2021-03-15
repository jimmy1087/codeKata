val = 14

#Option 1
def sumsUpToN(n, i=1):
    if i == n:
        return i
    return i + sumsUpToN(n, i+1)

print(sumsUpToN(val))

'''
        (6)  = 6    --> Base case returns when i == n
    5 + (6)  = 6
    4 + (11) = 15
    3 + (15) = 18
    2 + (18) = 20
    1 + (20) = 21

'''
#Option 2
def sumsUpToNWithFormula(n):
    return n * (n + 1) // 2

print(sumsUpToNWithFormula(val))

#Option 3
def sumsUpToNOption3(n):
    if n == 0:
        return 0
    return n + sumsUpToNOption3(n-1)

print(sumsUpToNOption3(val))