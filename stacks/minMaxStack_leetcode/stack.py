class Stack:
    def __init__(self):
        self.data = []
        self.minMax = []

    def peek(self):
        return self.data[-1]

    def pop(self):
        self.minMax.pop()
        return self.data.pop()

    def push(self, number):
        newMinMax = (number, number)
        if self.minMax:
            lastMinMax = self.minMax[-1]
            newMinMax = ( min(number, lastMinMax[0]), max(number, lastMinMax[1]) )
        self.minMax.append(newMinMax)
        self.data.append(number)
    
    def getMin(self):
        if self.minMax:
            return self.minMax[-1][0]
        else:
            return None
    
    def getMax(self):
        if self.minMax:
            return self.minMax[-1][1]
        else:
            return None

stack = Stack()                     # []
stack.push(2)                       # [2]
print('min', stack.getMin(), 2)     
stack.push(7)                       # [2,7]
print('max', stack.getMax(), 7)     
stack.push(1)                       # [2,7,1]
print('min', stack.getMin(), 1)
print('max', stack.getMax(), 7)     
stack.push(8)                       # [2,7,1,8]
print('min', stack.getMin(), 1)
print('max', stack.getMax(), 8)     
stack.push(3)                       # [2,7,1,8,3]
print('min', stack.getMin(), 1)
print('max', stack.getMax(), 8)
stack.pop()                         # [2,7,1,8]
print('min', stack.getMin(), 1)
print('max', stack.getMax(), 8)
stack.pop()                         # [2,7,1]
print('min', stack.getMin(), 1)
print('max', stack.getMax(), 7)
stack.pop()                         # [2,7]
print('min', stack.getMin(), 2)
print('max', stack.getMax(), 7)
stack.pop()                         # [2]
print('min', stack.getMin(), 2)
print('max', stack.getMax(), 2)
stack.pop()                         # []
