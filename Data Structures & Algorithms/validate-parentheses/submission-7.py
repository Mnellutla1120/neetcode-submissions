class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }  

       for c in s:
        if c in closeToOpen:
             if stack[0] and stack[-1] == closeToOpen[c]:
                 stack.pop()
             else:
                return False #they arent in our defined order
        else:
            stack.append(c)
        
       if not stack:
             return True
       else:
             return False
            
        
        
