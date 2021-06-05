'''
Given a sequence of integers and an integer total target, 
return whether a contiguous sequence of integers sums up to target.

[1, 3, 1, 4, 23], 8 : True (because 3 + 1 + 4 = 8)    (2prevSum + me, prevSum + me)
    ^     ^
sum: 1+3+1+1 = 9 - 1 

[1, 1, 1, 3, 1],  4: True (because 1, 3)
       ^  ^
sum: 1 + 1 = 2 + 1 = 3 + 3 = 6 - 1 = 5 - 4 : True

[1, -3, 1, 4, 23], 8 : False
^^

[3,1,4]: 7: False
(3) .. (4,1) .. (8, 5): False

[-1, -2, -3 ] -6
(-1), (-3, -2) (-6, -5)

'''

def sumUpToTarget(array, target):
    start = 0
    curSum = 0
    negPos = 0
    for k, v in enumerate(array):
        while curSum + v > target:
            curSum -= array[start]
            start += 1
        if curSum + v == target:
            return True
        curSum += v
        print(curSum)
    return False
        
#a = [1, 3, 1, 4, 23]
#print(sumUpToTarget(a, 8))

a = [1, -3, 1, 4, 23]
print(sumUpToTarget(a, 5))
