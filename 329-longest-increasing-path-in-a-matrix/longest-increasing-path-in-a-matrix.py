class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Python Beginner Friendly https://leetcode.com/problems/longest-increasing-path-in-a-matrix/solutions/2052360/python-beginner-friendly-recursion-to-dp-intuition-explained/

        # Method I

        # m, n = len(matrix), len(matrix[0])
        
        # # create a dp array of size m * n to store already computed max_increasing_path_length for index (i, j)
        # # where 0 <= i < m and 0 <= j < n
        # # initialize the dp array by -1 as length of path can only be a whole number. 
        # dp = [[-1] * n for _ in range(m)]
        
        # def dfs(i, j, prev):
        #     if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
        #         return 0
            
        #     # if dp[i][j] != -1, that means dp[i][j] has been updated by some >= 0 path length.
        #     # hence directly use it without recomputing and save recursion time and space.
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     # compute if dp[i][j] = -1 meaning (i, j) still not computed
        #     left = dfs(i, j - 1, matrix[i][j])
        #     right = dfs(i, j + 1, matrix[i][j])
        #     top = dfs(i - 1, j, matrix[i][j])
        #     bottom = dfs(i + 1, j, matrix[i][j])
            
        #     # update the dp value after computing path length for index (i , j)
        #     # so that we can use it next time without recomputation.
        #     dp[i][j] = max(left, right, top, bottom) + 1
        #     return dp[i][j]
        
        # ans = -1
        # for i in range(m):
        #     for j in range(n):
        #         ans = max(ans, dfs(i, j, -1))
        # return ans

        #Topological Sort
        # https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

        m, n = len(matrix), len(matrix[0])
        indegree = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # modify indegre to outdeg instead
        for i in range(m):
            for j in range(n):
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        indegree[ni][nj] += 1
 
        # Start the topological sort with cells of zero indegree
        queue = deque([[x, y] for x in range(m) for y in range(n) if indegree[x][y] == 0])

        print(queue)

        max_inc_path = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0:
                            queue.append((ni, nj))
            max_inc_path += 1
        return max_inc_path
