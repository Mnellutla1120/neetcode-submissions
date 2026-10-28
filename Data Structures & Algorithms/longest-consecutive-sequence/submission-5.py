class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums) #no ugly repeats to deal w/
        res = 0
        l = 0 # our start idx and iterator
        longest_seq = 1
        n = -1
        if len(set_nums) == 1:
            return 1
        if len(set_nums) == 2 and abs(set_nums[i] - set_nums[0]) == 1:
             return 2

        while l < len(nums):
            if (nums[l] + n) in nums:
                 longest_seq += 1
                 n += 1
            l += 1
            res = max(longest_seq,res)
        return res

            
            


        



        