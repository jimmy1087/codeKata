/*
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Complexity: O(n)
Runtime: 0 ms
Memory Usage: 41.4 MB

*/
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length < 1) return 0;
        int u = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[u] != nums[i]) {
                u += 1;
                nums[u] = nums[i];
            }
        }
        return u+1;
    }
}