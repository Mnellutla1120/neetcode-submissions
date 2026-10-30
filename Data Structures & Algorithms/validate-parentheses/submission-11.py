class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {')':'(', '}':'{' , ']':'['}
        stack = []
        for c in s: #iterate through string
            if c in s_dict:
                 stack.append(c)
        for brac in range(len(stack)):
            if stack[brac] not in stack:
                stack.pop()
                return False
        return True
    
        


