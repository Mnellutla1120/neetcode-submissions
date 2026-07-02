class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_prof = 0

        while r <= len(prices)-1:
            if prices[l] < prices[r]: #future day is higher, so we want to sell prices[r] and buy prices[l]
                 profit = prices[r] - prices[l]
                 max_prof = max(max_prof, profit)
            else: #if prices[l] > prices[r], we keep looking until we can find a day where prices[r] is higher to max our profit
                 l = r
            r += 1
        return max_prof
