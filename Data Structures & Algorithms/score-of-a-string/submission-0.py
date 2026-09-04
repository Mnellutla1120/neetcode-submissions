class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0

        for c in range(len(s)-1):
             total += abs(ord(s[c]) - ord(s[c+1]))
        
        return total


        