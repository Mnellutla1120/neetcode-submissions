class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        if not nums: #base case
             return 0
        new_nums = set(nums)
        curr_streak = 0

        for n in new_nums:
             if n-1 not in new_nums: #we are at start
                 curr_streak = 1
                 longest_streak = max(curr_streak, longest_streak)
                 while n + curr_streak in new_nums:
                     curr_streak += 1
                     longest_streak = max(curr_streak, longest_streak)
        
        
        return longest_streak
   






    

        