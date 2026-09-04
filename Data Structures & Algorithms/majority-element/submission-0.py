class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums) // 2
        res = 0
        i = 0
        counter = 0

        for j in range(len(nums)):
             if nums[j] == nums[i]:
                 counter += 1
                 if counter > size:
                     res = nums[j]
        i += 1

        return res

        
        