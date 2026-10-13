class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or len(s)==1:
            return True
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        