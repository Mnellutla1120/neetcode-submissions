class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
             return False #can't check for permutation

        s1_ct, s2_ct = [0]*26,[0]*26
        for i in range(len(s1)):
             s1_ct[ord(s1[i]) - ord('a')] += 1
             s2_ct[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            #we only want to add one to it if the alphabet letters in strings are same
            matches += (1 if s1_ct[i] == s2_ct[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
             if matches == 26: return True

             index = ord(s2[r]) - ord('a')
             s2_ct[index] += 1
             if s1_ct[index] == s2_ct[index]:
                 matches += 1
             elif s1_ct[index] + 1 == s2_ct[index]:
                 matches -= 1
                
             index = ord(s2[l]) - ord('a')
             s2_ct[index] -= 1
             if s1_ct[index] == s2_ct[index]:
                 matches += 1
             elif s1_ct[index] - 1 == s2_ct[index]:
                 matches -= 1
             l +=1
        return matches == 26





