class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        miss = 0 

        while l < r:
            if nums[l+1] - nums[l] > 1:
                miss = l + 1
            l += 1
        return miss
        


        


        