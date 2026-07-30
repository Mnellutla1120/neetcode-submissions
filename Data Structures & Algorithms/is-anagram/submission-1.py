class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p = set(s)
        q = set(t)
        if p == q:
             return True
        return False