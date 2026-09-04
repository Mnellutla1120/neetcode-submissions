class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        c = 0
        while c < len(s) - 1:
             total += abs(ord(s[c]) - ord(s[c+1]))
             c += 1
        return total


        