
class Solution:
    def mySqrt(self, x: int) -> int:
      sub_counter = 0
      i = 1
      num = x
      while num > 0:
         num -= i
         i += 2
         if num >= 0: 
             sub_counter += 1
         
      return sub_counter

            



   

        