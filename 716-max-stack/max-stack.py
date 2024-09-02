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

# Method II

# import heapq
# class MaxStack:

#     def __init__(self):
#         self.stack = []
#         self.heap = []
#         self.deleted_ids = set()
#         self.id = 0
        

#     def push(self, x: int) -> None:
#         self.stack.append(( x, self.id))
#         heapq.heappush(self.heap, (-x, -self.id))
#         self.id+=1

#     def pop(self) -> int:

#         # Hard Delete
#         while self.stack and self.stack[-1][1] in self.deleted_ids:
#             self.stack.pop()

#         val, idx = self.stack.pop()
#         self.deleted_ids.add(idx)
#         return val
        

#     def top(self) -> int:
#         # Hard Delete
#         while self.stack and self.stack[-1][1] in self.deleted_ids:
#             self.stack.pop()
#         return self.stack[-1][0] 

#     def peekMax(self) -> int:
#         # Hard Delete
#         while self.heap and -self.heap[0][1] in self.deleted_ids:
#             heapq.heappop(self.heap)
#         return -self.heap[0][0]

#     def popMax(self) -> int:
#         # Hard Delete
#         while self.heap and -self.heap[0][1] in self.deleted_ids:
#             heapq.heappop(self.heap)

#         val, idx = heapq.heappop(self.heap)
#         self.deleted_ids.add(-idx) # flip the idx 
#         return -val





# Method III - Doesn't Work
# import heapq
# class MaxStack:

#     def __init__(self):
#         self.stack = []
#         self.heap = []
        

#     def push(self, x: int) -> None:
      
#     #   print(x, self.stack, self.heap)
#       self.stack.append(x)
#       heapq.heappush(self.heap,-x)
      
#       heapq.heapify(self.heap)
#     #   print(x, self.stack, self.heap)

      

#     def pop(self) -> int:
#         val = self.stack.pop()
#         # print("Stack and Heap before Pop",self.stack, self.heap)   

#         for i in range(len(self.heap)-1, -1, -1):

#             if self.heap[i]*(-1)==val:
#                 # print(i, self.heap[i])
#                 del self.heap[i]
#                 break
            
#         # print("Pop: ", val)
#         return val

#         # if val == self.heap[0] * -1:
#         #     heapq.heappop(self.heap)
#         # return val

#     def top(self) -> int:
#         return self.stack[-1]
      
#     def peekMax(self) -> int:
#         # print(self.heap) 
#         return self.heap[0] * -1

#     def popMax(self) -> int:

#         val = self.heap[0] * -1 
#         heapq.heappop(self.heap)

#         for i in range(len(self.stack)-1, -1, -1):
#             if self.stack[i]==val:
#                 del self.stack[i]
#                 break

#         return val
        

        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()