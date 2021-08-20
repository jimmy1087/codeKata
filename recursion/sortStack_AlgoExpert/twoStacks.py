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
        return []
    
    top = stack.pop()      # At each level, remove an element and store it in level-memory
    
    sortStack(stack)       # Recursion to reach a level of 

    putElementInStack(stack, top)  # After having a sorted array in previos step, insert level-memory value

    return stack

def putElementInStack(stack, value):

    if len(stack) == 0 or value >= stack[-1]:  # If stack is empty insert 1st element OR insert value at correct position
        stack.append(value)
        return  # Once the item has been inserted return, no further search needed

    top = stack.pop()  # Empty stack again and store at each level-memory de current value in order
    
    putElementInStack(stack, value) # Recursion to keep searching the right place

    stack.append(top)  # After inserting element at correct place, restore elements in stack

############################

a = [-5, 2, -2, 4, 3, 1]
print(sortStack(a))

b = [-10,-11,0,-12,-13]
print(sortStack(b))

c = [4,3,91,32,-14,-30]
print(sortStack(c))
