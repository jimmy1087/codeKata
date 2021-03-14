'''
Use recursion to write a function that accepts an array of numbers 
and returns a new array containing just the even numbers.
'''

def evenNumbers(a, ev = []):
    if len(a) == 0:
        return ev
    if a[0] % 2 == 0:
        ev.append(a[0])
    return evenNumbers(a[1:], ev)

a = [2,3,4,5,6,7,8,9,10]
print(evenNumbers(a))


def selectEvens(b):
    if len(b) == 0:
        return []
    if b[0] % 2 == 0:
        return [b[0]] + selectEvens(b[1:])
    else:
        return selectEvens(b[1:])

b = [2,3,4,5,6,7,8,9,10]
print(selectEvens(b))