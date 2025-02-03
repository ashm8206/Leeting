class StatisticsTracker:

    def __init__(self):
        self.total = 0
        self.size = 0
        self.queue = deque()

        self.modeDict = Counter()
        self.sorted_list = SortedList()
        
        self.p_queue = []

    def addNumber(self, number: int) -> None:
        self.total += number
        self.size += 1
        self.queue.append(number)
        self.modeDict[number] += 1
        self.sorted_list.add(number)
        heappush(self.p_queue, (-self.modeDict[number], number))

    def removeFirstAddedNumber(self) -> None:
        num = self.queue.popleft()
        self.total -= num
        self.size -= 1
        self.modeDict[num] -= 1
        # if self.modeDict[num] == 0:
            # del self.modeDict[num]
        self.sorted_list.remove(num)

    def getMean(self) -> int:
        return self.total // self.size        

    def getMedian(self) -> int:
        return self.sorted_list[self.size // 2]

    def getMode(self) -> int:
        # maxCount =  - 1
        # maxNum = -1
        # for k, v in self.modeDict.items():
        #     if v > maxCount:
        #         maxCount = v
        #         maxNum = k
        #     elif v==maxCount:
        #         maxNum = min(maxNum, k)
        # return maxNum

        while self.p_queue and -self.p_queue[0][0] != self.modeDict[self.p_queue[0][1]]:
            heappop(self.p_queue)
        return self.p_queue[0][1]



# Your StatisticsTracker object will be instantiated and called as such:
# obj = StatisticsTracker()
# obj.addNumber(number)
# obj.removeFirstAddedNumber()
# param_3 = obj.getMean()
# param_4 = obj.getMedian()
# param_5 = obj.getMode()

# class StatisticsTracker:

#     def __init__(self):
#         self.d = deque()
#         self.s = SortedList()
#         self.freq = defaultdict(int)
#         self.biggestf = 0
        
#     def addNumber(self, number: int) -> None:
#         self.d.append(number)
#         self.freq[number] += 1
#         self.s.add(number)

#     def removeFirstAddedNumber(self) -> None:
#         if self.d:
#             a = self.d.popleft()
#             self.freq[a] -= 1
#             if self.freq[a] == 0:
#                 del self.freq[a]

#             if a in self.s:
#                 self.s.remove(a)
      
#     def getMean(self) -> int:
#         ans = floor(sum(self.d) // len(self.d))
#         return ans
        
#     def getMedian(self) -> int:
#         if len(self.s) % 2 == 0:
#             mid = len(self.s) // 2
#             return self.s[mid]
#         else:
#             mid = len(self.s) // 2 
#             if mid >= 0 and mid < len(self.s):
#                 return self.s[mid]
#             else:
#                 return self.s[0]
        
#     def getMode(self) -> int:
#         biggest = max(self.freq.values())
#         ans = float('inf')
#         for a, b in self.freq.items():
#             if b == biggest:
#                 ans = min(ans, a)
#         return ans
        


# Your StatisticsTracker object will be instantiated and called as such:
# obj = StatisticsTracker()
# obj.addNumber(number)
# obj.removeFirstAddedNumber()
# param_3 = obj.getMean()
# param_4 = obj.getMedian()
# param_5 = obj.getMode()

# Your StatisticsTracker object will be instantiated and called as such:
# obj = StatisticsTracker()
# obj.addNumber(number)
# obj.removeFirstAddedNumber()
# param_3 = obj.getMean()
# param_4 = obj.getMedian()
# param_5 = obj.getMode()
        


# Your StatisticsTracker object will be instantiated and called as such:
# obj = StatisticsTracker()
# obj.addNumber(number)
# obj.removeFirstAddedNumber()
# param_3 = obj.getMean()
# param_4 = obj.getMedian()
# param_5 = obj.getMode()