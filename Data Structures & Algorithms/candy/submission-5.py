class Solution:
    def candy(self, ratings: List[int]) -> int:

         candy_counter = len(ratings)
         

         for i in range(len(ratings)-1):
            if abs(ratings[i] - ratings[i + 1]) > 0:
                 candy_counter += 1
         return candy_counter