from heapq import *
import heapq
class Solution:

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        
        # Time Complexity to remove an element from SortedList = O(logk)
        # Time Complexity to add an element into a SortedList = O(logk)
        sortedList = SortedList()
        
        i = 0
        n = len(nums)

        for j in range(n):
			# keep adding elements
            sortedList.add(nums[j])
            
            # if Window reached
            if j - i + 1 == k: 
				
                if k % 2 == 0: # even
                    medians.append((sortedList[k//2 - 1] + sortedList[k//2]) / 2)
				
                else: #odd
                    medians.append(sortedList[k//2])
                    
                # slide left ptr
                sortedList.remove(nums[i])
                i+=1

        return medians
#     def __init__(self):
#         self.maxheap, self.minheap = [], []
    
    
    
    # def rebalance(self, maxheap, minheap):
        
    #     if (len(maxheap) - len(minheap))==2:
    #          heappush(minheap, -heappop(maxheap))
                
    #     elif (len(maxheap) - len(minheap)) < 0:
    #         heappush(maxheap, -heappop(minheap))

            
    # def remove(self, heap, element):
        
    #     index = heap.index(element)
    #     heap[index] = heap[-1]
    #     del heap[-1]
        
    #     heapify(heap)
    #     # if index < len(heap):
    #     #     heapq._siftup(heap, index)
    #     #     heapq._siftdown(heap, 0, index)
            
    
    # def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    #     #Sliding window result is saved in [i-k+1]
    #     maxheap, minheap = [], []
    #     result = [0.0 for x in range(len(nums)-k + 1)] # number of windows
    #     for i in range(len(nums)):
            
    #         if not maxheap or nums[i] <= -maxheap[0]:
               
    #             heappush(maxheap, -nums[i])
    #         else:
    #             heappush(minheap, nums[i])
                
    #         self.rebalance(maxheap, minheap)
            
            
    #         if i-k+1 >=0: # first time we dont do anything, but after atleast k element 
    #                       # we remove one element every iteration and move sliding window
    #             if len(maxheap) == len(minheap):
                    
    #       # we have even number of elements, take the average of middle two elements
    #                 result[i - k + 1] = (-maxheap[0] / 2.0) + (minheap[0] / 2.0)
    #             else:  # because max-heap will have one more element than the min-heap
    #                 result[i - k + 1] = -maxheap[0] / 1.0

    #     # remove the element going out of the sliding window
                
    #             elementToBeRemoved = nums[i - k + 1]
    #             if elementToBeRemoved <= -maxheap[0]:
    #                 self.remove(maxheap, -elementToBeRemoved)
    #             else:
    #                 self.remove(minheap, elementToBeRemoved)

    #             self.rebalance(maxheap, minheap) # cuz we removed elements
    #     return result