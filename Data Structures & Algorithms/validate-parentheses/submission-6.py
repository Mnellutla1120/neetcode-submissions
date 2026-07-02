class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }  

       for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() #process this and eject both from stack, they should converge from out to in
                else:
                    return False
            else: 
                 stack.append(c)
       if not stack: #if stack is empty and everything processed correctly
             return True
       else:
             return False 