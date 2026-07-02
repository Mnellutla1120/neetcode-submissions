class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)-1):
            if i > max_reach: #O(n) faster than jump
                 return False
            max_reach = max(max_reach,nums[i] + i)
        return max_reach >= len(nums) - 1