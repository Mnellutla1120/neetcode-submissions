class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_prof = 0


        while r <= len(prices)-1:
            if prices[l] < prices[r]:
                 prof = prices[r] - prices[l]
                 max_prof = max(max_prof,prof)
            elif prices[l] >= prices[r]:
                 l = r #l is our "lowest" day, we must find a higher day
            r += 1 #verify if we can find a day that theres a higher prof.
            
        return max_prof

                 

