class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i # first subtract by 1
            i += 2
        return num == 0 #keep going until we get here 

        