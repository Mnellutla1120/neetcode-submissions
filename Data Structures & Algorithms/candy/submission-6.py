class Solution:
    def candy(self, ratings: List[int]) -> int:

         candies = len(ratings)
         candy_arr = candies * [1]

         

         for i in range(1,candies):
             if ratings[i] - ratings[i - 1] > 0: #if i is greater than i - 1
                 candy_arr[i] = candy_arr[i-1] + 1
         for i in range(candies - 2, -1, -1):
                 if ratings [i] > ratings[i + 1]: #bigger elem has a bigger rating
                     candy_arr[i] = max(candy_arr[i], candy_arr[i + 1] + 1) #choose the bigger, distinguishing num
                

         return sum(candy_arr)