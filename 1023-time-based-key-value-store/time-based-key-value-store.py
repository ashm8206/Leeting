class TimeMap:

    def __init__(self):
        self.keyMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            self.keyMap[key] =[(timestamp,value)]
        else:
            self.keyMap[key].append((timestamp,value))

        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.keyMap:
            return "" 
            # key not found

        # the smallest timestamp is greater than the one queried
        if self.keyMap[key][0][0] > timestamp:
            return "" 


        # idx = bisect.bisect_right(self.keyMap[key], [timestamp])

        left = 0
        right = len(self.keyMap[key])
        # right binsearch
        while left < right:
            mid = left + (right-left) // 2
            if self.keyMap[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        idx = left
        # idx = bisect.bisect_left(self.keyMap[key], [timestamp])
        # print(self.keyMap[key], timestamp)
        # print(idx)

        if idx < len(self.keyMap[key]) and self.keyMap[key][idx][0] == timestamp:
            # if [idx][0] == timestamp, 
            return self.keyMap[key][idx][1] 
        # if [idx][0] > timestamp, then return idx-1
        # if idx-1 < 0 , return empty
        
        return self.keyMap[key][idx-1][1] if idx - 1 >= 0 else ""
       
        # return self.keyMap[key][idx-1][1] if idx else ""
      

# Assumption: timestamp value will be strictly increasing

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

