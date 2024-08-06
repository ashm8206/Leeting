from sortedcontainers import SortedList
class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.max_values = SortedList()
        self.id = 0
        

    def push(self, x: int) -> None:
        self.stack.add((self.id, x))
        self.max_values.add((x, self.id))
        self.id+=1

    def pop(self) -> int:
        idx, val = self.stack.pop()
        self.max_values.remove((val, idx))
        return val
        

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.max_values[-1][0]

    def popMax(self) -> int:
        val, idx = self.max_values.pop()
        self.stack.remove((idx, val))
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()