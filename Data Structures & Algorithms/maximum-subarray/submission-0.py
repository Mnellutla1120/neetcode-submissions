class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
             return 0
        if len(nums) == 1:
             return nums[0]

        res = 0
        i = 0
        while i < len(nums):
            if nums[i] == max(nums): #find the max
                 res += nums[i] 
            i += 1
        
        return res




        