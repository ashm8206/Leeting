class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        #  Solve Largest hostorgam for every row

        # https://www.youtube.com/watch?v=tOylVCugy9k&themeRefresh=1


        if not matrix: return 0

        n, m = len(matrix), len(matrix[0])
        
        max_area = 0

        def largest_rec_hist(heights):
            #  Monotonotonically increasing stack
            maxAreaLocal = 0
            stack = []

            for i, h in enumerate(heights+[0]):
                
                while stack and heights[stack[-1]] >= h:
                    H = heights[stack.pop()]
                    # all elements inbetween
                    W = i if not stack else i - stack[-1] - 1

                    maxAreaLocal = max(maxAreaLocal, H*W)
                stack.append(i)

            return maxAreaLocal

        # this is Dp that builds on the previous
        dp = [0] * m 

        for r in range(n):
            # for every row
            for c in range(m):
                
                # re-initialize to 0 if the matrix is 0, dont count
                dp[c] = dp[c] + 1 if matrix[r][c]=='1' else 0

            # print(dp)
            # Now Columns have heights, Call largest histogram func
        
            max_area = max(max_area, largest_rec_hist(dp))
        return max_area
  
            
