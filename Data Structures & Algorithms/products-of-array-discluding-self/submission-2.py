import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #iterate through array and multiple everything, divide by wtv is in the index pos

        res = nums.copy()
        prod = math.prod(nums)
        for i in range(len(res)):
            res[i] = prod
        
        for j in range(len(nums)):

            res[j] //=  nums[j]
        

        
        return res