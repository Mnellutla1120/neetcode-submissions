class Solution:
       def canJump(self, nums: List[int]) -> bool:
        maxReach = 0  # repurposed init_ind to track farthest reachable
        for i in range(len(nums)):
            if i > maxReach:  # can't reach this index
                return False
            maxReach = max(maxReach, i + nums[i])  # expand reach
        return maxReach >= len(nums) - 1