class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        
        l = 0
        r = len(nums) - 1
        
        while l < r:
             m =  (l + r) // 2
             count = 0
             for num in nums:
                  if num <= m:
                      count += 1
             if count <= m:
                 l = m + 1
                
             else:
                 r = m
        return l

       


  
        