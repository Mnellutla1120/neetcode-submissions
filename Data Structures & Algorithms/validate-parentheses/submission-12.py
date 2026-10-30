class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {')':'(', '}':'{' , ']':'['}
        stack = []
        for c in s: #iterate through string
            if c in s_dict:
                 if stack.pop() != s_dict[c]:
                    #no complement
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        


