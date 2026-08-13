class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_count = len(ratings) #everyone gets one candy
        #if rating of subsequent child is less than or equal to rating of prev child, they get less candy

        for i in range(1,len(ratings)):
            if abs(ratings[i - 1] - ratings[i]) > 0:
                 candy_count += 1

        
        return candy_count
        
        