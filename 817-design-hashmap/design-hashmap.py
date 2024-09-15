class Bucket():
    def __init__(self):
        self.bucketArray =[]

    def get(self,key):
        for (k,v) in self.bucketArray:
            if key == k:
                return v
        return -1

    def update(self,key,value):
        found = False
        for i, kv in enumerate(self.bucketArray):
            if key == kv[0]:
                found = True
                self.bucketArray[i] = (key,value)
                break
        if not found:
            self.bucketArray.append((key,value))

    def remove(self,key):
        for i, kv in enumerate(self.bucketArray):
            if key == kv[0]:
                del self.bucketArray[i]
                break
    
        
    

class MyHashMap:

    def __init__(self):
        self.keyRange = 2069
        self.hash_table = [ Bucket() for _ in range(self.keyRange)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.keyRange
        self.hash_table[hash_key].update(key,value)

    def get(self, key: int) -> int:
        hash_key = key % self.keyRange
        return self.hash_table[hash_key].get(key)
        

    def remove(self, key: int) -> None:
        hash_key = key % self.keyRange
        self.hash_table[hash_key].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)