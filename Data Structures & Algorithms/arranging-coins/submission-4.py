class Solution:
    def arrangeCoins(self, n: int) -> int:
      #overall trend of # of rows is the (coins / 2).floor
      l = 1
      r = n
      res = 0
      while l <= r:
         mid = (l + r) // 2
         coins = ((mid)*(mid + 1)) // 2 # num of coins starting from midpoint (hypothesize comp rows)
         if coins > n: #more coins from the 'perfect' midpoint
            r = mid - 1
         else:
            l = mid + 1
            res = max(res,mid)
      return res






        


