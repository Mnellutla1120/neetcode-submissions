class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # A LOT like coin problem, so greedy may not work
         #top floor = len(cost)

         for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

         return min(cost[0], cost[1])



        
