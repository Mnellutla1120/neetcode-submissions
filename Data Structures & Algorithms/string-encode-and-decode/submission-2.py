class Solution:
    import re
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s) #add each word to array
        return "".join(res) #return da string



    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): #increment 
            j = i #second one
            while s[j] != '#':
                 j += 1
            length = int(s[i:j])
            i = j + 1 #keep going 
            j = i + length
            res.append(s[i:j])
            i = j
        return res





