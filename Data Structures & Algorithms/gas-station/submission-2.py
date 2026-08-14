class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
             return -1 # no circ :(
        tot = 0
        res = 0 #track idx
        for i in range(len(gas)-1):
            tot += (gas[i] - cost[i])
            if tot < 0:
                 tot = 0 #go back to start
                 res = i + 1
        return res
       


        

            
        
        



        