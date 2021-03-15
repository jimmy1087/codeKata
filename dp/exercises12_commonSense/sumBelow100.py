def sumBelow100(a):
    print('Recursion')
    if len(a) == 0:
        return 0
    if a[0] + sumBelow100(a[1:]) > 100:     # Recursion call 1
        return sumBelow100(a[1:])           # Recursion call 2
    else:
        return a[0] + sumBelow100(a[1:])    # Recursion call 3

a = [10,30,80]        # Since Recursion works backward, picking up numbers and evaluation will go in reverse order
print(sumBelow100(a))