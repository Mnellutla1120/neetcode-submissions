class Solution:
       def canJump(self, nums: List[int]) -> bool:
         max_reach = 0
         for i in range(len(nums)-1):
             if i > max_reach:
                 return False #O(n) is faster than jump
             else:
                 max_reach = max(max_reach,nums[i] + i)
         return max_reach >= len(nums)-1

