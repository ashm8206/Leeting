from sortedcontainers import SortedList

# LinkedList / Array 

# Arrays
# get O(1)
# Fetch in O(n) as you gotta move N elements

# Doubly Linked, (Pop in the Middle),  Doubly works better as we need the pointer to the element before
# get O(n)
# fetch O(1)

# TreeSet, AVL Tree SortedList 
# What is AVL, How does Self-balancing Work
# log(n) < SQRT(N)
class MRUQueue:

    def __init__(self, n: int):
        self.q = SortedList([ (i, i) for i in range(1, n+1)])
       
        # Stored as Index, Value, sorted on Index

    def fetch(self, k: int) -> int:
        last_idx = self.q[-1][0]
        _ , value  = self.q.pop(k-1) # 1 indexed, make it 0
        self.q.add((last_idx+1, value))

        return value
        
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)