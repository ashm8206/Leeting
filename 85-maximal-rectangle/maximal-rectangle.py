class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        #  Solve Largest hostorgam for every row

        # https://www.youtube.com/watch?v=tOylVCugy9k&themeRefresh=1


        if not matrix: return 0

        n, m = len(matrix), len(matrix[0])
        
        max_area = -2**31

        def largest_rec_hist(heights):
            # monotonic stack
            stack = []
            nonlocal max_area
            for curr_idx, h in enumerate(heights):
                start_idx = curr_idx
                while stack and stack[-1][1] > h:
                    old_idx, old_height = stack.pop()
                    max_area = max(max_area, old_height * (curr_idx - old_idx)) 
                    start_idx = old_idx # till wherever the previous could be extended
                stack.append((start_idx, h))
            if stack:
                for curr_idx, h in stack:
                     max_area = max(max_area, h * (m - curr_idx))
            return max_area



        dp = [0] * m
        
        for r in range(n):
            for c in range(m):
                
                # re-initialize to 0 if the matrix is 0, dont count
                dp[c] = dp[c] + 1 if matrix[r][c]=='1' else 0

            
            # Now Columns have heights, Call largest histogram func
            # print(dp) 
            max_area = max(max_area, largest_rec_hist(dp))
        return max_area
  
            
