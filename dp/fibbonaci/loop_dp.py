def fib(n):
    a = 1
    b = 1
    for i in range(2, n+1):
        tmp = a
        a = b
        b = a + tmp
    return b

print(fib(8))