def getFactorial(n):
    if n == 1:
        return 1
    return getFactorial(n-1) * n

'''
getFactorial(5):

            5
           / 
         (4) * 5    R: 24 * 5 =    120
         /
       (3) * 4      R: 6 * 4 = 24
       /
     (2) * 3        R: 2 * 3 = 6
    /
  (1) * 2           R: 1 * 2 = 2
  /
Base case return -> R: 1

'''

print('Return:', getFactorial(5), 'Expected:', 120)
print('Return:', getFactorial(4), 'Expected:', 24)
