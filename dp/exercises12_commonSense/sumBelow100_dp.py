def sumBelow100(a):
    print('Recursion')
    if len(a) == 0:
        return 0
    s = sumBelow100(a[1:])    # Recursion call only once!
    if a[0] + s > 100:
        return s
    else:
        return a[0] + s

a = [10,30,80]        # Since Recursion works backward, picking up numbers and evaluation will go in reverse order
print(sumBelow100(a))