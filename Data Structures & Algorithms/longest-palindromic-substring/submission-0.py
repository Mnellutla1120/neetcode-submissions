class Solution:
    def longestPalindrome(self, s: str) -> str:
         longest = ""
         for i in range(len(s)):
            #odd
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                 curr_len = r - l + 1
                 if curr_len > len(longest):
                     longest = s[l : r + 1] #from start to end
                 l -= 1
                 r += 1
            #even
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                 curr_len = r - l + 1
                 if curr_len > len(longest):
                     longest = s[l : r + 1] #from start to end
                 l -= 1
                 r += 1
         return longest
                
         
    