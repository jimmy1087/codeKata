def balanceBrackets(string):
    openBrackets  = '([{'
    closeBrackets = '}])'
    matchBrackets = {')':'(','}':'{',']':'['}
    stack = []
    for c in string:
        if c in openBrackets:
            stack.append(c)   #Appends item to the last position of the array LIFO   [1,2,3,....X]
        elif c in closeBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchBrackets[c]:
                stack.pop()   #By default pop() is -1:   last position appended LIFO [1,2,3,...._]  pop -> X
            else:
                return False
    return len(stack) == 0

s = '[()[]{}{[(())]}]'
print(s, balanceBrackets(s))

s = '[()'
print(s, balanceBrackets(s))

s = '[(]'
print(s, balanceBrackets(s))

s = '[((((('
print(s, balanceBrackets(s))