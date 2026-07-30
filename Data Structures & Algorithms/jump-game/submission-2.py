class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy algorithm, go backwards

        init_ind = 0 #our start
        for i in range(len(nums)-1): #go backwards through our loop
              if i + nums[i] > init_ind:
                 init_ind = i + nums[i]
        return init_ind == len(nums)-1 #we reached our goal!


            
