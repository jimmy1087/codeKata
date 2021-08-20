# Given an array that acts as a Stack
# Sort the stack without using any other Data Structure
# Sort in place. Commands allow:  [-1] last element  /  append  /  pop
##########################
# O(n^2) T || O(n) S
# T: Empty the stack, insert element at correct position
# S: Due to recursion stack
##########################
def sortStack(stack):
    
    if len(stack) == 0:    # Base case: An empty stack is in order
        return stack
    
    top = stack.pop()      # At each level, remove an element and store it in level-memory
    
    sortedStack = sortStack(stack)       # Recursion to reach a level of 

    tmp = []
    while sortedStack and top < sortedStack[-1]:
        tmp.append(sortedStack.pop())

    sortedStack.append(top) 
    while tmp:
        sortedStack.append(tmp.pop())

    return sortedStack

############################

a = [-5, 2, -2, 4, 3, 1]
print(sortStack(a))

b = [-10,-11,0,-12,-13]
print(sortStack(b))

c = [4,3,91,32,-14,-30]
print(sortStack(c))
