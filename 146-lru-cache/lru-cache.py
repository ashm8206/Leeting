class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.tail = Node(-1, -1)
        self.head = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node) # in LRU
        self.add(node) # # in LRU
        return node.val
        

    def put(self, key: int, value: int) -> None:

        # Remove old Node : Key
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        
        # ["LRUCache","put","put","put","put","get","get"]
        # [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

    
        node =  Node(key, value)
        self.dic[key] = node
        self.add(node)
        
        if len(self.dic) > self.capacity:
            lru_node = self.head.next
            lru_key = lru_node.key
            self.remove(lru_node)
            del self.dic[lru_key]
        # print([(v.key, v.val)for k, v in self.dic.items()])

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None
    
    def add(self, node):
       last_node = self.tail.prev
       last_node.next = node
       node.prev = last_node
       node.next = self.tail
       self.tail.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)