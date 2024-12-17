class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n = len(nums1)
        m = len(nums2)
        mid = 0
        mid2 = 0
        even = False

        if (n+m)%2==0:
            even = True
            mid2 = (n+m)//2
            mid = mid2 - 1
        else:
            mid = (n+m)//2
    

        minHeap = []
        
        for num in nums1:
            heappush(minHeap, num)
            
        
        for num in nums2:
            heappush(minHeap, num)
        
        

        for i in range(mid):
                heapq.heappop(minHeap)

        
        previous = heapq.heappop(minHeap)

        # print(previous)
        if even:
            nextNum = heapq.heappop(minHeap)
            # print(nextNum)
            ans = previous + nextNum
            ans = ans / 2
        else:
            ans = previous
        
        return ans

       
