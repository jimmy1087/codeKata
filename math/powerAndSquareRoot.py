'''
Determine if the given number is a power of some non-negative integer.

125 = 5**3
64  = 2*2*2*2*2*2 = 2**6 = 4*4*4 = 4**3

cubic roots = # ^ (1/3)
4th roots = # ^ (1/4)
5th roots = # ^ (1/5)

'''

def isPower(n):
    root = 2
    while root < n:
        result = round( n ** (1.0/root) ) # 1.0 force result to be float, otherwise int will floor the result
        print('Result', result, 'Root', root)
        if n == result ** root:
            return True
        root += 1
    return False

print('In', 125, 'Out', isPower(125))

print('In', 64, 'Out', isPower(64))

print('In', 27, 'Out', isPower(27))
