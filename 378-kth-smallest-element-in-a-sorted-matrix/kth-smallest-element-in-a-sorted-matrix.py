class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

 
        m, n = len(matrix), len(matrix[0]) 

        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x: 
                    c -= 1  
                    # decrease column until matrix[r][c] <= x
                cnt += (c + 1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left < right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                # ans = mid
                # right = mid - 1  
                right = mid
                # try to looking for a smaller value in the left side
            else:
                left = mid + 1 
                 # try to looking for a bigger value in the right side
        return left


        # pq = []
        # n = len(matrix) # n*n

        # for row in range(n):
        #     heapq.heappush(pq,(matrix[row][0],(row,0)))
        
        # while pq:
        #     value, (nr, nc) = heapq.heappop(pq)

            
        #     k-=1
        #     if k == 0:
        #         return value

        #     if nc < n - 1:
        #         heapq.heappush(pq, (matrix[nr][nc+1], (nr, nc+1)))
            
                
        # return -1
        
        # pq = []
        # for row in matrix:
        #     for col in row:
        #         heapq.heappush(pq,-col)
        #         if pq and len(pq) > k:
        #             heapq.heappop(pq)
        
        # return -1 * heapq.heappop(pq)
        # while pq and k > 1:
        #     heapq.heappop(pq)
        #     k -=1
        
        # return heapq.heappop(pq)
