class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
             if t  == "+" or t == "-" or t == "/" or t=="*":
                 a = stack.pop()
                 b = stack.pop()
             if t == "+":
                 stack.append(a + b)
             elif t == "-":
                 stack.append(a-b)
             elif t == "*":
                 stack.append(a*b)
             elif t== "/":
                 stack.append(int(a/b))
             else:
                 stack.append(int(t))
        return stack[-1]
        