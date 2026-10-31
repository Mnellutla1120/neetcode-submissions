class MinStack:

    def __init__(self):
        stack = []
        self.stack = stack
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if not self.stack:
            return 
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return 0
        return self.stack.pop()
        

    def getMin(self) -> int:
        if not self.stack:
             return 0
        min_s = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < min_s:
                min_s = self.stack[i]
        return min_s
        
