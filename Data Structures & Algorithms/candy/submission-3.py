class Solution:
    def candy(self, ratings: List[int]) -> int:

         ratings.sort()

         candy_counter = len(ratings)
         

         for i in range(1,len(ratings)):
            if abs(ratings[i - 1] - ratings[i]) > 0:
                 candy_counter += 1
         return candy_counter