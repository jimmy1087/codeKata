def str2int(string):
    d = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
    n = 0
    for s in string:
        n = n * 10 + d[s]
    return n

def str2intOption2(string):
    n = 0
    for s in string:
        n = n * 10 + ord(s) - ord('0')
    return n

'''
num1: 456
0*10 + 4 = 4
4*10 + 5 = 45
45*10 + 6 = 456

num2: 77
0*10 + 7 = 7
7*10 + 7 = 77
'''

def sumArrays(num1, num2):
    return str(str2intOption2(num1) + str2intOption2(num2))

n1='456'
n2='77'

print(sumArrays(n1,n2))