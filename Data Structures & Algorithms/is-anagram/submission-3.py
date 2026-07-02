class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_set = {}
        t_set = {}
        for char in s:
            s_set[char] = s_set.get(char,0) + 1
        for char in t:
            t_set[char] = t_set.get(char,0) + 1
        return s_set == t_set 
    