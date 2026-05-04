class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        if key in self.map.keys():
            node_remove = self.map[key]
            self._remove(node_remove) # remove node
            self._add(node_remove)   #  add node at end
            return node_remove.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            node_remove = self.map[key] # remove
            node_remove.val = value   # overwrite value
            self._remove(node_remove) # prev, next None, dangling
        else:
            self.map[key] = Node(key, value) # prev, next None, dangling
        
        node = self.map[key] # safely access 
        self._add(node) # add end

        if len(self.map) > self.capacity:
            node_remove = self.head.next # if exceeds cap, add at begining
            self._remove(node_remove)
            del self.map[node_remove.key]
        
    def _remove(self, node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None
    
    def _add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)