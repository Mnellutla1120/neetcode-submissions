class Solution:
    def missingNumber(self, nums: List[int]) -> int:
     n = len(nums)
     if nums[0] != 0:
        return 0
     if nums[n-1] != n:
        return n
     num_sum = sum(nums)
     z = len(nums)- 1

     while z > 0:
        num_sum -= nums[z]
        z -= 1
     
     return num_sum
  



    


    
        


        


        