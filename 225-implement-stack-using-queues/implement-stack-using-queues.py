from collections import deque
class MyStack:
    # Neetcode with Top enhacement
    # https://www.youtube.com/watch?v=rW4vm0-DLYc
    def __init__(self):
        # self.top_val = 0
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

        size = len(self.queue)
        while size > 1:
            self.queue.appendleft(self.queue.pop())

            size -=1
    
        # self.top_val = x

    def pop(self) -> int:
        return self.queue.pop() # return the Topmost one


    def top(self) -> int:

        return self.queue[-1] # return queue front
        # return self.top_val
        

    def empty(self) -> bool:
        
        return len(self.queue)==0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()