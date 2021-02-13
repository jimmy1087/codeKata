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

# For each item in the array
#  calculate the corresponding pair (difference with target)
#  check if this difference is stored in the dictionary (Has already been visited before)
#    if found
#         return [difference, currentItem]
#    else 
#         store currentItem in dictionary // access in dictionary is consider to be o(1)

# o(n) Time | o(1) Space
def twoNumbersSum(array, target):
    m = {}
    for n in array:
        diff = target - n
        if diff in m:
            return [diff, n]
        else:
            m[n] = True
    return False

'''
Test
a = [3, 5, -4, 8, 11, 1, -1, 6], target = 10
---
m = {3:T, 5:T, -4:T, 8:T, 11:T, 1:T, -1:T}

diff = 10 - (-1) = 11
if 11 in m:
    return [11, -1]
'''

import pytest

def test_1():
    a = [3, 5, -4, 8, 11, 1, -1, 6]
    assert [11, -1] == twoNumbersSum(a, 10)