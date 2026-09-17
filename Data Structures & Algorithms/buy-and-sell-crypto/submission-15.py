class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        l = 0
        r = 1

        while r < len(prices):
            profit = prices[r] - prices[l]

            if prices[l] > prices[r]: #prices[r] is NOT a good selling day, but can be a buying day
               l = r
            r += 1 #we want to iterate this to find the best selling day
        
            max_prof = max(max_prof, profit)
        
        return max_prof





        
        
        


    