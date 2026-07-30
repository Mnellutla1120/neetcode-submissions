class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        curr_streak = 1
        res = 0

        for n in new_nums:
             if n + 1 in new_nums:
                 curr_streak += 1
        

        return curr_streak
   






    

        