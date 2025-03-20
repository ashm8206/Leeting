from heapq import *
class MedianFinder:

    def __init__(self):
        self.arr = SortedList() 
        # Self-balancing Binary Search Trees (like an AVL Tree)
        # Multiset
        self.size = 0

    def addNum(self, num: int) -> None:
        self.arr.add(num)
        self.size+=1

    def findMedian(self) -> float:
        # n = len(self.arr)
        n = self.size
        if n % 2 == 1:
            return self.arr[n//2]
        return (self.arr[n//2] + self.arr[n//2-1]) / 2
    
    # https://leetcode.com/problems/find-median-from-data-stream/solutions/1330646/c-java-python-minheap-maxheap-solution-picture-explain-clean-concise/?envType=company&envId=facebook&favoriteSlug=facebook-six-months
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.maxheap = [] 
    #     # smaller than or equal to arbitary x, track largest number here
    #     # greater than x, track smallest number here             
    #     self.minheap = [] 
        

    # def addNum(self, num: int) -> None:
    #     # We partition the elements on the top of maxheap which is the apparent middle
    #     # We do this by maintaining two heaps of equal length or, maxheap having 1 more element than min_heap
        
    #     #partition logic
    #     if not self.maxheap or -self.maxheap[0] > num:
    #         heappush(self.maxheap, -num) # left Boundary
    #     else:
    #         heappush(self.minheap,num)
            
    #     # size adjusting logic
    #     if (len(self.maxheap) - len(self.minheap)) == 2: 
    #         # Max can have  + 1 than min, if it is +2 then  we shift
    #         heappush(self.minheap,-heappop(self.maxheap))
    #     elif (len(self.maxheap) - len(self.minheap)) < 0: # maxheap less elements than  min_heap
    #         heappush(self.maxheap,-heappop(self.minheap))

    # def findMedian(self) -> float:
        
    #     if len(self.maxheap) == len(self.minheap): # even
    #         return (-self.maxheap[0]/2.0) + (self.minheap[0]/2.0)
        
    #     return -self.maxheap[0] / 1.0 # odd, so lower number
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()