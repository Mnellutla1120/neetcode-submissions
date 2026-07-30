class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      i = 0
      for j in range(len(nums)):
         while i < len(nums):
             if nums[i] + nums[j] == target:
                 return [j,i]
             i+=1  
