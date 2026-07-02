class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy algorithm, go backwards

        end_ind = len(nums) - 1 #where we want to be
        for i in range(len(nums)-1,-1,-1): #go backwards through our loop
              if i + nums[i] >= end_ind:
                 end_ind = i
        return end_ind == 0 #we reached our goal!


            
