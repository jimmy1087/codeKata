def charsInArray(a):
    if len(a) == 0: return 0
    return len(a[0]) + charsInArray(a[1:])

a = ['abc','d','ef','ghij']

print(charsInArray(a))