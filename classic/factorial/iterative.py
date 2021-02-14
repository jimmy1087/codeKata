def getFactorial(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

print('Return:', getFactorial(5), 'Expected:', 120)
print('Return:', getFactorial(4), 'Expected:', 24)

            