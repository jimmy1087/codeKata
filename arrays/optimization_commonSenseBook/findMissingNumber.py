# Write a function that accepts an array of distinct integers from 0, 1, 2, 3…up to N. 
# However, the array will be missing one integer, and your function is to return the missing one
# ie:
# [2,3,0,6,1,5]  -> Missing 4
# [0, 1, 2, 4, 5, 6] : missing 3: sum = 18

def findMissingNumberOptA(array):

    nums = {}
    for n in array:
        nums[n] = True

    for i in range(len(array)):
        if i not in nums:
            return i
    return -1

a = [2,3,0,6,1,5]
print(findMissingNumberOptA(a))

b = [0, 1, 2, 4, 5, 6]
print(findMissingNumberOptA(b))

def findMissingNumberOptB(array):
    total_sum = 0
    for i in range(1, len(array)+1):
        total_sum += i

    current_sum = 0
    for n in array:
        current_sum += n
    
    return total_sum - current_sum

a = [2,3,0,6,1,5]
print(findMissingNumberOptB(a))

b = [0, 1, 2, 4, 5, 6]
print(findMissingNumberOptB(b))