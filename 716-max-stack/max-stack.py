# from sortedcontainers import SortedList
import heapq

class MaxStack:

    def __init__(self):
        # self.stack = SortedList()
        # self.max_values = SortedList()
        self.stack = []
        self.heap = []
        self.deleted_ids = set()
        self.id = 0
        

    def push(self, x: int) -> None:
        self.stack.append(( x, self.id))
        heapq.heappush(self.heap, (-x, -self.id))
        # self.max_values.add((x, self.id))
        self.id+=1

    def pop(self) -> int:

        while self.stack and self.stack[-1][1] in self.deleted_ids:
            self.stack.pop()

        val, idx = self.stack.pop()
        self.deleted_ids.add(idx)
        return val
        

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.deleted_ids:
            self.stack.pop()
        return self.stack[-1][0] 

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.deleted_ids:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.deleted_ids:
            heapq.heappop(self.heap)

        val, idx = heapq.heappop(self.heap)
        self.deleted_ids.add(-idx)
        return -val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()