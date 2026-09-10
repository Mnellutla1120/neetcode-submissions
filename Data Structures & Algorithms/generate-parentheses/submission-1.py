class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open < n
        #only add a closing parenthesis if closed < open
        #valid if open == closed == n

        stack = []
        res = []

        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack)) #form complete. string
            
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                dfs(openN, closedN+1)
                stack.pop()
        dfs(0,0)
        return res
            


