'''
https://www.algoexpert.io/questions/Kadane's%20Algorithm
Write a function that return the max sum that can be obtained by summing all int
in a sub-array of the input array. The subarray must contain only adjacent numbers

array: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
output: 18

Steps:
 
array:           [3,  5,  -9,  1,  3, -2,  3,  4,   7,  2,  -9,   6,   3,   1, -5, 4]
curSum option A  *3, *8, *-1,  0, *4, *2, *5, *9, *16, *18, *9, *15, *18, *19, 14, 18
curSum option B   3,  5,  -9, *1,  3, -2,  3,  4,   7,  2,  -9,   6,   3,   1, -5, 4
maxSum            3,  8,   8,  8,  8,  8,  8,  9,  16,  18, 18,  18,  18,  19, 19, 19

Return maxSum 19

'''

def kadanesAlgorithm(array):
    curSum = array[0]
    maxSum = array[0]
    for idx in range(1, len(array)):
        curSum = max(curSum + array[idx], array[idx])
        maxSum = max(maxSum, curSum)
    return maxSum

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(array))