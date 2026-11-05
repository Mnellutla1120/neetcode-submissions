class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c not in closeToOpen: #opening bracket
                 stack.append(c)
            else: 
                 if not stack: 
                     return False
                 if closeToOpen[c] != stack.pop():
                     return False
            
        
        return (len(stack) == 0)

