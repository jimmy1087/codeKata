class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

def balanceBrackets(string):
    stack = Stack()
    openBrackets  = '([{'
    closeBrackets = '}])'
    matchBrackets = {')':'(','}':'{',']':'['}
    for c in string:
        if c in openBrackets:
            stack.push(c)
        elif c in closeBrackets:
            if stack.isEmpty():
                return False
            if stack.top() == matchBrackets[c]:
                stack.pop()
            else:
                return False
    return stack.isEmpty()

s = '[()[]{}{[(())]}]'
print(s, balanceBrackets(s))

s = '[()'
print(s, balanceBrackets(s))

s = '[(]'
print(s, balanceBrackets(s))

s = '[((((('
print(s, balanceBrackets(s))