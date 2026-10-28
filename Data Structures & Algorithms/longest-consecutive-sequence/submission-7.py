class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums) #no ugly repeats to deal w/
        res = 0
        l = 0 # our start idx and iterator
        longest_seq = 1
        n = -1

        while l < len(nums):
            if (nums[l] + n) in set_nums:
                 longest_seq += 1
                 n += 1
            l += 1
        res = max(longest_seq,res)
        return res

            
            


        



        