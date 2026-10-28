class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums) #no ugly repeats to deal w/
        res = 0
        n_inc = 1 #incrementer
        if not nums:
             return 0
        longest_seq = 1
        for start in set_nums:
             if start - 1 not in set_nums:
                while start + n_inc in set_nums:
                     longest_seq += 1
                     n_inc += 1
                     if start + n_inc not in set_nums:
                         break
             res = max(res, longest_seq)
             n_inc = 1
             longest_seq = 1 #reset ts
        return res

           
        