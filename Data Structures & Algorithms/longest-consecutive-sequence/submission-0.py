class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        max_streak = 0
        curr_streak = 0
        for num in new_nums:
             if num-1 not in new_nums:
                 curr_streak = 1
                 curr_num = num
                 while curr_num+1 in new_nums:
                     curr_streak += 1
                     curr_num += 1
                 if curr_streak > max_streak:
                     max_streak = curr_streak
        return max_streak

            

            
        