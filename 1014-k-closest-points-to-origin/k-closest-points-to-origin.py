import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # heap = []
        
        
        # for x, y in points:
        #     dist = x**2 + y**2

            
        #     heapq.heappush(heap,(dist*-1,[x,y]))
        #     #only after pushing we eject the smallest
        #     # as heap reorders
        #     if len(heap) > k:
        #         heapq.heappop(heap)
    
        # return [ls for _, ls in heap]

        nums = [(x**2 + y**2,[x,y]) for x,y in points]

        def partition(nums, l, r):

            pivot = nums[r]
            next_idx = l
            
            for i in range(l, r):
                if nums[i][0] < pivot[0]:
                    nums[i], nums[next_idx] = nums[next_idx], nums[i]
                    next_idx+=1
            nums[r], nums[next_idx] = nums[next_idx], nums[r]
            return next_idx
        
        def quickSelect(nums, l, r, k):

            if l==r:
                return l

            p = partition(nums, l, r)

            if p < k:
                return quickSelect(nums, p+1,r, k)
            elif p > k:
                return quickSelect(nums, l,p-1, k)
            else:
                return p

        if k == len(points):
            return points

        return [ ele[1] for ele in nums[:quickSelect(nums,0, len(nums)-1,k)]]

        
        
    
            
            