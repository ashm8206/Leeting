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
            self._remove(node_remove)
            self._add(node_remove)
            # remove node
            # add node at end
           
            return node_remove.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            node_remove = self.map[key]
            node_remove.val = value
            self._remove(node_remove) # dangling now
            
        else:
            self.map[key] = Node(key, value) 
        
        node = self.map[key]
        # add the node at tail with updated value 
        self._add(node)

        if len(self.map) > self.capacity:
            node_remove = self.head.next
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