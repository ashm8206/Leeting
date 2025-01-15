import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        ans = [-10**6, 10**6]
        maxVal = -10**6

        pq = []
        n = len(nums)

        for i in range(n):
            heapq.heappush(pq, (nums[i][0], nums[i], 0)) #(val, list_idx, ele_idx)
            maxVal = max(maxVal,nums[i][0])
        
        while pq:
            minVal, row, eleIdx = heapq.heappop(pq)

            if abs(maxVal - minVal) < abs(ans[1] - ans[0]):
                ans = [minVal, maxVal]

            if eleIdx+1 == len(row):
                # reached end of list
                return ans
                # break

            heapq.heappush(pq, (row[eleIdx+1], row, eleIdx+1))
            maxVal = max(maxVal, row[eleIdx+1])
        return ans








        # # min_val = 2**31
        # max_val = -2**31

        # min_heap = []

        # for idx, el in enumerate(nums):
        #     heapq.heappush(min_heap, (el[0], 0, el)) # 1st col every row
        #     max_val = max(max_val,el[0])
        
        # ans = [-2**31, 2**31]

        # while min_heap:
        #     min_val, idx, row = heapq.heappop(min_heap)

        #     if max_val - min_val < ans[1] - ans[0]:
        #         ans = [min_val, max_val]
            
        #     if (idx + 1) == len(row):
        #         return ans
            
        #     heapq.heappush(min_heap, (row[idx+1], idx+1,row))
        #     max_val = max(max_val,row[idx+1])
        # return ans
