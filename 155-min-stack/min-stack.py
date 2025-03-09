class MinStack:

    def __init__(self):
        self.stack = [] #O(1)
  
        

    def push(self, val: int) -> None:
        if self.stack:
            minVal = min(val, self.stack[-1][1])
            self.stack.append((val,minVal))
        else:
            self.stack.append((val,val))
        

    def pop(self) -> None:
        self.stack.pop() #O(1)

    def top(self) -> int:
        return self.stack[-1][0] #O(1)
        

    def getMin(self) -> int:
        return self.stack[-1][1] #O(1)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()