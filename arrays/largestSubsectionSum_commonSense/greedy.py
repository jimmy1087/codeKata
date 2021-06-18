def largestSubsectionSum(array):
    maxStartIdx = 0
    maxEndIdx = 0
    maxSumSoFar = 0
    curStartIdx = 0
    curEndIdx = 0
    curSum = 0
    for i, v in enumerate(array):
        newSum = curSum + v
        if newSum <= 0:
            curSum = 0
            if i + 1 < len(array):
                curStartIdx = i + 1
                curEndIdx = i + 1
        else:
            curSum = newSum
            curEndIdx = i
            if curSum > maxSumSoFar:
                maxSumSoFar = curSum
                maxStartIdx = curStartIdx
                maxEndIdx = curEndIdx
    total = 0
    result = []
    for i in range(maxStartIdx,maxEndIdx+1):
        result.append(array[i])
        total += array[i]
    print('Total:', total, 'Subsection:', result)

'''
Tests
'''   
a = [1,2,-3]
largestSubsectionSum(a)  # [1, 2] -> 3

a = [3, -4, 4, -3, 5, -9]
largestSubsectionSum(a)  # [4, -3, 5] -> 6

