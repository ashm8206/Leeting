class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            minElement = min(val, 2**31)
        else:
            minElement = min(val, self.stack[-1][1])
        self.stack.append((val,minElement))
        

    def pop(self) -> None:
        
        self.stack.pop()

    def top(self) -> int:
      
        topElement, _ = self.stack[-1]
        return topElement
        

    def getMin(self) -> int:
 
        _, minElement = self.stack[-1]
        return minElement


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()