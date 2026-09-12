class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        rang = len(nums) + 1
        l = 0
        miss = 0

        while l < rang:
            if nums[l] != l:
                return l
            l += 1

        return 0
        
    
    
        


        


        