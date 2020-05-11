'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

Runtime: 68 ms  
Memory: 15.4 MB
Time Complexity:  O(n)   
Space complexity: O(n)

Given an array, rotate the array to the right by k steps, where k is non-negative.
a[1,2,3,4,5,6]

a[(i+k)%n] 
will traverse the array starting from a given K and
restart index to zero when len of array is reached (MOD %)

Solution taken from suggestion in problem.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0] * n
        
        for i in range(n):
            a[(i+k)%n] = nums[i]
            
        nums[:] = a