class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_set = {"]":"[","}":"{",")":"("}

        for char in s:
            if char in bracket_set:
                if stack and stack[-1] == bracket_set[char]:
                    stack.pop() #if unempty and both brackets exist
                else:
                    return False 
            else:
                stack.append(char)
        return True if not stack else False







        