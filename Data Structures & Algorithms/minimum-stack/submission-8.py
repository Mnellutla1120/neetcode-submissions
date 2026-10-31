class MinStack:

    def __init__(self):
        stack = []
        self.stack = stack
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
        

    def pop(self) -> None:
        if not self.stack:
            return 
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        if not self.stack:
             return 
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minStack:
            return
        return self.minStack[-1]
        
        
