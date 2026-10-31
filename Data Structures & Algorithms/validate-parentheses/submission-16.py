class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in closeToOpen:
                stack.append(c)
                if not stack:
                    return False
                if closeToOpen[c] != stack.pop():
                    return False
            
            return (len(stack) == 0)

