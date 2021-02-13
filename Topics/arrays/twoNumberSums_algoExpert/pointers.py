'''
https://www.algoexpert.io/questions/Two%20Number%20Sum
Given an array of numbers
If any two numbers in an array sum up to the target sum
Return them in any order

Input
a = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

Output
[11, -1]
'''

# Sort the array 
# Use a left pointer and a right pointer at both ends of the array
# Check on each loop if the sum of values at pointers == Target
# Else move either left or right pointer to check again

# Since the array is sorted asc, whenever we move a pointer, 
# all possible combinations far from the pointers have already been considered.

# o(nlogn) Time | o(1) Space
def twoNumbersSum(array, target):
    array.sort()  # quickSort time complexity in avg is     log(n)
    left = 0
    right = len(array)-1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == target:
            return [array[left], array[right]]
        elif currentSum > target:
            right -= 1
        else:
            left += 1
    return False

'''
Test
a = [3, 5, -4, 8, 11, 1, -1, 6]   target = 8
---
a.sort() = [-4, -1, 1, 3, 5, 6, 8, 11]  
             0   1  2  3  4  5  6   7

left = 0
right = 7

L1: -4 + 11 = 7  ... smaller ... Left  = 1
L2: -1 + 11 = 10 ... bigger  ... Right = 6
L3: -1 + 8  = 7  ... smaller ... Left  = 2
L4:  1 + 8  = 9  ... bigger  ... Right = 5
L5:  1 + 6  = 7  ... smaller ... Left  = 3 
L6:  3 + 6  = 9  ... bigger  ... Right = 4
L7:  3 + 5  = 8  ... Found

'''

import pytest

def test_1():
    a = [3, 5, -4, 8, 11, 1, -1, 6]
    assert [-1, 11] == twoNumbersSum(a, 10)

def test_2():
    a = [3, 5, -4, 8, 11, 1, -1, 6]
    assert [3, 5] == twoNumbersSum(a, 8)