class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_set = {")":"(","]":"[","}":"{"} #goes backward since its a stack
        #pop from the stack accordingly when detected
        for symbol in s:
            if symbol in bracket_set:
                if stack and stack[-1] == bracket_set[symbol]:
                     stack.pop()
                else:
                     return False
            else:
                stack.append(symbol) #add open parenthesis to stack
        return True if not stack else False #if stack is empty



