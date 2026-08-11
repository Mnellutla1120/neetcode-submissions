class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #place two empty places next to flowerbed
        f = [0] + flowerbed + [0]
        for i in range(1, len(f)-1): #skip 1st and last (fake empties)
          if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
             f[i] = 1
             n -= 1
        return n == 0
           


    

    
        