class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}


        for i,n in enumerate(nums): #idx, val
            diff = target - n
            if diff in h_map:
                 return [h_map[diff],i]
            else:
                h_map[n] = i
         

        