class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof = 0
        l = 0
        r = 1
        while r < len(prices):
             profit = prices[r] - prices[l]
             if prices[l] > prices[r]:
                 l = r #find the max smolest #
             r += 1 #keep finding the best time to sell
             max_prof = max(max_prof,profit)
        return max_prof


        







        
        
        


    