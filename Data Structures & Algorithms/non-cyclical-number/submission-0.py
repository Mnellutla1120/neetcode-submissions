class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            tot = 0
            for s in str(n):
                tot += int(s) ** 2
            n = tot
        return n == 1 



        