class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         s_set = {}
         t_set = {}

         for i in range(len(s)):
             char = s[i]
             if char in s_set:
                 s_set[char] += 1
             else:
                 s_set[char] = 1

        # Count how many times each character appears in t
         for j in range(len(t)):
             char = t[j]
             if char in t_set:
                 t_set[char] += 1
             else:
                 t_set[char] = 1

        # Compare both dictionaries — if same, they're anagrams
         if s_set == t_set:
             return True
         else:
             return False