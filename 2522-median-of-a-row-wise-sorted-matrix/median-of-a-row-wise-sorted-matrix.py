class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        # https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/solutions/2507284/basic-practice-binary-search-in-general-paradigm-python/

        def getSmallerCount(grid, t):
            # leftmost binary search
            n = len(grid)
            m = len(grid[0])
            cnt = 0
            
            for r in range(n):
                # Find the position of the first element >= t
                # This is equivalent to C++'s lower_bound
                left, right = 0, m
                while left < right:
                    mid = (left + right) // 2
                    if grid[r][mid] >= t:
                        right = mid
                    else:
                        left = mid + 1
                cnt += left
            return cnt

        l = 1
        r = 10**6
        n = len(grid)
        m = len(grid[0])

        totalCnt = n * m 
        reqCnt = (totalCnt)//2
        
        while l < r:
            mid = (l + r + 1)//2
            smallerCount = getSmallerCount(grid, mid)
            if smallerCount<=reqCnt:
                l = mid
            else:
                r = mid - 1
        return r

