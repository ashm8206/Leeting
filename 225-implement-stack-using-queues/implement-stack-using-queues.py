from collections import deque
class MyStack:
    # Neetcode with Top enhacement
    # https://www.youtube.com/watch?v=rW4vm0-DLYc
    def __init__(self):
        self.top_val = 0
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.top_val = x

    def pop(self) -> int:
        size = len(self.queue)
        while size > 1:
            
            val = self.queue.popleft() # pop front
            if size == 2:
                self.top_val = val
                
            self.queue.append(val)
            size -=1 
        return self.queue.popleft() # the Topmost one


    def top(self) -> int:

        return self.top_val
        

    def empty(self) -> bool:
        
        return len(self.queue)==0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()