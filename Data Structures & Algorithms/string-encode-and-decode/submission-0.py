class Solution:

    def encode(self, strs: List[str]) -> str:
         res = ""
         for s in strs:
             res += str(len(s)) + "#" + s #"4#neet5#co#de"
         return res
  
    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #i is pointer, can declare two vars at same time :)
      
        while i < len(s):
             j = i
             while s[j] != "#":
                 j += 1
             length_of_string = int(s[i:j]) #how many following characters we have to read after j (the num) to get length of string
             res.append(s[j + 1 : j + 1 + length_of_string])
             i = j + 1 + length_of_string #start of next string
        return res
        


        





