'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
Runtime: 88 ms
Memory Usage: 15.6 MB
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)