from collections import defaultdict
class StockPrice:

    def __init__(self):
        self.map = defaultdict(int)
        self.curr_timestamp = -1
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        #Map  TS -> Price
        self.map[timestamp] = price

        if timestamp > self.curr_timestamp:
            self.curr_timestamp = timestamp
        
       
     
        heapq.heappush(self.min_heap,(price, timestamp))
        heapq.heappush(self.max_heap,(-price, timestamp))

        

    def current(self) -> int:
        # value of get max TS
        return self.map[self.curr_timestamp]

    def maximum(self) -> int:

        price, timestamp = self.max_heap[0]

        # Pop pairs from heap with the price doesn't match with hashmap.
        while -price != self.map[timestamp]:
            heappop(self.max_heap)
            price, timestamp = self.max_heap[0]
        return -price

    def minimum(self) -> int:    
        price, timestamp = self.min_heap[0]

        # Pop pairs from heap with the price doesn't match with hashmap.
        while price != self.map[timestamp]:
            heappop(self.min_heap)
            price, timestamp = self.min_heap[0]
        return price

        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()