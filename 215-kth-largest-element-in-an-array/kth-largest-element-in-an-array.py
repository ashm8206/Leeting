import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time Complexity O(nLogN)
        heap  = []

        for num in nums:
            heapq.heappush(heap,num)

            if len(heap)>k:
                heapq.heappop(heap)
        
        return heap[0]
        
        return pq[0]
        while k and pq:
           res = heapq.heappop(pq)
           k-=1
        return res


        # This is TLE: 

        # def qselect(nums, l, r, k):

        #     p = partition(nums,l, r)

        #     # print(nums[p],p, k)

        #     if p < k:
        #         return qselect(nums, p+1, r, k)
        #     if p > k:
        #         return qselect(nums, l, p-1, k)

        #     return nums[p]

        
        # def partition(nums,l, r):

        #     pivot = nums[r]

        #     new_idx = l
            
        #     for i in range(l, r):
        #         if nums[i] < pivot:
        #             nums[i], nums[new_idx] = nums[new_idx], nums[i]
        #             new_idx+=1

        #     nums[r], nums[new_idx] = nums[new_idx], nums[r]
        #     return new_idx

        
        # return qselect(nums, 0, len(nums)-1, len(nums)-k)
        



