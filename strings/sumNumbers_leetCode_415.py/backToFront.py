
def addStrings(num1: str, num2: str) -> str:
    maxLength = max(len(num1), len(num2))
    result = []
    idx = 1
    remainder = 0
    while idx <= maxLength:
        s = int(remainder)
        if idx <= len(num1):
            s += ord(num1[idx*-1]) - ord('0')
        if idx <= len(num2):
            s += ord(num2[idx*-1]) - ord('0')
        if s > 9:
            remainder = s//10
        else:
            remainder = 0
        result.append(s%10)
        idx += 1
    if remainder > 0:
        result.append(remainder)
    return ''.join(reversed(list(map(str,result))))
        
'''
num1:  "456"    length: 3
num2:   "77"    length: 2

idx     r   num1[-idx]  num2[-idx]  s         result    r
1       0   6           7           0+6+7=13  [3]       1
2       1   5           7           1+5+7=13  [3,3]     1
3       1   4           -           1+4       [3,3,5]   0
4
'''

n1 = '456'
n2 = '77'

print(addStrings(n1, n2))